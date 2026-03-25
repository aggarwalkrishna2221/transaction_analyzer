def transaction_categorizer():
    expenses = []
    places = []

    while True:
        inp = input("Enter the amount you spent and on what (or 'done' to finish): ")
        if inp.lower() == "done":
            break

        spent_where_pos = inp.find(" ")
        if spent_where_pos == -1:
            print("Please enter both amount and place. Example: 500 food")
            continue

        spent = inp[:spent_where_pos]
        spent_where = inp[spent_where_pos + 1:] 

        try:
            int_inp = float(spent)
            if int_inp < 0:
                print("Expenses cannot be negative.")
                continue
            expenses.append(int_inp)
            places.append(spent_where)  
        except:
            print("Please enter a valid number.")
            continue 

 
    if len(expenses) == 0:
        print("No transactions recorded.")
        return

    transactions = len(expenses)
    total = sum(expenses)
    largest_transaction = max(expenses)

    print("\n--- Summary ---")
    print("Total Transactions:", transactions)
    print("Total money spent:", total)
    print("Largest transaction:", largest_transaction)
    print("Expenses:", expenses)
    print("Places:", places)

transaction_categorizer()
