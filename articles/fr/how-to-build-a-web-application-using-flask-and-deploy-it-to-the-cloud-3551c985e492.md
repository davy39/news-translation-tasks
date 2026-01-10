---
title: Comment créer une application web avec Flask et la déployer dans le cloud
subtitle: ''
author: Salvador Villalon Jr
co_authors: []
series: null
date: '2018-08-28T15:04:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OrCZB4PxwGqppjkoIMzCaA.png
tags:
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer une application web avec Flask et la déployer dans le cloud
seo_desc: 'Introduction

  In each section, I will show pieces of code for you to follow along. All the code
  used in the tutorial is available in this GitHub Repository.

  What is HTTP and What Does it Have to do with Flask?

  HTTP is the protocol for websites. The in...'
---

### **Introduction**

Dans chaque section, je vais vous montrer des extraits de code à suivre. Tout le code utilisé dans ce tutoriel est disponible dans ce [Dépôt GitHub](https://github.com/salvillalon45/SPGISummer2018-FlaskTutorial).

## Qu'est-ce que HTTP et quel est son rapport avec Flask ?

[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) est le protocole des sites web. Internet l'utilise pour interagir et communiquer avec les ordinateurs et les serveurs. Permettez-moi de vous donner un exemple de la manière dont vous l'utilisez tous les jours.

Lorsque vous tapez le nom d'un site web dans la barre d'adresse de votre navigateur et que vous appuyez sur Entrée, un message HTTP est envoyé à un serveur.

Par exemple, lorsque je vais dans ma barre d'adresse et que je tape google.com, puis que j'appuie sur Entrée, une requête HTTP est envoyée à un serveur Google. Le serveur Google reçoit la requête et doit déterminer comment l'interpréter. Le serveur Google envoie une réponse HTTP qui contient les informations que mon navigateur web reçoit. Ensuite, il affiche ce que vous avez demandé sur une page dans le navigateur.

### Comment Flask est-il impliqué ?

Nous allons écrire du code qui prendra en charge le traitement côté serveur. Notre code recevra des requêtes. Il déterminera ce que ces requêtes traitent et ce qu'elles demandent. Il déterminera également quelle réponse envoyer à l'utilisateur.

Pour tout cela, nous utiliserons Flask.

## Qu'est-ce que Flask ?

![Image](https://cdn-media-1.freecodecamp.org/images/1SnE5y1jhzqsSoFvgFyWc4mRLXX-iuG2DPtm align="left")

[Flask (Un Microframework Python)](http://flask.pocoo.org/" rel="noopener" target="*blank" title=")

Il simplifie le processus de conception d'une application web. Flask nous permet de nous concentrer sur ce que **les utilisateurs demandent et sur le type de réponse à renvoyer.**

En savoir plus sur les [micro frameworks](https://en.wikipedia.org/wiki/Microframework).

## Comment fonctionne une application Flask ?

Le code nous permet d'exécuter une application web de base que nous pouvons servir, comme si c'était un site web.

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(debug=True)
```

Ce morceau de code est stocké dans notre main.py.

**Ligne 1 :** Ici, nous importons le module Flask et créons un serveur web Flask à partir du module Flask.

**Ligne 3 : name signifie ce fichier actuel.** Dans ce cas, ce sera main.py. Ce fichier actuel représentera mon application web.

Nous créons une instance de la classe Flask et l'appelons app. Ici, nous créons une nouvelle application web.

**Ligne 5 :** Elle représente la page par défaut. Par exemple, si je vais sur un site web comme "google.com/" sans rien après le slash. Alors ce sera la page par défaut de Google.

![Image](https://cdn-media-1.freecodecamp.org/images/rl8hovE8cNuaTMh6X8S8y4LLYoAVTJ5uvSMh align="left")

*C'est ce que représentera @app.route("/")*

**Lignes 6-7 :** Lorsque l'utilisateur va sur mon site web et qu'il accède à la page par défaut (rien après le slash), la fonction ci-dessous sera activée.

**Ligne 9 :** Lorsque vous exécutez votre script Python, Python attribue le nom "**main**" au script lors de son exécution.

Si nous importons un autre script, **l'instruction if empêchera les autres scripts de s'exécuter.** Lorsque nous exécutons main.py, il changera son nom en **main** et seule cette instruction if sera activée.

**Ligne 10 :** Cela exécutera l'application. Avoir `debug=True` permet aux erreurs Python possibles d'apparaître sur la page web. Cela nous aidera à tracer les erreurs.

### **Essayons d'exécuter main.py**

Dans votre Terminal ou Invite de Commande, allez dans le dossier qui contient votre main.py. Ensuite, faites `**py main.py**` ou `**python main.py**`. Dans votre terminal ou invite de commande, vous devriez voir cette sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/QynmMfSb7CoZkeuyC38ZLrTuA5eHtTkSxb6n align="left")

La partie importante est celle où il est écrit `Running on http://127.0.0.1:5000/`.

127.0.0.1 signifie cet ordinateur local. Si vous ne connaissez pas la signification de ceci (comme je ne le savais pas lorsque j'ai commencé — [cet article est vraiment utile](https://whatismyipaddress.com/localhost)), l'idée principale est que 127.0.0.1 et localhost font référence à cet ordinateur local.

Allez à cette adresse et vous devriez voir ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/3TazBO699jNj7C88MyFbf-jlqseyWRPL5N4X align="left")

*Félicitations ! Vous avez créé un site web avec Flask !*

#### **Plus de plaisir avec Flask**

Plus tôt, vous avez vu ce qui se passait lorsque nous avons exécuté main.py avec une route qui était app.route("/").

Ajoutons plus de routes pour que vous puissiez voir la différence.

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)
```

Dans les **lignes 9-11**, nous avons ajouté une nouvelle route, cette fois vers **/salvador.**

Maintenant, exécutez à nouveau main.py et allez sur [http://localhost:5000/salvador](http://localhost:5000/salvador).

![Image](https://cdn-media-1.freecodecamp.org/images/63Ib3PYx1He2Y0pRiH9As7OivEc-dBmsVdYE align="left")

Jusqu'à présent, nous avons renvoyé du texte. Rendons notre site web plus joli en ajoutant du HTML et du CSS.

## HTML, CSS et Environnements Virtuels

### HTML et Modèles dans Flask

Tout d'abord, créez un nouveau fichier HTML. J'ai appelé le mien **home.html.**

Voici un peu de code pour vous aider à démarrer.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Tutoriel Flask</title>
  </head>
  <body>
    <h1> Ma Première Tentative avec Flask </h1>
    <p> Flask est Amusant </p>
  </body>
</html>
```

#### **Point Important à Retenir**

Le Framework Flask recherche les fichiers HTML dans un dossier appelé **templates.** Vous **devez créer un dossier templates** et y mettre tous vos fichiers HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/Ggzs2MzQiYmno0hkvLCbdj2-rWl4gzqkjZil align="left")

*Rappelez-vous de toujours garder le main.py à l'extérieur de votre dossier templates*

Maintenant, nous devons modifier notre main.py afin de pouvoir visualiser le fichier HTML que nous avons créé.

```py
from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)
  Nous avons apporté deux nouvelles modifications
```

**Ligne 1 :** Nous avons importé la méthode `render_template()` du framework flask. `render_template()` recherche un modèle (fichier HTML) dans le dossier templates. Ensuite, il rendra le modèle que vous demandez. En savoir plus sur la [fonction render_templates()](http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates).

**Ligne 7 :** Nous changeons le retour afin qu'il retourne maintenant `render_template("home.html")`. Cela nous permettra de visualiser notre fichier HTML.

Maintenant, visitez votre localhost et voyez les changements : [http://localhost:5000/](http://localhost:5000/).

![Image](https://cdn-media-1.freecodecamp.org/images/YmVgj3pCcduDB6T5UBabraK-glrVPNGhc4R9 align="left")

### **Ajoutons plus de pages**

Créons un **about.html** à l'intérieur du **dossier templates.**

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>À propos de Flask</title>
  </head>
  <body>
    <h1> À propos de Flask </h1>
    <p> Flask est un micro framework web écrit en Python.</p>
    <p> Les applications qui utilisent le framework Flask incluent Pinterest,
      LinkedIn, et la page web communautaire de Flask elle-même.</p>
  </body>
</html>
```

Apportons une modification similaire à celle que nous avons faite précédemment à notre main.py.

```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(debug=True)
```

Nous avons apporté trois nouvelles modifications :

**Ligne 9 :** Changez la route en `"/about"`.

**Ligne 10 :** Changez la fonction pour qu'elle soit maintenant `def about():`

**Ligne 11 :** Changez le retour pour qu'il retourne maintenant `render_template("about.html")`.

Maintenant, voyez les changements : [http://localhost:5000/about](http://localhost:5000/about).

![Image](https://cdn-media-1.freecodecamp.org/images/O1Oo1GXYO2LHnXRiz8-VmKuvpywABTV7MuVn align="left")

### Connectons les Deux Pages avec une Navigation

Pour connecter les deux pages, nous pouvons avoir un menu de navigation en haut. Nous pouvons utiliser Flask pour faciliter le processus de création d'un menu de navigation.

Tout d'abord, créons un **template.html.** Ce **template.html** servira de modèle parent. Nos deux modèles enfants en hériteront du code.

```html
 <!DOCTYPE html>
<html lang="en" dir="ltr">
 <head>
   <meta charset="utf-8">
   <title>Modèle Parent Flask</title>
   <link rel="stylesheet" href="{{ url_for('static',     filename='css/template.css') }}">
 </head>
 <body>
    <header>
      <div class="container">
        <h1 class="logo">Première Application Web</h1>
        <strong><nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Accueil</a></li>
            <li><a href="{{ url_for('about') }}">À propos</a></li>
          </ul>
        </nav></strong>
      </div>
    </header>
    
    {% block content %}
    {% endblock %}
    
 </body>
</html>
```

**Lignes 13-14 :** Nous utilisons la fonction appelée `url_for()`. Elle accepte le nom de la fonction comme argument. Pour l'instant, nous lui avons donné le nom de la fonction. Plus d'informations sur la [fonction url_for()](http://flask.pocoo.org/docs/0.12/quickstart/#url-building).

Les deux lignes avec les accolades seront **remplacées par le contenu de home.html et about.html.** Cela dépendra de l'URL sur laquelle l'utilisateur navigue.

Ces modifications permettent aux pages enfants (home.html et about.html) de se connecter au parent (template.html). Cela nous permet de ne pas avoir à **copier le code du menu de navigation dans about.html et home.html.**

Contenu de about.html :

```javascript
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>À propos de Flask</title>
  </head>
  <body>
    {% extends "template.html" %}
    {% block content %}
    
    <h1> À propos de Flask </h1>
    <p> Flask est un micro framework web écrit en Python.</p>
    <p> Les applications qui utilisent le framework Flask incluent Pinterest,
      LinkedIn, et la page web communautaire de Flask elle-même.</p>
      
    {% endblock %}
  </body>
</html>
```

Contenu de home.html :

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Tutoriel Flask</title>
  </head>
  <body>
    {% extends "template.html" %}
    {% block content %}
    
    <h1> Ma Première Tentative avec Flask </h1>
    <p> Flask est Amusant </p>
    
    {% endblock %}
  </body>
</html>
```

Essayons d'ajouter un peu de CSS.

## Ajout de CSS à Notre Site Web

### Une note importante à retenir

De la même manière que nous avons créé un dossier appelé **templates** pour stocker tous nos modèles HTML, nous avons besoin d'un dossier appelé **static.**

Dans **static**, nous stockerons notre CSS, JavaScript, images et autres fichiers nécessaires. C'est pourquoi il est important que vous créiez un **dossier CSS** pour stocker vos feuilles de style. Après avoir fait cela, votre dossier de projet devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ui4uCQ2KhjEaJ1JQ71XgXwNIs5TkzPuaGU8W align="left")

### Lier notre CSS avec notre fichier HTML

Notre template.html est celui qui lie toutes les pages. Nous pouvons insérer le code ici et il sera applicable à toutes les pages enfants.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Modèle Parent Flask</title>
    
    <link rel="stylesheet" href="{{ url_for('static',    filename='css/template.css') }}">
    
</head>
  <body>
    <header>
      <div class="container">
        <h1 class="logo">Première Application Web</h1>
        <strong><nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Accueil</a></li>
            <li><a href="{{ url_for('about') }}">À propos</a></li>
          </ul>
        </nav></strong>
      </div>
    </header>
    
{% block content %}
{% endblock %}

 </body>
</html>
```

**Ligne 7 :** Ici, nous donnons le chemin où se trouve template.css.

Maintenant, voyez les changements : [http://localhost:5000/about](http://localhost:5000/about).

![Image](https://cdn-media-1.freecodecamp.org/images/kvI3GKRQwhuu2O2giyPZBvu2am63So7OLH32 align="left")

## Avancer avec Flask et virtualenv

Maintenant que vous êtes familiarisé avec l'utilisation de Flask, vous pouvez commencer à l'utiliser dans vos futurs projets. Une chose à toujours faire est d'utiliser virtualenv.

### Pourquoi utiliser virtualenv ?

Vous pouvez utiliser Python pour d'autres projets que le développement web.

Vos projets peuvent avoir différentes versions de Python installées, différentes dépendances et packages.

Nous utilisons virtualenv pour créer un environnement isolé pour votre projet Python. Cela signifie que chaque projet peut avoir ses propres dépendances, indépendamment des dépendances des autres projets.

### Commencer avec virtualenv

Tout d'abord, exécutez cette commande dans votre invite de commande ou terminal :

```bash
pip install virtualenv
```

Deuxièmement, faites ce qui suit :

```bash
virtualenv "nom de l'environnement virtuel"
```

Ici, vous pouvez donner un nom à l'environnement. Je lui donne généralement un nom comme virtual. Cela ressemblera à ceci : `virtualenv virtual`.

Après avoir configuré l'environnement virtuel, vérifiez votre dossier de projet. Il devrait ressembler à ceci. L'environnement virtuel doit être créé dans le **même répertoire où se trouvent vos fichiers d'application.**

![Image](https://cdn-media-1.freecodecamp.org/images/nlsgTQVp9ZrBHudAD4yKWF7tywO5fsaiYvHq align="left")

*À quoi ressemble le répertoire*

### Activation de l'environnement virtuel

Maintenant, allez dans votre terminal ou invite de commande. Allez dans le répertoire qui contient le fichier appelé **activate.** Le fichier appelé **activate** se trouve dans un dossier appelé **Scripts pour Windows** et **bin pour OS X et Linux.**

Pour l'environnement OS X et Linux :

```bash
$ nom de l'environnement virtuel/bin/activate
```

Pour l'environnement Windows :

```bash
nom de l'environnement virtuel\Scripts\activate
```

Comme j'utilise une machine Windows, lorsque j'active l'environnement, cela ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/FnmOzwRngsHOTcuJr4gMBnvyB6VhYGhcdyI2 align="left")

*Vous devriez voir ceci au début de votre ligne d'invite de commande*

L'étape suivante consiste à installer flask dans votre environnement virtuel afin que nous puissions exécuter l'application dans notre environnement. Exécutez la commande :

```bash
pip install flask
```

Exécutez votre application et allez sur [http://localhost:5000/](http://localhost:5000/)

Nous avons enfin créé notre application web. Maintenant, nous voulons montrer notre projet au monde entier.

(Plus d'informations sur virtualenv peuvent être trouvées dans les guides suivants sur [virtualenv](https://realpython.com/python-virtual-environments-a-primer/) et [Documentation Officielle de Flask](http://flask.pocoo.org/docs/0.12/installation/#installation))

## Envoyons-le dans le Cloud

Pour montrer aux autres le projet que nous avons réalisé, nous devons apprendre à utiliser les services Cloud.

### Déployer Votre Application Web dans le Cloud

Pour déployer notre application web dans le cloud, nous utiliserons [Google App Engine](https://cloud.google.com/appengine/) (Environnement Standard). Il s'agit d'un exemple de **Plateforme en tant que Service (PaaS).**

**PaaS** fait référence à la **fourniture de systèmes d'exploitation et de services associés via Internet sans téléchargements ni installation**. Cette approche permet aux clients de créer et de déployer des applications sans avoir à investir dans l'infrastructure sous-jacente (Plus d'informations sur PaaS, consultez [TechTarget](https://searchitchannel.techtarget.com/definition/cloud-services)).

> Google App Engine est une offre de plateforme en tant que service qui permet aux développeurs et aux entreprises de créer et d'exécuter des applications en utilisant l'infrastructure avancée de Google — [TechOpedia](https://www.techopedia.com/definition/31267/google-app-engine-gae).

#### **Avant de commencer :**

Vous aurez besoin d'un [Compte Google](https://accounts.google.com/signup/v2?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp). Une fois que vous avez créé un compte, allez sur la [Console Google Cloud Platform](https://console.cloud.google.com) et créez un nouveau projet. De plus, vous devez installer le [Google Cloud SDK](https://cloud.google.com/sdk/).

À la fin de ce tutoriel, la structure de votre projet ressemblera à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/Nb7fiERQFkKC5chGteCvWkQCkShVq7a1auUe align="left")

*Structure du Dossier de Projet*

Nous devrons créer trois nouveaux fichiers : app.yaml, appengine_config.py et requirements.txt.

Contenu de app.yaml :

```yml
runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /static
  static_dir: static
- url: /.*
  script: main.app
  
libraries:
  - name: ssl
    version: latest
```

Si vous deviez consulter le [Tutoriel de Google](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env) dans la partie où ils **parlent du contenu de app.yaml**, il ne comprend pas la section où j'ai écrit sur les bibliothèques.

Lors de ma première tentative de déploiement de mon application web simple, mon déploiement n'a jamais fonctionné. Après plusieurs tentatives, j'ai appris que nous devions inclure la bibliothèque SSL.

La bibliothèque SSL nous permet de [créer des connexions sécurisées entre le client et le serveur](https://wiki.python.org/moin/SSL). Chaque fois que l'utilisateur accède à notre site web, il devra se connecter à un serveur exécuté par Google App Engine. Nous devons créer une connexion sécurisée pour cela. (Je viens de l'apprendre, alors si vous avez des suggestions à ce sujet, faites-le moi savoir !)

Contenu de appengine_config.py :

```py
from google.appengine.ext import vendor

# Ajoutez les bibliothèques installées dans le dossier "lib".
vendor.add('lib')
```

Contenu de requirements.txt :

```javascript
Flask
Werkzeug
```

Maintenant, dans notre environnement virtuel **(assurez-vous que votre virtualenv est activé)**, nous allons installer les nouvelles dépendances que nous avons dans requirements.txt. Exécutez cette commande :

```bash
pip install -t lib -r requirements.txt
```

**\-t lib :** Ce drapeau copie les bibliothèques dans un dossier lib, qui est téléchargé sur App Engine lors du déploiement.

**\-r requirements.txt :** Indique à pip d'installer tout ce qui se trouve dans requirements.txt.

### Déploiement de l'Application

Pour déployer l'application sur Google App Engine, utilisez cette commande.

```bash
gcloud app deploy
```

J'inclus généralement — **project [ID du Projet]**

Cela spécifie le projet que vous déployez. La commande ressemblera à ceci :

```bash
gcloud app deploy --project [ID du Projet]
```

### L'Application

Maintenant, vérifiez l'URL de votre application. L'application sera stockée de la manière suivante :

```bash
"votre id de projet".appspot.com
```

Mon application est ici : [http://sal-flask-tutorial.appspot.com](http://sal-flask-tutorial.appspot.com)

## Conclusion

Grâce à ce tutoriel, vous avez tous appris à :

* Utiliser le framework appelé Flask pour utiliser Python comme langage côté serveur.
    
* Apprendre à utiliser HTML, CSS et Flask pour créer un site web.
    
* Apprendre à créer des environnements virtuels en utilisant virtualenv.
    
* Utiliser Google App Engine Standard Environment pour déployer une application dans le cloud.
    

#### **Ce que j'ai appris**

J'ai appris trois choses importantes de ce petit projet.

**Premièrement, j'ai appris la différence entre un site web statique et une application web**

**Sites Web Statiques :**

* Cela signifie que le serveur sert des fichiers HTML, CSS et JavaScript au client. Le contenu du site ne change pas lorsque l'utilisateur interagit avec lui.
    

**Applications Web :**

* Une application web ou un site web dynamique génère du contenu basé sur des données récupérées (la plupart du temps à partir d'une base de données) qui change en fonction de l'interaction de l'utilisateur avec le site. Dans une application web, le serveur est responsable de l'interrogation, de la récupération et de la mise à jour des données. Cela rend les applications web plus lentes et plus difficiles à déployer que les sites web statiques pour des applications simples ([Reddit](https://www.reddit.com/r/Python/comments/1iewqt/deploying_static_flask_sites_for_free_on_github/)).
    

**Côté Serveur et Côté Client :**

* J'ai appris qu'une application web a deux côtés. Le côté client et le côté serveur. Le côté client est ce avec quoi l'utilisateur interagit et le côté serveur est où toutes les informations que l'utilisateur a saisies sont traitées.
    

**Deuxièmement, j'ai appris les Services Cloud**

La plupart de mes projets précédents étaient des sites web statiques, et pour les déployer, j'ai utilisé [GitHub Pages](https://pages.github.com/). GitHub Pages est un service d'hébergement de sites statiques gratuit conçu pour héberger des projets à partir d'un dépôt GitHub.

Lorsque je travaillais avec des applications web, je ne pouvais pas utiliser GitHub Pages pour les héberger. GitHub Pages est uniquement destiné aux sites web statiques, pas à quelque chose de dynamique comme une application web qui nécessite un serveur et une base de données. J'ai dû utiliser des services cloud tels que [Amazon Web Services](https://aws.amazon.com/) ou [Heroku](https://www.heroku.com/)

**Troisièmement, j'ai appris à utiliser Python comme langage côté serveur**

Pour créer le côté serveur de l'application web, nous avons dû utiliser un langage côté serveur. J'ai appris que je pouvais utiliser le framework appelé Flask pour utiliser Python comme langage côté serveur.

#### **Prochaines Étapes :**

Vous pouvez construire toutes sortes de choses avec Flask. J'ai réalisé que Flask aide à rendre le code derrière le site web plus facile à lire. J'ai créé les applications suivantes pendant l'été 2018 et j'espère en créer d'autres.

Projets Personnels

* [Une Application SMS Twilio](http://twilio-pokedex.appspot.com/)
    
* [Mon Site Web Personnel](http://salvador-villalon.appspot.com/)
    

Pendant mon stage

* [Partie d'un projet où j'ai appris Docker et les Conteneurs](http://spgi2018-container-project.appspot.com/)
    

Voici la liste des ressources qui m'ont aidé à créer ce tutoriel :

* "App Engine — Construire des Backends Web et Mobile Scalables dans N'importe Quel Langage | App Engine | Google Cloud." *Google*, Google, [cloud.google.com/appengine/](https://cloud.google.com/appengine/).
    
* "Créer un Site Web avec Python Flask." *PythonHow*, [pythonhow.com/building-a-website-with-python-flask/](https://pythonhow.com/building-a-website-with-python-flask/).
    
* "Flask — Conférence 2 — Programmation Web avec Python et JavaScript de CS50." *YouTube*, 6 févr. 2018, [youtu.be/j5wysXqaIV8](https://youtu.be/j5wysXqaIV8).
    
* "Commencer avec Flask sur l'Environnement Standard App Engine | Environnement Standard App Engine pour Python | Google Cloud." *Google*, Google, [cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env).
    
* "Installation." *Bienvenue | Flask (Un Microframework Python)*, [flask.pocoo.org/docs/0.12/installation/](http://flask.pocoo.org/docs/0.12/installation/).
    
* "Python — Déployer des Sites Flask Statiques Gratuitement sur les Pages GitHub." *Reddit*, [www.reddit.com/r/Python/comments/1iewqt/deploying_static_flask_sites_for_free_on_github/.](http://www.reddit.com/r/Python/comments/1iewqt/deploying_static_flask_sites_for_free_on_github/.)
    
* Real Python. "Environnements Virtuels Python : Un Primer — Real Python." *Real Python*, Real Python, 7 août 2018, [realpython.com/python-virtual-environments-a-primer/](https://realpython.com/python-virtual-environments-a-primer/).
    
* "Qu'est-ce que les Services Cloud ? — Définition de WhatIs.com." *SearchITChannel*, [searchitchannel.techtarget.com/definition/cloud-services](https://searchitchannel.techtarget.com/definition/cloud-services).
    
* "Qu'est-ce que Google App Engine (GAE) ? — Définition de Techopedia." *Techopedia.com*, [www.techopedia.com/definition/31267/google-app-engine-gae.](http://www.techopedia.com/definition/31267/google-app-engine-gae.)
    

Si vous avez des suggestions ou des questions, n'hésitez pas à laisser un commentaire.