import os
import time
# Importa o mysqlconnector
import mysql.connector

print ("################################")
print ("Bem vindo ao Auto incremento em Python")
print ("################################\n\n")


# Insira o nome do seu servidor geralmente é localhost
hostvic = input("Insira seu hostname:")
print("Seu hostname é: " + hostvic + " vamos para o próximo dado.\n\n")

# Insira seu usário o padrão é root
usuariovic = input("Insira seu usuário:")
print("Seu usuário é: " + usuariovic + " vamos para o próximo dado.\n\n")

# Insira sua senha
senhavic = input("Insira sua senha:")
print("Sua senha é: *********** vamos para o próximo dado.\n\n")

#Insira seu banco de dados
banco = input("Insira o nome do seu banco de dados:")
print("O banco de dados escolhido foi " + banco)

#Escolha a tabela
tabela = input("\n\nInsira o nome da tabela:")
print("A tabela escolhida foi " + tabela)

#Escolha a tabela
numero = input("\n\nInsira o valor inicial:")
print("O valor inicial será definido para " + numero)




# Faz a conexão com o banco de dados
bancodb = mysql.connector.connect(
  host= hostvic ,
  user= usuariovic,
  password= senhavic,
  database = banco
)

vaidb = bancodb.cursor()
zeroum = "ALTER TABLE `" + tabela + "` ADD PRIMARY KEY( `id`);"
zerodois = "ALTER TABLE `" + tabela + "` MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT="+ numero + ";"


# Executa as duas querys
vaidb.execute(zeroum)
vaidb.execute(zerodois)
bancodb.commit()






