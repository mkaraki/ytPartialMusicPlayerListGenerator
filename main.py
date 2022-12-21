import yaml
import os
import json


def readData(file, override=[]):
    if ('import' in override):
        override.pop('import')

    with open(file, 'r', encoding='utf-8') as iny:
        yml = yaml.safe_load(iny)

        allitems = []

        for i, ov in enumerate(yml):
            v = dict(override, **ov)

            if ('import' in v):
                allitems.extend(readData(v['import'], v))
                continue

            if (i < len(yml) - 1):
                v['next'] = yml[i + 1]['id']
            else:
                v['next'] = yml[0]['id']

            if (not 'platform' in v):
                v['platform'] = 'yt'

            if (not 'url' in v):
                if (v['platform'] == 'yt'):
                    v['url'] = 'https://www.youtube.com/watch?v=' + v['video']

            allitems.append(v)

        return allitems


allitems = readData('items.yaml')
editedallitems = []

for i, v in enumerate(allitems):
    if (i < len(allitems) - 1):
        v['next'] = allitems[i + 1]['id']
    else:
        v['next'] = allitems[0]['id']

    editedallitems.append(v)

    with open('out/' + v['id'] + '.json', 'w', encoding='utf-8') as ojs:
        json.dump(v, ojs)


with open('out/data.json', 'w', encoding='utf-8') as aojs:
    json.dump(editedallitems, aojs)
