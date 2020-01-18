import subprocess as sub


def ssh_connect():
    user = "musa"
    host = "10.49.235.101"
    ssh_connect = sub.Popen(['sudo ssh %s@%s' %
                                    (user, host)],
                                    stdout=sub.PIPE,
                                    stdin=sub.PIPE, shell=True)
    ssh_connect.stdin.write('Musamustfa\n')


print(ssh_connect())