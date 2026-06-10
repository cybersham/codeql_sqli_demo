import sqlite3
import sys
from urllib.parse import parse_qs 

def get_username(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def main():
    if len(sys.argv) > 1:
        fake_url_input = f"user={sys.argv[1]}"
        parsed = parse_qs(fake_url_input)
        user_input = parsed['user'][0] 
        
        results = get_username(user_input)
        print(results)

if __name__ == "__main__":
    main()