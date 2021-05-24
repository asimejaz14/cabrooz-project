def create_message(status=None, message=None, data=None):
    if status:
        pass
    elif not status:
        status = 500
    return {"status": status, "message": message, "data": data}


def get_default_param(request, key, default):
    key = request.query_params.get(key, request.data.get(key, default))
    return key or default