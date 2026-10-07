#Sort an e-commerce catalog

names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

catalog = list(zip(names, prices, ratings))

sorted_by_price = sorted(catalog, key=lambda product: product[1], reverse = True)
sorted_by_rating = sorted(catalog, key=lambda product: product[2])

print(sorted_by_rating)
