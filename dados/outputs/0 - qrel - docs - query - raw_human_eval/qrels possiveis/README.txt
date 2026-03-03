- qrel-float.csv: o score é o score calculado com a média das avaliações feitas.
- qrel-int.csv: é o score do qrel-float arredondado (usando round do pandas).

O ideal seria usar qrel-float.csv, mas as ferramentas tradicionais de avaliação (pytrec_eval e pyserini) considerando scores apenas inteiro. Caso seja usado o pyserini para avaliar datasets, ele fará o truncamento do score. Com isso, perdemos muita informação, pois um score de 1.7 ou 1.6 é convertido para 1 em vez de 2.

O qrel do dataset usado é o qrel-int.csv.