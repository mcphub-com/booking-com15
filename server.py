import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/DataCrawler/api/booking-com15'

mcp = FastMCP('booking-com15')

@mcp.tool()
def get_languages() -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/meta/getLanguages'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_currency() -> dict: 
    '''Get the list of currencies that are available.'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/meta/getCurrency'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_exchange_rates(base_currency: Annotated[str, Field(description='Base currency.')]) -> dict: 
    '''Obtain a list of exchange rates for all currencies utilizing the base currency.'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/meta/getExchangeRates'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'base_currency': base_currency,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_to_lat_long(query: Annotated[str, Field(description='Names of locations, apartment, address, cities, districts, places, countries, counties etc.')]) -> dict: 
    '''Get location/address latitude and longitude'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/meta/locationToLatLong'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_location() -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/meta/getLocations'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def test_api() -> dict: 
    '''To check if server is up and running'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/test'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_hotel_destination(query: Annotated[str, Field(description='Names of locations, cities, districts, places, countries, counties etc.')]) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_filter(dest_id: Annotated[str, Field(description='dest_id can be retrieved from api/v1/hotels/searchDestination(Search Hotel Destination) endpoint in Hotels collection.')],
               search_type: Annotated[str, Field(description='search_type can be retrieved from api/v1/hotels/searchDestination(Search Hotel Destination) endpoint in hotel collection.')],
               arrival_date: Annotated[Union[str, datetime], Field(description='The date on which you will arrive or check-in')],
               departure_date: Annotated[Union[str, datetime], Field(description='The date of departure or check-out.')],
               adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 1')] = None,
               children_age: Annotated[Union[str, None], Field(description='The number of children, including infants, who are under 18. Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17')] = None,
               room_qty: Annotated[Union[int, float, None], Field(description='The number of rooms that are required. The default value is set to 1. Default: 1')] = None,
               categories_filter: Annotated[Union[str, None], Field(description='categories_filter can be retrieved from api/v1/hotels/getFilter(Get Filter) endpoint in Hotels collection. Note: For the initial request, leave it blank.')] = None,
               languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getFilter'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'dest_id': dest_id,
        'search_type': search_type,
        'arrival_date': arrival_date,
        'departure_date': departure_date,
        'adults': adults,
        'children_age': children_age,
        'room_qty': room_qty,
        'categories_filter': categories_filter,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_sort_by(dest_id: Annotated[str, Field(description='dest_id can be retrieved from api/v1/hotels/searchDestination(Search Hotel Destination) endpoint in Hotels collection.')],
                search_type: Annotated[str, Field(description='search_type can be retrieved from api/v1/hotels/searchDestination(Search Hotel Destination) endpoint in Hotels collection.')],
                arrival_date: Annotated[Union[str, datetime], Field(description='The date on which you will arrive or check-in')],
                departure_date: Annotated[Union[str, datetime], Field(description='The date of departure or check-out.')],
                adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 1')] = None,
                children_age: Annotated[Union[str, None], Field(description='The number of children, including infants, who are under 18. Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17')] = None,
                room_qty: Annotated[Union[int, float, None], Field(description='The number of rooms that are required. The default value is set to 1. Default: 1')] = None,
                categories_filter: Annotated[Union[str, None], Field(description='categories_filter can be retrieved from api/v1/hotels/getFilter(Get Filter) endpoint in Hotels collection.')] = None,
                languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getSortBy'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'dest_id': dest_id,
        'search_type': search_type,
        'arrival_date': arrival_date,
        'departure_date': departure_date,
        'adults': adults,
        'children_age': children_age,
        'room_qty': room_qty,
        'categories_filter': categories_filter,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_hotels(dest_id: Annotated[Union[int, float], Field(description='dest_id can be retrieved from api/v1/hotels/searchDestination(Search Hotel Destination) endpoint in Hotels collection. Default: -2092174')],
                  search_type: Annotated[str, Field(description='search_type can be retrieved from api/v1/hotels/searchDestination(Search Hotel Destination) endpoint in Hotels collection.')],
                  arrival_date: Annotated[Union[str, datetime], Field(description='The date on which you will arrive or check-in')],
                  departure_date: Annotated[Union[str, datetime], Field(description='The date of departure or check-out.')],
                  adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 1')] = None,
                  children_age: Annotated[Union[str, None], Field(description='The number of children, including infants, who are under 18. Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17')] = None,
                  room_qty: Annotated[Union[int, float, None], Field(description='The number of rooms that are required. The default value is set to 1. Default: 1')] = None,
                  page_number: Annotated[Union[int, float, None], Field(description='The page number. Default: 1')] = None,
                  price_min: Annotated[Union[int, float, None], Field(description='Minimum Price filter for search. Default: 0')] = None,
                  price_max: Annotated[Union[int, float, None], Field(description='Maximum Price filter for search. Default: 0')] = None,
                  sort_by: Annotated[Union[str, None], Field(description='sort_by can be retrieved from api/v1/hotels/getSortBy(Get Sort By) endpoint in Hotels collection.')] = None,
                  categories_filter: Annotated[Union[str, None], Field(description='categories_filter can be retrieved from api/v1/hotels/getFilter(Get Filter) endpoint in Hotels collection.')] = None,
                  units: Annotated[Literal['metric', 'imperial', None], Field(description='The measurement of distance in metric or imperial.')] = None,
                  temperature_unit: Annotated[Literal['c', 'f', None], Field(description='The temperature unit in Fahrenheit or Celsius. c = Celsius f = Fahrenheit')] = None,
                  languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                  currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                  location: Annotated[Union[str, None], Field(description='location can be retrieved from api/v1/meta/getLocations(Get Location) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'dest_id': dest_id,
        'search_type': search_type,
        'arrival_date': arrival_date,
        'departure_date': departure_date,
        'adults': adults,
        'children_age': children_age,
        'room_qty': room_qty,
        'page_number': page_number,
        'price_min': price_min,
        'price_max': price_max,
        'sort_by': sort_by,
        'categories_filter': categories_filter,
        'units': units,
        'temperature_unit': temperature_unit,
        'languagecode': languagecode,
        'currency_code': currency_code,
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_hotels_by_coordinates(latitude: Annotated[str, Field(description='Latitude of the searched location. latitude can be retrieved from api/v1/meta/locationToLatLong(Location to Lat Long) endpoint in Meta collection.')],
                                 longitude: Annotated[str, Field(description='Longitude of the searched location. longitude can be retrieved from api/v1/meta/locationToLatLong(Location to Lat Long) endpoint in Meta collection.')],
                                 arrival_date: Annotated[Union[str, datetime], Field(description='The date on which you will arrive or check-in')],
                                 departure_date: Annotated[Union[str, datetime], Field(description='The date of departure or check-out.')],
                                 radius: Annotated[Union[int, float, None], Field(description='The hotels that are within the radius. The radius is measured in kilometers. Default is set to 100. Range is between 10 to 500. Default: 0')] = None,
                                 adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 1')] = None,
                                 children_age: Annotated[Union[str, None], Field(description='The number of children, including infants, who are under 18. Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17')] = None,
                                 room_qty: Annotated[Union[int, float, None], Field(description='The number of rooms that are required. The default value is set to 1. Default: 1')] = None,
                                 price_min: Annotated[Union[int, float, None], Field(description='Minimum Price filter for search. Default: 0')] = None,
                                 price_max: Annotated[Union[int, float, None], Field(description='Maximum Price filter for search. Default: 0')] = None,
                                 units: Annotated[Literal['metric', 'imperial', None], Field(description='The measurement of distance in metric or imperial.')] = None,
                                 page_number: Annotated[Union[str, None], Field(description='')] = None,
                                 temperature_unit: Annotated[Literal['c', 'f', None], Field(description='The temperature unit in Fahrenheit or Celsius. c = Celsius f = Fahrenheit')] = None,
                                 languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                                 currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                                 location: Annotated[Union[str, None], Field(description='location can be retrieved from api/v1/meta/getLocations(Get Location) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotelsByCoordinates'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'arrival_date': arrival_date,
        'departure_date': departure_date,
        'radius': radius,
        'adults': adults,
        'children_age': children_age,
        'room_qty': room_qty,
        'price_min': price_min,
        'price_max': price_max,
        'units': units,
        'page_number': page_number,
        'temperature_unit': temperature_unit,
        'languagecode': languagecode,
        'currency_code': currency_code,
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_hotel_details(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                      arrival_date: Annotated[Union[str, datetime], Field(description='The date on which you will arrive or check-in')],
                      departure_date: Annotated[Union[str, datetime], Field(description='The date of departure or check-out.')],
                      adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 1')] = None,
                      children_age: Annotated[Union[str, None], Field(description='The number of children, including infants, who are under 18. Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17')] = None,
                      room_qty: Annotated[Union[int, float, None], Field(description='The number of rooms that are required. The default value is set to 1. Default: 1')] = None,
                      units: Annotated[Literal['metric', 'imperial', None], Field(description='The measurement of distance in metric or imperial.')] = None,
                      temperature_unit: Annotated[Literal['c', 'f', None], Field(description='The temperature unit in Fahrenheit or Celsius. c = Celsius f = Fahrenheit')] = None,
                      languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                      currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelDetails'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'arrival_date': arrival_date,
        'departure_date': departure_date,
        'adults': adults,
        'children_age': children_age,
        'room_qty': room_qty,
        'units': units,
        'temperature_unit': temperature_unit,
        'languagecode': languagecode,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_room_availability(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                          min_date: Annotated[Union[str, datetime], Field(description='The starting date range.')],
                          max_date: Annotated[Union[str, datetime], Field(description='The ending date range')],
                          room_qty: Annotated[Union[int, float, None], Field(description='The number of rooms that are required. The default value is set to 1. Default: 0')] = None,
                          adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 0')] = None,
                          currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                          location: Annotated[Union[str, None], Field(description='location can be retrieved from api/v1/meta/getLocations(Get Location) endpoint in Meta collection.')] = None) -> dict: 
    '''Check for availability on future dates.'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getAvailability'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'min_date': min_date,
        'max_date': max_date,
        'room_qty': room_qty,
        'adults': adults,
        'currency_code': currency_code,
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_description_and_info(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                             languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getDescriptionAndInfo'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_room_list(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                  arrival_date: Annotated[Union[str, datetime], Field(description='The date on which you will arrive or check-in')],
                  departure_date: Annotated[Union[str, datetime], Field(description='The date of departure or check-out.')],
                  adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 1')] = None,
                  children_age: Annotated[Union[str, None], Field(description='The number of children, including infants, who are under 18. Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17')] = None,
                  room_qty: Annotated[Union[int, float, None], Field(description='The number of rooms that are required. The default value is set to 1. Default: 1')] = None,
                  units: Annotated[Literal['metric', 'imperial', None], Field(description='The measurement of distance in metric or imperial.')] = None,
                  temperature_unit: Annotated[Literal['c', 'f', None], Field(description='The temperature unit in Fahrenheit or Celsius. c = Celsius f = Fahrenheit')] = None,
                  languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                  currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                  location: Annotated[Union[str, None], Field(description='location can be retrieved from api/v1/meta/getLocations(Get Location) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getRoomList'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'arrival_date': arrival_date,
        'departure_date': departure_date,
        'adults': adults,
        'children_age': children_age,
        'room_qty': room_qty,
        'units': units,
        'temperature_unit': temperature_unit,
        'languagecode': languagecode,
        'currency_code': currency_code,
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def payment_features_of_the_hotel(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                                  languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getPaymentFeatures'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_hotel_policies(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                       languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelPolicies'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_children_policies(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                               languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/propertyChildrenPolicies'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_hotel_reviews_filter_metadata(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                                      languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelReviewsFilterMetadata'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_hotel_review_scores(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                            languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelReviewScores'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_hotel_reviews_sort_option(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                                  languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''Obtain all the available sort parameters for hotel reviews.'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelReviewsSortOption'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_hotel_reviews(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                      sort_option_id: Annotated[Union[str, None], Field(description='sort_option_id can be retrieved from api/v1/hotels/getHotelReviewsSortOption(Get Hotel Reviews(Tips) Sort Option) endpoint in Hotels collection.')] = None,
                      page_number: Annotated[Union[int, float, None], Field(description='The page number. Default: 1')] = None,
                      languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelReviews'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'sort_option_id': sort_option_id,
        'page_number': page_number,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_question_and_answer(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                            languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getQuestionAndAnswer'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_nearby_cities(latitude: Annotated[str, Field(description='Latitude of the searched location. latitude can be retrieved from api/v1/meta/locationToLatLong(Location to Lat Long) endpoint in Meta collection.')],
                      longitude: Annotated[str, Field(description='Longitude of the searched location. longitude can be retrieved from api/v1/meta/locationToLatLong(Location to Lat Long) endpoint in Meta collection.')],
                      languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getNearbyCities'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_popular_attraction_near_by(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                                   languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getPopularAttractionNearBy'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_room_list_with_availability(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                                    arrival_date: Annotated[Union[str, datetime], Field(description='The date on which you will arrive or check-in')],
                                    departure_date: Annotated[Union[str, datetime], Field(description='The date of departure or check-out.')],
                                    adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 1')] = None,
                                    children_age: Annotated[Union[str, None], Field(description='The number of children, including infants, who are under 18. Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17')] = None,
                                    room_qty: Annotated[Union[int, float, None], Field(description='The number of rooms that are required. The default value is set to 1. Default: 1')] = None,
                                    units: Annotated[Literal['metric', 'imperial', None], Field(description='The measurement of distance in metric or imperial.')] = None,
                                    temperature_unit: Annotated[Literal['c', 'f', None], Field(description='The temperature unit in Fahrenheit or Celsius. c = Celsius f = Fahrenheit')] = None,
                                    languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                                    currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                                    location: Annotated[Union[str, None], Field(description='location can be retrieved from api/v1/meta/getLocations(Get Location) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getRoomListWithAvailability'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'arrival_date': arrival_date,
        'departure_date': departure_date,
        'adults': adults,
        'children_age': children_age,
        'room_qty': room_qty,
        'units': units,
        'temperature_unit': temperature_unit,
        'languagecode': languagecode,
        'currency_code': currency_code,
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_hotel_photos(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')]) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelPhotos'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_hotel_facilities(hotel_id: Annotated[str, Field(description='hotel_id can be retrieved from api/v1/hotels/searchHotels(Search Hotels) or api/v1/hotels/searchHotelsByCoordinates(Search Hotels By Coordinates ) endpoint in Hotels collection.')],
                         arrival_date: Annotated[Union[str, datetime, None], Field(description='The date on which you will arrive or check-in')] = None,
                         departure_date: Annotated[Union[str, datetime, None], Field(description='The date of departure or check-out.')] = None,
                         languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelFacilities'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hotel_id': hotel_id,
        'arrival_date': arrival_date,
        'departure_date': departure_date,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_flight_location(query: Annotated[str, Field(description='Names of airport, locations, cities, districts, places, countries, counties etc.')],
                           languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''Find airports by their location, address, state, country, etc.'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/flights/searchDestination'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_flights(fromId: Annotated[str, Field(description='From/Departure location Id. fromId can be retrieved from api/v1/flights/searchDestination(Search Flight Location) endpoint in Flights collection as id.')],
                   toId: Annotated[str, Field(description='To/Arrival location Id. toId can be retrieved from api/v1/flights/searchDestination(Search Flight Location) endpoint in Flights collection as id.')],
                   departDate: Annotated[Union[str, datetime], Field(description='Departure or travel date. Format: YYYY-MM-DD')],
                   returnDate: Annotated[Union[str, datetime, None], Field(description='Return date. Format: YYYY-MM-DD')] = None,
                   stops: Annotated[Literal['none', '0', '1', '2', None], Field(description='Filters flights based on the number of stops. Accepted values are: none for no preference (returns flights with any number of stops) 0 for non-stop flights 1 for one-stop flights 2 for two-stop flights If provided, the value must be either none, 0, 1, or 2.')] = None,
                   pageNo: Annotated[Union[int, float, None], Field(description='The page number. Default: 1')] = None,
                   adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 1')] = None,
                   children: Annotated[Union[str, None], Field(description='The number of children, including infants, who are under 18. Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17')] = None,
                   sort: Annotated[Literal['BEST', 'CHEAPEST', 'FASTEST', None], Field(description='This parameter orders result by BEST, CHEAPEST or FASTEST flights.')] = None,
                   cabinClass: Annotated[Literal['ECONOMY', 'PREMIUM_ECONOMY', 'BUSINESS', 'FIRST', None], Field(description='Search for flights that match the cabin class specified. Cabin call can be either ECONOMY, PREMIUM_ECONOMY, BUSINESS or FIRST.')] = None,
                   currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fromId': fromId,
        'toId': toId,
        'departDate': departDate,
        'returnDate': returnDate,
        'stops': stops,
        'pageNo': pageNo,
        'adults': adults,
        'children': children,
        'sort': sort,
        'cabinClass': cabinClass,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_flights_multi_stops(legs: Annotated[str, Field(description="The legs must contain the fromId, toId and date in object format and must be passed in an array. EXAMPLE: [ { 'fromId': 'BOM.AIRPORT', 'toId': 'AMD.AIRPORT', 'date': '2024-05-25' }, … ] Note: If there are multiple stops, there should be more leg objects in the array.")],
                               pageNo: Annotated[Union[int, float, None], Field(description='The page number. Default: 1')] = None,
                               adults: Annotated[Union[int, float, None], Field(description='The number of guests who are 18 years of age or older. The default value is set to 1. Default: 1')] = None,
                               children: Annotated[Union[str, None], Field(description='The number of children, including infants, who are under 18. Example: Child 1 Age = 8 months Child 2 Age = 1 year Child 3 Age = 17 years Here is what the request parameter would look like: children_age: 0,1,17')] = None,
                               sort: Annotated[Literal['BEST', 'CHEAPEST', 'FASTEST', None], Field(description='This parameter orders result by BEST, CHEAPEST or FASTEST flights.')] = None,
                               cabinClass: Annotated[Literal['ECONOMY', 'PREMIUM_ECONOMY', 'BUSINESS', 'FIRST', None], Field(description='Search for flights that match the cabin class specified. Cabin call can be either ECONOMY, PREMIUM_ECONOMY, BUSINESS or FIRST.')] = None,
                               currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlightsMultiStops'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'legs': legs,
        'pageNo': pageNo,
        'adults': adults,
        'children': children,
        'sort': sort,
        'cabinClass': cabinClass,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_flight_details(token: Annotated[str, Field(description='token can be retrieved from api/v1/flights/searchFlights(Search Flights) or api/v1/flights/searchFlightsMultiStops(Search Flights Multi Stops) endpoints in Flights collection as token.')],
                       currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/flights/getFlightDetails'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'token': token,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_min_price(fromId: Annotated[str, Field(description='From/Departure location Id. fromId can be retrieved from api/v1/flights/searchDestination(Search Flight Location) endpoint in Flights collection as id.')],
                  toId: Annotated[str, Field(description='To/Arrival location Id. toId can be retrieved from api/v1/flights/searchDestination(Search Flight Location) endpoint in Flights collection as id.')],
                  departDate: Annotated[Union[str, datetime], Field(description='Departure or travel date. Format: YYYY-MM-DD')],
                  returnDate: Annotated[Union[str, datetime, None], Field(description='Return date. Format: YYYY-MM-DD')] = None,
                  cabinClass: Annotated[Literal['ECONOMY', 'PREMIUM_ECONOMY', 'BUSINESS', 'FIRST', None], Field(description='Search for flights that match the cabin class specified. Cabin call can be either ECONOMY, PREMIUM_ECONOMY, BUSINESS or FIRST.')] = None,
                  currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/flights/getMinPrice'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fromId': fromId,
        'toId': toId,
        'departDate': departDate,
        'returnDate': returnDate,
        'cabinClass': cabinClass,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_min_price_multi_stops(legs: Annotated[str, Field(description="The legs must contain the fromId, toId and date in object format and must be passed in an array. EXAMPLE: [ { 'fromId': 'BOM.AIRPORT', 'toId': 'AMD.AIRPORT', 'date': '2024-05-25' }, … ] Note: If there are multiple stops, there should be more leg objects in the array.")],
                              cabinClass: Annotated[Union[str, None], Field(description='Search for flights that match the cabin class specified. Cabin call can be either ECONOMY, PREMIUM_ECONOMY, BUSINESS or FIRST.')] = None,
                              currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/flights/getMinPriceMultiStops'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'legs': legs,
        'cabinClass': cabinClass,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_seat_map(offerToken: Annotated[str, Field(description='offerToken can be retrieved from api/v1/flights/searchFlights(Search Flights) or api/v1/flights/searchFlightsMultiStops(Search Flights Multi Stops) endpoints in Flights collection as offerToken.')],
                 currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/flights/getSeatMap'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'offerToken': offerToken,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_car_location(query: Annotated[str, Field(description='Names of locations, cities, districts, places, countries, counties etc.')],
                        languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''Find locations by searching for their name, address, city, state, country, etc.'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/cars/searchDestination'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_car_rentals(pick_up_latitude: Annotated[Union[int, float], Field(description="The pick up location's latitude. pick_up_latitude can be retrieved from api/v1/cars/searchDestination(Search Car Location) endpoint in Car Rental collection as latitude inside coordinates object. Default: 40.6397018432617")],
                       pick_up_longitude: Annotated[Union[int, float], Field(description="The pick up location's longitude. pick_up_longitude can be retrieved from api/v1/cars/searchDestination(Search Car Location) endpoint in Car Rental collection as longitude inside coordinates object. Default: -73.7791976928711")],
                       drop_off_latitude: Annotated[Union[int, float], Field(description="The drop off location's latitude. drop_off_latitude can be retrieved from api/v1/cars/searchDestination(Search Car Location) endpoint in Car Rental collection as latitude inside coordinates object. Default: 40.6397018432617")],
                       drop_off_longitude: Annotated[Union[int, float], Field(description="The drop off location's longitude. drop_off_longitude can be retrieved from api/v1/cars/searchDestination(Search Car Location) endpoint in Car Rental collection as longitude inside coordinates object. Default: -73.7791976928711")],
                       pick_up_date: Annotated[Union[str, datetime], Field(description='Pick up date Format: YYYY-MM-DD')],
                       drop_off_date: Annotated[Union[str, datetime], Field(description='Drop off date Format: YYYY-MM-DD')],
                       pick_up_time: Annotated[Union[str, datetime], Field(description='Pick up time Format: HH:MM Note: The format of time is 24 hours.')],
                       drop_off_time: Annotated[Union[str, datetime], Field(description='Drop off time Format: HH:MM Note: The format of time is 24 hours.')],
                       driver_age: Annotated[Union[int, float, None], Field(description="The driver's age. The default value is set to 30. Note: The driver age must be in the range of 20 to 65 years. Default: 30")] = None,
                       filters: Annotated[Union[str, None], Field(description='Used to refine search results based on specific suppliers, car categories, or other attributes. Multiple filters can be applied by passing them as a comma-separated list in the following format: :: For example: supplier::Avis,supplier::Budget,carCategory::medium,carCategory::large This will return results from Avis and Budget, and only cars in the medium and large categories. To discover available filters, make a request to the /api/v1/cars/searchCarRentals endpoint and refer to the data → filter section in the response.')] = None,
                       languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                       currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                       location: Annotated[Union[str, None], Field(description='location can be retrieved from api/v1/meta/getLocations(Get Location) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/cars/searchCarRentals'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pick_up_latitude': pick_up_latitude,
        'pick_up_longitude': pick_up_longitude,
        'drop_off_latitude': drop_off_latitude,
        'drop_off_longitude': drop_off_longitude,
        'pick_up_date': pick_up_date,
        'drop_off_date': drop_off_date,
        'pick_up_time': pick_up_time,
        'drop_off_time': drop_off_time,
        'driver_age': driver_age,
        'filters': filters,
        'languagecode': languagecode,
        'currency_code': currency_code,
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_packages(vehicle_id: Annotated[str, Field(description='Vehicle ID. vehicle_id can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as vehicle_id inside search_results object.')],
                 search_key: Annotated[str, Field(description='search_key can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as search_key.')],
                 languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                 currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/cars/getPackages'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vehicle_id': vehicle_id,
        'search_key': search_key,
        'languagecode': languagecode,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def vehicle_details(vehicle_id: Annotated[str, Field(description='Vehicle ID. vehicle_id can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as vehicle_id inside search_results object.')],
                    search_key: Annotated[str, Field(description='search_key can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as search_key.')],
                    units: Annotated[Literal['metric', 'imperial', None], Field(description='The measurement of distance in metric or imperial.')] = None,
                    currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                    languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/cars/vehicleDetails'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vehicle_id': vehicle_id,
        'search_key': search_key,
        'units': units,
        'currency_code': currency_code,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def booking_summary(vehicle_id: Annotated[str, Field(description='Vehicle ID. vehicle_id can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as vehicle_id inside search_results object.')],
                    search_key: Annotated[str, Field(description='search_key can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as search_key.')],
                    languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                    currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/cars/bookingSummary'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vehicle_id': vehicle_id,
        'search_key': search_key,
        'languagecode': languagecode,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def vehicle_supplier_details(vehicle_id: Annotated[str, Field(description='Vehicle ID. vehicle_id can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as vehicle_id inside search_results object.')],
                             search_key: Annotated[str, Field(description='')],
                             languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                             currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/cars/vehicleSupplierDetails'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vehicle_id': vehicle_id,
        'search_key': search_key,
        'languagecode': languagecode,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def vehicle_supplier_ratings(vehicle_id: Annotated[str, Field(description='Vehicle ID. vehicle_id can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as vehicle_id inside search_results object.')],
                             search_key: Annotated[str, Field(description='search_key can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as search_key.')],
                             languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                             currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/cars/vehicleSupplierRatings'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vehicle_id': vehicle_id,
        'search_key': search_key,
        'languagecode': languagecode,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def vehicle_supplier_review(vehicle_id: Annotated[str, Field(description='Vehicle ID. vehicle_id can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as vehicle_id inside search_results object.')],
                            search_key: Annotated[str, Field(description='search_key can be retrieved from api/v1/cars/searchCarRentals(Search Car Rentals) endpoint in Car Rental collection as search_key.')],
                            languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/cars/vehicleSupplierReview'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'vehicle_id': vehicle_id,
        'search_key': search_key,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def taxi_search_location(query: Annotated[str, Field(description='Names of locations, cities, districts, places, countries, counties etc.')],
                         languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/taxi/searchLocation'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_taxi(pick_up_place_id: Annotated[str, Field(description="The pick up location's place id. pick_up_place_id can be retrieved from api/v1/taxi/searchLocation(Taxi Search Location) endpoint in Taxi collection as googlePlaceId.")],
                drop_off_place_id: Annotated[str, Field(description="The drop off location's place id. drop_off_place_id can be retrieved from api/v1/taxi/searchLocation(Taxi Search Location) endpoint in Taxi collection as googlePlaceId.")],
                pick_up_date: Annotated[Union[str, datetime], Field(description='Pick up date Format: YYYY-MM-DD')],
                pick_up_time: Annotated[Union[str, datetime], Field(description='Pick up time Format: HH:MM Note: The format of time is 24 hours.')],
                currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/taxi/searchTaxi'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pick_up_place_id': pick_up_place_id,
        'drop_off_place_id': drop_off_place_id,
        'pick_up_date': pick_up_date,
        'pick_up_time': pick_up_time,
        'currency_code': currency_code,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_attraction_location(query: Annotated[str, Field(description='Names of locations, cities, districts, places, countries, counties etc.')],
                               languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/attraction/searchLocation'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_attractions(id: Annotated[str, Field(description='id can be retrieved from api/v1/attraction/searchLocation(Search Attraction Location) endpoint in Attraction collection as id inside products or destinations.')],
                       startDate: Annotated[Union[str, datetime, None], Field(description='Sort the data by the start date.')] = None,
                       endDate: Annotated[Union[str, datetime, None], Field(description='Sort the data by the end date.')] = None,
                       sortBy: Annotated[Literal['trending', 'attr_book_score', 'lowest_price', None], Field(description='This parameter orders result by trending, attr_book_score or lowest_price.')] = None,
                       page: Annotated[Union[int, float, None], Field(description='The page number. Default: 1')] = None,
                       currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                       languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                       typeFilters: Annotated[Union[str, None], Field(description='typeFilters can be retrieved from /api/v1/attraction/searchAttractions(Search Attractions) endpoint in Hotels collection. data->filterOptions-> typeFilters[]-> tagname. Note:- typeFilters should be separated by commas if passing multiple values. Example: tag1,tag2,tag')] = None,
                       priceFilters: Annotated[Union[str, None], Field(description='priceFilters can be retrieved from /api/v1/attraction/searchAttractions(Search Attractions) endpoint in Hotels collection. data->filterOptions-> priceFilters[]-> tagname. Note:- priceFilters should be separated by commas if passing multiple values. Example: tag1,tag2,tag')] = None,
                       ufiFilters: Annotated[Union[str, None], Field(description='ufiFilters can be retrieved from /api/v1/attraction/searchAttractions(Search Attractions) endpoint in Hotels collection. data->filterOptions-> ufiFilters[]-> tagname. Note:- ufiFilters should be separated by commas if passing multiple values. Example: tag1,tag2,tag')] = None,
                       labelFilters: Annotated[Union[str, None], Field(description='labelFilters can be retrieved from /api/v1/attraction/searchAttractions(Search Attractions) endpoint in Hotels collection. data->filterOptions-> labelFilters[]-> tagname. Note:- labelFilters should be separated by commas if passing multiple values. Example: tag1,tag2,tag')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/attraction/searchAttractions'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'startDate': startDate,
        'endDate': endDate,
        'sortBy': sortBy,
        'page': page,
        'currency_code': currency_code,
        'languagecode': languagecode,
        'typeFilters': typeFilters,
        'priceFilters': priceFilters,
        'ufiFilters': ufiFilters,
        'labelFilters': labelFilters,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_availability_calendar(id: Annotated[str, Field(description='id can be retrieved from api/v1/attraction/searchLocation(Search Attraction Location) endpoint in Attraction collection as id inside products or destinations.')],
                              languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/attraction/getAvailabilityCalendar'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_availability(slug: Annotated[str, Field(description='slug can be retrieved from api/v1/attraction/searchLocation(Search Attraction Location) endpoint in Attraction collection as productSlug inside products or destinations.')],
                     date: Annotated[Union[str, datetime, None], Field(description='The availability of the data.')] = None,
                     currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None,
                     languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/attraction/getAvailability'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'slug': slug,
        'date': date,
        'currency_code': currency_code,
        'languagecode': languagecode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_attraction_details(slug: Annotated[str, Field(description='slug can be retrieved from api/v1/attraction/searchLocation(Search Attraction Location) endpoint in Attraction collection as productSlug inside products or destinations.')],
                           languagecode: Annotated[Union[str, None], Field(description='To obtain the response data in a specific language, enter the languagecode. languagecode can be retrieved from api/v1/meta/getLanguages(Get Languages ) endpoint in Meta collection.')] = None,
                           currency_code: Annotated[Union[str, None], Field(description='The currency code. currency_code can be retrieved from api/v1/meta/getCurrency(Get Currency) endpoint in Hotels collection.')] = None) -> dict: 
    '''-'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/attraction/getAttractionDetails'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'slug': slug,
        'languagecode': languagecode,
        'currency_code': currency_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_attraction_reviews(id: Annotated[str, Field(description='id can be retrieved from api/v1/attraction/searchAttractions(Search Attractions) endpoint in Attraction collection as id inside products (data->products->id)')],
                           page: Annotated[Union[int, float, None], Field(description='The page number. Default: 1')] = None) -> dict: 
    '''Retrieves reviews for a specified attraction, including user ratings, comments, and review counts.'''
    url = 'https://booking-com15.p.rapidapi.com/api/v1/attraction/getAttractionReviews'
    headers = {'x-rapidapi-host': 'booking-com15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
