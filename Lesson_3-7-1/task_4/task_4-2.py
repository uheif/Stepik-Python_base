def cnt(data: list, direct: str):
    return sum([int(data[i][1]) for i in range(len(data)) if data[i][0] == direct])


indata = [input().split() for i in range(int(input()))]
print(cnt(indata, "восток") - cnt(indata, "запад"), cnt(indata, "север") - cnt(indata, "юг"))
