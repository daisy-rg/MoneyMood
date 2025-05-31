from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from tqdm import tqdm
import time
from services import create_user_flow, list_all_users

Base = declarative_base()

engine = create_engine('sqlite:///finance.db',echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():

    print("\n")
    print("  _______________________________________________________  ")
    print(" /                                                       \\ ")
    print("|                   MONEYMOOD FINANCE                    |")
    print("|               Your Cash Flow Companion                 |")
    print(" \\_______________________________________________________/")
    print("           [•] 2023 | v1.2.0 | by DevTeam [•]            ")

    for i in tqdm(range(10), desc="Program Loading...", unit="s"):
        time.sleep(1)

    while True:
        
        print("\n Main Menu:")
        print("1. Create User")
        print("2. List all users")
        print("3. Find a certain User")
        print("4. Find a certain User's Income")
        print("5. Find a certain User's Transactions")
        print("6. Delete User and all financial records")
        print("7. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            create_user_flow(session)
        elif choice == "2":
            view_users()
        elif choice == "3":
            find_user()
        elif choice == "4":
            user_income()
        elif choice == "5":
            user_transactions()
        elif choice == "6":
            delete_user()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Choice invalid!")
            
            
def view_users():
    with Session() as session:
        users = list_all_users(session)
        if users:
            print("\nRegistered Users:")
            for user in users:
                print(f"- {user.name} (ID: {user.id})")
        else:
            print("No users found.")

if __name__ == '__main__':
    main_menu()