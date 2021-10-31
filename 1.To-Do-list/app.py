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
def home(): 
    return (flask.render_template('index.html'))
if __name__=='__main__':
    app.run(debug=True)