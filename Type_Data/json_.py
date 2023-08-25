import json
i = 0
with open('data/purchase_log.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()

        dict_ = json.loads(line)
        print(dict_)

        i += 1
        if i > 5:
            break