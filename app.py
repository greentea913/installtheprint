from flask import Flask, request, render_template, send_file, make_response
import io
import matplotlib
matplotlib.use('Agg')
import base64
from createimage import draw_rectangle_with_dimensions
app = Flask(__name__)

def get_float(value, default=0.0):
    try:
        return float(value)
    except ValueError:
        return default
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.method == 'POST':
            # Get the user input from the form
            height = float(request.form.get('height', 1))
            width = float(request.form.get('width', 1))
            dot_x = float(request.form.get('dot_x', 1))
            dot_y = float(request.form.get('dot_y', 1))
            dot_xx = get_float(request.form.get('dot_xx', 0))
            dot_yy = get_float(request.form.get('dot_yy', 0))
            eyelevel = float(request.form.get('eyelevel', 1450))
            output = draw_rectangle_with_dimensions(width, height, dot_x, dot_y, dot_xx, dot_yy, eyelevel)

        # Convert the image output to a Data URL
        data_url = base64.b64encode(output).decode('utf-8')
        image_data_url = f"data:image/png;base64,{data_url}"

        # Create a response with an HTML page that includes the image and a return button
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Image with Return Button</title>
            <style>
                /* This CSS ensures that the image is never larger than the viewport */
                img {{
                    max-width: 90%;
                    max-height: 90vh; /* vh is the viewport height unit */
                    display: block; /* This removes any extra space below the image */
                    margin: auto; /* This centers the image horizontally */
                }}
                body {{
                    text-align: center; /* This centers the button text */
                    margin: 0;
                    padding: 0;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    height: 100vh;
                }}
                button {{
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <img src="{image_data_url}" alt="Generated Image">
            <button onclick="window.location.href='/'">Return to Form</button>
        </body>
        </html>
        '''
        return html

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)