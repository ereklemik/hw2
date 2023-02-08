import subprocess  as p
import json
# p1 = p.run('ps aux', shell=True, capture_output=True, text=True)

# with open('output.txt', 'w') as f:
#     f.write(p1.stdout)

# with open('output.txt', 'r') as f:
#     result = p.run('grep root | wc -l', stdin=f, capture_output=True, shell=True, text=True)

# print(result.stdout)


# result = p.run('ps aux', capture_output=True, text=True, shell=True)
# processes = result.stdout.splitlines()

# root_processes = [process.split()[10] for process in processes if process.startswith("root")]
# root_processes_dict = {"root": root_processes}

# print(root_processes_dict)


result = p.run("ps aux | awk '/^root/ { print $11 }'", capture_output=True, text=True, shell=True)
root_processes = result.stdout.splitlines()
root_processes_dict = {"root": root_processes}

print(root_processes_dict)