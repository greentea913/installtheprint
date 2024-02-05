from flask import Flask, render_template, request, send_file
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from createimage import draw_rectangle_with_dimensions
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user input from the form
        height = float(request.form.get('height', 1))
        width = float(request.form.get('width', 1))
        dot_x = float(request.form.get('dot_x', 1))
        dot_y = float(request.form.get('dot_y', 1))
        eyelevel = float(request.form.get('eyelevel', 1))
        output = draw_rectangle_with_dimensions(width, height, dot_x, dot_y, eyelevel )




        # Send the buffer as a response
        return send_file(io.BytesIO(output), mimetype='image/png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)