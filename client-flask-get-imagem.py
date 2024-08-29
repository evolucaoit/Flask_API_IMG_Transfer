import requests
import uuid

# URL do servidor
server_url = 'http://localhost:777'

# Endpoint de login
login_url = f'{server_url}/login'
login_data = {'username': 'admin', 'password': 'admin'}
response = requests.post(login_url, json=login_data)

if response.status_code == 200:
    token = response.json()['token']
    print('Login successful. Token:', token)

    # Endpoint de download de imagem
    img_url = f'{server_url}/img-download'
    headers = {'Authorization': token}
    img_response = requests.get(img_url, headers=headers)

    if img_response.status_code == 200:
        file_name = f'image_{uuid.uuid4().hex}.png'
        with open(file_name, 'wb') as f:
            f.write(img_response.content)
        print(f'Image downloaded successfully and saved as {file_name}')
    else:
        print('Failed to download image:', img_response.json())
else:
    print('Login failed:', response.json())
