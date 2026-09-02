import streamlit as st

from Easy_Ratios_Port import show_ratios_dashboard


# --------------------------------
# Dados Financeiros Base
# --------------------------------

BASE_DATA = {
    "sales": 50_000_000,
    "cost_of_sales": 20_000_000,
    "salaries": 15_000_000,
    "rent": 1_200_000,
    "marketing": 45_000,
    "admin_costs": 3_480_000,
    "tax_rate": 0.27,
    "fixed_assets": 10_411_000,
    "inventory": 450_000,
    "debtors": 435_000,
    "bank": 0,
    "long_term_liabilities": 1_500_000,
    "creditors": 46_000,
    "bank_overdraft": 0,
    "share_capital": 2_249_250,
}


# --------------------------------
# Funcao do Trimestre
# --------------------------------

def run_quarter(quarter_num):

    st.header(
        f"📊 Simulador de Cenários Empresariais - Trimestre {quarter_num}"
    )

    # --------------------------------
    # Copiar dados base
    # --------------------------------

    data = BASE_DATA.copy()

    opening_balance = 0

    cash_from_operations = 0

    cash_from_investments = 0

    cash_from_financing = 0

    # --------------------------------
    # Controlo na Barra Lateral
    # --------------------------------

    st.sidebar.header(
        f"Decisões do Trimestre {quarter_num}"
    )

    scenario1 = st.sidebar.checkbox(
        "Mudar para uma renda mais barata",
        key=f"q{quarter_num}_s1"
    )

    scenario2 = st.sidebar.checkbox(
        "Aumentar o marketing",
        key=f"q{quarter_num}_s2"
    )

    scenario3 = st.sidebar.checkbox(
        "Contratar 2 colaboradores",
        key=f"q{quarter_num}_s3"
    )

    scenario4 = st.sidebar.checkbox(
        "Novo fornecedor",
        key=f"q{quarter_num}_s4"
    )

    scenario5 = st.sidebar.checkbox(
        "Comprar novo computador",
        key=f"q{quarter_num}_s5"
    )

    scenario6 = st.sidebar.checkbox(
        "Aumentar formação e desenvolvimento",
        key=f"q{quarter_num}_s6"
    )

    scenario7 = st.sidebar.checkbox(
        "Aumentar custos de consultoria",
        key=f"q{quarter_num}_s7"
    )

    # --------------------------------
    # Aplicar Cenários
    # --------------------------------

    if scenario1:

        data["rent"] -= 80_000

        data["bank"] += 80_000

        data["creditors"] += 22_000

        cash_from_operations += 80_000

    if scenario2:

        data["marketing"] += 50_000

        data["sales"] += 500_000

        data["bank"] += 450_000

        data["creditors"] += 121_500

        cash_from_operations += 450_000

    if scenario3:

        data["salaries"] += 500_000

        data["sales"] += 2_000_000

        data["bank"] += 1_500_000

        data["creditors"] += 405_000

        cash_from_operations += 1_500_000

    if scenario4:

        data["cost_of_sales"] -= 500_000

        data["bank"] += 500_000

        data["creditors"] += 135_000

        cash_from_operations += 500_000

    if scenario5:

        data["fixed_assets"] += 500_000

        data["bank_overdraft"] += 500_000

        cash_from_investments -= 500_000

    if scenario6:

        data["admin_costs"] += 500_000

        data["sales"] += 1_000_000

        data["bank"] += 500_000

        data["creditors"] += 135_000

        cash_from_operations += 500_000

    if scenario7:

        data["admin_costs"] += 750_000

        data["cost_of_sales"] -= 1_000_000

        data["bank"] += 250_000

        data["creditors"] += 67_500

        cash_from_operations += 250_000

    # --------------------------------
    # Cálculos
    # --------------------------------

    gross_profit = (
        data["sales"]
        - data["cost_of_sales"]
    )

    expenses = (
        data["salaries"]
        + data["rent"]
        + data["marketing"]
        + data["admin_costs"]
    )

    ebt = gross_profit - expenses

    tax = ebt * data["tax_rate"]

    net_profit = ebt - tax

    current_assets = (
        data["inventory"]
        + data["debtors"]
        + data["bank"]
    )

    total_assets = (
        data["fixed_assets"]
        + current_assets
    )

    total_liabilities = (
        data["long_term_liabilities"]
        + data["creditors"]
        + data["bank_overdraft"]
    )

    equity = (
        data["share_capital"]
        + net_profit
    )

    total_equity_liabilities = (
        total_liabilities
        + equity
    )

    closing_balance = (
        opening_balance
        + cash_from_operations
        + cash_from_investments
        + cash_from_financing
    )

    # --------------------------------
    # Rácios do Trimestre
    # --------------------------------

    if data["sales"] != 0:

        gross_profit_ratio = (
            gross_profit / data["sales"]
        )

        net_profit_ratio = (
            net_profit / data["sales"]
        )

        debtors_days = (
            data["debtors"]
            / data["sales"]
        ) * 365

    else:

        gross_profit_ratio = 0

        net_profit_ratio = 0

        debtors_days = 0

    if total_equity_liabilities != 0:

        roi = (
            net_profit
            / total_equity_liabilities
        )

    else:

        roi = 0

    if data["creditors"] != 0:

        current_ratio = (
            current_assets
            / data["creditors"]
        )

    else:

        current_ratio = 0

    if equity != 0:

        debt_to_equity = (
            total_liabilities
            / equity
        )

    else:

        debt_to_equity = 0

    # --------------------------------
    # Demonstração de Resultados
    # --------------------------------

    st.subheader("📄 Demonstração de Resultados")

    st.write(
        f"Vendas: {data['sales']:,.0f}"
    )

    st.write(
        f"Custo das Vendas: {data['cost_of_sales']:,.0f}"
    )

    st.write(
        f"Margem Bruta: {gross_profit:,.0f}"
    )

    st.write(
        f"Resultado Líquido: {net_profit:,.0f}"
    )

    # --------------------------------
    # Balanço
    # --------------------------------

    st.subheader("🏦 Balanço")

    st.write(
        f"Total de Ativos: {total_assets:,.0f}"
    )

    st.write(
        f"Total de Passivos: {total_liabilities:,.0f}"
    )

    st.write(
        f"Capital Próprio: {equity:,.0f}"
    )

    # --------------------------------
    # Fluxo de Caixa
    # --------------------------------

    st.subheader("💰 Fluxo de Caixa")

    st.write(
        f"Saldo Final: {closing_balance:,.0f}"
    )

    # --------------------------------
    # Rácios Financeiros
    # --------------------------------

    st.subheader("📊 Rácios Financeiros")

    st.write(
        f"Rácio de Margem Bruta: {gross_profit_ratio:.2%}"
    )

    st.write(
        f"Rácio de Resultado Líquido: {net_profit_ratio:.2%}"
    )

    st.write(
        f"ROI: {roi:.2%}"
    )

    st.write(
        f"Rácio de Liquidez Corrente: {current_ratio:.2f}"
    )

    st.write(
        f"Prazo Médio de Recebimentos: {debtors_days:.2f} dias"
    )

    st.write(
        f"Rácio Dívida/Capital Próprio: {debt_to_equity:.2f}"
    )

    st.success(
        "✅ Experimente diferentes combinações!"
    )


# --------------------------------
# Executar Um Único Período
# --------------------------------

st.title(
    "🏢 Simulador Financeiro Empresarial"
)

run_quarter(1)


# --------------------------------
# Painel de Análise de Rácios
# Aparece apenas uma vez
# --------------------------------

st.markdown("---")

st.header(
    "📚 Painel de Análise de Rácios"
)

show_ratios_dashboard()
