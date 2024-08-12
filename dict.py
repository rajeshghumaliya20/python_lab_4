emp = {
    'id': 1,
    'name': 'Ghumaliya Raj',
    'designation': 'Software Engineer',
    'salary': 100000
}
if 'designation' in emp:
    del emp['designation']
emp['name'] = 'Ghumaliya Rajesh'
print(emp)
