from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def init(request):
    try:
        with connection.cursor() as cursor:
            # Create the 'ex00_movies' table if it doesn't already exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex04_movies (
                    episode_nb serial PRIMARY KEY,
                    title varchar(64) UNIQUE NOT NULL,
                    opening_crawl text,
                    director varchar(32) NOT NULL,
                    producer varchar(128) NOT NULL,
                    release_date date NOT NULL
                )
            """)

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")



def populate(request):
    try:
        with connection.cursor() as cursor:
            # Insert data into the 'ex02_movies' table
            data = [
                (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
                (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
                (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
                (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
                (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
                (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
                (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
            ]
            
            for item in data:
                cursor.execute("""
                    INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s)
                """, item)

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    try:
        with connection.cursor() as cursor:
            # Retrieve all data from the 'ex02_movies' table
            cursor.execute("SELECT * FROM ex04_movies")
            data = cursor.fetchall()

        if not data:
            # If there's no data, display "No data available"
            return HttpResponse("No data available")

        # Define the table headers
        headers = ["Episode Number", "Title", "Opening Crawl", "Director", "Producer", "Release Date"]

        # Create a context dictionary to pass data to the template
        context = {'headers': headers, 'data': data}

        # Render the data using an HTML template
        return render(request, 'dis.html', context)


    except Exception as e:
        # Handle any errors and display an error message
        return HttpResponse(f"An error occurred: {str(e)}")

def remove(request):
    if request.method == 'POST':
        # Handle form submission to remove a movie (simulated)
        selected_movie_title = request.POST.get('title')
        try:
            with connection.cursor() as cursor:
                # Retrieve all data from the 'ex02_movies' table
                cursor.execute("DELETE FROM ex04_movies WHERE title = %s", [selected_movie_title])    
            return redirect(display)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    # Get the remaining movies (simulated)
    with connection.cursor() as cursor:
    # Retrieve all data from the 'ex02_movies' table
        cursor.execute("SELECT * FROM ex04_movies")
        data = cursor.fetchall()
    remaining_movies = data # Define your movie data here
    if remaining_movies:
        context = {'movies': remaining_movies}
        return render(request, 'remove.html', context)
    else:
        return HttpResponse("No data available")
