

# this is where we'll do the first app 
# This will be the back end of our website

# we'll import csv so we can handle csv files for stuff we can do for our webpage
import csv

# Then we import Flask

from flask import Flask
from flask import render_template
app = Flask(__name__)


# this function will go get the csv file and do stuff with later
def get_csv():
	csv_file_location = "./static/la-riots-deaths.csv"
	csv_file = open(csv_file_location, "rb")
	csv_object = csv.DictReader(csv_file)
	csv_reuseable_list = list(csv_object)
	return csv_reuseable_list
	
# now we are configuring flask using a lot of functions that are particular to flask

# here we connect this to a url ... the slash means it will be our homepage
# the route part is another function we've imported
@app.route("/")


# this is a function we're creating for creating a homepage
# we're going to use flask's render template to create our homepage
def index():
	template = 'index.html'
	object_list = get_csv()
	return render_template(template, object_list = object_list)

# now we're creating a link for the detail pages to link to
# we're going to take an id from the spreadsheet
# we're going to use that id for naming our new web pages
# the below will be a dynamically named page

@app.route("/<row_id>/")
def detail(row_id):
	template = "detail.html"
	object_list = get_csv()
	for object in object_list:
		if object['id'] == row_id:
			return render_template(template, object=object)
	
# this will return debug information, and we will allow it to reload when we update our data	
if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)

	
# our next steps will be to take data from a csv file and fling it into a web page
		
	
	


