import os

def check_disk_space():
    disk_usage = os.popen("df -h /").read()
    print("Speicherplatz-Überprüfung:")
    print(disk_usage)

if __name__ == "__main__":
    check_disk_space()
