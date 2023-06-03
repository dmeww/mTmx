import os
import shutil
import fnmatch


def move_md_files_to_root(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, '*.md'):
            source = os.path.join(dirpath, filename)
            destination = os.path.join(root_dir, filename)
            shutil.move(source, destination)

def remove_non_md_files_and_directories(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            shutil.rmtree(os.path.join(dirpath, dirname))
        for filename in filenames:
            if not filename.endswith('.md'):
                os.remove(os.path.join(dirpath, filename))
            if filename == 'Template.md':
                os.remove(os.path.join(dirpath, filename))

def pre_option():
    # hexo_repo/source
    print('正在删除上一次部署的文件...')
    os.system('rm -rf /data/data/com.termux/files/home/hexo_repo/source/_posts')
    print('创建临时文件夹...')
    os.system('mkdir /data/data/com.termux/files/home/_posts')
    print('正在下载最新笔记...')
    os.system('rclone copy myone:应用/remotely-save/Obsidian /data/data/com.termux/files/home/_posts')


def append_option():
    print('正在把文件移动到目标目录...')
    os.system('mv /data/data/com.termux/files/home/_posts /data/data/com.termux/files/home/hexo_repo/source')
    print('正在部署博客...')
    os.system('cd /data/data/com.termux/files/home/hexo_repo && hexo clean && hexo deploy')
    print('部署完成，等待下一次部署')

def do_task():
    pre_option()
    print('正在整理笔记文件...')
    # root_dir = os.getcwd()+'/_posts'
    root_dir = '/data/data/com.termux/files/home/_posts'
    move_md_files_to_root(root_dir)
    remove_non_md_files_and_directories(root_dir)
    append_option()


