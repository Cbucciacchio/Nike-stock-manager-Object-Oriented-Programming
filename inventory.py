from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
# method 1: to return the cost of the shoes.
    def get_cost(self):
        return self.cost
        
# method 2: to return the quantity of the shoes.
    def get_quantity(self):
        return self.quantity

# method 3: to returns a string representation of a class.
    def __str__(self):
        return f" Country: \t {self.country}\n Code: \t\t {self.code}\n Product: \t {self.product}\n Cost: \t\t {self.cost}\n Quantity: \t {self.quantity}\n"
        

#=============Shoe list===========
# This list will be used to store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
'''
This function will open the file inventory.txt
and read the data from this file, then create 
a shoes object with this data and append this 
object into the shoes list.
'''
def read_shoes_data():
    with open("inventory.txt", "r") as file:
        next(file)  # Skip the header line
        for line in file:
            try:
                data = line.strip().split(",")  # Since the data is comma-separated
                shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                shoe_list.append(shoe)
            except Exception as e:
                print(f"An error occurred: {e}")
    return shoe_list
    

'''
This function will allow a user to capture data
about a shoe and use this data to create a shoe 
object and append this object inside the shoe list.
'''
def capture_shoes():
    while True:
        country = input("Enter the country of the shoe: ")
        code = input("Enter the code of the shoe: ")
        product = input("Enter the product name of the shoe: ")
        cost = float(input("Enter the cost of the shoe: "))
        quantity = int(input("Enter the quantity of the shoe: "))
        
        # Create a Shoe object and append to the list
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        more_shoes = input("Do you want to enter more shoes? (yes/no): ")
        if more_shoes.lower() != "yes":
            break
            
    return shoe_list

'''
This function will iterate over the shoes 
list and print the details of the shoes 
returned from the __str__ function. 
'''
def view_all():
    table = []

    for shoe in shoe_list:
        shoe_data = [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        table.append(shoe_data)

    print(tabulate(table, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="pretty"))
    
'''
This function will find the shoe object with the lowest quantity,
which is the shoes that need to be re-stocked. Ask the user if they
want to add this quantity of shoes and then update it.
'''
def re_stock():
    min_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"The shoe with the lowest quantity is: {min_quantity_shoe}")
    answer = input("Do you want to restock this shoe? (yes/no): ")

    if answer.lower() == "yes":
        new_quantity = int(input("Enter the new quantity: "))
        min_quantity_shoe.quantity = new_quantity
        write_to_file(shoe_list)

    def write_to_file(shoes):
        with open("inventory.txt", "w") as file:
            file.write("country,code,product,cost,quantity\n")  # Writing the header
            for shoe in shoes:
                line = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                file.write(line)
        print("Inventory updated successfully.")

'''
This function will search for a shoe from 
the list using the shoe code and return 
this object so that it will be printed.
'''
def search_shoe():
    code = input("Enter the code of the shoe to search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return shoe
    print("Shoe not found.")
    return None


'''
This function will calculate the total value for each item.
Prints this information on the console for all the shoes.
'''
def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Value of {shoe.product}: {value}")

'''
Function to determine the product with the highest 
quantity and print this shoe as being for sale.
'''
def highest_qty():
    highest_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"The shoe with the highest quantity for sale is: {highest_quantity_shoe}")


#==========Main Menu=============

def main():
    while True:
        print("\n1. Load shoe data")
        print("2. Add shoe")
        print("3. View all shoes")
        print("4. Restock shoe")
        print("5. Search shoe")
        print("6. Calculate value per item")
        print("7. Find highest quantity shoe")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            read_shoes_data()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            view_all()
        elif choice == 4:
            re_stock()
        elif choice == 5:
            search_shoe()
        elif choice == 6:
            value_per_item()
        elif choice == 7:
            highest_qty()
        elif choice == 8:
            print("Closing the app....... Bye thank you!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 8.")

if __name__ == "__main__":
    main()