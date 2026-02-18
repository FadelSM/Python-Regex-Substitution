import re

n = int(input())
for _ in range(n):
    line = input()
    # Replace '&&' surrounded by spaces with 'and'
    line = re.sub(r'(?<=\s)(&&)(?=\s)', 'and', line)
    # Replace '||' surrounded by spaces with 'or'
    line = re.sub(r'(?<=\s)(\|\|)(?=\s)', 'or', line)
    print(line)
