# version 0.3.0
import bip38

print('Choose an option:')
print('1 - BIP38')
print('2 - Seed phrase')
option = input()
print('')

def calc_seed(password, code):
    carteira_ascii_int = password % code
    carteira_ascii_int = carteira_ascii_int ** (code // 1000000)
    carteira_ascii_int = carteira_ascii_int // password
    carteira_ascii_int = carteira_ascii_int // code
    carteira_ascii_int = carteira_ascii_int // password - code
    carteira_ascii_int = carteira_ascii_int // (password * 2 * (code * (password // (code * code))))
    carteira_ascii_int *= carteira_ascii_int
    carteira_ascii_int = carteira_ascii_int // (password * 2 * (code * (password // (code * code))))
    carteira_ascii_int = carteira_ascii_int // password
    carteira_ascii_int = carteira_ascii_int % 56291044072069903211573076371188843891112757796638879846590117541962083956126160349962904078614842833889730890469898359048994712549790806075701492229771053119667209801737135108808032927445072844988234
    carteira_ascii_int = carteira_ascii_int + 10014633776421543822972231830989607683036093290721757356475647237580413103907090794144664079943751461911925025369471433198538998882482335177182815168555167389866050887798592322840405343882495891842515200
    carteira_ascii_int = carteira_ascii_int + (password * 342063431316347235708866670518074675149310403702454932040416204068800789531424653525030533557071372935643795222139148262226638049492311405974311076231656387391 + 2455348766317105749638060990027751334328476)

    ascii_str = str(carteira_ascii_int)

    verify_ascii_code = ''
    wallet = ''

    for character in ascii_str:
        verify_ascii_code += character
        ascii_str = ascii_str[1:]

        if int(verify_ascii_code) > 31 and int(verify_ascii_code) < 127:
            wallet += chr(int(verify_ascii_code))
            verify_ascii_code = ''

    print(wallet)


while option != 0:
    if option == '1':
        print('Enter the BIP38 encrypted private key:')
        encrypted_key = input()
        print('Enter the passphrase:')
        passphrase = input()
        print('Decrypted key:', bip38.bip38_decrypt(encrypted_key, passphrase))

    elif option == '2':
        print('Enter the password:')
        password = input()
        print('Enter the number code:')
        code = input()

        password_ascii = ''
        code_ascii = ''

        for character in password:
            password_ascii += str(ord(character))
        
        for character in code:
            code_ascii += str(ord(character))

        calc_seed(int(password_ascii), int(code_ascii))