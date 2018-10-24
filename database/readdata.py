import csv

ACCEPTED_MSG = """
 Brand: {}
"""

csv_file = open('products.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

for row in csv_reader:
    ProductId, Category, Brand, Name, In_stock_number, Price = row
    print(ProductId, Category, Brand, Name, In_stock_number, Price)

    if Brand == "Pantene":
        print(ACCEPTED_MSG);
csv_file.close()
