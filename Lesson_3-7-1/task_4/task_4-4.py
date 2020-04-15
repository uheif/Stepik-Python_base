"""итератор"""

[([d[key].append(int(val)) for i in range(int(input())) for key, val in [input().split()]],
  print(sum(d['восток']) - sum(d['запад']), sum(d['север']) - sum(d['юг']))) for d in
 [{'север': [], 'юг': [], 'запад': [], 'восток': []}]]
