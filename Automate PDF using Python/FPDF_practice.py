#Clearing Environment
%reset -f 

#Importing dependencies
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        #logo
        self.image(r'C:/Users/papr8016/Desktop/Automate PDF using Python/arsenal-logo-vector.png',x=200,y=0,w=15) #If height is not provided, python will proportionately will assign it.
        #font
        self.set_font("helvetica","B",20)
        #Padding
        self.cell(80)
        #title
        self.cell(30,10,'TITLE',border=True, ln=1,align="C")
        #line break
        self.ln(20)
        
    def footer(self):
        #set the position of footer
        self.set_y(-15) #if we give +ve 15, it will start from top
        #set font
        self.set_font("courier","I",10)
        #Page number
        self.cell(0,10,f"Page {self.page_no()}/{{nb}}",align="C")
        
   
      
        
        
#Create FPDF object
'''It takes followinng parameters:
    Layout - Potrait("P") , Landscape ("L")
    Unit - milimeters ("mm"), centimeter("cm") , inches("in")
    Format - "A3" ,"A4"(Default),"A5","Letter","Legal", (WIDTH=100,HEIGHT=150)''' #CustomSize
    
pdf = PDF("P","mm","Legal")

#To get total page numbers
pdf.alias_nb_pages()  

#Add a page
pdf.add_page()

#Specify font
''' available fonts - 'times','courier',"helvetica","Arial"
    next argument it can take - Bold ("B") ,Underline ("U"), Italics ("I") ,regular(""),combination ex.("BU") '''

pdf.set_font("courier","B",16)
pdf.set_text_color(0,174,239) #red,green,blue components - each takes between 0 to 255 
#Add text
""" Important arguments 
    w = width if specified 0 then it will cover whole page,
    h = height ,
    txt = text message that you wish to display
    ln = 0/False , 1/True - move cursor down to the next line
    border = 0/False , 1/True -  Draw border around cell"""

pdf.cell(120,100,"Hi there!" , ln=True , border=True)

#Adding other text on same line
pdf.cell(80,10,"This is Prasad.")

#New_Page
#Add page break
pdf.set_auto_page_break(auto=True , margin = 25) #Margin is how far from bottom page break is added, here 25mm
pdf.add_page()
pdf.set_font("times","",15)

#Creating multiple lines
for i in range(1,51):#Loop will iterate over 30
    pdf.cell(0,10,f"Line number {i}",ln=True) #width 0 means it will occupy entire page area
    

#Adding new page to explain how to create header and footer
""" To use Header and Footer methods of FPDF, we need to apply concept of Object
    Oriented Programming (OOP)"""


#Export PDF file
pdf.output("pdf_1.pdf") #Open the file in web browser by right clicking it and selecting any web browser installed.
