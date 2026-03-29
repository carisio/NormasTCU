# NormasTCU

## Overview

NormasTCU iis a dataset for Legal Information Retrieval (LIR) in Brazilian Portuguese composed of normative documents from the Brazilian Federal Court of Accounts (Tribunal de Contas da União - TCU), along with queries and human-annotated relevance judgments.

The dataset includes:
- **14,469 legal documents** (normative acts);
- **46 queries**;
- **812 judge query-document pairs** derived from 3,048 human annotations with 3-level graded relevance.

## Usage

To use the dataset, load que files docs.csv, query.csv, and qrel.csv:

```python
import pandas as pd

docs = pd.read_csv("docs.csv")
queries = pd.read_csv("query.csv")
qrels = pd.read_csv("qrel.csv")
```

## Dataset Structure

The NormasTCU dataset consists of three main files:

```plaintext
NormasTCU/
│── doc.csv               # Corpus
│── query.csv             # Queries
│── qrel.csv              # Relevance judgments for each query
│── raw_human_eval.csv    # Anonymized relevance judgments from each human annotator (before aggregation)
```

### **Documents (`doc.csv`)**
The `doc.csv` file contains **16,045 legal documents** from the TCU's selected jurisprudence. Each row represents a legal document and includes the following fields:

#### Fields of a Document in the Corpus

| Field                     | Description                                                     | Type            | Missing values     |
|--------------------------|-----------------------------------------------------------------|-----------------|--------------------|
| KEY                      | ID                                                              | Text            | --                 |
| UNIDADEBASICAAUTORA      | Superior authoring organizational unit                          | Text            | --                 |
| ORIGEM                   | Source of the normative act                                     | Text            | --                 |
| NUMNORMA                 | Document number                                                 | Text            | --                 |
| ANONORMA                 | Document year                                                   | Text            | --                 |
| TIPONORMA                | Document type                                                   | Text            | --                 |
| TITULO                   | Document title                                                  | Text            | --                 |
| ASSUNTO                  | Subject / summary                                               | Text            | 7,191 (49.70%)     |
| TEXTONORMA               | Full text                                                       | HTML Text       | 5 (0.03%)          |
| DATAINICIOVIGENCIA       | Effective start date                                            | DD/MM/YYYY      | --                 |
| DATAFIMVIGENCIA          | Effective end date                                              | DD/MM/YYYY      | 13,629 (94.19%)    |
| SITUACAO                 | Expressly revoked or in force                                   | Text            | --                 |
| TEXTOANEXO               | Annex of the document                                           | HTML Text       | 13,237 (91.49%)    |
| TEMA                     | Whether the document is about external control or management    | Text            | 3,686 (25.48%)     |
| TAGSVCE                  | Tags                                                            | Text            | 3,849 (26.60%)     |
| NORMARELACIONADA         | Related documents of this dataset                               | Text            | 9,918 (68.55%)     |


### **Queries (`query.csv`)**

The `query.csv` file contains **46 standardized queries**. Each row in the file contains the following fields:

| Field   | Description |
|---------|------------|
| `KEY`    | Unique query identifier |
| `TEXT`  | Query text |

### **Relevance Judgments (qrel.csv)**

The `qrel.csv` file contains relevance assessments for query-document pairs.

Each row in the file contains the following fields:

| Field     | Description                                              |
|-----------|----------------------------------------------------------|
| **QUERY_ID** | Query identifier                                        |
| **DOC_ID**   | Document identifier                                     |
| **SCORE**    | Relevance score (0 = irrelevant, 1 = partially relevant, 2 = relevant)    |

## Citation
If you use the NormasTCU dataset, please cite:

```bibtex
@misc{normastcu2026,
  author    = {Fernandes, Leandro Carísio and 
               de Castro, Marcos Vinícius Borela and 
               Ribeiro, Leandro dos Santos and 
               da Silva Pacheco, Leonardo Augusto and 
               de Oliveira Sandes, Edans Flávius},
  title     = {{NormasTCU}}
}
```

## Contact

- **Leandro Carísio Fernandes**  
  Câmara dos Deputados, Brasília, Brazil  
  Email: [carisio@gmail.com](mailto:carisio@gmail.com)

- **Marcos Vinícius Borela de Castro**  
  Tribunal de Contas da União (TCU), Brasília, Brazil  
  Email: [borela@tcu.gov.br](mailto:borela@tcu.gov.br)

- **Leandro dos Santos Ribeiro**  
  Tribunal de Contas da União (TCU), Brasília, Brazil  
  Email: [leandro.santos.r@gmail.com](mailto:leandro.santos.r@gmail.com)

- **Leonardo Augusto da Silva Pacheco**  
  Tribunal de Contas da União (TCU), Brasília, Brazil  
  Email: [leonardo3108@gmail.com](mailto:leonardo3108@gmail.com)

- **Edans Flávius de Oliveira Sandes**  
  Tribunal de Contas da União (TCU), Brasília, Brazil  
  Email: [edansfs@tcu.gov.br](mailto:edansfs@tcu.gov.br)


## Acknowledgments
We would like to thank the Brazilian Federal Court of Accounts (TCU) for providing the documents and supporting this research.