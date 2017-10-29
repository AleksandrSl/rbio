from statistics import mean
exs = {}
genes = []

with open('edata.csv') as in_f:
    samples = in_f.readline().split('","')[1:]
    for name in samples:
        exs[name] = []

    for line in in_f:
        elements = line.strip().split(',')
        gene = elements[0]
        data = list(map(int, elements[1:]))
        if mean(data) > 100:
            genes.append(gene)
            for k, sample in enumerate(samples):
                exs[sample].append(data[k])


# print(exs.keys())
sorted_exs = {}
for name in samples:
    sorted_exs[name] = [i for i in exs[name]]
    sorted_exs[name].sort()
# sorted_exs = {key: sorted(value) for key, value in exs.items()}

print(sorted_exs['NA06985'])
