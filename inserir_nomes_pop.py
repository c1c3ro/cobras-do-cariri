#script utilizado para inserir os nomes populares das cobras no banco de dados

from utils.database import *

nomes_pop = {
    0: 'Cobra-Cega, Cobra-Coral, Cobra-Coral-Falsa, Cobra-de-Duas-Cabeças, Coral, Coral-D’Água, Coral-Falsa, Falsa-Coral',
    1: 'Anaconda, Boiuçu, Cobra-de-Veado, Ctaia, Jauacanga, Jiboia, Jiboia-Branca, Jiboia-Cinzenta, Jiboia-da-Cauda-Vermelha, Jiboia-do-Cerrado, Kuong-Kuong, Salamanta-Boi, Suaçu',
    2: 'Boitinga, Cobra-de-Veado, Cobra-Veadeira, Jiboia-Branca, Salamanta, Suaçuboia, Suassuboia, Veadeira',
    3: 'Cobra-Arco-Íris, Jiboia-Arco-Íris, Jiboia, Salamanta, Serpente-de-Veado, Serpente-Furta-Cor, Uaçubói',
    4: 'Acutimboia, Acutioia, Boitipó, Caninana-Marrom-Listrada, Cipó, Cobra-Cipó, Cobra-Espada, Sacaiboia',
    6: 'Cobra-Cipó, Corredeira, Papa-Rato, Rateira',
    7: 'Cobra-Cipó',
    9: 'Bicuda, Boitiaboia, Cipó, Cipó-Bicuda, Cobra-Bicuda, Cobra-Cipó, Cobra-Cipó-Bicuda, Cobra-Flecha',
    10: 'Araboia, Cainana, Cainana-Flor-de-Algodão, Cainana-Teiú, Caninana, Cobra-Tigre, Cobra-Voadora, Jacaninã, Malha-de-Teiú, Papa-Ovo, Papa-Pinto, Yacaninã',
    11: 'Cinco-Minutos, Cobra-da-Terra, Cobra-do-Folhiço, Cobra-Rainha, Coral-Falsa, Falsa-Cabeça-Preta, Falsa-Coral, Onze-Horas, Tantila',
    12: 'Cobra-da-Terra',
    13: 'Cobra-de-Ferrão, Cobra-Rainha, Coral-Falsa, Coralzinha, Falsa-Coral',
    14: 'Cobra-de-Leite, Cobra-Preta, Limpa-Mato, Muçurana, Mussurana',
    15: 'Cobra-D’água, Jararaca-D’água, Surucucurana, Trairamboia',
    17: 'Cobra-D’água, Jararaca-D’água',
    19: 'Cobra-D’água, Cobra-de-Cadarço, Cobra-de-Caçote, Cobra-de-Listra-Vermelha, Corre-Campo',
    21: 'Cobra-D’água, Cobra-Preta, Jararacuçu-D’água, Jararaquinha',
    22: 'Boipeva, Casco-de-Burro, Cobra-Corredeira, Cobra-D’água, Cobra-de-Caçote, Cobra-de-Caçote-Amarela, Cobra-de-Capim, Cobra-de-Jardim, Cobra-de-Lixo, Cobra-do-Capim, Cobra-do-Lixo, Cobra-Lisa, Cobra-Verde, Cobra-Verde-Argentina, Cobra-Verde-do-Capim, Coral-Falsa, Falsa-Coral, Jararaquinha, Parelheira, Peça-Nova, Rainha',
    23: 'Cobra-Cipó, Corre-Campo, Surradeira, Tabuleira',
    24: 'Cobra-D’água, Cobra-Verde, Jabutuboia, Jararaquinha, Parelheira',
    26: 'Cobra-Coral (juvenil), Cobra-D’água, Cobra-Espada, Jararaquinha, Parelheira, Surucucu-de-Fogo',
    27: 'Cobra-D’água, Cobra-Verde, Cobra-Verde-da-Caatinga',
    28: 'Coral, Coral-Falsa, Falsa-Coral',
    30: 'Bacorá, Boi-Corá, Boicorá, Cobra-Coral, Cobra-Coral-Falsa, Cobra-de-Coral, Coral, Coral-Falsa, Falsa-Coral-de-Barriga-Branca, Falsa-Coral-Tricolor',
    31: 'Boiubu, Bojobi, Caninana, Cipó-Verde, Cobra-Cipó, Cobra-Cipó-Comum, Cobra-Cipó-Listrada, Cobra-Cipó-Verde, Cobra-Corredeira, Cobra-Facão, Cobra-Papagaio, Cobra-Verde, Cobra-Verde-Lisa, Corre-Campo, Papagaia, Papa-Pinto',
    32: 'Boiru, Boiúna, Cobra-de-Leite, Cobra-Preta, Coral-Falsa, Falsa-Coral, Limpa-Mato, Limpa-Pasto, Mamadeira, Moçurana, Muçurana, Mussurana, Mussurana-Limpa-Campo',
    33: 'Cobra-Corredeira',
    35: 'Come-Lesma, Dorme-Dorme, Dormideira, Dormideira-de-Jardim, Dorminhoca, Jaracuçu-Dormideira, Jararaca-Preguiçosa, Papa-Lesma, Urutú-Péva, Urutuzinho-Pequeno',
    37: 'Cobra-Corredeira, Cobra-Capim, Cobra-do-Capim, Cobra-do-Folhiço, Cobra-Rainha, Corre-Campo, Corredeira-do-Campo, Corredeira-Pintada, Corredeirinha, Jararaquinha',
    39: 'Cobra-Espada, Corre-Campo',
    40: 'Jararaca, Jararaca-Falsa, Jararaquinha',
    42: 'Cipó-do-Papo-Amarelo, Jararaquinha',
    43: 'Achatadeira, Boca-de-Caçapa, Boca-de-Capanga, Boipeba, Boipeva, Boipeva-Comum, Boipeva-do-Campo, Boipeva-Grande, Cabeça-de-Patrona, Capitão-do-Campo, Capitão-do-Mato, Cobra-Chata, Corre-Campo, Cotiara, Cururuboia, Esparradeira, Falsa-Jararaca, Focinho-de-Cachorro, Goipeba, Goipeva, Jararaca-Malha-de-Cascavel, Jaracambeva, Jaracuçu, Jaracuçu-Capitão, Jaracuçu-de-Tapiti, Jaracuçu-do-Brejo, Jaracuçu-Dourado, Jaracuçu-Não-Venenoso, Jaracuçu-Tapete, Jararaca, Jararaca-Amarela, Jararacambeva, Jararacuçu-Bolacha, Jararacuçu-Tapiti, Jericá, Jeriquá, Jurucoá, Malha-de-Sapo, Mata-Boi, Pepeua, Pepeva, Surucucu-Cascuda, Urutu, Urutu-Amarelo, Urutu-Falsa, Urutu-Preto, Urutu-Tábua, Urutu-Tapete',
    44: 'Cobra-Corá, Cobra-Coral, Cobra-de-Coral, Coral, Coral-Verdadeira, Ibiboboca',
    45: 'Boichumbeguaçu, Cobra-Corá, Cobra-Coral, Cobra-Coral-de-Bigode, Cobra-Coral-da-Guiana, Cobra-Coral-Vermelha, Coral, Coral-Verdadeira',
    46: 'Cobra-Cega, Cobra-de-Chumbinho',
    47: 'Cobra-Chumbo, Cobra-da-Terra, Cobra-de-Chumbinho',
    48: 'Cabeça-de-Capanga, Jararaca, Jararaca-Avermelhada, Jararaca-Malha-de-Cascavel, Jararaca-da-Seca, Jararaca-da-Caatinga, Jararaca-do-Sertão, Jararaca-Rosada, Jararaca-Vermelha, Jararaquinha, Jararacussu, Jararaca-da-Folha-Seca ',
    51: 'Acuambóia, Boca-Podre, Cambéua, Caiçaca, Caiçara, Comboia, Cuamboia, Japoboia, Jaracuçu, Jararaca, Jararaca-Açu, Jararaca-da-Amazônia, Jararaca-do-Amazonas, Jararaca-do-Norte, Jararaca-do-Rabo-Branco, Jararaca-Grão-de-Arroz, Jararacarana, Mapanare, Surucucu, Surucucu-da-Várzea, Surucucu-do-Barranco, Surucucurana',
    52: 'Boicinim, Boicininga, Boiçununga, Boiquira, Cascabel, Cascavé, Cascavel, Cascavel-de-Quatro-Ventas, Cascavelha, Cobra-de-Chocalho, Cobra-de-Guizo, Cobra-do-Chocalho, Maracá, Maracaboia, Maracamboia, Surucucu-Cascavel',
}

# conn = get_conn()
conn = start_conn()
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