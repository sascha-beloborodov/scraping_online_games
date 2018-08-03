import pymysql
import os
from functools import reduce
from logger import log_error

db = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    db=os.getenv('DB_NAME')
)

def make_ids_string(matches):
    ids = reduce(lambda prev, match: str(match['match_id']) + ', ' + prev , matches, '')
    ids = ids[:-2]  
    return ids
            

def insert_matches(matches=[]):
    if len(matches) == 0:
        return
    cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        ids = make_ids_string(matches)
        sql = 'SELECT * FROM matches WHERE match_id IN ('+ids+')'
        cursor.execute(sql)
        results = cursor.fetchall()
        exceptIds = list(map(lambda db_match: db_match['match_id'], results))
        filteredMatches = list(filter(lambda match: None if int(match['match_id']) in exceptIds else match, matches))
        if (len(filteredMatches)):
            cursor.executemany("""
                INSERT INTO matches (match_id, date, mode, range_type, winner_type, winner_region, duration_string, duration, radiant_heroes, dire_heroes)
                VALUES (%(match_id)s, %(date)s, %(mode)s, %(range_type)s, %(winner_type)s, %(winner_region)s, %(duration_string)s, %(duration)s, %(radiant_heroes)s, %(dire_heroes)s)""", filteredMatches)
            db.commit()
    except BaseException as err:
        log_error(err)
    finally:
        cursor.close()
        db.close()
    