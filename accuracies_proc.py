log_path = "/data/w2b/accuracies.log"
sem_accs = dict()
synt_accs = dict()
current_header = None
header_match = "[INFO] Current vec len "
sem_match = "Semantic accuracy: "
synt_match = "Syntactic accuracy: "
for l in open(log_path, "r").readlines():
    l = str(l)
    if l.startswith(header_match):
        current_header = l[len(header_match):-1]
    if sem_match in l:
        sem_offset = l.index(sem_match) + len(sem_match)
        synt_offset = l.index(synt_match) + len(synt_match)

        new_sem_val = l[sem_offset:l.find(" ", sem_offset)]
        new_synt_val = l[synt_offset:l.find(" ", synt_offset)]
        try:
            sem_accs[current_header].append(new_sem_val)
            synt_accs[current_header].append(new_synt_val)
        except KeyError:
            sem_accs[current_header] = [new_sem_val]
            synt_accs[current_header] = [new_synt_val]

import pandas as pd

sem_accs = pd.DataFrame(sem_accs)
synt_accs = pd.DataFrame(synt_accs)

print()
