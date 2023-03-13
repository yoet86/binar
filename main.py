from flask import Flask, request, redirect, url_for
import os
from os.path import join, dirname, realpath
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

import pandas as pd
import sqlite3

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title': LazyString(lambda: 'API Documentation for Data Processing and Modeling'),
        'version': LazyString(lambda: '2.0.0'),
        'description': LazyString(lambda: 'Dokumentasi API untuk Data Processing dan Modeling'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json'
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,config=swagger_config)

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

# Root URL
@app.route('/')
def hello():
    return "Hello World"

# Get the uploaded files
@swag_from("docs/data.yml", methods=['POST'])
@app.route("/uploadfiles", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
          # save the file
           df = pd.read_csv(file_path,encoding='latin-1', sep=',')
      return str(df)
             
if (__name__ == "__main__"):
     app.run(port = 5000)
