from board import (taxi, bus, underground, river)

print("Scotland Yard - The Pythonic Way")

def _predict(position: int, vehicle: str) -> list[int]:
    ret = []
    paths = []

    match vehicle:
        case "taxi":
            paths = taxi
        case "bus":
            paths = bus
        case "underground":
            paths = underground
        case "concealed":
            paths = taxi + bus + underground + river

    for pair in paths:
        pair = list(pair)
        if position in pair:
            index = bool(pair.index(position))
            if pair[int(not index)] in ret:
                continue
            ret.append(pair[int(not index)])

    return ret

def predict(positions: list[int], vehicle: str) -> list[int]:
    ret = []

    for position in positions:
        _ret = _predict(position, vehicle)
        for x in _ret:
            if x in ret:
                continue
            ret.append(x)

    return ret

possible = [42]

for i in range(42):
    print(f"\nchance {i}")
    possible = predict(possible, "taxi")
    print(possible)

"""
TODO: Reject possible positions where the 
requested vehicle is not available to 
narrow down on Mr. X

So, you need to make the thing interactive.
Use input() first. If it is successful,
make a flask web app.
"""

