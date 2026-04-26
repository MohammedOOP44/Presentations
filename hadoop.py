import mysql.connector
from mysql.connector import Error

# Initialize connection variable
connection = None

# 1. Configuration: Replace with your Cloud MySQL credentials
DB_CONFIG = {
    "host": "your_mysql_cloud_host",
    "database": "your_database_name",
    "user": "your_username",
    "password": "your_password",
    "port": 3306 # Default port for MySQL
}

try:
    # 2. Establish connection
    connection = mysql.connector.connect(**DB_CONFIG)
    
    if connection.is_connected():
        print("Successfully connected to MySQL Cloud Database!")
        cursor = connection.cursor()

        # 3. Create the Anime Table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Anime (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            score DECIMAL(3, 2),
            genre VARCHAR(100),
            episodes INT
        )
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'Anime' is ready.")

        # 4. Function to Insert a New Anime
        def insert_anime(title, score, genre, episodes):
            insert_query = "INSERT INTO Anime (title, score, genre, episodes) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (title, score, genre, episodes))
            connection.commit()
            print(f"Inserted: {title}")

        # 5. Function to Fetch and Display Data
        def fetch_animes():
            cursor.execute("SELECT * FROM Anime")
            records = cursor.fetchall()
            print("\n--- Anime List ---")
            for row in records:
                print(f"ID: {row[0]} | Title: {row[1]} | Score: {row[2]} | Genre: {row[3]} | Eps: {row[4]}")

        # Testing the functions
        insert_anime("Naruto", 8.3, "Action/Ninja", 220)
        insert_anime("Bleach", 8.2, "Action/Supernatural", 366)
        
        fetch_animes()

except Error as error:
    # This will catch and print the specific MySQL error cleanly
    print(f"Error while connecting to MySQL: {error}")

finally:
    # 6. Closing the connection safely
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("\nMySQL connection is closed.")