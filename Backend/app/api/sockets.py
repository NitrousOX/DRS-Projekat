from flask_socketio import SocketIO

def init_sockets(socketio):
    @socketio.on('connect')
    def handle_connect():
        print('Client connected')

    @socketio.on('message')
    def handle_message(data):
        print('Received message:', data)
        socketio.emit('response', 'Server received your message: ' + data)
