# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IbaotuYinxiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 类别
    type = scrapy.Field()
    # 图片名称
    img = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 文件后缀
    ext = scrapy.Field()
    # 源下载地址
    url = scrapy.Field()
    # 时长
    time = scrapy.Field()
    # 时长
    img_path = scrapy.Field()
    # 时长
    file_path = scrapy.Field()