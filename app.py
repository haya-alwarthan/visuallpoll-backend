import mimetypes

from stats_data import getClassesStats, getStatusTotal
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
from flask import Flask,render_template 
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource,reqparse,abort
from data import getData
import json

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
pollution_data=getData()
classes_stats= getClassesStats()
rel=list(pollution_data.values())[:5]
print(json.dumps(rel, indent = 4))
predicted_images= {
1:{
    'img':'',
    'lat':0,
    'lng':0,
    'detection':[
        {
            'bbox':[1,1,1,1],
            'class':'garbage'
        },
        {
             'bbox':[1,1,1,1],
            'class':'garbage'
        },
    ],


}

}




class PollutionItem(Resource):

    def get(self, id):
        print(pollution_data[id])
        return pollution_data[id]
        


class PollutionList(Resource):
#starts with 0, ends with 7873
 def get(self, offset,limit):
        if int(offset)>=int(limit):
            abort(404,messege= "Offset can not be larger than limit")
        relist= list(pollution_data.values())
        return relist[int(offset):int(limit)]      


class ClassesStats(Resource):
#starts with 0, ends with 7873
    def get(self):
        relist= list(classes_stats.values())
        return relist   

class StatusTotal(Resource):
#starts with 0, ends with 7873
    def get(self):
        return getStatusTotal()     



# add a paramete to the request
api.add_resource(PollutionItem,'/api/pollution/<string:id>')
api.add_resource(PollutionList,'/api/pollutions/<string:offset>/<string:limit>')
api.add_resource(ClassesStats,'/api/stats/classes')
api.add_resource(StatusTotal,'/api/stats/total')


@app.route('/')
@cross_origin()
def root():
    return render_template("index.html")

# The above function returns the HTML code to be displayed on the page

 
 
# Debug flag to view all logs(remove it in production)
if __name__ == '__app__':
   app.run(debug=True)