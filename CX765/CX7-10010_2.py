import PyPDF2
print("What do you want to do?")

while True:
        Commands = input("(Your command?) => ")
        if Commands == "Encrypt" or Commands == "encrypt":
                user_wish = input("Please write the file's origin > ")

        else:
                print("Please state a proper response")

        def encrypt(user_wish):
        ############################ ENCRYPTION #############################
                try:
                        pdfFile = open(user_wish , "rb")
                        pdfReader = PyPDF2.PdfFileReader(pdfFile)
                        pdfWriter = PyPDF2.PdfFileWriter()
                        for pageNum in range(pdfReader.numPages):
                                pdfWriter.addPage(pdfReader.getPage(pageNum))
                                
                        pdfWriter.encrypt("swordfish")
                        resultPdf = open("encryptedminutes.pdf" , "wb")
                        pdfWriter.write(resultPdf)
                        resultPdf.close()
                except OSError as e:
                        print("\nWe found no file matching that description\n")

        ############################ ENCRYPTION #############################

        try:
                encrypt(user_wish)
        except NameError:
                pass
