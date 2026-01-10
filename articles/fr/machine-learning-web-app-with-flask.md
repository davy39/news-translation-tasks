---
title: Comment transformer votre Jupyter Notebook en une application web conviviale
subtitle: ''
author: Tooba Jamal
co_authors: []
series: null
date: '2022-10-03T22:52:51.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-web-app-with-flask
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Purple-Illustrated-Technology-Blog-Banner-1.png
tags:
- name: deployment
  slug: deployment
- name: 'Jupyter Notebook '
  slug: jupyter-notebook
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment transformer votre Jupyter Notebook en une application web conviviale
seo_desc: "Being able to build predictive models is a superpower – but you can't make\
  \ much of these models if users can't use them. \nIn this article, we will go through\
  \ the process of building and deploying a machine learning web app using Flask and\
  \ PythonAnywh..."
---

Être capable de construire des modèles prédictifs est un super-pouvoir – mais vous ne pouvez pas tirer grand-chose de ces modèles si les utilisateurs ne peuvent pas les utiliser. 

Dans cet article, nous allons passer en revue le processus de construction et de déploiement d'une application web de machine learning en utilisant Flask et PythonAnywhere. 

Flask est un Framework web Python facile à utiliser, et PythonAnywhere est un service d'hébergement web fourni par Anaconda.

## Comment construire une application web de Machine Learning

L'idée de transformer vos modèles prédictifs en une application web peut sembler intimidante. Mais je vous promets que c'est relativement facile et direct. 

Voici les étapes que nous devrons suivre pour y parvenir :

1. Sauvegarder le modèle de machine learning
2. Construire une page web en utilisant HTML
3. Construire un Backend en utilisant Flask 
4. Le styliser comme vous le souhaitez
5. Le déployer sur le web

Je voulais construire une application web de prédiction du diabète et j'ai donc utilisé [ce](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.) jeu de données pour le faire. Vous pouvez utiliser n'importe quel jeu de données de votre choix, car le processus restera le même.

Avant de commencer, comprenons la structure du répertoire que nous allons suivre. Cela sera utile pour garder nos fichiers organisés et faciliter le déploiement.

### Structure du répertoire

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Untitled-Workspace.png)
_Structure du répertoire que nous allons suivre_

J'ai nommé mon répertoire racine diabetes_app, mais vous pouvez nommer le vôtre comme vous le souhaitez. 

Nous avons trois autres répertoires et un fichier Python dans diabetes_app (répertoire racine). Le répertoire Models contiendra notre modèle entraîné. Le répertoire Static contient deux autres répertoires : CSS contiendra toutes les feuilles de style sauvegardées et script contiendra les fichiers JavaScript, le cas échéant. Enfin, le dossier Templates contiendra les fichiers HTML sauvegardés et app.py est notre fichier Python qui contient le code du Backend (Flask).

Maintenant que nous avons une structure de fichiers organisée, commençons.

## Comment sauvegarder le modèle de Machine Learning

Sauvegarder le modèle est la plus facile de toutes les tâches. Nous utiliserons la bibliothèque Python pickle pour ce faire. 

Une fois que vous avez terminé l'entraînement, les tests et le réglage des hyperparamètres, sauvegardez le modèle le plus performant dans une variable. Pour moi, le meilleur modèle était RandomForestClassifier et je l'ai sauvegardé ainsi :

```python
clf = RandomForestClassifier()
clf.fit(X_train.values, y_train)
```

Maintenant, `clf` contient mon modèle RandomForestClassifier entraîné qui est prêt à être sauvegardé dans un fichier. Pour cela, je vais devoir importer la bibliothèque pickle et sauvegarder le clf comme ceci :

```python
import pickle
pickle.dump(clf, open('model.pkl', 'wb'))
```

pickle.dump() est une fonction utilisée pour sauvegarder des modèles. Le premier paramètre est le nom du modèle (clf dans notre cas) et le second est une autre fonction qui sauvegarde le modèle sur le disque. 'model.pkl' est le nom du fichier dans lequel je veux que mon modèle soit sauvegardé et 'wb' fait référence à _write binary_ (écriture binaire) qui écrit les données du modèle dans le fichier 'model.pkl'.

Après cette étape, vous aurez votre fichier de modèle sauvegardé dans le même répertoire que celui où vous travaillez. N'oubliez pas de copier le fichier model.pkl dans le dossier models de notre répertoire de projet. Et maintenant que nous avons sauvegardé notre modèle, nous sommes prêts à avancer.

## Comment construire une page web en utilisant HTML

La fonctionnalité principale de toute application web de machine learning est de faire des prédictions. Et pour cela, l'utilisateur devra très probablement répondre à quelques questions si vous n'avez pas utilisé de données non structurées ou téléchargé des documents dans d'autres cas. 

Le jeu de données de prédiction des risques de diabète au stade précoce est au format .csv avec 17 caractéristiques (dont 16 sont utilisées comme entrées). Nous utiliserons des formulaires HTML pour créer un formulaire qu'un utilisateur peut remplir pour obtenir ses prédictions. Par exemple :

```html
<form action="{{ url_for('predict')}}" method="post">
    <p>Quel est votre âge ?</p>
     <input type="number" name="Age" placeholder="Entrez votre âge" 			  		required="required" /><br> 
    <p>Quel est votre genre ?</p>
     <label><input type="radio" name="Sex" value="1" required="required" 		/>Homme</label>
        <label><input type="radio" name="Sex" value="0" required="required" 		/>Femme</label><br>
     <button type="submit">Prédire</button>
</form>
<p> {{ prediction }} </p>

```

Ci-dessus, nous avons créé un formulaire avec deux questions. L'attribut action du formulaire est défini sur `{{ url_for('predict') }}` ce qui affichera notre prédiction lorsque le formulaire sera soumis. Pour l'âge, nous fournissons à l'utilisateur un champ de saisie numérique, et pour le genre, nous avons des boutons radio. 

L'attribut value contient la valeur pour chaque bouton radio. Homme a la valeur 1 et femme a la valeur 0, qui seront utilisées comme entrées pour notre prédiction. Assurez-vous que chaque champ de saisie possède des attributs de valeur correspondant à votre jeu de données final (traité/prêt pour la prédiction). J'avais une caractéristique de genre encodée en binaire, j'ai donc utilisé les valeurs 1 et 0 pour le genre. 

La balise de paragraphe affichera les résultats de la prédiction. Prediction est une variable qui contiendra notre prédiction dans le fichier Python que nous verrons à l'étape suivante.    
Vous pouvez ajouter autant de questions que vous le souhaitez et n'importe quel type de saisie qui vous convient – la fonctionnalité restera la même.

## Comment construire le Backend en utilisant Flask

Nous en sommes maintenant à l'étape la plus intéressante, qui consiste à construire le Backend. Jetez d'abord un coup d'œil au code, puis nous l'approfondirons.

```python
import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]  
    prediction = model.predict(features) 
    result = prediction[0]

    return render_template('index.html', prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
```

Commencez par importer les bibliothèques dont nous allons avoir besoin. Nous aurons besoin de NumPy pour gérer les valeurs d'entrée, de Flask pour faire des prédictions, et de pickle pour charger le modèle que nous avons sauvegardé à la première étape.

Tout d'abord, nous créons notre objet app que nous utiliserons tout au long de la construction de notre Backend. Deuxièmement, nous chargeons notre modèle en utilisant la fonction pickle.load(). Cette fois, nous avons remplacé 'wb' par 'rb' qui signifie _'read binary'_ (lecture binaire), ce qui indique à pickle de lire les données. 

@app.route('/') signifie que nous sommes sur la page d'accueil de notre application et que nous voulons y faire quelque chose. Pour ce faire, nous définissons une fonction `home` qui affiche notre fichier HTML créé à l'étape précédente comme page d'accueil.

@app.route('/predict',methods=['POST']) effectue le travail principal en nous permettant de faire des prédictions. /predict signifie que nous nous sommes déplacés vers la page de prédiction de notre application. 

Nous définissons ici une fonction predict, à l'intérieur de laquelle nous stockons d'abord toutes les valeurs d'entrée dans un tableau appelé int_features en utilisant request.form.values(). Une fois que nous avons nos valeurs d'entrée, nous les convertissons en un tableau 2D pour la prédiction et effectuons la prédiction comme nous le faisons habituellement. Enfin, nous stockons la prédiction dans la variable prediction que nous utiliserons pour afficher le résultat sur notre application web. 

render_template('index.html', prediction=result) indique à Flask d'assigner le résultat à la variable prediction et de l'afficher dans notre fichier index.html. 

Rappelez-vous de l'attribut action défini sur predict dans notre HTML ? C'est la même fonction predict que nous avons définie ici. Lorsque l'utilisateur soumet le formulaire, la fonction predict est appelée. 

Enfin, nous lançons notre application dans les deux dernières lignes. debug=True est un argument optionnel (par défaut False) qui recharge automatiquement la page web lorsque vous apportez des modifications au code. Cela sera utile lorsque vous ferez le stylisme de votre application.

## Comment styliser l'application comme vous le souhaitez

Pour garder les choses simples, je vous ai montré la manière la plus simple de construire une application web de machine learning. Mais vous pouvez faire beaucoup plus avec elle. 

J'ai stylisé mon application en trois pages web distinctes pour l'accueil, le formulaire/questions et les résultats. J'ai également ajouté un peu de JavaScript pour afficher des actualités de santé aléatoires provenant du monde entier sur la page d'accueil et un peu de style pour rendre les choses jolies. 

La façon de lier les fichiers CSS et JavaScript lors de l'utilisation de Flask est la suivante :

```html
 <link rel="stylesheet" href="{{ url_for('static',filename='css/style.css') }}">
 <script type="text/javascript" 
  src="{{ url_for('static',filename='script/script.js') }}"></script>
```

Pour ajouter plus d'une page web, il vous suffit d'ajouter plus de routes au fichier Python comme nous l'avons fait à l'étape précédente. Supposons que nous voulions ajouter une page de résultats séparée pour afficher les prédictions. La route /predict ressemblera à ceci :

```python
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]  
    prediction = model.predict(features)  
    result = prediction[0]

    return render_template('results.html', prediction=result)
```

Au lieu d'afficher index.html, nous affichons results.html avec notre prédiction. Vous pouvez structurer et styliser votre fichier results.html comme vous le souhaitez et y ajouter la prédiction.

## Comment déployer l'application sur le web

Maintenant que nous avons terminé le stylisme, l'application est prête à être poussée sur le cloud. PythonAnywhere est facile à utiliser et propose un plan gratuit pour déployer des applications Python. Vous devrez d'abord créer un compte et choisir le plan gratuit. 

Ensuite, vous devrez donner un nom à votre application, aller dans l'onglet des fichiers et supprimer le site existant. Téléchargez tous vos fichiers en respectant la même structure de répertoire que celle discutée ci-dessus. Allez ensuite dans l'onglet web et cliquez sur le bouton bleu de rechargement. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/pythonanywhere.png)
_Fichiers téléchargés_

Si vous avez des fichiers CSS et JavaScript dans votre projet, vous devrez définir leur URL et le chemin du répertoire dans la section des fichiers statiques (static files) de l'onglet web. 

L'URL sera /static/ puisque nous servons des fichiers statiques et le répertoire sera /home/votre-nom-de-site/mysite/assets puisque nos fichiers CSS et JavaScript sont sauvegardés dans le répertoire static.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/paw.png)
_Section des fichiers statiques_

Rechargez le site web en cliquant à nouveau sur le bouton bleu de rechargement et FÉLICITATIONS – vous avez déployé votre application web de machine learning sur le cloud.

## Conclusion

Déployer des applications web de machine learning n'est pas aussi difficile qu'il n'y paraît – du moins pas autant que d'apprendre les théories du machine learning. Et si vous avez fait cela, le déploiement n'est qu'une brise qui peut vous emmener vers de nouveaux sommets. 

J'espère que cet article vous a aidé à comprendre comment vous pouvez déployer vos modèles et les rendre plus attrayants. Le code de l'application web d'évaluation des risques de diabète que j'ai construite se trouve sur mon [GitHub](https://github.com/ToobaJamal/diabetes_risk_assessment). 

Déployez vos modèles et montrez au monde votre super-pouvoir !

> Envie de vous connecter sur LinkedIn ? Contactez-moi sur [Tooba Jamal](https://www.linkedin.com/in/tooba-jamal/)