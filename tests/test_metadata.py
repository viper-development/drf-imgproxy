from django.test import TestCase

import drf_imgproxy


class MetadataTest(TestCase):
    def test_version(self):
        self.assertEqual(drf_imgproxy.__version__, '0.1.0')