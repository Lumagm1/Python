# Write code below 💖
peso = int(input("What do you have left in pesos? "))
soles = int(input("What do you have left in soles? "))
reais = int(input("What do you have left in reais? "))

peso = peso * 0.00028 #columbian
soles = soles * 0.29
reais = reais * 0.20

usd = peso + soles + reais

print(usd)