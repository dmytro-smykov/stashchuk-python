def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"distance to your destination is {route['distance']}"
    if ('speed' in route) and ('time' in route):
        return f"distance to your destination is {route['speed'] * route['time']}"
    return 'no distance info is available'


print(route_info({'distance': 30}))
print(route_info({'speed': 10, 'time': 3}))
print(route_info({'spee': 10}))
