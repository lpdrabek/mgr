from sweather.metaweather import get_woeid


def populate_cache(redis, cities_list):
    if not redis.hgetall('cities'):
        for city in cities_list:
            city = city.lower()
            redis.hset("cities", city, get_woeid(city))
    