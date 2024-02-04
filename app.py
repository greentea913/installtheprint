from flask import Flask, render_template, request, send_file
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user input from the form
        height = float(request.form.get('height', 1))
        width = float(request.form.get('width', 1))


        # Create a Matplotlib figure
        fig, ax = plt.subplots()
        ax.annotate(f"{width}", xy=(2 + width / 2, 2), xytext=(0, -30),
                    textcoords="offset points", ha='center', va='bottom')

        # Annotate height
        ax.annotate(f"{height}", xy=(2, 2 + height / 2), xytext=(-30, 0),
                    textcoords="offset points", ha='right', va='center')
        # Draw the rectangle with the user-specified height and width
        rectangle = plt.Rectangle((0, 0), width, height, fill=None,  edgecolor = 'blue', linewidth= 2)
        ax.add_patch(rectangle)
        ax.set_xlim([0, max(10, width)])
        ax.set_ylim([0, max(10, height)])
        # ax.set_xlim(0,1100)
        # ax.set_ylim(0, 1100)
        ax.set_aspect('equal')
        ax.axis('off')

        # Save it to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi = 300)
        plt.close(fig)
        buf.seek(0)

        # Send the buffer as a response
        return send_file(buf, mimetype='image/png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)