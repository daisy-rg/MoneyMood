from db.models import User, Income, Transaction, TransactionCategory
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
        date = input("Enter date (YYYY-MM-DD): ")
        
        
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

        transaction = Transaction(
            amount=amount,
            date=date,
            category=category,
            description=description,
            user_id=user.id
        )
        session.add(transaction)
        session.commit()
        print(f" Transaction '{amount}' added.")

        add_another = input("Add another transaction? (y/n): ").lower()
        if add_another != 'y':
            break