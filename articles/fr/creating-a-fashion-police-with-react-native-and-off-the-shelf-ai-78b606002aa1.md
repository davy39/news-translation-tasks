---
title: Comment créer une "police de la mode" avec React Native et une IA prête à l'emploi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-17T17:41:39.000Z'
originalURL: https://freecodecamp.org/news/creating-a-fashion-police-with-react-native-and-off-the-shelf-ai-78b606002aa1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*buihVJMdtoCO0q0GhwR3jg.jpeg
tags:
- name: app development
  slug: app-development
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
seo_title: Comment créer une "police de la mode" avec React Native et une IA prête
  à l'emploi
seo_desc: 'By Kelsey Wang

  Imagine you’ve just stumbled into a Nordstrom at your local mall, lost in the Slenderman-looking
  mannequins and racks of overpriced coats. Or, more realistically, you’re browsing
  online because you’re too lazy to go to the store. You’r...'
---

Par Kelsey Wang

Imaginez que vous venez de tomber sur un Nordstrom dans votre centre commercial local, perdu parmi les mannequins qui ressemblent à Slenderman et les racks de manteaux surévalués. Ou, plus réalistement, vous naviguez en ligne parce que vous êtes trop paresseux pour aller en magasin. Vous essayez de trouver un cadeau d'anniversaire pour votre ami, mais vous n'avez aucune idée de ce qu'il aimerait. Quel est son style ? Veut-il une chemise noire déchirée ou un pull rayé vert et blanc ? Vous devriez le savoir, mais ce n'est pas le cas.

Pas besoin d'avoir peur, car **la police de la mode personnalisable et artificiellement intelligente est là.** Nous allons utiliser les services "prêts à l'emploi" [Custom Vision](https://www.customvision.ai/) de Microsoft pour classer les vêtements comme "mignons" ou "pas mignons" selon les données que vous lui avez fournies. Si vous faites des achats en ligne, vous pouvez simplement tester cela dans le navigateur, mais nous créerons également une application React Native simple pour utiliser le modèle d'IA sur les photos que vous pourriez prendre en magasin.

![Image](https://cdn-media-1.freecodecamp.org/images/6S4ELSHnu0COV5c3FgoySFbiPxLZEFEV6nES)
_Les racks de vêtements vous intimident ?? Lisez la suite !_

Bien sûr, les goûts sont subjectifs, donc le meilleur aspect est que vous adapterez l'application pour qu'elle corresponde au goût de votre ami (ou de votre partenaire, ou du vôtre) en matière de mode en téléchargeant des photos de vêtements qu'il aime et qu'il n'aime pas.

Encore une fois, pour faire cela relativement facilement et rapidement, nous utiliserons l'API de prédiction Custom Vision de Microsoft. Il existe d'autres services similaires, comme les services [AutoML Vision](https://cloud.google.com/vision/) de Google. Ceux-ci permettent aux personnes ayant une expérience limitée en apprentissage automatique ou en vision par ordinateur de créer et de former des modèles personnalisés pour, par exemple, classer des images avec des étiquettes peu communes. Ils sont relativement rapides et faciles à utiliser, parfaits pour ce type de projet.

### Mise en route

Pour commencer ce projet, vous devez créer un compte Azure et créer un nouveau projet, etc. Azure offre un essai gratuit, et j'ai simplement suivi les instructions [ici](https://docs.microsoft.com/fr-fr/azure/cognitive-services/custom-vision-service/getting-started-build-a-classifier).

Points à noter : assurez-vous de "changer de répertoire" vers le compte Azure que vous avez créé — sinon, il ne vous permettra pas de créer un nouveau projet de vision personnalisée. De plus, lorsque vous [créez le projet](https://www.customvision.ai/projects), notez que nous utilisons un classificateur multiclasse (et plus spécifiquement, un classificateur binaire), car chaque image doit simplement être étiquetée comme "mignonne" ou "pas mignonne".

![Image](https://cdn-media-1.freecodecamp.org/images/o-dro4nnLL7Xj1Gbfz8omBQkxC9hnhBIlo8M)
_Création du nouveau projet_

Une fois que vous avez déterminé le style de la personne pour laquelle vous souhaitez créer une émulation d'IA (appelons cette personne le _predictee_), vous devrez recueillir des informations sur le style du predictee. Plus il y en a, mieux c'est. Comme nous avons très peu de visibilité sur la manière exacte dont le modèle de prédiction est formé et ne pouvons pas ajuster aucune partie de celui-ci, nous devons le traiter comme une boîte noire. Cependant, comme pour la plupart des systèmes d'IA basés sur les données, plus vous lui fournissez des données de haute qualité et diversifiées, mieux il fonctionnera.

### Faire des achats en ligne pour un ami ? Pas besoin d'application !

Tout d'abord, j'ai testé les capacités de l'IA pour les achats en ligne. Cela a été assez facile car j'ai simplement pris des captures d'écran de photos de vêtements que j'aimais et que je n'aimais pas, et je les ai fournies au modèle. Il n'est pas nécessaire de créer une application pour cela — vous pouvez simplement l'entraîner et l'utiliser dans le [navigateur](https://www.customvision.ai).

#### Entraînement de l'IA

Nordstrom était en fait très bien pour cela car ils ont des photos de chaque article qu'ils vendent sans qu'une personne ne le porte, prises dans des conditions d'éclairage et des arrière-plans très similaires. Mon hypothèse est que le modèle fonctionnerait mieux dans ces conditions cohérentes, afin qu'il puisse peut-être distinguer les nuances de motif et de couleur plutôt que la couleur de l'arrière-plan ou la taille ou la couleur de peau des personnes.

J'ai en fait commencé avec seulement des chemises à manches courtes — j'ai sauvegardé 40 photos de celles que j'aimais et 40 de celles que je n'aimais pas. J'en ai choisi 30 au hasard pour chaque catégorie à donner au modèle de Microsoft pour l'entraînement, et j'ai sauvegardé 10 de chaque pour tester le modèle. Et oui, je sais que c'est un ensemble de données très petit, mais j'ai une vie en dehors des captures d'écran de Nordstrom :/

![Image](https://cdn-media-1.freecodecamp.org/images/0Pb9V3JYtLRhqSlPNxBV7xxKVLbRi8lNlrUB)
_Données d'entraînement étiquetées que j'ai entrées dans l'interface web Custom Vision_

#### Test de l'IA

Après l'entraînement, j'ai appliqué le modèle à mon ensemble de test de 10 chemises étiquetées "mignonnes" et 10 "pas mignonnes" en utilisant la fonctionnalité "Test rapide". J'ai obtenu les résultats suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/ZGNrviZ8CnCz7Zew8-Zu6q7Wz61aO3pClOR4)

Le _rappel_ — les vêtements réellement mignons correctement classés comme mignons — était de 8/10, soit 0,80. La _précision_ — les vêtements classés comme mignons qui étaient réellement mignons — était de 8/13, soit environ 0,62. Le [score F1](https://fr.wikipedia.org/wiki/F-mesure) est arrondi à 0,70. Pas génial, pas terrible, je dirais, pour un modèle prêt à l'emploi. Faites-en ce que vous voulez, mais je pense que c'est définitivement mieux qu'un ami ignorant pour choisir des vêtements pour moi.

Lorsque j'ai examiné les classifications de chaque image, j'ai vu que l'IA avait tendance à classer les images en fonction de la couleur. Si vous regardez les données d'entraînement ci-dessus, vous pouvez voir que je favorisais des couleurs plus unies comme le blanc, le noir et le bleu, tandis que les chemises brillantes étaient principalement étiquetées "pas mignonnes".

![Image](https://cdn-media-1.freecodecamp.org/images/koq3Vi62EEJVOLmDg97TBM0lYEVM1ncp6rIW)
_Le classificateur avait raison sur celle-ci._

Cette vision simpliste de mon goût ne fonctionnait pas toujours, cependant. Regardons quelques autres exemples.

![Image](https://cdn-media-1.freecodecamp.org/images/uQRzq7cITyyl51gGfxV8pVxzb2WXNJsLtjFX)

L'IA n'a pas vraiment compris le "style" des chemises, seulement la couleur. J'ai étiqueté beaucoup de chemises avec des "plis" (comme dans l'épaule de la chemise grise ci-dessus) comme "pas mignonnes", pourtant l'IA a toujours classé la chemise grise comme mignonne. La chemise rouge ci-dessus aurait peut-être été trop brillante pour être classée comme "mignonne" et a donc été mal classée. Donc oui, l'IA ne s'en est pas trop mal sortie car après tout, la couleur _est_ un grand facteur qui influence mon propre style, mais elle semblait aussi échouer à saisir des nuances plus subtiles de mon goût.

### Allez en magasin ? Vous aurez besoin d'une application pour cela.

Je voulais aussi tester les capacités de l'IA dans la nature — comme prendre des photos de vêtements dans un magasin et utiliser cela pour décider d'acheter ou non un certain vêtement.

Créer une application pour soi est plus facile que jamais, alors ne vous inquiétez pas — nous ne allons pas déployer complètement sur l'App Store. Cela prend trop de temps, de toute façon. J'ai utilisé [React Native](http://www.reactnative.com/) pour rapidement mettre ensemble une application multiplateforme (fonctionne sur iPhones et Androids) avec la fonctionnalité dont j'avais besoin.

La fonctionnalité ? Eh bien, ce serait la capacité de prendre une photo d'un vêtement et d'avoir l'IA prédire instantanément si le predictee le jugerait "mignon" ou non. Donc **nous devons pouvoir utiliser l'appareil photo du téléphone, pouvoir prendre des photos, utiliser l'API de prédiction Microsoft sur les photos que nous prenons en temps réel, et transmettre les résultats à l'utilisateur.** Cela est assez facile à faire avec les services d'[Expo](https://expo.io/), et si vous voulez plonger dans les détails, tout mon code est disponible sur [Github](https://github.com/kelseyywang/fAshIon-police).

#### Une note à propos de l'API de prédiction

La partie la plus confuse de la création de cela a été d'essayer d'envoyer le fichier image pris depuis l'appareil photo du téléphone directement via le point de terminaison de l'API. Vous êtes censé envoyer les données sous forme de "flux d'octets", et il y a très peu de support ou de documentation à ce sujet de la part de Microsoft. J'ai essayé d'envoyer une image encodée en binaire, j'ai essayé d'envoyer le fichier image dans un format de données de formulaire, j'ai essayé de redimensionner l'image puis de faire une combinaison des méthodes ci-dessus — mais rien de ce que j'ai essayé n'a fonctionné.

Pour être honnête, j'ai passé des heures et des heures à essayer de comprendre pourquoi rien ne me donnait une bonne réponse. Finalement, j'ai demandé à un ami d'un ami qui avait en fait rencontré ce problème exact auparavant, et il a dit qu'il avait finalement abandonné l'idée d'envoyer directement le fichier image, et avait plutôt utilisé une autre API pour télécharger l'image d'abord, puis envoyer l'URL web de l'image.

En entendant cela, j'ai admis ma défaite et adopté cette solution : j'ai utilisé l'[API Imgur](https://apidocs.imgur.com/) pour télécharger les images prises depuis le téléphone, puis [envoyer l'URL web de l'image](https://docs.microsoft.com/fr-fr/azure/cognitive-services/custom-vision-service/use-prediction-api).

#### En tout cas...

Après cela, l'application a fonctionné ! Et l'IA a fonctionné de manière surprenamment similaire à la façon dont elle s'est comportée sur l'ensemble de test de Nordstrom. Elle était toujours entraînée sur les images de Nordstrom.com, donc voyez les résultats suivants sur quelques vêtements que je possède déjà :

![Image](https://cdn-media-1.freecodecamp.org/images/ousTUOb2sGofYA94Upv4uUaB5Nc8CuAPUKW4)

Vous pouvez voir à quel point l'IA est confiante dans le classement de la chemise noire comme "mignonne" et de la chemise rayée comme "pas mignonne". C'est bien car cela montre que l'IA n'a pas été fortement influencée par les nouvelles conditions d'éclairage, et c'est mauvais (mais attendu) car elle semble toujours perpétuer la vision simpliste de "couleurs ternes mignonnes, couleurs vives pas mignonnes". Mais dans l'ensemble — c'est assez cool de pouvoir utiliser cette "police de la mode" dans la vie réelle !

### Réflexions finales

Eh bien, c'était amusant ! Il y a quelques choses ~excitant mais faciles~ que j'ai finalement ajoutées, comme varier aléatoirement le langage qui est rapporté par l'IA, en disant des choses comme "J'aime ça !!" ou "Ne gaspillez pas votre argent..." au lieu des simples étiquettes "mignon" et "pas mignon". Le meilleur aspect de cette application est qu'elle est complètement ouverte et adaptable — vous pouvez changer l'expérience utilisateur ou littéralement l'entraîner sur n'importe quoi pour qu'elle prédise un monument, un panneau de signalisation, ou même [un hot-dog ou pas un hot-dog](https://youtu.be/ACmydtFDTGs).

J'ai également fait une petite vidéo sur l'utilisation de cela dans la vie réelle pour lancer ma chaîne YouTube nerd. Vous pouvez la regarder [ici](https://youtu.be/yonPtreuTdE) si vous voulez voir l'application appliquée pour faire de vrais choix de mode (et me regarder être maladroit devant une caméra) !

Merci d'avoir lu :)