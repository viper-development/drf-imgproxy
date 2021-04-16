#########
Changelog
#########

All notable changes to this project will be documented in this file.

The format is based on `Keep a changelog`_ and this project adheres to
`Semantic Versioning`_.

.. _Keep a changelog: https://keepachangelog.com/en/1.0.0
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html

*************
`Unreleased`_
*************

Added
=====

* ``IMGPROXY_SKIP``, option to skip imgproxy URL generation and only
  return the url of the source file.

.. _Unreleased: https://github.com/viper-development/drf-imgproxy/compare/1.0.1...HEAD

**********************
`1.0.1`_ -- 2021-01-12
**********************

Added
=====

* Automated publishing to PyPI
* More metadata on PyPI

.. _1.0.1: https://github.com/viper-development/drf-imgproxy/compare/1.0.0...1.0.1

**********************
`1.0.0`_ -- 2021-01-12
**********************

Added
=====

* Serializer for Django REST Framework which generates URLs for image
  assets that are served via imgproxy.
* PyPI package to easily install this project.

.. _1.0.0: https://github.com/viper-development/drf-imgproxy/releases/tag/1.0.0
