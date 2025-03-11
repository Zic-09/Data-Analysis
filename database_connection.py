import mysql.connector
# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host="localhost", # Host name (e.g., localhost)
        user="root", # MySQL username
        password="Oluwadarasimi18", # MySQL password
        database="tutorial", # Database name
        port=3306 # Specify the custom port here if not 3306
    )
    # Check if the connection was successful
    if connection.is_connected():
        print("Connected to MySQL database.")
    else:
        print("Failed to connect to database.")


    with connection.cursor() as cursor: # Creating a cursor
        #cursor.execute("SELECT * FROM us_housing_data;") # Executing a SELECT query
        #results = cursor.fetchall() # Fetching all results
        #for row in results:
        #print(row) # Print results
        #cursor.close() # Always learn to close the cursor

        #cursor.execute("SELECT west, month FROM us_housing_data;")
        #results = cursor.fetchone()
        #if results:
        #   print(results)  # Prints the tuple (west_value, month_value)
        #else:
        #   print("No data found.")
        #connection.close()

        cursor.execute("SELECT DISTINCT month_name FROM us_housing_data;")
        results = cursor.fetchall()
        for row in results:
            print(row)
except mysql.connector.Error as e:
    print("Error:", e)
finally:
    if connection:
        connection.close()
        print("MySQL Connection Closed.")