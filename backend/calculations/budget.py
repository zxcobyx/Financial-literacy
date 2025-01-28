def calculate_budget(income):
    necessary_expenses = income * 0.5
    discretionary_spending = income * 0.3
    savings = income * 0.2
    return {
        'Необходимые расходы': necessary_expenses,
        'Дискреционные расходы': discretionary_spending,
        'Сбережения': savings
    }
