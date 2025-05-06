# Arbitary keyword arguments
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}:{value}")
# Calling the function with arbitary keyword arguments
describe_person(name="Raman", age=30, city ="New York", profession="Engineer")
