from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def init(request):
    try:
        with connection.cursor() as cursor:
            # Create the 'ex00_movies' table if it doesn't already exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex00_movies (
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
