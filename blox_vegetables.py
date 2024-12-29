import random

fruit1 = "Common: rocket"
fruit2 = "Legendary: quake"
fruit3 = "Mithyc: T-rex"
fruit4 = "Common: bomb"
fruit5 = "Legendary: buddha"
fruit6 = "Mithyc: kitsune"
fruit7 = "Sweetok: dragon rework"

all_fruits = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7]
chances = [75, 45, 25, 80, 15, 3, 1]
result = random.choices(all_fruits, weights=chances, k=1)[0]

print(result)