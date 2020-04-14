from fpdf import Template


class GeneratePDF:

    def __init__(self, elements):
       self.pdf = Template(format="A4", elements=elements)
       self.pdf.add_page()

    def addtext(self, field,text):
       self.pdf[field] = text

    def addimage(self, field, image_path):
       self.pdf[field] = image_path


    def generatePDF(self, filename):
       self.pdf.render(filename)
    


