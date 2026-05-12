import random
import string


class StringGenerator:
    @staticmethod
    def generate_random_string(length: int) -> str:
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
