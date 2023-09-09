from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render, redirect

# Create your views here.

def init(request):
    try:
        with connection.cursor() as cursor:
            # Create the 'ex00_movies' table if it doesn't already exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex06_movies (
                    episode_nb serial PRIMARY KEY,
                    title varchar(64) UNIQUE NOT NULL,
                    opening_crawl text,
                    director varchar(32) NOT NULL,
                    producer varchar(128) NOT NULL,
                    release_date date NOT NULL,
                    created TIMESTAMP DEFAULT NOW(),
                    updated TIMESTAMP DEFAULT NOW()
                );         
                CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                RETURNS TRIGGER AS $$
                BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
                END;
                $$ language 'plpgsql';
                CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                update_changetimestamp_column();
            """)

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def display(request):
    try:
        with connection.cursor() as cursor:
            # Retrieve all data from the 'ex02_movies' table
            cursor.execute("SELECT * FROM ex06_movies")
            data = cursor.fetchall()

        if not data:
            # If there's no data, display "No data available"
            return HttpResponse("No data available")

        # Define the table headers
        headers = ["Episode Number", "Title", "Opening Crawl", "Director", "Producer", "Release Date"]

        # Create a context dictionary to pass data to the template
        context = {'headers': headers, 'data': data}

        # Render the data using an HTML template
        return render(request, 'ex06/display.html', context)

    except Exception as e:
        # Handle any errors and display an error message
        return HttpResponse(f"An error occurred: {str(e)}")


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
                    INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s)
                """, item)

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
    

def update(request):
    if request.method == 'POST':
        selected_film = request.POST.get('film')
        new_opening_crawl = request.POST.get('new_opening_crawl')
        print(new_opening_crawl) 
        if selected_film is not None and new_opening_crawl is not None:
            try:
                with connection.cursor() as cursor:
                    # Execute a raw SQL UPDATE query
                    sql = "UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s"
                    cursor.execute(sql, [new_opening_crawl, selected_film])
                
                return redirect(display)  # Redirect to a success page
            except Exception as e:
                return HttpResponse(str(e))
    with connection.cursor() as cursor:
        # Retrieve all data from the 'ex02_movies' table
        cursor.execute("SELECT * FROM ex06_movies")
        data = cursor.fetchall()
    return render(request, 'ex06/update.html', {'movies': data})
