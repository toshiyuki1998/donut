def convert(ws):
    table_content = convert_to_html_table(ws)
    html_template = generate_html_template(table_content)
    return html_template

def convert_to_html_table(ws):
    table_content = ""
    for row_idx, row in enumerate(ws.iter_rows(), start=1):
        table_content += "<tr>"
        for col_idx, cell in enumerate(row, start=1):
            cell_value = cell.value if cell.value is not None else ""
            cell_value = newline_to_html_breaks(str(cell_value))
            css_class = f"cell-{row_idx}-{col_idx}"
            
            rowspan, colspan = get_col_row_span(ws, cell)
            table_content += f'<td class="{css_class}" rowspan="{rowspan}" colspan="{colspan}">{cell_value}</td>'
        table_content += "</tr>"
    return table_content

def newline_to_html_breaks(text):
    return text.replace('\n', '<br>').replace('\r\n', '<br>')

def get_col_row_span(ws, cell):
    rowspan = 1
    colspan = 1

    if cell.coordinate in ws.merged_cells:
        for merged_range in ws.merged_cells.ranges:
            if cell.coordinate in merged_range:
                rowspan = merged_range.max_row - merged_range.min_row + 1
                colspan = merged_range.max_col - merged_range.min_col + 1
                break

    return rowspan, colspan

def generate_html_template(table_content):
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body>
        <table class="excel-table">
            {table_content}
        </table>
    </body>
    </html>
    """
    return html_template