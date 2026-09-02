import streamlit as st

def show_ratios_dashboard():

st.subheader("📊 Painel de Análise de Rácios")

ratios = {

    "Rácio de Crescimento do Volume de Negócios": {
        "formula": "(Volume de Negócios do Ano Atual - Volume de Negócios do Ano Anterior) / Volume de Negócios do Ano Anterior × 100",
        "description": "Determina o crescimento do volume de vendas. Crescimento rápido pode causar problemas de fluxo de caixa."
    },

    "Margem de Lucro Bruto": {
        "formula": "Lucro Bruto / Vendas × 100",
        "description": "Mostra a percentagem das vendas disponível para cobrir despesas operacionais."
    },

    "Margem de Lucro Líquido": {
        "formula": "Lucro Líquido Após Impostos / Vendas × 100",
        "description": "Indica a percentagem da receita que permanece após todas as despesas."
    },

    "Return on Investment (ROI)": {
        "formula": "Lucro Antes de Juros e Impostos / Total de Passivos & Capital Próprio × 100",
        "description": "Mede o retorno sobre os fundos totais investidos por credores e acionistas."
    },

    "Return on Equity (ROE)": {
        "formula": "Lucro Líquido Após Impostos / Capital Próprio × 100",
        "description": "Mostra o retorno obtido sobre o investimento dos acionistas."
    },

    "Rácio de Liquidez Corrente": {
        "formula": "Ativos Correntes / Passivos Correntes",
        "description": "Mede a capacidade de cumprir obrigações de curto prazo. Ideal: 2:1."
    },

    "Rácio de Liquidez Imediata": {
        "formula": "(Ativos Correntes - Inventário) / Passivos Correntes",
        "description": "Mede a liquidez imediata. Ideal: 1:1."
    },

    "Dias de Rotação de Stock": {
        "formula": "Inventário Final / Custo das Vendas × 365",
        "description": "Mostra quanto tempo o stock demora a ser vendido."
    },

    "Dias de Clientes": {
        "formula": "Contas a Receber / Vendas × 365",
        "description": "Mostra a rapidez com que os clientes pagam."
    },

    "Dias de Fornecedores": {
        "formula": "Contas a Pagar / Compras × 365",
        "description": "Mostra quanto tempo a empresa demora a pagar aos fornecedores."
    },

    "Rácio de Endividamento (Gearing)": {
        "formula": "Total de Passivos / Capital Próprio × 100",
        "description": "Mede o risco financeiro. Menos de 100% é geralmente aceitável."
    },

    "Rácio de Cobertura de Juros": {
        "formula": "Lucro Antes de Juros e Impostos / Despesa de Juros",
        "description": "Mostra a capacidade de pagar juros. Mais de 3 vezes é considerado bom."
    }
}


col1, col2 = st.columns([1, 2])


with col1:

    st.subheader("📌 Rácios")

    selected_ratio = st.radio(
        "Selecione um Rácio",
        list(ratios.keys()),
        key="main_ratios_radio"
    )


with col2:

    st.subheader("📖 Detalhes")

    st.markdown(f"### {selected_ratio}")

    st.write("**Fórmula:**")

    st.info(
        ratios[selected_ratio]["formula"]
    )

    st.write("**O que este rácio nos indica:**")

    st.success(
        ratios[selected_ratio]["description"]
    )
