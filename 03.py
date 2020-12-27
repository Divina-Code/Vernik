print("Hello user")

user_name = input("What is your name?")

print('Hello', user_name, "in your name"), len(user_name), 'letters'

user_year =int(input("When you was born?"))
if 2020 - user_year >= 18:
    print(user_name+ 'you can watch a horror movie')
elif 2020 - user_year >=16:
    print(user_name, 'you can watch serial')

else:
    print(user_year, 'you can watch a comedy')
