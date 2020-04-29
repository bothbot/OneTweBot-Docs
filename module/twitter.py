# -*- coding: UTF-8 -*-
import string
import nonebot
import urllib
import traceback
import os
#引入配置
import config
#日志输出
from helper import data_read,data_save,log_print
#引入测试方法
test = None
try:
    import test
except:
    pass
'''
推送列表维护，及推送处理模版类定义
'''

PushList_config_name = 'PushListData.json'
base_tweet_id = config.base_tweet_id

#10进制转64进制
def encode_b64(n:int) -> str:
    table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ$_'
    result = []
    temp = n - 1253881609540800000
    if 0 == temp:
        result.append('0')
    else:
        while 0 < temp:
            result.append(table[int(temp) % 64])
            temp = int(temp)/64
    return ''.join([x for x in reversed(result)])
def decode_b64(str):
    table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                "6": 6, "7": 7, "8": 8, "9": 9,
                "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16,
                "h": 17, "i": 18, "j": 19, "k": 20, "l": 21, "m": 22, "n": 23,
                "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
                "v": 31, "w": 32, "x": 33, "y": 34, "z": 35,
                "A": 36, "B": 37, "C": 38, "D": 39, "E": 40, "F": 41, "G": 42,
                "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49,
                "O": 50, "P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56,
                "V": 57, "W": 58, "X": 59, "Y": 60, "Z": 61,
                "$": 62, "_": 63}
    result = 0
    for i in range(len(str)):
        result *= 64
        result += table[str[i]]
    return result + 1253881609540800000
#推送列表
class PushList:
    #映射推送关联(推送对象(type:str,ID:int)->推送单元)
    __push_list = {
        'private':{},
        'group':{}
    } 
    __spy_relate = {} #映射对象关联(监测ID(ID:int)->推送单元)
    spylist = [str(base_tweet_id)] #流监测列表
    
    #支持的消息类型
    message_type_list = ('private','group') 
    #推送单元允许编辑的配置_布尔类型
    Pushunit_allowEdit = (
        #携带图片发送
        'upimg',
        #消息模版
        'retweet_template','quoted_template','reply_to_status_template',
        'reply_to_user_template','none_template',
        #推特转发各类型开关
        'retweet','quoted','reply_to_status',
        'reply_to_user','none',
        #推特个人信息变动推送开关
        'change_ID','change_name','change_description',
        'change_headimgchange'
        )
    """
        推送列表-》推送列表、监测人信息关联表及监测人单的列表-》推送单元
        注：每个推送单元绑定一个推特用户ID以及一个推送对象(群或QQ)
        注：推送单元的配置由其推送对象全局配置以及自身DIY设置共同完成
    """
    #清空推送设置
    def clear(self):
        self.__push_list = {
            'private':{},
            'group':{}
        } 
        self.__spy_relate = {} #映射对象关联(监测ID(ID:int)->推送单元)
        self.spylist = [str(base_tweet_id)] #流监测列表
    #推送单元解包
    def getAllPushUnit(self) -> list:
        sourcedata = self.__spy_relate.copy()
        PushUnits = []
        for PushUnitList in sourcedata.values():
            for PushUnit in PushUnitList:
                PushUnits.append(PushUnit)
        return PushUnits
    def savePushList(self) -> tuple:
        PushUnits = self.getAllPushUnit()
        return data_save(PushList_config_name,PushUnits)
    def readPushList(self) -> tuple:
        data = data_read(PushList_config_name)
        if data[0] != False:
            self.clear()
            for PushUnit in data[2]:
                self.addPushunit(PushUnit)
            return (True,data[1])
        return data
    #打包成推送单元中(推送类型-群/私聊，推送对象-群号/Q号,绑定的推特用户ID,单元描述,绑定的酷Q账号,推送模版,各推送开关)
    def baleToPushUnit(self,bindCQID:int,
                        pushtype:str,
                        pushID:int,
                        tweet_user_id:int,
                        des:str,
                        nick:str='',**config):
        Pushunit = {}
        if not config:
            config = {}
        #固有属性
        Pushunit['bindCQID'] = bindCQID #绑定的酷Q帐号(正式上线时将使用此帐户进行发送，用于适配多酷Q账号)
        Pushunit['type'] = pushtype #group/private
        Pushunit['pushTo'] = pushID #QQ号或者群号
        Pushunit['tweet_user_id'] = tweet_user_id #监测ID
        Pushunit['nick'] = nick #推送昵称(默认推送昵称为推特screen_name)
        Pushunit['des'] = des #单元描述
        Pushunit['config'] = config
        return Pushunit
    #增加一个推送单元，返回状态元组(布尔型-是否成功,字符串-消息)
    def addPushunit(self,Pushunit) -> tuple:
        if Pushunit['pushTo'] in self.__push_list[Pushunit['type']]:
            if Pushunit['tweet_user_id'] in self.__push_list[Pushunit['type']][Pushunit['pushTo']]['pushunits']:
                return ( False, '推送单元已存在' )
        else:
            #初始化推送对象(推送全局属性)
            self.__push_list[Pushunit['type']][Pushunit['pushTo']] = {
                #为推送对象设置全局默认属性
                'Pushunitattr':config.pushunit_default_config.copy(),
                #推送单元组
                'pushunits':{}
            }
        #添加单元至推送列表
        self.__push_list[Pushunit['type']][Pushunit['pushTo']]['pushunits'][Pushunit['tweet_user_id']] = Pushunit
        #同步监测关联（内部同步了监测列表）
        if Pushunit['tweet_user_id'] not in self.__spy_relate:
            self.__spy_relate[Pushunit['tweet_user_id']] = []
            if str(Pushunit['tweet_user_id']) != base_tweet_id:
                self.spylist.append(str(Pushunit['tweet_user_id']))
        self.__spy_relate[Pushunit['tweet_user_id']].append(Pushunit)
        return ( True, '添加成功！' )
    #删除一个推送单元，没有返回值
    def delPushunit(self,Pushunit):
        #从推送列表中移除推送单元
        del self.__push_list[Pushunit['type']][Pushunit['pushTo']]['pushunits'][Pushunit['tweet_user_id']]
        #从监测列表中移除推送单元
        self.__spy_relate[Pushunit['tweet_user_id']].remove(Pushunit)
        #检查监测对象的推送单元是否为空，为空则移出监测列表
        if self.__spy_relate[Pushunit['tweet_user_id']] == []:
            del self.__spy_relate[Pushunit['tweet_user_id']]
            if str(Pushunit['tweet_user_id']) != base_tweet_id:
                self.spylist.remove(str(Pushunit['tweet_user_id']))
        #鲨掉自己
        del Pushunit
    #获取一个推送单元，返回状态列表(布尔型-是否成功,字符串-消息/Pushunit)
    def getPushunit(self,message_type:str,pushTo:int,tweet_user_id:int) -> list:
        if message_type not in self.message_type_list:
            raise Exception("无效的消息类型！",message_type)
        if pushTo not in self.__push_list[message_type]:
            return (False,'推送对象不存在！')
        if tweet_user_id not in self.__push_list[message_type][pushTo]['pushunits']:
            return (False,'推送单元不存在！')
        return (True,self.__push_list[message_type][pushTo]['pushunits'][tweet_user_id])

    #获取推送单元某个属性的值 返回值-(布尔型-是否成功,字符串-消息/属性内容)
    def getPuslunitAttr(self,Pushunit,key) -> tuple:
        if key in Pushunit['config']:
            return (True,Pushunit['config'][key])
        if key not in self.__push_list[Pushunit['type']][Pushunit['pushTo']]['Pushunitattr']:
            return (False,'不存在此属性')
        res = self.__push_list[Pushunit['type']][Pushunit['pushTo']]['Pushunitattr'][key]
        return (True,res)
    
    #返回监测对象关联的推送单元组,监测对象不存在时返回空列表[]
    def getLitsFromTweeUserID(self,tweet_user_id:int) -> list:
        if tweet_user_id not in self.__spy_relate:
            return []
        return self.__spy_relate[tweet_user_id].copy()
    #返回推送对象关联的推送单元组,推送对象不存在时返回空列表[]
    def getLitsFromPushTo(self,message_type:str,pushTo:int) -> list:
        if message_type not in self.message_type_list:
            raise Exception("无效的消息类型！",message_type)
        if pushTo not in self.__push_list[message_type]:
            return []
        dict_ = self.__push_list[message_type][pushTo]['pushunits']
        res = []
        for v in dict_.values():
            res.append(v)
        return res
    #返回推送对象关联的推送单元组-带ID,推送对象不存在时返回空列表[]
    def getLitsFromPushToAndID(self,message_type:str,pushTo:int) -> dict:
        if message_type not in self.message_type_list:
            raise Exception("无效的消息类型！",message_type)
        if pushTo not in self.__push_list[message_type]:
            return []
        return self.__push_list[message_type][pushTo]['pushunits']
    #返回推送对象关联的推送属性组,推送对象不存在时返回空字典{}
    def getAttrLitsFromPushTo(self,message_type:str,pushTo:int) -> dict:
        if message_type not in self.message_type_list:
            raise Exception("无效的消息类型！",message_type)
        if pushTo not in self.__push_list[message_type]:
            return {}
        return self.__push_list[message_type][pushTo]['Pushunitattr']

    #移除某个监测对象关联的所有推送单元,参数-推特用户ID 返回值-(布尔型-是否成功,字符串-消息)
    def delPushunitFromTweeUserID(self,tweet_user_id:int) -> tuple:
        if tweet_user_id not in self.__spy_relate:
            return (False,'此用户不在监测列表中！')
        table = self.getLitsFromTweeUserID(tweet_user_id)
        if table == []:
            return (True,'移除成功！')
        for Pushunit in table:
            self.delPushunit(Pushunit)
        return (True,'移除成功！')
    #移除某个推送对象关联的所有推送单元,参数-消息类型，对象ID，CQID 返回值-(布尔型-是否成功,字符串-消息)
    def delPushunitFromPushTo(self,message_type:str,pushTo:int,self_id:int = 0) -> tuple:
        if message_type not in self.message_type_list:
            raise Exception("无效的消息类型！",message_type)
        table = self.getLitsFromPushTo(message_type,pushTo)
        if table == []:
            return (True,'移除成功！')
        for Pushunit in table:
            if self_id == 0 or self_id == Pushunit['bindCQID']:
                self.delPushunit(Pushunit)
        return (True,'移除成功！')
    #移除某个推送单元,参数-消息类型，对象ID 返回值-(布尔型-是否成功,字符串-消息)
    def delPushunitFromPushToAndTweetUserID(self,message_type:str,pushTo:int,tweet_user_id:int) -> tuple:
        if message_type not in self.message_type_list:
            raise Exception("无效的消息类型！",message_type)
        if pushTo not in self.__push_list[message_type]:
            return (False,'推送对象不存在！')
        if tweet_user_id not in self.__push_list[message_type][pushTo]['pushunits']:
            return (False,'推送单元不存在！')
        self.delPushunit(self.__push_list[message_type][pushTo]['pushunits'][tweet_user_id])
        return (True,'移除成功！')

    #设置指定推送对象的全局属性
    def PushTo_setAttr(self,message_type:str,pushTo:int,key:str,value) -> tuple:
        if message_type not in self.message_type_list:
            raise Exception("无效的消息类型！",message_type)
        if key not in self.Pushunit_allowEdit:
            return (False,'指定属性不存在！')
        if pushTo not in self.__push_list[message_type]:
            return (False,'推送对象不存在！')
        self.__push_list[message_type][pushTo]['Pushunitattr'][key][value]
        return (True,'属性已更新')
    #设置指定推送单元的特定属性
    def setPushunitAttr(self,message_type:str,pushTo:int,tweet_user_id:int,key:str,value):
        if message_type not in self.message_type_list:
            raise Exception("无效的消息类型！",message_type)
        if key not in self.Pushunit_allowEdit:
            return (False,'指定属性不存在！')
        if pushTo not in self.__push_list[message_type]:
            return (False,'推送对象不存在！')
        if tweet_user_id not in self.__push_list[message_type][pushTo]['pushunits']:
            return (False,'推送单元不存在！')
        self.__push_list[message_type][pushTo]['pushunits'][tweet_user_id][key][value]
        return (True,'属性已更新')
#字符串模版
class tweetToStrTemplate(string.Template):
    delimiter = '$'
    idpattern = '[a-z]+_[a-z_]+'

class tweetEventDeal:
    #用户信息维护列表
    userinfolist = {}
    #检测个人信息更新
    def check_userinfo(self, userinfo):
        """
            运行数据比较
            用于监测用户的信息修改
            用户ID screen_name
            用户昵称 name
            描述 description
            头像 profile_image_url
        """
        """
            tweetinfo['user']['id'] = tweet.user.id
            tweetinfo['user']['id_str'] = tweet.user.id_str
            tweetinfo['user']['name'] = tweet.user.name
            tweetinfo['user']['description'] = tweet.user.description
            tweetinfo['user']['screen_name'] = tweet.user.screen_name
            tweetinfo['user']['profile_image_url'] = tweet.user.profile_image_url
            tweetinfo['user']['profile_image_url_https'] = tweet.user.profile_image_url_https
        """
        if userinfo['id'] in self.userinfolist:
            old_userinfo = self.userinfolist[userinfo['id']]
            data = {}
            str = ''
            if old_userinfo['name'] != userinfo['name']:
                data['type'] = 'change_name'
                str = old_userinfo['name'] + "(" + old_userinfo['screen_name'] + ")" + \
                ' 的昵称已更新为 ' + userinfo['name'] + "(" + userinfo['screen_name'] + ")"
                old_userinfo['name'] = userinfo['name']
            if old_userinfo['description'] != userinfo['description']:
                data['type'] = 'change_description'
                str = old_userinfo['name'] + "(" + old_userinfo['screen_name'] + ")" + ' 的描述已更新为 ' + userinfo['description']
                old_userinfo['description'] = userinfo['description']
            if old_userinfo['screen_name'] != userinfo['screen_name']:
                data['type'] = 'change_ID'
                str = old_userinfo['name'] + "(" + old_userinfo['screen_name'] + ")" + \
                    ' 的ID已更新为 ' + userinfo['name'] + "(" + userinfo['screen_name'] + ")"
                old_userinfo['screen_name'] = userinfo['screen_name']
            if old_userinfo['profile_image_url_https'] != userinfo['profile_image_url_https']:
                data['type'] = 'change_headimgchange'
                str = old_userinfo['name'] + "(" + old_userinfo['screen_name'] + ")" + '的头像已更新'
                old_userinfo['profile_image_url'] = userinfo['profile_image_url']
                old_userinfo['profile_image_url_https'] = userinfo['profile_image_url_https']

            if str != '':
                data['user_id'] = userinfo['id']
                data['user_id_str'] = userinfo['id_str']
                data['str'] = str
                eventunit = self.bale_event(data['type'],data['user_id'],data)
                self.deal_event(eventunit)
        else:
            if userinfo['id_str'] in push_list.spylist:
                self.userinfolist[userinfo['id']] = userinfo
    #打包事件(事件类型，引起变化的用户ID，事件数据)
    def bale_event(self, event_type,user_id:int,event_data):
        eventunit = {
            'type':event_type,
            'user_id':user_id,
            'data':event_data
        }
        return eventunit
    #事件预处理-发送事件
    def deal_event(self, event):
        table = push_list.getLitsFromTweeUserID(event['user_id'])
        if test:
            test.event_push(event)
        for Pushunit in table:
            #获取属性判断是否可以触发事件
            res = push_list.getPuslunitAttr(Pushunit,event['type'])
            if res[0] == False:
                raise Exception("获取Pushunit属性值失败",Pushunit)
            if res[1] == 1:
                self.deal_event_unit(event,Pushunit)
    def deal_event_unit(self,event,Pushunit):
        raise Exception('未定义事件处理单元')
    #推特标识到中文
    def type_to_str(self, tweettype):
        if tweettype == 'retweet':
            return '转推' #纯转推
        elif tweettype == 'quoted':
            return '转推并评论' #推特内含引用推文(带评论转推)
        elif tweettype == 'reply_to_status':
            return '回复' #回复(推特下评论)
        elif tweettype == 'reply_to_user':
            return '提及' #提及(猜测就是艾特)
        else:
            return '发推' #未分类(估计是主动发推)
    #将推特数据应用到模版
    def tweetToStr(self, tweetinfo, nick, upimg=config.pushunit_default_config['upimg'], template_text=''):
        if nick == '':
            if tweetinfo['user']['name']:
                nick = tweetinfo['user']['name']
            else:
                nick = tweetinfo['user']['screen_name']
        #模版变量初始化
        template_value = {
            'tweet_id':tweetinfo['id_str'], #推特ID
            'tweet_id_min':encode_b64(tweetinfo['id']),#压缩推特id
            'tweet_nick':nick, #操作人昵称
            'tweet_user_id':tweetinfo['user']['screen_name'], #操作人ID
            'tweet_text':tweetinfo['text'], #发送推特的完整内容
            'related_user_id':'', #关联用户ID
            'related_user_name':'', #关联用户昵称-昵称-昵称查询不到时为ID(被评论/被转发/被提及)
            'related_tweet_id':'', #关联推特ID(被评论/被转发)
            'related_tweet_id_min':'', #关联推特ID的压缩(被评论/被转发)
            'related_tweet_text':'', #关联推特内容(被转发或被转发并评论时存在)
        }
        if tweetinfo['type'] != 'none':
            template_value['related_tweet_id'] = tweetinfo['Related_tweet']['id_str']
            template_value['related_tweet_id_min'] = encode_b64(tweetinfo['Related_tweet']['id'])
            template_value['related_tweet_text'] = tweetinfo['Related_tweet']['text']

        if tweetinfo['type'] != 'none':
            template_value['related_user_id'] = tweetinfo['Related_user']['screen_name']
            if tweetinfo['Related_user']['id'] in self.userinfolist:
                template_value['related_user_name'] = self.userinfolist[tweetinfo['Related_user']['id']]['name']
            else:
                if hasattr(tweetinfo['Related_user'],'name'):
                    template_value['related_user_name'] = tweetinfo['Related_user']['name']
                else:
                    template_value['related_user_name'] = tweetinfo['Related_user']['screen_name']

        #生成模版类
        s = ""
        t = None
        if template_text == '':
            #默认模版
            if tweetinfo['type'] == 'none':
                deftemplate_none = "推特ID：$tweet_id_min，【$tweet_nick】发布了：\n$tweet_text"
                t = tweetToStrTemplate(deftemplate_none)
            elif tweetinfo['type'] == 'retweet':
                deftemplate_another = "推特ID：$tweet_id_min，【$tweet_nick】转了【$related_user_name】的推特：\n$tweet_text\n====================\n$related_tweet_text"
                t = tweetToStrTemplate(deftemplate_another)
            elif tweetinfo['type'] == 'quoted':
                deftemplate_another = "推特ID：$tweet_id_min，【$tweet_nick】转发并评论了【$related_user_name】的推特：\n$tweet_text\n====================\n$related_tweet_text"
                t = tweetToStrTemplate(deftemplate_another)
            else:
                deftemplate_another = "推特ID：$tweet_id_min，【$tweet_nick】回复了【$related_user_name】：\n$tweet_text"
                t = tweetToStrTemplate(deftemplate_another)
        else:
            #自定义模版
            t = tweetToStrTemplate(template_text)

        #转换为字符串
        s = t.safe_substitute(template_value)
        #组装图片
        if upimg == 1:
            s = s + "\n"
            if 'extended_entities' in tweetinfo:
                for media_unit in tweetinfo['extended_entities']:
                    #组装CQ码
                    file_suffix = os.path.splitext(media_unit['media_url'])[1]
                    s = s + '[CQ:image,file=tweet/' + media_unit['id_str'] + file_suffix + ']'
        return s
    #尝试从缓存中获取昵称
    def tryGetNick(self, tweet_user_id,nick):
        if tweet_user_id in self.userinfolist:
            return self.userinfolist[tweet_user_id]['name']
        return nick
    #尝试从缓存中获取用户信息,返回用户信息表
    def tryGetUserInfo(self, tweet_user_id) -> list:
        if tweet_user_id in self.userinfolist:
            return self.userinfolist[tweet_user_id]['name']
        return {}
    #消息发送(消息类型，消息发送到，消息内容)
    def send_msg(self, message_type:str, send_id:int, message:str,bindCQID:int = config.default_bot_QQ):
        bot = nonebot.get_bot()
        try:
            if message_type == 'private':
                bot.sync.send_msg_rate_limited(self_id=bindCQID,user_id=send_id,message=message)
            elif message_type == 'group':
                bot.sync.send_msg_rate_limited(self_id=bindCQID,group_id=send_id,message=message)
        except:
            s = traceback.format_exc(limit=5)
            log_print(2,s)
            pass
    #图片保存（待优化）
    def seve_image(self, name, url, file_path='img'):
        #保存图片到磁盘文件夹 cache/file_path中，默认为当前脚本运行目录下的 cache/img 文件夹
            base_path = 'cache/' #基准路径
            try:
                if not os.path.exists(base_path + file_path):
                    log_print(4,'文件夹' + base_path + file_path + '不存在，重新建立')
                    #os.mkdir(file_path)
                    os.makedirs(base_path + file_path)
                #获得图片后缀
                file_suffix = os.path.splitext(url)[1]
                #拼接图片名（包含路径）
                filename = '{}{}{}{}'.format(base_path + file_path,os.sep,name,file_suffix)
                #下载图片，并保存到文件夹中
                if not os.path.isfile(filename):
                    urllib.request.urlretrieve(url,filename=filename)
            except IOError:
                s = traceback.format_exc(limit=5)
                log_print(2,'文件操作失败'+s)
            except Exception:
                s = traceback.format_exc(limit=5)
                log_print(2,s)
#建立列表
push_list = PushList()


