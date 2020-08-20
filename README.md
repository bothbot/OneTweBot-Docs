# Docs分支

**此分支为项目文档所在分支 此文档通过Hexo部署。**

### 文档维护(文档维护者请参见，仅部署后端可忽略)

#### 依赖

本文档网站搭建使用[HEXO](https://hexo.io/)，当前页面搭建基于[NodeJS LTS](https://nodejs.org/en/download/)请安装Node.js 12以搭建开发环境。

#### 环境配置

##### 全局HEXO

推荐在全局安装HEXO以搭建其他页面

```
node i -g hexo
```

##### Plugins

进入`/docs`文件夹，在Shell内运行

```shell
npm i
```

安装依赖，并安装Git插件

```shell
npm i hexo-deployer-git --save
```

#### 使用

##### 添加新文档

```Shell
hexo new "<标题(建议英文)>"
```

或直接在`source/_post/`内添加Markdown文档(须仿照其他文档设置抬头)

##### 修改文档

略

##### 编译

hexo文档项目使用

```mermaid
graph LR;

A[本地编辑] --> B[本地编译]
B --> C[本地预览]
E[清理当前项目] --> B
B --> D[部署到GitHub页面]
C --> D
A --> E

```

的模式，故编译时建议先**清理本地静态页面**

```shell
npm run clean
```

或

```shell
hexo clean
```

然后进行**编译生成**

```shell
npm run generate
```

##### 部署

最后部署到GitHub

```shell
npm run deploy
```

之后网页便会自动Push到仓库的`gh-pages`分支，并自动部署到服务器。