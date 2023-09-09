from django.shortcuts import redirect, render
from .models import Movies
from django.http import HttpResponse

# Create your views here.

def populate(request):
    try:
        # Data to be inserted
        data = [
            {
                'episode_nb': 1,
                'title': 'The Phantom Menace',
                'director': 'George Lucas',
                'producer': 'Rick McCallum',
                'release_date': '1999-05-19',
            },
            {
                'episode_nb': 2,
                'title': 'Attack of the Clones',
                'director': 'George Lucas',
                'producer': 'Rick McCallum',
                'release_date': '2002-05-16',
            },
            {
                'episode_nb': 3,
                'title': 'Revenge of the Sith',
                'director': 'George Lucas',
                'producer': 'Rick McCallum',
                'release_date': '2005-05-19',
            },
            {
                'episode_nb': 4,
                'title': 'A New Hope',
                'director': 'George Lucas',
                'producer': 'Gary Kurtz, Rick McCallum',
                'release_date': '1977-05-25',
            },
            {
                'episode_nb': 5,
                'title': 'The Empire Strikes Back',
                'director': 'Irvin Kershner',
                'producer': 'Gary Kurtz, Rick McCallum',
                'release_date': '1980-05-17',
            },
            {
                'episode_nb': 6,
                'title': 'Return of the Jedi',
                'director': 'Richard Marquand',
                'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
                'release_date': '1983-05-25',
            },
            {
                'episode_nb': 7,
                'title': 'The Force Awakens',
                'director': 'J. J. Abrams',
                'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
                'release_date': '2015-12-11',
            },
        ]

        # Insert data into the 'Ex03Movies' model
        for item in data:
            Movies.objects.create(**item)

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
    

def display(request):
    try:
        data = Movies.objects.all()

        if not data:
            return HttpResponse("No data available")

        context = {'data': data}
        return render(request, 'ex05/display.html', context)

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")

def remove(request):
    if request.method == 'POST':
        selected_movie_title = request.POST.get('title')
        print(selected_movie_title)
        try:
            movie_to_remove  = Movies.objects.get(title = selected_movie_title)
            movie_to_remove.delete()
            return redirect(display)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
    remaining = Movies.objects.all()
    if not remaining:
        return HttpResponse("no data available")
    context = {'movies': remaining}
    return (render(request, 'ex05/remove.html', context))
