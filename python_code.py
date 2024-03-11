import pyodbc

# Database connection parameters
server = 'localhost'
database = 'InventMgmt'
username = 'sa'
password = 'Siddhu@1831'
driver = 'SQL Server'



# Connect to the database
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

try:
    # Query data from the database
    query = '''
            SELECT Customers.CustomerName, Orders.OrderDate, Items.ProductName, Orders.Quantity, Orders.UnitCost, Transactions.Amount
            FROM Orders
            INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
            INNER JOIN Items ON Orders.ItemID = Items.ItemID
            INNER JOIN Transactions ON Orders.OrderID = Transactions.OrderID
            ORDER BY Orders.OrderDate DESC;
            '''

    cursor.execute(query)

    # Fetch data and display on the screen
    print("Report:")
    print("------------------------------------------------------------")
    for row in cursor.fetchall():
        print(f"Customer: {row.CustomerName}, OrderDate: {row.OrderDate}, Product: {row.ProductName}, Quantity: {row.Quantity}, UnitCost: {row.UnitCost}, Amount: {row.Amount}")

    # Save data to a text file
    with open('report.txt', 'w') as file:
        file.write("Report:\n")
        file.write("------------------------------------------------------------\n")
        for row in cursor.fetchall():
            file.write(f"Customer: {row.CustomerName}, OrderDate: {row.OrderDate}, Product: {row.ProductName}, Quantity: {row.Quantity}, UnitCost: {row.UnitCost}, Amount: {row.Amount}\n")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
