# -*- coding: utf-8 -*-
import scrapy
from xigua.items import XiguaItem
import re
import logging


class XgSpider(scrapy.Spider):
    name = 'xg'
    allowed_domains = ['editor.xiguaji.com']

    logging.getLogger("requests").setLevel(logging.WARNING
                                           )  # 将requests的日志级别设成WARNING

    logging.basicConfig(
        level=logging.DEBUG,
        format=
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='xigua.log',
        filemode='w')

    def start_requests(self):
        for tag in [1, 2, 7, 8, 9, 10, 11, 13, 14, 16, 17, 18, 19]:
            for p in range(1, 2):
                yield scrapy.Request(
                    url="http://editor.xiguaji.com/Templet?partial=1&tagIds={number}&page={page}".format(number=tag,
                                                                                                         page=p),
                    callback=self.parse, meta={"type": tag})

    def parse(self, response):
        item = XiguaItem()
        imgs = re.findall(r'src="(.*?)"', str(response.body))
        for img in imgs:
            item["img_url"] = img
            item["img_type"] = self.check(int(response.meta["type"]))
            yield item

    def check(self, img_type):
        if img_type == 1:
            return "美文"
        elif img_type == 2:
            return "美食"
        elif img_type == 7:
            return "教育"
        elif img_type == 8:
            return "健康"
        elif img_type == 9:
            return "职场"
        elif img_type == 10:
            return "党政"
        elif img_type == 11:
            return "法律"
        elif img_type == 13:
            return "传统"
        elif img_type == 14:
            return "校园"
        elif img_type == 16:
            return "资讯"
        elif img_type == 17:
            return "旅游"
        elif img_type == 18:
            return "电商"
        else:
            return "母婴"
