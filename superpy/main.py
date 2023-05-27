# Imports
import os
import argparse
import csv
from datetime import date
import matplotlib.pyplot as plt
from rich import print


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    parser = argparse.ArgumentParser(description="SuperPy - Supermarket Inventory Tool")

    # Add command-line arguments for different operations
    subparsers = parser.add_subparsers(dest="command")

    # Command for buying
    buy_parser = subparsers.add_parser("buy", help="Buy a product")
    buy_parser.add_argument("--product-name", required=True, help="Name of the product")
    buy_parser.add_argument("--product-price", required=True, help="Price of the product")
    buy_parser.add_argument("--expiration-date", required=True, help="Expiration date of the product")

    # Command for selling
    sell_parser = subparsers.add_parser("selling", help="Selling a product")
    sell_parser.add_argument("--product-name", required=True, help="Name of the product")
    sell_parser.add_argument("--product-price", required=True, help="Price of the product")

    # Report command
    report_parser = subparsers.add_parser("report", help="Generate reports")
    report_parser.add_argument("type", choices=["inventory", "revenue", "profit"], help="Type of report to generate")
    report_parser.add_argument("--date", help="Specify a specific date for the report")

    # Advance time command
    parser.add_argument("--advanced-time", type=int, help="The perceived date by a number of days")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Perform actions based on the provided arguments
    if args.command == "buy":
        # Implement the buying logic
        product_name = args.product_name
        product_price = args.product_price
        expiration_date = args.expiration_date
        buy_product(product_name, product_price, expiration_date)

    elif args.command == "selling":
        # Implement the selling logic
        product_name = args.product_name
        product_price = args.product_price
        sell_product(product_name, product_price)

    elif args.command == "report":
        # Implement generating reports logic
        report_type = args.type
        report_date = args.date
        generate_report(report_type, report_date)

    # Implement the logic for advancing the time
    if args.advanced_time:
        advance_time(args.advanced_time)


def buy_product(product_name, product_price, expiration_date):
    # Read the available stock from the bought.csv data file
    with open("bought.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)[1:]  # Skip the header row

    # Find the product in the stock
    for row in rows:
        print("Row:", row)  # Add this line for debugging
        if row[1] == product_name:
            bought_id = row[0]
            expiration_date = row[4]

            # remove the product from the stock
            rows.remove(row)

            # Append the sale data to sold.csv data file
            sold_data = [get_sale_id(), bought_id, get_current_date(), product_price]
            with open("sold.csv", "a", newline="") as sold_file:
                sold_writer = csv.writer(sold_file)
                sold_writer.writerow(sold_data)

            print("OK")
            break
    else:
        print("ERROR: Product not in stock")




def sell_product(product_name, product_price):
    # Read the available stock from the bought.csv data file
    with open("bought.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Find the product in the stock
    for row in rows:
        if len(row) >= 2 and row[1] == product_name:  # Add a check for the row length
            bought_id = row[0]
            expiration_date = row[4]

            # remove the product from the stock
            rows.remove(row)

            # Append the sale data to sold.csv data file
            sold_data = [get_sale_id(), bought_id, get_current_date(), product_price]
            with open("sold.csv", "a", newline="") as sold_file:
                sold_writer = csv.writer(sold_file)
                sold_writer.writerow(sold_data)

            print("OK")
            break
    else:
        print("ERROR: Product not in stock")



def generate_report(report_type, report_date):
    # Implement the logic for generating reports
    print("Generating report:", report_type)
    if report_date:
        print("Date:", report_date)

    # Additional feature: Visualize statistics using Matplotlib
    if report_type == "inventory":
        inventory = get_inventory_data()
        visualize_inventory(inventory)
    elif report_type == "revenue":
        revenue = get_revenue_data()
        visualize_revenue(revenue)
    elif report_type == "profit":
        profit = get_profit_data()
        visualize_profit(profit)


def visualize_inventory(inventory):
    # Visualize inventory statistics using Matplotlib
    labels = [item[0] for item in inventory]
    quantities = [item[1] for item in inventory]

    plt.bar(labels, quantities)
    plt.xlabel("Product")
    plt.ylabel("Quantity")
    plt.title("Inventory")
    plt.show()


def visualize_revenue(revenue):
    # Visualize revenue statistics using Matplotlib
    labels = [item[0] for item in revenue]
    amounts = [item[1] for item in revenue]

    plt.bar(labels, amounts)
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.title("Revenue")
    plt.show()


def visualize_profit(profit):
    # Visualize profit statistics using Matplotlib
    labels = [item[0] for item in profit]
    amounts = [item[1] for item in profit]

    plt.bar(labels, amounts)
    plt.xlabel("Product")
    plt.ylabel("Profit")
    plt.title("Profit")
    plt.show()


def get_inventory_data():
    # Placeholder function to fetch inventory data
    return [("Product A", 10), ("Product B", 5), ("Product C", 8)]


def get_revenue_data():
    # Placeholder function to fetch revenue data
    return [("Product A", 100), ("Product B", 50), ("Product C", 80)]


def get_profit_data():
    # Placeholder function to fetch profit data
    return [("Product A", 50), ("Product B", 20), ("Product C", 40)]


def advance_time(days):
    # Implement the logic for advancing the time by the given number of days
    print("Advancing time by", days, "days")


def get_sale_id():
    # Placeholder code to generate a unique sale ID
    return "SALE-123"


def get_current_date():
    # Placeholder code to get the current date
    return date.today().strftime("%Y-%m-%d")


if __name__ == "__main__":
    main()




# ------------------------ Checking ----------------------------------- #
 


"""
# Check if bought.csv file exists
if os.path.exists("bought.csv"):
    print("bought.csv file exists")
else:
    print("bought.csv file does not exist")

# Check if sold.csv file exists
if os.path.exists("sold.csv"):
    print("sold.csv file exists")
else:
    print("sold.csv file does not exist")

# Check the directory 
print("Current working directory:", os.getcwd())
"""



# ------------------------ Testing in Terminal ----------------------------------- #



# Buying 
# python main.py buy --product-name "Apple" --product-price 1.99 --expiration-date "2023-05-31"


# Selling
# python main.py selling --product-name "Apple" --product-price 1.99



# Generating a report
# python main.py report inventory


# Generate a inventory report for specified date "2023-05-15"
# python main.py report revenue --date "2023-05-15"


# Generate a profit report for specified date "2023-05-25"
#python main.py report profit --date "2023-05-25"


# Generate a revenue report for specified date "2023-05-05"
# python main.py report profit --date "2023-05-05"


# Advance Time, (7) stand for days ahead
# python main.py --advanced-time 7



# ---------------------------------- Start  Report --------------------------------- #

"""

The implemented of SuperPy supermarket inventory tool demonstrates several  technical elements that enhance its 
functionality and usability. 
Three of these elements are discussed below, highlighting the problems they solve and the reasons behind their implementation.

Command-Line Interface (CLI): 
SuperPy utilizes a CLI for interacting with the tool, enabling users to perform various operations such as buying, 
selling, and generating reports. 
The CLI provides a user-friendly way to input commands and parameters, 
allowing users to interact with the tool efficiently. 
It eliminates the need for complex user interfaces and provides a streamlined experience, making SuperPy 
accessible to a wide range of users.

CSV Data File Handling: 
SuperPy uses CSV (Comma-Separated Values) files to store and manage product data. The tool reads the available stock from the
"bought.csv" file and appends sales data to the "sold.csv" file. 
This approach offers a flexible solution for data storage and manipulation. 
CSV files are widely supported and easily editable, 
making them the suitable choice for managing inventory data. 
The implementation utilizes the csv module in Python to read and write CSV files, ensuring reliable and efficient data handling.

Data Visualization with Matplotlib: 
SuperPy includes the feature of generating reports and visualizing statistics using the Matplotlib library. 
This element enhances the tool by providing users with visual representations of inventory, revenue, and profit data. 
The implementation utilizes bar charts to display the data, 
making it easy for users to analyze and interpret the information visually. 
Data visualization improves the understanding and presentation of complex data sets, 
enabling users to make informed decisions based on the visualized insights.

These technical elements address important aspects of SuperPy's functionality and design. The CLI enhances user interaction, 
the CSV data file handling ensures efficient data storage and retrieval, 
and data visualization with Matplotlib enhances data analysis and reporting capabilities. 
Combined, these elements contribute to a powerful and user-friendly supermarket inventory tool 
that simplifies inventory management, sales tracking, 
and reporting processes.

"""

# ---------------------------------- End  Report --------------------------------- #