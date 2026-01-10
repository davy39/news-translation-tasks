---
title: Comment utiliser Python et Flask pour créer une application web — un tutoriel
  approfondi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-19T06:09:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-python-and-flask-to-build-a-web-app-an-in-depth-tutorial-437dbfe9f1c6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YBU3f_vPFza9Xk4-X9rzNw.png
tags:
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser Python et Flask pour créer une application web — un tutoriel
  approfondi
seo_desc: 'By Abhinav Suri

  Python is an incredibly versatile language. It’s considered to be a staple of modern
  development. It’s used for the simplest of scripts to complex machine learning and
  neural network training algorithms.

  But perhaps the less-known usa...'
---

Par Abhinav Suri

Python est un langage incroyablement polyvalent. Il est considéré comme un pilier du développement moderne. Il est utilisé aussi bien pour les scripts les plus simples que pour des algorithmes complexes d'apprentissage automatique et d'entraînement de réseaux neuronaux.

Mais l'utilisation peut-être la moins connue de Python est son usage en tant que serveur web. Éclipsé par des frameworks plus populaires tels que Node/Express et Ruby on Rails, Python est souvent négligé comme choix de serveur web par la plupart des développeurs.

Avoir un backend écrit en Python est vraiment utile pour plusieurs raisons, parmi lesquelles :

* Il est facile de passer de l'apprentissage de Python comme langage de script classique à son utilisation pour créer un backend.
* C'est le meilleur choix si vous prévoyez de servir des parties de votre application déjà écrites en Python (Par exemple : soumettre un formulaire, évaluer une entrée via un modèle Tensorflow et renvoyer le résultat à l'utilisateur).
* Il possède un écosystème diversifié de packages et d'outils pour vous aider dans le développement, sans oublier une formidable communauté de développeurs (puisque le langage existe depuis très longtemps).

Le but de cet article est de démontrer comment Python peut être utilisé pour créer une application web full stack. Dans ce tutoriel, j'utiliserai Flask, un « microframework » Python, pour développer une application web.

Je m'en voudrais de ne pas mentionner qu'il existe d'autres frameworks Python plus populaires comme Django, mais Flask est utile pour le développeur en herbe car il est minimaliste et oblige les développeurs à créer ou utiliser les composants dont ils ont besoin au sein de l'App en fonction de leurs exigences (plutôt que d'appeler un outil en ligne de commande qui génère 20 fichiers automatiquement... je te regarde, Ruby on Rails). Bien sûr, je ne vais pas expliquer comment démarrer une application web totalement de zéro, je vais plutôt vous donner une introduction à Flask puis passer à la façon dont vous pouvez utiliser un projet appelé flask-base pour gagner du temps à l'avenir.

### Intro à Flask

Flask est un microframework (comprenez : il n'est pas livré avec grand-chose) pour le développement web en Python. Avant de plonger dans le vif du sujet, couvrons quelques concepts de base du développement backend.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AHN-uIv1sIOnNe2k7C7GZw.png)
_Source : flask.pocoo.org_

### Routes

Imaginez que vous visitez `apple.com` et que vous voulez aller dans la section Mac à l'adresse `apple.com/mac/`. Comment les serveurs d'Apple savent-ils qu'ils doivent vous servir la page spécifique affichant les détails sur les appareils Mac ? C'est très probablement parce qu'ils ont une application web tournant sur un serveur qui sait que lorsque quelqu'un cherche `apple.com` et va dans la section `/mac/` du site, il doit gérer cette requête et renvoyer certaines pages. La logique consistant à déterminer quoi faire quand quelqu'un va sur `/mac/` est gérée par une **route**.

Ainsi, quand je visite `apple.com` (ce qui implique `apple.com/`), la route `/` gère ce qui est affiché. Si je vais sur `apple.com/purchase`, il y a une route `/purchase`. Si je vais sur `apple.com/purchase/1` où `1` est un identifiant d'article, il y a très probablement un gestionnaire de route générique `/purchase/<int:item-id>` qui gère cette requête. Les routes peuvent également gérer les requêtes GET et POST.

### Application de base

Alors, comment créer une application Flask de base avec des routes ? Eh bien, jetons un coup d'œil à la documentation. Créez un fichier Python appelé `hello.py` contenant ce qui suit :

```py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	# Renvoie la chaîne Hello World
	return "Hello World"
```

Analysons ce qui se passe ici :

1. Nous importons notre dépendance Flask.
2. Nous créons une instance d'une App Flask. L'argument passé à l'instanciateur Flask (`__name__`) s'évalue en une chaîne qui "nomme" l'App Flask. Lorsqu'elle est exécutée depuis la ligne de commande, `__name__ == "__main__"`. Vous pouvez définir le premier argument comme vous le souhaitez.
3. Nous configurons une route `[/](http://blah.com/)` sur notre App qui exécute la fonction `[hello(](http://blah.com/))` immédiatement en dessous lorsque cette route est visitée. Notez que la fonction doit renvoyer une chaîne ou un template rendu.

Sur la ligne de commande, configurons ce qu'on appelle un environnement virtuel (cela nous aidera à isoler notre environnement de développement et les installations de packages du reste de notre système).

1. Si ce n'est pas déjà fait, installez pip via `easy_install pip` (vous devrez peut-être utiliser `sudo` si vous êtes sur Mac).
2. Exécutez `pip install virtualenv` pour installer virtualenv via pip.
3. Dans le répertoire de votre App, créez votre environnement virtuel en exécutant `virtualenv venv` (cela crée un environnement virtuel dans un dossier appelé `venv` du répertoire courant).
4. Exécutez `source venv/bin/activate` pour activer l'environnement virtuel. C'est spécifiquement requis pour y installer des packages. Vous pouvez désactiver l'environnement virtuel en exécutant `deactivate` depuis la ligne de commande. C'est assez simple.

Maintenant que notre environnement virtuel est installé et activé, installons Flask. C'est très simple, exécutez juste `pip install Flask`. Nous pouvons ensuite lancer l'exemple précédent en écrivant ceci dans notre terminal :

```py
FLASK_APP=hello.py flask run
```

Vous devriez voir quelque chose comme `* Running on http://localhost:5000/` dans votre terminal. Et si vous visitez ce lien dans votre navigateur, vous verrez une page affichant simplement `Hello World`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R5tXaIavSyLU-AAjYbhEZQ.png)

### Application d'exemple : Penn Club Review

_Note : Le code de ce projet se trouve sur [ce dépôt GitHub](https://github.com/abhisuri97/penn-club-ratings)._

Maintenant, trouvons un projet à créer afin de démontrer toutes les capacités de Flask. Un projet récent que j'ai conçu est une application d'évaluation de clubs appelée « PennClubReview ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*JB2JUMBqQ0XtUhHW90vrmg.png)

Je suis actuellement étudiant à l'Université de Pennsylvanie. L'un des problèmes les plus courants auxquels les nouveaux étudiants sont confrontés est de choisir les clubs à rejoindre sur le campus. Ce processus est d'autant plus complexe que certains clubs sont très sélectifs, comportent plusieurs cycles d'entretiens et exigent un investissement temporel important. Souvent, aucun de ces aspects n'est abordé lors des sessions d'information des clubs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n2bqJ6Q5a77Ys25QHsn51w.jpeg)
_Foire aux clubs de l'UPenn_

Ainsi, pour remédier à ce problème, nous pouvons créer une application où :

* Un administrateur peut définir des questions de sondage auxquelles les utilisateurs répondront à propos des clubs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kH6bClToQcIBi0-Mv43ytA.png)

* Les utilisateurs peuvent voir les notes moyennes pour chaque question de sondage pour chaque club.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QcXVN_FGxJHMSFLPWYIxdw.png)

* Les utilisateurs peuvent voir les réponses individuelles pour les clubs. Si un utilisateur choisit de soumettre un autre avis, sa réponse précédente est écrasée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3MezfoNWhhApiWDDc2GCEQ.png)

* Les utilisateurs peuvent suggérer des clubs que les administrateurs pourront modifier/approuver pour les afficher publiquement (les administrateurs doivent être informés par e-mail lorsque cela se produit).

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Zno4pimA9vju_urGfzrbQ.png)

* Un utilisateur ou un administrateur doit pouvoir modifier ses propres informations de compte.
* Un administrateur doit avoir la possibilité d'ajouter/supprimer des utilisateurs, des questions de sondage, des catégories de clubs et des clubs du système.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4V0lieTFYeLvurHNX4LLXA.png)

### Décomposition des composants de l'application

Pour développer cette application, nous aurons besoin de composants supplémentaires en plus de Flask, tels qu'une base de données de support, un système de gestion des connexions, un moyen d'organiser les routes et la gestion des e-mails. Nous *pourrions* coder cela de zéro. Mais il existe déjà un excellent boilerplate qui peut vous offrir un très bon point de départ.

### Présentation de Flask-Base

![Image](https://cdn-media-1.freecodecamp.org/images/1*V5DYt-I1jIsvt37qGCR2Ug.png)

Flask-base est un projet que mes amis et moi avons développé dans le cadre d'une organisation à but non lucratif gérée par des étudiants appelée [Hack4Impact](https://hack4impact.org/). Nous travaillons avec des organisations à but non lucratif pendant un semestre pour développer des projets techniques qui les aident à accomplir leur mission.

En travaillant sur tant de projets, nous avons réalisé que nous répétions souvent le même code dans toutes nos applications. Nous avons donc décidé de créer une base de code unique contenant les parties les plus communes dont toute App que nous créons aurait besoin. Cette base de code inclurait :

* Un schéma d'authentification des utilisateurs
* La gestion des comptes
* Des Blueprints (pour gérer les routes)
* Une base de données de support
* L'envoi d'e-mails (avec une file d'attente Redis)

Il est récemment devenu assez populaire, récoltant plus de 1200 étoiles sur GitHub en quelques mois. Cette base de code est parfaite pour ce que nous essayons de mettre en place. Vous pouvez trouver le dépôt GitHub contenant le code de Flask-base [ici](https://github.com/hack4impact/flask-base).

### Configuration du développement de l'application

D'abord, clonons flask-base. Suivez les instructions sur la page README.md. En résumé, exécutez ce qui suit :

```py
git clone https://github.com/hack4impact/flask-base.git

cd flask-base

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py recreate_db

python manage.py setup_dev
```

D'accord. Je vais détailler ce que nous avons fait ici :

* Cloner le dépôt depuis GitHub (c'est-à-dire le télécharger) puis entrer dans son répertoire.
* Créer un nouvel environnement virtuel et l'activer.
* Lire les dépendances de packages dans le fichier `requirements.txt` et les installer toutes via `pip`.
* Instancier la base de données (la recréer) et insérer également une règle d'administrateur (via setup_dev).

De plus, créons une migration de base de données active. Cela permettra de suivre les changements dans nos modèles de base de données sans avoir besoin de recréer notre base de données (c'est-à-dire supprimer toutes les informations puis reconstruire la base de données de zéro). Les migrations nous permettent de préserver les informations. Nous pouvons le faire via la commande ci-dessous.

Pour lancer l'App, exécutez `honcho start -f Local` (vous devrez installer Honcho si ce n'est pas déjà fait). Si vous rencontrez des problèmes, il y a de fortes chances qu'ils aient déjà été abordés dans le README de flask-base. Maintenant, vous pouvez visiter `localhost:5000` et accéder à une application flask-base fonctionnelle.

Pour vous connecter à l'App en tant qu'administrateur, allez sur le lien de connexion et saisissez comme nom d'utilisateur `flask-base-admin@example.com` avec le mot de passe `password`. Vous pouvez ensuite inviter de nouveaux utilisateurs dans l'application depuis l'écran d'administration. Notez qu'avant de faire cela, vous devrez créer un fichier `config.env` contenant les deux variables suivantes :

```
MAIL_PASSWORD=unMotDePasseSendGrid
MAIL_USERNAME=unUtilisateurSendGrid
```

Lors de la création d'un compte utilisateur, le compte reste non confirmé jusqu'à ce que le nouvel utilisateur invité clique sur un lien envoyé à son e-mail. De plus, un utilisateur peut s'inscrire à l'App et passera par un flux d'authentification similaire concernant la confirmation.

Consultez la documentation de flask-base pour avoir une meilleure idée de certaines de ses capacités prêtes à l'emploi. Pour l'instant, nous allons passer à la façon dont nous pouvons l'utiliser pour créer notre App.

### Bases de données !

![Image](https://cdn-media-1.freecodecamp.org/images/1*nyIxZDJIv4TwxOI00Lyu0A.png)

Toute notre logique de base de données est enveloppée par l'ORM SQLAlchemy, nous n'avons donc pas à écrire des instructions de base de données très verbeuses pour exécuter des requêtes ou ajouter/supprimer des enregistrements. Tous les *modèles* de base de données (considérez-les comme des classes) sont contenus dans le dossier `app/models`. Réfléchissons aux modèles nécessaires pour l'application elle-même.

Nous avons besoin d'un modèle `Club` qui contient le `name` du club (Type : String), une `description` du club (Type : Text) et une variable `is_confirmed` (Type : Boolean) pour savoir si un club suggéré a été approuvé par un administrateur pour être affiché. De plus, nous voulons un moyen de se référer aux catégories d'un club, et un autre moyen de se référer aux réponses aux questions qui appartiennent à un club.

Réfléchissons à la relation entre les Clubs et les Catégories de clubs. Nous pouvons la voir ainsi : un club a plusieurs catégories (par exemple, un club peut être un club d'« Impact Social » et de « Tech ») et une catégorie de club peut appartenir à plusieurs clubs (par exemple, il peut y avoir plusieurs clubs « Tech » sur le campus). Le seul attribut de ce `ClubCategory` est un `category_name` (Type : String).

Nous pouvons créer cette relation (une relation plusieurs à plusieurs) via une table d'association.

### Club et catégories de club (Plusieurs à plusieurs)

Maintenant, comment encoder cette logique dans flask-base ? Tout d'abord, créez un fichier appelé `club.py` dans `app/models`. Créons d'abord les modèles `Club` et `ClubCategory`.

Nous avons maintenant deux modèles, mais ils ne sont pas connectés l'un à l'autre. Chacun a des attributs individuels, mais aucun ne peut être explicitement relié à l'autre. Nous faisons la connexion via une association comme je l'ai mentionné plus tôt. Après l'import de `db`, ajoutez les lignes suivantes.

Cela crée une nouvelle table d'association (un intermédiaire entre le modèle Club et ClubCategory). Il y a deux colonnes dans cette table, `club_id` et `club_category_id`, qui se réfèrent aux identifiants respectifs de leurs modèles (notez que l'attribut `id` est une clé primaire au sein de chaque modèle, c'est-à-dire l'élément unique pour chaque enregistrement). Mais au sein de la table d'association, nous nous référons à ces clés primaires comme des clés étrangères (car elles font référence à d'autres tables). De plus, nous devons ajouter une ligne au modèle `Club` en bas.

```
categories = db.relationship('ClubCategory', secondary=club_category_assoc, backref='clubs')
```

Et cela crée réellement la relation bidirectionnelle entre les modèles `Club` et `ClubCategory` et configure une relation entre `Club` et `ClubCategory` en utilisant la table d'association `club_category_assoc`. Le `backref` indique au modèle `ClubCategory` comment se référer aux modèles `Club`. Ainsi, avec un club donné `club`, vous pouvez exécuter `club.categories` pour obtenir un tableau d'objets catégories. Avec une `ClubCategory` donnée appelée `category`, vous pouvez obtenir tous les clubs de cette catégorie en faisant `category.clubs`.

Vous pouvez voir cela en action en faisant ce qui suit :

Dans `app/models/__init__.py`, ajoutez la ligne correspondante.

Et lancez ensuite `python manage.py shell`. Exécutez les commandes suivantes pour interagir avec vos modèles de base de données (notez que `>>>` indique une entrée que vous saisissez).

### Questions et réponses (Plusieurs à un)

Super ! Nous avons maintenant des modèles Club et ClubCategory fonctionnels. Passons maintenant aux modèles `Question` et `Answer`. Pour une question, nous devons suivre le `content` de la question qui sera une chaîne contenant le texte de la question elle-même. Nous inclurons également un attribut `max_rating` qui contiendra la note maximale qu'un individu peut donner pour la question. Par exemple, si le contenu de la question est « Notez la communauté du club, 10 étant le meilleur », nous pourrions définir `max_rating` à 10. De plus, nous suivrons un booléen `free_response` pour déterminer si nous permettrons aux gens d'inclure une réponse supplémentaire facultative sous forme longue. Enfin, nous devrons avoir une relation avec le modèle `Answer`. Ce sera une relation un à plusieurs car une question peut avoir plusieurs réponses mais une réponse ne peut avoir qu'une seule question.

Le modèle `Answer` aura les attributs suivants :

* un attribut `answer` correspondant à la réponse textuelle libre d'une réponse (si la question permet une réponse textuelle libre)
* une `rating` allant de 1 jusqu'à la note maximale pour la question
* un `user_id` lié à l'utilisateur qui a écrit la question (encore une fois, un utilisateur peut avoir plusieurs réponses, mais une réponse ne peut avoir qu'un seul utilisateur)
* un `question_id` se référant à la `question` à laquelle la réponse appartient
* un `club_id` se référant au `club` auquel la réponse appartient

Créons un fichier `question.py`.

La plupart des éléments ici sont assez simples, sauf pour la dernière ligne. La dernière ligne connecte les modèles `Question` et `Answer`. Elle dit de configurer une relation avec le modèle `Answer` qui peut se référer au modèle `Question` via le mot-clé `question`. Étant donné une réponse `a`, vous pouvez obtenir la question via `a.question` et étant donné une question `q`, vous pouvez obtenir les réponses qui lui sont associées via `q.answers`. Configurons maintenant le modèle `Answer`. Créez un nouveau fichier appelé `answer.py` dans le dossier models et collez-y ce qui suit.

Ce fichier est beaucoup plus long, mais rappelez-vous qu'une réponse est liée à beaucoup de choses. Commençons par le début, notez que `question_id` se réfère au modèle `Question` via la clé étrangère `questions.id` (la colonne `id` de la table `questions` qui contient les enregistrements des instances du modèle `Question`).

Notez que nous avons également une colonne `user_id` qui se réfère à un utilisateur. Allons dans `user.py` dans le dossier `app/models` et ajoutons la ligne suivante après la déclaration de `role_id`.

Cette instruction utilise une syntaxe très similaire à celle du modèle `Question`.

Notez également qu'il y a un attribut `club_id` qui se réfère au club auquel la réponse est associée. Modifiez le fichier `club.py` pour inclure la ligne suivante comme dernier attribut du modèle `Club`.

Enfin, ajoutez ces deux lignes à `__init__.py` dans `app/models`.

Et maintenant nous devrions pouvoir jouer avec nos bases de données comme suit.

Enfin, abordons la méthode `newAnswer`. Cette méthode est utilisée pour insérer de nouvelles réponses dans la base de données tout en s'assurant que si un utilisateur a déjà répondu à cette question, nous la supprimons et insérons la nouvelle réponse.

Encore une fois, nous pouvons lancer `python manage.py shell`.

Voilà, nous en avons fini avec les modèles :)

### Vues

Maintenant que la partie base de données est réglée, créons le moyen pour les utilisateurs d'interagir avec l'application elle-même. Commençons par configurer quelques blueprints.

### Blueprints

Les Blueprints sont un excellent moyen d'organiser votre application Flask. Ils vous permettent de regrouper toutes les routes associées entre elles dans un seul fichier. Par exemple, toutes les actions associées à un compte, telles que la gestion du compte, la réinitialisation du mot de passe utilisateur, le mot de passe oublié, etc., seraient incluses dans le blueprint `account`.

Chaque blueprint a un dossier associé sous `app`. Par exemple, il y a un dossier `account/` et un dossier sous `templates` contenant les templates HTML réels qui seront rendus à l'utilisateur.

Ajoutons quelques blueprints. Avant la ligne `return app` de `app/__init__.py`, ajoutez ce qui suit.

Ces appels créent des blueprints montés respectivement aux préfixes d'URL `/club`, `/question` et `/category`. Créons les dossiers `club`, `question` et `category` pour chacun des blueprints. Dans chacun des dossiers, créez les fichiers `__init__.py`, `forms.py` et `views.py`.

### Formulaires et vues de club

Je vais vous expliquer comment configurer les vues/templates pour le blueprint `club`. Les autres vues sont assez faciles à comprendre à partir du code.

Ainsi, dans la vue club, nous voulons afficher plusieurs choses :

1. Si vous êtes administrateur, vous devriez pouvoir créer un club et lui donner un nom, une description et des catégories.
2. Si vous êtes administrateur, vous devriez pouvoir voir tous les clubs, y compris ceux qui ne sont pas confirmés.
3. Si vous êtes administrateur ou utilisateur, vous devriez pouvoir voir les informations d'un club individuel.
4. Si vous êtes administrateur, vous devriez pouvoir modifier les informations d'un club et supprimer un club.

Créons d'abord quelques formulaires dans `forms.py` que nous passerons ensuite à nos vues, spécifiquement la vue qui gère la création d'un nouveau club et celle qui modifie les informations du club.

Dans `forms.py` pour `club`, ajoutez les lignes suivantes :

Flask-base utilise `wtforms` pour créer des formulaires. wtforms nous permet de créer des formulaires de manière orientée objet où chaque formulaire est une classe.

Nous créons donc deux formulaires, l'un appelé `NewClubForm` qui étend la classe de base `Form` de `wtforms`, et possède 3 champs - `name` (Type : Text), `desc` (Type : Text) contenant la description du club, et `categories` (un menu déroulant à sélection multiple). Avec le champ `categories`, nous interrogeons le modèle `ClubCategory` avec une fonction Lambda (qui est fondamentalement une fonction anonyme) pour obtenir les noms de catégories et remplir les options du champ de sélection de catégorie avec les résultats de cette requête.

Enfin, nous avons un champ `submit`, pour que le bouton de soumission puisse être rendu.

Ensuite, nous avons un `EditClubForm` qui étend l'ensemble de champs de `NewClubForm` en ajoutant un nouveau champ appelé `is_confirmed`. Rappelez-vous que `is_confirmed` dans notre modèle `Club` détermine si l'instance de club donnée peut être affichée ou non au public. Nous ajouterons la fonction permettant aux utilisateurs de suggérer un club, et par défaut, les clubs suggérés sont masqués jusqu'à ce qu'ils soient approuvés par un administrateur. Nous écrasons également le champ `submit` pour afficher le texte "Modifier le club".

Dans `views.py` sous `club/`, nous créons quelques routes.

* `/new-club` (GET, POST) ACCÈS CONNECTÉ : Rend et accepte les données du formulaire pour créer un nouveau club.
* `/clubs` (GET) ACCÈS ADMIN : Affiche tous les clubs.
* `/<int:club_id>/` (:info) (GET) ACCÈS CONNECTÉ : Rendra les infos pour une instance de club donnée avec `id = club_id` et on peut accéder à la route via /club/1 ou /club/1/info.
* `/<int:club_id>/change-club-details` (GET, POST) ACCÈS ADMIN : Rend et accepte les données du formulaire pour modifier les informations du club.
* `/<int:club_id>/delete` (GET) ACCÈS ADMIN : Rend la page pour supprimer le club.
* `/<int:club_id>/_delete` (GET) ACCÈS ADMIN : Supprime le club avec l'ID spécifié.

Pour la première route `/new-club`, nous voulons également permettre aux utilisateurs réguliers de créer un nouveau club, c'est pourquoi nous ne protégeons l'accès que par connexion. Voyons comment créer une route pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yFgliJzFFPNOzZzIouynrg.png)

Analyse du code. À la ligne 1, nous déclarons où la route sera accessible. Par exemple, elle sera sur le blueprint `club` à la sous-route `/new-club`. L'URL complète pour y accéder est `domainedebase.com/club/new-club`.

Nous plaçons ensuite un décorateur de route `@login_required` sur la route ; ce décorateur renverra une erreur 403 si l'utilisateur n'est pas connecté, mais lui permettra de voir la route s'il est connecté.

Ensuite, nous définissons une méthode pour gérer les requêtes vers la route (notez que ce nom doit être unique). Cette méthode peut être référencée par `club.new_club` dans le templating Jinja.

Nous instancions ensuite notre `NewClubForm` créé précédemment. Dans la ligne suivante, nous vérifions si la soumission du formulaire était valide (notez que cette route acceptera également les requêtes POST) via la méthode `form.validate_on_submit()`. Si c'est le cas, nous créons une nouvelle instance de `Club` avec `name`, `description` et `categories` correspondant aux champs du formulaire. Notez que pour `is_confirmed`, nous le définissons selon que l'utilisateur actuel est un administrateur ou non (car si un utilisateur régulier soumet ce formulaire, nous voulons que le nouveau club n'apparaisse pas à tout le monde, donc nous définissons `is_confirmed` sur False). Nous ajoutons ensuite la nouvelle instance de club à la session de base de données et validons (commit) la session.

Enfin, si l'utilisateur qui soumet le formulaire n'est pas un administrateur, nous générons un lien à envoyer à l'administrateur du formulaire par e-mail. Ce lien doit mener directement à la route admin `change_club_details` qui permettra à l'admin de basculer `is_confirmed`. Nous parcourons ensuite la base de données pour tous les utilisateurs ayant un rôle d'administrateur et ajoutons une tâche d'envoi d'e-mail à notre file d'attente Redis. Dans la méthode `get_queue()`, nous mettons en file d'attente le travail `send_email` spécifiquement, en définissant le destinataire sur l'e-mail de l'admin, le sujet égal à...

ajoutez l'instance de club (à utiliser comme variable de template) et le lien (également à utiliser comme variable de template).

Nous passons également le `template` que nous créons dans `app/templates/club/email/suggested_club.html` et `.txt`. Le contenu est le suivant pour le fichier HTML :

et pour le fichier .txt

![Image](https://cdn-media-1.freecodecamp.org/images/1*36XzqKy9_c55E3DW5sCmHw.png)

Ensuite, nous nous occuperons de la route `/clubs` qui affiche tous les clubs dans un tableau. Pour le gestionnaire de route, nous pouvons simplement passer tous les clubs dans un template.

Et le template de club que nous rendons est situé à `app/templates/club/clubs.html` avec le contenu suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mg_VlCs8G3iXdVjSWbMqnw.png)

La plupart de ceci est assez simple si vous connaissez Jinja (ou n'importe quel langage de template). Fondamentalement, la boucle for `{% for c in clubs %} ... {% endfor %}` passera en revue tous les clubs et pour chaque club, elle rendra le nom du club `{{ c.name }}` et les catégories du club.

Notez que pour chacun des clubs rendus, nous incluons également une ligne :

Cela renvoie à la page d'info individuelle du club pour l'instance de club donnée qui est rendue. Passons à la création de cette route.

Notez que pour cette vue, nous n'avons besoin de passer que les informations de l'instance de club à la vue manage_club. Nous pouvons le faire facilement via :

Nous pouvons également configurer quelques autres routes car notre page `manage_club.html` affiche en réalité plusieurs routes.

Configurons la route `/change-club-details` qui rend et accepte simplement les infos du formulaire `EditClubForm`.

Notez que lors de l'enregistrement du champ `club.is_confirmed`, nous devons convertir les valeurs de chaîne `True` et `False` en leurs équivalents booléens comme indiqué dans la spécification `forms.py` pour `EditClubForm`. Nous le faisons via une fonction personnalisée `bool` définie comme suit :

Le `bool` par défaut de Python renverra `True` si n'importe quelle chaîne est définie, y compris `'False'`, d'où la nécessité de définir notre propre fonction.

Nous définissons également `delete` pour rendre la page de suppression et la fonction `_delete` qui supprime réellement l'instance de club.

Notez que pour la route `_delete`, nous avons une redirection vers la route `clubs` qui liste toutes les instances de club.

Passons maintenant au template `manage_club.html` à l'adresse `app/templates/club/manage_club.html`. Son contenu est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*x7grARvAt4ViUuSXMSogHA.gif)

Analysons ce fichier. Sur la première ligne, nous étendons simplement notre mise en page de base (layout), puis nous importons les macros de formulaire. Les macros sont essentiellement des méthodes dans Jinja.

Nous avons une variable `endpoints` qui contiendra des liens vers les différentes parties de la page de gestion. Dans la macro `navigation`, nous rendons tous les éléments individuels de la liste dans `endpoints`.

Nous créons également une macro `club_info` qui contiendra les informations relatives au club et toutes les réponses associées au club en faisant ce qui suit.

Enfin, nous écrivons réellement la logique pour rendre la page à l'intérieur des balises `{% block content %} ... {% endblock %}`. Nous basculons entre les sous-pages à rendre en vérifiant le `request.endpoint` pour voir s'il s'agit du point de terminaison de suppression ou s'il y a un formulaire (auquel cas on rend le formulaire). Sinon, nous appelons simplement la macro `club_info`. Et nous en avons fini avec les routes et vues de club. La plupart des autres routes pour les catégories et les questions suivent une logique similaire.

### Vues et formulaires principaux

La route principale est la partie publique de l'application. Les comportements des routes sont les suivants :

* / (GET) : affiche tous les clubs, les questions associées et les notes moyennes pour chaque club par question dans un tableau.
* /submit-review/<int:club_id> (GET, POST) : Génère dynamiquement le formulaire pour soumettre un avis sur un club basé sur les questions de la base de données `Question`. Accepte également les données du formulaire et les enregistre comme réponses pour le club correspondant à club_id.

La première route est très simple et correspond à la route `/clubs` que nous avons implémentée plus tôt. La seule différence est que les `questions` doivent également être transmises.

La partie la plus intéressante ici est la façon de calculer la note moyenne et de la passer à la route. Je crée une liste appelée `all_c` et pour chacun des clubs, je crée un `club_obj` contenant les informations de base du club. Pour chacune des réponses d'un club, j'ajoute une nouvelle propriété au `club_obj` correspondant au contenu de la question, si elle n'existe pas déjà. J'ajoute chacune des notes à une liste, puis je parcours chacune des propriétés du `club_obj`. Si la propriété a une valeur de type liste, je remplace cette liste par la moyenne des notes de cette liste. J'ajoute ensuite `club_obj` à `all_c` et je le passe au template.

#### Génération dynamique de formulaires

Pour la route `submit-review`, je dois créer un formulaire dynamiquement basé sur les questions que j'ai dans mon modèle `Question`. Le code est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*i2b9pI3LtmCIDHBVnrXc6w.png)

Nous créons d'abord une classe de formulaire factice qui hérite de la classe de base `Form`. Ensuite, pour chacune des questions, nous créons de nouveaux champs de formulaire `setattr(F, ...)` sur le formulaire factice `F`. La méthode `setattr` prend comme deuxième argument le nom du champ de formulaire. Nous le définissons sur l'ID de la question avec `_q` ajouté pour la note et `_resp` pour une réponse libre si indiqué. Pour le champ de formulaire de note, nous créons un `SelectField` avec des choix allant de 1 jusqu'à `max_rating`.

Pour gérer une soumission de formulaire, nous utilisons la même instruction if `form.validate_on_submit()` mais au lieu de chercher des champs nommés spécifiques du formulaire, nous parcourons tous les champs du `form` et créons une nouvelle réponse en utilisant la méthode `newAnswer`. Cette méthode supprimera toute réponse précédente avant d'en ajouter une nouvelle pour l'utilisateur s'il a déjà répondu pour ce club.

### Lancement

Maintenant que la majeure partie de l'App est terminée, nous pouvons lancer cette application sur Heroku.

Si vous ne vous êtes jamais inscrit sur Heroku :

1. Allez sur Heroku.com et créez un compte.
2. Installez la CLI.

Si vous n'avez pas configuré de dépôt git initialement, exécutez `git init` et connectez-vous avec votre compte Heroku.

Ensuite, faites un `git add` de tous les fichiers pertinents (c'est-à-dire tout sauf `config.env` et `venv/`) et exécutez `pip freeze > requirements.txt` pour vous assurer que toutes les dépendances que vous avez installées sont incluses.

Exécutez `heroku create` pour créer une nouvelle instance Heroku et lancez `git push heroku master` pour ajouter vos fichiers au dépôt Heroku.

Une fois que c'est fait, vous devrez définir certaines variables d'environnement avec la commande suivante :

Une fois cela fait, exécutez ce qui suit pour créer la base de données sur Heroku :

puis la commande suivante créera le compte administrateur :

Vous devrez également créer une instance Redis togo pour gérer la file d'attente des tâches :

et enfin lancez la commande suivante qui dira à Heroku de lancer un dyno (comprenez un sous-serveur) qui gère notre file d'attente Redis :

Vous pouvez ensuite exécuter `heroku open` pour ouvrir votre application Heroku en cours d'exécution dans une fenêtre séparée.

### Extension de l'application et conclusion

Il est assez facile de copier la structure actuelle de l'application et de l'étendre pour ajouter plus d'informations ou de routes à l'App. Il suffit de regarder n'importe laquelle des routes précédentes qui ont été implémentées. Si, pour une raison quelconque, vous souhaitez inclure un téléchargement de fichier quelconque, vous devrez intégrer l'App avec Amazon S3 si vous prévoyez de faire tourner l'application sur Heroku (puisqu'elle possède un système de fichiers éphémère).

Dans l'ensemble, flask-base offre un excellent point de départ pour créer votre application Flask. Bien sûr, le backend peut être assez verbeux à coder, mais en conséquence, il vous donne un contrôle très granulaire sur votre application.