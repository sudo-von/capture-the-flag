import string
import subprocess
import os

os.chdir('/home/mario/Documents/ctf/hackdef2018/quals/4cr')
chars = '.-_}'+string.ascii_letters+string.digits#string.printable
f = open('secret').read()

flag = 'hackdef{'

for i in range(30):
    for c in chars:
        #r = subprocess.run(['wine C2C_module.exe', flag+c], stdout=subprocess.PIPE).stdout.decode('utf-8')
        p = subprocess.Popen(['wine C2C_module.exe '+flag+c],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        r, err = p.communicate()
        p.terminate()
        if r.decode('utf-8') in f:
            flag = flag+c
            print(flag)
            if '}' in flag:
                quit()
print(flag)
#hackdef{RC4_is_c0mm0nly_used_by_m4lwar3}
"""compare exe output with secret
noticed hackdef{ was the same as secret
bruteforced by comparing secret with exe output"""