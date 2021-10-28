import flask
import flask_sqlalchemy
app = flask.Flask(__name__, template_folder="Templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db= flask_sqlalchemy.SQLAlchemy(app)

class item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    task=db.Column(db.String(), nullable=False,unique=True)
    Time=db.Column(db.String())
    active=db.Column(db.Integer())
    def __repr__(self):
        return (f'Item {self.task}')


@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def home(): 
    if flask.request.method == 'POST':
        next_todo=flask.request.form['title']
        print(next_todo)
        list=item.query.all()
        return (flask.render_template('index.html',list=list))
    else:
        list=item.query.all()
        return (flask.render_template('index.html',list=list))
if __name__=='__main__':
    app.run(debug=True)