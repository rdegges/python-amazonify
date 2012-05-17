"""The simplest way to build Amazon Affiliate links, in Python."""


from urlparse import urlparse, urlunparse


def amazonify(url, affiliate_tag):
    """Generate an Amazon affiliate link given any Amazon link and affiliate
    tag.

    :param str url: The Amazon URL.
    :param str affiliate_tag: Your unique Amazon affiliate tag.
    :rtype: str
    :returns: An equivalent Amazon URL with the desired affiliate tag included.

    Usage::

        >>> from amazonify import amazonify
        >>> url = 'someamazonurl'
        >>> tag = 'youraffiliatetag'
        >>> print amazonify(url, tag)
        ...
    """

    # Firstly, remove all querystrings from the URL:
    new_url = urlparse(url)
    new_url = new_url[:4] + ('',) + new_url[5:]

    return urlunparse(new_url)
