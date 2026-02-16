#!/usr/bin/env python3
"""Convert markdown files to PDF using markdown and weasyprint"""

import markdown
from weasyprint import HTML, CSS
import os

CSS_STYLE = """
@page {
    size: letter;
    margin: 1in;
}

body {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
    max-width: 100%;
}

h1 {
    font-size: 24pt;
    color: #1a1a1a;
    border-bottom: 2px solid #333;
    padding-bottom: 10px;
    margin-top: 40px;
    page-break-before: always;
}

h1:first-of-type {
    page-break-before: avoid;
}

h2 {
    font-size: 18pt;
    color: #2a2a2a;
    margin-top: 30px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 5px;
}

h3 {
    font-size: 14pt;
    color: #3a3a3a;
    margin-top: 20px;
}

h4 {
    font-size: 12pt;
    font-style: italic;
    color: #4a4a4a;
}

code {
    font-family: 'Courier New', monospace;
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 10pt;
}

pre {
    background-color: #f4f4f4;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
    font-size: 10pt;
}

blockquote {
    border-left: 4px solid #666;
    margin-left: 0;
    padding-left: 20px;
    font-style: italic;
    color: #555;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px 12px;
    text-align: left;
}

th {
    background-color: #f0f0f0;
    font-weight: bold;
}

hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 30px 0;
}

a {
    color: #0066cc;
    text-decoration: none;
}

ul, ol {
    margin-left: 20px;
}

li {
    margin-bottom: 5px;
}

strong {
    color: #1a1a1a;
}

em {
    color: #444;
}
"""

def convert_md_to_pdf(md_path, pdf_path):
    """Convert a markdown file to PDF"""
    print(f"Converting {md_path} to {pdf_path}...")

    # Read markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc']
    )

    # Wrap in HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
    {html_content}
    </body>
    </html>
    """

    # Convert to PDF
    HTML(string=full_html).write_pdf(
        pdf_path,
        stylesheets=[CSS(string=CSS_STYLE)]
    )

    print(f"Successfully created {pdf_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    files_to_convert = [
        ('THE_ARCHITECTURE_OF_PUZZLEMENT.md', 'The_Architecture_of_Puzzlement.pdf'),
        ('TWENTY_ORIGINAL_PUZZLES.md', 'Twenty_Original_Puzzles.pdf'),
    ]

    for md_file, pdf_file in files_to_convert:
        md_path = os.path.join(base_dir, md_file)
        pdf_path = os.path.join(base_dir, pdf_file)

        if os.path.exists(md_path):
            convert_md_to_pdf(md_path, pdf_path)
        else:
            print(f"Warning: {md_path} not found")

if __name__ == '__main__':
    main()
