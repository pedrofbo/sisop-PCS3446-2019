import secrets

nbytes = input('numero de bytes: ')

numbers = secrets.token_hex(int(nbytes)).upper()

it = 0
while it < 2 * int(nbytes):
    print(f'{numbers[it]}{numbers[it + 1] } ', end = '')
    it += 2