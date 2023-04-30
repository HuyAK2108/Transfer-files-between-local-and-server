import argparse
import os

ROOT = 'huyv@den-l-006.amperecomputing.com:/work/huyv/'     # SERVER
DEFL =  os.getcwd()                                         # LOCAL

def parse_opt():
    parser = argparse.ArgumentParser(description= "Secure copy files from server to local, src is the path to file on SERVER, des is the path on LOCAL")
    parser.add_argument('-s', '--source', type= str, default= ROOT, help= 'path to source on SERVER')
    parser.add_argument('-d', '--destination', type= str, default= DEFL, help= 'path to destination on LOCAL')
    parser.add_argument('-r', '--recursive', action= 'store_true', help= 'folder')
    opt = parser.parse_args()
    return opt

def main(opt):
    src = opt.source
    des = opt.destination
    
    src = f"huyv@den-l-006.amperecomputing.com:{src}"
    print(f"🔥Copying from {src} to {des}🔥")
    
    if opt.recursive:
        cmd = f"cp -r {src} {des}"
        print(cmd)
        os.system(cmd)
        
    else:
        cmd = f"cp {src} {des}"
        print(cmd)
        os.system(cmd)
    
    print("\nDone!(👉ﾟヮﾟ)👉")
    
if __name__ == "__main__":
    opt = parse_opt()
    main(opt=opt)
    
    