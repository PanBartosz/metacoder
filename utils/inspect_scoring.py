import yaml
from textwrap import indent, fill
import shutil

terminal_width = shutil.get_terminal_size(fallback=(80, 20)).columns-10

with open("../translations.yaml", "r") as f:
    t = yaml.safe_load(f)

for part in t['parts']:
    total = 0
    for question in part['questions']:
        choices = t['q'][question]['choices']
        try:
            max_points = max([choice[2] for choice in choices])
        except:
            print(question)
            exit()
        total = total + max_points
    part['total'] = total
for part in t['parts']:
    print(f"{part['name']}")
    for question in part['questions']:
        head = t['q'][question]['head'].strip("#").strip()
        choices = t['q'][question]['choices']
        max_points = max([choice[2] for choice in choices])
        qpoints_str = f"({round(max_points*100 / part['total'], 2)}%) "
        print(f"{indent(fill(qpoints_str + head, width=terminal_width), '')}")
        for choice in choices:
            points = choice[2]
            points_str = f"[{choice[2]}] "
            print(f"{indent(fill(points_str + choice[1], width=terminal_width), '        ')}")
    print("\n")