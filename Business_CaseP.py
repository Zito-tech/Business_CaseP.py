from Easy_Ratios_Port import show_ratios_dashboard
import streamlit as st

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Análise de Rácios Financeiros",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# NAVEGAÇÃO DA PÁGINA
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "intro"


def go(page):
    st.session_state.page = page
    st.rerun()

# ============================================================
# INTRODUÇÃO
# ============================================================

INTRO_TEXT = """
## Introdução

A Análise de Rácios é utilizada para analisar demonstrações financeiras
porque facilita a medição e compreensão do desempenho de uma empresa.

### Principais razões incluem:

1. Simplificar informação financeira complexa.
2. Medir a rentabilidade.
3. Avaliar a liquidez.
4. Avaliar a solvência e o risco financeiro.
5. Analisar a eficiência através de comparações ano a ano.
"""

# ============================================================
# DADOS DO NEGÓCIO
# ============================================================

BASE_DATA = {
    "sales": 50_000_000,
    "cost_of_sales": 20_000_000,
    "salaries": 15_000_000,
    "rent": 1_200_000,
    "marketing": 45_000,
    "admin_costs": 3_480_000,
    "interest_paid": 80_000,
    "tax_rate": 0.27,

    "fixed_assets": 10_411_000,
    "inventory": 450_000,
    "debtors": 435_000,
    "bank": 0,

    "long_term_liabilities": 1_500_000,
    "creditors": 46_000,
    "bank_overdraft": 0,

    "share_capital": 2_307_650,
}

# ============================================================
# CÁLCULO DOS RESULTADOS FINANCEIROS
# ============================================================

def calculate_business():

    data = BASE_DATA.copy()

    # --------------------------------------------------------
    # Demonstração de Resultados
    # --------------------------------------------------------

    gross_profit = data["sales"] - data["cost_of_sales"]

    operating_expenses = (
        data["salaries"]
        + data["rent"]
        + data["marketing"]
        + data["admin_costs"]
    )

    operating_profit = gross_profit - operating_expenses

    profit_before_tax = operating_profit - data["interest_paid"]

    tax = profit_before_tax * data["tax_rate"]

    net_profit = profit_before_tax - tax

    # --------------------------------------------------------
    # Ativos
    # --------------------------------------------------------

    total_assets = (
        data["fixed_assets"]
        + data["inventory"]
        + data["debtors"]
        + data["bank"]
    )

    current_assets = (
        data["inventory"]
        + data["debtors"]
        + data["bank"]
    )

    # --------------------------------------------------------
    # Passivos
    # --------------------------------------------------------

    current_liabilities = (
        data["creditors"]
        + data["bank_overdraft"]
    )

    total_liabilities = (
        data["creditors"]
        + data["bank_overdraft"]
        + data["long_term_liabilities"]
    )

    # --------------------------------------------------------
    # Capital Próprio
    # --------------------------------------------------------

    equity = data["share_capital"] + net_profit

    # --------------------------------------------------------
    # Rácios
    # --------------------------------------------------------

    gross_profit_margin = gross_profit / data["sales"] * 100
    net_profit_margin = net_profit / data["sales"] * 100
    roi = net_profit / total_assets * 100

    current_ratio = (
        current_assets / current_liabilities
        if current_liabilities != 0 else 0
    )

    debtors_days = data["debtors"] / data["sales"] * 365

    debt_to_equity = (
        total_liabilities / equity
        if equity != 0 else 0
    )

    # --------------------------------------------------------
    # Verificação do Balanço
    # --------------------------------------------------------

    total_equity_and_liabilities = equity + total_liabilities

    balance_difference = total_assets - total_equity_and_liabilities

    return {
        "data": data,

        "gross_profit": gross_profit,
        "operating_expenses": operating_expenses,
        "operating_profit": operating_profit,
        "profit_before_tax": profit_before_tax,
        "tax": tax,
        "net_profit": net_profit,

        "total_assets": total_assets,
        "current_assets": current_assets,
        "current_liabilities": current_liabilities,
        "total_liabilities": total_liabilities,
        "equity": equity,

        "gross_profit_margin": gross_profit_margin,
        "net_profit_margin": net_profit_margin,
        "roi": roi,
        "current_ratio": current_ratio,
        "debtors_days": debtors_days,
        "debt_to_equity": debt_to_equity,

        "total_equity_and_liabilities": total_equity_and_liabilities,
        "balance_difference": balance_difference,
    }

# ============================================================
# GUIA DE RÁCIOS
# ============================================================

def show_ratios_dashboard():

    st.title("📚 Guia de Análise de Rácios")

    st.write(
        "Selecione um rácio abaixo para ver a fórmula, "
        "descrição e interpretação."
    )

    ratios = {

        "Margem de Lucro Bruto": {
            "formula": "Lucro Bruto ÷ Vendas × 100",
            "description": "Mostra a percentagem das vendas que permanece após deduzir o custo das vendas.",
            "interpretation": "Uma margem de lucro bruto mais elevada indica melhor controlo sobre o custo das vendas."
        },

        "Margem de Lucro Líquido": {
            "formula": "Lucro Líquido ÷ Vendas × 100",
            "description": "Mostra a percentagem das vendas que permanece como lucro final após despesas, juros e impostos.",
            "interpretation": "Uma margem de lucro líquido mais elevada indica maior rentabilidade global."
        },

        "ROI": {
            "formula": "Lucro Líquido ÷ Ativos Totais × 100",
            "description": "Mede o retorno obtido a partir dos ativos utilizados pela empresa.",
            "interpretation": "Um ROI mais elevado indica utilização mais eficaz dos ativos."
        },

        "Rácio Corrente": {
            "formula": "Ativos Correntes ÷ Passivos Correntes",
            "description": "Mede a capacidade da empresa para cumprir obrigações de curto prazo.",
            "interpretation": "Um rácio corrente mais elevado indica maior liquidez de curto prazo."
        },

        "Dias de Clientes": {
            "formula": "Clientes ÷ Vendas × 365",
            "description": "Mede o número médio de dias necessários para receber pagamentos dos clientes.",
            "interpretation": "Dias de clientes mais baixos indicam cobranças mais rápidas."
        },

        "Dívida para Capital Próprio": {
            "formula": "Passivos Totais ÷ Capital Próprio",
            "description": "Mede o risco financeiro comparando passivos com capital próprio.",
            "interpretation": "Um rácio mais elevado indica maior alavancagem e risco financeiro."
        }
    }

    selected = st.selectbox(
        "📌 Selecionar Rácio",
        list(ratios.keys()),
        key="ratio_selector"
    )

    ratio = ratios[selected]

    st.divider()

    st.subheader(f"📊 {selected}")

    st.info(f"**Fórmula:** {ratio['formula']}")
    st.success(f"**Descrição:** {ratio['description']}")
    st.warning(f"**Interpretação:** {ratio['interpretation']}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏠 Introdução", use_container_width=True):
            go("intro")

    with col2:
        if st.button("🏢 Simulação Empresarial", use_container_width=True):
            go("simulation")

# ============================================================
# RESET DO QUIZ
# ============================================================

def reset_quiz():

    st.session_state.quiz_index = 0
    st.session_state.quiz_score = 0
    st.session_state.quiz_submitted = False
    st.session_state.last_answer_correct = False

    keys_to_remove = [
        key for key in st.session_state.keys()
        if key.startswith("student_answer_")
    ]

    for key in keys_to_remove:
        del st.session_state[key]

# ============================================================
# QUIZ DO ESTUDANTE
# ============================================================

def show_student_quiz(results):

    st.divider()

    st.header("🎓 Atividade de Rácios para Estudantes")

    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0

    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0

    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    if "last_answer_correct" not in st.session_state:
        st.session_state.last_answer_correct = False

    quiz = [

        {
            "name": "Margem de Lucro Bruto",
            "formula": "Lucro Bruto ÷ Vendas × 100",
            "answer": results["gross_profit_margin"],
            "unit": "%"
        },

        {
            "name": "Margem de Lucro Líquido",
            "formula": "Lucro Líquido ÷ Vendas × 100",
            "answer": results["net_profit_margin"],
            "unit": "%"
        },

        {
            "name": "ROI",
            "formula": "Lucro Líquido ÷ Ativos Totais × 100",
            "answer": results["roi"],
            "unit": "%"
        },

        {
            "name": "Rácio Corrente",
            "formula": "Ativos Correntes ÷ Passivos Correntes",
            "answer": results["current_ratio"],
            "unit": ""
        },

        {
            "name": "Dias de Clientes",
            "formula": "Clientes ÷ Vendas × 365",
            "answer": results["debtors_days"],
            "unit": " dias"
        },

        {
            "name": "Dívida para Capital Próprio",
            "formula": "Passivos Totais ÷ Capital Próprio",
            "answer": results["debt_to_equity"],
            "unit": ""
        }
    ]

    total_questions = len(quiz)
    current_index = st.session_state.quiz_index

    if current_index >= total_questions:

        st.success("🎉 Quiz Concluído!")

        score = st.session_state.quiz_score
        percentage = score / total_questions * 100

        st.metric("Pontuação Final", f"{score} / {total_questions}")
        st.metric("Percentagem", f"{percentage:.0f}%")

        if percentage >= 80:
            st.balloons()
            st.success("🌟 Excelente trabalho!")
        elif percentage >= 50:
            st.info("👍 Bom esforço. Continua a praticar.")
        else:
            st.warning("📖 Continua a praticar os cálculos de rácios.")

        if st.button("🔄 Reiniciar Quiz", use_container_width=True):
            reset_quiz()
            st.rerun()

        return

    question = quiz[current_index]

    st.subheader(f"Pergunta {current_index + 1} de {total_questions}")

    st.progress((current_index + 1) / total_questions)

    st.markdown(f"### {question['name']}")
    st.info(f"**Fórmula:** {question['formula']}")

    answer_key = f"student_answer_{current_index}"

    student_answer = st.number_input(
        "Introduz a tua resposta:",
        min_value=0.0,
        step=0.01,
        format="%.2f",
        key=answer_key,
        disabled=st.session_state.quiz_submitted
    )

    if not st.session_state.quiz_submitted:

        if st.button("📤 Submeter Resposta", use_container_width=True):

            correct_answer = question["answer"]

            if abs(student_answer - correct_answer) < 0.1:
                st.session_state.quiz_score += 1
                st.session_state.last_answer_correct = True
            else:
                st.session_state.last_answer_correct = False

            st.session_state.quiz_submitted = True
            st.rerun()

    if st.session_state.quiz_submitted:

        correct_answer = question["answer"]

        st.divider()

        if st.session_state.last_answer_correct:
            st.success("✅ Correto! Muito bem.")
            st.write(f"A tua resposta: **{student_answer:.2f}{question['unit']}**")
        else:
            st.error("❌ Incorreto.")
            st.write(f"A tua resposta: **{student_answer:.2f}{question['unit']}**")
            st.info(f"A resposta correta é: **{correct_answer:.2f}{question['unit']}**")

        if current_index < total_questions - 1:
            if st.button("➡️ Próxima Pergunta", use_container_width=True):
                st.session_state.quiz_index += 1
                st.session_state.quiz_submitted = False
                st.session_state.last_answer_correct = False
                st.rerun()
        else:
            if st.button("🏁 Terminar Quiz", use_container_width=True):
                st.session_state.quiz_index += 1
                st.session_state.quiz_submitted = False
                st.rerun()

# ============================================================
# SIMULAÇÃO EMPRESARIAL
# ============================================================

def run_year():

    results = calculate_business()
    data = results["data"]

    st.title("🏢 Simulação Empresarial")

    st.write(
        "Utiliza a informação financeira abaixo para analisar "
        "o desempenho da empresa."
    )

    # ========================================================
    # DEMONSTRAÇÃO DE RESULTADOS
    # ========================================================

    st.header("📄 Demonstração de Resultados")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Vendas:** R{data['sales']:,.0f}")
        st.write(f"**Custo das Vendas:** R{data['cost_of_sales']:,.0f}")
        st.write(f"**Lucro Bruto:** R{results['gross_profit']:,.0f}")
        st.write(f"**Despesas Operacionais:** R{results['operating_expenses']:,.0f}")

    with col2:
        st.write(f"**Lucro Operacional:** R{results['operating_profit']:,.0f}")
        st.write(f"**Juros Pagos:** R{data['interest_paid']:,.0f}")
        st.write(f"**Lucro Antes de Impostos:** R{results['profit_before_tax']:,.0f}")
        st.write(f"**Imposto:** R{results['tax']:,.0f}")
        st.write(f"**Lucro Líquido:** R{results['net_profit']:,.0f}")

    # ========================================================
    # BALANÇO
    # ========================================================

    st.divider()

    st.header("📑 Balanço")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Ativos")
        st.write(f"Ativos Fixos: R{data['fixed_assets']:,.0f}")
        st.write(f"Inventário: R{data['inventory']:,.0f}")
        st.write(f"Clientes: R{data['debtors']:,.0f}")
        st.write(f"Banco: R{data['bank']:,.0f}")
        st.success(f"Total dos Ativos: R{results['total_assets']:,.0f}")

    with col2:
        st.subheader("Capital Próprio & Passivos")
        st.write(f"Capital Social: R{data['share_capital']:,.0f}")
        st.write(f"Lucro Líquido: R{results['net_profit']:,.0f}")
        st.write(f"Credores: R{data['creditors']:,.0f}")
        st.write(f"Descoberto Bancário: R{data['bank_overdraft']:,.0f}")
        st.write(f"Passivos de Longo Prazo: R{data['long_term_liabilities']:,.0f}")
        st.success(f"Total Capital Próprio + Passivos: R{results['total_equity_and_liabilities']:,.0f}")

    # ========================================================
    # RÁCIOS CALCULADOS
    # ========================================================

    st.divider()

    st.header("📊 Rácios Calculados")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Margem de Lucro Bruto", f"{results['gross_profit_margin']:.2f}%")
        st.metric("Margem de Lucro Líquido", f"{results['net_profit_margin']:.2f}%")

    with col2:
        st.metric("ROI", f"{results['roi']:.2f}%")
        st.metric("Rácio Corrente", f"{results['current_ratio']:.2f}")

    with col3:
        st.metric("Dias de Clientes", f"{results['debtors_days']:.2f} dias")
        st.metric("Dívida para Capital Próprio", f"{results['debt_to_equity']:.2f}")

    # ========================================================
    # VERIFICAÇÃO DO BALANÇO
    # ========================================================

    st.divider()

    st.subheader("⚖️ Verificação do Balanço")

    difference = results["balance_difference"]

    if abs(difference) < 1:
        st.success("✅ O Balanço está equilibrado.")
    else:
        st.error(f"❌ O Balanço não está equilibrado. Diferença: R{difference:,.2f}")

    # ========================================================
    # QUIZ DO ESTUDANTE
    # ========================================================

    show_student_quiz(results)
# ========================================================
# NAVEGAÇÃO
# ========================================================

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "📚 Guia de Rácios",
        use_container_width=True
    ):

        go("ratios")

with col2:

    if st.button(
        "🏠 Introdução",
        use_container_width=True
    ):

        go("intro")


# ============================================================
# PÁGINA DE INTRODUÇÃO
# ============================================================

def show_intro():

    st.title("📊 Análise de Rácios Financeiros")

    st.markdown(INTRO_TEXT)

    st.divider()

    st.subheader("Escolha uma Atividade")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📚 Guia de Análise de Rácios",
            use_container_width=True
        ):

            go("ratios")

    with col2:

        if st.button(
            "🏢 Simulação de Negócio",
            use_container_width=True
        ):

            go("simulation")


# ============================================================
# ROTEAMENTO PRINCIPAL
# ============================================================

page = st.session_state.page

if page == "intro":

    show_intro()

elif page == "ratios":

    show_ratios_dashboard()

elif page == "simulation":

    run_year()

