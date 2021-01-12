############
drf-imgproxy
############

Serialize Django's ImageField into `imgproxy
<https://github.com/imgproxy/imgproxy>`_ URLs for your Django REST
Framework APIs to generate thumbnails.

****************
Important Notice
****************

This package only provides the serializer class necessary to translate
your ImageField to signed imgproxy URLs.

It does not provide anything to upload images to your object storage
bucket. We suggest you use another Django storage backend library
that's able to communicate with your object storage solution, in
particular we recommend the following:

* `django-storages <https://github.com/jschneier/django-storages>`_
* `django-minio-storage
  <https://github.com/py-pa/django-minio-storage>`_

*****
Usage
*****

0. Installation
===============

You can easily install this package from PyPI with ``pip`` by doing:

.. code:: bash

   pip install drf-imgproxy


1. Quickstart
=============

In ``settings.py``:

.. code:: python

   INSTALLED_APPS = [
     ...
     'drf_imgproxy',
     ...
   ]

   # Configure this to either of the following:
   #  - 's3' for Amazon S3, Minio and any other S3-compatible object
   #    storage
   #  - 'gs' for Google Cloud Storage
   #  - 'abs' for Azure Blob Storage
   IMGPROXY_PROTOCOL = 's3'

   # Set the following to the bucket name that imgproxy uses.
   IMGPROXY_BUCKET_NAME = 'nerv_angel_captures'

   # Set both of the following to the appropiate values of
   # `IMGPROXY_KEY` and `IMGPROXY_SALT` of your imgproxy server.
   IMGPROXY_KEY = 'ThisIsNotASecureKeyAtAll'
   IMGPROXY_SALT = 'SeriouslyThisSaltIsVeryInsecure'

   # Set the following to the publicly accessible URL of your imgproxy
   # server.
   IMGPROXY_HOST = 'https://imgproxy.infra.nerv.tld'

   # Set the following variable to the available resolutions your API
   # provides.
   #
   # The format is `(<width>, <height>)`.
   IMGPROXY_RESOLUTIONS = (
       (640,  480),
       (800,  600),
       (1024, 768),
   )

In ``serializers.py``:

.. code:: python

   ...
   from drf_imgproxy.serializers import ImgproxyResizeableImageField
   ...


   class AngelActivity(ModelSerializer):
       ...
       captured_photo_thumbs = ImgproxyResizeableImageField(
           read_only=True,
           source='captured_photo'
       )
       ...

********
See also
********

* `drf-imgproxy-demo <https://github.com/viper-development/drf-imgproxy-demo>`_
