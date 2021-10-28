import flask
app = flask.Flask(__name__, template_folder="Templates")
@app.route('/')
@app.route('/home')
def home():
     return flask.render_template('index.html')
@app.route('/forms',methods=['POST'])
def forms():
    if flask.request.method == 'POST':
        f_name=flask.request.form['fname']
        l_name=flask.request.form['lname']
        return (flask.render_template('form_post.html',f_name=f_name,l_name=l_name))
    else:
        return flask.render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)