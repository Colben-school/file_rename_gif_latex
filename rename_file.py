# Magic command to convert gif to png

# ./magick convert -coalesce Action-SingleActionClient.gif action/anim_%d.png

##################### IMPORT #####################
import os
import glob 
import sys
import argparse

##################### GLobal variable #####################
  


def rename_file(name_file, PATH):
    PATH = str(PATH)
    name_file = str(name_file)
    cpt = 1


    folder = glob.glob(PATH+'/*')
    if folder == []:
        raise Exception('Error: Path not found')
    
    try:
        folder = sorted(folder, key=lambda name: int(os.path.splitext(os.path.basename(name))[0].split('_')[-1]))
    except:
        raise Exception('Error: Files not sorted because of name')
    
    for name in folder:
        os.rename(name, PATH+'/'+name_file+'_'+str(cpt)+'.png')
        cpt = cpt + 1
        
def parse_args():    
    parser = argparse.ArgumentParser(description='Rename a list of files with the same name and a number')
    parser.add_argument('--name_file', type=str, default='image_',
                        help='Name of file')
    parser.add_argument('--PATH', type=str, required=True, default='/home/benoitco/Documents/GIF file overleaf/test_script',
                        help='Path to folder')
    args = parser.parse_args()
    return args
        

def main():
    arg = parse_args()
    rename_file(arg.name_file, arg.PATH)


if __name__ == '__main__':
    main()