v_point = h_point = 0

for i in range(int(input())):
    direct: list = input().split()
    v_point += int(direct[1]) * ((direct[0] == "север") - (direct[0] == "юг"))
    h_point += int(direct[1]) * ((direct[0] == "восток") - (direct[0] == "запад"))

print(h_point, v_point)