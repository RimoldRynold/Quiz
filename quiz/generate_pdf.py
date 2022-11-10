from fpdf import FPDF


def save_pdf(name, question, answer):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt=f"Question : {question}", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Answer : {answer}", ln=2, align="C")
    pdf.output(name)
