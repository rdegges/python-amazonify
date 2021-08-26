"""The simplest way to build Amazon Affiliate links, in Python."""


from urllib.parse import urlparse, urlunparse, parse_qs
from urllib import urlencode


def amazonify(url, affiliate_tag):
    """Generate an Amazon affiliate link given any Amazon link and affiliate
    tag.

    :param str url: The Amazon URL.
    :param str affiliate_tag: Your unique Amazon affiliate tag.
    :rtype: str or None
    :returns: An equivalent Amazon URL with the desired affiliate tag included,
        or None if the URL is invalid.

    Usage::

        >>> from amazonify import amazonify
        >>> url = 'someamazonurl'
        >>> tag = 'youraffiliatetag'
        >>> print amazonify(url, tag)
        ...
    """
    # Ensure the URL we're getting is valid:
    new_url = urlparse(url)
    if not new_url.netloc:
        return None

    # Add or replace the original affiliate tag with our affiliate tag in the
    # querystring. Leave everything else unchanged.
    query_dict = parse_qs(new_url[4])
    query_dict['tag'] = affiliate_tag
    new_url = new_url[:4] + (urlencode(query_dict, True), ) + new_url[5:]

    return urlunparse(new_url)
