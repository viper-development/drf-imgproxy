import django
from django.conf import settings


def pytest_configure():
    settings.configure(
        INSTALLED_APPS=(
            'drf_imgproxy',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        IMGPROXY_PROTOCOL='s3',
        IMGPROXY_BUCKET_NAME='test_bucket',
        IMGPROXY_KEY='f'*16,
        IMGPROXY_SALT='f'*16,
        IMGPROXY_HOST='http://imgproxy.test.local',
        IMGPROXY_RESOLUTIONS=(
            (640, 480),
            (800, 600),
        ),
    )

    django.setup()
