import socketpool
import wifi
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_httpserver import Server, Request, Response, JSONResponse, Status, FileResponse
from routes import leftclick_route, rightclick_route, move_route, drag_route

m = Mouse(usb_hid.devices)

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

@server.route("/")
def base(request: Request):
    return FileResponse(request, "index.json", "/www")

@server.route("/leftclick")
def leftclick(request: Request):
    return leftclick_route(request)

@server.route("/rightclick")
def rightclick(request: Request):
    return rightclick_route(request)

@server.route("/move")
def move(request: Request):
    return move_route(request)

@server.route("/drag")
def move(request: Request):
    return drag_route(request)

server.serve_forever(str(wifi.radio.ipv4_address))
