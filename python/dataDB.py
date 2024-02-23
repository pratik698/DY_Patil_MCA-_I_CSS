import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database_name"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define a SQL query to create a table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT
    )
'''

# Execute the query to create the table
cursor.execute(create_table_query)

# Insert some data into the table
user_data = [('Alice', 30),
             ('Bob', 25),
             ('Charlie', 35)]

# Insert data into the table
insert_query = 'INSERT INTO users (name, age) VALUES (%s, %s)'
cursor.executemany(insert_query, user_data)

# Commit changes to the database
conn.commit()

# Select data from the table
cursor.execute('SELECT * FROM users')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Display the rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
