# import sqlite3, boto3

# user_input = input()

# query = "SELECT * FROM users WHERE id=" + user_input

# print(query)

# # github-actions-demo

# # def main():
# #     print("Hello, World!")
    


# # if __name__ == "__main__":
# #     main()

from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/execute')
def insecure_endpoint():
    # SOURCE: User input from a query parameter
    user_data = request.args.get('code')
    
    # SINK: Passing unsanitized input directly into eval()
    # CodeQL will flag this as a critical Code Injection vulnerability
    result = eval(user_data) 
    
    return f"Executed: {result}"

if __name__ == '__main__':
    app.run(debug=True)