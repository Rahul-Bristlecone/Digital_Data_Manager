import tabula

file = "C:\\Users\\Rahul.Sharma4\\OneDrive - Mahindra & Mahindra Ltd.-55241918-Bristlecone India Pvt Ltd\\ABS - SPS " \
       "Commerce\\SendPath\\DeliveryDocketReport8117C59967651.pdf"
output_file = "C:\\Users\\Rahul.Sharma4\\Downloads\\test2.csv"

pdf = tabula.read_pdf(file, pages = 1, lattice=True)[0]
pdf.to_csv(output_file)

print(pdf)

# tabula.convert_into(file, output_file, output_format="csv", pages='all')
