import mechanicalsoup

def test_proxy(url, proxy):

    browser = mechanicalsoup.StatefulBrowser()
    browser.session.proxies = proxy
    browser.open(url)

    source_code = browser.get_current_page()
    print(source_code)


if __name__ == '__main__':
    """ The proxy provided by the author does not work, unsurprisingly.
    A better approach is to find an updated one on the following URL 
    if the proxy address hardcoded bellow does not provide the expected
    functionality: https://www.proxyscrape.com/free-proxy-list """

    _url = 'http://ip.nefsc.noaa.gov/'
    hide_me_proxy = {'http': '105.29.64.217:80'}

    test_proxy(_url, hide_me_proxy)