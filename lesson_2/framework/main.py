from quopri import decodestring
from framework.requests import GetRequests, PostRequests


class Page_404:
    def __call__(self, request):
        return "404 NOTFOUND", "404 Not Found"


class Framework:
    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj
        print(self.routes_lst)
        print(self.fronts_lst)

    @staticmethod
    def get_request(env):
        request = {}
        method = env["REQUEST_METHOD"]
        request["method"] = method

        if method == "POST":
            data = PostRequests().get_request_params(env)
            request["data"] = Framework.decode_value(data)
            print(f"Нам пришёл post-запрос: {Framework.decode_value(data)}")

        if method == "GET":
            request_params = GetRequests().get_request_params(env)
            request["request_params"] = Framework.decode_value(request_params)
            print(
                f"Нам пришли GET-параметры:"
                f" {Framework.decode_value(request_params)}"
            )

        return request

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace("%", "=").replace("+", " "), "UTF-8")
            val_decode_str = decodestring(val).decode("UTF-8")
            new_data[k] = val_decode_str
        return new_data

    def __call__(self, env, start_response):
        path = env["PATH_INFO"]
        view = self.routes_lst[path] if path in self.routes_lst else Page_404()

        # print(env)
        request = self.get_request(env)
        for front in self.fronts_lst:
            front(request)

        code, body = view(request)
        # print(path, view, code, body)

        start_response(code, [("Content-Type", "text/html")])
        return [body.encode("utf-8")]
