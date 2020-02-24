
from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "mario_images"})
crawler.crawl(keyword="まりお流ラーメン", max_num=1000)