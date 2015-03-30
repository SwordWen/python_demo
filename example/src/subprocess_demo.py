import subprocess

def main():
    #cmd_line = "/home/workspace_c/gnugo-3.8/interface/gnugo"
    cmd_line = "/bin/bash /usr/games/gnugo"
    cwd="/home/workspace_c/gnugo-3.8/interface"
    proc = subprocess.Popen(cmd_line,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    proc.communicate()
    pass;

if __name__=="__main__":
    main()