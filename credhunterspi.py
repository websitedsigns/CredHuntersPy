from flask import Flask, render_template, request, redirect, url_for
from flask import flash, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coasters.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

class Coaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    theme_park = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Coaster(name='{self.name}', manufacturer='{self.manufacturer}', theme_park='{self.theme_park}')"

db.create_all()

@app.route('/')
def index():
    coasters = Coaster.query.all()
    return render_template('index.html', coasters=coasters)

@app.route('/coasters/add', methods=['POST'])
def add_coaster():
    name = request.form['name']
    manufacturer = request.form['manufacturer']
    theme_park = request.form['theme_park']

    if name and manufacturer and theme_park:
        new_coaster = Coaster(name=name, manufacturer=manufacturer, theme_park=theme_park)
        db.session.add(new_coaster)
        db.session.commit()
        flash('Coaster added successfully!', 'success')
    else:
        flash('Please fill in all fields.', 'error')

    return redirect(url_for('index'))

@app.route('/coasters/remove/<int:coaster_id>', methods=['POST'])
def remove_coaster(coaster_id):
    coaster = Coaster.query.get_or_404(coaster_id)
    db.session.delete(coaster)
    db.session.commit()
    flash('Coaster removed successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/coasters/json')
def coaster_json():
    coasters = Coaster.query.all()
    coaster_list = [{'name': coaster.name, 'manufacturer': coaster.manufacturer, 'theme_park': coaster.theme_park} for coaster in coasters]
    return jsonify(coaster_list)

if __name__ == '__main__':
    app.run(debug=True)
