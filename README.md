# 清理Ngx文件缓存

> 清理ngx_proxy_cache 产生的缓存文件，因为我们在配置缓存目录的时候是根据请求目录来生成的，所以有很多的缓存目录不能直接使用官方的例子清理，
> 官方的purge模块只有ee版本才能使用，ce的不能使用所以自己写一个简历的快递清理文件及目录

# 参数说明

* cache_root_dir: 放置文件缓存根目录
* cache_temp_dir: 删除目录时会把被删除目录临时放到这个目录
* multi_cache_dir: 有多级目录时需要配置，例: /n/b/  缓存目录为n-b时需要配置
* url: 需要清理的url，url不能添加请求协议头，如果添加再调用脚本时会结束脚本运行
* clear_index_dir: 所有xxx.xx.cn|com 缓存默认存入此目录

# 定时清理缓存

在清理目录时会将清理目录所有文件mv 到临时目录,目录文件还是存在所以需要定时任务去清理临时文件
可以使用系统级的crontab，也可以使用python的定时器

# 调用清理脚本

目录的*代表要清理目录下面所有缓存，绝对URL是清理文件，例:

```
 python clear_ngx_cache.py xx.xx.com/fuck/* # 清理目录
 python clear_ngx_cache.py xxx.xx.com/fuck/a.html #清理文件
 python clear_ngx_cache.py xxx.xx.com/* #清理整站
 python clear_ngx_cache.py xxx.xx.com/index.html #清理index.html
 python clear_ngx_cache.py xxx.xx.com/ #清理index目录
 ```

# 运行要求

python 版本要求 2.6+
