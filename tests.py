from unittest import TestCase

from amazonify import amazonify


class Amazonify(TestCase):

    def test_requires_url(self):
        self.assertRaises(TypeError, amazonify)
