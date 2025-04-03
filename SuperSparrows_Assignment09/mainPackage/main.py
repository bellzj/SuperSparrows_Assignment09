#main.py
# File Name : main.py
# Student Name: Nogaye Gueye, Zach Bell, Abel Yemaneab
# email:  yemaneag@mail.uc.edu, gueyene@mail.uc.edu, bellzj@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   04/03/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment has us learn how to manipulate data from a sql server

# Brief Description of what this module does. This module teaches us to utilize outside coding libraries.
# Citations: https://stackoverflow.com/questions/44149394/select-a-random-row-from-the-table-using-python/44149478#44149478, https://stackoverflow.com/questions/55021558/randomly-choose-rows-from-table-python-pandas-read-sql
from dataPackage.data import *
import random

# make instance of GroceryStoreDB
Store = GroceryStoreDB()
# Fetch product data
products = Store.fetch_products()

if products:
    # Randomly select a product
    selected_product = random.choice(products)

    # Store values in variables
    product_id = selected_product["ProductID"]
    description = selected_product["Description"]
    manufacturer_id = selected_product["ManufacturerID"]
    brand_id = selected_product["BrandID"]

    # Fetch Manufacturer Name
    manufacturer_name = Store.fetch_manufacturer_name(manufacturer_id)

    # Fetch Brand Name
    brand_name = Store.fetch_brand_name(brand_id)  # Assuming you have a function for this

    # Fetch Number of Items Sold
    number_of_items_sold = Store.fetch_number_of_items_sold(product_id)

    # Construct the sentence
    output_sentence = (
        f"The product '{description}', manufactured by {manufacturer_name} under the brand {brand_name}, "
        f"has sold a total of {number_of_items_sold} units."
    )

    # Print the final sentence
    print(output_sentence)

