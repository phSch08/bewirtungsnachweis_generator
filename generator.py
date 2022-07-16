from fpdf import FPDF
import os

def generate_pdf(catering_date, catering_location_1, catering_location_2, catering_location_3, catering_reason, catering_kostenstelle, catering_expense, catering_type, catering_hosts, catering_guests):
    class PDF(FPDF):

        # Page footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # default italic 8
            self.set_font('default', 'I', 8)
            # Page number
            self.cell(0, 10, 'Seite ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')



    # Instantiation of inherited class
    pdf = PDF('P', 'mm', 'A4')
    pdf.FPDF_FONT_DIR = os.path.join(os.path.dirname(__file__),'fonts')
    pdf.add_font("default", style='', fname=os.path.join(os.path.dirname(__file__),'fonts', 'FreeSans.ttf'))
    pdf.add_font("default", style='B', fname=os.path.join(os.path.dirname(__file__),'fonts', 'FreeSansBold.ttf'))
    pdf.add_font("default", style='I', fname=os.path.join(os.path.dirname(__file__),'fonts', 'FreeSansOblique.ttf'))
    pdf.alias_nb_pages()
    pdf.set_margins(left=15, top=15)
    pdf.add_page()

    # Make header
    pdf.set_font('default', 'B', 18)
    pdf.cell(180, 10, "Bewirtungsnachweis", "LTR", 1, "C")
    pdf.set_font('default', 'B', 12)
    pdf.cell(180, 8, "Hasso-Plattner-Institut für Digital Engineering gGmbH", "LR", 1, "C")
    pdf.cell(180, 8, "Prof.-Dr.-Helmert-Str. 2-3, 14482 Potsdam", "LRB", 1, "C")
    pdf.cell(180, 8, "", 0, 1, "C")

    pdf.set_font('default', '', 10)
    pdf.cell(180, 5, "Angaben zum Nachweis der Höhe und der betrieblichen Veranlassung", 0, 1, "C")
    pdf.cell(180, 5, "von Bewirtungsaufwendungen ( § 4 Abs. 5 Ziff. 2 EStG )", 0, 1, "C")
    pdf.cell(180, 8, "", 0, 1, "C")

    pdf.set_font('default', 'B', 10)
    pdf.cell(70, 5, "Tag der Bewirtung", "LTRB", 0, "L")
    pdf.cell(110, 5, "Ort der Bewirtung (genaue Bezeichnung, Anschrift)", "TRB", 1, "L")
    pdf.set_font('default', '', 10)
    pdf.cell(70, 5, catering_date, "LR", 0, "L")
    pdf.cell(110, 5, catering_location_1, "R", 1, "L")
    pdf.cell(70, 5, "", "LR", 0, "L")
    pdf.cell(110, 5, catering_location_2, "R", 1, "L")
    pdf.cell(70, 5, "", "LRB", 0, "L")
    pdf.cell(110, 5, catering_location_3, "BR", 1, "L")
    pdf.cell(180, 8, "", 0, 1, "C")

    # Bewirtende Personen
    pdf.set_font('default', 'B', 10)
    pdf.cell(70, 5, "Bewirtende Personen", "LTB", 0, "L")
    pdf.cell(110, 5, "", "TRB", 1, "L")

    pdf.set_fill_color(200)
    pdf.set_font('default', '', 10)
    for idx,el in enumerate(catering_hosts):
        pdf.cell(70, 5, el, "L", 0, "L", idx % 2)
        pdf.cell(110, 5, "Studierend am HPI, Prof.-Dr.-Helmert-Str. 2-3, 14482 Potsdam", "R", 1, "L", idx % 2)
    pdf.cell(180, 8, "", "T", 1, "C")

    # Bewirtete Personen
    pdf.set_font('default', 'B', 10)
    pdf.cell(70, 5, "Bewirtete Personen", "LTB", 0, "L")
    pdf.cell(110, 5, "", "TRB", 1, "L")

    pdf.set_fill_color(200)
    pdf.set_font('default', '', 10)
    for idx,el in enumerate(catering_guests):
        pdf.cell(70, 5, el, "L", 0, "L", idx % 2)
        pdf.cell(110, 5, "Studierend am HPI, Prof.-Dr.-Helmert-Str. 2-3, 14482 Potsdam", "R", 1, "L", idx % 2)
    pdf.cell(180, 8, "", "T", 1, "C")

    # Anlass
    pdf.set_font('default', 'B', 10)
    pdf.cell(180, 5, "Anlass der Bewirtung", "LTBR", 1, "L")
    pdf.set_font('default', '', 10)
    pdf.multi_cell(180, 5, catering_reason, "LBR", "L", ln=1)

    pdf.cell(180, 5, "", "", 1, "L")
    pdf.cell(180, 5, "Kostenstelle: " + catering_kostenstelle, "", 1, "L")
    pdf.cell(180, 5, "", "", 1, "L")
    pdf.set_font('default', 'B', 10)
    pdf.cell(180, 5, "Höhe der Aufwendungen: " + str(catering_expense) + "€", "", 1, "L")
    pdf.cell(180, 5, "", "", 1, "L")
    pdf.set_font('default', '', 10)
    pdf.cell(50, 5, "Bei Bewirtung der Gäste: ", "", 0, "L")
    if (catering_type == 0):
        pdf.cell(5, 5, "X", "LBTR", 0, "C")
    else:
        pdf.cell(5, 5, "", "LBTR", 0, "C")
    pdf.cell(55, 5, "", "", 0, "L")
    pdf.cell(50, 5, "In anderen Fällen: ", "", 0, "L")
    if (catering_type == 1):
        pdf.cell(5, 5, "X", "LBTR", 1, "C")
    else:
        pdf.cell(5, 5, "", "LBTR", 1, "C")
    pdf.cell(180, 5, "", "", 1, "L")
    pdf.set_font('default', 'B', 10)
    pdf.cell(180, 5, "Laut umseitiger / beigefügter Rechnung: " + str(catering_expense) + "€", "", 1, "L")
    pdf.cell(180, 30, "", "", 1, "L")

    pdf.set_font('default', '', 10)
    pdf.cell(70,5, "Ort, Datum", "T", 0, "C")
    pdf.cell(40,5, "", "", 0, "C")
    pdf.cell(70,5, "Unterschrift", "T", 0, "C")

    return pdf.output()
