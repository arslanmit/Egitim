from skyscanner.skyscanner import Flights
flights_service = Flights('am296617236898565695386145032921')
result = flights_service.get_result(
    country='TR',
    currency='EUR',
    locale='en-GB',
    originplace='IST-sky',
    destinationplace='OGU-sky',
    outbounddate='2017-01-20',
    inbounddate='2017-01-30',
    adults=1).parsed

print(result)
