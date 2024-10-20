from app import create_app
from app.users.userweb_controller import UserWebController

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

