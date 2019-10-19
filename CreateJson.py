import json

name = {'Steve': 'Smith'}
name['Ricky'] = 'Pointing'

Language = ['Python', 'CSharp', 'X++']

name['Language'] = Language

results = json.dumps(name)
print(results)