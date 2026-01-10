---
title: Comment rendre les chasses au trésor plus amusantes avec l'intelligence artificielle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-17T15:53:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-scavenger-hunts-more-fun-with-artificial-intelligence-74a184f3db33
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sM91z7-6k4OUh646nX8Pwg.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: AWS
  slug: aws
- name: Game Development
  slug: game-development
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Comment rendre les chasses au trésor plus amusantes avec l'intelligence
  artificielle
seo_desc: 'By Terren Peterson

  Scavenger hunts have existed for generations. The traditional game goes something
  like this:


  a leader writes down a list of objects on a scrap of paper.

  the teams then spend the afternoon searching the surrounding area — either ou...'
---

Par Terren Peterson

Les chasses au trésor existent depuis des générations. Le jeu traditionnel se déroule comme suit :

* un leader écrit une liste d'objets sur un bout de papier.
* les équipes passent ensuite l'après-midi à chercher les objets dans les environs — soit en extérieur, soit en intérieur.
* Elles cochent les objets de la liste au fur et à mesure qu'elles les trouvent, puis continuent jusqu'à ce que la liste soit complète.

Des règles simples. Mais beaucoup de plaisir.

#### Moderniser le jeu avec l'IA

J'ai écrit une application pour la plateforme Alexa d'Amazon qui modernise les chasses au trésor. Elle utilise les dernières technologies disponibles — y compris des outils d'intelligence artificielle comme la reconnaissance d'images et vocale.

Le principe du jeu ne change pas : trouver dix objets aléatoires situés dans votre maison — ou autour de votre quartier — en une heure. Sauf qu'Alexa facilite le déroulement du jeu.

Mon application est gratuite à activer si vous êtes l'un des millions de personnes qui possèdent un Amazon Alexa. L'article ci-dessous décrit comment chaque outil d'IA est utilisé, y compris les nouveaux services AWS — Rekognition et Polly. La compétence s'appelle [Scavenger Hunt](https://www.amazon.com/Drawrz-com-Scavenger-Hunt/dp/B06ZZ6F91T/). Voici un aperçu de son fonctionnement :

### Intelligence Artificielle #1 — Alexa

Le lancement du jeu commence par l'invocation de la compétence Alexa. Toute personne avec un appareil énonce la demande suivante.

> Alexa, demande à Scavenger Hunt de commencer une nouvelle partie.

N'importe lequel des millions de propriétaires d'Alexa peut utiliser sa voix pour faire cette demande. Le langage est subtil. Le choix des mots diffère lorsque cette intention est exprimée par différents genres, groupes d'âge, ethnies et démographies sociales. C'est la puissance de l'intelligence artificielle qui déchiffre ces subtiles différences de choix de mots et de dialecte en une simple demande pour commencer le jeu.

#### Comment fonctionne le jeu ?

Le jeu commence avec votre Alexa exécutant une variété de technologies différentes. Voici l'architecture des divers services et interfaces utilisés :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vT25AhbVVvW6mJOXwHFZng.jpeg)

La plateforme Alexa gère le traitement du langage, traduisant l'intention vocale en texte. Le [service Lambda](https://aws.amazon.com/lambda/) héberge la logique de traitement et le code est écrit en NodeJS. Le suivi du jeu sur la plateforme se fait via un code de jeu unique à quatre chiffres donné à l'utilisateur. La compétence identifie les objets à découvrir et les stocke dans un enregistrement sur une table DynamoDB.

La logique dans Lambda enregistre également l'horodatage du début du jeu. Cela sert de chronomètre virtuel comptant les soixante minutes pour jouer. À tout moment, l'utilisateur peut demander à Alexa une mise à jour du score. Alexa répond avec le temps restant et un registre actuel des objets recherchés.

### Intelligence Artificielle #2 — Polly

J'aime intégrer une excellente expérience vocale utilisateur dans mes applications Alexa. La qualité différencie désormais les jeux sur cette plateforme en croissance. Cela est crucial étant donné qu'il existe désormais plus de 10 000 compétences Alexa parmi lesquelles choisir.

Développer d'excellentes interfaces vocales utilisateur est comme produire une émission de radio. Une bonne émission génère plus d'excitation qu'une seule voix. Elle inclut des jingles et des sons qui simulent l'action. L'écriture de ces applications nécessite à la fois du code et un récit narratif intéressant.

Les bonnes histoires ne sont pas des monologues. Cette approche nécessite un codage avancé pour inclure plus d'un personnage. C'est là que j'ai utilisé le [service Polly](https://aws.amazon.com/polly/), complétant la voix standard d'Alexa. Voici à quoi ressemble le « script » pour le message d'introduction. Cela se joue lors du démarrage d'une nouvelle partie et montre comment les composants interagissent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4WXpanxtzbRhsHs7BbqtJQ.png)

L'intégration de musique nécessite l'enregistrement de courts clips Mp3 contenant des sons et des jingles. J'enregistre la musique sur mon bureau, puis je la télécharge dans un bucket S3. Ensuite, voici comment avoir plusieurs voix dans la compétence, car Alexa n'en a qu'une. Pour créer cette expérience audio, c'est un hybride de techniques. Polly a la capacité de générer 47 voix différentes dans 24 langues différentes. C'est facile à utiliser, et un court enregistrement prend quelques minutes. Commencez par aller dans la console et lancez le service Polly.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4so0tIiQ-VpLw0zi-8eFXQ.png)

Il y a de nombreuses voix dans la langue anglaise parmi lesquelles choisir. J'ai sélectionné l'anglais, Royaume-Uni dans la liste déroulante, et j'ai cliqué sur le bouton radio pour une voix féminine nommée Amy. Ensuite, j'ai tapé mon script dans la zone de texte, et Polly l'a converti en parole. L'option en bas à droite sauvegarde l'enregistrement dans un fichier Mp3. J'ai mis le fichier dans un bucket S3 où il est accessible à la compétence Alexa.

#### Intégration des voix utilisant SSML

La section précédente a décrit comment créer les différentes parties du script. Maintenant, il est temps de les rassembler. La plateforme Alexa exige que chaque compétence ait une API qui respecte un modèle de message standard. Dans ce modèle, différents attributs représentent les caractéristiques de l'interaction utilisateur. L'attribut audioOutput de l'objet de réponse est ce qu'Alexa lit à l'utilisateur.

Pour créer l'attribut avec les quatre parties, vous devez créer un balisage qui ressemble à ceci :

```
<speak>
  <audio src=\"https://s3.amazonaws.com/.../introClip.mp3\" />
  <audio src=\"https://s3.amazonaws.com/.../pollyVoice.mp3\" />
  L'utilisation de la voix naturelle d'Alexa ne nécessite aucun balisage
  <audio src=\"https://s3.amazonaws.com/.../closingClip.mp3\" />
</speak>
```

Le balisage pointe vers chaque fichier mp3 mis en scène dans un emplacement accessible publiquement sur Internet. C'est aussi ainsi qu'un navigateur assemble des images et du texte en utilisant HTML dans un seul panneau de verre. Alexa fait de même avec l'assemblage audio en utilisant SSML.

### Intelligence Artificielle #3 — Rekognition

Le jeu nécessite un marqueur de score, donc un autre service joue ce rôle. Le cerveau derrière notre officiel moderne est le [service AWS Rekognition](https://aws.amazon.com/rekognition/). Celui-ci scanne les images, identifie tous les objets visibles et les suit pour le jeu. Voici les détails sur la technologie de support.

#### Traitement d'images piloté par événements

Les images sont téléchargées vers un bucket S3 via le site web scavengerskill.com. Le bucket est configuré pour déclencher un événement pour chaque nouvel objet ajouté. Cet événement exécute une fonction Lambda, appelant l'API Rekognition pour scanner l'image. La réponse de l'appel API contient les objets détectés. La fonction écrit les détails dans une table DynamoDB, les rendant disponibles pour la compétence Alexa.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vhHY-KONpFYYCroJjTXC-Q.png)

Par exemple, voici une photo d'un jeu et la réponse correspondante de l'API Rekognition.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LXw2RttveXJpxWz_EIhE3A.jpeg)

```
{
 "captureDt": "2017–04–16",
 "captureTm": "21:45:40",
 "gameId": "9180",
 "imageId": "9180/upload_13277b04a3c001948f3e570580f377c4.JPG",
 "labels": [
   { "Confidence": 98.8132629395, "Name": "Couch" },
   { "Confidence": 98.8132629395, "Name": "Furniture" },
   { "Confidence": 85.2093963623, "Name": "Lamp" },
   { "Confidence": 85.2093963623, "Name": "Table Lamp" },
   { "Confidence": 83.6216506958, "Name": "Coffee Table" },
   { "Confidence": 83.6216506958, "Name": "Table" },
   { "Confidence": 66.3723068237, "Name": "Dining Table" },
   { "Confidence": 54.6450958252, "Name": "Hardwood" },
   { "Confidence": 54.6450958252, "Name": "Wood" },
   { "Confidence": 52.6244163513, "Name": "Beverage" },
   { "Confidence": 52.6244163513, "Name": "Drink" },
   { "Confidence": 52.0414428711, "Name": "Lampshade" },
   { "Confidence": 50.595413208, "Name": "Dining Room" },
   { "Confidence": 50.595413208, "Name": "Indoors" },
   { "Confidence": 50.595413208, "Name": "Room" }
 ]
}
```

La réponse contient un tableau d'étiquettes applicables à la photo et un intervalle de confiance pour chacune. Dans ce jeu, je cherchais une « Lamp » et le service l'a identifiée dans la photo avec une certitude de 85 %. Le marqueur de score m'a crédité de l'avoir trouvée !

#### Amazon démocratise le traitement d'images

La valeur du service Rekognition réside dans sa simplicité. Amazon a déjà formé les modèles de machine learning pour reconnaître de nombreux objets. Tout ce que je dois faire pour utiliser le service est d'appeler l'API avec l'adresse de l'objet que je veux scanner. Cela rend un service très puissant simple et peu coûteux. Si je scanne 1 000 images, cela me coûte 1 $. Cela me permet de me concentrer sur la création de l'expérience utilisateur, y compris un gameplay excitant.

### Conclusion

J'aime jouer à cette version moderne de la chasse au trésor avec ma famille. C'est amusant de courir dans le jardin en prenant des photos des objets dans la maison et le quartier, puis de vérifier avec Alexa les objets qu'elle correspond. Veuillez l'essayer et faites-moi savoir ce que vous en pensez !

> « Oh, les endroits où tu iras ! Il y a du plaisir à faire ! 
> Il y a des points à marquer. Il y a des jeux à gagner. 
> Et les choses magiques que tu peux faire avec cette balle 
> feront de toi le gagnant le plus gagnant de tous. » 
>   
> — **Dr. Seuss**, **Oh, The Places You’ll Go!**