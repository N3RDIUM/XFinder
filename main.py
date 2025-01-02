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
        case _:
            pass

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
        if len(_ret) == 0:
            continue
        for x in _ret:
            if x in ret:
                continue
            ret.append(x)

    return ret

possible = [eval(input("Enter initial position: "))]

i = 1
while True:
    print(f"\nRound {i}")
    possible = predict(possible, input("Enter vehicle type: "))
    print(f"Possible positions: {possible}")
    i += 1

