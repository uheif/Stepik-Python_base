known = [input().lower() for i in range(int(input()))]
unknown = [word.lower() for i in range(int(input())) for word in input().split() if word.lower() not in known]
print('\n'.join(set(unknown)))