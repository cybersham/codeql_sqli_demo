import sqlite3

def get_username(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def main():
    user_input = "admin' OR '1'='1"
    results = get_username(user_input)
    print(results)

if __name__ == "__main__":
    main()
