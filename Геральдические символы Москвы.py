import pandas as pd
import pdfkit
data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/data-102743-2019-11-13.utf.csv", delimiter=";")
html = '''<html>
<head>
    <title>Геральдические символы Москвы</title>
    <meta charset="utf-8"/>
</head>
<body>'''
for i, item in data.iterrows():
    if i == 0:
        html += '<h1>' + item['Name'] + '</h1>'
    else:
        html += '<h1 style="page-break-before:always">' + \
            item['Name'] + '</h1>'
    html += '''<p>
        <img style="width:80%;margin-left:10%"
        src="https://op.mos.ru/MEDIA/showFile?id=''' + item['Picture'] + '''">
    </p>'''
    html += '<p style="font-size:150%">' + item['Description'] + '</p>'
html += '</body></html>'

config = pdfkit.configuration(
    wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
options = {
    'page-size': 'A4',
    'header-right': '[page]'
}
pdfkit.from_string(html, 'heraldic.pdf',
                   configuration=config, options=options)
