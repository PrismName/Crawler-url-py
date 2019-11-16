import urllib.request
import urllib.error
import urllib.parse
import re


patterns_a_href_link = re.compile(r'''<a href="(.*?)"''')


def parser_link(response):
    """parse link from http response content
    :param response: http response content
    :return:
    """
    a_links = patterns_a_href_link.findall(response)

    if a_links:
        for link in a_links:
            url_parser = urllib.parse.urlparse(link)
            if url_parser.scheme == "javascript" or url_parser.scheme == "" and url_parser.netloc == "":
                continue
            if not link.startswith("http://") and not link.startswith("https://"):
                link = _url_join(url_parser.scheme, url_parser.netloc,
                                 url_parser.path, url_parser.params,
                                 url_parser.query, url_parser.fragment)
            print(link)


def _url_join(scheme, netloc, path, params, query, fragment):
    """join url
    :params scheme:
    :params netloc:
    :params path:
    :params params:
    :params query:
    :params fragment:
    :return: url
    """
    if scheme == "":
        scheme = "http://"
        return scheme + netloc + path + params + query + fragment
    return scheme + "://" + netloc + path + params + query + fragment



def downloader(url):
    """download request content
    :param url: target website url
    :param headers: http request headers
    :return: http response content
    """
    try:
        request = urllib.request.Request(url=url)
        request.add_header("User-Agent", "__spider_man__")
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            return response.read().decode("utf-8")
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        pass


if __name__ == "__main__":
    url = str(input("enter a url address"))
    response = downloader(url)

    parser_link(response)

