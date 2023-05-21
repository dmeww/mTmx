# 简介
## 模块名：定时更新Github Pages

## 实现过程
> 1. 在 Obsidian 使用 RemotelySave 插件 把笔记同步到 Onedrive 
> 2. 通过 Rclone 绑定 Onedrive 
> 3. 使用Python 实现一个定时任务
> 3.1 下载 Onedrive 中的笔记
> 3.2 删除上一次同步的笔记
> 3.3 使用Hexo清除上一次的生成的页面
> 3.4 使用Hexo的插件部署到 Github Pages
