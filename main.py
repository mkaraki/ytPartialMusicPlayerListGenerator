import yaml
import os
import json

with open('items.yaml', 'r', encoding='utf-8') as iny:
    yml = yaml.safe_load(iny)

    allitems = []

    for i, ov in enumerate(yml):
        v = ov
        if (i > 0):
            v['next'] = yml[i - 1]['id']

        if (not 'platform' in v):
            v['platform'] = 'yt'

        if (not 'url' in v):
            if (v['platform'] == 'yt'):
                v['url'] = 'https://www.youtube.com/watch?v=' + v['video']

        allitems.append(v)

        with open('out/' + v['id'] + '.json', 'w', encoding='utf-8') as ojs:
            json.dump(v, ojs)

    with open('out/data.json', 'w', encoding='utf-8') as aojs:
        json.dump(allitems, aojs)
