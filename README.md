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
pip install -r requirement.txt && npm i
```

进行一键安装。

### 使用

#### 编写

使用Markdown或reST修改`source/`中的对应文档，其中index.rst为文档入口（首页），各文档均会打包生成为`.html`文件。

###### 动态编写

可在VSCode中使用**reStructuredText**扩展进行动态编写。

#### 编译

使用

```
sphinx-build -b html source build
```
编译静态页面。

#### 本地服务

推荐使用Python内置提供的HTTP.SERVER进行本地环境启动。

```
# 进入静态网页根目录
cd build
# 在本地80端口启动服务
python -m http.server 80
```

#### 一键脚本

- 编译：`npm run build`
- 编译并开启80端口服务：`npm run serve`
- 提交本地仓库：`npm run done`
  *提交本地仓库将会自动`git add .`之后请求用户进行基于CZ格式化的Commit*