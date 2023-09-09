from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.
def init(request):
    try:
        with connection.cursor() as cursor:
            # Create the 'ex00_movies' table if it doesn't already exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex08_planets (
                    id serial PRIMARY KEY,
                    name varchar(64) UNIQUE NOT NULL,
                    climate varchar,
                    diameter int,
                    orbital_period int,
                    population bigint,
                    rotation_period int,
                    surface_water real,
                    terrain varchar(128)
               );
                           """ )
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex08_people (
                    id serial PRIMARY KEY,
                    name varchar(64) unique NOT NULL,
                    birth_year varchar(32),
                    gender varchar(32),
                    eye_color varchar(32),
                    hair_color varchar(32),
                    height int,
                    mass real,
                    homeworld VARCHAR(64) REFERENCES ex08_planets(name)
               );
                           """ )
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def readline(line):
    line  = line.split('\t')
    people = {
    'name':  line[0].strip() if line[0].strip() != 'NULL' else None,
    'birth_year':  line[1].strip() if line[1].strip() != 'NULL' else None,
    'gender':  line[2].strip() if line[2].strip() != 'NULL' else None,
    'eye_color':  line[3].strip() if line[3].strip() != 'NULL' else None,
    'hair_color':  line[4].strip() if line[4].strip() != 'NULL' else None,
    'height':  line[5].strip() if line[5].strip() != 'NULL' else None,
    'mass':  line[6].strip() if line[6].strip() != 'NULL' else None,
    'homeworld':  line[7].strip() if line[7].strip() != 'NULL' else None,
    }

    return people


def readplanets(line):
    line  = line.split('\t')
    planet = {
        'name' : line[0].strip() if line[0].strip() != 'NULL' else None,
        'climate' : line[1].strip() if line[1].strip() != 'NULL' else None,
        'diameter' : line[2].strip() if line[2].strip() != 'NULL' else None,
        'orbital_period': line[3].strip() if line[3].strip() != 'NULL' else None,
        'population': line[4].strip() if line[4].strip() != 'NULL' else None,
        'rotation_period': line[5].strip() if line[5].strip() != 'NULL' else None,
        'surface_water': line[6].strip() if line[6].strip() != 'NULL' else None,
        'terrain': line[7].strip() if line[7].strip() != 'NULL' else None,
    }
    return planet    

def populate(request):
    with open('data/people.csv') as f:
        people = [readline(line) for line in f.readlines()]
    with open('data/planets.csv') as f:
        planets = [readplanets(line) for line in f.readlines()]

    try:
        with connection.cursor() as cursor:
            for planet in planets:
                cursor.execute("""
                INSERT INTO ex08_planets (name, climate, diameter, orbital_period, population, rotation_period, \
                            surface_water, terrain)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, [planet['name'], planet['climate'], planet['diameter'], planet['orbital_period'], planet['population'], \
                    planet['rotation_period'], planet['surface_water'], planet['terrain']])
                
        with connection.cursor() as cursor:
            for person in people:
                cursor.execute("""
                INSERT INTO ex08_people (name, birth_year, gender, eye_color, hair_color, height, \
                            mass, homeworld)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, [person['name'], person['birth_year'], person['gender'], person['eye_color'], person['hair_color'], \
                    person['height'], person['mass'], person['homeworld']])
        return HttpResponse("ok")
    except Exception as e:
        return HttpResponse(str(e))
    
def display(request):
    sql_query = """
        SELECT
            p.name AS character_name,
            pl.name AS homeworld,
            pl.climate
        FROM
            ex08_people p
        LEFT JOIN
            ex08_planets pl ON p.homeworld = pl.name
        WHERE
            pl.climate
            LIKE '%windy%'    
        ORDER BY
            p.name
        """
    try:  
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            characters = cursor.fetchall()
        context = {'characters_data': characters}
        return render(request, 'ex08/display.html', context)
    except Exception as e:
        return HttpResponse(f"error: {str(e)}")