# PROJECT DESCRIPTION
The Expense Tracking System is a Python-based project designed to facilitate the management and tracking of financial expenses. The project adopts object-oriented programming (OOP) principles, consisting of two main classes: Expense and ExpenseDatabase.

THE Expense CLASS 

Attributes
id: A universally unique identifier (UUID) string, automatically generated for each expense.
title: A string representing the title or description of the expense.
amount: A float indicating the monetary value of the expense.
created_at: A timestamp representing the date and time when the expense was created in Coordinated Universal Time (UTC).
updated_at: A timestamp indicating the last time the expense was updated in UTC.

Methods
init(self, title, amount): The constructor method initializes the attributes of the Expense class, generating a unique ID and capturing the current UTC time for both creation and update timestamps.
update(self, title=None, amount=None): This method allows for the dynamic updating of the expense's title and/or amount. The updated_at timestamp is automatically set to the current UTC time whenever an update occurs.
to_dict(self): Returns a dictionary representation of the expense, encapsulating all attributes.
str(self): Overrides the default string representation to provide a human-readable format including the expense ID, title, amount, creation timestamp, and last update timestamp.

THE ExpenseDatabase CLASS

Attributes
expenses: A list storing instances of the Expense class.

Methods
init(self): Initializes the expenses list when a new ExpenseDatabase object is created.
add_expense(self, expense): Adds an expense to the list of expenses.
remove_expense(self, expense_id): Removes an expense from the list based on its unique ID.
get_expense_by_id(self, expense_id): Retrieves an expense by its unique ID, returning None if not found.
get_expenses_by_title(self, title): Retrieves a list of expenses with matching titles.
to_dict(self): Returns a list of dictionaries, each representing an expense in the database.
str(self): Provides a string representation of the ExpenseDatabase object by concatenating the string representations of each expense in the list.

A USAGE EXAMPLE
The project includes an example demonstrating the use of the Expense and ExpenseDatabase classes. This example creates an ExpenseDatabase object, adds expenses, updates an expense, and performs operations such as printing the database, getting expenses by ID or title.

# HOW TO CLONE

To clone the repository, follow the steps below:
Open a text editor such as vs code, submlime text, atom, notepad ++ and so on
- Open the terminal
- Navigate to the directory where you want to clone your project or you create new folder in a known directory of yours
- Clone the GitHub repository to your local machine using the command below:
git clone https://github.com/Victor-Akinode/expense-tracking-system.git

or you copy the HTTPS or SSH link to the project by clicking on the code, then choose between the HTTPS or SSH, after that, use the command git clone + the HTTPS or SSH link you just copy and hit enter.
- The project will be cloned and you'd see the progress on your terminal, you'd get a success response once it is done cloning.

# HOW TO RUN THE CODE:
To run the code, 

- Navigate to the directory where you have the cloned project
- Enter the project folder using this command:
cd expense-tracking-system
- Run the example Python script to see the Expense and ExpenseDatabase classes in action using the command below:
python3 victor_akinode.py

This script showcases the basic functionalities of the expense tracking system.

# THE EXAMPLE:
This section creates an instance of ExpenseDatabase, adds an expense, updates it, and performs operations like printing the database, getting expenses by ID or title.

The example demonstrates the usage of both the Expense and ExpenseDatabase classes:

- Example usage:
expense_db = ExpenseDatabase()

- Create an expense
expense1 = Expense("Groceries", 50.00)

- Add the expense to the database
expense_db.add_expense(expense1)

- Print the expenses in the database
print("Expenses in the database:")
print(expense_db)

- Update the title and amount of the expense

expense1.update(title="Monthly Groceries", amount=60.00)

- Print the updated expense

print("\nUpdated Expense:")
print(expense1)

- Print the expenses in the database after the update
print("\nExpenses in the database after update:")
print(expense_db)

- Get an expense by ID
expense_id_to_find = expense1.id
found_expense = expense_db.get_expense_by_id(expense_id_to_find)
if found_expense:
    print(f"\nExpense found by ID {expense_id_to_find}:\n{found_expense.to_dict()}")
else:
    print(f"\nExpense with ID {expense_id_to_find} not found.")

- Get expenses by title
title_to_find = "Monthly Groceries"
matching_expenses = expense_db.get_expenses_by_title(title_to_find)
if matching_expenses:
    print(f"\nExpenses found with title '{title_to_find}':")
    for expense in matching_expenses:
        print(expense.to_dict())
else:
    print(f"\nNo expenses found with title '{title_to_find}'.")



# CODE EXPLANATION
Let us break the code down into bits for better comprehenesion:

FOR Expense CLASS
The Expense class represents an individual financial expense. Here's a breakdown of the class:


import uuid
from datetime import datetime, timezone


class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())  # Generate a unique identifier using UUID.
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)  # Record the creation timestamp in UTC.
        self.updated_at = self.created_at  # Set the initial update timestamp to the creation timestamp.

    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)  # Update the timestamp to the current UTC time.

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }

    def __str__(self):
        return f"Expense ID: {self.id}\nTitle: {self.title}\nAmount: ${self.amount}\nCreated At: {self.created_at}\nLast Updated At: {self.updated_at}"


Initialization (__init__): When an instance of the Expense class is created, it generates a unique ID using the uuid module, sets the title and amount, and records the creation timestamp in UTC. The updated_at timestamp is initially set to the creation timestamp.
Update Method (update): Allows updating the title and/or amount of the expense. The updated_at timestamp is automatically set to the current UTC time whenever an update occurs.
Dictionary Representation (to_dict): Returns a dictionary representation of the expense with attributes like ID, title, amount, creation timestamp, and last update timestamp.
String Representation (__str__): Overrides the default string representation to provide a human-readable format with the key details of the expense.



FOR ExpenseDatabase Class
The ExpenseDatabase class manages a collection of Expense instances. Here's the breakdown:

class ExpenseDatabase:
    def __init__(self):
        self.expenses = []  # Initialize an empty list to store Expense instances.

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                break

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title):
        matching_expenses = [expense for expense in self.expenses if expense.title == title]
        return matching_expenses

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]

    def __str__(self):
        return "\n".join(str(expense) for expense in self.expenses)


Initialization (__init__): Initializes the expenses attribute as an empty list when a new ExpenseDatabase object is created.
Add Expense Method (add_expense): Adds an expense to the list of expenses.
Remove Expense Method (remove_expense): Removes an expense from the list based on its unique ID.
Get Expense by ID Method (get_expense_by_id): Retrieves an expense by its unique ID, returning None if not found.
Get Expenses by Title Method (get_expenses_by_title): Retrieves a list of expenses with matching titles.
Dictionary Representation (to_dict): Returns a list of dictionaries, each representing an expense in the database.
String Representation (__str__): Provides a string representation of the ExpenseDatabase object by concatenating the string representations of each expense in the list.


# Contributions

Contributions to this project are welcome! If you have ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request on the GitHub repository.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize this description based on any additional features or modifications you make to the project.
