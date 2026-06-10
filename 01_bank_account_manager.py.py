"""
Module: 01_bank_account_manager.py
Description: A console-based banking application to simulate account opening, 
             deposits, withdrawals, and fixed deposit interest calculations.
Author: Engineering Student & Content Creator (@sujnanadeevige108)
"""

# Initialise mock database with timestamped account numbers as keys
# Format: { 'account_number': ['Account Holder Name', current_balance] }
bank_details = {
    '101120242219': ['Suresh', 1000.00], 
    '110120242010': ['Sunil', 1000.00]
}

def display_menu():
    """Prints the banking system operations menu."""
    print("\n" + "*" * 35)
    print("      SAVINGS BANK SIMULATOR      ")
    print("*" * 35)
    print("1. Open Savings Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Calculate Fixed Deposit (FD)")
    print("5. Exit Application")
    print("-" * 35)
    print("Note: Option 1 automatically generates your unique ID.")
    print("*" * 35)

def main():
    while True:
        display_menu()
        
        # Exception handling to prevent crashes from invalid text inputs
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("\nError: Please enter a valid number between 1 and 5.")
            continue

        # ----------------------------------------------------
        # OPTION 1: OPEN ACCOUNT
        # ----------------------------------------------------
        if choice == 1:
            date = input("Enter today's date (DDMMYYYY): ").strip()
            time = input("Enter current time (HHMM): ").strip()
            
            # Concatenate date and time to generate a unique account number
            ac_no = date + time
            print(f"\nSuccess! Your system-generated Account Number is: {ac_no}")
            
            name = input("Enter account holder's name: ").strip()
            
            try:
                md = float(input("Enter initial deposit value (Minimum 1000.00): "))
                if md < 1000.00:
                    print("Warning: Depositing less than 1000.00 may trigger maintenance fees.")
            except ValueError:
                print("Invalid amount. Setting default minimum balance to 1000.00.")
                md = 1000.00
                
            bank_details[ac_no] = [name, md]
            print("\nUpdated System Registry Snapshot:")
            print(bank_details)

        # ----------------------------------------------------
        # OPTION 2: DEPOSIT MONEY
        # ----------------------------------------------------
        elif choice == 2:
            an = input("Enter your account number: ").strip()
            if an in bank_details:
                try:
                    dm = float(input("Enter amount to deposit: "))
                    bank_details[an][1] += dm
                    print(f"\nTransaction Successful: Rs. {dm:.2f} deposited.")
                    print(f"Current Available Balance: Rs. {bank_details[an][1]:.2f}")
                except ValueError:
                    print("Error: Invalid transaction amount.")
            else:
                print("\nError: Account number not registered in the system.")

        # ----------------------------------------------------
        # OPTION 3: WITHDRAW MONEY
        # ----------------------------------------------------
        elif choice == 3:
            ac = input("Enter your account number: ").strip()
            if ac in bank_details:
                try:
                    wm = float(input("Enter amount to withdraw: "))
                    current_balance = bank_details[ac][1]
                    projected_balance = current_balance - wm
                    
                    # Enforce the minimum threshold limit rule
                    if projected_balance < 1000.00:
                        print("\nTransaction Denied: Insufficient funds.")
                        print("Your account must retain a minimum balance of Rs. 1000.00.")
                    else:
                        bank_details[ac][1] = projected_balance
                        print(f"\nTransaction Successful: Rs. {wm:.2f} withdrawn.")
                        print(f"Remaining Balance: Rs. {bank_details[ac][1]:.2f}")
                except ValueError:
                    print("Error: Invalid transaction amount.")
            else:
                print("\nError: Account record not found. Please create an account first.")

        # ----------------------------------------------------
        # OPTION 4: FIXED DEPOSIT LOGIC
        # ----------------------------------------------------
        elif choice == 4:
            try:
                p = float(input("Enter Fixed Deposit principal amount: "))
                r = 8.0  # Fixed annual interest rate percentage
                t = int(input("Enter lock-in period duration (in years): "))
                
                # Simple Interest Formula Execution
                si = (p * r * t) / 100
                total_maturity_amount = p + si
                
                print(f"\n--- FD Projection Breakdown ---")
                print(f"Fixed Annual Interest Rate: {r}% per annum")
                print(f"Total Accrued Interest: Rs. {si:.2f}")
                print(f"Total Maturity Yield (Principal + Interest): Rs. {total_maturity_amount:.2f}")
            except ValueError:
                print("Error: Please input valid numeric values for FD calculations.")

        # ----------------------------------------------------
        # OPTION 5: TERMINATE SYSTEM
        # ----------------------------------------------------
        elif choice == 5:
            print("\nShutting down core banking simulation terminal. Goodbye!")
            break

        else:
            print("\nInvalid operation selection. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    main()
