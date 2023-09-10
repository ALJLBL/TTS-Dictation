import webbrowser
from app import app
from waitress import serve

def open_browser():
    webbrowser.open_new('http://localhost:8080')

if __name__ == '__main__':
    open_browser()
    serve(app, host='0.0.0.0', port=8080)