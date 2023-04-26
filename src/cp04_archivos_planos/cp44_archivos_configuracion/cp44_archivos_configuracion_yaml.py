import yaml

print('# ARCHIVO YML CON UN SOLO DOCUMENTO')
with open('config.yml') as f:
    contenido_yml = yaml.load(f, Loader=yaml.SafeLoader)

print(contenido_yml)
print()

print(contenido_yml['stages'][0]['when']['event'][0])
print()

print('# ARCHIVO YML CON MÁS DE UN DOCUMENTO')
lista = []
with open('multi_config.yml') as f:
    contenido_yml = yaml.load_all(f, Loader=yaml.SafeLoader)
    for doc in contenido_yml:
        lista.append(doc)

print(lista[0]['stages'][0]['when']['event'][0])
print(lista[1]['stages'][0]['when']['event'][0])
print()

print('# ESCRIBIR TU PROPIO ARCHIVO YAML')
print()

print('# UN DOCUMENTO')
user_details = {'UserName': 'Alice', 'Password': 'star123*', 'phone': 3256,
                'AccessKeys': ['EmployeeTable', 'SoftwaresList', 'HardwareList']}

with open('mi_archivo.yaml', 'w') as f:
    yaml.safe_dump(user_details, f)

print()

print('# DOS DOCUMENTOS')
user_details = [{'UserName': 'Alice', 'Password': 'star123*', 'phone': 3256,
                 'AccessKeys': ['EmployeeTable', 'SoftwaresList', 'HardwareList']},
                {'UserName': 'Alice', 'Password': 'star123*', 'phone': 3256,
                 'AccessKeys': ['EmployeeTable', 'SoftwaresList', 'HardwareList']}]

with open('mi_archivo_multi.yaml', 'w') as f:
    yaml.safe_dump_all(user_details, f)

# leo el archivo multi documentos para verificar
lista = []
with open('mi_archivo_multi.yaml') as f:
    contenido_yml = yaml.load_all(f, Loader=yaml.SafeLoader)
    for doc in contenido_yml:
        lista.append(doc)
print(lista)