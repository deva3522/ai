data = [
    ["GREEN", "HARD", "NO", "WRINKLED", "YES"],
    ["ORANGE", "HARD", "YES", "SMOOTH", "NO"],
    ["GREEN", "SOFT", "NO", "WRINKLED", "YES"]
]

h = ['0', '0', '0', '0']

for i in data:
    if h == ['0', '0', '0', '0'] and i[-1] == 'YES':
        h = i[:-1]
    if i[-1] == 'YES':
        for j in range(len(i) - 1):
            if h[j] != i[j]:
                h[j] = '?'
print("Final Hypothesis:", h)
