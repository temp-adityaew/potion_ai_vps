from flask import Flask

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Definisikan route untuk endpoint '/' dengan method GET
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)
