from faker import Faker

f = Faker()
for _ in range(100):
    print(f.email())

