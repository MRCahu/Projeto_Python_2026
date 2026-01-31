# 📊 Dashboard de Análise Salarial no Mercado de Dados

Este projeto contém o código-fonte e o dataset utilizados para a Análise Exploratória de Dados (EDA) e a construção de um Dashboard Interativo de Salários no Mercado Global de Dados.

O objetivo é fornecer insights estratégicos sobre a evolução salarial, a remuneração por nível de experiência e a comparação entre regimes de trabalho (remoto vs. presencial), seguindo as melhores práticas de **Storytelling com Dados** (Cole Knaflic) e **Análise de Negócio** (Cathy Tanimura).

---

## 🛠️ Estrutura do Projeto

O projeto segue um padrão de organização modular e profissional:

| Diretório | Conteúdo |
| :--- | :--- |
| `dados/` | Contém o dataset original (`salarios_dados.csv`). |
| `scripts/` | Contém o script principal do dashboard (`dashboard_salarios.py`). |
| `requirements.txt` | Lista de dependências Python com versões fixas para reprodutibilidade. |
| `README.md` | Documentação do projeto. |

---

## 🚀 Como Executar o Dashboard

Para rodar o dashboard localmente, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.8+ recomendada).

### 2. Instalação das Dependências

Navegue até o diretório raiz do projeto e instale as bibliotecas necessárias. As versões são fixadas para garantir a compatibilidade:

```bash
pip install -r requirements.txt
```

### 3. Execução

Execute o script do Streamlit a partir do diretório raiz do projeto:

```bash
streamlit run scripts/dashboard_salarios.py
```

O dashboard será aberto automaticamente no seu navegador padrão (geralmente em `http://localhost:8501`).

---

## 💡 Insights Chave (Storytelling)

A análise focou em três grandes áreas de interesse estratégico:

### 1. Evolução do Mercado (2020-2025)
*   **Insight:** O mercado de dados experimentou um crescimento salarial acentuado até 2024, com uma subsequente **estabilização em 2025**. Isso sugere que o setor está amadurecendo e as faixas salariais estão se consolidando.

### 2. Hierarquia Salarial e Cargos de Elite
*   **Insight:** Cargos de **Engenharia de Machine Learning** e **Pesquisa (Research Scientist)** apresentam as medianas salariais mais altas, indicando a valorização de habilidades em Inteligência Artificial e Modelagem Avançada.
*   **Fundação Estrutural (Thomas Nield):** A diferença salarial entre níveis (`junior`, `pleno`, `senior`, `executivo`) é clara e bem definida, validando a progressão de carreira no setor.

### 3. Regime de Trabalho (Análise de Negócio)
*   **Insight:** A mediana salarial para o regime **Presencial** é ligeiramente superior ao **Remoto**. Isso pode ser um indicativo de que as empresas que pagam os salários mais altos (Big Techs em hubs caros) ainda priorizam o modelo presencial ou híbrido, ou que o custo de vida nesses locais é refletido na remuneração.

---

## ✅ Checklist de Qualidade (Observabilidade)

Este projeto foi validado com base nos pilares de Observabilidade de Dados (Barr Moses):

| Pilar | Status | Detalhes |
| :--- | :--- | :--- |
| **Freshness** | OK | Dados atualizados até 2025. |
| **Volume** | OK | Base robusta com mais de 133 mil registros. |
| **Schema** | OK | Tipos de dados consistentes (após tratamento inicial). |
| **Distribution** | OK | Baixa incidência de valores nulos. |
| **Qualidade** | Alerta | Presença de *outliers* (salários muito altos) que foram tratados visualmente com Boxplots (Cole Knaflic) para não distorcer a análise de mediana. |

---

**Desenvolvido por:** Manus AI, para Mauro (Analista de Dados & IA).
