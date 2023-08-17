import subprocess
import datetime


result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
output = result.stdout
splitted_output = output.split('\n')

# variables initialization
user_processes = {}
total_memory_used = 0
total_cpu_used = 0.0
max_memory_process = ('', 0)
max_cpu_process = ('', 0.0)

for item in splitted_output:
    if item and not item.startswith('USER'):
        columns = item.split()
        user = columns[0]  # USER
        memory = int(columns[5])  # RSS
        cpu = float(columns[2])  # %CPU

        # counting user values
        if user in user_processes:
            user_processes[user] += 1
        else:
            user_processes[user] = 1

        # counting system values
        total_memory_used += memory
        total_cpu_used += cpu

        # counting max for RSS
        if memory > max_memory_process[1]:
            max_memory_process = (columns[-1][:20], memory)  # slice of last 20 symbols column COMMAND
        # # counting max for CPU
        if cpu > max_cpu_process[1]:
            max_cpu_process = (columns[-1][:20], cpu)  # slice of last 20 symbols column COMMAND


# data for report
report = f"Отчёт о состоянии системы:\n"
report += f"Пользователи системы: {', '.join(user_processes.keys())}\n"
report += f"Процессов запущено: {sum(user_processes.values())}\n"
report += "Пользовательских процессов:\n"
for user, count in user_processes.items():
    report += f"{user}: {count}\n"
report += f"Всего памяти используется: {total_memory_used / 1024:.1f} mb\n"
report += f"Всего CPU используется: {total_cpu_used:.1f}%\n"
report += f"Больше всего памяти использует: ({max_memory_process[0]})\n"
report += f"Больше всего CPU использует: ({max_cpu_process[0]})\n"


# saving report
current_datetime = datetime.datetime.now().strftime('%d-%m-%Y-%H:%M')
file_name = f"{current_datetime}-scan.txt"
with open(file_name, 'w') as file:
    file.write(report)

print(report)
