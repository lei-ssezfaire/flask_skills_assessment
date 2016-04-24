from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index_page():
    """Homepage with link to application"""

    return render_template("index.html")
    

@app.route("/application-form")
def handle_form():
	"""Handles the submission of applicant information form"""

	return render_template("application-form.html")


@app.route("/application-confirmation")
def application_confirmation():
	"""Displays application confirmation message"""

	first_name = request.args.get("first-name")
	last_name = request.args.get("last-name")
	job_title = request.args.get("job-title")
	salary = request.args.get("salary-requirement")

	return render_template("application-response.html",
							first_name=first_name,
							last_name=last_name,
							job_title=job_title,
							salary=salary)


if __name__ == "__main__":
    app.run(debug=True)
