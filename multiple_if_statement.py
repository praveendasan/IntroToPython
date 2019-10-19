province = input('What province do you live in? ')

if province in ('chennai', 'madurai'\
                'nagercoil'):
    tax = .5
elif province.lower() == 'azhagai':
    tax = .4
else:
    tax = .9
print(tax)