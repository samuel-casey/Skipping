import responder
api = responder.API()
@api.route("/hello/{who}")
def hello_to(req, resp, *, who):
    resp.text = f"hello, {who}!"

@api.route("/hello/{who}/json")
def hello_to(req, resp, *, who):
    resp.media = {"hello": who}

# To render template
# api.route("/hello/{who}/html")
# def hello_html(req, resp, *, who):
#     resp.html = api.template('hello.html', who=who)


api.run()