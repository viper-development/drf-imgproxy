from django.apps import apps
from django.test import TestCase

from drf_imgproxy.apps import DrfImgproxyConfig


class DrfImgproxyConfigTest(TestCase):
    def test_app_name(self):
        self.assertEqual(DrfImgproxyConfig.name, 'drf_imgproxy')
        self.assertEqual(apps.get_app_config('drf_imgproxy').name,
                         'drf_imgproxy')
