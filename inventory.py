from tabulate import tabulate

#========The beginning of the class==========
class Shoe:
    """
    A class to represent a Shoe.

    Attributes
    ----------
    country : str
        The country of the shoe
    code : str
        The code of the shoe
    product : str
        The name of the product
    cost : float
        The cost of the shoe
    quantity : int
        The quantity of the shoe
    """

    def __init__(self, country, code, product, cost, quantity):
        """Initializes the Shoe with provided values."""

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        """Return the cost of the Shoe."""
        return self.cost
        
    def get_quantity(self):
        """Return the quantity of the Shoe."""
        return self.quantity

    def __str__(self):
        """
        Returns a string representation of a Shoe with all attributes.
        
        Returns
        -------
        str
            a formatted string with all the Shoe attributes
        """
        return f" Country: \t {self.country}\n Code: \t\t {self.code}\n Product: \t {self.product}\n Cost: \t\t {self.cost}\n Quantity: \t {self.quantity}\n"
        

#=============Shoe list===========
# This list will be used to store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
def write_to_file(shoes):
    """
    Writes the updated inventory information to the file.
    """
    try:
        with open("inventory.txt", "w") as file:
            file.write("country,code,product,cost,quantity\n")  # Writing the header
            for shoe in shoes:
                line = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                file.write(line)
        print("Inventory updated successfully.")
    except FileNotFoundError:
        print("Could not find the file to write to. Please check the file path and try again.")       
        
        
def read_shoes_data():
    """
    Open the file inventory.txt and read the data from it.
    
    The function creates a Shoe object with the read data and appends 
    this object into the shoes list.
    """
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header line
            for line in file:
                try:
                    data = line.strip().split(",")  # Since the data is comma-separated
                    shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                    shoe_list.append(shoe)
                except Exception as e:
                    print(f"An error occurred: {e}")
        print("Stock has been loaded from file.")
    except FileNotFoundError:
        print("Could not find the file to read from. Please check the file path and try again.")
    return shoe_list
    

def capture_shoes():
    """
    Allows a user to capture data about a shoe.
    The function creates a Shoe object with the provided data 
    and appends this object into the shoe list.
    """
    more_shoes = "yes"
    while more_shoes.lower() == "yes":
        country = input("Enter the country of the shoe: ")
        code = input("Enter the code of the shoe: ")
        product = input("Enter the product name of the shoe: ")
        cost = float(input("Enter the cost of the shoe: "))
        quantity = int(input("Enter the quantity of the shoe: "))

        # Create a Shoe object and append to the list
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        more_shoes = input("Would you like to capture another shoe in the inventory? (yes/no): ")
            
    return shoe_list

 
def view_all():
    """
    Iterates over the shoes list and prints the details of the shoes.
    """
    table = []

    for shoe in shoe_list:
        shoe_data = [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        table.append(shoe_data)

    print(tabulate(table, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="pretty"))
    

def re_stock():
    """
    Finds the Shoe object with the lowest quantity in the shoe_list.
    Asks the user if they want to add this quantity of shoes and updates it.
    """
    min_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"The shoe with the lowest quantity is: {min_quantity_shoe}")
    answer = input("Do you want to restock this shoe? (yes/no): ")

    if answer.lower() == "yes":
        new_quantity = int(input("Enter the new quantity: "))
        min_quantity_shoe.quantity = new_quantity
        write_to_file(shoe_list)


def search_shoe():
    """
    Searches for a Shoe in the list using the shoe code and returns this object.
    """
    code = input("Enter the code of the shoe to search: ").upper()
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return shoe
    print("Shoe not found.")
    return None


def value_per_item():
    """
    Calculates the total value for each Shoe item in the list.
    
    Prints this information on the console for all the shoes.
    """
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Value of {shoe.product}: {value}")


def highest_qty():
    """
    Determines the Shoe with the highest quantity in the shoe_list.
    Prints this shoe as being for sale.
    """
    highest_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.get_quantity())
    print(f"Advert: The shoe with the highest quantity for sale is:\n{highest_quantity_shoe}")


#==========Main Menu=============

def main():
    """
    Handles the main loop of the program. Provides an interface for user interaction.
    """
    choice = 0
    while choice != 8:
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
        elif choice in range(3, 8) and not shoe_list:
            print("Please load the data before performing this action.")
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
            print("Closing the app..............Bye thank you!")
        else:
            print("Invalid choice. Please choose a number between 1 and 8.")

if __name__ == "__main__":
    main()
