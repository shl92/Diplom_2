from faker import Faker


class ProfileMethods:
    @staticmethod
    def generate_user():
        fake = Faker()
        profile = {"email": fake.email(),
                   "password": fake.password(),
                   "name": fake.user_name()}
        return profile
