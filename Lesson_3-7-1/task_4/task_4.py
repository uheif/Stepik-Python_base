v_point = h_point = 0

for i in range(int(input())):
    direct: list = input().split()
    k = 1 if direct[0] == "север" or direct[0] == "восток" else -1
    if direct[0] == "север" or "юг":
        v_point += k * int(direct[1])
    else:
        h_point += k * int(direct[1])

print(f"{v_point} - {h_point}")
