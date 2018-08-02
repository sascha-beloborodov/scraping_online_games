import pymysql
import os

db = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    db=os.getenv('DB_NAME')
)

def insert_matches(matches=[]):
    if len(matches) == 0:
        return
    try:
        cursor = db.cursor()
        cursor.executemany("""
            INSERT INTO matches (match_id, date, mode, range_type, winner_type, winner_region, duration_string, duration, radiant_heroes, dire_heroes)
            VALUES (%(match_id)s, %(date)s, %(mode)s, %(range_type)s, %(winner_type)s, %(winner_region)s, %(duration_string)s, %(duration)s, %(radiant_heroes)s, %(dire_heroes)s)""", matches)
        db.commit()
        cursor.close()
        db.close()
    except BaseException as err:
        print(err)
    