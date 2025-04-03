# data.py

import pyodbc

class GroceryStoreDB:
    def __init__(self):
        """Initialize and establish a connection to the database."""
        self.conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )
    
    def fetch_products(self):
        """Fetch product data from tProduct and return a list of dictionaries."""
        cursor = self.conn.cursor()

        query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
        cursor.execute(query)

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.close()
        return results
    
    def fetch_manufacturer_name(self, manufacturer_id):
        """Fetch Manufacturer name using ManufacturerID and return the name."""
        cursor = self.conn.cursor()

        query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
        cursor.execute(query)

        manufacturer = cursor.fetchone()

        cursor.close()
        return manufacturer[0] if manufacturer else None
    
    def fetch_brand_name(self, brand_id):
        """Fetch Brand name using BrandID and return the name."""
        cursor = self.conn.cursor()

        query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
        cursor.execute(query)

        brand = cursor.fetchone()

        cursor.close()
        return brand[0] if brand else None
    
    def fetch_number_of_items_sold(self, product_id):
        """Fetch the number of items sold for a given ProductID."""
        cursor = self.conn.cursor()

        query = f"""
        SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
        FROM dbo.tTransactionDetail
        INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
        WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = {product_id})
        """

        cursor.execute(query, (product_id,))
        result = cursor.fetchone()

        cursor.close()

        return result[0] if result and result[0] is not None else 0

