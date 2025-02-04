import subprocess, signal

matrixProc = subprocess.Popen(['sudo', 'python3', '-m', 'matrix.matrixControl'], # The matrix process
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,  # Capture stdout (optional)
                              stderr=subprocess.PIPE,
                              text=True,
                              bufsize=1)

def controlMatrix(args):
    global matrixProc

    if matrixProc.poll() is None:
        matrixProc.stdin.write(args + '\n')


def quitMatrix():
    matrixProc.send_signal(signal.SIGINT) # This is extremely poor practice, and should be fixed

def dispClock():
    controlMatrix('clock')
