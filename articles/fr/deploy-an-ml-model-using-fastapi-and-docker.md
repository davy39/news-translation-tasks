---
title: Comment déployer un modèle TensorFlow en tant que service API RESTful
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-07T14:58:44.000Z'
originalURL: https://freecodecamp.org/news/deploy-an-ml-model-using-fastapi-and-docker
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/deploying-tensorflow-heroku-docker.png
tags:
- name: deployment
  slug: deployment
- name: Docker
  slug: docker
- name: 'fastai, '
  slug: fastai
- name: Machine Learning
  slug: machine-learning
- name: REST API
  slug: rest-api
- name: TensorFlow
  slug: tensorflow
seo_title: Comment déployer un modèle TensorFlow en tant que service API RESTful
seo_desc: "By Neil Ruaro\nIf you're like I am, then you've probably watched and read\
  \ a number of tutorials on creating machine learning models with TensorFlow, PyTorch,\
  \ Scikit-Learn or any other framework out there. \nBut there is one thing that these\
  \ tutorials t..."
---

Par Neil Ruaro

Si vous êtes comme moi, vous avez probablement regardé et lu un certain nombre de tutoriels sur la création de modèles d'apprentissage automatique avec TensorFlow, PyTorch, Scikit-Learn ou tout autre framework disponible. 

Mais il y a une chose que ces tutoriels tendent à omettre, et c'est le déploiement du modèle.

Dans ce tutoriel, je vais discuter de la manière de déployer un modèle TensorFlow CNN qui classe les images de nourriture sur Heroku en utilisant FastAPI et Docker.

### Technologies que nous allons utiliser

Si vous n'êtes pas familier, FastAPI est un framework web Python pour créer des applications API rapides. Et à mon avis, c'est le plus facile à apprendre parmi tous les frameworks web Python disponibles.

FastAPI a également une intégration par défaut avec la documentation Swagger et facilite la configuration et la mise à jour.

Docker, en revanche, est un incontournable de l'industrie en ingénierie logicielle, car c'est l'un des logiciels de conteneurisation les plus populaires disponibles. Docker est utilisé pour développer, déployer et gérer des applications dans des environnements virtualisés appelés conteneurs.

Le principal argument de vente de l'utilisation de Docker est qu'il résout le problème "ça marche sur ma machine, pourquoi pas sur la vôtre ?". Coïncidence, j'ai effectivement rencontré ce problème exact en travaillant sur ce projet, l'ayant finalement résolu lorsque j'ai décidé d'utiliser Docker.

Heroku, enfin, est une plateforme cloud où vous pouvez déployer, gérer et mettre à l'échelle des applications web. Elle fonctionne avec des applications back-end, front-end ou full-stack.

## Prérequis

Avant de commencer, vous aurez d'abord besoin des éléments suivants :

1. Un compte Docker
2. Un compte Heroku, et le CLI Heroku
3. Une installation Python

## L'application que nous construisons

Nous allons construire un service API RESTful pour un modèle CNN TensorFlow qui classe les images de nourriture. 

Après avoir construit le service API, je vous montrerai comment dockeriser l'application, puis la déployer sur Heroku.

## Comment télécharger les nécessités

Vous devrez d'abord cloner le dépôt GitHub à ce [lien](https://github.com/eRuaro/food-vision-api).

`git clone https://github.com/eRuaro/food-vision-api.git`

Il y a deux branches dans ce dépôt – vous utiliserez la branche `start-here` car `main` est la branche complétée.

Une fois que vous avez obtenu le dépôt cloné, vous devrez télécharger [Docker](https://docs.docker.com/get-docker/) sur votre système local, ainsi que le [CLI Heroku](https://devcenter.heroku.com/articles/heroku-cli).

Vous devez également installer les packages suivants sur pip :

1. FastAPI
2. TensorFlow
3. Numpy
4. Uvicorn
5. Image

Pour ce faire, créez un fichier `requirements.txt` sur la branche `start-here`, et mettez-y ce qui suit. Notez que vous pouvez utiliser n'importe quelle autre version des packages listés ci-dessous, tant qu'ils fonctionnent encore ensemble.

```
fastapi==0.73.0
numpy==1.19.5
uvicorn==0.15.0
image==1.5.33
tensorflow-cpu==2.7.0

```

Après quoi vous pouvez installer les packages en utilisant la commande  
`pip install -r requirements.txt`.

Actuellement, notre branche `start-here` contient le fichier du modèle sauvegardé, ainsi que le notebook Jupyter utilisé pour créer le modèle. Le notebook contient également le code qui implémente notre fonctionnalité API. C'est-à-dire qu'il implémente la prédiction de la classe alimentaire d'une image basée sur son lien URL.

## Brève introduction à FastAPI

Avec cela en tête, commençons à écrire le code ! Dans le répertoire racine, créez un fichier `main.py`. Dans ce fichier, ajoutez les lignes de code suivantes :

```
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
import os

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

@app.get("/")
async def root():
    return {"message": "Bienvenue dans l'API Food Vision !"}
    
if __name == "__main__":
	port = int(os.environ.get('PORT', 5000))
	run(app, host="0.0.0.0", port=port)
```

L'exécution de la commande `python -m uvicorn main:app --reload` exécutera l'application et écoutera les modifications que nous apportons au serveur. 

Alternativement, vous pouvez utiliser `python main.py` et cela exécutera l'application sur le port 5000, grâce aux trois dernières lignes de code. Cependant, cela n'écoutera pas les modifications que nous apportons, vous devrez donc relancer l'application chaque fois que vous souhaitez voir vos modifications.

Nous avons également ajouté le `CORSMiddleware` qui nous permet essentiellement d'accéder à l'API sur un hôte différent. C'est-à-dire que nous pouvons étendre l'application en créant une interface front-end pour celle-ci. Nous n'aborderons pas cela dans cet article, mais je l'ai mis ici au cas où vous souhaiteriez créer un front-end pour interagir avec l'API également.

En allant sur le port où l'application est en cours d'exécution, vous obtiendrez ceci.

```
{
    "message": "Bienvenue dans l'API Food Vision !"
}

```

La commande `python -m uvicorn main:app --reload` fait référence à ce qui suit :

```
main -> Le fichier main.py
app -> L'objet créé à l'intérieur de main.py avec la ligne app = FastAPI()
--reload -> Faire redémarrer le serveur après les modifications du code

```

Décortiquons le code que nous avons écrit jusqu'à présent.

```
@app.get("/")
async def root():
    return {"message": "Bienvenue dans l'API Food Vision !"}

```

`@app` est nécessaire pour les commandes FastAPI. Le `get` est une méthode HTTP, tandis que le `"/"` est le chemin URL de cette requête API spécifique. En dessous, nous appelons une fonction qui retournera quelque chose. Ici, nous retournons simplement un message `json` simple.

C'est-à-dire que nous avons un modèle pour écrire des points de terminaison API avec FastAPI.

```
@app.http_method("url_path")
async def functionName():
    return something

```

## Comment écrire la fonctionnalité de l'API

Écrivons la fonctionnalité principale de l'API, c'est-à-dire, prendre une URL d'image de nourriture sur Internet, et prédire le nom de cette nourriture. 

Tout d'abord, étendons le code que nous avons écrit précédemment, importons toutes les fonctions nécessaires que nous allons utiliser, et chargeons le modèle lui-même.

```python
from fastapi import FastAPI
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import get_file 
from tensorflow.keras.utils import load_img 
from tensorflow.keras.utils import img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax
from numpy import argmax
from numpy import max
from numpy import array
from json import dumps
from uvicorn import run
import os

app = FastAPI()
model_dir = "food-vision-model.h5"
model = load_model(model_dir)

...
...
...

if __name == "__main__":
	port = int(os.environ.get('PORT', 5000))
	run(app, host="0.0.0.0", port=port)
```

Après avoir chargé le modèle, ajoutons les classes de nourriture que nous avons, qui sont basées sur le jeu de données Food 101.

```python
class_predictions = array([
    'apple pie',
    'baby back ribs',
    'baklava',
    'beef carpaccio',
    'beef tartare',
    'beet salad',
    'beignets',
    'bibimbap',
    'bread pudding',
    'breakfast burrito',
    'bruschetta',
    'caesar salad',
    'cannoli',
    'caprese salad',
    'carrot cake',
    'ceviche',
    'cheesecake',
    'cheese plate',
    'chicken curry',
    'chicken quesadilla',
    'chicken wings',
    'chocolate cake',
    'chocolate mousse',
    'churros',
    'clam chowder',
    'club sandwich',
    'crab cakes',
    'creme brulee',
    'croque madame',
    'cup cakes',
    'deviled eggs',
    'donuts',
    'dumplings',
    'edamame',
    'eggs benedict',
    'escargots',
    'falafel',
    'filet mignon',
    'fish and chips',
    'foie gras',
    'french fries',
    'french onion soup',
    'french toast',
    'fried calamari',
    'fried rice',
    'frozen yogurt',
    'garlic bread',
    'gnocchi',
    'greek salad',
    'grilled cheese sandwich',
    'grilled salmon',
    'guacamole',
    'gyoza',
    'hamburger',
    'hot and sour soup',
    'hot dog',
    'huevos rancheros',
    'hummus',
    'ice cream',
    'lasagna',
    'lobster bisque',
    'lobster roll sandwich',
    'macaroni and cheese',
    'macarons',
    'miso soup',
    'mussels',
    'nachos',
    'omelette',
    'onion rings',
    'oysters',
    'pad thai',
    'paella',
    'pancakes',
    'panna cotta',
    'peking duck',
    'pho',
    'pizza',
    'pork chop',
    'poutine',
    'prime rib',
    'pulled pork sandwich',
    'ramen',
    'ravioli',
    'red velvet cake',
    'risotto',
    'samosa',
    'sashimi',
    'scallops',
    'seaweed salad',
    'shrimp and grits',
    'spaghetti bolognese',
    'spaghetti carbonara',
    'spring rolls',
    'steak',
    'strawberry shortcake',
    'sushi',
    'tacos',
    'takoyaki',
    'tiramisu',
    'tuna tartare',
    'waffles'
])
```

Maintenant que nous avons les classes de nourriture, écrivons la fonctionnalité principale de l'API.

```
@app.post("/net/image/prediction/")
async def get_net_image_prediction(image_link: str = ""):
    if image_link == "":
        return {"message": "Aucun lien d'image fourni"}
    
    img_path = get_file(
        origin = image_link
    )
    img = load_img(
        img_path, 
        target_size = (224, 224)
    )

    img_array = img_to_array(img)
    img_array = expand_dims(img_array, 0)

    pred = model.predict(img_array)
    score = softmax(pred[0])

    class_prediction = class_predictions[argmax(score)]
    model_score = round(max(score) * 100, 2)

    return {
        "model-prediction": class_prediction,
        "model-prediction-confidence-score": model_score
    }
```

Ici, nous faisons une requête **post** à l'endpoint `/net/image/prediction/` et fournissons l'`image_url` en tant que paramètre de requête. C'est-à-dire que l'endpoint complet lors de l'envoi d'un lien URL d'image serait `/net/image/prediction/image_url=image-url`.

Pour simplifier, nous donnons à `image_link` une valeur par défaut de `""` et lorsqu'il n'y a pas de lien passé à l'endpoint, nous retournons simplement un message indiquant qu'aucun lien d'image n'a été fourni. 

`get_file()` télécharge l'image via le lien URL fourni, tandis que `load_img()` charge l'image au format PIL, et la transforme en la taille d'image appropriée que le modèle souhaite. 

`img_to_array()` convertit l'image chargée en un tableau NumPy. `expand_dims()` étend les dimensions du tableau d'une à l'index zéro.

Nous utilisons ensuite `model.predict()` pour obtenir la prédiction du modèle sur l'image chargée, et obtenir le score de confiance du modèle sur ladite prédiction en utilisant `softmax()`. J'ai utilisé softmax ici car c'est la fonction d'activation utilisée dans la création du modèle.

Nous obtenons enfin le type de nourriture en utilisant `argmax()` sur le score de confiance du modèle. Nous utiliserons cela comme l'index que nous utiliserons pour rechercher dans le tableau `class_predictions` qui contient les différentes classes de nourriture que nous avons. 

Enfin, nous multiplions le score de confiance du modèle par 100 afin que la plage du score soit de 1 à 100.

Nous retournons ensuite la prédiction du modèle et le score de confiance du modèle.

## Pourquoi nous devons utiliser Docker pour déployer cette application

Vous pouvez en fait déployer cette application telle quelle sur Heroku, en utilisant la méthode habituelle de définition d'un `Procfile`. Mais lorsque j'ai essayé cette méthode, je continuais à obtenir une erreur [`ValueError: Out of range float values are not JSON compliant`](https://stackoverflow.com/questions/71152285/valueerror-out-of-range-float-values-are-not-json-compliant-error-on-heroku-an). J'obtiens également cette erreur lorsque j'exécute l'application sur le _Windows Subsystem for Linux_ (WSL). Cependant, lorsque je l'exécute sur Windows, l'erreur disparaît.

Vous pouvez en fait éviter cette erreur en ajoutant cette ligne de code, après l'assignation initiale de la variable `model_score` :

```
model_score = dumps(model_score.tolist())
```

Cela permet à l'application de s'exécuter à la fois sur Heroku et WSL, mais elle ne retournera que ces valeurs lors de la requête POST.

```
{
    "model-prediction": "apple pie",
    "model-prediction-confidence-score": NaN,
}
```

Donc, cela fonctionne sur ma machine (Windows), mais pas sur Heroku (en utilisant Procfile), ni sur WSL. C'est le genre de problème que Docker résout ! 

## Comment dockeriser l'application

Commençons à dockeriser l'application. Créez un `Dockerfile` dans le répertoire racine du projet et mettez-y le contenu suivant :

```
FROM python:3.7.3-stretch

# Informations sur le mainteneur
LABEL maintainer="votre-adresse-email"

# Créer des répertoires de travail
RUN  mkdir -p  /food-vision-api
WORKDIR  /food-vision-api

# Mettre à jour pip sans cache
RUN pip install --no-cache-dir -U pip

# Copier le fichier des exigences de l'application dans le répertoire de travail créé
COPY requirements.txt .

# Installer les dépendances de l'application à partir du fichier des exigences
RUN pip install -r requirements.txt

# Copier chaque fichier dans le dossier source vers le répertoire de travail créé
COPY  . .

# Exécuter l'application python
CMD ["python", "main.py"]
```

Cela tire l'image Python 3.7.3 et installe tous les packages nécessaires définis dans le fichier `requirements.txt`. Ensuite, il exécute l'application en utilisant la commande `python main.py` comme défini dans la dernière ligne du fichier.

Vous pouvez ensuite construire et exécuter l'application en utilisant les commandes CLI suivantes :

```
$ docker image build -t <nom-de-l-app> .
$ docker run -p 5000:5000 -d <nom-de-l-app>
```

Ensuite, vous pouvez arrêter l'application et libérer des ressources système en exécutant ce qui suit :

```
$ docker container stop <id-du-conteneur>
$ docker system prune
```

`id-du-conteneur` est retourné lors de l'exécution de la commande `docker run` ci-dessus. 

## Comment déployer sur Heroku

Avec l'application maintenant dockerisée, nous pouvons la déployer sur Heroku. Je suppose que vous avez déjà installé le CLI Heroku et que vous avez déjà connecté le CLI à votre compte Heroku. 

Créons d'abord l'application sur Heroku via le CLI :

```
$ heroku create <nom-de-l-app>
```

Ensuite, nous pouvons pousser et publier l'application via le conteneur Docker que nous avons créé précédemment avec les commandes suivantes :

```
$ heroku container:push web --app <nom-de-l-app>
$ heroku container:release web --app <nom-de-l-app>
```

Après cela, vous pouvez aller sur votre tableau de bord Heroku et ouvrir l'application. Vous devriez être accueilli avec le message JSON que nous avons dans le répertoire `"/"` de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-7.png)
_Message JSON d'accueil sur le répertoire `"/"`_

Lorsque vous naviguez vers `/docs`, vous serez accueilli avec la documentation Swagger de l'application. Ici, vous pouvez jouer avec la requête POST que nous avons créée et voir si les prédictions du modèle sont correctes. Notez que vous devez télécharger des liens d'images avec `jpeg` ou `png` dans leur URL.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-8.png)
_Documentation Swagger de l'application sur `/docs`_

Essayons cela en utilisant une image de gâteau au chocolat, son lien URL est [celui-ci](https://tallypress.com/wp-content/uploads/2017/11/7-irresistible-chocolate-cakes-you-should-try-in-klang-valley.jpg).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-9.png)
_Image de tallypress.com_

Collez le lien dans la zone de texte dans `/docs` comme ceci, puis appuyez sur `Execute`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-10.png)
_Démonstration de l'application_

Après avoir appuyé sur le bouton `Execute`, cela prendra quelques secondes jusqu'à ce que nous obtenions la prédiction du modèle. C'est parce que nous utilisons `tensorflow-cpu` car nous sommes limités par la RAM et la taille du slug de notre application lorsque nous utilisons le niveau gratuit de Heroku. 

Après l'exécution, vous devriez être accueilli avec cette réponse :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-11.png)
_Réponse de l'API après utilisation_

Comme vous pouvez le voir, le modèle l'a prédit correctement, avec un score de confiance de 2,65 %. Ce score de confiance est acceptable car nous ne traitons pas de la précision du modèle (qui nécessite la valeur de vérité au préalable), et nous traitons des données que le modèle n'a jamais vues auparavant. 

## Conclusion

Dans cet article, vous avez appris comment déployer un modèle CNN TensorFlow sur Heroku en le servant en tant qu'API RESTful, et en utilisant Docker. 

Si vous trouvez cet article utile, n'hésitez pas à le partager sur les réseaux sociaux. Connectons-nous sur [Twitter](https://twitter.com/neil_ruaro) ! Vous pouvez également me soutenir en [m'offrant un café](https://www.buymeacoffee.com/eRuaro).