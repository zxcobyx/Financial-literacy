# Константы для процентов кувшинов
NECESSARY_EXPENSES_PERCENTAGE = 55
SELF_CARE_PERCENTAGE = 10
EDUCATION_PERCENTAGE = 10
SAVINGS_PERCENTAGE = 10
INVESTMENTS_PERCENTAGE = 10
GIFTS = 5

# Список кувшинов с их процентами
BUCKETS_CONFIG = [
    {"name": "Необходимые расходы", "percentage": NECESSARY_EXPENSES_PERCENTAGE},
    {"name": "Забота о себе", "percentage": SELF_CARE_PERCENTAGE},
    {"name": "Образование", "percentage": EDUCATION_PERCENTAGE},
    {"name": "Копилка", "percentage": SAVINGS_PERCENTAGE},
    {"name": "Инвестиции", "percentage": INVESTMENTS_PERCENTAGE},
    {"name": "Подарки и благотворительность", "percentage": GIFTS},
]

# Константы для процентов бюджета 50/30/20
OBLIGATORY_EXPENSES_PERCENTAGE = 50
ENTERTAINMENT_PERCENTAGE = 30
DEBTS_PERCENTAGE = 20

# Список категорий бюджета с их процентами
BUDGET_CONFIG = [
    {"name": "Обязательные расходы", "percentage": OBLIGATORY_EXPENSES_PERCENTAGE},
    {"name": "Развлечения, хобби, путешествия", "percentage": ENTERTAINMENT_PERCENTAGE},
    {"name": "Кредиты и займы", "percentage": DEBTS_PERCENTAGE},
]