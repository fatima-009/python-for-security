# Delivery Route Planner
# Decides whether a package can be delivered, based on the weather,
# the distance of the route and the delivery vehicles available.

route_km = 4.5
is_storm = False
has_scooter = True
has_van = False
has_courier_app = False

# A route of 0 (falsy) means there is nowhere to deliver
if not route_km:
    print(False)

# Up to 1 km: a delivery on foot works if there is no storm
elif route_km <= 1:
    if not is_storm:
        print(True)
    else:
        print(False)

# More than 1 km, up to 6 km: a scooter works if there is no storm
elif route_km <= 6:
    if has_scooter and not is_storm:
        print(True)
    else:
        print(False)

# More than 6 km: a van or a courier app is needed
elif route_km > 6:
    if has_van or has_courier_app:
        print(True)
    else:
        print(False)