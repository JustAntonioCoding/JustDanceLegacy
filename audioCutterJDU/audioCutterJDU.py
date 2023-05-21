import os, json, subprocess
print('JDU AUDIO CUTTER BY JUST ANTONIO')
print('--------------------------------')

# Removes NUL at the end of musictrack
def loadjson(path):
    try:
        return json.load(open(path, encoding='utf-8'))
    except:
        return json.loads(open(path, encoding='utf-8').read()[:-1])

# Making input folder
try:
    os.mkdir('input')
    input('Insert your *codename*_musictrack.tpl.ckd and *codename*.ogg files in input and then run again.')
    exit()
except:
    pass

# Making output folder
os.makedirs('output', exist_ok=True)

for files in os.listdir('input'):
    if files.endswith('.ogg'): # Loading all *.ogg files
        songName = files.replace('.ogg', '')
        print('Loaded '+songName+'.ogg')
        # Loading musictracks
        # Checks for NULL value at the end of musictrack and overwrites original file without it
        path = 'input/' + songName + '_musictrack.tpl.ckd'
        musictrack=loadjson(path)
        # Calculating timestamp cut
        startBeat=abs(musictrack['COMPONENTS'][0]['trackData']['structure']['startBeat'])
        marker=musictrack['COMPONENTS'][0]['trackData']['structure']['markers'][startBeat]
        timeStamp=marker/48
        # Making song audio
        subprocess.run('ffmpeg -y -ss "'+str(timeStamp)+'ms" -nostats -loglevel 8 -i input/'+songName+'.ogg output/'+songName+'.ogg')
        # Making amb audio (assumed that it's amb intro)
        subprocess.run('ffmpeg -y -ss 0 -t "'+str(timeStamp)+'ms" -nostats -loglevel 8 -i input/'+songName+'.ogg output/amb_'+songName+'_intro.ogg')
        print('Done '+songName+'.ogg\n')
