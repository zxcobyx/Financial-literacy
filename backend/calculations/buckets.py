from backend.services.bucket_service import BucketCalculator
from backend.models.bucket_model import Bucket
from backend.utils.constants import BUCKETS_CONFIG

def create_buckets():
    """
    Создание кувшинов.
    """
    calculator = BucketCalculator()

    # Создание кувшинов
    for bucket_config in BUCKETS_CONFIG:
        bucket = Bucket(bucket_config["name"], bucket_config["percentage"])
        calculator.add_bucket(bucket)

    return calculator

def calculate_buckets(income):
    """
    Расчет сумм для кувшинов.
    """
    calculator = create_buckets()
    return calculator.calculate_buckets(income)
