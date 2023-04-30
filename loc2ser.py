import argparse
import os

ROOT = os.getcwd()                                          # LOCAL
DEFL = 'huyv@den-l-006.amperecomputing.com:/work/huyv/'     # SERVER

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type= str, default= ROOT, help= 'path to source')
    parser.add_argument('-d', '--destination', type= str, default= DEFL, help= 'path to destination')
    parser.add_argument('-r', '--recursive', action= 'store_true', help= 'folder')
    opt = parser.parse_args()
    return opt

def main(opt):
    src = opt.source
    des = opt.destination
    des = f"huyv@den-l-006.amperecomputing.com:{des}"
    
    print(f"🔥Copying from {src} to {des}🔥")
    
    # if opt.recursive:
    #     cmd = f"cp -r {src} {des}"
    #     print(cmd)
    #     os.system(cmd)
        
    # else:
    #     cmd = f"cp {src} {des}"
    #     print(cmd)
    #     os.system(cmd)
    
    print("\nDone!（づ￣3￣）づ╭❤️～")
    
if __name__ == "__main__":
    opt = parse_opt()
    main(opt=opt)
    
    