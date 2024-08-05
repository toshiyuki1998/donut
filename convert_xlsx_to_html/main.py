import openpyxl
from . import generate_css_styles
from . import excel_to_html

# ファイルパスを定義
excel_file_path = "/opt/machine_learning/donut/data/templates/invoice/inv_01b.xlsx"
html_output_path = "./output.html"
css_output_path = "./styles.css"

def generate_html_and_css_files(excel_path, css_path, html_path, sheet_name):
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    ws = wb[sheet_name]
    
    generate_html_file(ws, html_path)

    generate_css_file(ws, css_path)

    print("完了しました。")

def generate_html_file(ws, html_path):
    html_content = excel_to_html.convert(ws)
    with open(html_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print("HTMLファイルを作成しました。")

def generate_css_file(ws, css_path):
    css_styles = generate_css_styles.generate(ws)
    with open(css_path, "w", encoding="utf-8") as css_file:
        css_file.write(css_styles)

    print("CSSファイルを作成しました。")

if __name__ == "__main__":
    generate_html_and_css_files(excel_file_path, css_output_path, html_output_path)