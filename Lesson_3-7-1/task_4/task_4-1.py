data = {"восток": 0, "запад": 0, "север": 0, "юг": 0}
for i in range(int(input())):
    indata = input().split()
    data[indata[0]] += int(indata[1])

print(data["восток"] - data["запад"], data["север"] - data["юг"])
