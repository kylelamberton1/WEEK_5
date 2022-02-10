from application import app
from application.models import To_do

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    