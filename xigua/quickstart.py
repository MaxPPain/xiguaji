from scrapy import cmdline

# cmdline.execute("scrapy crawl xg".split())
cmdline.execute("scrapy crawl xg -o test.json -t json".split())
