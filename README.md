# Nike Stock Manager Capstone project (OOP)

## Overview
The Nike-stock-manager-Object-Oriented-Programming is a Python application developed to optimize the stock taking and management process in a Nike warehouse. Serving as an efficient warehouse management system, this software facilitates store managers in various regions to keep track of the stock, manage shoe items, and generate various reports and statistics.

## Features
- Load Shoe Data: Retrieve shoe data from an inventory.txt file to get a list of all shoe items available.
- Add Shoe: Enter the details of a new shoe item to the inventory.
- View All Shoes: Display the list of all shoe items in a tabular format.
- Restock Shoe: Identify the shoe with the lowest stock and facilitate its restocking.
- Search Shoe: Look up a particular shoe in the inventory using its unique code.
- Calculate Value Per Item: Determine the total value of each shoe item by multiplying its cost with its quantity.
- Find Highest Quantity Shoe: Identify and display the shoe with the highest quantity in stock.

## How to Use
1. Ensure you have Python installed on your machine.
2. Clone/download the script to your local machine.
3. Run the script in a Python environment.
4. Navigate through the main menu by selecting the respective options (1 to 8).
5. For options that require input, follow the on-screen prompts.


## Technologies Used
- Python: The primary programming language used for developing the application.
- tabulate: A Python library used to render a list of dictionaries as a table in various formats.

## Code Overview
The software employs the concept of Object-Oriented Programming. The Shoe class is defined with attributes like country, code, product, cost, and quantity. This class is responsible for managing individual shoe items.

Several functions are defined outside the class, handling operations like reading shoe data from a file, capturing shoe details, viewing all shoes, restocking shoes, and more. The main() function at the bottom provides a menu-driven interface for users to interact with the system.

The inventory.txt file is used to store the shoe data persistently. Each time data is loaded or modified, this file is accessed to ensure the data stays updated between sessions.

Note: Always ensure you have a backup of your inventory.txt file, as the application will overwrite it during certain operations.
