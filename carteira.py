carteira_ascii_str = '11511097112321021051011081003211810510111932991081171169910432981011161191011011103211597116111115104105321109711210710511032971081121049732991111051103210210111099101321011091121161213298105116116101114'

carteira = ''
verificar_ascii_codigo = ''

print(len(carteira_ascii_str))

for caracter in carteira_ascii_str:
    verificar_ascii_codigo += caracter
    carteira_ascii_str = carteira_ascii_str[1:]

    if (int(verificar_ascii_codigo) > 96 and int(verificar_ascii_codigo) < 123) or int(verificar_ascii_codigo) == 32:
        carteira += chr(int(verificar_ascii_codigo))
        verificar_ascii_codigo = ''

print(carteira)