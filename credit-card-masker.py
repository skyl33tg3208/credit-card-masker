username = input('enter your username: ')
credit_card = input('enter your credit card number: ')

# Mask all but the last 4 digits
hidden_credit_card = '*' * (len(credit_card) -4) + credit_card[-4:]

print(f'Hi {username}, your credit card number ends in {hidden_credit_card}')