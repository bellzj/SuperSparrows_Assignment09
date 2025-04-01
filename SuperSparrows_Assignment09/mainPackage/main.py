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

