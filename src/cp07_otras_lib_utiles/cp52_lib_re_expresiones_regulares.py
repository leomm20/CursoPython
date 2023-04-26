import re

# patron = r'\sN\w{3}-\d{5}\s'
# o bien
# patron = re.compile(r'\sN\w{3}-\d{5}\s')

patron = re.compile(r'\sN\w{3}-\d{5}\s', re.IGNORECASE)

texto = 'se juega al fútbol martes y jueves'
patron = r'martes|jueves'
print(re.findall(patron, texto))
print()

texto = 'bla bla bla Nert-85948 bla bla bla Nirh-444453 ja eoi Nirh-43453 oi'
patron = r'\sN\w{3}-\d{5}\s'
print(re.search(patron, texto))
print()

print(re.search(patron, texto).group())
print()
patron = r'\s(N\w{3})-(\d{5})\s'
print(re.search(patron, texto).group(1))
print(re.search(patron, texto).group(2))
print()

print(re.search(patron, texto).span())
print()

print(re.findall(patron, texto))
print()

for e in re.finditer(patron, texto):
    print(e.group())
print()

