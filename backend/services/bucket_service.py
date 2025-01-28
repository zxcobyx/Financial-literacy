from backend.models.bucket_model import Bucket

class BucketCalculator:
    def __init__(self):
        """
        Инициализация калькулятора кувшинов.
        """
        self.buckets = []

    def add_bucket(self, bucket):
        """
        Добавление кувшина в список.

        :param bucket: Кувшин.
        """
        self.buckets.append(bucket)

    def calculate_buckets(self, income):
        """
        Расчет сумм для всех кувшинов на основе дохода.

        :param income: Доход.
        :return: Словарь с суммами для каждого кувшина.
        """
        result = {}
        for bucket in self.buckets:
            result[bucket.name] = bucket.calculate_amount(income)
        return result
