# IGL-IA: Decisão de Rush no Valorant

Este projeto usa **Machine Learning** (aprendizado de máquina) para simular a decisão de dar **rush** ou **não rush** em uma rodada de Valorant, baseado em algumas condições da partida.

## Como o modelo funciona

- **Algoritmo usado**: `DecisionTreeClassifier` (árvore de decisão) da biblioteca `scikit-learn`.
- **Bibliotecas principais**:
  - `scikit-learn` (`DecisionTreeClassifier` e `plot_tree`)
  - `matplotlib` (para visualizar a árvore de decisão)
  - `random` (para gerar dados de treino aleatórios)

## Dados usados para treinar o modelo

O código gera 1000 exemplos aleatórios com as seguintes variáveis (features):

- `vantagem`:
  - `0` = sem vantagem de jogadores
  - `1` = com vantagem de jogadores
- `spike`:
  - `0` = spike não plantada
  - `1` = spike plantada
- `teammates`:
  - número de aliados vivos (entre 1 e 5)
- `tempo`:
  - tempo restante da rodada (entre 10 e 90 segundos)

A regra usada para definir a decisão correta (rótulo `y`) é:

- Se `spike == 0` **e** (tem vantagem **ou** tem 3 ou mais aliados vivos **ou** tempo menor ou igual a 30), então:
  - decisão = `1` (fazer rush)
- Caso contrário:
  - decisão = `0` (não rush)

Esses pares de entrada (`x`) e saída (`y`) são usados para treinar a árvore de decisão.

## Treinamento do modelo

- O modelo é criado assim:
  - `model = DecisionTreeClassifier(max_depth=4)`
- A árvore é treinada com:
  - `model.fit(x, y)`
- A profundidade máxima (`max_depth=4`) é usada para deixar o modelo mais simples e evitar overfitting.

## Visualização da árvore

O código usa o `plot_tree` e o `matplotlib` para mostrar a árvore de decisão:

- As features usadas são:
  - `"vantagem"`, `"spike"`, `"teammates"`, `"tempo"`
- As classes da saída são:
  - `"não rush"` (0)
  - `"rush"` (1)
- A árvore é exibida em uma figura com cores que indicam as decisões.

## Exemplo de previsão

No final do script, é feita uma previsão para um cenário específico:

- Entrada de exemplo: `[1, 1, 4, 45]`
  - `1` = tem vantagem
  - `1` = spike plantada
  - `4` = quatro aliados vivos
  - `45` = 45 segundos de tempo restante

O modelo responde com:

- `0` = não rush
- ou
- `1` = rush

E imprime no terminal: `Previsão para a ronda: 0` ou `1`, dependendo do que o modelo aprendeu.

## Resumo

Este projeto mostra um exemplo simples de:

- Como gerar dados de treino artificiais para um problema de decisão.
- Como treinar uma árvore de decisão com `scikit-learn`.
- Como visualizar a lógica aprendida pelo modelo com `matplotlib`.
- Como usar o modelo treinado para fazer previsões em novas situações de jogo.

