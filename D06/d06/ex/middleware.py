import random
import time

from d06.settings import USERNAMES

class AnonymousUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'username' not in request.session:
            request.session['username'] = random.choice(USERNAMES)
            request.session['username_timestamp'] = time.time()

        if 'username_timestamp' in request.session and time.time() - request.session['username_timestamp'] > 42:
            request.session['username'] = random.choice(USERNAMES)
            request.session['username_timestamp'] = time.time()

        response = self.get_response(request)
        return response
