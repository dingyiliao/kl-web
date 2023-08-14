import scrapy


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['']
    custom_settings = {
        'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        },
        'Spider.pipelines.SQLitePipeline': 400
    }

    def start_requests(self):
        return super().start_requests()
    
    def parse(self, response, **kwargs):
        return super().parse(response, **kwargs)
