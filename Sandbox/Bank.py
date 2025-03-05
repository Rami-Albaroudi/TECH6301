import random
import datetime


class BankAccount:
    def __init__(self, name, accountType, balance=0):
        """
        Constructor for creating a bank account.

        Args:
            name (str): The account holder's name
            accountType (str): The type of account ('chequing' or 'savings')
            balance (float, optional): Initial balance. Defaults to 0.
        """
        self.__name = name
        self.__accountType = accountType.lower()
        self.__balance = balance
        self.__accountID = random.randint(100000, 999999)
        self.__filename = f"{self.__name}_{self.__accountType}_{self.__accountID}.txt"

        # Create transaction file
        with open(self.__filename, 'w') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Account created on {timestamp}\n")
            file.write(f"Initial balance: ${self.__balance:.2f}\n")
            file.write("-" * 50 + "\n")

    def deposit(self, amount):
        """
        Deposit money into the account and record the transaction.

        Args:
            amount (float): The amount to deposit

        Returns:
            bool: True if deposit was successful, False otherwise
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False

        self.__balance += amount

        # Record the transaction
        with open(self.__filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(
                f"{timestamp} - Deposit: ${amount:.2f} - Balance: ${self.__balance:.2f}\n")

        print(
            f"${amount:.2f} deposited successfully. New balance: ${self.__balance:.2f}")
        return True

    def withdraw(self, amount):
        """
        Withdraw money from the account and record the transaction.

        Args:
            amount (float): The amount to withdraw

        Returns:
            bool: True if withdrawal was successful, False otherwise
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount > self.__balance:
            print("Insufficient funds. Withdrawal failed.")
            return False

        self.__balance -= amount

        # Record the transaction
        with open(self.__filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(
                f"{timestamp} - Withdrawal: ${amount:.2f} - Balance: ${self.__balance:.2f}\n")

        print(
            f"${amount:.2f} withdrawn successfully. New balance: ${self.__balance:.2f}")
        return True

    def getBalance(self):
        """
        Get the current account balance.

        Returns:
            float: The current balance
        """
        return self.__balance

    def getAccountID(self):
        """
        Get the account ID.

        Returns:
            int: The account ID
        """
        return self.__accountID

    def getUsername(self):
        """
        Get the account holder's name.

        Returns:
            str: The account holder's name
        """
        return self.__name

    def getAccountType(self):
        """
        Get the account type.

        Returns:
            str: The account type ('chequing' or 'savings')
        """
        return self.__accountType

    def getTransactionHistory(self):
        """
        Get the transaction history by reading the statement file.

        Returns:
            str: The transaction history as a string
        """
        try:
            with open(self.__filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Transaction history not found."


# Test the BankAccount class
if __name__ == "__main__":
    # Create a chequing account for John with an initial balance of $1000
    john_account = BankAccount("John", "chequing", 1000)

    # Create a savings account for Jane with an initial balance of $2000
    jane_account = BankAccount("Jane", "savings", 2000)

    # Perform some transactions
    john_account.deposit(500)
    john_account.withdraw(200)
    john_account.withdraw(2000)  # This should fail due to insufficient funds

    # Display account information
    print("\nAccount Information (John):")
    print(f"Name: {john_account.getUsername()}")
    print(f"Account Type: {john_account.getAccountType()}")
    print(f"Account ID: {john_account.getAccountID()}")
    print(f"Current Balance: ${john_account.getBalance():.2f}")

    # Display transaction history
    print("\nTransaction History (John):")
    print(john_account.getTransactionHistory())
