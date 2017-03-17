# 清理nginx代理缓存
> 清理ngx_proxy_cache 产生的缓存文件，因为我们在配置缓存目录的时候是根据请求目录来生成的所以有很多的缓存目录不能直接使用官方的例子清理

- 调用清理脚本
> 目录的*代表要清理目录下面所有缓存，绝对URL是清理文件
 
 <pre>
 python clear_ngx_cache.py xx.xx.com/fuck/*
 python clear_ngx_cache.py xxx.xx.com/fuck/a.html
 </pre>
