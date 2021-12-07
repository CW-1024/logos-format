import sys
from subprocess import Popen, PIPE, STDOUT
filterList = ["%hook","%end","%log","%orig","%class","%new","%init", "%ctor","%group","%subclass"]
fileContentsList = sys.stdin.read().splitlines()
newList = []
for line in fileContentsList:
    if any(token in line for token in filterList):
            newList.append("/* clang-format off */")
            newList.append(line)
            newList.append("/* clang-format on */")
    else:
            newList.append(line)
command = ["clang-format"] + sys.argv[1:]
process = Popen(command, stdout=PIPE, stderr=None, stdin=PIPE)
stdoutData = process.communicate(input= "\n".join(newList).encode())[0]
refinedArr = stdoutData.decode().splitlines()
for line in refinedArr:
    if "/* clang-format off */" not in line and "/* clang-format on */" not in line:
        print(line)
