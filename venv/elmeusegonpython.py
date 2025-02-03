from flask import flask, render_template_string
app=flask(__name__)
@app.route('/')
def home():
    html_content= """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset ="UTF-8">
    <title> Hola titol</title>
    </head>
    <body>
    <h1>El meu segon python</h1>
    <ul>
    </body>
    """

    for index in range(10):
        html_content+= f"<li>hola[index]</li>\n"

    html_content +="""
    </ul>
    </body>
    </html>
    """
with open("output.html","w") as file:
    file.write(html_content)

print("HTML file has been generated")