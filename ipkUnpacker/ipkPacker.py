import os, subprocess
print('Just Antonio IPK packer/unpacker')

unpakkeFolder = '__unpakke1.2(1008)'

# consoleVariations = ["pc", "wiiu", "wii", "nx", "x360", "durango", "scarlett", "ps3", "orbis", "prospero", "ggp"]
console = 'ps3' # change when packing

cmd = ''
folderUnpack = ''

case = input('Pick option: \n1. Pack \n2. Unpack \nYour choice: ')
print('\n')
if case == '1': # PACKING
        for folder in os.listdir():
            folderAbs = os.path.abspath(folder)
            if os.path.isdir(folderAbs): # check if listed files and folder are ONLY folders
                if folder == unpakkeFolder: # exludes Unpakke folder from packing
                    continue
                else: # building command line
                    cmd = '"' + os.path.join(os.path.abspath(unpakkeFolder), 'unpakke.exe') + '" "' # global path of unpakke.exe
                    cmd += os.path.abspath(unpakkeFolder) + r'\modules\ubiart.umod" ' # global path for module ubiart.umod
                    cmd += 'pack "' # option to pack
                    cmd += folderAbs + '" "' # global path of folder to pack
                    cmd += folderAbs + '_' + console + '.ipk" ' # global path of output file
                    subprocess.run(cmd)
                    cmd = ''
                    print(folder + '.ipk packed!\n')
            else:
                continue
elif case == '2': # UNPACKING
        for file in os.listdir():
            fileAbs = os.path.abspath(file)
            if file.endswith('.ipk'): # check if listed files are *.ipk
                cmd = '"' + os.path.join(os.path.abspath(unpakkeFolder), 'unpakke.exe') + '" "' # global path of unpakke.exe
                cmd += os.path.abspath(unpakkeFolder) + r'\modules\ubiart.umod" ' # global path for module ubiart.umod
                cmd += 'unpack "' # option to unpack
                cmd += fileAbs+ '" "' # global path of folder to unpack
                try:
                    folderUnpack = fileAbs.rsplit('_', 1)[0] # remove e.g. *_ps3* if present
                except:
                    folderUnpack = fileAbs # otherwise use full ipk name
                cmd += folderUnpack + '"'
                os.makedirs(folderUnpack, exist_ok=True) # making folder for unpacking
                try:
                    subprocess.run(cmd)
                except:
                    continue
                cmd = ''
                print(file + ' unpacked!\n')
            else:
                continue
else:
    print('Invalid input.')
