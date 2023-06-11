from faker import Faker


faker = Faker('ru_RU')


def generate_city():
    city = faker.city()
    return city
