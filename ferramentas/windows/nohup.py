import sys
from subprocess import Popen, PIPE

CREATE_NEW_PROCESS_GROUP = 0x00000200
DETACHED_PROCESS = 0x00000008

def main():
    if len(sys.argv) > 0:
        print "executando o processo ",sys.argv
        #processo = Popen(["cmd.exe","/c",sys.argv[1:]], creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,  shell=True, close_fds=True)
        processo = Popen(["cmd.exe","/c",sys.argv[1:]] , stdin=PIPE, stdout=PIPE, stderr=PIPE,creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,  shell=True, close_fds=True)
        print "PID do processo"
        print(processo.pid)
    else:
        print "Voce deve fornece ao menos 1 arqumento, por exemplo o nome do programa que quer executar...\n"

if __name__ == "__main__":
    main()
