from flask import Flask, request, Response, jsonify
import json
import sys

app = Flask(__name__)


if len(sys.argv) > 1: 
  mode = sys.argv[1]
  
  
else:
    print("missing required argument: testing|production")
    exit()
if mode =="testing":
  from flask_cors import CORS
  CORS(app)
  app.run(debug=True)
elif mode == "production":
    import bjoern
    print("running in production mode!")
    bjoern.run(app, "0.0.0.0", 5000)
else: 
    print("invalid mode, please choose either 'production or testing")
    exit()
