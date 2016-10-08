from skyscanner.skyscanner import Flights
flights_service = Flights('am296617236898565695386145032921')
result = flights_service.get_result(
    country='TR',
    currency='USD',
    locale='en-GB',
    originplace='IST-sky',
    destinationplace='DAR-sky',
    outbounddate='2017-05-20',
    inbounddate='2017-05-31',
    adults=1).parsed

print(result)
