"""
An ATM machine returning 50, 200, 500 notes. Write a class-based (OOPs) program
to print how many different types of notes the ATM machine will return?
Validate if the user enter wrong amount for withdrawal.
Print a valid message and ask either continue/cancel, with this perform your operations
I/P : 950
O/P :
500 notes : 1
200 notes : 2
50 notes : 1
"""


class ATM:
    def __init__(self):
        self.available_notes = [500, 200, 50]

    def withdraw_cash(self, amount):
        notes_count = {}
        remaining_amount = amount

        for note in self.available_notes:
            if remaining_amount >= note:
                note_count = remaining_amount // note
                notes_count[note] = note_count
                remaining_amount %= note

        if remaining_amount == 0:
            return notes_count
        else:
            print("Invalid withdrawal amount. Please enter a valid amount.")
            return None

    def print_notes(self, notes_count):
        if notes_count is not None:
            for note, count in notes_count.items():
                print(f"{note} notes : {count}")

atm = ATM()

while True:
    try:
        amount = int(input("Enter the amount to withdraw: "))
        notes_count = atm.withdraw_cash(amount)
        if notes_count is not None:
            atm.print_notes(notes_count)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

    choice = input("Do you want to continue (C) or cancel (X)? ").upper()
    if choice != "C":
        break
