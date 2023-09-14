from flask import Flask, render_template, request, redirect, url_for, abort, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms import validators
from sqlalchemy import or_, desc
from functools import wraps



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recettes.db'
#initialize db
db = SQLAlchemy(app)

app.secret_key = os.urandom(15)

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#create db model 
class Recettes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    nameEng = db.Column(db.String(200), nullable=True)
    
    img1 = db.Column(db.String(250), nullable=True)
    img2 = db.Column(db.String(250), nullable=True)
    img3 = db.Column(db.String(250), nullable=True)
    img4 = db.Column(db.String(250), nullable=True)
    img5 = db.Column(db.String(250), nullable=True)
    img6 = db.Column(db.String(250), nullable=True)
    img7 = db.Column(db.String(250), nullable=True)
    img8 = db.Column(db.String(250), nullable=True)
    img9 = db.Column(db.String(250), nullable=True)
    img10 = db.Column(db.String(250), nullable=True)
    p1 = db.Column(db.String(500), nullable=True)
    p2 = db.Column(db.String(500), nullable=True)
    p3 = db.Column(db.String(500), nullable=True)
    p4 = db.Column(db.String(500), nullable=True)
    p5 = db.Column(db.String(500), nullable=True)
    p6 = db.Column(db.String(500), nullable=True)
    p7 = db.Column(db.String(500), nullable=True)
    p8 = db.Column(db.String(500), nullable=True)
    p9 = db.Column(db.String(500), nullable=True)
    p10 = db.Column(db.String(500), nullable=True)
    p1Eng = db.Column(db.String(500), nullable=True)
    p2Eng = db.Column(db.String(500), nullable=True)
    p3Eng = db.Column(db.String(500), nullable=True)
    p4Eng = db.Column(db.String(500), nullable=True)
    p5Eng = db.Column(db.String(500), nullable=True)
    p6Eng = db.Column(db.String(500), nullable=True)
    p7Eng = db.Column(db.String(500), nullable=True)
    p8Eng = db.Column(db.String(500), nullable=True)
    p9Eng = db.Column(db.String(500), nullable=True)
    p10Eng = db.Column(db.String(500), nullable=True)
    meal = db.Column(db.String(50), nullable=True)
    mealEng = db.Column(db.String(50), nullable=True)
    energy1 = db.Column(db.String(50), nullable=True)
    energy2 = db.Column(db.String(50), nullable=True)
    energy3 = db.Column(db.String(50), nullable=True)
    energy1Eng = db.Column(db.String(50), nullable=True)
    energy2Eng = db.Column(db.String(50), nullable=True)
    energy3Eng = db.Column(db.String(50), nullable=True)
    sit1 = db.Column(db.String(50), nullable=True)
    sit2 = db.Column(db.String(50), nullable=True)
    sit3 = db.Column(db.String(50), nullable=True)
    sit1Eng = db.Column(db.String(50), nullable=True)
    sit2Eng = db.Column(db.String(50), nullable=True)
    sit3Eng = db.Column(db.String(50), nullable=True)
    color1 = db.Column(db.String(50), nullable=True)
    color2 = db.Column(db.String(50), nullable=True)
    color3 = db.Column(db.String(50), nullable=True)
    color1Eng = db.Column(db.String(50), nullable=True)
    color2Eng = db.Column(db.String(50), nullable=True)
    color3Eng = db.Column(db.String(50), nullable=True)
    like_count = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(15), nullable=True)
    prepTime = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #create func to return strng when something is added
    def __repr__(self):
        return '<Name %r>' % self.id

with app.app_context():
    db.create_all()


class ColorForm(FlaskForm):
    color = SelectField('Color', choices=[('all', 'Couleur'), ('vert', 'Vert'), ('blanc', 'Blanc'), ('bleu', 'Bleu'), ('orange', 'Orange'), ('rouge', 'Rouge'), ('marron', 'Marron'), ('jaune', 'Jaune') ], validators=[DataRequired()])
    energy = SelectField('Energy', choices=[('all', 'Energie'), ('joie', 'Joie'), ('nostalgie', 'Nostalgie'),('reconfort', 'Reconfort'),('leger', 'Leger'),('relaxant', 'Relaxant'),('romantique', 'Romantique'),('puissance', 'Puissance'),('amour', 'Amour'),('partage', 'Partage'),('festif', 'Festif')], validators=[DataRequired()])
    situation = SelectField('Situation', choices=[('all', 'Contexte'), ('famille', 'Famille'),('rapide', 'Rapide'), ('amis', 'Amis'),('fete', 'Fete'),('brunch', 'Brunch'),('apero-meze', 'Apero-meze'),('sportif', 'Sportif'),('convalescence', 'Convalescence'), ('slow-food', 'Slow-food')], validators=[DataRequired()])
    submit = SubmitField('Filter')
    
class ColorForm2(FlaskForm):
    color = SelectField('Color', choices=[('all', 'Couleur'), ('vert', 'Vert'), ('blanc', 'Blanc'), ('bleu', 'Bleu'), ('orange', 'Orange'), ('rouge', 'Rouge'), ('marron', 'Marron'), ('jaune', 'Jaune') ], validators=[DataRequired()])
    energy = SelectField('Energy', choices=[('all', 'Energie'), ('joie', 'Joie'), ('nostalgie', 'Nostalgie'),('reconfort', 'Reconfort'),('leger', 'Leger'),('relaxant', 'Relaxant'),('romantique', 'Romantique'),('puissance', 'Puissance'),('amour', 'Amour'),('partage', 'Partage'),('festif', 'Festif')], validators=[DataRequired()])
    situation = SelectField('Situation', choices=[('all', 'Contexte'), ('famille', 'Famille'),('rapide', 'Rapide'), ('amis', 'Amis'),('fete', 'Fete'),('brunch', 'Brunch'),('apero-meze', 'Apero-meze'),('sportif', 'Sportif'),('convalescence', 'Convalescence'), ('slow-food', 'Slow-food')], validators=[DataRequired()])
    submit = SubmitField('Filter')


class MainFilterForm(FlaskForm):
    main_filter = SelectField('Main Filter', choices=[('apéritif', 'Apéritif'), ('entrée', 'Entrée'), ('plat principal', 'Plat principal'), ('légume', 'Légume'), ('dessert', 'Dessert'), ('fruit', 'Fruit'), ('boisson', 'boisson'), ('petit-déjeuner', 'Petit-déjeuner')], validators=[DataRequired()])
    submit = SubmitField('Filter')

def login_required(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('/'))
        return route_function(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = Recettes.query.get_or_404(id)
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/upload')
    except:
        return "There was a problem deleting the data"

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    item_to_update =  Recettes.query.get_or_404(id)
    if request.method == "POST":
        item_to_update.name = request.form['name']
        item_to_update.nameEng = request.form['nameEng']
        for i in range(1, 11):
            if f"image{i}" in request.files:
                image = request.files[f"image{i}"]
                if image.filename:
                    filename = secure_filename(image.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image.save(image_path)
                    setattr(item_to_update, f"img{i}", image_path)
        
        item_to_update.p1 = request.form['p1']
        item_to_update.p1Eng = request.form['p1Eng']
        item_to_update.p2 = request.form['p2']
        item_to_update.p2Eng = request.form['p2Eng']
        item_to_update.p3 = request.form['p3']
        item_to_update.p3Eng = request.form['p3Eng']
        item_to_update.p4 = request.form['p4']
        item_to_update.p4Eng = request.form['p4Eng']
        item_to_update.p5 = request.form['p5']
        item_to_update.p5Eng = request.form['p5Eng']
        """
        item_to_update.p6 = request.form['p6']
        item_to_update.p6Eng = request.form['p6Eng']
        item_to_update.p7 = request.form['p7']
        item_to_update.p7Eng = request.form['p7Eng']
        item_to_update.p8 = request.form['p8']
        item_to_update.p8Eng = request.form['p8Eng']
        item_to_update.p9 = request.form['p9']
        item_to_update.p9Eng = request.form['p9Eng']
        item_to_update.p10 = request.form['p10']
        """
        item_to_update.p10Eng = request.form['p10Eng']
        item_to_update.meal = request.form['meal']
        item_to_update.mealEng = request.form['mealEng']
        item_to_update.energy1 = request.form['energy1']
        item_to_update.energy2 = request.form['energy2']
        item_to_update.energy3 = request.form['energy3']
        item_to_update.energy1Eng = request.form['energy1Eng']
        item_to_update.energy2Eng = request.form['energy2Eng']
        item_to_update.energy3Eng = request.form['energy3Eng']
        item_to_update.sit1 = request.form['sit1']
        item_to_update.sit2 = request.form['sit2']
        item_to_update.sit3 = request.form['sit3']
        item_to_update.sit1Eng = request.form['sit1Eng']
        item_to_update.sit2Eng = request.form['sit2Eng']
        item_to_update.sit3Eng = request.form['sit3Eng']
        item_to_update.color1 = request.form['color1']
        item_to_update.color2 = request.form['color2']
        item_to_update.color3 = request.form['color3']
        item_to_update.color1Eng = request.form['color1Eng']
        item_to_update.color2Eng = request.form['color2Eng']
        item_to_update.color3Eng = request.form['color3Eng']
        item_to_update.prepTime = request.form['prepTime']

        
        try:
            db.session.commit()
            print("here")
            return redirect('/upload')
        except:
            return "There was an error"
    else:
        return render_template('update.html', item_to_update=item_to_update)

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    selected_meal = request.args.get('main_filter')
    page = request.args.get('page', 1, type=int)
    per_page = 5

    # Create the base query
    query = db.session.query(Recettes).order_by(desc(Recettes.date_created))

    form = ColorForm2(request.form)

    if selected_meal:
        query = query.filter(Recettes.meal.ilike(selected_meal))

    selected_color = form.color.data
    selected_energy = form.energy.data
    selected_situation = form.situation.data
    
    
    if form.validate_on_submit():
        if selected_color != 'all':
            query = query.filter(
                (Recettes.color1 == selected_color) |
                (Recettes.color2 == selected_color) |
                (Recettes.color3 == selected_color)
            )
        
        if selected_energy != 'all':
            query = query.filter(
                or_(
                    Recettes.energy1 == selected_energy,
                    Recettes.energy2 == selected_energy,
                    Recettes.energy3 == selected_energy
                )
            )
    
        if selected_situation != 'all':
            query = query.filter(Recettes.sit1 == selected_situation)
    
    search_query = request.args.get('search_query')
    if search_query:
        search_columns = [Recettes.name, Recettes.p1, Recettes.p2, Recettes.p3, Recettes.p4, Recettes.p5]
        query_filters = [column.ilike(f'%{search_query}%') for column in search_columns]
        query = query.filter(or_(*query_filters))
    
    # Paginate the query
    paginated_results = query.paginate(page=page, per_page=per_page, error_out=False)
    total_recipes = db.session.query(Recettes).count()

    return render_template('recipes.html', results=paginated_results, main_filter=selected_meal, selected_meal=selected_meal, total_recipes=total_recipes, form=form, search_query=search_query)

@app.route('/videos', methods=['GET', 'POST'])
def videos():
    selected_meal = request.args.get('main_filter')
    form = ColorForm2()
    search_query = request.args.get('search_query')

    if selected_meal:
        main_results = Recettes.query.filter(Recettes.meal.ilike(selected_meal)).all()
        if main_results:
            # Main filter has a valid result, proceed with filtering based on color, energy, and situation
            if form.validate_on_submit():
                selected_color = form.color.data
                selected_energy = form.energy.data
                selected_situation = form.situation.data

                filtered_results = [result for result in main_results if
                                    result.color1 == selected_color and
                                    result.energy1 == selected_energy and
                                    result.sit1 == selected_situation]
                results = filtered_results
            else:
                results = main_results
        else:
            # Main filter does not have a valid result, fallback to default behavior
            results = Recettes.query.order_by(Recettes.date_created.desc())
    else:
        # No main filter selected, fallback to default behavior
        if form.validate_on_submit():
            selected_color = form.color.data
            selected_energy = form.energy.data
            selected_situation = form.situation.data

            if selected_color != 'all' and selected_energy != 'all' and selected_situation != 'all':
                results = Recettes.query.filter_by(color1=selected_color,
                                                   energy1=selected_energy,
                                                   sit1=selected_situation).order_by(Recettes.date_created.desc())
            elif selected_color != 'all' and selected_situation == 'all' and selected_energy == 'all':
                results = Recettes.query.filter_by(color1=selected_color).order_by(Recettes.date_created.desc())
            elif selected_energy != 'all' and selected_situation == 'all' and selected_color == 'all':
                results = Recettes.query.filter_by(energy1=selected_energy).order_by(Recettes.date_created.desc())
            elif selected_situation != 'all' and selected_color == 'all' and selected_energy == 'all':
                results = Recettes.query.filter_by(sit1=selected_situation).order_by(Recettes.date_created.desc())
            elif selected_color != 'all' and selected_situation != 'all' and selected_energy == 'all':
                results = Recettes.query.filter_by(color1=selected_color, sit1=selected_situation).order_by(
                    Recettes.date_created.desc())
            elif selected_color != 'all' and selected_energy != 'all' and selected_situation == 'all':
                results = Recettes.query.filter_by(color1=selected_color, energy1=selected_energy).order_by(
                    Recettes.date_created.desc())
            elif selected_situation != 'all' and selected_energy != 'all' and selected_color == 'all':
                results = Recettes.query.filter_by(sit1=selected_situation, energy1=selected_energy).order_by(
                    Recettes.date_created.desc())
            else:
                results = Recettes.query.order_by(Recettes.date_created.desc())
        else:
            results = Recettes.query.order_by(Recettes.date_created.desc())
    
    search_columns = [Recettes.name, Recettes.p1, Recettes.p2, Recettes.p3, Recettes.p4, Recettes.p5]
    
    if search_query:
        query_filters = []
        for column in search_columns:
            query_filters.append(column.ilike(f'%{search_query}%'))
        
        results = results.filter(or_(*query_filters)).order_by(Recettes.date_created.desc())
    
    
    page = request.args.get('page', 1, type=int)
    per_page = 5
    paginated_results = results.paginate(page=page, per_page=per_page)
    total_recipes = Recettes.query.count()
    

    return render_template('videos.html', form=form, results=paginated_results, main_filter=selected_meal, total_recipes=total_recipes, search_query=search_query)

@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def recipe(recipe_id):
    selected_meal = request.args.get('main_filter')
    form = ColorForm2()
    recipe = Recettes.query.get(recipe_id)
    
    print(recipe)
    print(recipe.name)
    print(recipe.img1)
    
    if selected_meal:
        main_results = Recettes.query.filter(Recettes.meal.ilike(selected_meal)).all()
        if main_results:
            # Main filter has a valid result, proceed with filtering based on color, energy, and situation
            if form.validate_on_submit():
                selected_meal = request.args.get('main_filter')
                selected_color = form.color.data
                selected_energy = form.energy.data
                selected_situation = form.situation.data

                filtered_results = [result for result in main_results if result.meal == selected_meal and result.color1 == selected_color and result.energy1 == selected_energy and result.sit1 == selected_situation]
                results = sorted(filtered_results, key=lambda x: x.date_created, reverse=True)
            else:
                results = sorted(main_results, key=lambda x: x.date_created, reverse=True)
        else:
            # Main filter does not have a valid result, fallback to default behavior
            results = Recettes.query.order_by(Recettes.date_created.desc()).all()
    else:
        # No main filter selected, fallback to default behavior
        if form.validate_on_submit():
            selected_color = form.color.data
            selected_energy = form.energy.data
            selected_situation = form.situation.data

            if selected_color != 'all' and selected_energy != 'all' and selected_situation != 'all':
                results = Recettes.query.filter_by(color1=selected_color, energy1=selected_energy, sit1=selected_situation).order_by(Recettes.date_created.desc()).all()
            elif selected_color != 'all' and selected_situation == 'all' and selected_energy == 'all':
                results = Recettes.query.filter_by(color1=selected_color).order_by(Recettes.date_created.desc()).all()
            elif selected_energy != 'all' and selected_situation == 'all' and selected_color == 'all':
                results = Recettes.query.filter_by(energy1=selected_energy).order_by(Recettes.date_created.desc()).all()
            elif selected_situation != 'all' and selected_color == 'all' and selected_energy == 'all':
                results = Recettes.query.filter_by(sit1=selected_situation).order_by(Recettes.date_created.desc()).all()
            elif selected_color != 'all' and selected_situation != 'all' and selected_energy == 'all':
                results = Recettes.query.filter_by(color1=selected_color, sit1=selected_situation).order_by(Recettes.date_created.desc()).all()
            elif selected_color != 'all' and selected_energy != 'all' and selected_situation == 'all':
                results = Recettes.query.filter_by(color1=selected_color, energy1=selected_energy).order_by(Recettes.date_created.desc()).all()
            elif selected_situation != 'all' and selected_energy != 'all' and selected_color == 'all':
                results = Recettes.query.filter_by(sit1=selected_situation, energy1=selected_energy).order_by(Recettes.date_created.desc()).all()
            else:
                results = Recettes.query.order_by(Recettes.date_created.desc()).all()
        else:
            results = Recettes.query.order_by(Recettes.date_created.desc()).all()

    return render_template('recipe.html', form=form, results=results, main_filter=selected_meal, recipe=recipe)

def login_required(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('index'))
        return route_function(*args, **kwargs)
    return decorated_function



@app.route('/upload', methods=['POST', 'GET'])
@login_required
def upload():
    if request.method == "POST":
        name = request.form['name']
        nameEng = request.form['nameEng']
        if 'image1' in request.files:
            image1 = request.files['image1']
            img1 = request.form['img1']
            if image1.filename:
                filename = secure_filename(image1.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image1.save(image_path)
                img1 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            else:
                img1 = None
        if 'image2' in request.files:
            image2 = request.files['image2']
            img2 = request.form['img2']
            if image2.filename:
                filename = secure_filename(image2.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image2.save(image_path)
                img2 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            else:
                img2 = None
        if 'image3' in request.files:
            image3 = request.files['image3']
            img3 = request.form['img3']
            if image3.filename:
                filename = secure_filename(image3.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image3.save(image_path)
                img3 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            else:
                img3 = None
        if 'image4' in request.files:
                image4 = request.files['image4']
                img4 = request.form['img4']
                if image4.filename:
                    filename = secure_filename(image4.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image4.save(image_path)
                    img4 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                else:
                    img4 = None
        if 'image5' in request.files:
                image5 = request.files['image5']
                img5 = request.form['img5']
                if image5.filename:
                    filename = secure_filename(image5.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image5.save(image_path)
                    img5 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                else:
                    img5 = None
        if 'image6' in request.files:
                image6 = request.files['image6']
                img6 = request.form['img6']
                if image6.filename:
                    filename = secure_filename(image6.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image6.save(image_path)
                    img6 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                else:
                    img6 = None
        if 'image7' in request.files:
                image7 = request.files['image7']
                img7 = request.form['img7']
                if image7.filename:
                    filename = secure_filename(image7.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image7.save(image_path)
                    img7 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                else:
                    img7 = None
        if 'image8' in request.files:
                image8 = request.files['image8']
                img8 = request.form['img8']
                if image8.filename:
                    filename = secure_filename(image8.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image8.save(image_path)
                    img8 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                else:
                    img8 = None
        if 'image9' in request.files:
                image9 = request.files['image9']
                img9 = request.form['img9']
                if image9.filename:
                    filename = secure_filename(image9.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image9.save(image_path)
                    img9 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                else:
                    img9 = None
        if 'image10' in request.files:
                image10 = request.files['image10']
                img10 = request.form['img10']
                if image10.filename:
                    filename = secure_filename(image10.filename)
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image10.save(image_path)
                    img10 = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                else:
                    img10 = None
        p1 = request.form['p1']
        p2 = request.form['p2']
        p3 = request.form['p3']
        p4 = request.form['p4']
        p5 = request.form['p5']
        """
        p6 = request.form['p6']
        p7 = request.form['p7']
        p8 = request.form['p8']
        p9 = request.form['p9']
        p10 = request.form['p10']
        """
        p1Eng = request.form['p1Eng']
        p2Eng = request.form['p2Eng']
        p3Eng = request.form['p3Eng']
        p3Eng = request.form['p3Eng']
        p4Eng = request.form['p4Eng']
        p5Eng = request.form['p5Eng']
        """
        p6Eng = request.form['p6Eng']
        p7Eng = request.form['p7Eng']
        p8Eng = request.form['p8Eng']
        p9Eng = request.form['p9Eng']
        """
        p10Eng = request.form['p10Eng']
        
        meal = request.form['meal']
        mealEng = request.form['mealEng']
        energy1 = request.form['energy1']
        energy2 = request.form['energy2']
        energy3 = request.form['energy3']
        energy1Eng = request.form['energy1Eng']
        energy2Eng = request.form['energy2Eng']
        energy3Eng = request.form['energy3Eng']
        sit1 = request.form['sit1']
        sit2 = request.form['sit2']
        sit3 = request.form['sit3']
        sit1Eng = request.form['sit1Eng']
        sit2Eng = request.form['sit2Eng']
        sit3Eng = request.form['sit3Eng']
        color1 = request.form['color1']
        color2 = request.form['color2']
        color3 = request.form['color3']
        color1Eng = request.form['color1Eng']
        color2Eng = request.form['color2Eng']
        color3Eng = request.form['color3Eng']
        prepTime = request.form['prepTime']

        new_data = Recettes(name=name, nameEng=nameEng, img1=img1, img2=img2, img3=img3, img4=img4, img5=img5, img6=img6, img7=img7, img8=img8, img9=img9, img10=img10, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p1Eng=p1Eng, p2Eng=p2Eng, p3Eng=p3Eng, p4Eng=p4Eng, p5Eng=p5Eng,  p10Eng=p10Eng, meal=meal, mealEng=mealEng, energy1=energy1, energy2=energy2, energy3=energy3, energy1Eng=energy1Eng, energy2Eng=energy2Eng, energy3Eng=energy3Eng, sit1=sit1, sit2=sit2, sit3=sit3, sit1Eng=sit1Eng, sit2Eng=sit2Eng, sit3Eng=sit3Eng, color1=color1, color2=color2, color3=color3, color1Eng=color1Eng, color2Eng=color2Eng, color3Eng=color3Eng, prepTime=prepTime)
        #push
        try:
            db.session.add(new_data)
            db.session.commit()
            return redirect('/upload')
        except:
            return "Something went wrong"
    else:
        all_data = Recettes.query.order_by(Recettes.date_created.desc()).all()
        return render_template('upload.html', all_data=all_data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'theMagictheLaila' and password == '345dkgb&':
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=120)
            session['logged_in'] = True
            return redirect('/upload')
        
        else:
            return """
                <script>
                    window.close();
                </script>
                """
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)