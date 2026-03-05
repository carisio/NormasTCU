- qrel-float.csv: o score é o score calculado com a média das avaliações feitas.
- qrel-int.csv: é o score do qrel-float arredondado (usando round do pandas).

O ideal seria usar qrel-float.csv, mas as ferramentas tradicionais de avaliação (pytrec_eval e pyserini) considerando scores apenas inteiro. Caso seja usado o pyserini para avaliar datasets, ele fará o truncamento do score. Com isso, perdemos muita informação, pois um score de 1.7 ou 1.6 é convertido para 1 em vez de 2.

O qrel do dataset usado é o qrel-int.csv.

---------
Nota:
     Os qrels_leave_{anotador}_out.csv é o qrels gerado com 3 anotadores e o {anotador} removido.
     Foram gerados apenas para fazer análise de sensibilidade para rankeamento de sistemas, ou seja, ver o tanto que o ranking muda em relação ao agregado. Na prática, muda muito pouco. A correlação dos ranking gerados com os qrels_leave_{anotador}_out.csv e o qrels do dataset é muito alta, independentemente do anotador que foi removido.