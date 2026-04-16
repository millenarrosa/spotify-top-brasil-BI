# 🎵 Dashboard Spotify Brasil - Business Intelligence

> **Desenvolvido por:** Millena e Manuela

Este projeto consiste num dashboard de Business Intelligence (BI) desenvolvido no **Power BI** para analisar as tendências, artistas e volumes de reprodução das músicas mais ouvidas no Spotify Brasil.

---

## 1. Contexto dos Dados
Este projeto utiliza dados extraídos do Spotify Brasil para analisar o desempenho das músicas mais populares. O conjunto de dados permite uma visão estratégica sobre o consumo musical e a relevância dos artistas no mercado atual, transformando grandes volumes de dados brutos em inteligência competitiva.

## 2. Definição do Escopo

### Escopo dos Dados
* **Incluído:** Dados de performance do Top 50; métricas de volume de streaming; análise de permanência no ranking.
* **Excluído:** Dados demográficos de ouvintes, metadados técnicos de áudio (bpm, key, etc.) e dados financeiros privados.

### Perguntas de Negócio
| Pergunta de Negócio | Objetivo Estratégico |
| :--- | :--- |
| **Quem são os artistas com maior domínio de audiência?** | Identificar artistas estratégicos para campanhas e parcerias. |
| **Quais músicas apresentam maior retenção no ranking?** | Diferenciar hits virais passageiros de sucessos consolidados. |
| **Qual a concentração de plays no Top 10 vs restante da lista?** | Avaliar a competitividade e a barreira de entrada no topo do ranking. |
| **Qual artista tem a melhor eficiência de plays por música?** | Revelar artistas com bases de fãs altamente engajadas. |

## 3. Proposta de Valor
* **Situação Atual:** Análises manuais em tabelas isoladas, dificultando a perceção de tendências e padrões.
* **Benefícios de BI:** Centralização em dashboards interativos que permitem identificar padrões de sucesso instantaneamente através de filtros dinâmicos.
* **Diferencial Estratégico:** Transforma dados brutos em inteligência para otimizar investimentos em marketing e planeamento de novos lançamentos.

---

## 📊 Funcionalidades do Dashboard
O relatório permite visualizar:
* **Ranking de Popularidade:** As músicas com maior número de plays totais.
* **Consistência dos Artistas:** Análise de "dias na lista" para identificar hits duradouros.
* **Métricas de Desempenho:** Total de plays acumulados e análise por data de recolha.
* **Top Artistas:** Identificação dos artistas que mais dominam o top 10.

---

## 📂 Estrutura do Repositório
* `top10_spotify_brasil.pbix`: Arquivo principal do Power BI com o dashboard.
* `dados.csv`: Base de dados (posições, nomes das músicas, artistas, dias na lista e total de plays).
* `/Imagens`: Demonstrações visuais

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Ter o [Microsoft Power BI Desktop](https://powerbi.microsoft.com/desktop/) instalado.

### Passo a Passo
1.  Faça o download ou clone este repositório.
2.  Abra o arquivo `top10_spotify_brasil.pbix` no Power BI Desktop.
3.  **Ajuste da Fonte de Dados (Caso necessário):**
    Se o Power BI exibir um erro de "Fonte de dados não encontrada":
    * Vá ao menu **Página Inicial** > **Transformar Dados** > **Configurações da fonte de dados**.
    * Clique em **Alterar Fonte**.
    * Selecione o caminho local onde salvou o arquivo `dados.csv`.
    * Clique em **Aplicar Alterações**.

---

## 🛠️ Tecnologias Utilizadas
* **Power BI:** Construção de gráficos e ETL (Power Query).
* **CSV:** Fonte de dados estruturada.

---
**Documento de Escopo de BI - Projeto Spotify Brasil** *Trabalho Final de BI elaborado por Millena e Manuela.*
