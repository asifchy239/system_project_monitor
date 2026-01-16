import subprocess
from datetime import datetime
current_time = datetime.now()
cpu_info = subprocess.getoutput("top -bn1 | grep 'Cpu(s)'")
memory_info = subprocess.getoutput("free -m")
log_file = "/var/log/syslog"
count_error = 0
count_warning = 0
with open(log_file,"r") as file:
	for line in file:
		if "ERROR" in line:
			count_error += 1
		if "WARNING" in line:
			count_warning += 1
with open("system_report.txt","w") as report:
    report.write("SYSTEM MONITORING REPORT\n")
    report.write(str(current_time) + "\n\n")

    report.write("CPU INFORMATION:\n")
    report.write(cpu_info + "\n\n")

    report.write("MEMORY INFORMATION:\n")
    report.write(memory_info + "\n\n")

    report.write("LOG SUMMARY:\n")
    report.write(f"Error COunt: {count_error}\n")
    report.write(f"Warning COunt:{count_error}\n")
    print("System report generated successfully")
