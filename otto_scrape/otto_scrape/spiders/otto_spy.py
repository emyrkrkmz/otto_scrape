import scrapy
import json
from scrapy_playwright.page import PageMethod
from otto_scrape.items import Product

#keywords = [bademantel, bettwäsche, pouf, bodenkissen, memory foam kissen, sitzkissen, nackenkissen, teppich, kuscheldecke]

class OttoSpySpider(scrapy.Spider):
    name = "otto_spy"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.failed_urls = []  # List to store failed URLs

    def start_requests(self):
        for i in range(1):
            pagination = i * 120
            url = f"https://www.otto.de/suche/memory%20foam%20kissen/?l=gl&o={pagination}"
        
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
                    errback=self.errback
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
                    errback=self.errback
                )

    async def parse(self, response):
        page = response.meta["playwright_page"]
       
        products = response.xpath('//div[@class="find_tile__productImageContainer"]')
        
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
        page = failure.request.meta.get("playwright_page")
        url = failure.request.url  # Get the failed URL

        if page:
            screenshot_path = f"screenshots/error_memoryfoamkissen.png"
            self.logger.info(f"Saving screenshot to {screenshot_path}")
            await page.screenshot(path=screenshot_path, full_page=True)
            await page.close()

        # Append the failed URL to the list
        self.failed_urls.append(url)
        self.logger.error(f"Failed to process {url}")

    def closed(self, reason):
        # Save failed URLs to a JSON file after the spider finishes
        if self.failed_urls:
            file_path = f"failed_urls_memoryfoamkissen.json"
            with open(file_path, "w") as f:
                json.dump(self.failed_urls, f, indent=4)
            self.logger.info(f"Saved failed URLs to {file_path}")
