from app.Database import dbConnection
from app import app

if __name__ == '__main__':
    app.run(debug=True)

@app.shell_context_processor
def make_shell_context():
    return {'db': dbConnection()}