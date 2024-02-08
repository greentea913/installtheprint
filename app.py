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
        # Get the user input from the form
        height = float(request.form.get('height', 1))
        width = float(request.form.get('width', 1))
        dot_x = float(request.form.get('dot_x', 1))
        dot_y = float(request.form.get('dot_y', 1))
        dot_xx = get_float(request.form.get('dot_xx', 0))
        dot_yy = get_float(request.form.get('dot_yy', 0))
        title = str(request.form.get('framename', ""))
        eyelevel = float(request.form.get('eyelevel', 1450))
        try:
            output = draw_rectangle_with_dimensions(title, width, height, dot_x, dot_y, dot_xx, dot_yy, eyelevel)
        except Exception as e:
            # Handle the exception in a way that makes sense for your application
            print(str(e))
            return str(e), 500


        # Convert the image output to a Data URL
        data_url = base64.b64encode(output).decode('utf-8')
        image_data_url = f"data:image/png;base64,{data_url}"
        return render_template('imageoutput.html', image_data_url=image_data_url)
        

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)