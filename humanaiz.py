from arrow import now

hum = now().humanize()

print(hum)
print(now().dehumanize(hum))