# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:57:33 2021

@author: PolarBearJ
"""
# Favourites Application

import sqlite3
import webbrowser

conn = sqlite3.connect(":memory:")

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS favourites (title TEXT, url TEXT)''')

def add_fav(title, url):
    c.execute('''INSERT INTO FAVOURITES (title, url) VALUES (?,?)''', (title, url))
    conn.commit()

def remove_fav(title):
    c.execute('''DELETE FROM favourites WHERE title=?''',(title,))
    conn.commit()
    
def get_favs():
    c.execute('''SELECT * FROM favourites''')
    return c.fetchall()

def get_fav(title):
    c.execute('''SELECT * FROM favourites WHERE title=?''', (title,))
    return c.fetchone()



while True:
    response = input("v to visit a favourite, ls for list, add for new, rm to delete, q to quit:\n")
    if response == 'v':
        shortcut = input("Enter the shortcut:\n")
        record = get_fav(shortcut)
        print(record)
        try:
            webbrowser.open(record[1])
        except:
            print("Cannot open")
    elif response == 'ls':
        print(get_favs())
    elif response == 'add':
        destination = input("Where do you want this shortcut to go?:\n")
        shortcut = input("What is the shortcut?:\n")
        add_fav(shortcut, destination)
    elif response == 'rm':
        shortcut = input("What is the shortcut?:\n")
        remove_fav(shortcut)
    elif response == 'q':
        break
