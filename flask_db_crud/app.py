from application import app
from application.models import Games

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
