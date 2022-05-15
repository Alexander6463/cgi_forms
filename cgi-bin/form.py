#!/usr/bin/env python3
import cgi

from sqlalchemy.orm import Session

from database import Planet, Galaxy, Spaceship


form = cgi.FieldStorage()
session = Session()

action = form.getfirst("action")

planet_name = form.getfirst("planet_name", "")
planet_mass = form.getfirst("planet_mass", "")
planet_galaxy = form.getfirst("planet_galaxy", "")

if planet_name and planet_mass and planet_galaxy:
    session.add(Planet(name=planet_name, mass=planet_mass, galaxy=planet_galaxy))

galaxy_name = form.getvalue("galaxy_name", "")
galaxy_age = form.getvalue("galaxy_age", "")
if galaxy_name and galaxy_age and planet_galaxy:
    session.add(Galaxy(name=galaxy_name, age=galaxy_age))

spaceship_cost = form.getvalue("spaceship_cost", "")
spaceship_mass = form.getvalue("spaceship_mass", "")
spaceship_producer = form.getvalue("spaceship_producer", "")
if planet_name and planet_mass and planet_galaxy:
    session.add(Spaceship(
        cost=spaceship_cost,
        mass=spaceship_mass,
        producer=spaceship_producer
    ))

session.commit()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT_1: {}</p>".format(action))
print("<p>TEXT_1: {}</p>".format(action))

print("""</body>
        </html>""")