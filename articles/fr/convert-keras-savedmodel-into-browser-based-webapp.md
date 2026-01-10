---
title: Comment convertir un SavedModel Keras en une application web par navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-18T16:36:22.000Z'
originalURL: https://freecodecamp.org/news/convert-keras-savedmodel-into-browser-based-webapp
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/beach-photo.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: keras
  slug: keras
- name: Machine Learning
  slug: machine-learning
seo_title: Comment convertir un SavedModel Keras en une application web par navigateur
seo_desc: "By Suchandra Datta\nIf you're a Python developer who works with Keras SavedModels,\
  \ this article is for you. \nPerhaps you're not sure how to use SavedModels to leverage\
  \ the power of machine learning in browser-based web apps. But don't worry – we'll\
  \ co..."
---

Par Suchandra Datta

Si vous êtes un développeur Python qui travaille avec les SavedModels de Keras, cet article est pour vous.

Peut-être ne savez-vous pas comment utiliser les SavedModels pour exploiter la puissance du machine learning dans des applications web par navigateur. Mais ne vous inquiétez pas – nous allons couvrir toutes les étapes de base nécessaires pour commencer.

En plus de cela, nous passerons en revue certains concepts importants qui vous aideront à faciliter votre transition de Python vers JavaScript.

Avant de plonger dans le processus, répondons à quelques questions qui pourraient vous venir à l'esprit à ce stade.

## Qu'est-ce qu'un SavedModel Keras ?

Un modèle Keras est composé de l'architecture du réseau, des poids du modèle et d'un optimiseur pour votre fonction de perte.

Le format par défaut pour sauvegarder des modèles sur disque est le format SavedModel. Ce format nous permet de sauvegarder des modèles avec des objets personnalisés avec un minimum de tracas.

SavedModel stocke l'optimiseur, la perte et l'architecture du réseau dans le fichier `saved_model.pb`, tandis que les poids sont stockés dans le répertoire `variables`.

Pour des informations plus détaillées sur le format SavedModel, consultez la documentation officielle [ici](https://www.tensorflow.org/guide/keras/save_and_serialize).

## Comment entraîner un SavedModel Keras si je n'ai pas de GPU ?

La plupart des passionnés de machine learning n'ayant pas accès à des installations GPU commencent le développement de modèles sur Google Colaboratory.

Je suis un grand admirateur de Google Colab et de ses fonctionnalités depuis que je m'intéresse au domaine du machine learning. Il offre un environnement Jupyter Notebook avec un accès gratuit aux GPU avec un temps d'entraînement maximum de 12 heures.

Si vous avez des questions concernant Google Colaboratory, rendez-vous dans leur section FAQ disponible [ici](https://research.google.com/colaboratory/faq.html#:~:text=How%20long%20can%20notebooks%20run,or%20based%20on%20your%20usage.).

## Pourquoi voudrais-je convertir un SavedModel en une application web ?

Les produits basés sur le web sont partout, et ils sont généralement assez faciles à utiliser. Vous lisez probablement cet article depuis un navigateur en ce moment, que ce soit depuis votre téléphone, votre ordinateur de bureau ou votre portable.

Les modèles de machine learning, en fin de compte, sont destinés à être utilisés dans le monde réel et non à être conservés dans une boîte en verre. Alors, quelle meilleure façon d'apporter votre modèle aux utilisateurs que par un support web ?

De plus, les applications par navigateur ne nécessitent aucun frais d'installation et peuvent être consultées de manière uniforme sur plusieurs appareils.

## D'accord, commençons

J'avais construit un modèle CNN simple de détection d'émotions qui pouvait prédire 7 émotions (joie, tristesse, neutre, colère, surprise, peur et dégoût) en utilisant Python et l'API Keras.

Essayer de le convertir dans un format adapté au web sans expérience préalable s'est avéré un peu difficile. L'ensemble du processus, que je décrirai ensuite, est possible grâce à la merveilleuse documentation de [Tensorflow.js](https://www.tensorflow.org/js/tutorials/setup), aux [MDN Web docs](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications) et à la [documentation d'hébergement Firebase](https://firebase.google.com/docs/hosting).

En utilisant ces ressources, j'ai pu réduire le processus aux étapes suivantes :

* Convertir le SavedModel Keras au format Layers de Tensorflow.js
* Charger le modèle via JavaScript et les Promises
* Accéder à une image téléchargée par un utilisateur
* Prétraiter l'image téléchargée
* Inférence du modèle dans le navigateur et affichage de la sortie via une interface utilisateur

Examinons chacune de ces étapes plus en détail.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-15.png)
_Photo de Unsplash_

## Comment convertir un SavedModel Keras au format Layers de Tensorflow.js

Pour convertir un SavedModel Keras au format layers de Tensorflow.js, nous devrions utiliser le script `tensorflowjs_converter`. Nous pouvons également utiliser l'API Python comme décrit dans leur documentation officielle [ici](https://www.tensorflow.org/js/tutorials/conversion/import_keras).

J'ai rencontré une erreur frustrante avec la première méthode car, pour une raison quelconque, le `tensorflowjs_converter` ne semblait pas fonctionner sur Google Colab.

J'avais sauvegardé le modèle sur le drive et la partie "My Drive" du chemin du fichier, spécifiquement l'espace, semblait causer des problèmes. J'ai trouvé cela mentionné dans ce ticket GitHub #3618 [ici](https://github.com/tensorflow/tfjs/issues/3618).

L'utilisation de l'API Python a fonctionné de manière fluide, ce qui m'a donné un fichier `model.json` pour l'architecture du modèle et des fichiers binaires pour les poids. J'étais maintenant prêt à l'utiliser sur le web !

![Image](https://www.freecodecamp.org/news/content/images/2021/05/pic.png)
_Code pour convertir le format SavedModel au format Layers_

Mais attendez ! Pourquoi avons-nous besoin de convertir ? Pourquoi ne pas simplement entraîner notre modèle en utilisant Tensorflow.js lui-même ?

Eh bien, vous devez effectuer cette conversion si vous avez déjà passé beaucoup de temps à entraîner vos modèles Keras sur de grands jeux de données et que vous ne voulez pas les réécrire et les réentraîner en utilisant JavaScript.

## Comment charger le modèle via JavaScript et les Promises

[Tensorflow.js](https://www.tensorflow.org/js/tutorials) est une bibliothèque basée sur JavaScript pour le développement de modèles de machine learning. Vous pouvez l'utiliser dans le navigateur ainsi que via l'environnement d'exécution JavaScript populaire Node.js.

Vous pouvez le configurer de deux manières différentes : soit en l'incluant à l'aide d'une balise script, soit en l'utilisant via Node.js.

Comme le modèle CNN que j'ai entraîné est assez simple, j'ai opté pour l'approche de la balise script.

```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@2.0.0/dist/tf.min.js"></script>
```

Maintenant que nous avons inclus la bibliothèque Tensorflow.js, l'étape suivante consiste à charger le modèle. Nous pouvons charger le modèle des manières suivantes :

* Stockage local du navigateur (localStorage)
* Stockage IndexedDB du navigateur
* À partir d'un point de terminaison HTTP ou HTTPS
* À partir du système de fichiers natif en utilisant Node.js

Le chargement du modèle à partir d'un point de terminaison HTTPS semblait être la méthode la plus faisable pour moi. J'ai donc hébergé les fichiers du modèle sur Firebase Hosting et chargé le modèle à l'aide du code suivant :

```javascript
const model = await tf.loadLayersModel('model.json');	
```

Tensorflow utilise la méthode `fetch` pour charger des ressources en utilisant une approche basée sur les Promises. Fetch renvoie une Promise qui se résout en la réponse contenant les ressources demandées.

Une Promise en JavaScript est un proxy pour une valeur que vous ne connaissez pas à cet instant précis, mais qui sera peut-être connue plus tard.

Par exemple, lors de la demande de ressources basées sur une URL, nous ne savons pas immédiatement si nous obtiendrons réellement ces ressources – nous devrons attendre un certain temps jusqu'à ce que le serveur réponde (ou non).

Mais attendre sous n'importe quelle forme est préjudiciable à la réactivité et à l'interaction continue de l'utilisateur, ce qui est critique pour les pages web. JavaScript vous permet donc d'utiliser des appels asynchrones via des Promises. Celles-ci vous permettent de demander des ressources ET de continuer avec les instructions suivantes indépendamment de la réponse du serveur.

Pour permettre une gestion des erreurs plus propre et plus facile avec les Promises, `async/await` a été introduit. `await` bloque le flux de contrôle jusqu'à ce qu'une Promise revienne, et les fonctions avec des instructions `await` sont déclarées `async`.

## Comment accéder à une image téléchargée par un utilisateur

Créons une fonctionnalité simple de téléchargement de fichier en utilisant une balise HTML `input` et un autre bouton qui lancera les calculs de prédiction lors du clic.

```html
<div class="container" id="tray">
		<div id="uploadFile" class="custombutton">
			<i class="fa fa-file" style="font-size:25px;color: #1ab5e3"></i><br/><br/>
			<input type="file" name="fileupload" accept="image/*" onchange="display(event)">
		</div>
		<div class="custombutton">
			<i class="fa fa-bar-chart" style="font-size:25px;color: #1ab5e3"></i><br/><br/>
			<input type="button" name="predict" onclick="predict_emotion()" value="PRÉDIRE">
		</div>
	</div>
```

Les boutons de téléchargement de fichier et de prédiction ressemblent à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-24.png)

Ensuite, nous accédons au fichier image téléchargé et l'affichons en utilisant des URL d'objet comme décrit dans les MDN Web docs [ici](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications).

```javascript
let input_image = document.getElementById("input_image")
input_image.src = URL.createObjectURL(event.target.files[0]);
document.getElementById("input_image_container").style.display = "block";

<div id="input_image_container"><img src="#" id="input_image" style="top:5vh;"></div>
```

Après avoir téléchargé une image, cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-25.png)

## Comment prétraiter l'image téléchargée

Ceci est spécifique au domaine du modèle et nécessite différentes étapes pour différentes applications.

Pour mon modèle, je n'ai pas eu grand-chose à faire, juste une normalisation et un redimensionnement simples que j'ai facilement effectués en utilisant les fonctions de Tensorflow.js.

Consultez leur [référence API officielle](https://js.tensorflow.org/api/latest/) pour une compréhension approfondie des fonctions proposées et de leurs cas d'utilisation.

```javascript
// Étapes de prétraitement 
		/*
		(1) Redimensionner en 48*48
		(2) Convertir en niveaux de gris en utilisant la moyenne simple
		(3) Convertir en float
		(4) Remodeler en (1,48,48,1)
		(5) Normaliser en divisant par 255.0
		*/
let step1 = tf.browser.fromPixels(input)
.resizeNearestNeighbor([48,48])
.mean(2)
.toFloat()
.expandDims(0)
.expandDims(-1)
.div(255.0)
```

## Inférence du modèle dans le navigateur et affichage de la sortie via une interface utilisateur

La fonction `predict` renvoie les prédictions – dans notre cas, un tenseur avec 7 valeurs de probabilité pour les 7 émotions.

Nous augmentons l'échelle des probabilités pour l'affichage dans le navigateur en utilisant un `div` pour chaque émotion et la largeur du `div` pour spécifier la valeur de probabilité mise à l'échelle.

```javascript
pred = model.predict(step1)
pred.data()
    .then((data) => {console.log(data)
		   		output = document.getElementById("output_chart")
		    	output.innerHTML = ""
		    	max_val = -1
		    	max_val_index = -1
				for(let i=0;i<data.length;i++)
				{
					style_text = "width: "+data[i]*150+"px; height: 25px; position:relative; margin-top: 3vh; background-color: violet; "
					output.innerHTML+="<div style = '" +style_text+ "'></div>"
					if(data[i] > max_val)
					{
						max_val = data[i]
						max_val_index = i
					}
				}
				EMOTION_DETECTED = emotions[max_val_index]
				document.getElementsByClassName("output_screen")[0].style.display="flex";
document.getElementById("output_text").innerHTML=""
document.getElementById("output_text").innerHTML = "<p>Émotions et probabilités mises à l'échelle correspondantes</p><p>Émotion détectée : " + EMOTION_DETECTED + "(" + (max_val*100).toFixed(2) + "% de probabilité)</p>"
```

Super – nous avons tous les blocs de construction prêts ! Maintenant, mettons tout cela ensemble. Nous allons intégrer les parties suivantes :

* Le balisage HTML qui sert d'interface utilisateur simple
* La balise script pour accéder à Tensorflow.js
* La balise script pour nos icônes Font Awesome
* Le code JavaScript pour le chargement du modèle, l'inférence et la sortie

Voici le code JavaScript final :

```javascript
// Afficher l'image téléchargée par l'utilisateur
function display(event)
	{
		let input_image = document.getElementById("input_image")
		input_image.src = URL.createObjectURL(event.target.files[0]);
		document.getElementById("input_image_container").style.display = "block";
	}
    
// Prédire l'émotion et afficher la sortie
async function predict_emotion()
	{
		let input = document.getElementById("input_image");
		// Étapes de prétraitement 
		/*
		(1) Redimensionner en 48*48
		(2) Convertir en niveaux de gris en utilisant la moyenne simple
		(3) Convertir en float
		(4) Remodeler en (1,48,48,1)
		(5) Normaliser en divisant par 255.0
		*/
		let step1 = tf.browser.fromPixels(input).resizeNearestNeighbor([48,48]).mean(2).toFloat().expandDims(0).expandDims(-1).div(255.0)
		const model = await tf.loadLayersModel('model.json');
		pred = model.predict(step1)
		pred.print()
		console.log("Fin de la fonction de prédiction")
		// Ce tableau est encodé avec l'index i = émotion correspondante. Dans le jeu de données, 0 = Colère, 1 = Dégoût, 2 = Peur, 3 = Joie, 4 = Tristesse, 5 = Surprise et 6 = Neutre
		emotions = ["Colère", "Dégoût", "Peur", "Joie", "Tristesse", "Surprise", "Neutre"]
		// À quel index du tenseur obtenons-nous la plus grande valeur ?
		pred.data()
		    .then((data) => {console.log(data)
		    	output = document.getElementById("output_chart")
		    	output.innerHTML = ""
		    	max_val = -1
		    	max_val_index = -1
				for(let i=0;i<data.length;i++)
				{
					style_text = "width: "+data[i]*150+"px; height: 25px; position:relative; margin-top: 3vh; background-color: violet; "
					output.innerHTML+="<div style = '" +style_text+ "'></div>"
					if(data[i] > max_val)
					{
						max_val = data[i]
						max_val_index = i
					}
				}
				EMOTION_DETECTED = emotions[max_val_index]
				document.getElementsByClassName("output_screen")[0].style.display="flex";
				document.getElementById("output_text").innerHTML=""
				document.getElementById("output_text").innerHTML = "<p>Émotions et probabilités mises à l'échelle correspondantes</p><p>Émotion détectée : " + EMOTION_DETECTED + "(" + (max_val*100).toFixed(2) + "% de probabilité)</p>"
		})	

	}
```

Voici le HTML final et les balises script :

```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="styles/page_styling.css">
	
</head>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@2.0.0/dist/tf.min.js"></script>
<body>
	<div id="input_image_container"><img src="#" id="input_image" style="top:5vh;"></div>
	<div class="container" id="tray">
		<div id="uploadFile" class="custombutton">
			<i class="fa fa-file" style="font-size:25px;color: #1ab5e3"></i><br/><br/>
			<input type="file" name="fileupload" accept="image/*" onchange="display(event)">
		</div>
		<div class="custombutton">
			<i class="fa fa-bar-chart" style="font-size:25px;color: #1ab5e3"></i><br/><br/>
			<input type="button" name="predict" onclick="predict_emotion()" value="PRÉDIRE">
		</div>
	</div>
	<div class="container output_screen">
		<div id="emotion_tags">
			<ul>
				<li>Colère</li>
				<li>Dégoût</li>
				<li>Peur</li>
				<li>Joie</li>
				<li>Tristesse</li>
				<li>Surprise</li>
				<li>Neutre</li>
			</ul>
		</div>
		<div id="output_chart"></div>
		<div id="output_text"></div>
	</div>
<script src="scripts/script.js"></script>
</body>
</html>

```

Voici un exemple de sortie, où les trois premières émotions prédites sont la tristesse, la joie et le neutre :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-8.png)
_Prédictions et interface utilisateur_

## Conclusion

Dans cet article, nous avons passé en revue les étapes de base nécessaires pour convertir un SavedModel Keras dans un format adapté au web. Nous avons appris à charger, prétraiter et effectuer des inférences dans le navigateur en utilisant Tensorflow.js et à afficher la sortie via une interface utilisateur.

J'espère que vous avez apprécié la lecture de cet article et qu'il vous a été utile. Passez une bonne journée et je vous souhaite bonne chance dans votre parcours de codage !

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-16.png)
_Photo de Unsplash_"