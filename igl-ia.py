import random # gerar numeros aleatorios
from sklearn.tree import DecisionTreeClassifier, plot_tree # lib da ia e plot da arvore
import matplotlib.pyplot as plt # lib p mostrar a arvore

x = [] #dataset de analises
y = [] #resposta para decisão

for _ in range(1000): #loop 1000x
    advantage = random.randint(0,1) #gerar numero aleatorio 0 ou 1, (0 = sem vantagem, 1 = com vantagem)
    spike = random.randint(0,1) #gerar numero aleatorio 0 ou 1, (0 = sem spike, 1 = com spike)
    teammates = random.randint(1,5) #gerar numero aleatorio entre 1 e 5,
    tempo = random.randint(10,90) #gerar numero aleatorio entre 10 e 90,

    if spike == 0 and (advantage == 1 or teammates >= 3 or tempo <= 30): #se spike nao tiver plantada e (com: tem vantagem, tem 3 ou mais aliados vivos, tem tempo menor de 30), decição vai ser rush
        decision = 1 #rush
    else: #se nao, decisão vai ser não rush
        decision = 0 #não rush

    x.append([advantage, spike, teammates, tempo])  #ex: 1, 0, 4, 20 (tem vantagem, spike nao plantada, 4 alidados vivos, tempo 20 - menor que trinta)
    y.append(decision) #resposta correta da rodada, baseado nas circunstancias, o algoritmo tem que aprender a analisar padrões entre circunstancias e resposta correta

model = DecisionTreeClassifier(max_depth=4) #model de arvore, max_depth para limitar a arvore e evitar overfitting
model.fit(x, y) #treinando o modelo com os dados de dataset

plt.figure(figsize=(12,8)) #tamanho da figura
plot_tree(
    model,
    feature_names=["vantagem", "spike", "teammates", "tempo"], #nomes das features
    class_names=["não rush", "rush"], #nomes das classes
    filled=True #preencher a arvore com cores
)
plt.show() #mostrar a arvore

round = [[1, 1, 4, 45]] #ex: 1, 1, 4, 45 (tem vantagem, spike plantada, 4 alidados vivos, tempo 45 - maior que trinta)
prediction = model.predict(round) #previsão para a ronda
print(f"Previsão para a ronda: {prediction[0]}")