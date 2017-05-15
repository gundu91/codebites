from flask import Flask, request, render_template, redirect, url_for, Markup
		
app = Flask(__name__)

# Debug logging
import logging
import sys
# Defaults to stdout
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
try: 
	log.info('Logging to console')
except:
	_, ex, _ = sys.exc_info()
	log.error(ex.message)

@app.route('/')
def index():
	return render_template('index.html')
	
#@app.route('/resulsts/')
#def results_page():
#
#	# Get user input
#	user_input = request.args.get('user_input') # OR user_input = request.args.getlist("name")
#	if not user_input:
#		return redirect(url_for('index'))
#
#	return render_template('results/index.html', keyword_param=variable)
	
	
@app.errorhandler(404)
def page_not_found(e):
	return render_template("/error-pages/404.html")

if __name__ == "__main__":
	app.debug = True
	app.run()