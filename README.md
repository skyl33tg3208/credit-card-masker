# Credit Card Masker 💳

A simple Python script that takes a user's name and credit card number, then masks all but the last four digits for security.

## 🔧 How It Works

1. Prompts the user to enter a username and credit card number.
2. Uses Python string slicing to replace all but the last 4 digits with asterisks (`*`).
3. Displays the masked credit card number with a friendly message.

## 🧪 Example
Enter your username: Kenny
Enter your credit card number: 1234567812345678

Hi Kenny, your credit card number ends in ************5678


## 🚀 Tech Used

- Python 3.x
- No external libraries

## 📁 File

- `credit_card_masker.py` — contains the main script

## 💡 Future Ideas

- Add input validation (e.g. make sure card number is all digits)
- Format output with spaces (e.g. `**** **** **** 5678`)
- Save masked output to a log file (for mock audit trails)


