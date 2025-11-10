import yaml
from textwrap import indent, fill
import shutil
import argparse

terminal_width = shutil.get_terminal_size(fallback=(80, 20)).columns-10

parser = argparse.ArgumentParser(prog = "Inspect scoring of XPHI TQRI",
                                 description = "Using this tool you can view all items included in XPHI TQRI and inspect the scoring")

parser.add_argument("-p", "--path", help = "Path to the XPHIRQRI.yaml file")
args = parser.parse_args()

with open(args.path, "r") as f:
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
    print(f"{part['name']} - {part['total']}")
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
