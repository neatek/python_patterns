import json
from framework.templates import render


class Index:
    def __call__(self, request):
        return "200 OK", render("index.html", date=request.get("date", None))


class Contacts:
    def __call__(self, request):
        # Process request
        print("contacts_request", request)
        if request["data"]:
            with open("contacts.txt", "w") as file1:
                file1.write(json.dumps(request["data"]))

        # Render template
        return "200 OK", render("contact.html")


class Test:
    def __call__(self, request):
        return "200 OK", "test"
