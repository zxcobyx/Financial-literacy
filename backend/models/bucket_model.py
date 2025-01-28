class Bucket:
    def __init__(self, name, percentage):
        """
        Инициализация кувшина.

        :param name: Название кувшина.
        :param percentage: Процент дохода, который будет выделен для этого кувшина.
        """
        self.name = name
        self.percentage = percentage

    def calculate_amount(self, income):
        """
        Расчет суммы для кувшина на основе дохода.

        :param income: Доход.
        :return: Сумма для кувшина.
        """
        return income * (self.percentage / 100)
