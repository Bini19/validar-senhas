import re  
import pwinput

def valida_senha(nome, senha):
  if nome == senha:
    return "Erro: A senha não deve ser igual ao nome"
  if (len(senha)<8): 
    flag = -1
    return "A senha deve conter no minimo 8 caracteres" 
      
  elif not re.search("[a-z]", senha): 
    flag = -1
      
  elif not re.search("[A-Z]", senha): 
    flag = -1
    return "A senha deve conter no minimo UM caracter MAIUSCULO"
      
  elif not re.search("[0-9]", senha): 
    flag = -1
    return "A senha deve conter no minimo UM número"
      
  elif not re.search("[_@$*Ç!#¨&.]", senha): 
    flag = -1
    return "A senha deve conter no minimo UM caracter especial"
      
  elif re.search("\s", senha): 
    flag = -1
      
  else: 
    flag = 0
    return "Login realizado com sucesso!"
  if flag ==-1: 
    return "Senha inválida"
  return None

  
if __name__=='__main__':
  nome = input("Digite seu login: ")
  senha = pwinput.pwinput("Digite sua senha: ")
  validacao = valida_senha(nome, senha)
  print(validacao)


#Guilherme Bini 24/10/22