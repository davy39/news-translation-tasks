---
title: Comment configurer la vérification par e-mail dans une application Flask
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-01-09T17:56:18.000Z'
originalURL: https://freecodecamp.org/news/setup-email-verification-in-flask-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-maksim-goncharenok-5605061.jpg
tags:
- name: Flask Framework
  slug: flask
- name: Python
  slug: python
seo_title: Comment configurer la vérification par e-mail dans une application Flask
seo_desc: 'Email verification is a crucial aspect of creating a new user account or
  signing up for a service. It helps confirm that the email address provided is valid
  and belongs to the intended user.

  In this article, we will explore the process of handling em...'
---

La vérification par e-mail est un aspect crucial de la création d'un nouveau compte utilisateur ou de l'inscription à un service. Elle permet de confirmer que l'adresse e-mail fournie est valide et appartient à l'utilisateur prévu.

Dans cet article, nous allons explorer le processus de gestion de la vérification par e-mail dans Flask. Le sujet inclura la configuration d'une route pour gérer le processus de vérification par e-mail, et le stockage du statut de vérification dans une base de données. 

À la fin de cet article, vous aurez une compréhension approfondie de la manière d'implémenter la vérification par e-mail dans votre propre application Flask.

Avant de commencer, assurez-vous d'avoir une bonne compréhension de l'authentification de base des utilisateurs dans Flask. Vous pouvez consulter [ce tutoriel](https://ashutoshkrris.hashnode.dev/how-to-set-up-basic-user-authentication-in-a-flask-app) pour en savoir plus.

## **Démonstration du projet**

Voici ce que vous allez construire dans ce tutoriel :

%[https://www.youtube.com/watch?v=7o-wY65gHD8]

Le lien vers le dépôt GitHub est disponible à la fin du tutoriel. N'hésitez pas à le consulter chaque fois que vous êtes bloqué.

## Authentification de base des utilisateurs Flask

Pour commencer, vous allez utiliser un modèle Flask qui inclut l'authentification de base des utilisateurs. Vous pouvez obtenir le code à partir de [ce dépôt](https://github.com/ashutoshkrris/Flask-User-Authentication). Après avoir créé et activé un environnement virtuel, exécutez la commande suivante pour installer toutes les dépendances :

```bash
$ pip install -r requirements.txt
```

Créez un fichier nommé `.env` dans le répertoire racine et ajoutez le contenu suivant :

```
export SECRET_KEY=fdkjshfhjsdfdskfdsfdcbsjdkfdsdf
export DEBUG=True
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=sqlite:///db.sqlite
export FLASK_APP=src
export FLASK_DEBUG=1
```

Exécutez la commande suivante pour exporter toutes les variables d'environnement du fichier `.env` :

```bash
source .env
```

Exécutez les commandes suivantes pour configurer la base de données :

```bash
flask db init
flask db upgrade
```

Exécutez la commande suivante pour exécuter le serveur Flask :

```bash
python manage.py run
```

Une fois l'application en cours d'exécution, allez sur [http://localhost:5000/register](http://localhost:5000/register) pour enregistrer un nouvel utilisateur. Vous remarquerez qu'après avoir terminé l'enregistrement, l'application vous connectera automatiquement et vous redirigera vers la page principale.

Avant de continuer, je vous recommande d'explorer l'application puis de passer en revue le code, en particulier le blueprint **accounts**. Cela vous donnera une meilleure compréhension de la manière dont l'authentification des utilisateurs est implémentée.

## Comment modifier l'implémentation actuelle

Dans cette section, vous allez modifier l'implémentation existante de l'authentification des utilisateurs dans notre application Flask.

### Modèles

Tout d'abord, vous devrez ajouter deux nouveaux champs – `is_confirmed` et `confirmed_on` dans le modèle `User` de votre application.

Ouvrez le fichier `src/accounts/models.py` et mettez à jour la classe `User` avec ce qui suit :

```python
class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    def __init__(
        self, email, password, is_admin=False, is_confirmed=False, confirmed_on=None
    ):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin
        self.is_confirmed = is_confirmed
        self.confirmed_on = confirmed_on

    def __repr__(self):
        return f"<email {self.email}>"
```

Le champ `is_confirmed` est un champ booléen pour indiquer si l'adresse e-mail de l'utilisateur a été confirmée, défini comme non nullable et par défaut à `False`. Le champ `confirmed_on` est un champ `datetime` pour l'heure à laquelle l'e-mail de l'utilisateur a été confirmé, défini comme nullable.

Pour migrer et appliquer ces changements dans la base de données, exécutez les commandes suivantes :

```bash
flask db migrate
flask db upgrade
```

### Comment créer l'administrateur

Ensuite, dans le fichier `manage.py`, mettez à jour la commande `create_admin` pour prendre en compte les nouveaux champs de la base de données :

```python
@cli.command("create_admin")
def create_admin():
    """Crée l'utilisateur administrateur."""
    email = input("Entrez l'adresse e-mail : ")
    password = getpass.getpass("Entrez le mot de passe : ")
    confirm_password = getpass.getpass("Entrez à nouveau le mot de passe : ")
    if password != confirm_password:
        print("Les mots de passe ne correspondent pas")
    else:
        try:
            user = User(
                email=email,
                password=password,
                is_admin=True,
                is_confirmed=True,
                confirmed_on=datetime.now(),
            )
            db.session.add(user)
            db.session.commit()
            print(f"Admin avec l'e-mail {email} créé avec succès !")
        except Exception:
            print("Impossible de créer l'utilisateur administrateur.")
```

Remarquez que le champ `is_confirmed` est défini à `True` dans ce cas car vous ne voulez pas que l'administrateur vérifie son compte.

### Comment ajouter un nouveau décorateur pour vérifier si l'utilisateur est déconnecté

Si vous regardez les fonctions `register()` et `login()` dans `src/accounts/views.py`, vous trouverez le code suivant dans les deux :

```python
if current_user.is_authenticated:
    flash("Vous êtes déjà inscrit.", "info")
    return redirect(url_for("core.home"))
```

Le code vérifie si un utilisateur est déjà connecté. Si l'utilisateur est authentifié, un message est affiché à l'aide de la fonction `flash` et l'utilisateur est redirigé vers la page d'accueil à l'aide de la fonction `redirect` de Flask. 

Si l'utilisateur n'est pas authentifié, il sera autorisé à continuer le processus qu'il tentait de compléter. Cela signifie essentiellement que vous exigez que l'utilisateur soit déconnecté pour continuer le flux.

Au lieu de répéter le code à deux endroits, vous pouvez créer un décorateur pour vérifier si l'utilisateur est déconnecté.

Créez un nouveau dossier `utils` dans le dossier `src`, et un fichier `decorators.py` dans le dossier `utils` avec le contenu suivant :

```python
from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user


def logout_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            flash("Vous êtes déjà authentifié.", "info")
            return redirect(url_for("core.home"))
        return func(*args, **kwargs)

    return decorated_function
```

Le code ci-dessus définit un décorateur appelé `logout_required` qui est utilisé pour envelopper les routes dans une application Flask. 

Si l'utilisateur est authentifié, un message est affiché à l'aide de la fonction `flash` et l'utilisateur est redirigé vers la page d'accueil à l'aide de la fonction `redirect` de Flask. Si l'utilisateur n'est pas authentifié, il sera autorisé à continuer et la fonction de route décorée sera exécutée.

Vous pouvez maintenant utiliser ce décorateur dans les fonctions `register()` et `login()` comme suit :

```python
from src.utils.decorators import logout_required


@accounts_bp.route("/register", methods=["GET", "POST"])
@logout_required
def register():
	...
    
    
@accounts_bp.route("/login", methods=["GET", "POST"])
@logout_required
def login():
	...
```

## Comment ajouter la vérification par e-mail à votre application Flask

Dans cette section, vous allez apprendre comment ajouter la vérification par e-mail à votre application Flask.

### Jeton de confirmation

La confirmation par e-mail doit contenir une URL unique que l'utilisateur peut cliquer pour confirmer son compte. L'URL doit être au format suivant : `http://localhost:5000/confirm/<id>`. 

La partie `<id>` de l'URL est un identifiant unique qui est généré en utilisant l'adresse e-mail de l'utilisateur et un horodatage. Nous pouvons utiliser le package [itsdangerous](http://pythonhosted.org/itsdangerous/) pour encoder ces informations dans l'`<id>`. Lorsque l'utilisateur clique sur le lien, l'application peut décoder l'`<id>` pour récupérer l'adresse e-mail de l'utilisateur et vérifier son compte.

Pour fournir une couche de sécurité supplémentaire au jeton, le package `itsdangerous` nécessite un sel de mot de passe. Vous pouvez définir une variable d'environnement pour cela dans le fichier `.env` :

```
other env vars...
export SECURITY_PASSWORD_SALT=fkslkfsdlkfnsdfnsfd
```

Exécutez la commande suivante pour exporter la variable d'environnement du fichier `.env` :

```bash
source .env
```

Ajoutez le `SECURITY_PASSWORD_SALT` à la configuration de votre application (`Config`) dans le fichier `config.py` :

```python
class Config:
	...other configs
    SECURITY_PASSWORD_SALT = config("SECURITY_PASSWORD_SALT", default="very-important")
```

Créez un fichier `src/accounts/token.py` et ajoutez le code suivant :

```python
from itsdangerous import URLSafeTimedSerializer

from src import app


def generate_token(email):
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    return serializer.dumps(email, salt=app.config["SECURITY_PASSWORD_SALT"])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    try:
        email = serializer.loads(
            token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=expiration
        )
        return email
    except Exception:
        return False

```

Ce code définit deux fonctions pour générer et confirmer des jetons pour la vérification par e-mail dans une application Flask :

La fonction `generate_token` prend une adresse e-mail comme argument et retourne un jeton qui est généré en utilisant la classe `URLSafeTimedSerializer` du package `itsdangerous`. 

La classe `URLSafeTimedSerializer` est initialisée avec la clé secrète de l'application, qui est stockée dans la variable de configuration `SECRET_KEY`. La méthode `dumps` de l'instance `URLSafeTimedSerializer` est appelée avec l'adresse e-mail et un sel de mot de passe comme arguments. Comme mentionné précédemment, le sel de mot de passe est stocké dans la variable de configuration `SECURITY_PASSWORD_SALT`.

La fonction `confirm_token` prend un jeton et un temps d'expiration optionnel comme arguments et retourne l'adresse e-mail qui a été utilisée pour générer le jeton. 

L'instance `URLSafeTimedSerializer` est initialisée avec la clé secrète de l'application, et la méthode `loads` est appelée avec le jeton, le sel de mot de passe et le temps d'expiration comme arguments. 

Si le jeton est valide et n'a pas expiré, l'adresse e-mail est retournée. Si le jeton est invalide ou a expiré, une exception est levée et attrapée par le bloc `except`, ce qui fait que la fonction retourne `False`.

### Comment mettre à jour la fonction `register()`

Lorsque l'utilisateur s'inscrit, vous devez générer un jeton en utilisant l'adresse e-mail de l'utilisateur.

```python
from src.accounts.token import confirm_token, generate_token


@accounts_bp.route("/register", methods=["GET", "POST"])
@logout_required
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        token = generate_token(user.email)
        
        ...
```

La variable `token` sera utilisée lors de l'envoi d'un e-mail à l'utilisateur avec le jeton inclus dans l'URL de l'e-mail.

### Comment gérer la confirmation par e-mail

Pour confirmer l'e-mail, créez une nouvelle fonction de vue dans le fichier `src/accounts/views.py` :

```python
@accounts_bp.route("/confirm/<token>")
@login_required
def confirm_email(token):
    if current_user.is_confirmed:
        flash("Compte déjà confirmé.", "success")
        return redirect(url_for("core.home"))
    email = confirm_token(token)
    user = User.query.filter_by(email=current_user.email).first_or_404()
    if user.email == email:
        user.is_confirmed = True
        user.confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash("Vous avez confirmé votre compte. Merci !", "success")
    else:
        flash("Le lien de confirmation est invalide ou a expiré.", "danger")
    return redirect(url_for("core.home"))
```

Le code ci-dessus définit une route pour la fonction de vue `confirm_email` dans une application Flask. La route est décorée avec le décorateur `@login_required`, qui nécessite que l'utilisateur soit connecté pour accéder à la vue. La route prend un argument `token`, qui est inclus dans l'URL de la route.

La fonction de vue vérifie d'abord si le compte de l'utilisateur est déjà confirmé. Si le compte est déjà confirmé, un message est affiché à l'aide de la fonction `flash` de la bibliothèque Flask-Babel et l'utilisateur est redirigé vers la page d'accueil à l'aide de la fonction `redirect` de Flask.

Si le compte n'est pas confirmé, la fonction `confirm_token` est appelée avec le `token` comme argument pour confirmer le jeton et récupérer l'adresse e-mail qui a été utilisée pour générer le jeton. Si le jeton est invalide ou a expiré, la fonction `confirm_token` retourne `False`, et un message est affiché indiquant que le lien de confirmation est invalide ou a expiré.

Si le jeton est valide, le compte de l'utilisateur est confirmé en définissant le champ `is_confirmed` à `True` et le champ `confirmed_on` à l'heure actuelle. Les modifications sont ensuite validées dans la base de données. Un message est affiché indiquant que le compte a été confirmé, et l'utilisateur est redirigé vers la page d'accueil.

### Comment envoyer la confirmation par e-mail

Créons d'abord un modèle d'e-mail de base qui sera utilisé lors de l'envoi de l'e-mail. Créez un fichier `templates/accounts/confirm_email.html` et ajoutez le code suivant :

```html
<p>
  Bienvenue ! Merci de vous être inscrit. Veuillez suivre ce lien pour activer votre
  compte :
</p>
<p><a href="{{ confirm_url }}">{{ confirm_url }}</a></p>
<br />
<p>Cordialement !</p>

```

Le placeholder `confirm_url` est utilisé pour insérer une URL dans le message e-mail. Lorsque le modèle est rendu, le placeholder `confirm_url` est remplacé par l'URL réelle que l'utilisateur doit visiter pour confirmer son compte.

#### Comment configurer Flask-Mail

Ensuite, vous aurez besoin d'une bibliothèque appelée `Flask-Mail` pour envoyer des e-mails en utilisant Flask.

Installez la bibliothèque en utilisant la commande pip :

```bash
pip install Flask-Mail
```

Initialisez la bibliothèque `Flask-Mail` dans le fichier `src/__init__.py` comme suit :

```python
...other imports...
from flask_mail import Mail

...other initializations...
mail = Mail(app)
...
```

Vous pouvez définir des variables d'environnement pour votre e-mail et votre mot de passe qui seront utilisés pour envoyer des e-mails dans le fichier `.env` :

```
export EMAIL_USER=votre-email
export EMAIL_PASSWORD=votre-mot-de-passe
```

Exécutez la commande suivante pour exporter les variables d'environnement du fichier `.env` :

```bash
source .env
```

Mettez à jour la classe `Config` dans le fichier `config.py` :

```python
class Config(object):
    ...other configs

    # Paramètres de messagerie
    MAIL_DEFAULT_SENDER = "noreply@flask.com"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = False
    MAIL_USERNAME = config("EMAIL_USER")
    MAIL_PASSWORD = config("EMAIL_PASSWORD")
```

> Note : Si votre compte Gmail a une [authentification à deux étapes](https://support.google.com/accounts/topic/28786?hl=en&ref_topic=3382253), Google bloquera la tentative. Utilisez un [mot de passe d'application](https://support.google.com/accounts/answer/185833?hl=en) pour vous connecter.

#### Comment créer une fonction pour envoyer un e-mail

Ensuite, créez un fichier `email.py` dans le dossier `src/utils` et ajoutez le code suivant :

```python
from flask_mail import Message

from src import app, mail


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config["MAIL_DEFAULT_SENDER"],
    )
    mail.send(msg)

```

La fonction prend trois arguments : l'adresse e-mail du destinataire (`to`), le sujet de l'e-mail (`subject`), et le corps de l'e-mail (`template`). 

La classe `Message` de la bibliothèque Flask-Mail est utilisée pour créer un nouveau message e-mail avec le sujet et le destinataire spécifiés. L'argument `html` est utilisé pour définir le corps de l'e-mail au `template` fourni, qui est censé être une chaîne HTML. L'argument `sender` est utilisé pour spécifier l'expéditeur par défaut de l'e-mail, qui est stocké dans la variable de configuration `MAIL_DEFAULT_SENDER`.

La méthode `send` de l'objet `mail` est ensuite appelée avec l'objet message comme argument pour envoyer l'e-mail. 

#### Comment envoyer l'e-mail (enfin)

Envoyons enfin l'e-mail de confirmation depuis la fonction `register()` :

```python
from src.utils.email import send_email


@accounts_bp.route("/register", methods=["GET", "POST"])
@logout_required
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = generate_token(user.email)
        confirm_url = url_for("accounts.confirm_email", token=token, _external=True)
        html = render_template("accounts/confirm_email.html", confirm_url=confirm_url)
        subject = "Veuillez confirmer votre e-mail"
        send_email(user.email, subject, html)

        login_user(user)

        flash("Un e-mail de confirmation a été envoyé par e-mail.", "success")
        return redirect(url_for("accounts.inactive"))

    return render_template("accounts/register.html", form=form)
```

La fonction `url_for` est ensuite appelée pour générer une URL pour la route `confirm_email` avec le `token` comme argument. L'argument `_external` est défini à `True` pour générer une URL absolue avec le nom de domaine complet. La fonction `render_template` est appelée pour rendre un modèle HTML pour le message e-mail, en utilisant le `confirm_url` comme placeholder dans le modèle.

La fonction `send_email` est ensuite appelée pour envoyer l'e-mail avec le modèle rendu comme corps, en utilisant l'adresse e-mail de l'utilisateur comme destinataire et un sujet de "Veuillez confirmer votre e-mail".

Enfin, l'utilisateur est connecté en utilisant la fonction `login_user` de la bibliothèque Flask-Login et un message est affiché indiquant qu'un e-mail de confirmation a été envoyé. L'utilisateur est ensuite redirigé vers la vue `inactive`. Vous la créerez plus tard.

Un exemple d'e-mail ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-05-234354.png)

## Comment gérer les comptes inactifs

Chaque fois que vous créez un nouveau compte, vous êtes redirigé vers une vue appelée `inactive` où l'on vous demande de confirmer votre compte.

Créons une fonction de vue dans le fichier `src/accounts/views.py` :

```python
@accounts_bp.route("/inactive")
@login_required
def inactive():
    if current_user.is_confirmed:
        return redirect(url_for("core.home"))
    return render_template("accounts/inactive.html")
```

La fonction de vue vérifie si le compte de l'utilisateur est confirmé. Si le compte est confirmé, l'utilisateur est redirigé vers la page d'accueil en utilisant la fonction `redirect` de Flask. Si le compte n'est pas confirmé, le modèle `inactive.html` est rendu en utilisant la fonction `render_template` de Flask.

Créons le fichier `inactive.html` dans le dossier `templates/accounts` :

```html
{% extends "_base.html" %} {% block content %}

<div class="text-center">
  <h1>Bienvenue !</h1>
  <br />
  <p>
    Vous n'avez pas confirmé votre compte. Veuillez vérifier votre boîte de réception (et votre dossier de spam)
    - vous devriez avoir reçu un e-mail avec un lien de confirmation.
  </p>
  <p>
    Vous n'avez pas reçu l'e-mail ?
    <a href="{{ url_for('accounts.resend_confirmation') }}">Renvoyer</a>.
  </p>
</div>

{% endblock %}

```

Le modèle inclut un lien vers la route `resend_confirmation`.

### Comment renvoyer l'e-mail

Considérez un cas où l'utilisateur n'a pas pu confirmer le compte avant l'expiration du jeton. En tant qu'utilisateur, vous voudrez avoir une option pour renvoyer l'e-mail, n'est-ce pas ?

Créez une nouvelle fonction de vue dans `src/accounts/views.py` :

```python
@accounts_bp.route("/resend")
@login_required
def resend_confirmation():
    if current_user.is_confirmed:
        flash("Votre compte a déjà été confirmé.", "success")
        return redirect(url_for("core.home"))
    token = generate_token(current_user.email)
    confirm_url = url_for("accounts.confirm_email", token=token, _external=True)
    html = render_template("accounts/confirm_email.html", confirm_url=confirm_url)
    subject = "Veuillez confirmer votre e-mail"
    send_email(current_user.email, subject, html)
    flash("Un nouvel e-mail de confirmation a été envoyé.", "success")
    return redirect(url_for("accounts.inactive"))
```

Ce code définit une route pour la fonction de vue `resend_confirmation` dans une application Flask. La route est décorée avec le décorateur `login_required`, qui nécessite que l'utilisateur soit connecté pour accéder à la vue.

La fonction de vue vérifie d'abord si le compte de l'utilisateur est déjà confirmé. Si le compte est confirmé, un message est affiché indiquant que le compte a déjà été confirmé et l'utilisateur est redirigé vers la page d'accueil.

Si le compte n'est pas confirmé, un jeton est généré comme précédemment. La fonction `url_for` est ensuite appelée pour générer une URL pour la route `confirm_email` avec le `token` comme argument. La fonction `send_email` est ensuite appelée pour envoyer l'e-mail avec le modèle rendu comme corps, en utilisant l'adresse e-mail de l'utilisateur comme destinataire et un sujet de "Veuillez confirmer votre e-mail". Un message est affiché indiquant qu'un nouvel e-mail de confirmation a été envoyé, et l'utilisateur est redirigé vers la vue `inactive`.

### Comment ajouter un middleware pour les routes

Maintenant que vous avez le mécanisme de vérification par e-mail prêt, vous voulez que vos routes dans le package `core` soient accessibles uniquement par les utilisateurs avec un compte confirmé. Pour ce faire, vous pouvez ajouter un décorateur sur ces routes.

Créez un nouveau décorateur dans le fichier `src/utils/decorators.py` :

```python
def check_is_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_confirmed is False:
            flash("Veuillez confirmer votre compte !", "warning")
            return redirect(url_for("accounts.inactive"))
        return func(*args, **kwargs)

    return decorated_function
```

Ce code définit un décorateur appelé `check_is_confirmed`. Le décorateur prend une fonction comme argument et retourne une fonction décorée.

Le décorateur fonctionne en vérifiant si le compte de l'utilisateur est confirmé. Si le compte n'est pas confirmé, un message est affiché avertissant l'utilisateur de confirmer son compte, et l'utilisateur est redirigé vers la vue `inactive`. Si le compte est confirmé, la fonction décorée est appelée comme d'habitude.

Vous pouvez maintenant utiliser ce décorateur dans la fonction de vue `home` dans le fichier `src/core/views.py` :

```python
from src.utils.decorators import check_is_confirmed


@core_bp.route("/")
@login_required
@check_is_confirmed
def home():
    return render_template("core/index.html")
```

Voici à quoi cela ressemble lorsque vous vous connectez et que votre compte n'est pas vérifié :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-05-234723.png)

## Comment ajouter de nouveaux cas de test

Maintenant que vous avez ajouté la fonctionnalité principale, il est temps de mettre à jour la suite de tests.

### Comment modifier la méthode `setUp()` dans `base_test.py`

Remplacez la méthode `setUp()` par le code suivant :

```python
def setUp(self):
    db.create_all()
    unconfirmed_user = User(email="unconfirmeduser@gmail.com",
                                password="unconfirmeduser")
    db.session.add(unconfirmed_user)
    confirmed_user = User(email="confirmeduser@gmail.com",
                              password="confirmeduser", is_confirmed=True)
    db.session.add(confirmed_user)
    db.session.commit()
```

La méthode crée maintenant deux utilisateurs – un utilisateur avec un compte confirmé et un autre utilisateur sans compte confirmé.

Notez que vous devrez remplacer l'utilisation de l'ancienne adresse e-mail et du mot de passe par l'adresse e-mail et le mot de passe de l'utilisateur non confirmé dans tous les fichiers de test.

### Comment ajouter de nouveaux cas de test dans `test_routes.py`

Puisque les utilisateurs non authentifiés ne peuvent pas accéder à la page d'accueil, ajoutons un cas de test dans la classe `TestLoggingInOut` pour voir si l'utilisateur est redirigé vers la page de connexion :

```python
def test_home_route_requires_login(self):
    self.client.get("/logout", follow_redirects=True)
    self.client.get('/', follow_redirects=True)
    self.assertTemplateUsed('accounts/login.html')
```

Créez une nouvelle classe `TestEmailConfirmationToken` dans le même fichier :

```python
class TestEmailConfirmationToken(BaseTestCase):
    def test_confirm_token_route_requires_login(self):
        # Assurez-vous que la route confirm/<token> nécessite un utilisateur connecté.
        self.client.get("/logout", follow_redirects=True)
        self.client.get('/confirm/some-unique-id', follow_redirects=True)
        self.assertTemplateUsed('accounts/login.html')

    def test_confirm_token_route_valid_token(self):
        # Assurez-vous que l'utilisateur peut confirmer le compte avec un jeton valide.
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post('/login', data=dict(
                email='unconfirmeduser@gmail.com', password='unconfirmeduser'
            ), follow_redirects=True)
            token = generate_token('unconfirmeduser@gmail.com')
            response = self.client.get(
                '/confirm/'+token, follow_redirects=True)
            self.assertIn(
                b'You have confirmed your account. Thanks!', response.data)
            self.assertTemplateUsed('core/index.html')
            user = User.query.filter_by(
                email='unconfirmeduser@gmail.com').first_or_404()
            self.assertIsInstance(user.confirmed_on, datetime)
            self.assertTrue(user.is_confirmed)

    def test_confirm_token_route_invalid_token(self):
        # Assurez-vous que l'utilisateur ne peut pas confirmer le compte avec un jeton invalide.
        token = generate_token('test@test1.com')
        with self.client:
            self.client.get("/logout", follow_redirects=True)
            self.client.post('/login', data=dict(
                email='unconfirmeduser@gmail.com', password='unconfirmeduser'
            ), follow_redirects=True)
            response = self.client.get('/confirm/'+token,
                                       follow_redirects=True)
            self.assertIn(
                b'The confirmation link is invalid or has expired.',
                response.data
            )

    def test_confirm_token_route_expired_token(self):
        # Assurez-vous que l'utilisateur ne peut pas confirmer le compte avec un jeton expiré.
        user = User(email='test@test1.com', password='test1')
        db.session.add(user)
        db.session.commit()
        token = generate_token('test@test1.com')
        self.assertFalse(confirm_token(token, -1))
```

Le code ci-dessus teste la fonctionnalité de vérification par e-mail de l'application.

* Le cas de test `test_confirm_token_route_requires_login` teste que lorsqu'un utilisateur essaie d'accéder à la route de confirmation lorsqu'il n'est pas connecté, il est redirigé vers la page de connexion.
* Le cas de test `test_confirm_token_route_valid_token` teste que lorsqu'un utilisateur essaie d'accéder à la route de confirmation avec un jeton valide, son compte est confirmé et il est redirigé vers la page d'index.
* Le cas de test `test_confirm_token_route_invalid_token` teste que lorsqu'un utilisateur essaie d'accéder à la route de confirmation avec un jeton invalide, un message d'erreur est affiché.
* Le cas de test `test_confirm_token_route_expired_token` teste que lorsqu'un utilisateur essaie d'accéder à la route de confirmation avec un jeton expiré, un message d'erreur est affiché.

## **Conclusion**

Dans ce tutoriel, vous avez appris comment gérer la vérification par e-mail dans votre application Flask. Vous avez également écrit quelques cas de test supplémentaires afin de tester les nouvelles fonctionnalités.

Voici le lien vers le [dépôt GitHub](https://github.com/ashutoshkrris/Flask-User-Authentication-With-Email-Verification). N'hésitez pas à le consulter chaque fois que vous êtes bloqué.

### **Étapes suivantes recommandées**

* Vous pouvez ajouter une fonctionnalité "mot de passe oublié" dans l'application.
* Vous pouvez permettre aux utilisateurs de gérer leurs profils.
* Vous pouvez ajouter plus de cas de test afin de tester plus minutieusement l'application.

Merci d'avoir lu. J'espère que vous avez trouvé cet article utile. Vous pouvez me suivre sur [Twitter](https://twitter.com/ashutoshkrris).