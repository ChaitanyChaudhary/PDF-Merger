from PyPDF2 import PdfWriter

merger = PdfWriter()

pdf_names = input("Enter PDF Names (separated by commas ','): ")

for pdf in pdf_names.split(","):
    merger.append(pdf.strip())

merger.write("merged-pdf.pdf")
merger.close()
