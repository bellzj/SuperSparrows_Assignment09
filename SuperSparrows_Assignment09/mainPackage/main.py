#main.py

from dataPackage import Zach
import random

# Fetch product data
products = Zach.fetch_products()

if products:
    # Randomly select a product
    selected_product = random.choice(products)

    # Store values in variables
    product_id = selected_product["ProductID"]
    description = selected_product["Description"]
    manufacturer_id = selected_product["ManufacturerID"]
    brand_id = selected_product["BrandID"]

    # Fetch Manufacturer Name
    manufacturer_name = Zach.fetch_manufacturer_name(manufacturer_id)

    # Fetch Brand Name
    brand_name = Zach.fetch_brand_name(brand_id)  # Assuming you have a function for this

    # Fetch Number of Items Sold
    number_of_items_sold = Zach.fetch_number_of_items_sold(product_id)

    # Construct the sentence
    output_sentence = (
        f"The product '{description}', manufactured by {manufacturer_name} under the brand {brand_name}, "
        f"has sold a total of {number_of_items_sold} units."
    )

    # Print the final sentence
    print(output_sentence)

