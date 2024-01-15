#Goal: Simplify the SMB process.
#This script was designed after doing HTB-Dancing and struggling through the SMB process.

print("Welcome to ZSMB. ZuL SMB simplified")
print("Do you want to (1)Check Shares,\n (2)Connect to a share,\n (3)Move around files, \n(4) Get files, \n(5)Delete files?")
userInput = int(input("Which number?"))
if userInput == 1:
    print("smbclient TARGET_IP_HERE -L")
elif userInput == 2:
    print("smbclient \\\\TARGET_IP_HERE\\SHARE_HERE  .If user and password, use -U and --password password_here to input them.")
elif userInput == 3:
    print("dir lists the directory. ls lists files. cd moves directory. pwd states current location.")
elif userInput == 4:
    print("get file_name.file_type . You can also name a dir path like /folder/file.file_type")