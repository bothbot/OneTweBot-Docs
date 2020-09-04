
资源
#########

API列表
=============

本列表中各指令按模块划分和排序。

.. hint:: **API注记规则**


   ======================     ==========================     =====================================================
      注记                         说明                       用例
   ======================     ==========================     =====================================================
      ``<提示信息>``              此处应填入指定内容            ``!t <编号> <译文>`` 应填入 ``!t #1234 早上好``
      ``[可选内容]``              此处内容可以不填写            ``!反馈 <反馈标题>[ <反馈内容>]`` 写入 ``!反馈 有BUG 使用不了命令`` 与 ``!反馈 命令无效`` 均合法
   ======================     ==========================     =====================================================
   
.. hint:: **指令识别规则**

   * 指令前方的 ``!`` 为注记符，可以使用全角（中文）的 ``！`` 进行替换。
   * 指令前方的 ``#`` 做注记符时，不可以使用全角（日文）的 ``＃`` 进行替换。
   * 指令通常有多种表示形式，其功能完全相同。
   * 指令中通常使用空格作为分隔符，实际上可以使用回车换行进行分隔，与空格等价。

BOT管理命令
-------------

用户反馈
**********

.. admonition:: 插件：反馈

   本插件用于让用户向管理员提出消息反馈，以便项目维护和意见问题收集。



.. topic:: 信息反馈

   .. versionadded:: LTS

   +--------------+--------------------------------------+
   | 指令         | ``!反馈 <反馈标题>[ <反馈内容>]``    |
   |              +--------------------------------------+
   |              | ``!feedback <反馈标题>[ <反馈内容>]``|
   +--------------+--------------------------------------+
   | 权限         | 任何人                               | 
   +--------------+----------+---------------------------+
   | 参数         | 反馈标题 | 想要反馈的问题标题        | 
   |              +----------+---------------------------+
   |              | 反馈内容 | 想要反馈的问题内容        | 
   +--------------+----------+---------------------------+


.. topic:: 处理反馈

   .. versionadded:: LTS

.. topic:: 完成反馈

   .. versionadded:: v3

.. topic:: 反馈列表

   .. versionadded:: LTS


消息流管理
**********

.. admonition:: 插件：消息流管理

   本插件会对BOT的消息流进行管理，并支持打开/关闭/编辑消息流状态。

.. topic:: 查看指定消息流状态

   .. versionadded:: v3

.. topic:: 开启指定消息流

   .. versionadded:: v3

.. topic:: 关闭指定消息流

   .. versionadded:: v3

.. topic:: 查看消息流状态

   .. versionadded:: v3

.. topic:: 开启消息流

   .. versionadded:: v3

.. topic:: 关闭消息流

   .. versionadded:: v3

.. topic:: 获取消息流组标识

   .. versionadded:: v3

.. topic:: 消息流定向放行

   .. versionadded:: v3

.. topic:: 消息流定向阻止

   .. versionadded:: v3

.. topic:: 放行数据流

   .. versionadded:: v3

.. topic:: 阻止数据流

   .. versionadded:: v3


权限管理
**********

.. admonition:: 插件：权限管理

   本插件用于用户的权限管理，部分命令需要用户持有相应权限才可以触发使用。

.. hint:: **关于权限**

   除了权限管理、反馈管理等功能外，其他需要授权使用的各插件权限均独立。
   对于用户等级做以下划分：

      * 超级管理员
      * 群主/管理员
      * 普通用户

   插件在授权后，通常会有两个权限等级：

      * 插件管理员
      * 插件授权用户

   其中超级管理员与群主/管理员（私聊时视为管理员）会持有插件管理员对插件的使用权限；
   （群内群成员等）普通用户会持有插件授权用户的使用权限。

.. topic:: 合法权限组列表

   .. versionadded:: LTS

.. topic:: 合法权限列表

   .. versionadded:: LTS

.. topic:: 查看授权

   .. versionadded:: LTS

.. topic:: 远程授权

   .. versionadded:: v3

.. topic:: 远程取消授权

   .. versionadded:: v3

.. topic:: 远程禁用授权

   .. versionadded:: v3

.. topic:: 查询授权

   .. versionadded:: LTS



插件管理
*********

.. admonition:: 插件：插件管理

   本插件为内置插件管理，可通过远程和本地编辑全局和某一聊天内的插件启用状态。

.. topic:: 查看插件帮助信息

   .. versionadded:: v3

.. topic:: 全局禁用插件

   .. versionadded:: v3

.. topic:: 全局启用插件

   .. versionadded:: v3

.. topic:: 禁用插件

   .. versionadded:: v3

.. topic:: 启用插件

   .. versionadded:: v3

.. topic:: 查看插件列表

   .. versionadded:: LTS

推送命令
---------

推特推送
*********

.. admonition:: 插件：推特推送管理

   本插件基于推特开发者账号所使用的TwitterAPI进行推文获取和推送，可作为稳定的推特订阅途经。

.. topic:: 推特订阅授权

   .. versionadded:: LTS

.. topic:: 取消推特订阅授权

   .. versionadded:: LTS

.. topic:: 定向清空转推列表

   .. versionadded:: LTS

.. topic:: 定向清空转推对象

   .. versionadded:: LTS

.. topic:: 全局转推列表

   .. versionadded:: LTS

.. topic:: 添加辅助转推

   .. versionadded:: v3

.. topic:: 删除辅助转推

   .. versionadded:: v3

.. topic:: 查看辅助转推列表

   .. versionadded:: v3

.. topic:: 启动主监听

   .. versionadded:: v3

.. topic:: 关闭主监听

   .. versionadded:: v3

.. topic:: 启动辅助监听

   .. versionadded:: v3

.. topic:: 关闭辅助监听

   .. versionadded:: v3

.. topic:: 获取推文

   .. versionadded:: LTS

.. topic:: 推送优先级设置列表

   .. versionadded:: v3

.. topic:: 设置推送优先级

   .. versionadded:: v3

.. topic:: 查询推特用户

   .. versionadded:: LTS

.. topic:: 查看推文列表

   .. versionadded:: LTS

.. topic:: 添加推特账号订阅

   .. versionadded:: LTS

.. topic:: 删除推特账号订阅

   .. versionadded:: LTS

.. topic:: 查看当前账号订阅列表

   .. versionadded:: LTS

.. topic:: 清空当前账号订阅列表

   .. versionadded:: LTS

.. topic:: 查看转推设置列表

   .. versionadded:: LTS

.. topic:: 修改转推设置

   .. versionadded:: LTS

.. topic:: 转推单元设置

   .. versionadded:: v3

.. topic:: 转推单元设置列表

   .. versionadded:: v3

.. topic:: 压缩推特ID

   .. versionadded:: LTS

.. topic:: 解压推特ID

   .. versionadded:: LTS


RSS订阅
*********
.. admonition:: 插件：RSShub推送管理

   本插件基于RSSHub，支持一切合法RSS订阅。同时针对Bilibili直播/动态与推特时间线，支持直接使用主页/直播间地址进行订阅。

.. topic:: RSS订阅授权

   .. versionadded:: LTS

.. topic:: 取消RSS订阅授权

   .. versionadded:: LTS

.. topic:: 启动RSS监听

   .. versionadded:: LTS

.. topic:: 关闭RSS监听

   .. versionadded:: LTS

.. topic:: 设置RSS优先级

   .. versionadded:: v3

.. topic:: RSS优先级设置列表

   .. versionadded:: v3

.. topic:: 添加RSS订阅

   .. versionadded:: LTS

.. topic:: 取消RSS订阅

   .. versionadded:: LTS

.. topic:: 订阅源解码

   .. versionadded:: LTS

.. topic:: 查看订阅列表

   .. versionadded:: LTS

.. topic:: 清空订阅列表

   .. versionadded:: LTS

翻译命令
---------

推特翻译
************

.. admonition:: 插件：烤推

   本插件主要实现的功能是对推特推文的人工翻译自动嵌字，
   可通过消息中的文本生成含有翻译的图片，支持使用自定义
   的嵌字模板。

.. topic:: 推特翻译授权

   .. versionadded:: LTS


.. topic:: 取消推特翻译授权

   .. versionadded:: LTS


.. topic:: 设置烤推模板

   .. versionadded:: v3


.. topic:: 发起推特翻译

   .. versionadded:: LTS


.. topic:: 已翻译推特列表

   .. versionadded:: LTS


.. topic:: 获取最新推特翻译结果

   .. versionadded:: LTS

.. topic:: 获取指定推特翻译结果

   .. versionadded:: LTS

.. topic:: 显示推特翻译帮助信息

   .. versionadded:: LTS




机器翻译
*********
.. admonition:: 插件：翻译翻译

   本插件通过调用各翻译引擎的公开API进行机器翻译，用以为推文翻译提供参考。

.. warning:: **API限额**

   本插件所使用的API为免费版本的公开API，故存在翻译限额，使用时请节约流量。

.. topic:: 手动机器翻译

   .. versionadded:: v3


.. topic:: 启用流式翻译

   .. versionadded:: v3


.. topic:: 关闭流式翻译

   .. versionadded:: v3


.. topic:: 显示流式翻译列表

   .. versionadded:: v3


.. topic:: 清空流式翻译列表

   .. versionadded:: v3



其他功能
---------

内置的周边功能，欢迎使用BothBot协议进行个性化开发！

测试插件
*************

.. admonition:: 插件：插件例程

   本插件的示例插件。目前内置的示例可用于BOT收发测试的功能，主要目的为测试联通性。


.. topic:: 权限组测试

   .. versionadded:: v3

.. topic:: 固定回复测试

   .. versionadded:: v3

.. topic:: 图片传输测试

   .. versionadded:: v3
   
.. topic:: 随机回复测试

   .. versionadded:: LTS

.. topic:: 消息解析测试

   .. versionadded:: v3

.. topic:: 异常返回测试

   .. versionadded:: LTS


拓展资料阅读
=============

部分部署时需要的前置知识相关资料，在此罗列以供阅读。

* `构建服务器 <https://blog.csdn.net/ctrlxv/article/details/79054941>`_
* `Linux基础教程 <https://www.runoob.com/linux/linux-tutorial.html>`_
* `Go-CQHTTP <https://github.com/Mrs4s/go-cqhttp>`_
* `使用NGINX反向代理服务 <https://www.nginx.cn/doc/>`_
* `使用NOHUP挂载服务 <https://www.runoob.com/linux/linux-comm-nohup.html>`_
* `进程守护 <https://www.jianshu.com/p/e3f3d49093ca>`_