#Zach.py
import pyodbc
import random

def connect_to_database():
    """Connect to SQL Server instance and return connection object."""
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
        'Database=GroceryStoreSimulator;'
        'uid=IS4010Login;'
        'pwd=P@ssword2;'
    )
    return conn

def fetch_products():
    """Fetch product data from tProduct and return a list of dictionaries."""
    conn = connect_to_database()
    cursor = conn.cursor()

    query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
    cursor.execute(query)

    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return results

def fetch_manufacturer_name(manufacturer_id):
    """Fetch Manufacturer name using ManufacturerID and return the name."""
    conn = connect_to_database()
    cursor = conn.cursor()

    query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
    cursor.execute(query)

    manufacturer = cursor.fetchone()

    cursor.close()
    conn.close()

    return manufacturer[0] if manufacturer else None

def fetch_brand_name(brand_id): #Abel
    """Fetch Brand name using BrandID and return the name."""
    conn = connect_to_database()
    cursor = conn.cursor()

    query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
    cursor.execute(query)

    brand = cursor.fetchone()

    cursor.close()
    conn.close()

    return brand[0] if brand else None

def fetch_number_of_items_sold(product_id):
    """Fetch the number of items sold for a given ProductID."""
    conn = connect_to_database()
    cursor = conn.cursor()

    query = f"""
    SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
    FROM dbo.tTransactionDetail
    INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
    WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = {product_id})
    """
    
    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0] if result and result[0] is not None else 0

