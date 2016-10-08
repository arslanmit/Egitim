from skyscanner.skyscanner import *

flights_service = Flights('am296617236898565695386145032921')
result = flights_service.get_result(
    country='TR',
    currency='EUR',
    locale='en-GB',
    originplace='IST-sky',
    destinationplace='OGU-sky',
    outbounddate='2017-02-11',
    inbounddate='2017-02-19',
    adults=1).parsed

print(result)
