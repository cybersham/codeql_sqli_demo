import sqlite3,sys

def get_username(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def main():
    # Taking input from command line - this is untrusted external input
    user_input = sys.argv[1]  # ← CodeQL treats this as tainted source
    results = get_username(user_input)
    print(results)

if __name__ == "__main__":
    main()
