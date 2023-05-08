import random


def generate_otp():
    generated_otp = ""
    for i in range(6):
        generated_otp += str(random.randint(0, 9))
    return generated_otp
