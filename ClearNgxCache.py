#!/usr/bin/python
# -*- coding:utf8 -*-

import os

try:
    from hashlib import md5
except:
    from md5 import md5


class ClearNgxCache:
    cache_root_dir = "/data/xxx/"
    cache_temp_dir = "/data/xxx/"
    multi_cache_dir = ["/news/detail/"]
    url = None
    clear_dir_cmd = "mv -o %s %s"
    clear_file_cmd = "rm -rf %s"

    def __init__(self, url):
        self.url = url

    def clear_cache(self):
        if self.url is None or str(self.url).find("http://") != -1:
            print("URL为空或者添加请求协议(http|https)")
            exit(0)
        # 整站清理
        self.clear_total_file()
        # 缓存root目录
        cache_dir = None
        # 多级目录处理
        if not (self.multi_cache_dir is None) and len(self.multi_cache_dir) != -1:
            for temp_cache_dir in self.multi_cache_dir:
                if str(self.url).find(temp_cache_dir) != -1:
                    cache_dir = self.cache_root_dir + str(temp_cache_dir).strip("/").replace("/", "-")
        # 检查要清理缓存类型
        clear_type = self.check_cache_type()
        # 如果类型是目录以及是多路径的直接删除
        if not (cache_dir is None) and clear_type == "dir":
            self.clear_dir(cache_dir)
            exit(0)

        # 获取URL的md5值
        cache_dir = self.process_file(cache_dir, clear_type)
        # 根据类型清理缓存
        if clear_type == "dir":
            self.clear_dir(cache_dir)
            exit(0)
        elif clear_type == "file":
            self.clear_file(cache_dir)
            exit(0)
        print("没有匹配到要清理的文件缓存")

    # 整站清理
    def clear_total_file(self):
        url = str(self.url)
        if len(url.split("/")) == 1 and url[len(url) - 1] == "*":
            self.clear_dir(self.cache_root_dir)

    # 清理文件
    def clear_file(self, cache_file):
        if cache_file is None:
            print("清理文件不能为空")
            exit(0)
        if os.path.exists(cache_file) is False:
            print("清理文件不存在")
            exit(0)
        temp_clear_cmd = self.clear_file_cmd % cache_file
        print("清理命令:%s" % temp_clear_cmd)
        # os.popen(temp_clear_cmd)

    # 清理目录
    def clear_dir(self, cache_dir):
        if cache_dir is None:
            print("清理目录不能为空")
            exit(0)
        if os.path.exists(cache_dir) is False:
            print("清理目录不存在")
            exit(0)
        temp_clear_cmd = self.clear_dir_cmd % (cache_dir + "/*", self.cache_temp_dir)
        print("清理命令:%s" % temp_clear_cmd)
        # os.popen(temp_clear_cmd)

    # 检查清理类型 目录|文件
    def check_cache_type(self):
        url_flag = self.url[len(self.url) - 1]
        if url_flag == "*":
            return "dir"
        else:
            return "file"

    # 清理文件缓存，需要传入缓存目录
    def process_file(self, cache_dir, clear_type):
        if clear_type is None:
            print("清理类型不能为空")
            exit(0)
        m = md5()
        m.update("%s" % self.url)
        url_md5 = m.hexdigest()
        md5_url_len = len(url_md5)
        dir1 = url_md5[md5_url_len - 1:]
        dir2 = url_md5[md5_url_len - 3:md5_url_len - 1]
        dir3 = url_md5[md5_url_len - 5:md5_url_len - 3]
        if clear_type == "dir":
            return "%s%s/%s/%s" % (self.cache_root_dir, dir1, dir2, dir3)
        if clear_type == "file":
            temp_cache_dir = self.cache_root_dir
            if not (cache_dir is None):
                temp_cache_dir = cache_dir + "/"
            return "%s%s/%s/%s/%s" % (temp_cache_dir, dir1, dir2, dir3, url_md5)
        return None


clearNgxCache = ClearNgxCache("m.maiche.com/news/detail/a.html")
clearNgxCache.clear_cache()
