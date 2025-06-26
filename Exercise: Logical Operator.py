# check is magician AND expert: "you are a master magician"
# check is magician but not expert: "at least you're getting there"
# if you're not a magician: "You need magic powers"

is_magician = True
is_expert = False

if is_magician and is_expert:
    print('you are a master magician')

elif is_magician and not is_expert:
    print('at least you are getting there')

elif not is_magician:
    print('You need magic powers')
