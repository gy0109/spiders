""""""

"""
scrapy的概念：Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架


scrapy框架的运行流程以及数据传递过程：
调度器把requests-->引擎-->下载中间件--->下载器
下载器发送请求，获取响应---->下载中间件---->引擎--->爬虫中间件--->爬虫
爬虫提取url地址，组装成request对象---->爬虫中间件--->引擎--->调度器
爬虫提取数据--->引擎--->管道
管道进行数据的处理和保存


scrapy框架的作用：通过少量代码实现快速抓取


掌握scrapy中每个模块的作用： 

引擎(engine)：负责数据和信号在不腰痛模块间的传递 
调度器(scheduler)：实现一个队列，存放引擎发过来的request请求对象 
下载器(downloader)：发送引擎发过来的request请求，获取响应，并将响应交给引擎 
爬虫(spider)：处理引擎发过来的response，提取数据，提取url，并交给引擎 
管道(pipeline)：处理引擎传递过来的数据，比如存储 
下载中间件(downloader middleware)：可以自定义的下载扩展，比如设置代理ip 
爬虫中间件(spider middleware)：可以自定义request请求和进行response过滤


理解异步和非阻塞的区别：异步是过程，非阻塞是状态

"""