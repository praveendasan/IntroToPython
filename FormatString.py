 # string formatting in python
firstname = 'Praveen'
lastName = 'Dasan'

# output = 'Hello, ' + firstname + ' ' + lastName
# output = 'Hello, {} {}'.format(firstname, lastName)
# output = 'Hello, {1} {0}'.format(firstname, lastName)
output = f'Hello, {firstname} {lastName}'
print(output)