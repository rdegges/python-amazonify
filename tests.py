from unittest import TestCase

from amazonify import amazonify


class Amazonify(TestCase):

    def test_requires_url(self):
        self.assertRaises(TypeError, amazonify)

    def test_requires_affiliate_tag(self):
        self.assertRaises(TypeError, amazonify, 'http://www.amazon.com/PostgreSQL-High-Performance-Gregory-Smith/dp/184951030X/ref=trdrt_tipp_dp_img_GWTB_507846?pf_rd_p=1367759962&pf_rd_s=right-4&pf_rd_t=101&pf_rd_i=507846&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=1216X6HJC7KEWY0X3VD7')

    def test_strips_original_querystrings(self):
        pass
