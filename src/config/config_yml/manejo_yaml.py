import yaml
"""
SafeLoader: Carga un subconjunto de YAML de forma segura, se usa principalmente si 
    la entrada proviene de una fuente que no es de confianza.
FullLoader: Carga el YAML completo pero evita la ejecución de código arbitrario. 
    Todavía representa un riesgo potencial cuando se usa para la entrada que no es de confianza.
BaseLoader: Carga todos los escalares básicos de YAML como cadenas.
"""

# LEER ARCHIVO YAML
with open('config.yml') as f:
    contenido_yml = yaml.load(f, Loader=yaml.SafeLoader)
print(contenido_yml)
"""
Devolverá:
{'stages': [{'name': 'Build something', 'when': {'branch': 'master', 'event': ['push', 'pull_request']},
'steps': [{'runScriptConfig': {'image': 'busybox', 'shellScript': 'echo ${FIRST_KEY} && echo ${ALIAS_ENV}'},
'env': {'FIRST_KEY': 'VALUE', 'SECOND_KEY': 'VALUE2'},
'envFrom': [{'sourceName': 'my-secret', 'sourceKey': 'secret-key', 'targetKey': 'ALIAS_ENV'}]},
{'runScriptConfig': {'image': 'busybox', 'shellScript': 'date -R'},
'when': {'branch': ['master', 'dev'], 'event': 'push'}}]},
{'name': 'Publish my image', 'steps': [{'publishImageConfig': {'dockerfilePath': './Dockerfile',
'buildContext': '.', 'tag': 'rancher/rancher:v2.0.0', 'pushRemote': True, 'registry': 'reg.example.com'}}]},
{'name': 'Deploy some workloads', 'steps': [{'applyYamlConfig': {'path': './deployment.yaml'}}]}],
'branch': {'include': ['master', 'feature/*'], 'exclude': ['dev']}, 'timeout': 30,
'notification': {'recipients': [{'recipient': '#mychannel', 'notifier': 'c-wdcsr:n-c9pg7'},
{'recipient': 'test@example.com', 'notifier': 'c-wdcsr:n-lkrhd'}],
'condition': ['Failed', 'Success', 'Changed'], 'message': 'my-message'}}
"""
print(contenido_yml['stages'][0]['when']['event'][0])
"""
Devolverá:
push
"""

# LEER UN ARCHIVO YAML QUE CONTENGA VARIOS DOCUMENTOS
lista = []
with open('multi_config.yml') as f:
    contenido_yml = yaml.load_all(f, Loader=yaml.SafeLoader)
    for doc in contenido_yml:
        lista.append(doc)

print(lista[0]['stages'][0]['when']['event'][0])
print(lista[1]['stages'][0]['when']['event'][0])


# ESCRIBIR UN ARCHIVO YAML
user_details = {'UserName': 'Alice',
                'Password': 'star123*',
                'phone': 3256,
                'AccessKeys': ['EmployeeTable',
                               'SoftwaresList',
                               'HardwareList']}

with open('mi_archivo.yaml', 'w') as f:
    yaml.safe_dump(user_details, f)


# ESCRIBIR UN ARCHIVO YAML CON MÚLTIPLES DOCUMENTOS
user_details = [{'UserName': 'Alice',
                'Password': 'star123*',
                'phone': 3256,
                'AccessKeys': ['EmployeeTable',
                               'SoftwaresList',
                               'HardwareList']},
                {'UserName': 'Alice',
                'Password': 'star123*',
                'phone': 3256,
                'AccessKeys': ['EmployeeTable',
                               'SoftwaresList',
                               'HardwareList']}]

with open('mi_archivo_multi.yaml', 'w') as f:
    yaml.safe_dump_all(user_details, f)


# LEER YAML EN FORMATO DE CONJUNTO DE TOKENS
# Sirve tanto para archivos con 1 o más documentos
with open('config.yml') as f:
    contenido_yml = yaml.scan(f, Loader=yaml.SafeLoader)
    for token in contenido_yml:
        print(token)
# Para mayor información: https://pynative.com/python-yaml/#h-python-yaml-load-read-yaml-file

with open('multi_config.yml') as f:
    contenido_yml = yaml.scan(f, Loader=yaml.SafeLoader)
    for token in contenido_yml:
        print(token)