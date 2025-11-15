import datetime
class SimpleLogMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("SimpleLogMiddleware initialized...")

    def __call__(self, request):
        print("----- Request Log -----")
        print("Time:",datetime.datetime.now())
        print("Path:",request.path)
        print("Method:",request.method)
        print("User:",request.user if request.user.is_authenticated else "Anonymous")
        print("------------------------")

        response = self.get_response(request)

        print("Response status:",response.status_code)

        return response