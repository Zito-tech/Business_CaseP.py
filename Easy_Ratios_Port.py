 import streamlit as st
 def show_ratios_dashboard():

st.title("📊 Painel de Análise de Rácios")

# Dicionário com os rácios
ratios = {
    "Taxa de Crescimento do Volume de Negócios": {
        "formula": "(Volume de Negócios do Ano Atual - Volume de Negócios do Ano Anterior) / Volume de Negócios do Ano Anterior × 100",
        "description": "Determina o crescimento das vendas. Um crescimento rápido pode causar problemas de tesouraria."
    },
    "Margem Bruta": {
        "formula": "Lucro Bruto / Vendas × 100",
        "description": "Mostra a percentagem das vendas disponível para cobrir despesas operacionais."
    },
    "Margem Líquida": {
        "formula": "Resultado Líquido / Vendas × 100",
        "description": "Indica a percentagem da receita que sobra após todas as despesas."
    },
    "Rentabilidade do Investimento (ROI)": {
        "formula": "Resultado Antes de Juros e Impostos / Total do Passivo e Capital Próprio × 100",
        "description": "Mede o retorno sobre o total de fundos investidos por credores e acionistas."
    },
    "Rentabilidade dos Capitais Próprios (ROE)": {
        "formula": "Resultado Líquido / Capitais Próprios × 100",
        "description": "Mostra o retorno obtido sobre o investimento dos acionistas."
    },
    "Rácio de Liquidez Corrente": {
        "formula": "Ativo Corrente / Passivo Corrente",
        "description": "Mede a capacidade de cumprir obrigações de curto prazo. Ideal: 2:1."
    },
    "Rácio de Liquidez Reduzida": {
        "formula": "(Ativo Corrente - Inventários) / Passivo Corrente",
        "description": "Mede a liquidez imediata. Ideal: 1:1."
    },
    "Prazo Médio de Armazenamento": {
        "formula": "Inventário Final / Custo das Vendas × 365",
        "description": "Mostra quanto tempo o stock demora a ser vendido."
    },
    "Prazo Médio de Recebimentos": {
        "formula": "Clientes / Vendas × 365",
        "description": "Mostra a rapidez com que os clientes pagam."
    },
    "Prazo Médio de Pagamentos": {
        "formula": "Fornecedores / Compras × 365",
        "description": "Mostra quanto tempo a empresa demora a pagar aos fornecedores."
    },
    "Rácio de Endividamento": {
        "formula": "Passivo Total / Capitais Próprios × 100",
        "description": "Mede o risco financeiro. Menos de 100% é geralmente aceitável."
    },
    "Rácio de Cobertura de Juros": {
        "formula": "Resultado Antes de Juros e Impostos / Encargos com Juros",
        "description": "Mostra a capacidade de pagar juros. Mais de 3 vezes é bom."
    }
}

# Layout com duas colunas
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📌 Rácios")
    selected_ratio = st.radio("Seleciona um rácio", list(ratios.keys()))

with col2:
    st.subheader("📖 Detalhes")
    st.markdown(f"### {selected_ratio}")
    st.write("**Fórmula:**")
    st.info(ratios[selected_ratio]["formula"])
    st.write("**O que este rácio indica:**")
    st.success(ratios[selected_ratio]["description"])
