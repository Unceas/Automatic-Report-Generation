import pandas as pd
from fpdf import FPDF

# ---------------------------
# 1. Load Data from CSV
# ---------------------------
file_path = r"C:\Users\kayus\OneDrive\Desktop\Automatic-Report\sample_data.csv"  #  Update if needed
df = pd.read_csv(file_path)

# ---------------------------
# 2. Basic Data Analysis
# ---------------------------
num_rows = len(df)
num_columns = len(df.columns)
column_names = df.columns.tolist()
summary_stats = df.describe().round(2)

# ---------------------------
# 3. PDF Report Class
# ---------------------------
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Automated Report - CodTech Internship", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_title(self, title):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def add_text(self, text):
        self.set_font("Arial", '', 11)
        self.multi_cell(0, 8, text)
        self.ln()

    def add_table(self, dataframe):
        self.set_font("Arial", 'B', 10)
        page_width = self.w - 2 * self.l_margin
        col_width = page_width / len(dataframe.columns)

        for col in dataframe.columns:
            self.cell(col_width, 10, str(col), border=1, align='C')
        self.ln()

        self.set_font("Arial", '', 10)
        for row in dataframe.itertuples(index=False):
            for val in row:
                self.cell(col_width, 10, str(val), border=1, align='C')
            self.ln()

# ---------------------------
# 4. Generate PDF
# ---------------------------
pdf = PDFReport()
pdf.add_page()

pdf.add_title(" Dataset Summary")
pdf.add_text(f"Total Rows: {num_rows}")
pdf.add_text(f"Total Columns: {num_columns}")
pdf.add_text(f"Column Names: {', '.join(column_names)}")

pdf.add_title(" Statistical Summary")
pdf.add_table(summary_stats)

# ---------------------------
# 5. Save PDF
# ---------------------------
output_path = r"C:\Users\kayus\OneDrive\Desktop\Automatic-Report\sample_report.pdf"
pdf.output(output_path)
print(f" PDF Report generated at: {output_path}")
