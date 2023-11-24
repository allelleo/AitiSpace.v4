import random
import string


async def generate_password(length=10):
    return "".join(
        [random.choice(list(string.ascii_letters + string.digits)) for _ in range(length)]
    )
