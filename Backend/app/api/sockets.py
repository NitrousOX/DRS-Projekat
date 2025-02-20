from flask_socketio import  emit

def init_sockets(socketio):
    @socketio.on('connect')
    def handle_connect():
        print('Client connected')
        emit('connected', {'data': 'You are connected!'})
    
    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')
    
    @socketio.on('client_message')
    def handle_client_message(data):
        print('Received message from client:', data)
        emit('server_response', {'data': 'Message received!'})
