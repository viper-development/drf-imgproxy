from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from drf_imgproxy.serializers import ImgproxyResizeableImageField


class FakeFile:
    def __init__(self, name, url=None):
        self.name = name
        self.url = url


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

    def test_skip(self):
        fake_url = 'https://imgproxy.test.local/test.png'
        file = FakeFile('test.png', url=fake_url)

        with self.settings(IMGPROXY_SKIP=True):
            res = self.serializer.to_representation(file)

            self.assertEqual(res, {
                '480p': fake_url,
                '600p': fake_url,
            })
