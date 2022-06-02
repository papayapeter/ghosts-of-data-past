"""runs a flask websocket server"""

import os
from threading import Lock
import flask
from flask import Flask
from flask_socketio import SocketIO
import redis
import shortuuid
import time

# flask & socketio setup
app = Flask(
    __name__, static_url_path='', static_folder=os.path.join('site', 'build')
    )
app.config.from_object('config.DevConfig')
socketio = SocketIO(app)

# threading
thread = None
thread_lock = Lock()


# background task function
def chat():
    print('connecting to redis database')
    database = redis.Redis(host='localhost', port=6379, db=0)
    subscriber = database.pubsub()
    subscriber.psubscribe('__keyspace@0__:*')

    while True:
        message = subscriber.get_message()
        if message:
            # get the key of the changed item
            key = str(message['channel']).split(':', 1)[1].strip('\'')

            if '*' not in key:
                # get writing event updates
                print(key)
                if 'writing' in key:
                    writing_state = database.hgetall(key)
                    print(key, int(writing_state[b'state'].decode('utf-8')))
                    socketio.emit(
                        'writing_state',
                        {
                            'writer': writing_state[b'writer'].decode('utf-8'),
                            'state':
                            int(writing_state[b'state'].decode('utf-8'))
                            }
                        )
                # get incoming messages
                else:
                    chat_message = database.hgetall(key)
                    socketio.emit(
                        'chat_message',
                        {
                            'id': key,
                            'sender': chat_message[b'sender'].decode('utf-8'),
                            'text': chat_message[b'text'].decode('utf-8'),
                            'imageData': chat_message[b'image_data'],
                            'alt': chat_message[b'alt'].decode('utf-8'),
                            'timestamp': int(time.time() * 1000)
                            }
                        )
        socketio.sleep(0.1)


# on connect start the background thread (if it's the first connect)
@socketio.on('connect')
def connect():
    print('client connected')
    global thread
    with thread_lock:
        if thread is None:
            print('starting background thread')
            thread = socketio.start_background_task(chat)


# index page
@app.route('/')
def index():
    return flask.send_file('site/build/index.html')


# about page
@app.route('/about')
def about():
    return flask.send_file('site/build/about.html')


# run server
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
    # socketio.run(app)