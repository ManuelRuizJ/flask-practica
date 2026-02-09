from app import create_app

app = create_app()
c = app.test_client()

r = c.get('/login')
print('GET /login', r.status_code)

r = c.post('/login', data={'username':'admin','password':'admin'}, follow_redirects=False)
print('POST admin/admin', r.status_code, r.headers.get('Location'))

r = c.post('/login', data={'username':'foo','password':'bar'}, follow_redirects=True)
print('POST invalid (follow redirects)', r.status_code)
print('Response contains Credenciales:', b'Credenciales' in r.data)
