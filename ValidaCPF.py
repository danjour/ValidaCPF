import re
#Passível de muitas melhorias

def valida_cpf(cpf):
  cpf=re.sub('[^0-9]','',cpf)  #Retira alguns dados inválidos
  i = 0
  soma=0
  while i < len(cpf):
    soma+=int(cpf[i]) #Soma todos os dígitos
    i+=1
  soma=str(soma) #Transforma em letra para comparar
  if(soma[0]!=soma[1]):
    return False
  else:
    return True
  
def num_igual(cpf): #Validação se todos os números não são iguais
    cpf=re.sub('[^0-9]','',cpf) #Retira alguns dados inválidos
    i = 0
    while i < len(cpf): #Compara o primeiro dígito com o resto
        if cpf[0] != cpf[i]:
            return False
            break
        i += 1
    return True

cpf=(input())

if((num_igual(cpf))==False):
  if(valida_cpf(cpf)==True):
    print("CPF válido")
else:
  print("CPF inválido")
