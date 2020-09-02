关于
#######

关于本项目
==========

版本动态
----------

目前主要维护两个版本:

* `v3 <https://github.com/chenxuan353/tweetToBot/tree/v3>`_
  活跃迭代更新的框架，目前重构自LTS版本，支持更多功能和自定义插件，能够和主流CQ框架进行适配。

* `LTS(Master) <https://github.com/chenxuan353/tweetToBot>`_
  稳定使用的框架，可以在CoolQ-CQHTTP框架下稳定运行，支持目前仍在维护的Go语言重构版本 `go-cqhttp <https://github.com/Mrs4s/go-cqhttp>`_。
  
  .. WARNING::
     由于众所周知的原因CoolQ已停止维护，因此目前更建议使用V3版本，本文档中全部命令均支持V3版本，部分不支持原有LTS版本。

项目进度&注意事项
------------------

支持多个bot远程连接此后端，已经对可能的冲突进行了处理。

目前推特的推送流异常后将尝试5次重启(重启前等待十秒)，五次重启均失败时需要手动重启。

对监听的修改将立刻保存至文件中。

已经保证了每个群就算是多个BOT同时存在也只会添加一个相同监听对象的推送。

现在配置文件读取后会以JSON的形式输出到日志中，如果丢失了配置文件，可以凭日志回档。

并且在退群时会自动卸载监听(需要bot在线)，配置异常时可以手动清除检测。

注记
--------------

* 接收推送的接口已经二次封装，只要事件符合推送事件处理器的数据格式，就可以正常推送。

* 为了保证推送的正常运行使用了多线程。

* 安装思源黑体CN之后可以修复字体问题。

基于本服务的扩展功能
---------------------

欢迎基于本通用代码框架进行其他插件的开发！

目前可以使用的仓库有：

* `OkayuTweetBot(分仓库) <https://github.com/OkayuDeveloper/OkayuTweetBot>`_: 使用旧Tweepy协议进行编写和获取推文，并实现部分娱乐插件。

联系我们
============

欢迎通过 `ISSUES <https://github.com/chenxuan353/tweetToBot/issues>`_ 向我们提交问题反馈和建议！

加入我们
==============

.. DANGER::
   快来817874522（大雾）

欢迎通过 `电子邮件 <mailto:1362941473@qq.com>`_ 联系我们！

.. HINT::
   如有需要可考虑开设售后群，届时请Feel Free在ISSUE中提出。

特别鸣谢
============

特别感谢 `richardchien <https://github.com/richardchien>`_ 和 `Mrs4s <https://github.com/Mrs4s>`_ 对CQHTTP的巨大贡献。

