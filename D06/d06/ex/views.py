from django.shortcuts import render

def homepage(request):
    username = request.session.get('username')
    return render(request, 'ex/homepage.html', {'username': username})
