import PyPDF2
print("What do you want to do?")



Commands = input("=> ")
if Commands == "Encrypt":
	user_wish = input("Please write the file's origin > ")
else:
	print("Please state a proper response")

def encrypt(user_wish):
############################ ENCRYPTION #############################
	pdfFile = open(user_wish , "rb")
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	pdfWriter = PyPDF2.PdfFileWriter()
	for pageNum in range(pdfReader.numPages):
		pdfWriter.addPage(pdfReader.getPage(pageNum))

	pdfWriter.encrypt("swordfish")
	resultPdf = open("encryptedminutes.pdf" , "wb")
	pdfWriter.write(resultPdf)
	resultPdf.close()
############################ ENCRYPTION #############################


encrypt(user_wish)
