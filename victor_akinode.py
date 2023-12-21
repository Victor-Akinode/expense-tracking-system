import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

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

class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

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

# HERE ARE SOME EXAMPLES:
expense_db = ExpenseDatabase()

# Create an expense
expense1 = Expense("Groceries", 50.00)

# Add the expense to the database
expense_db.add_expense(expense1)

# Print the expenses in the database
print("Expenses in the database:")
print(expense_db)

# Update the title and amount of the expense
expense1.update(title="Monthly Groceries", amount=60.00)

# Print the updated expense
print("\nUpdated Expense:")
print(expense1)

# Print the expenses in the database after the update
print("\nExpenses in the database after update:")
print(expense_db)

# Get an expense by ID
expense_id_to_find = expense1.id
found_expense = expense_db.get_expense_by_id(expense_id_to_find)
if found_expense:
    print(f"\nExpense found by ID {expense_id_to_find}:\n{found_expense.to_dict()}")
else:
    print(f"\nExpense with ID {expense_id_to_find} not found.")

# Get expenses by title
title_to_find = "Monthly Groceries"
matching_expenses = expense_db.get_expenses_by_title(title_to_find)
if matching_expenses:
    print(f"\nExpenses found with title '{title_to_find}':")
    for expense in matching_expenses:
        print(expense.to_dict())
else:
    print(f"\nNo expenses found with title '{title_to_find}'.")
