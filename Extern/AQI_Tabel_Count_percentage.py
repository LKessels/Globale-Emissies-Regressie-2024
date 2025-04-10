from IPython.display import display, HTML

# Read the content of the HTML file and display it
with open('AQI_Tabel_Count_percent.html', 'r') as file:
    html_content = file.read()

display(HTML(html_content))