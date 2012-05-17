"""The simplest way to build Amazon Affiliate links, in Python."""


from urlparse import urlparse, urlunparse


def amazonify(url, affiliate_tag):

    # Firstly, remove all querystrings from the URL:
    new_url = urlparse(url)
    new_url = new_url[:4] + ('',) + new_url[5:]

    return urlunparse(new_url)
