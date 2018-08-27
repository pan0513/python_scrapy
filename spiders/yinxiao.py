# -*- coding: utf-8 -*-
import scrapy
import os
from ibaotu_yinxiao.items import IbaotuYinxiaoItem


class YinxiaoSpider(scrapy.Spider):
    name = 'yinxiao'
    allowed_domains = ['ibaotu.com']
    page = 1;
    url = "https://ibaotu.com/yinxiao/10-0-0-91529-0-"
    start_urls = [url + str(page) + ".html"]

    def parse(self, response):
        print 'parse'
        for each in response.xpath("//div[@class='content-index clearfix']"):
            print '#########################################################'
            print each.xpath(".//img[@class='scrollLoading']/@data-url").extract()[0]
            print each.xpath(".//img[@class='scrollLoading']/@alt").extract()[0]
            print each.xpath("./div[@class='audio-info']/span/text()").extract()[0]
            print each.xpath("./div[@class='audio-box clearfix']/audio/source/@src").extract()[0]
            print each.xpath("./div[@class='audio-box clearfix']/span/text()").extract()[0]
            # 初始化模型对象
            item = IbaotuYinxiaoItem()
            # 职位名称
            item['type'] = 'animal'
            # 详情连接
            item['img'] = each.xpath(".//img[@class='scrollLoading']/@data-url").extract()[0]
            # 职位类别
            item['title'] = each.xpath(".//img[@class='scrollLoading']/@alt").extract()[0]
            # 招聘人数
            item['ext'] = each.xpath("./div[@class='audio-info']/span/text()").extract()[0]
            # 工作地点
            item['url'] = each.xpath("./div[@class='audio-box clearfix']/audio/source/@src").extract()[0]
            # 发布时间
            item['time'] = each.xpath("./div[@class='audio-box clearfix']/span/text()").extract()[0]

            # 下载详情图片
            yield scrapy.Request(url='http:' + item['img'], callback=self.downloadImg, meta={'data': item})
            # 下载音效文件
            yield scrapy.Request(url='http:' + item['url'], callback=self.downloadFile, meta={'data': item})
            yield item



        if self.page < 32:
            self.page += 1

            # 每次处理完一页的数据之后，重新发送下一页页面请求
            # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.page) + ".html", callback=self.parse)

    def downloadImg(self, response):
        item = response.meta['data']
        print item
        root_dir = 'yinxiao_img'
        if not os.path.exists(root_dir):
            os.mkdir(root_dir)

        paths =  response.url.split('/')[-1]
        filename = root_dir + '/' + paths

        with open(filename, 'wb') as f:
            f.write(response.body)
            item['img_path'] = paths
        f.close()
        yield item

    def downloadFile(self, response):
        item = response.meta['data']
        print item
        root_dir = 'yinxiao_file'
        if not os.path.exists(root_dir):
            os.mkdir(root_dir)

        paths = response.url.split('/')[-1]
        filename = root_dir + '/' + paths

        with open(filename, 'wb') as f:
            f.write(response.body)
            item['file_path'] = paths
        f.close()
        yield item