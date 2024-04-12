from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/ecommerce'
db=SQLAlchemy(app)

class Buy(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    email=db.Column(db.Integer,nullable=False)
    phone_no=db.Column(db.Integer,nullable=False)
    adress=db.Column(db.Integer,nullable=False)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/buy",methods=['GET','POST'])
def buy():
    if(request.method=='POST'):
        uname=request.form.get('name')
        uemail=request.form.get('uemail')
        uphone=request.form.get('uphone')
        uadress=request.form.get('uadress')
        entry=Buy(name=uname,phone_no=uphone,email=uemail,adress=uadress)
        db.session.add(entry)
        db.session.commit()

    return render_template("buy.html")
if __name__=='__main__':
    app.run(debug=True)
