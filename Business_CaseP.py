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
# Função do Trimestre
# --------------------------------

def run_quarter(quarter_num):

    st.title(
        f"📊 Simulador de Cenários Empresariais - Trimestre {quarter_num}"
    )

    # Copiar dados base
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


