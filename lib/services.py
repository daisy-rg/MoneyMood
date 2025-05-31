from db.models import User, Income, Transactions, TransactionCategory
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine("sqlite:///lib/db/finance.db")
Session = sessionmaker(bind=engine)






def create_user_flow(session):
    print("\n--- Create New User ---")
    name = input("Enter user's name: ")
    age = int(input("Enter user's age: "))
    profession = input("Enter user's profession: ")

    user = User(name=name, age=age, profession=profession)
    session.add(user)
    session.commit()
    print(f" User '{name}' created with ID {user.id}")

    print("\n--- Add Income ---")
    amount = float(input("Enter income amount: "))
    source = input("Enter income source: ")

    income = Income(amount=amount, source=source, user_id=user.id)
    session.add(income)
    session.commit()
    print(f" Income of {amount} added for user {user.name}")

    while True:
        print("\n--- Add Transaction ---")
        amount = float(input("Enter transaction amount: "))
        date_string = input("Enter date (YYYY-MM-DD): ")
        
        
        print("Choose a category:")
        categories = list(TransactionCategory)
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {cat.value}")

        while True:
            try:
                cat_choice = int(input("Enter the number for category: "))
                if 1 <= cat_choice <= len(categories):
                    category = categories[cat_choice - 1].value
                    break
                else:
                    print("Invalid number. Try again.")
            except ValueError:
                print("Please enter a valid number.")

        description = input("Enter transaction description: ")
        
        date_obj = datetime.strptime(date_string, "%Y-%m-%d").date()
        transactions = Transactions(
            amount=amount,
            date=date_obj,
            category=category,
            description=description,
            user_id=user.id
        )
        session.add(transactions)
        session.commit()
        print(f" Transaction '{amount}' added.")

        add_another = input("Add another transaction? (y/n): ").lower()
        if add_another != 'y':
            break
        
        
def list_all_users(session):
        users = session.query(User).all()
        return users
    
 

def find_user(session):
    user_id = input("Enter user ID (or press Enter to search by name): ").strip()

    if user_id:
        user = session.query(User).filter_by(id=user_id).first()
    else:
        name = input("Enter user name: ").strip()
        user = session.query(User).filter_by(name=name).first()

    if user:
        print(f"\nFound user: {user.name} (ID: {user.id}, Age: {user.age}, Profession: {user.profession})")
    else:
        print("User not found.")

def user_income(session):
    user_id = input("Enter user ID: ").strip()
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print("User not found.")
        return

    if user.income:
        print(f"\nIncomes for {user.name}:")
        for income in user.income:
            print(f"- {income.source}: ${income.amount}")
    else:
        print(f"{user.name} has no income records.")

def user_transactions(session):
    user_id = input("Enter user ID: ").strip()
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print("User not found.")
        return

    if user.transactions:
        print(f"\nTransactions for {user.name}:")
        for txn in user.transactions:
            print(f"- ${txn.amount} on {txn.date} [{txn.category}]: {txn.description}")
    else:
        print(f"{user.name} has no transactions.")
        
def delete_user(session):
    user_id = input("Enter the ID of the user to delete: ").strip()

    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print("User not found.")
        return

    confirm = input(f"Are you sure you want to delete user '{user.name}' and all their records? (y/n): ").lower()
    if confirm == 'y':
        session.delete(user)
        session.commit()
        print(f"User '{user.name}' and all their records have been deleted.")
    else:
        print("Deletion canceled.")
           