from arrow import now

tommorow = now().shift(days=1)
print(tommorow)