from unittest import TestCase
from urlparse import urlparse

from amazonify import amazonify


class Amazonify(TestCase):

    def test_requires_url(self):
        self.assertRaises(TypeError, amazonify)

    def test_requires_affiliate_tag(self):
        self.assertRaises(TypeError, amazonify, 'http://www.amazon.com/PostgreSQL-High-Performance-Gregory-Smith/dp/184951030X/ref=trdrt_tipp_dp_img_GWTB_507846?pf_rd_p=1367759962&pf_rd_s=right-4&pf_rd_t=101&pf_rd_i=507846&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=1216X6HJC7KEWY0X3VD7')

    def test_returns_string(self):
        self.assertIsInstance(amazonify('http://www.amazon.com/PostgreSQL-High-Performance-Gregory-Smith/dp/184951030X/ref=trdrt_tipp_dp_img_GWTB_507846?pf_rd_p=1367759962&pf_rd_s=right-4&pf_rd_t=101&pf_rd_i=507846&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=1216X6HJC7KEWY0X3VD7', 'rdegges-20'), str)

    def test_returns_none_for_invalid_urls(self):
        self.assertFalse(amazonify('', 'rdegges-20'))
        self.assertFalse(amazonify('http://?hi=there', 'rdegges-20'))
        self.assertFalse(amazonify('?hi=there', 'rdegges-20'))
        self.assertFalse(amazonify('/yo/yo/', 'rdegges-20'))

    def test_strips_original_querystrings(self):
        parsed_url = urlparse('http://www.amazon.com/PostgreSQL-High-Performance-Gregory-Smith/dp/184951030X/ref=trdrt_tipp_dp_img_GWTB_507846?pf_rd_p=1367759962&pf_rd_s=right-4&pf_rd_t=101&pf_rd_i=507846&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=1216X6HJC7KEWY0X3VD7')
        self.assertNotIn(parsed_url.query, amazonify(parsed_url.geturl(), 'rdegges-20'))
