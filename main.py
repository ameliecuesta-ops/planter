from flask import Flask, request, render_template, redirect, url_for, session,make_response
from PIL import Image
from werkzeug.utils import secure_filename
#import mysql.connector
import os
#import csv
from create import create_vase_carre, create_vase_rond


app = Flask(__name__)
#os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.secret_key = 'une_cle'

BASE_UPLOAD_FOLDER = r'C:\Users\tomds\HeliotropicPlanter\static\data'


@app.route('//<objet>')
def index(objet):
    return render_template('index.html', objet=objet)

@app.route('/a_propos')
def index():
    return render_template('a_propos.html')

@app.route('/contact')
def index():
    return render_template('contact.html')

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        style = request.form['style']
        width = request.form["width"]
        length = request.form['length']
        height = request.form["height"]
        nbdrain = request.form['nbdrain']
        handles= request.form['handles']
        path= ""+BASE_UPLOAD_FOLDER+"/"+style+"_"+str(width)+"_"+str(length)+"_"+str(height)+"_"+str(nbdrain)+"_"+str(handles)+"_"+"vase.obj"
        if os.path.exist(path):
            return redirect(url_for('', path))
        else:
            if style == "carre" :
                return redirect(url_for('',create_vase_carre(BASE_UPLOAD_FOLDER,style,width,length,height,nbdrain,handles)))
            elif style =="rond":
                return redirect(url_for('',create_vase_rond(BASE_UPLOAD_FOLDER,style,width,length,height,nbdrain,handles)))
    else:
        return "Erreur : méthode non autorisée ❌", 405
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)