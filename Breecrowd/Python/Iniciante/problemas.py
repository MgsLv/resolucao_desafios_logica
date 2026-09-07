def problema1000():
    print('Hello World!')

def problema1001():
    a = int(input())
    b = int(input())
    x = a + b
    print('X =', x)

def problema1002():
    pi = 3.14159
    raio = float(input())
    area = pi * (raio*raio)
    print("A=%.4f" % area)

def problema1003():
    a = int(input())
    b = int(input())
    soma = a + b
    print(f"SOMA = {soma}")

def problema1005():
    a = float(input())
    b = float(input())
    result = ((a*3.5) + (b*7.5))/11
    print(f"MEDIA = {result:.5f}")

def problema1041():
    cord = []

while len(cord) < 2:
    linha = input().split()
        for valor in linha:
            cord.append(float(valor))
        
    cordX = float(cord[0])
    cordY = float(cord[1])
    
    if cordX > 0 and cordY > 0:
        print("Q1")
    elif cordX > 0 and cordY < 0:
        print("Q4")
    elif cordX < 0 and cordY > 0:
        print("Q2")
    elif cordX < 0 and cordY < 0:
        print("Q3")
    elif cordX == 0 and cordY == 0:
        print("Origem")
    elif cordX == 0:
        print("Eixo Y")
    elif cordY == 0:
        print("Eixo X")


def problema1051():
    renda = float(input())

    if renda <=  2000:
        print("Isento")
    elif renda >= 2000.01 and renda <= 3000.00:
        renda -= 2000
        imposto = (8/100) * renda
        print(imposto)
    elif renda >= 3000.01 and renda <= 4500.00:
        renda -= 3000
        imposto = (8/100) * 1000 + (18/100) * renda
        print(imposto)
    elif renda > 4500.00:
        renda -= 4500
        imposto = (8/100) * 1000 + (18/100) * 1500 + (28/100) * renda
        print(imposto)

def problema1052():
    mes = int(input())

    if mes == 1:
        print("January")
    elif mes == 2:
        print("February")
    elif mes == 3:
        print("March")
    elif mes == 4: 
        print("April")
    elif mes == 5:
        print("May")
    elif mes == 6:
        print("June")
    elif mes == 7: 
        print("July")
    elif mes == 8: 
        print("August")
    elif mes == 9: 
        print("September")
    elif mes == 10: 
        print("October")
    elif mes == 11:
        print("November")
    elif mes == 12: 
        print("December")
    else:
        print("Error")

def problema1069():
    casos = int(input())
    
    for caso in range(casos):
        aberto = 0
        diamantes = 0
        
        mina = str(input().strip())
        
        for char in mina:
            if char == "<":
                aberto += 1
                
            if char == ">" and aberto > 0:
                aberto -= 1
                diamantes += 1    
    
        print(diamantes)


def problema1541():
    while True:
        try:
            entrada = input().split(" ")
            if not entrada or entrada[0] == '0':
                break
            
            a = int(entrada[0])
            b = int(entrada[1])
            c = int(entrada[2])
            
            area_casa = a * b
            area_total = (area_casa * 100) / c 
            lado = int(area_total ** 0.5)
            
            print(lado)
        except EOFError:
            break

def problema1168():
    entrada = input().upper()

    matriz = []
    for i in range(12):
        linha = []
        for j in range(12):
            valor = float(input())
            linha.append(valor)
        matriz.append(linha)
        
    soma = 0
    quant_elementos = 0
    
    for i in range(12):
        for j in range(12):
            if i + j > 11:
                soma += matriz[i][j]
                quant_elementos += 1
        
    resultado = soma / quant_elementos
    
    if entrada == "S":
        print(f"{soma:.1f}")
    elif entrada == "M":
        print(f"{resultado:.1f}")

def problema1168N3():
    vezes = int(input())

    valorLeds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    for _ in range(vezes):
        numero = input().strip()
        
        leds = 0
        
        for num in numero:
            digito = int(num)
            leds += valorLeds[digito]
            
        print(f"{leds} leds")

def problema1171():
    seq = int(input())
    resp = {}
    
    for num in range(seq):
        num = int(input())
        
        if num not in resp:
            resp[num] = 1
        else: 
            resp[num] += 1
        
    orderResp = dict(sorted(resp.items()))
    
    for num in orderResp:
        quant = orderResp[num]
        print(f"{num} aparece {quant} vez(es)")
    

def problema1847():
    entrada = input().split()
    a = int(entrada[0])
    b = int(entrada[1])
    c = int(entrada[2])
    
    feliz = False
    
    if b < a: 
        if c >= b:
            feliz = True
        elif (b - c) < (a - b):
            feliz = True
        else:
            feliz = False
    
    elif b > a:
        if c <= b:
            feliz = False
        elif (c - b) < (b - a): 
            feliz = False
        else: 
            feliz = True
    
    else: 
        if c > b: 
            feliz = True
        else: 
            feliz = False
    
    if feliz:
        print(":)")
    else:
        print(":(")

def problema3053N4():
    qtdMovimentos = int(input())

    moeda = input()
    
    for _ in range(qtdMovimentos):
        
        movimento = int(input())
        if movimento == 1:
            if moeda == 'A':
                moeda = 'B'
            elif moeda == 'B':
                moeda = 'A'
        elif movimento == 2:
            if moeda == 'B':
                moeda = 'C'
            elif moeda == 'C':
                moeda = 'B'
        else: 
            if moeda == 'A':
                moeda = 'C'
            elif moeda == 'C':
                moeda = 'A'
                
    print(moeda)
