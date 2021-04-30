import requests
import re
from bs4 import BeautifulSoup



class InternalCrawler:
    def __init__(self, sitename, homeurl):
        """
        Initialize with name of site
        """
        self.sitename = sitename
        self.homeurl = homeurl
        self.found_links = set()
        self.all_links = []

    def get_links(self, homeurl=None):

        if homeurl is None:
            homeurl = self.homeurl
        html = requests.get(homeurl)
        bs =BeautifulSoup(html.text, 'html.parser')
        urlpart = '{}://{}'.format(urlparse(homeurl).scheme, urlparse(homeurl).netloc)
        found_links = set()
        #print(bs.text)
        all_full_links = [link for link in bs.find_all('a', href=re.compile('^(/|.*'+urlpart+')') )]
        all_abs_links = [link for link in bs.find_all('a', href=re.compile('^(./)') )]
        for link in all_abs_links + all_full_links:
            #print("ffs")

            if link.attrs['href'] not in self.found_links:
                #print(link.attrs['href'])
                if(link.attrs['href'].startswith('/')):
                    self.all_links.append(urlpart+link.attrs['href'])
                    self.found_links.add(urlpart+link.attrs['href'])
                else:
                    self.all_links.append(link.attrs['href'])
                    self.found_links.add(link.attrs['href'])

    def crawl_and_store(self):
        print(f"Crawling {self.sitename} starting from {self.homeurl}")
        self.get_links()
        for link in self.all_links:
            if 'https' not in link:
                link = self.homeurl + link[1:]
            self.get_links(link)
