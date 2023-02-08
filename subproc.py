import subprocess as p

p1 = p.run('ps aux', shell=True, capture_output=True, text=True)

with open('output.txt', 'w') as f:
    f.write(p1.stdout)

with open('output.txt', 'r') as f:
    result = p.run('grep root | wc -l', stdin=f, capture_output=True, shell=True, text=True)

print(result.stdout)

