# python-amazonify

The simplest way to build Amazon Affiliate links, in Python.


![amazonify](https://github.com/rdegges/python-amazonify/raw/master/assets/amazonify.jpg)


## Install

To install ``python-amazonify``, simply run
``pip install amazonify`` and you'll get the latest version installed
automatically.


## Usage

Using ``amazonify`` is really easy. All you do is pass it the Amazon URL you'd
like to make into an affiliate link, and your Amazon affiliate tag.

``` python
>>> from amazonify import amazonify
>>>
>>> # Your Amazon affiliate tag:
>>> affiliate_tag = 'rdegges-20'
>>>
>>> # Some non-affiliate Amazon URLs:
>>> urls = [
...     'http://www.amazon.com/Canon-21-1MP-Frame-Digital-Camera/dp/B001G5ZTLS/ref=sr_1_1?ie=UTF8&qid=1337148615&sr=8-1',
...     'http://www.amazon.com/Transcend-Compact-Flash-Card-400X/dp/B002WE4H8I/ref=pd_bxgy_p_img_b',
...     'http://www.amazon.com/Canon-LP-E6-Battery-Digital-Cameras/dp/B001KELVS0/ref=pd_bxgy_e_img_b',
...     'http://www.amazon.com/Canon-50mm-1-8-Camera-Lens/dp/B00007E7JU/ref=sr_1_1?ie=UTF8&qid=1337148688&sr=8-1',
...     'http://www.amazon.com/Canon-70-300mm-4-5-6-Lens-Cameras/dp/B0007Y794O/ref=sr_1_3?ie=UTF8&qid=1337148688&sr=8-3',
... ]
>>> affiliate_urls = [amazonify(u, tag) for u in urls]
>>> affiliate_urls
[
    'http://www.amazon.com/Canon-21-1MP-Frame-Digital-Camera/dp/B001G5ZTLS/ref=sr_1_1?tag=rdegges-20',
    'http://www.amazon.com/Transcend-Compact-Flash-Card-400X/dp/B002WE4H8I/ref=pd_bxgy_p_img_b?tag=rdegges-20',
    'http://www.amazon.com/Canon-LP-E6-Battery-Digital-Cameras/dp/B001KELVS0/ref=pd_bxgy_e_img_b?tag=rdegges-20',
    'http://www.amazon.com/Canon-50mm-1-8-Camera-Lens/dp/B00007E7JU/ref=sr_1_1?tag=rdegges-20',
    'http://www.amazon.com/Canon-70-300mm-4-5-6-Lens-Cameras/dp/B0007Y794O/ref=sr_1_3?tag=rdegges-20'
]
```

**NOTE**: If the URL you try to ``amazonify`` is invalid, ``amazonify`` will return ``None``.


## Confused?

Have no idea what I'm talking about? See
[Amazon's Affiliate Program](https://affiliate-program.amazon.com/gp/associates/network/main.html).

Or...

[Shop on Amazon!](http://www.amazon.com/?_encoding=UTF8&tag=rdegges-20&linkCode=ur2&camp=1789&creative=390957)


## Tests

[![Build Status](https://secure.travis-ci.org/rdegges/python-amazonify.png?branch=master)](http://travis-ci.org/rdegges/python-amazonify)

Want to run the tests? No problem:

``` bash
$ git clone git://github.com/rdegges/python-amazonify.git
$ cd python-amazonify
$ python setup.py develop
...
$ pip install -r requirements.txt  # Install test dependencies.
$ nosetests
.............
----------------------------------------------------------------------
Ran 13 tests in 0.166s

OK
```


## Changelog

v0.1: 5-16-2012

    - Initial release!
