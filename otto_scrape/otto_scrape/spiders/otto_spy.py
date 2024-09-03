import scrapy
from scrapy_playwright.page import PageMethod
from otto_scrape.items import Product

#keywords = [bademantel, bettwäsche, pouf, bodenkissen, memory foam kissen, sitzkissen, nackenkissen, teppich, kuscheldecke]

class OttoSpySpider(scrapy.Spider):
    name = "otto_spy"

    def start_requests(self):
        for i in range(10):
            pagination = i * 120
            url = f"https://www.otto.de/suche/bademantel/?l=gl&o={pagination}"
        
            if i == 1:
                yield scrapy.Request(
                url,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod("evaluate", """
                             const scrollToEnd = async () => {
                                 let currentScrollPosition = 0;
                                 let newScrollPosition = 0;

                                 while (true) {
                                     window.scrollBy(0, window.innerHeight);
                                     await new Promise(resolve => setTimeout(resolve, 200)); 

                                     newScrollPosition = window.scrollY;     

                                     if (newScrollPosition === currentScrollPosition) {
                                         break; // Stop scrolling if the scroll position doesn't change
                                     }

                                     currentScrollPosition = newScrollPosition;
                                 }
                             };
                             scrollToEnd();
                         """),
                            PageMethod("wait_element", 'button#onetrust-reject-all-handler'),
                            PageMethod("click", 'button#onetrust-reject-all-handler'),
                        ]
                    ),
                    callback=self.parse,
                )
                
            else:
                yield scrapy.Request(
                    url,
                    meta=dict(
                        playwright=True,
                        playwright_include_page=True,
                        playwright_page_methods=[
                            PageMethod("evaluate", """
                                 const scrollToEnd = async () => {
                                     let currentScrollPosition = 0;
                                     let newScrollPosition = 0;

                                     while (true) {
                                         window.scrollBy(0, window.innerHeight);
                                         await new Promise(resolve => setTimeout(resolve, 200)); 

                                         newScrollPosition = window.scrollY;     

                                         if (newScrollPosition === currentScrollPosition) {
                                             break; // Stop scrolling if the scroll position doesn't change
                                         }

                                         currentScrollPosition = newScrollPosition;
                                     }
                                 };
                                 scrollToEnd();
                             """),
                            ]
                        ),
                        callback=self.parse,
                    )

    # async def links(self, response):
    #     page = response.meta["playwright_page"]
        
    #     products = response.xpath('//div[@class="find_tile__productImageContainer"]')
    #     #next_button = response.xpath('//li[@id="reptile-paging-top-next"]/button')        
        
    #     for index in range(1, len(products) + 1):
            
    #         url = response.xpath(f'//section/article[{index}]/ul/li/div/div[2]/header/a/@href').get()
    #         full_rul = 'https://www.otto.de' + url
            
    #         yield {
    #             "url" : full_rul
    #         }
        
        
    async def parse(self, response):
        page = response.meta["playwright_page"]

       
        products = response.xpath('//div[@class="find_tile__productImageContainer"]')
        #next_button = response.xpath('//li[@id="reptile-paging-top-next"]/button')
       
        
        popUp = 'id="onetrust-reject-all-handler"'
        
        for index in range(1, len(products) + 1):
            
            url = response.xpath(f'//section/article[{index}]/ul/li/div/div[2]/header/a/@href').get()
            full_rul = 'https://www.otto.de' + url
            
            yield scrapy.Request(
                full_rul,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod("wait_element", '//span[contains(@class,"retailer-name")]'),
                        PageMethod("click", '//span[contains(@class,"retailer-name")]'),
                        PageMethod("wait_element", '//div[contains(@class, "pl_table-view--full-bleed")]/div[8]'),
                        PageMethod("click", '//div[contains(@class, "pl_table-view--full-bleed")]/div[8]')
                    ],
                ),
                callback=self.parse_product,
                errback=self.errback,
                dont_filter=True,
            )

        
        await page.close()

        
    async def parse_product(self, response):
        page = response.meta["playwright_page"]
        product = Product()
        
        
        product["Url"] = response.url
        product["Company_Name"] = response.xpath('//h1[@class = "pd_header__headline"]/text()').get()
        product["Address"] = response.xpath('//div[contains(@class, "pl_table-view--full-bleed")]/div[8]/div/div[2]/p[2]/text()').get()
        product["Phone_Number"] = response.xpath('//div[contains(@class, "pl_table-view--full-bleed")]/div[8]/div/div[2]/p[3]/a[1]/text()').get()
        product["Mail"] = response.xpath('//div[contains(@class, "pl_table-view--full-bleed")]/div[8]/div/div[2]/p[3]/a[2]/text()').get()
        product["Product_Name"] = response.xpath('//h1[@data-qa="variationName"]/div[2]/text()').get()
        
        
        
        yield product
        
        await page.close()
        
    
    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()