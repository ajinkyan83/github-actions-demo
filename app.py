import sqlite3, boto3

user_input = input()

query = "SELECT * FROM users WHERE id=" + user_input

print(query)

# github-actions-demo

# def main():
#     print("Hello, World!")
    


# if __name__ == "__main__":
#     main()