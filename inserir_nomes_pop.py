#script utilizado para inserir os nomes populares das cobras no banco de dados

from utils.database import *

nomes_pop = {
    10: 'Cobra-Cipó',
    11: 'Cobra-Cipó, Corredeira, Papa-Rato, Rateira',
    12: 'Cobra-Arco-Íris, Jiboia-Arco-Íris, Jiboia, Salamanta, Serpente-de-Veado, Serpente-Furta-Cor, Uaçubói',
    13: 'Cobra-Chumbo, Cobra-da-Terra, Cobra-de-Chumbinho',
    14: 'Boipeva, Casco-de-Burro, Cobra-Corredeira, Cobra-D’água, Cobra-de-Caçote, Cobra-de-Caçote-Amarela, Cobra-de-Capim, Cobra-de-Jardim, Cobra-de-Lixo, Cobra-do-Capim, Cobra-do-Lixo, Cobra-Lisa, Cobra-Verde, Cobra-Verde-Argentina, Cobra-Verde-do-Capim, Coral-Falsa, Falsa-Coral, Jararaquinha, Parelheira, Peça-Nova, Rainha',
    15: 'Cobra-D’água, Cobra-Verde, Cobra-Verde-da-Caatinga',
    16: 'Cobra-D’água, Jararaca-D’água, Surucucurana, Trairamboia',
    17: 'Cipó-Olhuda, Cobra-Cipó, Cobra-Fio, Dorme-Dorme, Dormideira, Dorminhoca, Jararaquinha, Papa-Lesma',
    18: 'Cacaual, Cobra-Cipó, Cobra-Olho-de-Gato, Dormideira, Jararaca, Jararaca-de-Parede, Jararaca-de-Patioba, Jararaca-de-Tabuleiro, Jararaca-do-Rabo-Fino, Jararaquinha, Jiboia-Dormideira, Olho-de-Gato, Rabo-Fino',
    19: 'Cobra-D’água, Cobra-de-Cadarço, Cobra-de-Caçote, Cobra-de-Listra-Vermelha, Corre-Campo',
    20: 'Cobra-Corá, Cobra-Coral, Cobra-de-Coral, Coral, Coral-Verdadeira, Ibiboboca',
    21: 'Boichumbeguaçu, Cobra-Corá, Cobra-Coral, Cobra-Coral-de-Bigode, Cobra-Coral-da-Guiana, Cobra-Coral-Vermelha, Coral, Coral-Verdadeira',
    22: 'Bicuda, Boitiaboia, Cipó, Cipó-Bicuda, Cobra-Bicuda, Cobra-Cipó, Cobra-Cipó-Bicuda, Cobra-Flecha',
    23: 'Bacorá, Boi-Corá, Boicorá, Cobra-Coral, Cobra-Coral-Falsa, Cobra-de-Coral, Coral, Coral-Falsa, Falsa-Coral-de-Barriga-Branca, Falsa-Coral-Tricolor',
    24: 'Cobra-Cipó, Corre-Campo, Surradeira, Tabuleira',
    25: 'Boiubu, Bojobi, Caninana, Cipó-Verde, Cobra-Cipó, Cobra-Cipó-Comum, Cobra-Cipó-Listrada, Cobra-Cipó-Verde, Cobra-Corredeira, Cobra-Facão, Cobra-Papagaio, Cobra-Verde, Cobra-Verde-Lisa, Corre-Campo, Papagaia, Papa-Pinto',
    26: 'Boiru, Boiúna, Cobra-de-Leite, Cobra-Preta, Coral-Falsa, Falsa-Coral, Limpa-Mato, Limpa-Pasto, Mamadeira, Moçurana, Muçurana, Mussurana, Mussurana-Limpa-Campo',
    27: 'Cobra-Corredeira',
    28: 'Cobra-Corredeira, Cobra-Capim, Cobra-do-Capim, Cobra-do-Folhiço, Cobra-Rainha, Corre-Campo, Corredeira-do-Campo, Corredeira-Pintada, Corredeirinha, Jararaquinha',
    29: 'Cinco-Minutos, Cobra-da-Terra, Cobra-do-Folhiço, Cobra-Rainha, Coral-Falsa, Falsa-Cabeça-Preta, Falsa-Coral, Onze-Horas, Tantila',
    30: 'Jararaca, Jararaca-Falsa, Jararaquinha',
    31: 'Cipó-do-Papo-Amarelo, Jararaquinha',
    32: 'Cobra-Espada, Corre-Campo',
    33: 'Araboia, Cainana, Cainana-Flor-de-Algodão, Cainana-Teiú, Caninana, Cobra-Tigre, Cobra-Voadora, Jacaninã, Malha-de-Teiú, Papa-Ovo, Papa-Pinto, Yacaninã',
    34: 'Achatadeira, Boca-de-Caçapa, Boca-de-Capanga, Boipeba, Boipeva, Boipeva-Comum, Boipeva-do-Campo, Boipeva-Grande, Cabeça-de-Patrona, Capitão-do-Campo, Capitão-do-Mato, Cobra-Chata, Corre-Campo, Cotiara, Cururuboia, Esparradeira, Falsa-Jararaca, Focinho-de-Cachorro, Goipeba, Goipeva, Jararaca-Malha-de-Cascavel, Jaracambeva, Jaracuçu, Jaracuçu-Capitão, Jaracuçu-de-Tapiti, Jaracuçu-do-Brejo, Jaracuçu-Dourado, Jaracuçu-Não-Venenoso, Jaracuçu-Tapete, Jararaca, Jararaca-Amarela, Jararacambeva, Jararacuçu-Bolacha, Jararacuçu-Tapiti, Jericá, Jeriquá, Jurucoá, Malha-de-Sapo, Mata-Boi, Pepeua, Pepeva, Surucucu-Cascuda, Urutu, Urutu-Amarelo, Urutu-Falsa, Urutu-Preto, Urutu-Tábua, Urutu-Tapete',
    35: 'Araboia, Cainana, Cainana-Flor-de-Algodão, Cainana-Teiú, Caninana, Cobra-Tigre, Cobra-Voadora, Jacaninã, Malha-de-Teiú, Papa-Ovo, Papa-Pinto, Yacaninã',
    36: 'Cobra-Cega, Cobra-de-Chumbinho',
    37: 'Cobra-de-Leite, Cobra-Preta, Limpa-Mato, Muçurana, Mussurana',
    38: 'Cabeça-Preta, Cabeça-Preta-Coroada, Cabeça-Preta-de-Faixa-Amarela, Cobra-Coral, Cobra-Coroada, Cobra-da-Terra, Cobra-Mineira, Coral-Falsa, Falsa-Coral, Serpente-Coroada',
    39: 'Boicinim, Boicininga, Boiçununga, Boiquira, Cascabel, Cascavé, Cascavel, Cascavel-de-Quatro-Ventas, Cascavelha, Cobra-de-Chocalho, Cobra-de-Guizo, Cobra-do-Chocalho, Maracá, Maracaboia, Maracamboia, Surucucu-Cascavel',
    40: 'Cobra-D’água, Jararaca-D’água',
    41: 'Azulão-Boia, Boiubu, Cobra-Cipó, Cobra-Jericoá, Cobra-Paraíso, Cobra-Papagaio, Cobra-Verde, Jericoá',
    43: 'Cobra-D’água, Cobra-Verde, Jabutuboia, Jararaquinha, Parelheira',
    44: 'Cobra-Coral (juvenil), Cobra-D’água, Cobra-Espada, Jararaquinha, Parelheira, Surucucu-de-Fogo',
    45: 'Coral, Coral-Falsa, Falsa-Coral'
}

conn = get_conn()
cursor = conn.cursor()

add_nome_pop = ("INSERT INTO COBRA_NOME_POP "
                "(idCOBRA, nome) "
                "VALUES (%s, %s)")

for key in nomes_pop:
    nomes = nomes_pop[key].split(', ')
    for nome in nomes:
        data_nomes = (key, nome)
        cursor.execute(add_nome_pop, data_nomes)

conn.commit()

cursor.close()
conn.close()