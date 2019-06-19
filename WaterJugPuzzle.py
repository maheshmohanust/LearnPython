from _collections import defaultdict


jug1, jug2, aim = 4, 3, 2
lookup = defaultdict(lambda: False)


def find_water_level(quant1, quant2):

    if(quant1 == aim and quant2 == 0) or (quant2 == aim and quant1 == 0):
        print((quant1, quant2))
        return True
    if not lookup[(quant1, quant2)]:
        print((quant1, quant2))
        lookup[(quant1, quant2)] = True
        return (find_water_level(0, quant2) or
                find_water_level(quant1, 0) or
                find_water_level(jug1, quant2) or
                find_water_level(quant1, jug2) or
                find_water_level(quant1 + min(quant2, (jug1 - quant1)),
                                 quant2 - min(quant2, (jug1 - quant1))) or
                find_water_level(quant1 - min(quant1, (jug2 - quant2)),
                                 quant2 + min(quant1, (jug2 - quant2))))
    else:
        return False


print("Water Levels:")
find_water_level(0, 0)
