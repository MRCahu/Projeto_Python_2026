import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(
    page_title="Salary Insights Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo Customizado (Decluttering - Cole Knaflic)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# Cache para carregamento de dados
@st.cache_data
def load_data():
    df = pd.read_csv('../dados/salarios_dados.csv')
    # Renomear colunas para facilitar
    df.columns = [
        'ano', 'nivel_experiencia', 'tipo_contrato', 'cargo', 'salario', 
        'moeda', 'salario_usd', 'residencia_funcionario', 'regime_trabalho', 
        'local_empresa', 'tamanho_empresa', 'pais_iso'
    ]
    return df

df = load_data()

# --- SIDEBAR (Filtros) ---
st.sidebar.header("Filtros Estratégicos")
anos = st.sidebar.multiselect("Selecione os Anos", options=sorted(df['ano'].unique()), default=sorted(df['ano'].unique()))
niveis = st.sidebar.multiselect("Nível de Experiência", options=df['nivel_experiencia'].unique(), default=df['nivel_experiencia'].unique())

# Filtragem
df_filtered = df[(df['ano'].isin(anos)) & (df['nivel_experiencia'].isin(niveis))]

# --- HEADER ---
st.title("📊 Data Salary Insights Dashboard")
st.markdown(f"**Grande Ideia:** Analisar a maturidade e as tendências do mercado global de dados entre {min(anos)} e {max(anos)}.")

# --- KPI SECTION ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total de Registros", f"{len(df_filtered):,}")
with col2:
    st.metric("Média Salarial (USD)", f"${df_filtered['salario_usd'].mean():,.0f}")
with col3:
    st.metric("Mediana Salarial (USD)", f"${df_filtered['salario_usd'].median():,.0f}")
with col4:
    st.metric("Cargos Únicos", df_filtered['cargo'].nunique())

st.divider()

# --- INSIGHT 1: EVOLUÇÃO TEMPORAL ---
st.subheader("1. Evolução e Consolidação do Mercado")
evolucao = df_filtered.groupby('ano')['salario_usd'].median().reset_index()
fig_evolucao = px.line(
    evolucao, x='ano', y='salario_usd',
    title="Mediana Salarial Anual (USD)",
    labels={'salario_usd': 'Salário USD', 'ano': 'Ano'},
    markers=True,
    color_discrete_sequence=['#2c7fb8']
)
fig_evolucao.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_evolucao, use_container_width=True)

st.info("**Insight:** O mercado apresentou um crescimento acelerado até 2024, com uma leve estabilização em 2025, sugerindo uma maturidade nas faixas salariais.")

# --- INSIGHT 2: CARGOS DE ELITE ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("2. Top 10 Cargos por Salário")
    top_cargos = df_filtered.groupby('cargo')['salario_usd'].median().sort_values(ascending=False).head(10).reset_index()
    fig_cargos = px.bar(
        top_cargos, y='cargo', x='salario_usd',
        orientation='h',
        title="Top 10 Cargos (Mediana USD)",
        labels={'salario_usd': 'Salário USD', 'cargo': ''},
        color='salario_usd',
        color_continuous_scale='Blues'
    )
    fig_cargos.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False)
    st.plotly_chart(fig_cargos, use_container_width=True)

with col_right:
    st.subheader("3. Salário por Nível de Experiência")
    exp_order = ['junior', 'pleno', 'senior', 'executivo']
    # Garantir que apenas níveis presentes no filtro apareçam na ordem correta
    current_exp_order = [e for e in exp_order if e in df_filtered['nivel_experiencia'].unique()]
    
    fig_exp = px.box(
        df_filtered, x='nivel_experiencia', y='salario_usd',
        category_orders={"nivel_experiencia": current_exp_order},
        title="Distribuição Salarial por Nível",
        labels={'salario_usd': 'Salário USD', 'nivel_experiencia': 'Nível'},
        color='nivel_experiencia',
        color_discrete_sequence=px.colors.qualitative.Prism
    )
    fig_exp.update_layout(showlegend=False)
    st.plotly_chart(fig_exp, use_container_width=True)

# --- INSIGHT 4: REGIME DE TRABALHO ---
st.subheader("4. O Impacto do Regime de Trabalho")
regime_stats = df_filtered.groupby('regime_trabalho')['salario_usd'].median().sort_values(ascending=False).reset_index()
fig_regime = px.bar(
    regime_stats, x='regime_trabalho', y='salario_usd',
    title="Mediana Salarial por Regime de Trabalho",
    labels={'salario_usd': 'Salário USD', 'regime_trabalho': 'Regime'},
    color='salario_usd',
    color_continuous_scale='Viridis'
)
st.plotly_chart(fig_regime, use_container_width=True)

st.warning("**Insight de Negócio:** Contrariando a expectativa comum, o regime presencial mantém salários competitivos ou superiores ao remoto em diversas categorias, possivelmente devido a custos de vida em hubs tecnológicos.")

# --- TABELA DE DADOS (Observabilidade) ---
with st.expander("Visualizar Dados Brutos (Observabilidade)"):
    st.dataframe(df_filtered.head(100))
    st.write(f"Exibindo 100 de {len(df_filtered)} registros filtrados.")

# Footer
st.markdown("---")
st.markdown("Dashboard desenvolvido para Mauro | Analista de Dados & IA")
