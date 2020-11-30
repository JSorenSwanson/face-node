"""
MAIN INGRESS POINT FOR FORKING BUFFER PROCS 
THIS SCRIPT WILL BE USED AS INGRESS IN ```EYEBUFFER``` COMPOSE SERVICE  
"""
import subprocess
import sys

def execute(command):
    subprocess.check_call(command, stdout=sys.stdout, stderr=subprocess.STDOUT)

# Retrieve list of endpoints we should spawn which are marked as active (?)
"""
Static endpoints
# https://stream-uc2-delta.dropcam.com/nexus_aac/7174a4f808414039ba1a96180019226a/chunklist_w1838844450.m3u8?public=wzqonrwiHO (RING CAM)
# http://192.168.1.71:49152/video.mjpg?q=100&fps=100&id=0.7587060853631462&r=1599663296819 (LAPTOP CAM)
"""
print("=== INGRESS ===")
proc = subprocess.Popen(['python', 'detect_mask_video.py',
    "-s", "https://stream-uc2-delta.dropcam.com/nexus_aac/7174a4f808414039ba1a96180019226a/chunklist_w1838844450.m3u8?public=wzqonrwiHO",
    "-n", "2"], shell=False)
proc2 = subprocess.Popen(['python', 'detect_mask_video.py',
    "-s", "http://192.168.1.71:49152/video.mjpg?q=100&fps=100&id=0.7587060853631462&r=1599663296819",
    "-n", "1"], shell=False)

proc.wait()