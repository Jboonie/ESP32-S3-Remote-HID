import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_httpserver import Server, Request, Response, JSONResponse, Status

m = Mouse(usb_hid.devices)

def leftclick_route(request: Request):
    status = Status(200,"Ok")
    data = {"action":"leftclick"}
    try:
        m.click(Mouse.LEFT_BUTTON)
        data['status'] = '200'
    except:
        code = 500
        status = Status(500,"Failure")
        data['status'] = '500'
    print(data)
    return JSONResponse(request, data, status=status)

def rightclick_route(request: Request):
    status = Status(200,"Ok")
    data = {"action":"rightclick"}
    try:
        m.click(Mouse.RIGHT_BUTTON)
        data['status'] = '200'
    except:
        status = Status(500,"Failure")
        data['status'] = '500'
    print(data)
    return JSONResponse(request, data, status=status)

def move_route(request: Request):
    status = Status(200,"Ok")
    data = {"action":"move"}
    try:
        params = request.query_params
        x = int(params.get('x') or 0)
        y = int(params.get('y') or 0)
        t = int(params.get('t') or 0)
        m.move(x, y, t)
        data['x']=x
        data['y']=y
        data['t']=t
        data['status'] = '200'
    except:
        status = Status(500,"Failure")
        data['params'] = request.query_params
        data['status'] = '500'
    return JSONResponse(request, data, status=status)

def drag_route(request: Request):
    status = Status(200,"Ok")
    data = {"action":"drag"}
    try:
        params = request.query_params
        x = int(params.get('x') or 0)
        y = int(params.get('y') or 0)
        t = int(params.get('t') or 0)
        button = params.get('button') or 'left'

        m.press(Mouse.LEFT_BUTTON)
        if(button == 'left'):
            m.press(Mouse.LEFT_BUTTON)
        if(button == 'right'):
            m.press(Mouse.RIGHT_BUTTON)
        m.move(x, y, t)
        m.release_all()

        data['x']=x
        data['y']=y
        data['t']=t
        data['button']=button
        data['status'] = '200'
    except:
        status = Status(500,"Failure")
        data['params'] = request.query_params
        data['status'] = '500'
    return JSONResponse(request, data, status=status)
