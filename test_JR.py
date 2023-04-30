from requests import get, post, delete

print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/2').json())
print(get('http://localhost:5000/api/v2/jobs/33').json())  # работа с таким id отсутствует

print(post('http://localhost:5000/api/v2/jobs').json())  # отсутствует словарь
print(post('http://localhost:5000/api/v2/jobs', json={'job': 'cooker'}).json())  # выдаёт ошибку
print(post('http://localhost:5000/api/v2/jobs', json={'team_leader': '1', 'job': 'worker 1', 'work_size': '4',
                                                      'collaborators': '2', 'is_finished': False}).json())

print(delete('http://localhost:5000/api/v2/jobs/67').json())  # работа с таким id отсутствует
