# import modules from flask (jsonify is for google colab func)
from flask import Blueprint, render_template, request, redirect, jsonify
# import object instantiated from class in generator
from .generator import ai

generator = Blueprint('generator', __name__)
# create/specify a route
#'/' is index
@generator.route('/')
def index():
        # this blueprint and flask setup that we 
        # have configured here is going to look 
        # inside of templates for the files that we 
        # are going to return here
        return render_template('index.html')

# analyse route
@generator.route('/analyze', methods=['POST'])
def analyze():
        # extract title from index.html
        title = request.form['title']
        # generate text with ai and function
        text = ai.generate_text(title)
        # parse response text generated from ai to index.html
        return render_template('index.html', text=text)
