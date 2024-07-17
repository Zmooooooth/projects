from fpdf import FPDF

def main():
    userin = input("Name: ").strip()
    create_pdf(userin)

def create_pdf(input):
    string = input + " took CS50"
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 64)
    pdf.cell(185, 50, "CS50 Shirtificate", border=0, align="C")
    pdf.image("shirtificate.png", 10,80,190)

    pdf.set_font("helvetica", "",32)
    pdf.text(75, 150, string)

    pdf.output("shirtificate.pdf")




if __name__ == "__main__":
    main()
