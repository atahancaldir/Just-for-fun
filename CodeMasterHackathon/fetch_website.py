import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import datetime

class FetchWebsite():
    def __init__(self):
        self.internal_urls = set()
        self.external_urls = set()

        self.response_translator = {200: "OK", 404: "Not Found",
        310: "Too Many Redirects", 503: "Service Unavailable",
        400: "Bad Request", 408: "Request Timeout"}

        self.is_secured = False
        self.is_reachable = False

        self.response_code = 200

    def is_valid(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def get_url_data(self, url):
        session = requests.Session()
        session.max_redirects = 3

        start_time = datetime.datetime.now()
        error = True

        try:
            self.url_data = session.get(url, timeout=3)
            error = False
        except requests.exceptions.InvalidSchema:
            self.response_code = 400
        except requests.exceptions.TooManyRedirects:
            self.response_code = 310
        except requests.exceptions.ConnectionError:
            self.response_code = 503
        except requests.exceptions.ReadTimeout:
            self.response_code = 408
        except requests.exceptions.HTTPError:
            self.response_code = 404
        
        if self.response_code != 400:
            self.total_access_time = (datetime.datetime.now() - start_time).microseconds / 1000
            if self.response_code != 503:
                self.final_url = requests.get(url).url
        if self.response_code != 404 and self.response_code != 408 and self.response_code != 503 and self.response_code != 400 and self.response_code != 310:
            self.redirected_urls = [i.url for i in self.url_data.history]
        if self.response_code != 404 and self.response_code != 408 and self.response_code != 310 and self.response_code != 503 and self.response_code != 400:
            self.content_size = len(self.url_data.content)

        if not error:
            self.response_code = 200
            self.response_code = self.url_data.status_code
            self.is_reachable = True
            if self.final_url.startswith("https"):
                self.is_secured = True

        self.response_message = self.response_translator[self.response_code]

    def get_hyperlinks(self, url):
        domain_name = urlparse(url).netloc
        self.get_url_data(url)
        soup = BeautifulSoup(self.url_data.content, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not self.is_valid(href):
                continue
            if href in self.internal_urls:
                continue
            if domain_name not in href:
                if href not in self.external_urls:
                    self.external_urls.add(href)
                continue
            self.internal_urls.add(href)