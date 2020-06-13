from server import app
from flask import Flask,render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from multiprocessing import Value, Array
import random

allowSCDFaccess = Value('i', 1)

now = datetime.now()
d_string = now.strftime("%d%m%y")
t_string = now.strftime("%H%M%S")

pax = Array('i', [0,42,33,12,51,10])
lastUpdatedDate = Array('i', [0,int(d_string),int(d_string),int(d_string),int(d_string),int(d_string)])
lastUpdatedTime = Array('i', [0,int(t_string),int(t_string),int(t_string),int(t_string),int(t_string)])

"""app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_URI'] = 'sqlite://apidb.sqlite3'
app.config["SQLALCHEMY_TRACK_MODEIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class apidb(db.Model):
    __id = db.Column("id", db.Integer, primary_key=True)
    location = db.Column(db.String(100))
    numpax = db.Column("numpax",db.Integer)
    lastupdated = db.Column("lastupdated",db.Integer)

    def __init__(self, location):
        self.location = location

db.create_all()"""


"""



import ibm_boto3
from ibm_botocore.client import Config, ClientError

cos_credentials={
  "apikey": "3ifDMUyTxwW7C30JlKVRdi5FpijnReisfUVLNwjPgFBj",
  "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
  "iam_apikey_description": "Auto-generated for key 6c04872e-5bc4-431d-b608-28492aa4955f",
  "iam_apikey_name": "cloud-annotations-binding",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Writer",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/36c5a36d7ceb4e7690fc654b3802a2f9::serviceid:ServiceId-f43d7268-4c52-4dbd-b57b-d54ff7c7b1f2",
  "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/36c5a36d7ceb4e7690fc654b3802a2f9:ac1d32d4-e472-487b-86e8-d53aef97a86e::"
}
auth_endpoint = 'https://iam.bluemix.net/oidc/token'
service_endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'

cos = ibm_boto3.client('s3',
                         ibm_api_key_id=cos_credentials['apikey'],
                         ibm_service_instance_id=cos_credentials['resource_instance_id'],
                         ibm_auth_endpoint=auth_endpoint,
                         config=Config(signature_version='oauth'),
                         endpoint_url=service_endpoint)
cos.download_file(Bucket='bucketods-test',Key='timestamp0227.png',Filename='timestamp0227.png')

"""




# Create some test data for our catalog in the form of a list of dictionaries.



@app.route('/api/', methods=['GET'])
def home():
    return '''<h1>Emergency Response API</h1>
<p>A prototype API for accesing location, number of pax, and emergencies</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/locs/all', methods=['GET'])
def api_all():
    if allowSCDFaccess.value==1:
        locs = [
            {'id': 1,
             'location': 'Ground floor entrance 1',
             'number of pax': pax[1],
             'last updated date': lastUpdatedDate[1],
             'last updated time': lastUpdatedTime[1]},
            {'id': 2,
             'location': 'Ground floor entrance 2',
             'number of pax': pax[2],
             'last updated date': lastUpdatedDate[2],
             'last updated time': lastUpdatedTime[2]},
            {'id': 3,
             'location': 'Basement floor entrance 1',
             'number of pax': pax[3],
             'last updated date': lastUpdatedDate[3],
             'last updated time': lastUpdatedTime[3]},
             {'id': 4,
              'location': 'Basement floor shop 1',
              'number of pax': pax[4],
              'last updated date': lastUpdatedDate[4],
              'last updated time': lastUpdatedTime[4]},
              {'id': 5,
               'location': 'Basement floor atrium',
               'number of pax': pax[5],
               'last updated date': lastUpdatedDate[5],
               'last updated time': lastUpdatedTime[5]}
        ]
        return jsonify(locs)
    else:
        return 'SCDF has no access to the database currently as there are no emergencies.'

@app.route('/')
def hello_world():
    return render_template("index.html", static_url_path='/public')

@app.route('/<timestamp>')
def showTimestamp(timestamp):
    return app.send_static_file('indexname.html', content=timestamp)
    #return 'app.send_static_file('index.html')'

@app.route("/grantscdfaccess")
def grantscdfaccess():
    allowSCDFaccess.value = 1
    return "Access granted to SCDF"

@app.route("/denyscdfaccess")
def denyscdfaccess():
    allowSCDFaccess.value = 0
    return "SCDF access revoked"

@app.route("/write/<id>/<dataLoc>")
def writeDB(id, dataLoc):
    pax[int(id)] = int(dataLoc)
    now = datetime.now()
    d_string = now.strftime("%d%m%y")
    t_string = now.strftime("%H%M%S")
    lastUpdatedDate[int(id)] = int(d_string)
    lastUpdatedTime[int(id)] = int(t_string)
    return "Location " + id + " updated pax:" + dataLoc


@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
