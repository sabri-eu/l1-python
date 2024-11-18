def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello " + name)

names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names) # Ok!
greet_all(ages) # Error due to incompatible types