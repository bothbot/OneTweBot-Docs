# OneTweBot用户文档

![NONEBOT](https://img.shields.io/static/v1?label=Nonebot&message=1.7.0&color=green&style=flat-square&link=https://github.com/nonebot/nonebot)&nbsp;![PYTHON3.7](https://img.shields.io/static/v1?label=Python&message=3.7&color=blue&style=flat-square&link=https://www.python.org/)&nbsp;![MIT](https://img.shields.io/static/v1?label=LICENSE&message=MIT&color=red&style=flat-square&link=https://github.com/chenxuan353/tweetToBot/blob/v3/LICENSE)&nbsp;![CQHTTP-MIRAI](https://img.shields.io/static/v1?label=cqhttp-mirai&message=0.2.3&color=9cf&style=flat-square&link=https://github.com/yyuueexxiinngg/cqhttp-mirai)&nbsp;![MIRAI](https://img.shields.io/static/v1?label=Mirai&message=1.2.2&color=9cf&style=flat-square&link=https://github.com/mamoe/mirai)&nbsp;![AIOCQHTTP](https://img.shields.io/static/v1?label=CQHTTP&message=4.8&color=brightgreen&style=flat-square&link=https://github.com/nonebot/aiocqhttp)&nbsp;![GO-CQHTTP](https://img.shields.io/static/v1?label=go-cqhttp&message=stable&color=brightgreen&style=flat-square&link=https://github.com/Mrs4s/go-cqhttp)&nbsp;![SPHINX](https://img.shields.io/static/v1?label=sphinx&message=4.0&color=blue&style=flat-square&link=https://www.sphinx-doc.org/en/master)&nbsp;![COMMITIZEN](https://img.shields.io/static/v1?label=commitzen&message=friendly&color=brightgreen&style=flat-square&link=http://commitizen.github.io/cz-cli/)

#### [用户文档](https://bothbot-documentation.readthedocs.io/)

**此分支为OneTweBot项目文档仓库** 
项目主仓库目前位于[tweetToBot](https://github.com/chenxuan353/tweetToBot)

文档使用Python项目通用的[sphinx](https://www.sphinx-doc.org/en/master/index.html)进行部署和编写。基于Readthedocs提供的[sphinx_rtd_theme](https://github.com/rtfd/sphinx_rtd_theme)进行风格化构建。

目前使用Markdown和reStructuredText混编进行编写。

##### 计划中的特性

- 使用reStructuredText重构Markdown部分
- 进行SiteMap部署
- 添加中国大陆地区CDN

### 依赖

本文档commitizen友好，因此请使用`git cz`代替`git commit`进行更新和同步。

关于本地服务依赖，请在根目录使用

```shell
pip install -r requirement.txt && npm install commitizen -g && npm i
```

进行一键安装。

### 使用

#### 编写

使用Markdown或reST修改`source/`中的对应文档，其中index.rst为文档入口（首页），各文档均会打包生成为`.html`文件。

##### 动态编写

可在VSCode中使用**reStructuredText**扩展进行动态编写。

#### 编译

使用

```shell
sphinx-build -b html source static
```
编译静态页面至Static文件夹。

##### 编译并部署

使用

```shell
./make html
```

编译静态网页至`build/html`，可实现Push后自动更新部署至Readthedocs。

##### 生成PDF手册

*本地生成PDF时中文字体似乎问题，请使用ReadTheDocs托管处生成的PDF*

```shell
./make latexpdf
```

*EPUB/LATEX亦可*

```shell
./make epub
./make latex
```

#### 本地服务

推荐使用Python内置提供的HTTP.SERVER进行本地环境启动。

```shell
# 进入静态网页根目录
cd static
# 在本地80端口启动服务
python -m http.server 80
```

#### 一键脚本

- 编译：`npm run build`
- 编译并开启80端口服务：`npm run serve`
- 提交本地仓库：`npm run done`
  须安装git-cz

  ```shell
  npm i -g git-cz
  ```

  *提交本地仓库将会自动`git add .`之后请求用户进行基于CZ格式化的Commit，编写完成后需要手动`git push`*
