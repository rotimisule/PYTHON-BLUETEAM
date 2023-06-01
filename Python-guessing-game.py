##python guessing game
while True:
    user_guess = int(input("When was Python 1.0 released? "))
    python_release = 1994
    if user_guess > python_release:
        print('It was earlier than that!')
    elif user_guess < python_release:
        print('It was later than that!')
    else:
        print ('Correct!')
        break
    

