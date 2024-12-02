jug1, jug2, aim = 4, 3, 2
visited = set()

def water(amt1, amt2):
    if (amt1, amt2) in visited:
        return False
    if amt1 == aim or amt2 == aim:
        print(amt1, amt2)
        return True
    print(amt1, amt2)
    visited.add((amt1, amt2))
    return (water(0, amt2) or
            water(amt1, 0) or
            water(jug1, amt2) or
            water(amt1, jug2) or
            water(amt1 + min(amt2, jug1 - amt1), amt2 - min(amt2, jug1 - amt1)) or
            water(amt1 - min(amt1, jug2 - amt2), amt2 + min(amt1, jug2 - amt2)))

print("Steps:")
water(0, 0)
