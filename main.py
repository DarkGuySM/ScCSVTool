import lzma
import binascii
import os
import shutil
import glob








def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")



def Remove_junk():
    if os.name=="nt":
        os.system("del temp.txt")
        os.system("del temp.csv")
    else:
        os.system("rm temp.txt")
        os.system("rm temp.csv")



def DecompressCSV(filename):
    with open(filename, 'rb') as f:
        hexdata = f.read().hex()
        
    fixedhexdata=hexdata[:16]+"00"*4+hexdata[16:]
        
    with open("temp.txt","w") as file:
        file.write(fixedhexdata)
        file.close()
    
    with open('temp.txt') as f, open('temp.csv', 'wb') as fout:
        for line in f:
            fout.write(
                binascii.unhexlify(''.join(line.split()))
            )
    
    with lzma.open("temp.csv") as f:
        file_content = f.read()
    
    with open (filename,"wb") as f:
        f.write(file_content)
    
    Remove_junk()
    
    
    

    
    
def CompressCSV(filename):
    pass
    
    












clear()
folders=["Temp","In_compressed_csv","Out_decompressed_csv","In_decompressed_csv","Out_compressed_csv"]



for i in folders:
    try:    
        os.mkdir(i)
        print(f"[INFO] Created folder \'{i}\'.")
    except:
        print(f"[INFO] Folder \'{i}\' exists.")











if os.name=="nt":
    temp_dir= os.getcwd()+"\\"+folders[0]+"\\"
    in_compressed_dir= os.getcwd()+"\\"+folders[1]+"\\"
    out_decompressed_dir= os.getcwd()+"\\"+folders[2]+"\\"
    in_decompressed_dir= os.getcwd()+"\\"+folders[3]+"\\"
    out_compressed_dir= os.getcwd()+"\\"+folders[4]+"\\"
else:
    temp_dir=os.getcwd()+"/"+folders[0]+"/"
    in_compressed_dir=os.getcwd()+"/"+folders[1]+"/"
    out_decompressed_dir=os.getcwd()+"/"+folders[2]+"/"
    in_decompressed_dir= os.getcwd()+"/"+folders[3]+"/"
    out_compressed_dir= os.getcwd()+"/"+folders[4]+"/"





    








print("[INFO] Enter 1 for decompressing and 2 for compressing.")
option=input("[CHOOSE] Enter option>  ")
try:
    option=int(option)
except:
    print("[ERROR] Please enter correct option.")









if option==1:
    temp_files = glob.glob(temp_dir+"*")
    for f in temp_files:
        os.remove(f)
    os.chdir(in_compressed_dir)
    files=os.listdir()
    for file in files:
        shutil.copy(in_compressed_dir+file,temp_dir+file)
    os.chdir(temp_dir)
    print(f"\n[INFO] Number of files is {len(files)}\n")
    print("[INFO] Cleared temp directory.")
    for file in files:
        DecompressCSV(file)
        print(f"[INFO] \'{file}\' successfully decompressed.")
    print("\n")
    for file in files:
        os.replace(temp_dir+file,out_decompressed_dir+file)
        print(f"[INFO] \'{file}\' moved to output directory..")

elif option==2:
    temp_files = glob.glob(temp_dir+"*")
    for f in temp_files:
        os.remove(f)
    os.chdir(in_decompressed_dir)
    files=os.listdir()
    for file in files:
        shutil.copy(in_decompressed_dir+file,temp_dir+file)
    os.chdir(temp_dir)
    print(f"\n[INFO] Number of files is {len(files)}.\n")
    print("[INFO] Cleared temp directory.")
    for file in files:
        CompressCSV(file)
        print(f"[INFO] \'{file}\' successfully compressed.")
    print("\n")
    for file in files:
        os.replace(temp_dir+file,out_compressed_dir+file)
        print(f"[INFO] \'{file}\' moved to output directory..")
    
