# Django tutorial

## 视图层(View Layer)
### URL dispatcher  
干净、优雅的URL方案是高质量Web应用程序中的一个重要细节。Django允许您随意设计url，没有框架限制。  
查看万维网创始人Tim Berners-Lee撰写的[https://www.w3.org/Provider/Style/URI](https://www.w3.org/Provider/Style/URI)一文，了解关于为什么url应该是干净和可用的绝佳论据。   
#### 概述  
要为应用程序设计URL，需要创建一个Python模块，非正式地称为URLconf (URL配置)。这个模块是纯Python代码，是URL路径表达式到Python函数(您的视图)之间的映射。  

这个映射可以是短映射，也可以是长映射。它可以引用其他映射。而且，因为它是纯Python代码，所以可以动态构造它。  


Django还提供了一种根据活动语言翻译url的方法。有关更多信息，请参阅[https://docs.djangoproject.com/en/2.2/topics/i18n/translation/#url-internationalization](https://docs.djangoproject.com/en/2.2/topics/i18n/translation/#url-internationalization)国际化文档。  

#### Django如何处理请求  
当用户从您的django驱动的站点请求一个页面时，系统按照以下算法来确定要执行哪些Python代码:  
1. Django确定要使用的根URLconf模块。通常，这是ROOT_URLCONF设置的值，但是如果传入的HttpRequest对象具有urlconf属性(由中间件设置)，那么它的值将代替ROOT_URLCONF设置。  
2. Django加载该Python模块并查找变量urlpatterns。这应该是django.url .path()和/或django.url .re_path()实例的Python列表。  
3. Django按顺序运行每个URL模式，并在第一个匹配请求URL的模式处停止。  
4. 一旦其中一个URL模式匹配，Django就导入并调用给定的视图，这是一个简单的Python函数(或基于类的视图)。视图通过以下参数传递:  
- HttpRequest的一个实例.  
- 如果匹配的URL模式没有返回命名组，那么正则表达式中的匹配将作为位置参数提供。  
- 关键字参数由路径表达式匹配的任何命名部分组成，由django.url .path()或django.url .re_path()的可选 kwargs参数中指定的任何参数覆盖。  
5. 如果没有匹配的URL模式，或者在此过程的任何时刻引发异常，Django将调用一个适当的错误处理视图。参见下面的错误[https://docs.djangoproject.com/en/2.2/topics/http/urls/#error-handling](https://docs.djangoproject.com/en/2.2/topics/http/urls/#error-handling)处理。