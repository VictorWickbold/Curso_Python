import math
a = float(input('Digite um ângulo qualquer: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('='*45)
print('O seno de {}º é: {:.2f} \nO cosseno de {}º é: {:.2f} \nA tangente de {}º é: {:.2f}'.format(a,s,a,c,a,t))
print('='*45)