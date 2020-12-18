from django.test import TestCase

from drf_imgproxy.serializers import ImgproxyResizeableImageField


class FakeFile:
    def __init__(self, name):
        self.name = name


class ImgproxyResizeableImageFieldTest(TestCase):
    def setUp(self):
        self.serializer = ImgproxyResizeableImageField()

    def test_valid_file_to_representation(self):
        res = self.serializer.to_representation(FakeFile('test.png'))

        self.assertEqual(res, {
            '480p': ('http://imgproxy.test.local/'
                     'tOg8udnDDIvxC8SE2vRDuKn6EpJtuMHvKvGWHgmMQMI/'
                     'fit/640/480/no/1/'
                     'czM6Ly90ZXN0X2J1/Y2tldC90ZXN0LnBu/Zw.png'),
            '600p': ('http://imgproxy.test.local/'
                     'QQ59OfdiJxnIecjz3V5SRDEvOWLmLiYol_4yNpyelsk/'
                     'fit/800/600/no/1/'
                     'czM6Ly90ZXN0X2J1/Y2tldC90ZXN0LnBu/Zw.png'),
        })

    def test_invalid_file_to_representation(self):
        res = self.serializer.to_representation(FakeFile(None))
        self.assertEqual(res, None)
