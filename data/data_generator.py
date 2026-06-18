from faker import Faker
import csv
import random
import enum

fake = Faker()

def get_random_email():
    return fake.email()

def create_contact_form_data():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "subject": fake.sentence(nb_words=3),
        "message": fake.sentence(nb_words=25)
    }

def get_random_product():
    products = []

    with open("data/products_data.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            row["price"] = row["price"].replace("Rs. ", "").strip()
            products.append(row)

    return random.choice(products)

def get_random_product_word():
    products = []

    with open("data/products_data.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            products.append(row)

    random_product = random.choice(products)
    random_product = random_product[0]
    words = random_product.split(" ")
    return random.choice(words)

def get_random_cipher_integer():
    return random.randrange(1,9)

def create_card_information():
    card_number = fake.credit_card_number(card_type=None)
    expiry_date = fake.credit_card_expire(start="+1y", end="+5y")
    cvv = fake.credit_card_security_code()

    return {"card_number": card_number,
            "expiry_date": expiry_date,
            "cvv": cvv}

def get_register_user_form_data():

        country = random.choice(["India", "United States", "Canada", "Australia", "Israel", "New Zeland", "Singapore"])

        return {
            "name": fake.name_male(),
            "email": fake.email(),
            "password": fake.password(),
            "title": "Mr",
            "birth_date": fake.pyint(1,30,1),
            "birth_month": fake.pyint(1,12,1),
            "birth_year": fake.pyint(1940, 2026,1),
            "firstname": fake.first_name_male(),
            "lastname": fake.last_name_male(),
            "address1": fake.address(),
            "country": country,
            "zipcode": fake.zipcode(),
            "state": country,
            "city": fake.city(),
            "mobile_number": fake.phone_number()



    }




