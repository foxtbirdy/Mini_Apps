import PyPDF2

print("What do you want to do?")

def helpline():
	print("Commands You can do\n")
	print("1. Encrypt")
	print("2. Check Security")
	print("3. Usage")
	print("4. Credits")
	print("5. Help")
	print("6. Quit\n")

def usage():
	print("""
The program is created to encrypt PDF files.
This program requires the PDF's folder path and its name
The program also requires a password if both conditions have met,
Please note that the program cannot reverse the Encryption on the PDF so please be careful.
PROJECT IS STILL IN-BUILD
If you find a bug, Please create a issue on the Repository.
""")


def credits():
	print("""
A program done by,
CLIMAX_ aka Code_Blender_7
Twitter = @Black_2_white
Project made for Open Source Development
""")

def check_security():
        try:
                Folder2 = input("Please write the file's origin => ")
                target_file2 = input("(File name?) =>")
                file2 = Folder2 + ("\\") + target_file2 + ".pdf"
                pdfFile2 = open(file2, "rb")
                pdfReader2 = PyPDF2.PdfFileReader(pdfFile2)
                if pdfReader2.isEncrypted == True:
                        print("This file is locked")
                elif pdfReader2.isEncrypted == False:
                        print("This file is unlocked")
                else:
                        print("Error Input")
        except FileNotFoundError as e:
                print("We found no file matching that description")
                
active = True
while active:

                user = input("(Your command?) => ")
                Commands = user.lower()
                if Commands == "encrypt":
                        Folder = input("Please write the file's origin => ")
                        target_file = input("(File name?) =>")
                        file = Folder + ("\\") + target_file + ".pdf"
                                
                        print("RUNNING...\n\n")
                elif Commands == "help":
                        helpline()

                elif Commands == "quit":
                        print("Program Quit\nThank you for testing")
                        active = False
                elif Commands == "usage":
                        usage()   
                elif Commands == "credits":
                        credits()
                elif Commands == "check security":     
                        check_security()
                else:
                        print("Please add a Valid input. Type 'Help' for more Info")                                                                                                
                def encrypt():
############################ ENCRYPTION #############################
                        try:
                                pdfFile = open(file, "rb")
                                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                                pdfWriter = PyPDF2.PdfFileWriter()
                                for pageNum in range(pdfReader.numPages):
                                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                                password = input("Encryption Password => ")
                                pdfWriter.encrypt(password)
                                resultPdf = open(Folder + ("\\") + target_file + "[ENCRYPTED]" + ".pdf" , "wb")
                                pdfWriter.write(resultPdf)
                                resultPdf.close()
                                print("Encrypted")
                        except FileNotFoundError as e:
                                print("\nWe found no file matching that description\n")
                                print()
                                if pdfReader.isEncrypted == True:
                                        print("This file already has an encryption key on it")

########################### ENCRYPTION ##############################

                try:
                        encrypt()
                except NameError:
                        pass
