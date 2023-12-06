"""
Name: Kevin Zhao
Date: 11/27/23

File: sqlClient.py

Purpose: Create a client interface for the user to access the tysql.sqlite database
"""

import sqlite3, sqlLib
from sqlite3 import Error

""" Client interface for SQLite Database """

#---------------------------- Format OrderItems Result Set ------------------------------

def OIresult(rows):
    print("{0:^14} {1:^14} {2:^15} {3:^13}".format
    ("Product ID", "Quantity", "Item Price ($)", "Tax Price ($)"))  # Print the data
                                                                    # in a table

    print("{0:14} {1:14} {2:15} {3:13}".format("-"*14, "-"*14, "-"*14, "-"*13))

    for row in rows:
        prodID = row[0]
        quant = int(row[1])
        itemPrice = float(row[2])
        taxPrice = float(row[3])

        print("{0:^14} {1:^14} {2:^15.2f} {3:^13.2f}".format
        (prodID, quant, itemPrice, taxPrice))   # Print the data in a table

#---------------------------- Gather Inputs for Product Insert --------------------------

def prodInsertInputs():
    """ Gather product input data
        Args:
            None
        Returns:
            List of the corresponding product data (pid, vendor, name, price, desc)
    """

    p = []          # Use a list to store the product information

    print("Please enter the following information:")
    pid = input("Enter the product id: ")
    p.append(pid)

    vendor = input("Enter the vendor id (BRS01, BRS02, DLL01, FRB01, JTS01): ")
    p.append(vendor)

    name = input("Enter the product name (255 characters max): ")
    p.append(name)

    price = float(input("Enter the product price: $"))
    p.append(price)

    desc = input("Enter the product description: ")
    p.append(desc)

    return(p)       # Return the product information for SQL INSERT

#---------------------------- Format Product Result Set ---------------------------------

def prodResult(rows):
    print("{0:^13} {1:^13} {2:^20} {3:^15} {4:^46}".format
    ("Product ID", "Vendor ID", "Name", "Price ($)", "Description"))    # Print the data
                                                                        # in a table

    print("{0:13} {1:13} {2:20} {3:15} {4:46}".format
    ("-"*13, "-"*13, "-"*20, "-"*15, "-"*46))

    for row in rows:
        prodID = row[0]
        vendID = row[1]
        name = row[2]
        price = float(row[3])
        desc = row[4]

        print("{0:^13} {1:^13} {2:^20} {3:^16.2f} {4:<40}".format
        (prodID, vendID, name, price, desc))                # Print the data in a table

#---------------------------- Gather Inputs for Vendor Insert ---------------------------

def vendInsertInputs():
    """ Gather vendor input data
        Args:
            None
        Returns:
            List of the corresponding vendor data (vid, name, address, city, state,
            zip, country)
    """

    v = []          # Use a list to store the vendor information

    print("Please enter the following information:")
    vid = input("Enter the vendor id (10 characters max): ")
    v.append(vid)

    name = input("Enter the vendor name (50 characters max): ")
    v.append(name)

    address = input("Enter the vendor address (50 characters max): ")
    v.append(address)

    city = input("Enter the vendor city (50 characters max): ")
    v.append(city)

    state = input("Enter the vendor state (50 characters max): ")
    v.append(state)

    zip = input("Enter the vendor zip code (10 characters max): ")
    v.append(zip)

    country = input("Enter the vendor country (50 characters max): ")
    v.append(country)

    return(v)       # Return the vendor information for SQL INSERT

#---------------------------- Format Vendor Result Set ---------------------------------

def vendResult(rows):
    print("{0:^25} {1:^20} {2:^20} {3:^13}".format
    ("Vendor Name", "Address", "City", "State"))    # Print the data in a table

    print("{0:25} {1:20} {2:20} {3:13}".format
    ("-"*25, "-"*20, "-"*20, "-"*13))

    for row in rows:
        name = row[0]
        address = row[1]
        city = row[2]
        state = row[3]

        print("{0:^25} {1:^20} {2:^20} {3:^13}".format
        (name, address, city, state))               # Print the data in a table

#---------------------------- Gather Inputs for Customer Update ------------------------

def custUpdateInputs():
    """ Gather customer input data
        Args:
            None
        Returns:
            List of the corresponding customer data (contact name, email)
    """

    c = []          # Use a list to store the customer information

    print("Please enter the following information:")
    contact = input("Enter the new customer contact name (50 characters max): ")
    c.append(contact)

    email = input("Enter the new customer email address (255 characters max): ")
    c.append(email)

    return(c)       # Return the customer information for SQL UPDATE

#---------------------------- Format Customer Result Set -------------------------------

def custResult(rows):
    print("{0:^25} {1:^25}".format
    ("Customer Contact", "Email Address"))          # Print the data in a table

    print("{0:25} {1:25}".format
    ("-"*25, "-"*25))

    for row in rows:
        contact = row[0]
        email = row[1]

        print("{0:^25} {1:^25}".format
        (contact, email))                           # Print the data in a table

#---------------------------- main() for script testing --------------------------------

def main():
    database = "tysql_copy.sqlite"                  # SQLite database to use

    conn = sqlLib.create_connection(database)       # Create a database connection

#---------------------------- Test SELECT OrderItems -----------------------------------

    #result = sqlLib.select_orderItems(conn)         # Query OrderItems
    #OIresult(result)                                # Format result

#---------------------------- Test INSERT Product --------------------------------------

    #product = prodInsertInputs()                    # Gather product information
    #rowID = sqlLib.insert_product(conn, product)    # Insert a new product row
                                                     # in table Products
    #print(rowID)

#---------------------------- Test SELECT Products -------------------------------------

    #products = sqlLib.select_products(conn)         # Query Products
    #prodResult(products)                            # Format result

#---------------------------- Test INSERT Vendor ---------------------------------------

    #vendor = vendInsertInputs()                     # Gather vendor information
    #rowID = sqlLib.insert_vendor(conn, vendor)      # Insert a new vendor row
                                                     # in table Vendors
    #print(rowID)

#---------------------------- Test SELECT Vendor ---------------------------------------

    ''' Note for next time: "OMS01" should be gathered as user input
        You want to avoid hard coding values '''
    #result = sqlLib.select_vendor(conn, "OMS01")    # Query Vendors
    #vendResult(result)                              # Format result

#---------------------------- Test UPDATE Customer -------------------------------------

    ''' Note for next time: 1000000005 should be gathered as user input
        You want to avoid hard coding values '''
    contactInfo = custUpdateInputs()                        # Gather customer contact info
    sqlLib.update_customer(conn, 1000000005, contactInfo)   # Update a customer row
                                                            # in table Customers
                                                            # with new contact info

#---------------------------- Test SELECT Customer -------------------------------------

    ''' Note for next time: 1000000005 should be gathered as user input
        You want to avoid hard coding values '''
    result = sqlLib.select_customer(conn, 1000000005)       # Query Customers
    custResult(result)                                      # Format result

#---------------------------- Call main() ----------------------------------------------

if __name__ == '__main__':
    main()