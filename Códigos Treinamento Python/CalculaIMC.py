def quadrado(numero):
  valorquadrado = numero * numero
  return valorquadrado

def calcula_IMC(altura,peso):
  altura_quadrada = quadrado(altura)
  meu_imc = peso/altura_quadrada
  return meu_imc

def indice_gordura(meu_imc):
  if imc < 18.5:
    print("Magreza")
  elif imc >= 18.5 and imc < 25:
    print("Normal")
  elif imc >= 25 and imc < 30:
    print("Sobrepeso")
  elif imc >= 30 and imc < 40:
    print("Obesidade")
  else:
    print("Obesidade Grave") 


imc = calcula_IMC(1.75,75)
print("Seu IMC é : ", imc)
print("Você esta classificado como: ")
indice_gordura(imc)
