import basic

while True:
    text = input('Aussie> ')
    result, error = basic.Run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)