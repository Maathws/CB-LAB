import retornaDicionarioErp
import dataBase


conexaoDB = dataBase.conectarDataBaseGeral()
dataBase.criarDataBaseRestaurantesETabelas(conexaoDB)

dicionarioErp = retornaDicionarioErp.retornaDicionarioErp()

dataBase.inserirDataBaseRestaurantesETabelas(conexaoDB, dicionarioErp)