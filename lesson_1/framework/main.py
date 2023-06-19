class Page_404:
    def __call__(self, request):
        return "404 NOTFOUND", "404 Not Found"


class Framework:
    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj
        print(self.routes_lst)
        print(self.fronts_lst)

    def __call__(self, env, start_response):
        path = env["PATH_INFO"]
        view = self.routes_lst[path] if path in self.routes_lst else Page_404()

        request = {}
        for front in self.fronts_lst:
            front(request)

        code, body = view(request)
        print(path, view, code, body)

        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]
