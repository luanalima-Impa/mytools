import MYTOOLS

N=int(input("Aproximação com quantas casas decimais? "))
while not 0<N<100:
    N=int(input("Escolha um número maior que 0 e menor que 100: "))

h=MYTOOLS.e_real(N)
j=MYTOOLS.pi_real(N)

print(f"3,{j}")
print(f"2,{h}")
