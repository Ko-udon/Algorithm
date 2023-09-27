def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.pop(0)

    return time