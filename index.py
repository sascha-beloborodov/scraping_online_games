from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from libs.db import insert_matches
import json
from libs.logger import log_error
load_dotenv()

def simple_get(url, headers={}):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True, headers=headers)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def last_matches():
    url_matches = os.getenv('MATCHES_URL')
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    raw_html = simple_get(url_matches, headers=headers)
    soup = BeautifulSoup(raw_html, 'html.parser')
    matchesList = []
    for i, tr in enumerate(soup.find_all('tr')):
        match = {}
        try:
            for j, td in enumerate(tr.find_all('td')):
                try:
                    # Match ID col
                    if j == 0:
                        match['match_id'] = td.find('a').text
                        match['date'] = td.find('time')['datetime'][:-6]
                    # game mode col
                    elif j == 1:
                        match['mode'] = td.text
                        match['range_type'] = td.find('div').text
                    # result
                    elif j == 2:
                        match['winner_type'] = td.find('a').text
                        match['winner_region'] = td.find('div').text
                    # duration
                    elif j == 3:
                        match['duration_string'] = td.text
                        duration_list = td.text.split(':')
                        duration_in_sec = 0
                        for k, time_val in enumerate(reversed(duration_list)):
                            # seconds
                            if k == 0:
                                duration_in_sec += int(time_val)
                            if k == 1:
                                duration_in_sec += int(time_val) * 60
                            if k == 3:
                                duration_in_sec += int(time_val) * 3600
                        match['duration'] = duration_in_sec
                    # radiant team
                    elif j == 4:
                        match['radiant_heroes'] = json.dumps( list(map(lambda div: div.find('img')['title'] , td.find_all('div'))) )
                    # dire team
                    elif j == 5:
                        match['dire_heroes'] = json.dumps( list(map(lambda div: div.find('img')['title'] , td.find_all('div'))) )
                except BaseException as err:
                    log_error(err)
                    continue
            if (len(match)):
                match['created_at'] = datetime.today().strftime('%Y%m%d %H:%I:%S')
                match['updated_at'] = datetime.today().strftime('%Y%m%d %H:%I:%S')
                matchesList.append(match)
        except BaseException as detail:
            log_error(detail)
            continue;
    return matchesList

insert_matches(last_matches())