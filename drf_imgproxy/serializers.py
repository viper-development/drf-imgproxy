import base64
import hashlib
import hmac
import textwrap
from urllib.parse import urljoin

from django.conf import settings
from rest_framework import serializers


class ImgproxyResizeableImageField(serializers.ImageField):
    def generate_signed_url(self, width, height, data):
        key = bytes.fromhex(settings.IMGPROXY_KEY)
        salt = bytes.fromhex(settings.IMGPROXY_SALT)

        url = str.encode(
            f'{settings.IMGPROXY_PROTOCOL}://'
            f'{settings.IMGPROXY_BUCKET_NAME}/{data.name}')

        encoded_url = base64.urlsafe_b64encode(url).rstrip(b'=').decode()
        encoded_url = '/'.join(textwrap.wrap(encoded_url, 16))

        path = '/{resize}/{w}/{h}/{gravity}/{enlarge}/{url}.{ext}'.format(
            url=encoded_url,
            resize='fit',
            w=width,
            h=height,
            gravity='no',
            enlarge=1,
            ext='png',
        ).encode()

        digest = hmac.new(
            key, msg=salt+path, digestmod=hashlib.sha256).digest()
        protection = base64.urlsafe_b64encode(digest).rstrip(b'=')
        signed_url = (b'/%s%s' % (protection, path)).decode()

        return urljoin(settings.IMGPROXY_HOST, signed_url)

    def to_representation(self, data):
        if not data.name:
            return None
        return {f'{h}p': self.generate_signed_url(w, h, data)
                for w, h in settings.IMGPROXY_RESOLUTIONS}
