import flask
import flask_sqlalchemy
from datetime import datetime
app = flask.Flask(__name__, template_folder="Templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db= flask_sqlalchemy.SQLAlchemy(app)
#creating database model
class item(db.Model):
    #our database has the task the time stamp and the active as columns
    id=db.Column(db.Integer(),primary_key=True)
    task=db.Column(db.String(), nullable=False,unique=True)
    Time=db.Column(db.String())
    active=db.Column(db.Integer())
    def __repr__(self):
        return (f'Item {self.task}')

# we can add two decorators for the same wheel ie. both '/' and '/home' will take me to the same page
# here home page clears the database and displays a fresh list
@app.route('/',methods=['POST','GET'])
def landing():
    db.session.rollback()
    item.query.delete()
    db.session.commit()
    return flask.render_template('index.html')
# home page takes a new task from the user and adds it to the database
@app.route('/home',methods=['POST','GET'])
def home(): 
    try:
        # its put in a try block so that it always displays a page
        if flask.request.method == 'POST':
            todo=flask.request.form['title']
            #getting the current time 
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            db.session.add(item(task=todo,Time=current_time,active=1))
            db.session.commit()
            #getting all the data from the database
            List = item.query.all()
            #since the lastest task should ideally be on top we reverse the list
            return (flask.render_template('index.html',items=reversed(List)))
        else:
            List = item.query.all()
            return (flask.render_template('index.html',items=reversed(List)))    
    except:
        #catch block returns a blank list
        #print('error')
        db.session.rollback()
        return flask.render_template('index.html')
@app.route('/edit',methods=['POST'])
def change():
    #changes the status of the task when the user clicks on mark as done 
    #finding the id and then changing the active attribute
    row = item.query.filter_by(id=flask.request.form['Status']).first()
    row.active = 0
    db.session.commit()
    List = item.query.all()
    return (flask.render_template('index.html',items=reversed(List)))
@app.route('/delete',methods=['POST'])
def delete():
    #deletes the task when the user clicks on delete 
    #print(flask.request.form['Delete'])
    #finding the id and then deleting the row 
    obj = item.query.filter_by(id=flask.request.form['Delete']).one()
    db.session.delete(obj)
    db.session.commit()
    List = item.query.all()
    return (flask.render_template('index.html',items=reversed(List)))
if __name__=='__main__':
    app.run(debug=True)