import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

# Create users table if it does not exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        display_name TEXT NOT NULL
    )
''')

# Create workout_posts table if it does not exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS workout_posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        favourite TEXT NOT NULL,
        routine TEXT NOT NULL,
        user_id INTEGER NOT NULL, 
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Create kitchen_posts table if it does not exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS kitchen_posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_title TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        recipe TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Insert initial admin user
cur.execute("INSERT OR IGNORE INTO users (username, password, display_name) VALUES (?, ?, ?)",
            ('admin', 'adminpass', 'Admin')
            )

connection.commit()
connection.close()
