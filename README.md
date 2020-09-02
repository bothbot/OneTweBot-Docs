# Docs分支

**此分支为项目文档所在分支**

![](https://img.shields.io/badge/sphinx-4.0+-blue)

文档使用Python项目通用的[sphinx](https://www.sphinx-doc.org/en/master/index.html)进行部署和编写。基于Readthedocs提供的[sphinx_rtd_theme](https://github.com/rtfd/sphinx_rtd_theme)进行风格化构建。

目前使用Markdown和reStructuredText混编进行编写。

##### 计划中的特性

- 使用reStructuredText重构Markdown部分
- 进行SiteMap部署
- 添加中国大陆地区CDN

### 依赖

本文档citizen友好，因此请使用`git cz`代替`git commit`进行更新和同步。

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

```
sphinx-build -b html source static
```
编译静态页面至Static文件夹。

##### 编译并部署

使用
```
./make html
```
编译静态网页至`build/html`，可实现Push后自动更新部署至Readthedocs。

##### 生成PDF手册

由于未能解决图片问题（GitHub图床无法解析/Shield.io的Badge亦无法获取-Error403），因此暂时不支持生成。去除/解决图片问题（例如进行本地化存在`_static/`）后，方可正常生成。

*字体确定好像也有问题，现在能正常生成不过很丑*

```shell
./make pdf
```

*EPUB/LATEX亦可*

```
./make epub
./make latex
```

#### 本地服务

推荐使用Python内置提供的HTTP.SERVER进行本地环境启动。

```
# 进入静态网页根目录
cd static
# 在本地80端口启动服务
python -m http.server 80
```

#### 一键脚本

- 编译：`npm run build`
- 编译并开启80端口服务：`npm run serve`
- 提交本地仓库：`npm run done`
  *提交本地仓库将会自动`git add .`之后请求用户进行基于CZ格式化的Commit，编写完成后需要手动`git push`*