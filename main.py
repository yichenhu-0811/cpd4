import shutil
import os
from csv_to_meets_html import csv_to_html  # Import the correct function

def process_meets():
    meets_list = ""
    meets_dir = 'meets'
    output_folder = 'meets_pages'

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(meets_dir):
        if filename.endswith('.csv'):
            csv_path = os.path.join(meets_dir, filename)
            print(f"Processing {csv_path}...")

            # Call the function from csv_to_meets_html.py
            csv_to_html(csv_path, output_folder)

            meet_name = os.path.splitext(filename)[0]
            meet_page = os.path.join(output_folder, meet_name + ".html")
            meets_list += f'''
            <tr><td><a href="{meet_page}">{meet_name}</a></td></tr>
            '''

    html_content = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/reset.css">
        <link rel="stylesheet" href="style.css">
        <title>Cross Country Meet Tracker</title>
    </head>
    <body>
    <!-- Section for list of teams -->
    <section id="cross-country-meets">
        <h1>Latest Cross Country Meets</h1>
        <table id="meets-list">
            <thead>
                <tr>
                    <th>Meet Name</th>
                </tr>v
            </thead>
            <tbody>{meets_list}
            </tbody>
        </table>
    </section>
    </body>
    </html>
    '''

    with open("index.html", 'w', encoding='utf-8') as f:
        f.write(html_content)
        print("HTML file 'index.html' has been generated successfully.")

if __name__=="__main__":
    process_meets()
