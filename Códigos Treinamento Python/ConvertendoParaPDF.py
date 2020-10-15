import pdfkit

config = pdfkit.configuration(wkhtmltopdf ="C:/Python39/wkhtmltopdf/bin/wkhtmltopdf.exe")

pdfkit.from_url('http://google.com', 'out.pdf',configuration=config)

pdfkit.from_file('D:/Backup/Tarabalhos Facul/Aplicações da Internet/TrabalhoAV1/tabuada.html', 'out.pdf',configuration=config)

pdfkit.from_string('#GustavoNunes', 'out.pdf',configuration=config)
