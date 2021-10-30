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
@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def home(): 
    try: 
        if flask.request.method == 'POST':
            next_todo=flask.request.form['title']
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            db.session.add(item(task=next_todo,Time=current_time,active=1))
            db.session.commit()
            Lists=item.query.all()
            #print(Lists)
            return (flask.render_template('index.html',items=reversed(Lists)))
        elif flask.request.method == 'GET':
            print(flask.request)
        else:
            item.query.delete()
            db.session.add(item(task="Add something in the To Do list",Time="00:00:00",active=1))
            db.session.commit()
            Lists=item.query.all()
            return (flask.render_template('index.html',items=Lists))    
    except:
        db.session.rollback()
        item.query.delete()
        db.session.add(item(task="Add something in the To Do list",Time="00:00:00",active=1))
        db.session.commit()
        Lists=item.query.all()
        return (flask.render_template('index.html',items=Lists))
if __name__=='__main__':
    app.run(debug=True)