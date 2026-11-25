# Lab: Delivery Route Planner

An adapted version of the freeCodeCamp lab "Build a Travel Weather Planner". I kept the same logic and the same conditional statements, but changed the scenario and the variable names. The program decides whether a package can be delivered, based on the weather, the distance of the route and the delivery vehicles available.

## What changed from the original lab

| Original lab | This version |
|--------------|--------------|
| Commuting to a destination | Delivering a package |
| `distance_mi` (miles) | `route_km` (kilometers) |
| `is_raining` | `is_storm` |
| `has_bike` | `has_scooter` |
| `has_car` | `has_van` |
| `has_ride_share_app` | `has_courier_app` |

The distance limits (`1` and `6`) and the whole structure of the conditions are exactly the same.

> Note: the freeCodeCamp lab tests look for the original variable names, so they would not pass with these renamed variables. This version is for my own practice and for this repo. The original solution with the lab's variable names is the one to submit on freeCodeCamp.

## Topics practiced

| Topic | Where it is used |
|-------|------------------|
| Number and boolean variables | `route_km`, `is_storm`, `has_scooter`, `has_van`, `has_courier_app` |
| `if`, `elif` and `else` | Checking the route categories in ascending order |
| Nested `if` statements | A weather or vehicle check inside each distance category |
| Comparison operators | `route_km <= 1`, `route_km <= 6`, `route_km > 6` |
| Boolean operators `and`, `or`, `not` | `has_scooter and not is_storm`, `has_van or has_courier_app` |
| Truthy and falsy values | `if not route_km` treats `0` as "no route" |
| `print()` | Displaying `True` or `False` as the result |

## The rules

1. If `route_km` is falsy (`0`), print `False`.
2. If the route is 1 km or less, print `True` only if there is no storm. Otherwise print `False`.
3. If the route is more than 1 km and up to 6 km, print `True` only if there is a scooter and no storm. Otherwise print `False`.
4. If the route is more than 6 km, print `True` if there is a van or a courier app. Otherwise print `False`.

## Files

| File | Description |
|------|-------------|
| `delivery_route_planner.py` | The program |
| `README.md` | Notes on how the program works (this file) |

## How to run

```
python delivery_route_planner.py
```

## My values and output

```python
route_km = 4.5
is_storm = False
has_scooter = True
has_van = False
has_courier_app = False
```

```
True
```

The route is 4.5 km, which is more than 1 and up to 6, so the program needs a scooter and no storm. There is a scooter and no storm, so the result is `True`.

---

## The program

```python
route_km = 4.5
is_storm = False
has_scooter = True
has_van = False
has_courier_app = False

if not route_km:
    print(False)

elif route_km <= 1:
    if not is_storm:
        print(True)
    else:
        print(False)

elif route_km <= 6:
    if has_scooter and not is_storm:
        print(True)
    else:
        print(False)

elif route_km > 6:
    if has_van or has_courier_app:
        print(True)
    else:
        print(False)
```

## How it works

### The route categories

| Route length | Condition checked | Prints `True` when |
|--------------|-------------------|--------------------|
| `0` (falsy) | `not route_km` | Never. Always prints `False` |
| 1 km or less | `route_km <= 1` | There is **no** storm |
| More than 1, up to 6 km | `route_km <= 6` | There is a scooter **and** no storm |
| More than 6 km | `route_km > 6` | There is a van **or** a courier app |

### Why the order matters

The branches are checked from top to bottom, and **only the first true branch runs**. Because they go in **ascending order**, a branch like `route_km <= 6` does not need to say "greater than 1". By the time Python reaches it, the earlier branch (`<= 1`) has already been ruled out.

### The falsy check comes first

`if not route_km` is true when `route_km` is `0`, a falsy value. It goes first so that a route of `0` never reaches the other branches.

### The boolean operators

- `not is_storm` is true when there is **no** storm.
- `has_scooter and not is_storm` needs **both** parts to be true.
- `has_van or has_courier_app` needs **at least one** part to be true.

---

## Testing every scenario

I tested the program by changing the variables and checking each result.

| Route (km) | Storm | Scooter | Van | Courier app | Prints | Why |
|------------|-------|---------|-----|-------------|--------|-----|
| `0` | No | Yes | Yes | Yes | `False` | Falsy route |
| `0.5` | No | No | No | No | `True` | Short route, no storm |
| `0.5` | Yes | No | No | No | `False` | Short route, storm |
| `1` | No | No | No | No | `True` | Exactly 1 km is included |
| `1` | Yes | Yes | Yes | Yes | `False` | Storm stops the delivery |
| `3` | Yes | No | No | No | `False` | Storm and no scooter |
| `3` | No | No | No | No | `False` | No storm but no scooter |
| `3` | No | Yes | No | No | `True` | Scooter and no storm |
| `3` | Yes | Yes | No | No | `False` | Scooter but storm |
| `6` | No | Yes | No | No | `True` | Exactly 6 km is included |
| `6.5` | No | No | Yes | No | `True` | Long route with a van |
| `8` | Yes | No | No | Yes | `True` | Long route with a courier app |
| `8` | No | No | No | No | `False` | Long route and no vehicle |
