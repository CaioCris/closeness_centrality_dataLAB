# Closeness centrality #

Desafio - SEMANTIX dataLAB FIAP

## Desafio ##
```
Algoritmo de Proximidade:

Neste desafio, suponha que estamos fazendo uma análise de rede social e queremos extrair dessa rede social uma métrica chamada “Closeness centrality”, também chamada de Proximidade.

Essa métrica tenta aproximar uma medida de influência de um indivíduo dentro de uma rede social.

A distância entre quaisquer dois vértices é o seu caminho mais curto;
A métrica "Distanciamento" de um dado vértice (V) é a soma de todas as distâncias de cada vértice até (V).

A Proximidade de um vértice (V) é o inverso do "Distanciamento".
O desafio é classificar os vértices em um determinado grafo (fornecido no arquivo anexado) pela sua Proximidade. 
Cada linha do arquivo consiste em dois nomes de vértice separados por um único espaço, o que representa uma ligação entre esses dois vértices.
```

## Instalação (Python 2.7 ou Python 3.6) ##

Para MAC e Windowns:
https://www.python.org/downloads/

```
No Linux(Ubuntu) o Python 2.7 já veem instalado, mas pode ser atualizado para o 3.6!

Versões 14.04 e 16.04:

sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6

16.10 acima:

sudo apt-get update
sudo apt-get install python3.6

```

## Pandas e Numpy ##
```
Para Python 2.x:

Pandas:
pip install pandas

Numpy:
pip install numpy

Para Python 3.x:

Pandas:
pip3 install pandas

Numpy:
pip3 install numpy

Caso acontece algum erro quanto a MAC e Linux na instalação, utilize sudo antes do pip.

```

## Running ##
```
#!bash
cd closeness_centrality_dataLAB
python main.py (Python 2.7)
python3 main.py (Python 3.6)
```

### Solução ###

Não foi utilizado nenhum paco de processamento de grafos, como o networkx, apenas os pacotes numpy e pandas.

Foi utilizado o algoritmo BFS ou [Bread-First Search](https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/the-breadth-first-search-algorithm), conhecido como Busca em Largura em portugues, [Um algoritmo de busca em grafos utilizado para realizar uma busca ou travessia num grafo e estrutura de dados do tipo árvore. Intuitivamente, você começa pelo vértice raiz e explora todos os vértices vizinhoz.](https://pt.wikipedia.org/wiki/Busca_em_largura)
