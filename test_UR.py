from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/2').json())
print(get('http://localhost:5000/api/v2/users/33').json())  # пользователь отсутствует

print(post('http://localhost:5000/api/v2/users').json())  # отсутствует словарь
print(post('http://localhost:5000/api/v2/users', json={'name': 'Scott'}).json())  # выдаёт ошибку
print(post('http://localhost:5000/api/v2/users', json={'name': 'Scott', 'position': 'major',
                                                       'surname': 'Martin', 'age': 43, 'address': 'module_2',
                                                       'speciality': 'research engineer',
                                                       'hashed_password': 'wwww',
                                                       'email': 'scott_major@mars.org'}).json())

print(delete('http://localhost:5000/api/v2/users/67').json())  # пользоатель с таким id отсутствует
