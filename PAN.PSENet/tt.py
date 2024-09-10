import os
import subprocess
subprocess.run(['python', 'test.py', 'config/pan/pan_r18_ic15.py', 'checkpoints/pan_r18_ic15/checkpoint.pth.tar'])
# os.chdir('eval\ic15')
# args = ['-g=gt.zip', '-s=../../outputs/submit_ic15.zip']
# subprocess.run(['python', 'script.py'] + args)
# os.chdir('../..')