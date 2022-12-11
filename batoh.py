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
    backpack = []
    weight = 0
    itemCount = 0

    for item in sorted(items, key=lambda i: i[3], reverse=True):
        if weight + item[2] <= backpack_capacity:
            backpack.append(item)
            weight += item[2]
            itemCount += 1
    
    return backpack, weight, itemCount


def printBackpackContents(backpack):
    price = 0
    for item in backpack:
        print("Name: {0:<15} Weight: {1:<10} Price: {2}".format(item[0], item[2], item[3]))
        price += item[3]
    return price


def main():
    backpack_capacity = 3.3
    items = returnItems()
    backpack, weight, item_count = fillBackpack(items, backpack_capacity)
    price = printBackpackContents(backpack)
    print()
    print("Item count:", item_count, "\tWeight:", round(weight, 2), "\tPrice:", round(price, 2))


if __name__ == "__main__":
    main()
