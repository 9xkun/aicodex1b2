from app import create_app
from app.controllers.userweb_controller import UserWebController

app = create_app()

@app.route('/users')
def list_users():
    return UserWebController.list_users()

if __name__ == '__main__':
    app.run(debug=True)

