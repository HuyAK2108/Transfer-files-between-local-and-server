import argparse
import os

ROOT = os.getcwd()                                          # LOCAL
DEFL = 'huyv@den-l-006.amperecomputing.com:/work/huyv/'     # SERVER

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", default= ROOT, help="Source location")
    parser.add_argument("dst", default= DEFL, help="Destination location")
    parser.add_argument('-r', '--recursive', action= 'store_true', help= 'folder')
    opt = parser.parse_args()
    return opt

def main(opt):
    src = opt.src
    dst = opt.dst
    dst = f"huyv@den-l-006.amperecomputing.com:{dst}"
    
    print(f"🔥Copying from {src} to {dst}🔥")
    
    if opt.recursive:
        cmd = f"scp -r {src} {dst}"
    else:
        cmd = f"scp {src} {dst}"
    
    print(cmd)
    os.system(cmd)
    print("\nDone!")
    
if __name__ == "__main__":
    opt = parse_opt()
    main(opt=opt)
    
    