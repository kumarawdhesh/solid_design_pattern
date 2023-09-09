# Single Responsibility Principle (SRP)

"""
This principle states that a class should have only one reason to change, 
meaning it should have a single responsibility or job. In Python, 
you can achieve this by designing classes and functions that have a clear and specific purpose.

Example in Python:
In this example, the User class has two responsibilities: saving to the database and sending emails. 
To adhere to SRP, you could separate these responsibilities into different classes or functions.
"""


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_to_database(self):
        # Code to save the user to the database

    def send_email(self, message):
        # Code to send an email
        pass
