from django.test import TestCase
from .templatetags.base_image_tags import base_image

IMAGE_1X1 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4nGNgYGBgAAAABQABpfZFQAAAAABJRU5ErkJggg=='
IMAGE_16X9 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAJCAYAAAA7KqwyAAAAD0lEQVR4nGNgGAWjgAoAAAJJAAHZX3+dAAAAAElFTkSuQmCC'

class BaseImageTests(TestCase):
    def test_base_image_does_not_have_a_string(self):
        """
        image64 does not have a string
        """
        self.assertEqual(base_image(), IMAGE_1X1)

    def test_base_image_has_16x9_image(self): 
        """
        image64 has `16x9` as an img
        """
        self.assertEqual(base_image('16x9'), IMAGE_16X9)

    #def test_base_image_is_not_a_string(self): pass
    #def test_fail_base_image_is_an_integer(self):
    #    self.assertRaises(AttributeError, base_image(32), "")
    #def test_base_image_is_an_object(self): pass
    #def test_base_image_does_not_have_an_x(self): pass
    #def test_base_image_has_multiple_xs(self): pass

