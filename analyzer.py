sales_dict = {}
rev_dict = {}
filename = input("Enter the name of the sales data file (e.g., sales_data.txt): ")
if not filename.endswith(".txt"):
            print("Please provide a .txt file.")
            exit()

def revenue():
    revs = []
    for key, value in sales_dict.items():
        revenue = value[0] * value[1]
        revs.append(revenue)
        if key not in rev_dict:
            rev_dict[key] = revenue
    total_revenue = sum(revs)
    return f"The total revenue is Rp.{total_revenue:,.2f}"

def product_revenue(name):
    name = name.lower()
    for product in rev_dict:
        if product.lower() == name:
            return f"{product} has a revenue of Rp.{rev_dict[product]:,.2f}"
    return "Product not found."


try:
    with open(filename, 'r') as file:

        lines = file.readlines()
        for line in lines:
            line = line.strip().split(",")
            if line[0] == "Product":
                continue
            try:
                product = line[0]
                units = int(line[1])
                price = float(line[2])
                if product not in sales_dict:
                    sales_dict[product] = (units, price)
            except ValueError:
                print(f"Invalid data in line: {line}")
except FileNotFoundError:
    print(f"File {filename} not found.")
    exit()


print(sales_dict)
print(revenue())


while True:
    option = input("Do you want to get revenue of a product? (y/n): ").lower()
    if option == "y":
        name = input("Enter a product name to get revenue: ")
        print(product_revenue(name))
    elif option == "n":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter only 'y' or 'n'.")
