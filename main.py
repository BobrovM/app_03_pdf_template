from fpdf import FPDF
import pandas as pd


def add_lines(in_pdf, start=23, end=277, font=12):
    for index in range(start, end, font):
        in_pdf.line(10, index, 200, index)


df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():

    print(index)

    pdf.add_page()

    pdf.set_font(family="Times", style="BI", size=24)
    pdf.set_text_color(50, 50, 125)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, x2=200, y1=23, y2=23)

    add_lines(pdf)

    pdf.ln(255)
    pdf.set_font(family="Times", style="BU", size=10)
    pdf.set_text_color(100, 100, 200)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for jindex in range(row["Pages"]-1):
        pdf.add_page()

        add_lines(pdf)

        pdf.ln(267)
        pdf.set_font(family="Times", style="BU", size=10)
        pdf.set_text_color(100, 100, 200)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
