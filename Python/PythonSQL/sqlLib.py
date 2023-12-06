"""
Name: Kevin Zhao
Date: 11/27/23

File: sqlLib.py

Purpose: Create a library of SQL functions to access the tysql.sqlite database
"""

import sqlite3
from sqlite3 import Error

""" Library of functions for SQLite tutorial """

def create_connection(db):
    """ Create a connection to your SQLite database
        Args:
            param1: db = the database filename
        Returns:
            connection object or None if unable to connect
    """

    try:
        conn = sqlite3.connect(db)  # Create connection & return it
        print("Database connection established")
        return conn
    except Error as e:              # If error, print it
        print(e)
    
    return None

#--------------------------------------------------------------------------------

def select_orderItems(conn):
    """ Query: prod_id, quantity, item_price, calculated tax price from
        OrderItems

        Args:
            param1: conn = the connection object
        Returns:
            the queried data
    """
    cur = conn.cursor()     # Create cursor to store the result set to
                            # Allows you to move forward or backward through the
                            # result row by row
    cur.execute('''SELECT prod_id, quantity, item_price, quantity * item_price
                * 1.07 AS 'taxed_price(7%)' FROM OrderItems WHERE order_num = 
                20006;''')
    
    rows = cur.fetchall()   # Fetches all (or remaining) rows of query result
                            # and returns a list of tuples
    cur.close()
    return (rows)

#--------------------------------------------------------------------------------

def insert_product(conn, product):
    """ Add a product to the Products table
        Args:
            param1: conn = connection object for SQL database
            param2: product = a list containing the product info for
                              insertion into table Products
        Returns:
            rowID of last successful insert 
    """

    sql = ''' INSERT INTO Products(prod_id, vend_id, prod_name, prod_price,
              prod_desc) VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, product)
    conn.commit()               # Commit table updates to finalize them
    cur.close()
    return cur.lastrowid

#--------------------------------------------------------------------------------

def select_products(conn):
    """ Query: prod_id, vendor, name, price, description FROM Products
        Args:
            param1: conn = the connection object
        Returns:
            the queried data
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Products;")

    rows = cur.fetchall()   # Fetches all (or remaining) rows of query result
                            # and returns a list of tuples
    cur.close()
    return (rows)

#--------------------------------------------------------------------------------

def insert_vendor(conn, vendor):
    """ Add a vendor to the Vendors table
        Args:
            param1: conn = connection object for SQL database
            param2: vendor = a list containing the vendor info for
                             insertion into table Vendors
        Returns:
            rowID of last successful insert 
    """

    sql = ''' INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city,
              vend_state, vend_zip, vend_country) VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, vendor)
    conn.commit()               # Commit table updates to finalize them
    cur.close()
    return cur.lastrowid

#--------------------------------------------------------------------------------

def select_vendor(conn, vendorID):
    """ Query: name, address, city, state FROM Vendors
        Args:
            param1: conn = the connection object
            param2: vendorID = indicates target vendor for the query 
        Returns:
            the queried data
    """

    sql = ''' SELECT vend_name, vend_address, vend_city, vend_state
              FROM Vendors WHERE vend_id = ?; '''
    cur = conn.cursor()
    cur.execute(sql, [vendorID])    # Execute expects tuple as a parameter so
                                    # write the parameter as (vendorID,)
                                    # Using a list is also fine since it will be
                                    # automatically converted into a tuple

    rows = cur.fetchall()   # Fetches all (or remaining) rows of query result
                            # and returns a list of tuples
    cur.close()
    return (rows)

#--------------------------------------------------------------------------------

def update_customer(conn, custID, contactInfo):
    """ Update customer contact info for a specific customer id in Customers
        Args:
            param1: conn = connection object for SQL database
            param2: custID = indicates customer to update
            param3: contactInfo = a list containing the new customer contact name
                                  and email address
        Returns:
            None
    """

    sql = ''' UPDATE Customers SET cust_contact = ?, cust_email = ? WHERE
              cust_id = ?; '''
    cur = conn.cursor()
    cur.execute(sql, contactInfo + [custID])
    conn.commit()               # Commit table updates to finalize them
    cur.close()

#--------------------------------------------------------------------------------

def select_customer(conn, customer):
    """ Query: contact, email FROM Vendors
        Args:
            param1: conn = the connection object
            param2: customer = customer ID indicating target customer for the query 
        Returns:
            the queried data
    """

    sql = "SELECT cust_contact, cust_email FROM Customers WHERE cust_id = ?;"
    cur = conn.cursor()
    cur.execute(sql, [customer])

    rows = cur.fetchall()   # Fetches all (or remaining) rows of query result
                            # and returns a list of tuples
    cur.close()
    return (rows)