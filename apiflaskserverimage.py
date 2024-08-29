from flask import Flask, jsonify, request, send_file
import jwt
import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

# Endpoint para autenticação
@app.route('/login', methods=['POST'])
def login():
    auth_data = request.json
    if auth_data['username'] == 'admin' and auth_data['password'] == 'admin':
        token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

# Endpoint para download de imagem
@app.route('/img-download', methods=['GET'])
def img_download():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 403
    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired!'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token!'}), 403

    # Serve the image file
    return send_file('data.png', as_attachment=True)

if __name__ == '__main__':
    app.run(port=777)
