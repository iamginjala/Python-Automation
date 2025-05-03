from flask import Flask, render_template, request, redirect, url_for,Response,flash
from  forms import LogParserForm
from werkzeug.utils import secure_filename
from parser import parse_log_file
import os

import csv
import io


app = Flask(__name__)
app.secret_key = "5rrh7tgd57j9mngtyhd"

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_form():
    form = LogParserForm()
    if form.validate_on_submit():
        f = form.logform.data
        filename = secure_filename(f.filename)

        # Folder setup
        upload_dir = os.path.join(app.instance_path, 'logs')
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, filename)

        # Check if file already exists
        if os.path.exists(file_path):
            flash(f"File '{filename}' already exists. Please rename your file or try another.", 'warning')
            return redirect(url_for('upload_form'))

        # Save and confirm
        f.save(file_path)
        flash(f"'{filename}' uploaded successfully!", 'success')
        return redirect(url_for('analyze_file', filename=filename))

    return render_template('upload.html', form=form)


@app.route('/analyze/<filename>')
def analyze_file(filename):
    filepath = os.path.join(app.instance_path, 'logs', filename)
    summary = parse_log_file(filepath)
    return render_template("analyze.html", summary=summary, filename=filename)


@app.route('/download_csv/<filename>')
def download_csv(filename):

    filepath = os.path.join(app.instance_path, 'logs', filename)
    summary = parse_log_file(filepath)

    output = io.StringIO()
    writer = csv.writer(output)

    # Write log level counts
    writer.writerow(["Log Level", "Count"])
    for level, count in summary["levels"].items():
        writer.writerow([level, count])

    # Blank line
    writer.writerow([])

    # Write top recurring messages
    writer.writerow(["Message", "Frequency"])
    for msg, freq in summary["top_messages"]:
        writer.writerow([msg, freq])

    output.seek(0)
    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}_summary.csv"}
    )

if __name__ == '__main__':
    app.run(debug=True)