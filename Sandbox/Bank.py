import os
import datetime
import random
import calendar


class BankAccount:
    """
    A comprehensive class to simulate bank account operations including deposits, withdrawals,
    transfers, interest calculations, fees, statements, and more.
    """

    def __init__(self, name, accountType, balance=0):
        """
        Constructor to initialize a bank account.

        Args:
            name (str): The account holder's name
            accountType (str): The type of account ('chequing' or 'savings')
            balance (float, optional): Initial balance. Defaults to 0.
        """
        self.__name = name
        self.__accountType = accountType.lower()
        self.__balance = balance

        # Generate a random 6-digit account ID
        self.__accountID = random.randint(100000, 999999)

        # Create a transaction file for this account
        self.__filename = f"{self.__name}_{self.__accountType}_{self.__accountID}.txt"

        # Transaction limits
        self.__daily_withdrawal_limit = 1000 if accountType.lower() == "chequing" else 500
        self.__daily_withdrawals = 0
        self.__last_withdrawal_date = None

        # Initialize the transaction file with account creation details
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

        # Check daily withdrawal limits
        today = datetime.date.today()

        # Reset daily withdrawal counter if it's a new day
        if self.__last_withdrawal_date != today:
            self.__daily_withdrawals = 0
            self.__last_withdrawal_date = today

        # Check if withdrawal limit reached
        if self.__daily_withdrawals + amount > self.__daily_withdrawal_limit:
            print(
                f"Daily withdrawal limit of ${self.__daily_withdrawal_limit:.2f} exceeded.")
            return False

        if amount > self.__balance:
            print("Insufficient funds. Withdrawal failed.")
            return False

        self.__balance -= amount
        self.__daily_withdrawals += amount

        # Record the transaction
        with open(self.__filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(
                f"{timestamp} - Withdrawal: ${amount:.2f} - Balance: ${self.__balance:.2f}\n")

        print(
            f"${amount:.2f} withdrawn successfully. New balance: ${self.__balance:.2f}")
        return True

    def transfer(self, target_account, amount):
        """
        Transfer money to another account.

        Args:
            target_account (BankAccount): The recipient account
            amount (float): The amount to transfer

        Returns:
            bool: True if transfer was successful, False otherwise
        """
        if amount <= 0:
            print("Transfer amount must be positive.")
            return False

        if amount > self.__balance:
            print("Insufficient funds for transfer.")
            return False

        # Withdraw from this account
        self.__balance -= amount

        # Record the transaction in sender's file
        with open(self.__filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(
                f"{timestamp} - Transfer to {target_account.getUsername()}'s account: -${amount:.2f} - Balance: ${self.__balance:.2f}\n")

        # Deposit to target account
        target_account._BankAccount__balance += amount

        # Record the transaction in recipient's file
        with open(target_account._BankAccount__filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(
                f"{timestamp} - Transfer from {self.__name}'s account: +${amount:.2f} - Balance: ${target_account._BankAccount__balance:.2f}\n")

        print(
            f"${amount:.2f} transferred successfully to {target_account.getUsername()}'s account.")
        return True

    def add_interest(self):
        """
        Add interest to savings accounts. Typically called monthly or annually.

        Returns:
            float: The amount of interest added
        """
        if self.__accountType == "savings":
            # Example: 2.5% annual interest rate
            annual_rate = 0.025
            interest_amount = self.__balance * \
                (annual_rate / 12)  # Monthly interest
            self.__balance += interest_amount

            # Record the transaction
            with open(self.__filename, 'a') as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(
                    f"{timestamp} - Interest: +${interest_amount:.2f} - Balance: ${self.__balance:.2f}\n")

            return interest_amount
        return 0

    def apply_monthly_fee(self):
        """
        Apply monthly maintenance fee based on account type and balance.

        Returns:
            float: The fee amount applied
        """
        fee = 0

        if self.__accountType == "chequing":
            # Example: $5 monthly fee if balance is below $1000
            if self.__balance < 1000:
                fee = 5
                self.__balance -= fee

                # Record the transaction
                with open(self.__filename, 'a') as file:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    file.write(
                        f"{timestamp} - Monthly Fee: -${fee:.2f} - Balance: ${self.__balance:.2f}\n")

                print(f"Monthly maintenance fee of ${fee:.2f} applied.")

        return fee

    def close_account(self):
        """
        Close the bank account.

        Returns:
            float: The final balance that was withdrawn
        """
        final_balance = self.__balance

        # Record the account closure
        with open(self.__filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(
                f"{timestamp} - Account Closed - Final Balance: ${self.__balance:.2f}\n")
            file.write(
                f"{timestamp} - Withdrawal: ${self.__balance:.2f} - Balance: $0.00\n")

        print(
            f"Account closed. Final balance of ${self.__balance:.2f} has been withdrawn.")
        self.__balance = 0
        return final_balance

    def reopen_account(self):
        """
        Reopen a closed account.

        Returns:
            bool: True if reopening was successful
        """
        if self.__balance > 0:
            print("Account is already active.")
            return False

        # Record the account reopening
        with open(self.__filename, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - Account Reopened - Balance: $0.00\n")

        print("Account has been reopened successfully.")
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

    def generate_monthly_statement(self, month, year):
        """
        Generate a monthly account statement.

        Args:
            month (int): Month (1-12)
            year (int): Year (e.g., 2025)

        Returns:
            str: Formatted monthly statement
        """
        statement = f"\n{'='*60}\n"
        statement += f"MONTHLY STATEMENT - {calendar.month_name[month]} {year}\n"
        statement += f"Account: {self.__name} (ID: {self.__accountID})\n"
        statement += f"Account Type: {self.__accountType.capitalize()}\n"
        statement += f"{'='*60}\n\n"

        statement += f"{'DATE':<12}{'TRANSACTION':<30}{'AMOUNT':>10}{'BALANCE':>15}\n"
        statement += f"{'-'*67}\n"

        # Filter transactions for the specified month and year
        monthly_transactions = []
        try:
            with open(self.__filename, 'r') as file:
                for line in file:
                    if " - " in line:
                        try:
                            date_str = line.split(" - ")[0]
                            date_obj = datetime.datetime.strptime(
                                date_str, "%Y-%m-%d %H:%M:%S")
                            if date_obj.month == month and date_obj.year == year:
                                monthly_transactions.append(line.strip())
                        except:
                            continue
        except FileNotFoundError:
            return "Transaction history not found."

        # Format transactions for the statement
        for transaction in monthly_transactions:
            parts = transaction.split(" - ")
            date = datetime.datetime.strptime(
                parts[0], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")

            if "Deposit" in parts[1]:
                trans_type = "Deposit"
                amount = parts[1].split("$")[1]
            elif "Withdrawal" in parts[1]:
                trans_type = "Withdrawal"
                amount = "-" + parts[1].split("$")[1]
            elif "Interest" in parts[1]:
                trans_type = "Interest"
                amount = parts[1].split("+$")[1]
            elif "Fee" in parts[1]:
                trans_type = "Fee"
                amount = "-" + parts[1].split("$")[1]
            elif "Transfer" in parts[1]:
                if "to" in parts[1]:
                    trans_type = "Transfer Out"
                    amount = "-" + parts[1].split("$")[1]
                else:
                    trans_type = "Transfer In"
                    amount = "+" + parts[1].split("$")[1]
            else:
                trans_type = "Other"
                amount = "0.00"

            balance = parts[2].split("$")[1]
            statement += f"{date:<12}{trans_type:<30}{amount:>10}{balance:>15}\n"

        statement += f"\n{'='*60}\n"
        statement += f"Ending Balance: ${self.__balance:.2f}\n"
        statement += f"{'='*60}\n"

        return statement

    def categorize_transactions(self):
        """
        Analyze and categorize transactions.

        Returns:
            dict: Categories and their total amounts
        """
        categories = {
            "deposits": 0,
            "withdrawals": 0,
            "fees": 0,
            "interest": 0,
            "transfers_in": 0,
            "transfers_out": 0
        }

        try:
            with open(self.__filename, 'r') as file:
                for line in file:
                    if "Deposit:" in line:
                        amount = float(line.split("$")[1].split(" ")[0])
                        categories["deposits"] += amount
                    elif "Withdrawal:" in line:
                        amount = float(line.split("$")[1].split(" ")[0])
                        categories["withdrawals"] += amount
                    elif "Fee:" in line:
                        amount = float(line.split("$")[1].split(" ")[0])
                        categories["fees"] += amount
                    elif "Interest:" in line:
                        amount = float(line.split("+$")[1].split(" ")[0])
                        categories["interest"] += amount
                    elif "Transfer to" in line:
                        amount = float(line.split("$")[1].split(" ")[0])
                        categories["transfers_out"] += amount
                    elif "Transfer from" in line:
                        amount = float(line.split("+$")[1].split(" ")[0])
                        categories["transfers_in"] += amount
        except FileNotFoundError:
            return categories

        return categories


# Test the enhanced BankAccount class
if __name__ == "__main__":
    # Create a chequing account for John with an initial balance of $1000
    john_account = BankAccount("John", "chequing", 1000)

    # Create a savings account for Jane with an initial balance of $2000
    jane_account = BankAccount("Jane", "savings", 2000)

    # Perform some basic transactions
    john_account.deposit(500)
    john_account.withdraw(200)
    john_account.withdraw(2000)  # This should fail due to insufficient funds

    # Transfer between accounts
    john_account.transfer(jane_account, 300)

    # Apply interest to savings account
    interest = jane_account.add_interest()
    print(f"Interest added: ${interest:.2f}")

    # Apply monthly fee to checking account
    john_account.apply_monthly_fee()

    # Display account information
    print("\nAccount Information (John):")
    print(f"Name: {john_account.getUsername()}")
    print(f"Account Type: {john_account.getAccountType()}")
    print(f"Account ID: {john_account.getAccountID()}")
    print(f"Current Balance: ${john_account.getBalance():.2f}")

    print("\nAccount Information (Jane):")
    print(f"Name: {jane_account.getUsername()}")
    print(f"Account Type: {jane_account.getAccountType()}")
    print(f"Account ID: {jane_account.getAccountID()}")
    print(f"Current Balance: ${jane_account.getBalance():.2f}")

    # Generate monthly statement
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    print(john_account.generate_monthly_statement(current_month, current_year))

    # Categorize transactions
    john_categories = john_account.categorize_transactions()
    print("\nTransaction Categories (John):")
    for category, amount in john_categories.items():
        print(f"{category.replace('_', ' ').title()}: ${amount:.2f}")

    # Close and reopen account
    john_account.close_account()
    john_account.reopen_account()
    john_account.deposit(100)  # Start fresh after reopening

    # Display final transaction history
    print("\nFinal Transaction History (John):")
    print(john_account.getTransactionHistory())

    print("\nFinal Transaction History (Jane):")
    print(jane_account.getTransactionHistory())
