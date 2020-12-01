"""
MAIN INGRESS POINT FOR FORKING BUFFER PROCS 
THIS SCRIPT WILL BE USED AS INGRESS IN ```EYEBUFFER``` COMPOSE SERVICE  
"""
import time
import subprocess
import requests
import sys
import json




def execute(command):
    subprocess.check_call(command, stdout=sys.stdout, stderr=subprocess.STDOUT)

"""
Static endpoints
# https://stream-uc2-delta.dropcam.com/nexus_aac/7174a4f808414039ba1a96180019226a/chunklist_w1838844450.m3u8?public=wzqonrwiHO (RING CAM)
# http://192.168.1.71:49152/video.mjpg?q=100&fps=100&id=0.7587060853631462&r=1599663296819 (LAPTOP CAM)

proc2 = subprocess.Popen(['python', 'detect_mask_video.py',
    "-s", "http://192.168.1.71:49152/video.mjpg?q=100&fps=100&id=0.7587060853631462&r=1599663296819",
    "-n", "1"], shell=False)
proc = subprocess.Popen(['python', 'detect_mask_video.py',
    "-s", "https://stream-uc2-delta.dropcam.com/nexus_aac/7174a4f808414039ba1a96180019226a/chunklist_w1838844450.m3u8?public=wzqonrwiHO",
    "-n", "2"], shell=False)
"""

processes = {}

# A better approach might be to have this service exposed using Flask w/ an endpoint set up to spawn processes. 
# This would save our API Server a lot of request overhead w/ the cost of having a larger container footprint. 
while True:
    try:
        response = requests.get('http://flask:5000/api/nodesettings')
    except:
        print('ERROR REACHING ``FLASK`` SVC.')
        continue
    
    endpoints = json.loads(response.content)
    for node in endpoints:
        INGEST_URL = node['ingest_url']
        NODE_ID = str(node['nodeID'])

        if NODE_ID not in processes or processes[NODE_ID].poll() is not None:
            print('[[FORKING BUFFER FOR NODE ' + NODE_ID + ']]')
            sproc = subprocess.Popen(['python', 'detect_mask_video.py',
                "-s", INGEST_URL,
                "-n", NODE_ID], shell=False)
            processes[NODE_ID] = sproc
    time.sleep(5)

