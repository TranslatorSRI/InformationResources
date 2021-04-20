from biothings_explorer.smartapi_kg.dataload import load_specs
import os
import requests
import json

def makerow(jspec):
    info = jspec['info']
    title = info['title']
    version = info['version']
    description = info['description']
    description = ' '.join(description.split('\n'))
    maxlen = 200
    if len(description) > maxlen:
        description = description[:maxlen]+'...'
    try:
        urls = [ x['url'] for x in jspec['servers'] ]
    except:
        urls = []
    xt = info['x-translator']
    component = xt['component']
    team = xt['team']
    return f'{team}\t{title}\t{description}\t{version}\t{urls}\t{component}\n'

def create_templates():
    """Create Templates for each KP and ARA to fill in"""
    specs = load_specs()
    lines = []
    for spec in specs:
        if not 'x-translator' in spec['info']:
            continue
        lines.append(makerow(spec))
    lines.sort()
    with open('smartapiresources.txt', 'w') as outf:
        for line in lines:
            outf.write(line)

if __name__ == '__main__':
    create_templates()
