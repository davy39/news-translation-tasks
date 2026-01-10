---
title: Créer un clone de Heroku – Approvisionner l'infrastructure de manière programmatique
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-06-02T14:08:55.000Z'
originalURL: https://freecodecamp.org/news/build-a-heroku-clone-provision-infrastructure-programmatically
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/heroku-1.png
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: youtube
  slug: youtube
seo_title: Créer un clone de Heroku – Approvisionner l'infrastructure de manière programmatique
seo_desc: "Heroku is a platform as a service that enables developers to build, run,\
  \ and operate applications entirely in the cloud.\nHeroku makes it simple to do\
  \ things like create virtual machines to host applications and to deploy websites.\
  \  \nSome of the featu..."
---

Heroku est une plateforme en tant que service qui permet aux développeurs de créer, exécuter et gérer des applications entièrement dans le cloud.

Heroku simplifie des tâches comme la création de machines virtuelles pour héberger des applications et le déploiement de sites web.  
  
Certaines des fonctionnalités offertes par Heroku peuvent en réalité être créées facilement avec d'autres outils. 

Dans cet article, vous apprendrez à créer une application web très simple qui permet aux utilisateurs d'approvisionner des machines virtuelles et de déployer des sites web statiques en un clic, le tout hébergé sur Amazon Web Services.

Vous apprendrez à approvisionner l'infrastructure avec du code, puis vous pourrez appliquer ce que vous avez appris à vos propres applications.

Cet article est un complément au cours complet que nous venons de publier sur la chaîne YouTube freeCodeCamp.org, qui vous apprendra à approvisionner l'infrastructure de manière programmatique en utilisant Python.

Vous pouvez regarder le cours ci-dessous ou sur la chaîne YouTube freeCodeCamp.org (1,5 heure de visionnage).

%[https://youtu.be/zhJLVFR3pE8]

L'approvisionnement de l'infrastructure est lié à l'ingénierie de plateforme. Une équipe d'ingénierie de plateforme sert une organisation en planifiant, concevant et gérant ses plateformes cloud. Et souvent, cela peut être fait de manière programmatique.

Les outils que j'enseigne dans ce cours peuvent être utilisés pour bien plus que simplement l'approvisionnement de VM et le déploiement de sites web. Ils peuvent être utilisés pour l'ingénierie de plateforme afin de simplifier la gestion des plateformes cloud.

### API d'automatisation

Ce cours se concentre sur l'API d'automatisation de Pulumi. Pulumi a fourni à freeCodeCamp une subvention qui a rendu ce cours possible. 

Le SDK open source d'infrastructure en tant que code de Pulumi vous permet de créer, déployer et gérer l'infrastructure sur n'importe quel cloud, en utilisant de nombreux langages de programmation différents.

Leur API d'automatisation permet d'approvisionner l'infrastructure de manière programmatique en utilisant le moteur Pulumi. Basiquement, cela simplifie l'écriture d'un programme qui crée automatiquement des VM, des bases de données, des VPC, des sites web statiques et plus encore sur une variété de plateformes cloud différentes.

Je vais vous montrer comment créer notre application web clone de Heroku en utilisant Flask et Python en backend. Cependant, vous n'avez pas besoin de savoir déjà utiliser Flask et Python pour suivre. De plus, tout ce que je vous montre pourrait également être fait avec de nombreux autres frameworks et langages de programmation différents, et beaucoup des étapes sont les mêmes peu importe le framework web que vous utilisez.

Notre application approvisionnera des ressources sur AWS, mais Pulumi simplifie l'approvisionnement de ressources sur la plupart des principaux fournisseurs de cloud, et il ne faudrait pas beaucoup de mises à jour du code pour utiliser un autre fournisseur.

Merci à Komal Ali qui a créé le code sur lequel mon code dans ce cours est basé.

## Créer le clone de Heroku

### CLI de Pulumi

Tout d'abord, assurez-vous d'avoir installé la CLI de Pulumi. La méthode d'installation diffère selon votre système d'exploitation.

Si vous avez MacOS et [Homebrew](https://brew.sh/), vous pouvez utiliser la commande `brew install pulumi`.

Si vous avez Windows et [Chocolatey](https://chocolatey.org/), vous pouvez utiliser la commande `choco install pulumi`.

[Cette page vous donnera des méthodes supplémentaires pour installer Pulumi](https://www.pulumi.com/docs/get-started/install/).

### CLI AWS

Ce projet utilise également AWS, vous devrez donc vous assurer d'avoir un compte AWS et d'avoir configuré et authentifié la CLI.

Vous pouvez vous inscrire pour un compte AWS gratuit ici : [https://aws.amazon.com/free/](https://aws.amazon.com/free/)

Apprenez à installer la CLI AWS pour votre système d'exploitation ici : [https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

Pour MacOS, vous pouvez utiliser ces commandes :

```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

Pour Windows, il y a quelques étapes supplémentaires et vous devriez simplement [suivre les instructions ici](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html).

Ensuite, vous devez obtenir un ID de clé d'accès et une clé d'accès secrète auprès d'AWS. [Suivez les instructions d'Amazon pour obtenir celles-ci](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds).

Maintenant, exécutez ce qui suit dans la ligne de commande :

`aws configure`

Entrez votre ID de clé d'accès et votre clé d'accès secrète lorsque vous y êtes invité. Vous pouvez garder le "Nom de la région par défaut" et le "Format de sortie par défaut" comme None.

###   
Configurer le projet

Un projet Pulumi est simplement un répertoire avec quelques fichiers dedans. Il est possible pour vous de créer un nouveau projet à la main. La commande `pulumi new`, cependant, automatise le processus :

`pulumi new`

Si c'est la première fois que vous utilisez Pulumi, vous serez dirigé pour entrer un code d'accès ou vous connecter. Pour obtenir un code d'accès, allez sur [https://app.pulumi.com/account/tokens](https://app.pulumi.com/account/tokens)

La commande `pulumi new` vous permet de choisir parmi de nombreux modèles. Choisissez le modèle "aws-python". Vous pouvez sélectionner les valeurs par défaut pour les autres options.

Cette commande a créé tous les fichiers dont nous avons besoin, initialisé une nouvelle pile nommée `dev` (une instance de notre projet). 

Chaque programme Pulumi est déployé sur un _stack_. Un stack est une instance isolée et configurable indépendamment d'un programme Pulumi. Les stacks sont couramment utilisés pour désigner différentes phases de développement. Dans ce cas, nous l'avons appelé 'dev'.

Maintenant, nous devons installer deux dépendances supplémentaires pour notre projet avec

`venv/bin/pip install flask requests`

### Créer l'application Flask

Nous pouvons maintenant commencer à créer les fichiers pour notre application web Flask.

Pulumi a créé un fichier appelé "__main__.py". Changez le nom de ce fichier en "app.py" car il s'agit d'une application Flask et Flask recherchera un fichier avec ce nom.

Il y a du code dans ce fichier et nous utiliserons éventuellement un code similaire, mais pour l'instant, testons simplement que Flask fonctionne en remplaçant le code dans "app.py" par ce qui suit :

```python
from flask import Flask
  
app = Flask(__name__)
  
@app.route('/')
def hello_world():
    return 'Hello World'
  
if __name__ == '__main__':
  
    app.run()
```

Il s'agit de l'application web Flask la plus basique et nous pouvons la tester en exécutant la commande suivante dans le terminal :

`env/bin/flask run`

Ensuite, nous pouvons accéder à l'application en cours d'exécution dans le navigateur web à l'URL "[http://127.0.0.1:5000/](http://127.0.0.1:5000/)".

Si vous allez à cette URL, elle devrait dire "Hello World". Si c'est le cas, Flask fonctionne correctement, donc nous pouvons mettre à jour le fichier "app.py" avec ce qui suit :

```python
import os
from flask import Flask, render_template

import pulumi.automation as auto


def ensure_plugins():
    ws = auto.LocalWorkspace()
    ws.install_plugin("aws", "v4.0.0")


def create_app():
    ensure_plugins()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="secret",
        PROJECT_NAME="herocool",
        PULUMI_ORG=os.environ.get("PULUMI_ORG"),
    )

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    from . import sites

    app.register_blueprint(sites.bp)

    from . import virtual_machines

    app.register_blueprint(virtual_machines.bp)

    return app

```

Nous importons le framework d'automatisation de Pulumi sous le nom de variable `auto`. Ensuite, dans la fonction `ensure_plugins`, nous obtenons l'accès à `LocalWorkspace`. Un `Workspace` est le contexte d'exécution contenant un seul projet Pulumi. Les Workspaces sont utilisés pour gérer l'environnement d'exécution, fournissant diverses utilités telles que l'installation de plugins, la configuration de l'environnement, et la création, la suppression et la liste des stacks.

Parce que nous déployons des ressources AWS dans ce tutoriel, nous devons installer le plugin du fournisseur AWS dans le `Workspace` afin que le programme Pulumi puisse l'utiliser pendant l'exécution.

La fonction `create_app` est ce que Flask exécutera lorsque nous démarrerons l'application Flask. Nous exécutons d'abord la fonction `ensure_plugins`, puis créons l'application Flask. La fonction `app.config.from_mapping()` est utilisée par Flask pour définir certaines configurations par défaut que l'application utilisera. Cela ne sera pas une application prête pour la production, mais si vous déployez un jour une application Flask, assurez-vous de changer la clé secrète. Les autres variables sont utilisées par Pulumi.

Le reste du fichier est commun aux applications Flask. Nous définissons la route par défaut (`@app.route("/", methods=["GET"])`) pour rendre le modèle "index.html" (que nous devons encore créer.

Enfin, le fichier importe les fichiers sites et virtual_machines et les enregistre en tant que blueprint.

Un Blueprint dans Flask est un moyen d'organiser un groupe de vues et d'autres codes associés. Plutôt que d'enregistrer des vues et d'autres codes directement avec une application, ils sont enregistrés avec un blueprint. Ensuite, le blueprint est enregistré avec l'application lorsqu'il est disponible dans la fonction de fabrication.

En gros, nous utilisons des Blueprints pour pouvoir définir des routes supplémentaires pour notre application web dans d'autres fichiers que nous devons encore créer.

### Créer des modèles

Et en parlant de créer d'autres fichiers, créons-en quelques-uns. Créez un répertoire appelé "templates", puis créez un fichier à l'intérieur de ce répertoire nommé "index.html".

Ajoutez le code suivant :

```html
{% extends "base.html" %}

{% block content %}
  <div class="row row-cols-1 row-cols-md-2 g-4">
    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Sites Web Statiques</h5>
          <p class="card-text">Déployez votre propre site web statique en quelques secondes !</p>
          <a href="{{ url_for("sites.list_sites") }}" class="btn btn-primary">Commencer</a>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Machines Virtuelles</h5>
          <p class="card-text">Configurez une machine virtuelle pour le développement et les tests.</p>
          <a href="{{ url_for("virtual_machines.list_vms") }}" class="btn btn-primary">Commencer</a>
        </div>
      </div>
    </div>
  </div>
{% endblock %}
```

Je ne vais pas entrer dans trop de détails sur ce code. C'est du HTML basique, mais tout ce qui est entre accolades est une expression qui sera sortie dans le document final. Flask utilise la bibliothèque de modèles Jinja pour rendre les modèles. Vous remarquerez qu'elle rend dynamiquement une liste de sites et de machines virtuelles. Bientôt, nous créerons le code Python qui obtiendra ces listes en utilisant Pulumi. 

Mais ensuite, créez un fichier appelé "base.html". Vous remarquerez que "index.html" étend "base.html". Cela sera essentiellement l'en-tête que toutes nos pages partagent.

Ajoutez ce code :

```html
<!DOCTYPE html>
<head>
  <title>Herocool - {% block title %}{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for("static", filename="bootstrap.min.css") }}">
  <script src="{{ url_for("static", filename="bootstrap.min.js") }}"></script>
</head>
<body>
  <div class="container p-2">
    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <a href="{{ url_for("index") }}" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
        <span class="fs-3">Herocool</span>
      </a>
      {% block nav %}{% endblock %}
    </header>
  </div>
  <section class="container-md px-4">
    <div>
      <header class="row gy-4">
        <span class="fs-4">{% block header %}{% endblock %}</span>
        {% for category, message in get_flashed_messages(with_categories=true) %}
        <div class="alert alert-{{ category }}" role="alert">{{ message }}</div>
        {% endfor %}
      </header>
    </div>
    {% block content %}{% endblock %}
  </section>
</body>

```

Maintenant, nous allons rapidement créer le reste de nos modèles HTML, puis créer les fichiers Python qui font le vrai travail dans notre application.

À l'intérieur de notre répertoire "templates", créez deux autres répertoires appelés "sites" et "virtual_machines". À l'intérieur de chacun de ces répertoires, créez les trois mêmes fichiers : "index.html", "create.html", et "update.html".

Voici le code à ajouter à chacun :

**sites/index.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("sites.create_site") }}" class="nav-link active">Créer un site statique</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Répertoire des sites{% endblock %}
{% endblock %}

{% block content %}
  <table class="table">
    <tbody>
      {% if not sites %}
      <div class="container gy-5">
        <div class="row py-4">
          <div class="alert alert-secondary" role="alert">
            <p>Aucun site web n'est actuellement déployé. Créez-en un pour commencer !</p>
            <a href="{{ url_for("sites.create_site") }}" class="btn btn-primary">Créer un site statique</a>
          </div>
        </div>
      </div>
      {%  endif %}
      {% for site in sites %}
        <tr>
          <td class="align-bottom" colspan="4">
            <div class="p-1">
              <a href="{{ site["url"] }}" class="fs-5 align-bottom" target="_blank">{{ site["name"] }}</a>
            </div>
          </td>
          <td>
            <div class="float-end p-1">
              <form action="{{ url_for("sites.delete_site", id=site["name"]) }}" method="post">
                <input class="btn btn-sm btn-danger" type="submit" value="Supprimer">
              </form>
            </div>
            <div class="float-end p-1">
              <form action="{{ url_for("sites.update_site", id=site["name"]) }}" method="get">
                <input class="btn btn-sm btn-primary" type="submit" value="Modifier">
              </form>
            </div>
            <div class="float-end p-1">
              <a href="{{ site["console_url"] }}" class="btn btn-sm btn-outline-primary" target="_blank">Voir dans la console</a>
            </div>
          </td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}

```

**sites/create.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("sites.list_sites") }}" class="nav-link">Retour au répertoire des sites</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Créer un nouveau site statique{% endblock %}
{% endblock %}

{% block content %}
<section class="p-2">
  <form method="post">
    <div class="mb-3">
      <label for="site-id" class="form-label">Nom</label>
      <input type="text" class="form-control" name="site-id" id="site-id" aria-describedby="nameHelp" required>
      <div id="nameHelp" class="form-text">Choisissez un nom unique comme étiquette pour votre site web</div>
    </div>
    <div class="mb-3">
      <label for="file-url" class="form-label">URL du fichier</label>
      <input type="text" class="form-control" id="file-url" name="file-url">
    </div>
    <div class="mb-3">
      <strong>OU</strong>
    </div>
    <div class="mb-3">
      <label for="site-content" class="form-label">Contenu</label>
      <textarea class="form-control" name="site-content" id="site-content" rows="5"></textarea>
    </div>
    <button type="submit" class="btn btn-primary">Créer</button>
  </form>
</section>
{% endblock %}

```

**sites/update.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("sites.list_sites") }}" class="nav-link">Retour au répertoire des sites</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Mettre à jour le site '{{ name }}'{% endblock %}
{% endblock %}

{% block content %}
  <section class="p-2">
    <form method="post">
      <div class="mb-3">
        <label for="file-url" class="form-label">URL du fichier</label>
        <input type="text" class="form-control" name="file-url" id="file-url">
      </div>
      <div class="mb-3">
        <strong>OU</strong>
      </div>
      <div class="mb-3">
        <label for="site-content" class="form-label">Contenu</label>
        <textarea class="form-control" name="site-content" id="site-content" rows="5">{{ content }}</textarea>
      </div>
      <button type="submit" class="btn btn-primary">Mettre à jour</button>
    </form>
  </section>
{% endblock %}

```

**virtual_machines/index.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("virtual_machines.create_vm") }}" class="nav-link active">Créer une VM</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Machines Virtuelles Déployées{% endblock %}
{% endblock %}

{% block content %}
  <table class="table">
    <tbody>
      {% if not vms %}
      <div class="container gy-5">
        <div class="row py-4">
          <div class="alert alert-secondary" role="alert">
            <p>Aucune machine virtuelle n'est actuellement déployée. Créez-en une pour commencer !</p>
            <a href="{{ url_for("virtual_machines.create_vm") }}" class="btn btn-primary">Créer une VM</a>
          </div>
        </div>
      </div>
      {%  endif %}
      {% for vm in vms %}
      <tr>
        <td class="align-bottom" colspan="4">
          <div class="p-1">
            <pre> ssh -i ~/.ssh/id_rsa.pem ec2-user@{{ vm["dns_name"] }} </pre>
          </div>
        </td>
        <td>
          <div class="float-end p-1">
            <form action="{{ url_for("virtual_machines.delete_vm", id=vm["name"]) }}" method="post">
              <input class="btn btn-sm btn-danger" type="submit" value="Supprimer">
            </form>
          </div>
          <div class="float-end p-1">
            <form action="{{ url_for("virtual_machines.update_vm", id=vm["name"]) }}" method="get">
              <input class="btn btn-sm btn-primary" type="submit" value="Modifier">
            </form>
          </div>
          <div class="float-end p-1">
            <a href="{{ vm["console_url"] }}" class="btn btn-sm btn-outline-primary" target="_blank">Voir dans la console</a>
          </div>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}

```

**virtual_machines/create.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("virtual_machines.list_vms") }}" class="nav-link">Retour au répertoire des machines virtuelles</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Créer une nouvelle machine virtuelle{% endblock %}
{% endblock %}

{% block content %}
<section class="p-2">
  <form method="post">
    <div class="mb-3">
      <label for="vm-id" class="form-label">Nom</label>
      <input type="text" class="form-control" name="vm-id" id="vm-id" aria-describedby="nameHelp" required>
      <div id="nameHelp" class="form-text">Choisissez un nom unique comme étiquette pour votre machine virtuelle</div>
    </div>
    <div class="mb-3">
      <label for="vm-id" class="form-label">Type d'instance</label>
      <select name="instance_type" class="form-control" id="instance_type">
      {% for instance_type in instance_types %}
        <option value="{{ instance_type }}" {% if instance_type == curr_instance_type %} selected {% endif %}>
          {{ instance_type }}
        </option>
      {% endfor %}
      </select>
    </div>
    <div class="mb-3">
      <label for="vm-keypair" class="form-label">Clé publique</label>
      <textarea class="form-control" name="vm-keypair" id="vm-keypair-content" rows="5" aria-describedby="keypairHelp"></textarea>
      <div id="keypairHelp" class="form-text">La clé publique à utiliser pour se connecter à la VM</div>
    </div>
    <button type="submit" class="btn btn-primary">Créer</button>
  </form>
</section>
{% endblock %}
```

**virtual_machines/update.html**

```html
{% extends "base.html" %}

{% block nav %}
  <ul class="nav nav-pills">
    <li class="nav-item fs-6"><a href="{{ url_for("virtual_machines.list_vms") }}" class="nav-link">Retour au répertoire des machines virtuelles</a></li>
  </ul>
{% endblock %}

{% block header %}
  {% block title %}Mettre à jour la machine virtuelle '{{ name }}'{% endblock %}
{% endblock %}

{% block content %}
  <section class="p-2">
    <form method="post">
      <div class="mb-3">
        <label for="vm-id" class="form-label">Type d'instance</label>
        <select name="instance_type" class="form-control" id="instance_type">
          {% for instance_type in instance_types %}
            <option value="{{ instance_type }}" {% if instance_type == curr_instance_type %} selected {% endif %}>
              {{ instance_type }}
            </option>
          {% endfor %}
          </select>
      </div>
      <div class="mb-3">
        <label for="vm-keypair" class="form-label">Clé publique</label>
        <textarea class="form-control" name="vm-keypair" id="vm-keypair-content" rows="5">{{ public_key }}</textarea>
      </div>
      <button type="submit" class="btn btn-primary">Mettre à jour</button>
    </form>
  </section>
{% endblock %}

```

### Créer la fonctionnalité avec Python

Il est maintenant temps de créer la fonctionnalité de notre clone de Heroku en utilisant Python. Le fichier "app.py" importe des fichiers que nous devons encore créer. Dans le même répertoire que "app.py", créez "sites.py".

Ajoutez ce qui suit à "sites.py" :

```python
import json
import requests
from flask import (
    current_app,
    Blueprint,
    request,
    flash,
    redirect,
    url_for,
    render_template,
)

import pulumi
import pulumi.automation as auto
from pulumi_aws import s3

bp = Blueprint("sites", __name__, url_prefix="/sites")
```

Ce sont simplement les imports de base dont nous avons besoin pour Flask et Pulumi, y compris l'importation du framework d'automatisation.

Ensuite, ajoutez le code suivant à ce fichier. Cette fonction définit notre site web statique Pulumi s3 en termes de contenu que l'appelant passe. Cela nous permet de déployer dynamiquement des sites web basés sur des valeurs définies par l'utilisateur à partir du corps POST.

```python
def create_pulumi_program(content: str):
    # Créer un bucket et exposer un document d'index de site web
    site_bucket = s3.Bucket(
        "s3-website-bucket", website=s3.BucketWebsiteArgs(index_document="index.html")
    )
    index_content = content

    # Écrire notre index.html dans le bucket du site
    s3.BucketObject(
        "index",
        bucket=site_bucket.id,
        content=index_content,
        key="index.html",
        content_type="text/html; charset=utf-8",
    )

    # Définir la politique d'accès pour le bucket afin que tous les objets soient lisibles
    s3.BucketPolicy(
        "bucket-policy",
        bucket=site_bucket.id,
        policy=site_bucket.id.apply(
            lambda id: json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": {
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": ["s3:GetObject"],
                        # La politique fait référence au bucket explicitement
                        "Resource": [f"arn:aws:s3:::{id}/*"],
                    },
                }
            )
        ),
    )

    # Exporter l'URL du site web
    pulumi.export("website_url", site_bucket.website_endpoint)
    pulumi.export("website_content", index_content)
```

Le but de `pulumi.export` que vous voyez à la fin du code est d'exporter une sortie de stack nommée. Les valeurs exportées sont attachées à la ressource Stack du programme. Plus tard, vous verrez comment nous pouvons accéder à ces données qui sont exportées.

Pour l'instant, rien n'appelle la fonction que nous venons de créer. À ce stade, nous allons créer des points de terminaison URL qui peuvent être utilisés pour appeler cette fonction et créer des sites web. 

Tout d'abord, nous allons ajouter le code pour l'URL /new qui créera un nouveau site :

```python
@bp.route("/new", methods=["GET", "POST"])
def create_site():
    """crée de nouveaux sites"""
    if request.method == "POST":
        stack_name = request.form.get("site-id")
        file_url = request.form.get("file-url")
        if file_url:
            site_content = requests.get(file_url).text
        else:
            site_content = request.form.get("site-content")

        def pulumi_program():
            return create_pulumi_program(str(site_content))

        try:
            # créer une nouvelle stack, générant notre programme pulumi à la volée à partir du corps POST
            stack = auto.create_stack(
                stack_name=str(stack_name),
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
            # déployer la stack, en suivant les logs vers stdout
            stack.up(on_output=print)
            flash(
                f"Site '{stack_name}' créé avec succès", category="success")
        except auto.StackAlreadyExistsError:
            flash(
                f"Erreur : Site avec le nom '{stack_name}' existe déjà, choisissez un nom unique",
                category="danger",
            )

        return redirect(url_for("sites.list_sites"))

    return render_template("sites/create.html")
```

Pour une requête GET, cette route rend le modèle "create.html". Pour une requête POST, elle crée un nouveau site et redirige vers la liste des sites à la route `/`.

Vous remarquerez qu'il y a une `stack` créée. Pour rappel, chaque programme Pulumi est déployé sur une stack. Une stack est une instance isolée et configurable indépendamment d'un programme Pulumi. Dans ce code, le nom de la stack est basé sur l'ID que l'utilisateur tape dans le formulaire. Il y a aussi un nom de projet, et le programme, qui est le bloc de code que nous avons précédemment discuté.

Une fois la stack créée, nous pouvons exécuter des commandes contre la `Stack`, y compris update, preview, refresh, destroy, import et export. Dans ce code, nous utilisons `stack.up()` pour `up`dater la stack. Et nous passons une fonction de rappel à `stack.up()` pour la sortie standard.

Ensuite, ajoutez le code pour l'URL racine qui listera les sites :

```python
@bp.route("/", methods=["GET"])
def list_sites():
    """liste tous les sites"""
    sites = []
    org_name = current_app.config["PULUMI_ORG"]
    project_name = current_app.config["PROJECT_NAME"]
    try:
        ws = auto.LocalWorkspace(
            project_settings=auto.ProjectSettings(
                name=project_name, runtime="python")
        )
        all_stacks = ws.list_stacks()
        for stack in all_stacks:
            stack = auto.select_stack(
                stack_name=stack.name,
                project_name=project_name,
                # programme no-op, juste pour obtenir les sorties
                program=lambda: None,
            )
            outs = stack.outputs()
            if 'website_url' in outs:
                sites.append(
                    {
                        "name": stack.name,
                        "url": f"http://{outs['website_url'].value}",
                        "console_url": f"https://app.pulumi.com/{org_name}/{project_name}/{stack.name}",
                    }
                )
    except Exception as exn:
        flash(str(exn), category="danger")

    return render_template("sites/index.html", sites=sites)
```

Un `Workspace` est le contexte d'exécution contenant un seul projet Pulumi, un programme et plusieurs stacks. Nous obtenons donc d'abord l'accès `ws = auto.LocalWorkspace()`.

Ensuite, nous `list_stacks()`. Cela nous donne simplement accès au nom de la stack, donc nous devons utiliser `auto.select_stack()` pour accéder à la stack. Nous voulons spécifiquement `stack.outputs()`. Cela sera ce que nous avons exporté vers la stack, y compris `website_url`. 

Ensuite, nous ajoutons des informations pour chaque site à la liste `sites` qui est utilisée sur le frontend pour afficher la liste des sites. 

Maintenant, ajoutez le code pour la route /update. 

```python
@bp.route("/<string:id>/update", methods=["GET", "POST"])
def update_site(id: str):
    stack_name = id

    if request.method == "POST":
        file_url = request.form.get("file-url")
        if file_url:
            site_content = requests.get(file_url).text
        else:
            site_content = str(request.form.get("site-content"))

        try:

            def pulumi_program():
                create_pulumi_program(str(site_content))

            stack = auto.select_stack(
                stack_name=stack_name,
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
            # déployer la stack, en suivant les logs vers stdout
            stack.up(on_output=print)
            flash(f"Site '{stack_name}' mis à jour avec succès !",
                  category="success")
        except auto.ConcurrentUpdateError:
            flash(
                f"Erreur : le site '{stack_name}' a déjà une mise à jour en cours",
                category="danger",
            )
        except Exception as exn:
            flash(str(exn), category="danger")
        return redirect(url_for("sites.list_sites"))

    stack = auto.select_stack(
        stack_name=stack_name,
        project_name=current_app.config["PROJECT_NAME"],
        # noop juste pour obtenir les sorties
        program=lambda: None,
    )
    outs = stack.outputs()
    content_output = outs.get("website_content")
    content = content_output.value if content_output else None
    return render_template("sites/update.html", name=stack_name, content=content)
```

Vous remarquerez que la route /update est très similaire à la route /new. Puisqu'elle utilise le même `stack_name`, un nouveau site n'est pas créé.

Une nouvelle chose dans cette fonction est que le code obtient le contenu du site web pour le retourner au modèle frontend.

Enfin, ajoutez le code suivant pour une route /delete.

```
@bp.route("/<string:id>/delete", methods=["POST"])
def delete_site(id: str):
    stack_name = id
    try:
        stack = auto.select_stack(
            stack_name=stack_name,
            project_name=current_app.config["PROJECT_NAME"],
            # programme noop pour détruire
            program=lambda: None,
        )
        stack.destroy(on_output=print)
        stack.workspace.remove_stack(stack_name)
        flash(f"Site '{stack_name}' supprimé avec succès !", category="success")
    except auto.ConcurrentUpdateError:
        flash(
            f"Erreur : Le site '{stack_name}' a déjà une mise à jour en cours",
            category="danger",
        )
    except Exception as exn:
        flash(str(exn), category="danger")

    return redirect(url_for("sites.list_sites"))

```

Dans cette fonction de suppression, nous obtenons d'abord l'accès à la stack, puis nous détruisons et supprimons la stack. Simplement en appelant la fonction `stack.destroy()` supprimera la ressource sur AWS.

Maintenant, dans le même répertoire que "app.py", créez "virtual_machines.py".

Ajoutez ce qui suit à "virtual_machines.py". Cette fois, nous allons tout ajouter en une seule fois :

```python
from flask import (Blueprint, current_app, request, flash,
                   redirect, url_for, render_template)

import pulumi
import pulumi_aws as aws
import pulumi.automation as auto
import os
from pathlib import Path

bp = Blueprint("virtual_machines", __name__, url_prefix="/vms")
instance_types = ['c5.xlarge', 'p2.xlarge', 'p3.2xlarge']


def create_pulumi_program(keydata: str, instance_type=str):
    # Choisir la dernière AMI Linux amzn2 minimale.
    # TODO : Faire en sorte que l'utilisateur puisse choisir cela.
    ami = aws.ec2.get_ami(most_recent=True,
                          owners=["amazon"],
                          filters=[aws.GetAmiFilterArgs(name="name", values=["*amzn2-ami-minimal-hvm*"])])

    group = aws.ec2.SecurityGroup('web-secgrp',
                                  description='Activer l\'accès SSH',
                                  ingress=[aws.ec2.SecurityGroupIngressArgs(
                                      protocol='tcp',
                                      from_port=22,
                                      to_port=22,
                                      cidr_blocks=['0.0.0.0/0'],
                                  )])

    public_key = keydata
    if public_key is None or public_key == "":
        home = str(Path.home())
        f = open(os.path.join(home, '.ssh/id_rsa.pub'), 'r')
        public_key = f.read()
        f.close()

    public_key = public_key.strip()

    print(f"Clé publique : '{public_key}'\n")

    keypair = aws.ec2.KeyPair("dlami-keypair", public_key=public_key)

    server = aws.ec2.Instance('dlami-server',
                              instance_type=instance_type,
                              vpc_security_group_ids=[group.id],
                              key_name=keypair.id,
                              ami=ami.id)

    pulumi.export('instance_type', server.instance_type)
    pulumi.export('public_key', keypair.public_key)
    pulumi.export('public_ip', server.public_ip)
    pulumi.export('public_dns', server.public_dns)


@bp.route("/new", methods=["GET", "POST"])
def create_vm():
    """crée une nouvelle VM"""
    if request.method == "POST":
        stack_name = request.form.get("vm-id")
        keydata = request.form.get("vm-keypair")
        instance_type = request.form.get("instance_type")

        def pulumi_program():
            return create_pulumi_program(keydata, instance_type)
        try:
            # créer une nouvelle stack, générant notre programme pulumi à la volée à partir du corps POST
            stack = auto.create_stack(
                stack_name=str(stack_name),
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
            # déployer la stack, en suivant les logs vers stdout
            stack.up(on_output=print)
            flash(
                f"VM '{stack_name}' créée avec succès", category="success")
        except auto.StackAlreadyExistsError:
            flash(
                f"Erreur : VM avec le nom '{stack_name}' existe déjà, choisissez un nom unique",
                category="danger",
            )
        return redirect(url_for("virtual_machines.list_vms"))

    current_app.logger.info(f"Types d'instance : {instance_types}")
    return render_template("virtual_machines/create.html", instance_types=instance_types, curr_instance_type=None)


@bp.route("/", methods=["GET"])
def list_vms():
    """liste toutes les VM"""
    vms = []
    org_name = current_app.config["PULUMI_ORG"]
    project_name = current_app.config["PROJECT_NAME"]
    try:
        ws = auto.LocalWorkspace(
            project_settings=auto.ProjectSettings(
                name=project_name, runtime="python")
        )
        all_stacks = ws.list_stacks()
        for stack in all_stacks:
            stack = auto.select_stack(
                stack_name=stack.name,
                project_name=project_name,
                # programme no-op, juste pour obtenir les sorties
                program=lambda: None,
            )
            outs = stack.outputs()
            if 'public_dns' in outs:
                vms.append(
                    {
                        "name": stack.name,
                        "dns_name": f"{outs['public_dns'].value}",
                        "console_url": f"https://app.pulumi.com/{org_name}/{project_name}/{stack.name}",
                    }
                )
    except Exception as exn:
        flash(str(exn), category="danger")

    current_app.logger.info(f"VM : {vms}")
    return render_template("virtual_machines/index.html", vms=vms)


@bp.route("/<string:id>/update", methods=["GET", "POST"])
def update_vm(id: str):
    stack_name = id
    if request.method == "POST":
        current_app.logger.info(
            f"Mise à jour de la VM : {stack_name}, données du formulaire : {request.form}")
        keydata = request.form.get("vm-keypair")
        current_app.logger.info(f"Mise à jour de la clé publique : {keydata}")
        instance_type = request.form.get("instance_type")

        def pulumi_program():
            return create_pulumi_program(keydata, instance_type)
        try:
            stack = auto.select_stack(
                stack_name=stack_name,
                project_name=current_app.config["PROJECT_NAME"],
                program=pulumi_program,
            )
            stack.set_config("aws:region", auto.ConfigValue("us-east-1"))
            # déployer la stack, en suivant les logs vers stdout
            stack.up(on_output=print)
            flash(f"VM '{stack_name}' mise à jour avec succès !",
                  category="success")
        except auto.ConcurrentUpdateError:
            flash(
                f"Erreur : la VM '{stack_name}' a déjà une mise à jour en cours",
                category="danger",
            )
        except Exception as exn:
            flash(str(exn), category="danger")
        return redirect(url_for("virtual_machines.list_vms"))

    stack = auto.select_stack(
        stack_name=stack_name,
        project_name=current_app.config["PROJECT_NAME"],
        # noop juste pour obtenir les sorties
        program=lambda: None,
    )
    outs = stack.outputs()
    public_key = outs.get("public_key")
    pk = public_key.value if public_key else None
    instance_type = outs.get("instance_type")
    return render_template("virtual_machines/update.html", name=stack_name, public_key=pk, instance_types=instance_types, curr_instance_type=instance_type.value)


@bp.route("/<string:id>/delete", methods=["POST"])
def delete_vm(id: str):
    stack_name = id
    try:
        stack = auto.select_stack(
            stack_name=stack_name,
            project_name=current_app.config["PROJECT_NAME"],
            # programme noop pour détruire
            program=lambda: None,
        )
        stack.destroy(on_output=print)
        stack.workspace.remove_stack(stack_name)
        flash(f"VM '{stack_name}' supprimée avec succès !", category="success")
    except auto.ConcurrentUpdateError:
        flash(
            f"Erreur : la VM '{stack_name}' a déjà une mise à jour en cours",
            category="danger",
        )
    except Exception as exn:
        flash(str(exn), category="danger")

    return redirect(url_for("virtual_machines.list_vms"))
```

Il y a beaucoup de similitudes entre ce fichier et le fichier 'sites.py'. Une machine virtuelle a beaucoup plus de paramètres qui doivent être définis et Pulumi est capable de créer le type exact de VM que nous voulons. 

Nous pourrions permettre à l'utilisateur de tout personnaliser depuis l'interface web, mais nous donnons simplement à l'utilisateur la possibilité de choisir le type d'instance. 

Une chose qui est requise pour une VM est une paire de clés publique/privée. Lors de la création d'une VM sur AWS, vous devez fournir une clé publique. Ensuite, pour accéder à la VM, vous devez avoir la clé privée.

Vous pouvez créer des clés dans votre terminal. Exécutez la commande suivante :

`ssh-keygen -m PEM`

Plus tard, lors du test de l'application, vous devrez ouvrir le fichier de clé publique afin de pouvoir copier la clé et la coller dans le site web.

Maintenant, changez le répertoire avec le fichier que vous venez de créer. Le répertoire doit être le même que vous soyez sur MacOS ou Windows.

Tapez dans votre terminal :

`cd /Users/[username]/.ssh`

AWS a besoin que le fichier soit au format .pem et c'est pourquoi nous l'avons créé avec "PEM" ci-dessus. Maintenant, renommons le fichier pour qu'il ait la bonne extension. Vous devez changer le nom du fichier appelé `id_rsa` pour qu'il soit `id_rsa.pem`.

Sur macOS, vous pouvez renommer avec cette commande :

`mv id_rsa id_rsa.pem`

Sur Windows, utilisez :

`rename id_rsa id_rsa.pem`

Lors de l'exécution de l'application Flask, vous devrez peut-être entrer la clé publique que vous venez de créer. Vous pouvez ouvrir `id_rsa.pub` dans n'importe quel éditeur de texte afin de copier le texte. Si vous avez vim, vous pouvez utiliser cette commande pour ouvrir le fichier :

`vim /Users/beau/.ssh/id_rsa.pub`

### Tester l'application

Il est maintenant temps d'essayer l'application. Dans le terminal, exécutez cette commande :

`FLASK_RUN_PORT=1337 FLASK_ENV=development FLASK_APP=__init__ PULUMI_ORG=[votre-nom-d-org] venv/bin/flask run`

Maintenant, vous pouvez essayer l'application et créer des sites web et des VM. Assurez-vous de les supprimer après la création afin qu'AWS ne continue pas à vous facturer pour les ressources.

## Conclusion

Vous devriez maintenant savoir assez de choses pour commencer à approvisionner l'infrastructure dans vos propres applications en utilisant l'API d'automatisation de Pulumi. Et si vous voulez voir étape par étape comment faire les choses dans cet article, consultez le tutoriel vidéo :

%[https://youtu.be/zhJLVFR3pE8]