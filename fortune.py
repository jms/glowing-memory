import os
import random
from flask import current_app as app
from functools import lru_cache

secure_random = random.SystemRandom()

cookies = ['literature',
           'art',
           'medicine',
           'pets',
           'startrek',
           'magic',
           'science',
           'fortunes',
           'news',
           'education',
           'ascii-art',
           'riddles',
           'platitudes',
           'linuxcookie',
           'ethnic',
           'people',
           'law',
           'work',
           'linux',
           'men-women',
           'knghtbrd',
           'zippy',
           'debian',
           'computers',
           'miscellaneous',
           'definitions',
           'love',
           'kids',
           'sports',
           'humorists',
           'politics',
           'wisdom',
           'perl',
           'disclaimer',
           'drugs',
           'food',
           'goedel',
           'paradoxum',
           'cookie']


@lru_cache(maxsize=64)
def load_fortune_file(f: str) -> list:
    """
    load fortunes from a file and return it as list
    """
    saved = []
    try:
        with open(f, 'r') as datfile:
            text = datfile.read()
            for line in text.split('%'):
                if len(line.strip()) > 0:
                    saved.append(line)
    except OSError:
        app.logger.warning('fail to process file: {}'.format(f))
        pass
    else:
        return saved


def get_random_topic(cookies_list: list) -> str:
    """
    Pick a random fortune file
    """
    return secure_random.choice(cookies_list)


def get_random_fortune(fortunes: list) -> str:
    """
    return a random fortune from a list
    """
    return secure_random.choice(fortunes)


def get_fortune() -> str:
    """
    return random fortune
    """
    prefix = './datfiles'
    fortune_file = os.path.join(prefix, get_random_topic(cookies))
    data = load_fortune_file(fortune_file)
    fortune = get_random_fortune(data)
    app.logger.debug(load_fortune_file.cache_info())
    return fortune
