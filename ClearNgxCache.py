#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys, os

try:
    from hashlib import md5
except:
    from md5 import md5


class ClearNgxCache:
    # 服务器缓存根目录
    cachedir = "/data/ngx_cache/"

    # url值
    url = ""

    # url的目录数组
    paths = [];

    # url的md5值
    urlmd5 = ""

    # 多级URL目录
    mutil_paths = ["/fuck/l/"]

    # 根域名缓存目录
    cache_index = "index"

    # 初始化
    def __init__(self, url):
        self.url = url
        self.paths = str(url).split("/")
        self.url_md5()

    # 清理目录
    def clear_dir(self, dirname):
        cache_dir = ("%s%s" % (self.cachedir, dirname))
        if os.path.exists(cache_dir):
            print("find %s/*|xargs rm -rf" % (cache_dir))
            # 使用系统命令清理效率会高很多
            os.system("find %s%s/*|xargs rm -rf" % (self.cachedir, dirname))

    # 清理文件
    def clear_file(self, filePath):
        print(filePath)
        if os.path.exists(filePath):
            os.remove(filePath)
            print 'delete success'
        else:
            print 'file not find'

    # 获取url的md5值
    def url_md5(self):
        m = md5()
        m.update("%s" % self.url)
        self.urlmd5 = m.hexdigest()

    # 清理文件缓存，需要传入缓存目录
    def process_file(self, dirname):
        md5urllen = len(self.urlmd5)
        dir1 = self.urlmd5[md5urllen - 1:]
        dir2 = self.urlmd5[md5urllen - 3:md5urllen - 1]
        dir3 = self.urlmd5[md5urllen - 5:md5urllen - 3]
        dirPath = ("%s%s/%s/%s/%s/%s" % (self.cachedir, dirname, dir1, dir2, dir3, self.urlmd5))
        self.clear_file(dirPath)

    # 清理目录
    def clear_ngx_cache(self):
        dirname = self.paths[1]
        for path in self.mutil_paths:
            if str(self.url).find(path) != -1:
                dirname = path[1:len(path) - 1].replace("/", "-")
                break

        # 获取清理目录的标识符
        url_root_path = self.paths[len(self.paths) - 1]

        # 整站清理及首页
        if len(self.paths) == 2:
            if url_root_path == "*":
                self.clear_dir("")
            else:
                self.process_file(self.cache_index)
        else:
            # 清理目录
            if url_root_path == "*":
                self.clear_dir(dirname)
            else:
                self.process_file(dirname)


clearNgxCache = ClearNgxCache(sys.argv[1])
clearNgxCache.clear_ngx_cache()

