===============================
Skyscanner Python SDK
===============================

.. image:: https://api.travis-ci.org/Skyscanner/skyscanner-python-sdk.svg
    :target: https://travis-ci.org/Skyscanner/skyscanner-python-sdk

.. image:: https://img.shields.io/pypi/v/skyscanner.svg
    :target: https://pypi.python.org/pypi/skyscanner

.. image:: https://readthedocs.org/projects/skyscanner/badge/?version=latest
        :target: https://readthedocs.org/projects/skyscanner/?badge=latest
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/Skyscanner/skyscanner-python-sdk/badge.svg?branch=master&service=github
        :target: https://coveralls.io/github/Skyscanner/skyscanner-python-sdk?branch=master


Skyscanner Python SDK for Skyscanner's API

* Free software: Apache license
* SDK Documentation: https://skyscanner.readthedocs.org.
* API Documentation: http://business.skyscanner.net/portal/en-GB/Documentation/ApiOverview


Features
--------

* Tested on Python 2.6, 2.7, 3.3, 3.4
* Supports Flights, Hotels, and Carhire


Installation
------------

At the command line::

    $ easy_install skyscanner

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv skyscanner
    $ pip install skyscanner


Quick start
-----------

1. If you don't already have one, create a `Skyscanner account`_.
2. Sign into your account and under Add Apps click Travel APIs to create an API key
3. Set your API Key in your code::

    from skyscanner.skyscanner import Flights
    flights_service = Flights('am296617236898565695386145032921')

4. Get the flights live pricing result by writing a few lines of code::

    from skyscanner.skyscanner import Flights

    flights_service = Flights('am296617236898565695386145032921')
    result = flights_service.get_result(
        country='UK',
        currency='GBP',
        locale='en-GB',
        originplace='SIN-sky',
        destinationplace='KUL-sky',
        outbounddate='2017-05-28',
        inbounddate='2017-05-31',
        adults=1).parsed

    print(result)

Note that both the ``inbounddate`` and ``outbounddate`` might need to be updated.

.. _Skyscanner account: http://portal.business.skyscanner.net/en-gb/accounts/login/


More examples
-------------

For more example usage, refer to the `SDK documentation`_ or the `API documentation`_.

.. _SDK documentation: https://skyscanner.readthedocs.org/en/latest/usage.html
.. _API documentation: http://business.skyscanner.net/portal/en-GB/Documentation/ApiOverview
  

Known Issues
------------

* Tests might appear to be broken sometimes, this is due to the throttling in the API. In such cases, you will see the following error in the build log::

        requests.exceptions.HTTPError: 429 Client Error: Too many requests in the last minute.

* Please allow up to 15 minutes for your API key to be activated. Until it is activated you will get a 403 exception::
        
        requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: http://partners.api.skyscanner.net/apiservices/pricing/v1.0?apiKey=<Your API key>

    
