import pandas as pd
import glob as gl
from fpdf import FPDF
from pathlib import Path


filepaths = gl.glob("invoices/*xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=58, h=8, txt=f"Invoice No.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=58, h=8, txt=f"Date No.{date}")


    pdf.output(F"pdfs/{filename}.pdf")




