from .configParse import readConf

import psycopg2 
import pandas as pd

def writeDict():
    p = readConf('config.ini')
    con = psycopg2.connect(p)
    cur = con.cursor()
    q = ''
    categories = pd.read_csv('gos_cats.csv').to_dict()
    for cat in categories:
        for c in cat.challenges:
            points = c.val
            c_name = c.name
            c_desc = c.description
        q += f'INSERT INTO gos.challenges (points, name, description) VALUES({points}, \'{c_name}\', \'{c_desc}\')'
    cur.execute(q)
    cur.close()
    con.close()

    
