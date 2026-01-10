---
title: Comment authentifier les utilisateurs dans Flask avec Flask-Login
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-01T20:00:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-authenticate-users-in-flask
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/Auth-in-Flask.png
tags:
- name: Application Security
  slug: application-security
- name: authentication
  slug: authentication
- name: Flask Framework
  slug: flask
- name: Python
  slug: python
seo_title: Comment authentifier les utilisateurs dans Flask avec Flask-Login
seo_desc: 'By Ondiek Elijah Ochieng

  When you''re developing applications for the general public, it''s important to
  protect your users'' credentials and information. This means you need to know about
  code structure and how to implement various security measures.

  I...'
---

Par Ondiek Elijah Ochieng

Lorsque vous développez des applications pour le grand public, il est important de protéger les informations d'identification et les données de vos utilisateurs. Cela signifie que vous devez connaître la structure du code et savoir comment implémenter diverses mesures de sécurité.

Dans cet article, nous allons passer en revue les étapes pour créer une application web d'authentification d'utilisateurs avec Flask, un micro framework web. Pour l'authentification, nous utiliserons la bibliothèque Python `flask_login`.

Cette application inclut des fonctionnalités telles que la validation de formulaires, la création de comptes et la fonctionnalité de connexion/déconnexion pour les utilisateurs authentifiés.

## Installation et configuration de l'application

Vous pouvez trouver un guide complet sur la configuration et l'installation du projet dans mon dépôt [GitHub](https://github.com/Dev-Elie/User-Authentication-in-Flask/tree/main#readme).

### Structure de base de l'application

Pour cette application, nous aurons un environnement virtuel dans son propre répertoire, ainsi qu'un dossier contenant les fichiers principaux de l'application. Voici un aperçu de la structure de l'application :

**.**  
├── **auth-app**  
│   ├── app.py   
│   ├── database.db   
│   ├── forms.py   
│   ├── manage.py   
│   ├── **migrations**  
│   ├── models.py   
│   ├── requirements.txt   
│   ├── routes.py   
│   ├── **run**  
│   ├── **static**  
│   └── **templates**  
│       ├── auth.html   
│       ├── base.html   
│       └── index.html   
└── **venv**

### Usine d'application

Pour commencer, nous allons créer une fonction d'usine d'application dans le fichier app.py et l'appeler `create_app`. Cela est vital pour toute application Flask.

De plus, nous devons rendre certaines bibliothèques disponibles pour une utilisation dans notre projet, nous allons donc importer ce qui suit :

**app.py**

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)
```

Nous avons importé Flask, SQLAlchemy pour aider notre application Python à communiquer avec une base de données, Bcrypt pour le hachage des mots de passe, Migrate pour les migrations de base de données, et plusieurs autres méthodes de Flask-Login pour la gestion des sessions.

```python
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"
```

Pour utiliser flask_login, nous allons créer une instance comme montré ci-dessus. Nous ferons de même pour SQLAlchemy, Migrate et Bcrypt.

```python
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
```

Au lieu de créer notre instance Flask globalement, nous le ferons dans une fonction car le faire globalement devient difficile à mesure que le projet grandit. 

L'avantage de le faire dans une fonction est que cela permet plusieurs instances d'application (également pendant les tests). (Source : [flask.palletsprojects.com](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/#application-factories))

```python
def create_app():
    app = Flask(__name__)

    app.secret_key = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    return app
```

Flask-Login nécessite également que nous définissions une clé secrète pour fonctionner. De plus, vous remarquerez que nous avons nos initialisations à l'intérieur de l'usine d'application. Nous faisons cela pour éviter que les extensions ne se lient initialement à l'application, comme expliqué [ici](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/#factories-extensions).

Maintenant que nous avons terminé notre usine d'application de base, il est temps de déclarer notre modèle Utilisateur. Dans la table des utilisateurs, nous n'avons besoin que des colonnes email, nom d'utilisateur et mot de passe pour cette application.

**models.py**

```python
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
```

Nous importons db, une instance de SQLAlchemy, et une sous-classe UserMixin de Flask-Login dans l'extrait de code ci-dessus. Notre travail est simplifié par l'utilisation de UserMixin, qui nous permet d'utiliser des méthodes telles que **is_authenticated()**, **is_active()**, **is_anonymous()**, et **get_id()**.

Si nous n'incluons pas UserMixin dans notre modèle Utilisateur, nous obtiendrons des erreurs comme `'User' object has no attribute 'is_active'`.

Nous avons actuellement un modèle Utilisateur, mais nous n'avons pas encore créé la table. Pour ce faire, exécutez `python manage.py` sur votre terminal dans votre répertoire de projet—en supposant que vous avez bien configuré, installé les packages dans le fichier requirements.txt et que vous avez un environnement virtuel actif.

**manage.py**

```python
def deploy():
	"""Exécuter les tâches de déploiement."""
	from app import create_app,db
	from flask_migrate import upgrade,migrate,init,stamp
	from models import User

	app = create_app()
	app.app_context().push()
	db.create_all()

	# migrer la base de données vers la dernière révision
	init()
	stamp()
	migrate()
	upgrade()
	
deploy()
```

La fonction `deploy` importe la fonction `create_app` du fichier `app.py`, les méthodes de migration Flask-Migrate et le modèle Utilisateur. Nous nous assurons ensuite que nous travaillons dans un contexte d'application, à partir duquel nous pouvons maintenant appeler `db.create_all()`, qui prendra en charge la création de notre table.

Nous devons encore configurer les formulaires de connexion et d'inscription. Tout d'abord, nous devons préparer les deux formulaires Flask avant de les rendre sur le modèle. La configuration des formulaires est montrée ci-dessous. Pour garder cet article propre et précis, je vais omettre les lignes d'importation. Pour les lignes d'importation exclues, voir le dépôt [GitHub](https://github.com/Dev-Elie/User-Authentication-in-Flask).

### forms.py

**a). Formulaire d'inscription**

```python
class register_form(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(3, 20, message="Veuillez fournir un nom valide"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Les noms d'utilisateur doivent contenir uniquement des lettres, " "des chiffres, des points ou des traits de soulignement",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(8, 72)])
    cpwd = PasswordField(
        validators=[
            InputRequired(),
            Length(8, 72),
            EqualTo("pwd", message="Les mots de passe doivent correspondre !"),
        ]
    )
```

Dans l'extrait de code ci-dessus, nous appliquons simplement des validations aux champs requis importés de `wtforms` et les attribuons aux noms de variables de champs de formulaire. 

```python
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email déjà enregistré !")

    def validate_uname(self, uname):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Nom d'utilisateur déjà pris !")
```

Pour accélérer le processus de validation, nous devons réduire la charge et le temps nécessaires pour la validation côté serveur. Pour y parvenir, nous ajoutons les lignes de code ci-dessus—validation de l'email et du nom d'utilisateur à notre classe de formulaire d'inscription afin qu'elle soit gérée côté client.

**b). Formulaire de connexion**

```python
class login_form(FlaskForm):
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])
    # Étiquettes de remplissage pour permettre le rendu du formulaire
    username = StringField(
        validators=[Optional()]
    )
```

Pour rendre les champs de formulaire visibles sur le modèle, nous devons passer l'objet de formulaire à celui-ci via le rendu de la route. Il est maintenant temps de définir les différentes routes de notre application. Je vais également omettre les lignes d'importation pour cette section.

### routes.py

Il est important de fournir un rappel de chargeur d'utilisateur lors de l'utilisation de Flask-Login. Cela maintient l'objet utilisateur actuel chargé dans la session actuelle en fonction de l'ID stocké.

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

Dans les lignes de code qui suivent, nous définissons simplement trois routes pour cette application : accueil, connexion et inscription. Remarquez comment nous créons des instances de formulaire Flask puis les transmettons avec l'instruction de retour de la fonction ? Nous modifierons ces routes plus tard pour gérer nos besoins de connexion et d'inscription. Nous ajouterons également une route de déconnexion.

```python
app = create_app()

# Route d'accueil
@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.html",title="Accueil")

# Route de connexion
@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    return render_template("auth.html",form=form)

# Route d'inscription
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()

    return render_template("auth.html",form=form)
 
if __name__ == "__main__":
    app.run(debug=True)

```

Il est temps d'écrire un peu de code HTML. À ce stade, tout ce dont nous avons besoin, ce sont des formulaires dans le navigateur. **NB** : Je vais encore omettre certaines lignes de code pour garder cet article concis. Les fichiers complets sont disponibles sur [GitHub](https://github.com/Dev-Elie/User-Authentication-in-Flask), mais pour l'instant, concentrons-nous sur les principales zones d'intérêt.

**auth.html**

```html
<form action="{{ request.path }}" method="POST" class="...">
    
{{ form.csrf_token }}
    
{% with messages = get_flashed_messages(with_categories=true) %}
<!-- Catégories : success (vert), info (bleu), warning (jaune), danger (rouge) -->
{% if messages %}
{% for category, message in messages %}
<div class="alert alert-{{category}} alert-dismissible fade show" role="alert">
{{ message }}
<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>
{% endfor %}
{% endif %}
{% endwith %}

{% if request.path == '/register/' %}
{{ form.username(class_="form-control",placeholder="Nom d'utilisateur")}}
    
{% for error in form.username.errors %}
{{ error }}
{% endfor%}
    
{% endif%}
    
{{ form.email(class_="form-control",placeholder="Email")}}
    
{% for error in form.email.errors %}
{{ error }}
{% endfor%}
    
{{ form.pwd(class_="form-control",placeholder="Mot de passe")}}

{% for error in form.pwd.errors %}
{{ error }}
{% endfor%}
    
{% if request.path == '/register/' %}
{{ form.cpwd(class_="form-control",placeholder="Confirmer le mot de passe")}}
    
{% for error in form.cpwd.errors %}
{{ error }}
{% endfor%}
    
{% endif%}
    
<button type="submit" class="btn btn-block btn-primary mb-3">
{{ btn_action }}
</button>
    
<p>
{% if request.path != '/register/' %}
Nouveau ici ?
<a href="{{url_for('register')}}">Créer un compte</a>
{% else %}
Vous avez déjà un compte ?
<a href="{{url_for('login')}}">Connexion</a>
{% endif %}
</p>

```

Le modèle HTML montré ci-dessus sert à la fois de formulaire de connexion et d'inscription. Et j'ai simplement utilisé quelques astuces de modélisation Jinja.

Comme vous pouvez le voir ci-dessus, l'action du formulaire est définie sur `action="{{request.path}}"`, où `request.path` récupère le chemin à partir duquel la requête a été émise et l'assigne comme valeur pour l'action du formulaire. Cela élimine le besoin de coder en dur les chemins spécifiques. 

Nous définissons également une variable de jeton csrf qui permet à la validation du formulaire de se poursuivre tout en empêchant les attaques de détournement de session.

Il gère également les messages flashés. Les alertes Bootstrap 5 rendent simple le flashage de différents messages en fonction de leur catégorie. Voici un exemple de ce que cela fait.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/error-msg.png)

Nous imprimons simplement les noms de variables individuels de l'objet de formulaire pour afficher les champs de formulaire. Voici un exemple de l'extrait ci-dessus :

`{{ form.username(class_="form-control",placeholder="Nom d'utilisateur")}}`

Une autre chose à considérer est l'utilisation des instructions `if...else`, comme dans la ligne de code suivante :

`{% if request.path == '/register/' %}`

En masquant certains champs en fonction du chemin de la requête, nous pouvons facilement basculer entre les formulaires de connexion et d'inscription.

Vous vous souvenez des vérifications de validation que nous avons appliquées aux champs de formulaire ? De plus, nous aimerions informer l'utilisateur s'il échoue à fournir l'entrée requise—nous inclurons donc un peu de code pour cela. Un exemple du formulaire HTML ci-dessus est montré ci-dessous. 

Les lignes de code ci-dessous afficheront le message approprié à l'utilisateur si l'une des vérifications contre le nom d'utilisateur est violée.

```html
{% for error in form.username.errors %}
{{ error }}
{% endfor%}
```

Voici un exemple de ce à quoi cela ressemblerait :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/error-msg-2.png)

### Comment modifier routes.py

Dans Flask, l'ajout de nouveaux utilisateurs à la base de données est simple. Pour compléter le tutoriel d'aujourd'hui, nous devons enregistrer, connecter et déconnecter les utilisateurs—c'est-à-dire gérer les sessions.

**a). Route d'inscription**

Tout d'abord, en examinant de plus près l'extrait de code ci-dessous pour l'inscription de nouveaux utilisateurs, nous confirmons que le formulaire envoyant les données a passé toutes les vérifications de validation. Donc, `if form.validate_on_submit():`

```python
    ...
    
    if form.validate_on_submit():
        try:
            email = form.email.data
            pwd = form.pwd.data
            username = form.username.data
            
            newuser = User(
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )
    
            db.session.add(newuser)
            db.session.commit()
            flash(f"Compte créé avec succès", "success")
            return redirect(url_for("login"))

        except Exception as e:
            flash(e, "danger")
            
      ...
```

Si toutes les vérifications passent, nous obtenons les valeurs des champs de formulaire, qui sont ensuite passées à l'objet Utilisateur, ajoutées à la base de données, et toutes les modifications sont enregistrées.

Lorsque la base de données est mise à jour avec succès avec les nouvelles valeurs, l'utilisateur voit un message de succès. Après cela, l'application redirige l'utilisateur vers la page de connexion.

Toute exception qui pourrait survenir est capturée et affichée à l'utilisateur. Cela améliore l'expérience utilisateur en affichant des alertes plus agréables (et vous pouvez également modifier les messages en fonction des exceptions).

Il n'est pas sûr de stocker les mots de passe en texte brut car cela augmente le risque que les informations d'identification de l'utilisateur soient compromises en cas de violation. 

Le mot de passe de l'utilisateur est haché avant d'être enregistré, et ce qui est stocké dans la base de données est une combinaison hautement cryptée de caractères. Nous avons géré cela avec l'aide de Bcrypt. Le hachage est généré comme ceci :

`pwd=bcrypt.generate_password_hash(pwd)`

**b). Route de connexion**

```python
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Nom d'utilisateur ou mot de passe invalide !", "danger")
        except Exception as e:
            flash(e, "danger")
```

Après avoir passé la validation, le modèle Utilisateur est interrogé pour voir si un utilisateur existe avec l'email fourni. Si cela échoue, il affiche un message d'erreur. Mais si cela est validé, la deuxième étape consiste à comparer le mot de passe émis avec la version hachée de celui-ci. Et si les deux correspondent, l'accès est accordé et l'utilisateur est redirigé vers la page d'accueil.

**c). Route de déconnexion**

```python
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
```

La route ci-dessus, qui redirige vers la page de connexion, gère la terminaison des sessions actives.

Et c'est tout ! Nous avons construit notre application avec authentification des utilisateurs.

Merci d'avoir lu. J'espère que vous avez trouvé cet article utile. Continuez à lire, à construire, et meilleurs vœux. N'oubliez pas de me suivre sur Twitter également [**@dev_elie**](https://twitter.com/dev_elie).