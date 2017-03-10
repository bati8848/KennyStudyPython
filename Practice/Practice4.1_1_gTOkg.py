
while True:
    a = int(input('【input 0 to finish the game】\nPlease input a number:      '))

    if a==0:
        print('\n\n\nThe END, thank you.')
        break

    b= a/1000
    print('{} g is {} kg, Thank you\n'.format(str(a),str(b)))
