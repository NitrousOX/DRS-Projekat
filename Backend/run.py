from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        print(app.url_map)
    socketio.run(app, debug=True)
