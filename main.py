import random

greetings = ["Hello there", "Servus", "Guten Tag", "Moin", "Hai", "Apa kabar?", "Punten", "Salam", "Konichiwa", "Salute", "Ciao"]

number = random.randint(0, len(greetings) - 1)

print(f"The greeting you get is {greetings[number]}")