

def register_view(app, routes, view_func):
    for route in routes:
        app.add_url_rule(route, view_func=view_func)


def register_service(app, service_func):
    pass


def db_query(**kwargs):
    ret = ''
    return ret
