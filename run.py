# method 1
import os
import time

i_loop=1

if os.path.exists('infoC.csv'):
    os.remove('infoC.csv')
if os.path.exists('infoNC.csv'):
    os.remove('infoNC.csv')
if os.path.exists('infoR.csv'):
    os.remove('infoR.csv')
    
start = time.time()
while(i_loop <= 200):
    os.system('python virtual_ellipses_psycopy_adjusted_scale.py' + ' ' + str(i_loop))
    i_loop += 1
end = time.time()

print('time', str(end-start))
# import virtual_ellipses_underPython
# virtual_ellipses_underPython.main()
