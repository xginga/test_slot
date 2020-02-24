def has_duplicates2(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique_list)

ls = []
key = []
value = []
with open('./sample.csv','r') as f:
    for s_line in f:
        ls.append(s_line)

for i in ls:
    key_tmp, value_tmp = i.split(",")
    key.append(key_tmp)
    value.append(value_tmp.strip())

d = dict(zip(key,value))
for i in d:
    print(i, d[i])

