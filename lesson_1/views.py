from framework.templates import render


class Index:
    def __call__(self, request):
        # return "200 OK", "test"
        return "200 OK", render("index.html", date=request.get("date", None))


class Test:
    def __call__(self, request):
        return "200 OK", "test"
