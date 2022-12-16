import itertools
import random

def returnItems():
    items = [        
        ["Eggs", "dairy", 0.3, 28.1],
        ["Stawberry", "fruit", 0.2, 29.45],
        ["Asparagus", "vegetable", 0.4, 18.95],
        ["Cheese", "dairy", 0.7, 17.68],
        ["Legums", "vegetable", 0.5, 17.11],
        ["Baking cake", "dairy", 0.9, 11.14],
        ["Tomato", "vegetable", 0.3, 18.19],
        ["Hazelnut", "vegetable", 0.8, 27.35],
        ["Lemon", "fruit", 0.5, 15.79],
        ["Bread", "bakery", 1.1, 17.48],
        ["Fries", "bakery", 0.7, 18.32],
        ["Sandwich", "bakery", 1.0, 18.5],
        ["Yogurt", "dairy", 0.8, 27.61],
    ]

    return random.sample(items, 8)


def fillBackpack(items, backpack_capacity):
    max_price = 0
    best_combination = []

    items.sort(key=lambda x: x[3]/x[2], reverse=True)

    for r in range(1, len(items)+1):
        for combination in itertools.combinations(items, r):
            weight = sum([item[2] for item in combination])
            price = sum([item[3] for item in combination])

            classes_in_backpack = set()
            include_combination = True
            for item in combination:
                if item[1] in classes_in_backpack:
                    include_combination = False
                    break
                else:
                    classes_in_backpack.add(item[1])

            if weight <= backpack_capacity and price > max_price and include_combination:
                max_price = price
                best_combination = combination

    return best_combination, max_price


def printBackpackContents(backpack):
    price = 0
    for item in backpack:
        print("Name: {0:<10} Class: {1:<10} Weight: {2:<5} Price: {3}".format(item[0], item[1], item[2], item[3]))
        price += item[3]
    return price


def main():
    backpack_capacity = 0.9
    items = returnItems()
    backpack, price = fillBackpack(items, backpack_capacity)
    price = printBackpackContents(backpack)
    print()
    print("Total price:", round(price, 2))


if __name__ == "__main__":
    main()
