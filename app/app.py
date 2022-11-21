from flask import Flask,render_template
import socket
import os
import logging

env_user = os.environ.get('SA_USER')
print("environment variable user is:", env_user)

env_password = os.environ.get('SA_PASSWORD')
print("environment variable password is:", env_password)

if env_user == 'abcd':
                    print('user matching')
else:
    print('user not matching')    

if env_password == 'abcd':
                    print('password matching')
else:
    print('password not matching')    

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        env_password = os.environ.get('SA_PASSWORD')
        logging.info('Password is:')
        logging.info(env_password)
        return render_template('index.html', hostname=host_name, ip=host_ip, env=env_password)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
