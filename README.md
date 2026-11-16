# Análise de Anúncios de Veículos nos EUA — Dashboard Interativo

Aplicação web interativa desenvolvida como projeto prático da **Sprint 4 (Ferramentas de Desenvolvimento de Software)** do curso de Análise de Dados da **TripleTen**. O projeto consiste na análise exploratória e visualização interativa de dados de anúncios de veículos usados nos Estados Unidos (`vehicles_us.csv`).

🔗 **Acesse a aplicação online:** [Link do App no Render](https://sprint4-tripleten-j9oy.onrender.com/)

---

## Sobre o Projeto

O objetivo principal deste projeto é aplicar práticas de engenharia de software voltadas para dados, incluindo:
- Gerenciamento de ambientes virtuais e controle de versão com **Git** e **GitHub**;
- Análise Exploratória de Dados (EDA) e tratamento de valores ausentes;
- Construção de visualizações interativas com **Plotly Express**;
- Desenvolvimento e deploy de um painel web utilizando **Streamlit** e **Render**.

---

## Conjunto de Dados (`vehicles_us.csv`)

O dataset contém **51.525 registros** e **13 variáveis** descrevendo anúncios de venda de automóveis nos EUA:

| Coluna | Descrição |
| :--- | :--- |
| `price` | Preço anunciado do veículo (USD) |
| `model_year` | Ano de fabricação do modelo |
| `model` | Modelo e marca do veículo |
| `condition` | Estado de conservação (`new`, `like new`, `excellent`, `good`, `fair`, `salvage`) |
| `cylinders` | Número de cilindros do motor |
| `fuel` | Tipo de combustível (`gas`, `diesel`, `hybrid`, `electric`, `other`) |
| `odometer` | Quilometragem registrada no hodômetro (milhas) |
| `transmission` | Tipo de câmbio (`automatic`, `manual`, `other`) |
| `type` | Carroceria/categoria (`SUV`, `sedan`, `truck`, `pickup`, `coupe`, etc.) |
| `paint_color` | Cor externa do veículo |
| `is_4wd` | Indicador de tração nas 4 rodas (`1` = sim, `0` = não) |
| `date_posted` | Data de publicação do anúncio |
| `days_listed` | Quantidade de dias em que o anúncio permaneceu ativo |

---

## Funcionalidades da Aplicação

No painel interativo (`app.py`), o usuário pode explorar o mercado de veículos através de controles dinâmicos:
- **Distribuição de Quilometragem / Preços:** Histograma interativo para avaliar a concentração do estoque por faixa de rodagem ou valor.
- **Relação Preço vs. Quilometragem:** Gráfico de dispersão (*scatter plot*) segmentado por estado de conservação (`condition`), evidenciando a curva de depreciação dos veículos.
- **Análise por Categoria e Cor:** Visualização da distribuição de anúncios por tipo de carroceria e cor externa.

---

## Estrutura do Repositório

```text
sprint4_tripleten/
├── notebooks/
│   └── EDA.ipynb              # Notebook com limpeza, tratamento de nulos e análise exploratória
├── .streamlit/
│   └── config.toml            # Configurações do servidor Streamlit para deploy
├── app.py                     # Código principal da aplicação web Streamlit
├── vehicles_us.csv            # Base de dados utilizada no projeto
├── requirements.txt           # Dependências Python do projeto
└── README.md                  # Documentação do repositório
