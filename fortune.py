import os
import random

def load_fortune_file(f):
    saved = []
    try:
        with open(f, 'r') as datfile: 
            text = datfile.read()
            for line in text.split('\n%\n'):
                saved.append(line)
    except OSError:
        print('fail to process file: {}'.format(f))
    else:
        return saved

def get_datfiles():
    data_dir = './datfiles'
    cookies = os.listdir(data_dir)
    return cookies

def get_random_topic(cookies):
    return random.choice(cookies)

def get_random_fortune(fortunes):
    return random.choice(fortunes)

def get_fortune():
    prefix = './datfiles'
    cookies = get_datfiles()
    fortune_file = os.path.join(prefix, get_random_topic(cookies))
    data = load_fortune_file(fortune_file)
    return get_random_fortune(data)

