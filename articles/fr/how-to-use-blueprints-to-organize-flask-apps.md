---
title: Comment utiliser les Blueprints pour organiser vos applications Flask
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-09-01T15:25:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-blueprints-to-organize-flask-apps
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/blueprints.png
tags:
- name: Flask Framework
  slug: flask
- name: Python
  slug: python
seo_title: Comment utiliser les Blueprints pour organiser vos applications Flask
seo_desc: "Flask is a simple, easy-to-use microframework for Python that can help\
  \ you build scalable and secure web applications. \nSometimes you'll find developers\
  \ dumping all of their logic into a single file called app.py. You will find a lot\
  \ of tutorials tha..."
---

Flask est un microframework simple et facile à utiliser pour Python qui peut vous aider à construire des applications web scalables et sécurisées. 

Parfois, vous trouverez des développeurs qui mettent toute leur logique dans un seul fichier appelé app.py. Vous trouverez beaucoup de tutoriels qui suivent le même schéma. Mais ce n'est pas une bonne pratique pour une application à grande échelle. 

En faisant cela, vous violez clairement le _Principe de Responsabilité Unique_, où chaque partie de votre application doit gérer une seule responsabilité. 

Si vous avez travaillé avec Django, vous avez peut-être trouvé votre projet divisé en différents modules. Dans Flask, vous pouvez également organiser vos applications en utilisant les **Blueprints**, un concept intégré dans Flask similaire aux modules Python.

## À quoi ressemble une application Flask ?

Si vous suivez la documentation Flask pour créer une application minimale, la structure de votre projet ressemblera à ceci :

```md
/myapp
├── /templates
├── /static
└── app.py
```

Le dossier ne semble-t-il pas si propre ? Vous avez un fichier `app.py` où se trouve toute la logique de votre application, un dossier `templates` pour stocker vos fichiers HTML et un dossier `static` pour stocker vos fichiers statiques. 

Regardons le fichier app.py :

```py
from flask import Flask


app = Flask(__name__)

# Quelques Modèles Ici


# Routes liées aux fonctionnalités principales


# Routes liées à la Page de Profil


# Routes liées à la Page des Produits


# Routes liées à la Page de Blog


# Routes liées à la Page d'Administration

if __name__ == '__main__':
    app.run(debug=True)
```

Cela ne semble-t-il pas désordonné (en imaginant que vous avez construit une application à grande échelle) ? Vous avez tous vos modèles et différentes routes dans le même fichier, éparpillés ici et là.

## Comment les Blueprints résolvent-ils le problème ?

C'est là que les Blueprints de Flask entrent en jeu. Les Blueprints vous aident à structurer votre application en organisant la logique dans des sous-répertoires. En plus de cela, vous pouvez stocker vos templates et fichiers statiques avec la logique dans le même sous-répertoire.

Ainsi, avec les Blueprints, votre application aura maintenant cette apparence :

```md
/blueprint-tutorial
├── /myapp_with_blueprints
│   ├── __init__.py
│   ├── /admin
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /core
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   ├── /products
│   │   ├── /templates
│   │   ├── /static
│   │   └── routes.py
│   └── /profile
|       ├── /templates
|       ├── /static
|       └── routes.py		
├── app.py
├── /static
└── /templates
```

Maintenant, vous pouvez voir que vous avez une séparation claire des responsabilités. La logique liée à l'administration réside dans le dossier `admin`, la logique liée aux produits réside dans le dossier `products`, et ainsi de suite. 

De plus, nous avons également séparé les templates et les fichiers statiques dans les sous-répertoires où ils sont nécessaires, afin que les fichiers non pertinents ne se chargent pas lors de l'accès à une page qui n'en a pas besoin.

## Comment utiliser les Blueprints

Maintenant que vous comprenez les problèmes que les Blueprints résolvent, voyons comment nous pouvons utiliser les Blueprints dans nos applications.

### Comment définir un Blueprint

Définissons notre tout premier blueprint pour la fonctionnalité **admin** dans le fichier `admin/routes.py` :

```py
from flask import Blueprint


# Définition d'un blueprint
admin_bp = Blueprint(
    'admin_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

```

Puisque Blueprint est un concept intégré de Flask, vous pouvez l'importer depuis la bibliothèque Flask. Lors de la création de l'objet de la classe `Blueprint`, le premier paramètre est le nom que vous souhaitez donner à votre Blueprint. Ce nom sera utilisé ultérieurement pour le routage interne (nous verrons cela ci-dessous). 

Le deuxième paramètre est le nom du package Blueprint, généralement `__name__`. Cela aide à localiser le `root_path` pour le blueprint. 

Les troisième et quatrième paramètres passés sont des [arguments de mot-clé](https://ashutoshkrris.hashnode.dev/what-are-args-and-kwargs-in-python) optionnels. En définissant les paramètres `template_folder` et `static_folder`, vous spécifiez que vous utiliserez des templates et des fichiers statiques spécifiques au blueprint. 

### Comment définir des routes avec des Blueprints

Maintenant que vous avez créé un blueprint pour la fonctionnalité liée à l'administration, vous pouvez l'utiliser lors de la création de routes pour les administrateurs.

```py
from flask import Blueprint


# Définition d'un blueprint
admin_bp = Blueprint(
    'admin_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@admin_bp.route('/admin')   # Concentrez-vous ici
def admin_home():
    return "Hello Admin!"
```

Dans l'extrait ci-dessus, concentrez-vous sur la ligne où la route est définie. Au lieu de l'habituel `@app.route('...')`, nous avons utilisé `@admin_bp.route('...')`. C'est ainsi que vous liez une route à un blueprint particulier.

### Comment enregistrer vos Blueprints

Maintenant, vous avez un blueprint et une route qui lui est enregistrée. Mais votre application saura-t-elle automatiquement ce blueprint ? 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-112849.png)
_Non. Vous devez le faire._

Alors, faisons-le. Dans le fichier `__init__.py`, nous allons créer une application Flask et y enregistrer nos blueprints :

```py
from flask import Flask


app = Flask(__name__)

from .admin import routes

# Enregistrement des blueprints
app.register_blueprint(admin.admin_bp)

```

Pour enregistrer le blueprint, nous utilisons la méthode `register_blueprint()` et passons le nom du blueprint. De plus, vous pouvez passer d'autres paramètres à la méthode pour plus de personnalisation. L'un d'eux est `url_prefix` que vous pourriez nécessiter.

```py
app.register_blueprint(admin.admin_bp, url_prefix='/admin')
```

De même, vous pouvez enregistrer le reste de vos blueprints si vous en avez plus.

## Routage des templates avec les Blueprints

Sans les Blueprints, pour créer des liens dans vos templates, vous utiliseriez quelque chose de similaire à ce qui suit :

```html
<a href="{{ url_for('admin_home') }}">My Link</a>
```

Mais avec les blueprints en place, vous pouvez maintenant définir vos liens comme suit :

```html
<a href="{{ url_for('admin_bp.admin_home') }}">My Link</a>
```

Le `admin_bp` que nous avons utilisé ci-dessus est le nom que nous avons donné à notre blueprint pour le routage interne lors de la création de l'objet. 

Pour imprimer le nom du blueprint du template Jinja2 auquel appartient la page actuelle, vous pouvez utiliser `{{request.blueprint}}`.

Note : Pour utiliser des actifs spécifiques aux Blueprints, vous pouvez utiliser la bibliothèque <a href="https://flask-assets.readthedocs.io/en/latest/">Flask-Assets</a>.

## Conclusion

Blueprint est un outil incroyable pour organiser et structurer vos applications Flask. 

Dans cet article, vous avez appris ce que les blueprints ont à offrir et comment les utiliser dans vos applications Flask.

Merci d'avoir lu !

Vous pouvez me suivre sur [Twitter](https://twitter.com/ashutoshkrris)[.](https://ireadblog.com/)