from waitress import serve
import webserver

if __name__ == '__main__':
    serve(webserver.app, port=80)