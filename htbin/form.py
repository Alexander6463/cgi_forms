#!/usr/bin/env python3
import cgi
import html

from database import Planet, Galaxy, Spaceship, SessionLocal


form = cgi.FieldStorage()
session = SessionLocal()

planet_name = html.escape(form.getfirst("planet_name"))
planet_mass = html.escape(form.getfirst("planet_mass"))
planet_galaxy = html.escape(form.getfirst("planet_galaxy"))

if planet_name and planet_mass and planet_galaxy:
    session.add(Planet(name=planet_name, mass=planet_mass, galaxy=planet_galaxy))

galaxy_name = html.escape(form.getvalue("galaxy_name"))
galaxy_age = html.escape(form.getvalue("galaxy_age"))
if galaxy_name and galaxy_age and planet_galaxy:
    session.add(Galaxy(name=galaxy_name, age=galaxy_age))

spaceship_cost = html.escape(form.getvalue("spaceship_cost"))
spaceship_mass = html.escape(form.getvalue("spaceship_mass"))
spaceship_producer = html.escape(form.getvalue("spaceship_producer"))
if planet_name and planet_mass and planet_galaxy:
    session.add(Spaceship(
        cost=spaceship_cost,
        mass=spaceship_mass,
        producer=spaceship_producer
    ))
session.commit()
session.close()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Данные успешно обработаны!</h1>")

print("""</body>
        </html>""")
