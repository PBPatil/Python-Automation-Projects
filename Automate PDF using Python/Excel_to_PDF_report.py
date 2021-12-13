%reset -f

#Import Dependencies
import pandas as pd
import numpy as np
from fpdf import FPDF



# Reading input files
path = r'C:\Users\Desktop\Football Clubs\England\Premier League'
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
pdf = FPDF()
pdf.add_page()

pdf.image(path + '/Football_field.svg.png',x=0,y=0,w=210,h=300)
# pdf.image(path + '/footer.png', x=8, y=0,w=195,h=30)
pdf.image(path + '/premier-league_logo.jpg', x=188, y=0, w=18)

pdf.set_fill_color(255,255,255)
pdf.set_text_color(0,0,0)
pdf.set_font("Arial","B", size=20)
pdf.set_xy(10,22)
pdf.cell(58, 16, txt= nickname.upper(), ln=1, align="L")

pdf.set_fill_color(200,0,0)
pdf.set_text_color(255,255,255)
pdf.set_font("Arial", size=30, style='B')
pdf.set_xy(10,35)
pdf.cell(0, 10, txt='ARSENAL FC', ln=1, align="L" , fill = True)

pdf.set_fill_color(255,255,255)
pdf.set_text_color(0,0,150)
pdf.set_font("Arial", size=9.5, style='BI')
pdf.set_xy(136,45)
pdf.cell(50, 10, txt= "Currently Managed by", ln=0, align="L")

pdf.set_fill_color(255,255,255)
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size=11, style='BI')
pdf.set_xy(175,45)
pdf.cell(50, 10, txt= gaffer, ln=0, align="L")

pdf.set_fill_color(255,255,255)
pdf.set_text_color(0,0,150)
pdf.set_font("Arial", size=20, style='B')
pdf.set_xy(10,64)
pdf.cell(200, 10, txt='CLUB HISTORY', ln=1, align="L")

pdf.set_fill_color(255,255,255)
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size=10.9, style="B")
pdf.set_xy(10,75)
pdf.multi_cell(120, 5, txt= history, ln=1, align="L")

pdf.set_fill_color(255,255,255)
pdf.set_text_color(0,0,150)
pdf.set_font("Arial", size=20, style='B')
pdf.set_xy(10,153)
pdf.cell(200, 10, txt='TROPHY CABINET', ln=1, align="L")

pdf.set_fill_color(255,255,255)
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size=10.9, style="B")
pdf.set_xy(10,164)
pdf.multi_cell(190, 5, txt= cabinet, ln=1, align="L")

pdf.image(path + '/arsenal_logo.jpg', x=124, y=58, w=80)

pdf.set_fill_color(255,255,255)
pdf.set_text_color(255,230,230)
pdf.set_font("Arial", size=12, style='B')
pdf.set_xy(137,130)
pdf.cell(130, 10, txt= motto, ln=1, align="L")

pdf.image(path + '/Emirates.jpg', x=10, y=184,w=190)

pdf.set_fill_color(255,255,255)
pdf.set_text_color(0,0,250)
pdf.set_font("Arial", size= 11, style='B')
pdf.set_xy(150,260)
pdf.cell(2, 2, txt= ground, ln=1, align="L")

# pdf.image(path + '/header.jpg', x=8, y=260,w=195,h=30)


pdf.output(path +"/ArsenalFC.pdf")
