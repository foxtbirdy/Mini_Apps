import PyPDF2

print("What do you want to do?")

def helpline():
        print("Commands You can do")
        print("1. Encrypt")
        print("2. Help")
        print("3. Usage")
        print("4. Credits")
        print("5. Quit")

def usage():
        print("""
The program is created to encrypt PDF files.
This program requires the PDF's folder path and its name
The program also requires a password if both conditions have met
Please note that the program cannot reverse the Encryption on the PDF so please be careful.
""")
        
def credits():
        print("""
A program done by,
CLIMAX_ aka Code_Blender_7
Twitter = @Black_2_white
Project made for Open Source Development
""")
active = True
while active:
        Commands = input("(Your command?) => ")
        if Commands == "Encrypt" or Commands == "encrypt":
                Folder = input("Please write the file's origin => ")
                target_file = input("(File name?) =>")
                file = Folder + ("\\") + target_file + ".pdf"

        elif Commands == "help" or Commands == "Help":
                helpline()
        elif Commands == "quit" or Commands == "Quit":
                print("Program Quit\nThank you for testing")
                active = False
        elif Commands == "Usage" or Commands == "usage":
                usage()   
        elif Commands == "Credits" or Commands == "credits":
                credits()
        else:
                print("Please state a proper response")

        def encrypt():
# ############################ ENCRYPTION #############################
                try:
                        pdfFile = open(file, "rb")
                        pdfReader = PyPDF2.PdfFileReader(pdfFile)
                        pdfWriter = PyPDF2.PdfFileWriter()
                        for pageNum in range(pdfReader.numPages):
                                pdfWriter.addPage(pdfReader.getPage(pageNum))
                                
                        pdfWriter.encrypt("swordfish")
                        resultPdf = open("encryptedminutes.pdf" , "wb")
                        pdfWriter.write(resultPdf)
                        resultPdf.close()
                        print("Encrypted")
                except FileNotFoundError as e:
                        print("\nWe found no file matching that description\n")


############################# ENCRYPTION #############################

        try:
                encrypt()
        except NameError:
                pass
