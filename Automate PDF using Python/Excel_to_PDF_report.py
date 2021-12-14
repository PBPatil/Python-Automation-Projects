# Cleaning environment
%reset -f

# Import Dependencies
import pandas as pd
import numpy as np
from fpdf import FPDF



# Reading input files
path = r'C:\Users\papr8016\Desktop\Football Clubs\England\Premier League'
Input_path = path+"\Arsenal.xlsx"
df = pd.read_excel(Input_path, sheet_name='Data')


# Creating variables
nickname = df['Nickname'].iloc[0]
history = df['History'].iloc[0]
coach = df['Current Manager'].iloc[0]
cabinet = df['Cabinet'].iloc[0]
ground = df['Stadium'].iloc[0]
motto = df['Club Motto'].iloc[0]
establishment = str(df['Founded in'].iloc[0])
gaffer = df['Current Manager'].iloc[0]

# PDF creation
pdf = FPDF() # Initializing object
pdf.add_page() # Adding new page

pdf.image(path + '/Football_field.svg.png',x=0,y=0,w=210,h=300) # Background wallpaper
pdf.image(path + '/premier-league_logo.jpg', x=188, y=0, w=18)  # Top Right corner logo 

# Title of Document
pdf.set_fill_color(200,0,0)
pdf.set_text_color(255,255,255)
pdf.set_font("Arial", size=30, style='B')
pdf.set_xy(10,32)
pdf.cell(0, 12.5, txt='ARSENAL FC', ln=1, align="C" , fill = True)

# Text box of header
pdf.set_fill_color(0,0,150)
pdf.set_text_color(255,255,255)
pdf.set_font("Arial", size=20, style='B')
pdf.set_xy(12,64)
pdf.cell(55, 10, txt='CLUB HISTORY', ln=1, align="L",fill=True)

# Text box of brief history
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size=10.9, style="B")
pdf.set_xy(12,76)
pdf.multi_cell(120, 5, txt= history, ln=1, align="L")

# Text box of header
pdf.set_fill_color(0,0,150)
pdf.set_text_color(255,255,255)
pdf.set_font("Arial", size=20, style='B')
pdf.set_xy(12,153)
pdf.cell(65, 10, txt='TROPHY CABINET', ln=1, align="L",fill=True)

# Text box of trophies won 
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size=10.9, style="B")
pdf.set_xy(12,165)
pdf.multi_cell(190, 5, txt= cabinet, ln=1, align="L")

# Club's Crest Image
pdf.image(path + '/arsenal_logo.jpg', x=124, y=58, w=80)

# Club's Latin Motto 
pdf.set_text_color(220,220,220)
pdf.set_font("Arial", size=14, style='B')
pdf.set_xy(130,130)
pdf.cell(130, 10, txt= motto, ln=1, align="L")

# Inserting Text
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size= 10.9)
pdf.set_xy(145,135)
pdf.cell(130, 10, txt= "Coach:", ln=1, align="L")

# Adding Manager's Name

pdf.set_text_color(0,0,150)
pdf.set_font("Arial", size=10.9, style='B')
pdf.set_xy(158,135)
pdf.cell(130, 10, txt= gaffer, ln=1, align="L")


# Inserting stadium Picture
pdf.image(path + '/Emirates.jpg', x=10, y=184,w=190)

# Stadium Name Text Box
pdf.set_fill_color(255,0,0)
pdf.set_text_color(255,255,250)
pdf.set_font("Arial", size= 15, style='B')
pdf.set_xy(150,260)
pdf.cell(47,8, txt= ground, ln=1, align="L" ,fill=True) 

# Exporting PDF
pdf.output(path +"/ArsenalFC.pdf") 
