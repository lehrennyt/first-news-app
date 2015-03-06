# this is where we'll do the first app 
# This will be the back end of our website

# First we import Flask

from flask import Flask
from flask import render_template
app = Flask(__name__)

# now we are configuring flask using a lot of functions that are particular to flask

# here we connect this to a url ... the slash means it will be our homepage
# the route part is another function we've imported
@app.route("/")


# this is a function we're creating for creating a homepage
# we're going to use flask's render template to create our homepage
def index():
	template = 'index.html'
	return render_template(template)

# this will return debug information, and we will allow it to reload when we update our data	
if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)
	
		
	
	


