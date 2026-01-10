---
title: 'Événement Snap : Comment créer des événements de calendrier simplement en
  prenant une photo'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-24T02:09:36.000Z'
originalURL: https://freecodecamp.org/news/snap-events-how-you-can-now-create-calendar-events-just-by-taking-a-picture-af21f3bfaeef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tKKgP6X-F2JtaXPhgBb_Cg.jpeg
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Événement Snap : Comment créer des événements de calendrier simplement
  en prenant une photo'
seo_desc: 'By Arjun Krishna Babu

  Google just published my first Android app, Snap Event, in their Play Store. Snap
  Event creates calendar events from photographs of the event’s poster.

  The app is by no means perfect, but it’s functional and is a proof of concep...'
---

Par Arjun Krishna Babu

Google vient de publier ma première application Android, [Snap Event](https://play.google.com/store/apps/details?id=io.github.arjunkrishnababu96.snapevent), dans leur Play Store. Snap Event crée des événements de calendrier à partir de photographies de l'affiche de l'événement.

L'application n'est en aucun cas parfaite, mais elle est fonctionnelle et constitue une preuve de concept que l'idée fonctionne.

Cet article est un compte rendu de la manière dont j'ai construit et publié cette application.

### Motivation

Les gens disent que la meilleure façon d'apprendre un nouveau langage de programmation ou un framework est de faire un projet avec. Bien sûr, vous avez besoin d'une certaine familiarité avec les bases de ce que vous essayez d'apprendre. Mais passé ce stade, les projets sont la voie à suivre.

Il y avait trois facteurs motivants derrière le développement de cette application :

1. Ma précédente tentative d'apprentissage d'Android il y a deux ans avait échoué. Je voulais lui donner une autre chance.
2. J'avais déjà une idée de projet en tête.
3. L'un de mes professeurs nous a demandé à chacun de construire une application Android. Nous obtiendrions des crédits pour cela.

Chaque fois que je voyais une affiche pour un événement, comme un concert ou une conférence, je prenais sa photo pour garder une trace de ce qui était exactement sur l'affiche. La plupart des gens que je connaissais faisaient cela. J'ai cherché, mais je n'ai pas trouvé d'application qui convertit les images d'affiches en événements de calendrier. C'était surprenant. Ou peut-être que je n'ai pas assez bien cherché.

Alors, mon ami [Alexander "Alex" Kaberlein](https://github.com/akaberlein) et moi avons décidé de construire cette application.

### Développement de l'application

Créer des événements de calendrier à partir de leurs affiches se résume à trois choses :

1. Détecter le texte à partir de l'image.
2. Comprendre le texte détecté.
3. Créer un événement de calendrier.

Notre objectif était de livrer une application fonctionnelle le plus tôt possible, puis de corriger ses défauts. Par conséquent, nous avons fait quelques compromis pendant la phase de conception. Cela devait être une expérience d'apprentissage, après tout. Nous n'avons aucune intention de gagner de l'argent avec cette application.

#### Détection de texte à partir de l'image

Bien que, rétrospectivement, l'étape deux était plus difficile, notre projet aurait pu être abandonné immédiatement si nous avions échoué à détecter le texte à partir de l'image. Je n'avais aucune connaissance en vision par ordinateur. Alex avait une certaine familiarité avec [OpenCV](http://opencv.org/), mais nous n'avions pas assez de temps pour développer nos propres modèles de reconnaissance d'image.

Sur la base de ce que j'ai lu sur Internet, j'étais conscient de certaines bibliothèques et services prêts à l'emploi pour la reconnaissance d'image. En particulier, les trois services que nous avons considérés étaient :

1. [Amazon Rekognition](https://aws.amazon.com/rekognition/)
2. [Google Cloud Vision](https://cloud.google.com/vision/)
3. [Google Mobile Vision](https://developers.google.com/vision/)

Il ne nous a pas fallu longtemps pour nous décider pour [Google Mobile Vision](https://developers.google.com/vision/) :

* Amazon Rekognition était supposé être très bon pour détecter les objets dans l'image. Mais nous ne savions pas comment il fonctionnait avec le texte.
* Cloud Vision était capable de détecter le texte, mais il n'est pas gratuit (malgré son coût peu élevé).
* Mobile Vision était capable de détecter le texte, gratuit, et probablement bien intégré avec Android.

Nous avons donc choisi Mobile Vision.

Ensuite, nous voulions être sûrs que Mobile Vision détectait le texte à notre satisfaction. Nous ne voulions pas découvrir au dernier moment que Mobile Vision n'était pas à la tâche. Pour cela, nous avons construit une petite application jouet pour détecter le texte à partir d'images que nous avons codées en dur dans l'application. Vous pouvez la trouver [ici](https://github.com/arjunkrishnababu96/mobile-vision-prototype).

Le prototype a bien fonctionné, et nous avons décidé de procéder à l'application principale.

Capturer l'image et l'enregistrer sur le téléphone était plus facile que je ne le pensais. Cependant, je voulais afficher toutes les images prises par l'application dans des cartes à défilement vertical. C'est là que j'ai rencontré mon premier ensemble majeur de problèmes :

* Les images haute résolution prennent beaucoup de mémoire, ce qui fait trembler les défilements. Cela malgré l'utilisation de `[RecyclerView](https://developer.android.com/guide/topics/ui/layout/recyclerview.html)`.
* Centrer les images dans les cartes était plus difficile que je ne le pensais. Vous devez manipuler un objet `[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap.html)` et faire des calculs mathématiques non triviaux.

La documentation Android (précisément [cette](https://developer.android.com/topic/performance/graphics/index.html) page) m'a orienté vers des solutions pour ces deux problèmes. Il existe une bibliothèque appelée [Glide](https://github.com/bumptech/glide) qui gère les complexités associées à l'importation de plusieurs images dans votre application. Elle gère également les désagréments comme le centrage correct de vos images dans votre `ImageView`.

La documentation pour Glide aurait pu être meilleure. J'ai dû recourir à des sites tiers pour comprendre certains cas d'utilisation. À ce propos, vous pourriez vouloir lire [cette excellente introduction à Glide](https://inthecheesefactory.com/blog/get-to-know-glide-recommended-by-google/en).

#### Reconnaissance de texte utilisant Mobile Vision

Mobile Vision supporte :

1. [Détection de visage](https://developers.google.com/vision/face-detection-concepts)
2. [Détection de code-barres](https://developers.google.com/vision/android/barcodes-overview)
3. [Détection de texte](https://developers.google.com/vision/text-overview), ce que nous voulions.

La bibliothèque est capable de nous fournir du texte dans le format que nous désirons. Il peut s'agir de blocs de texte entiers, de lignes, de mots, etc. Notre plan d'attaque était d'extraire chaque ligne de texte dans l'affiche, puis de déterminer ce que chacune de ces lignes signifiait.

Il y avait quelques choses que j'ai remarquées concernant la détection de texte utilisant Mobile Vision :

* Cela ne fonctionne pas bien avec le texte manuscrit.
* Les lignes de texte extraites ne sont pas toujours dans l'ordre de haut en bas.
* Le texte détecté diffère parfois pour la même image sur plusieurs exécutions — un comportement non déterministe inattendu.
* Cela plante occasionnellement lors de l'utilisation du format `.jpg` pour les images. J'ai eu recours à l'utilisation de formats `.png`.
* Utilisez la méthodologie `ARGV_8888` pour stocker les pixels en mémoire. Il m'a fallu des heures pour comprendre pourquoi mon application continuait à planter. Une partie de mon application utilisait `RGB_565` par défaut, et une autre partie attendait des images en `ARGV_8888`. Voir [cette](https://developer.android.com/reference/android/graphics/Bitmap.Config.html) page pour en savoir plus sur ce que signifient ces configurations.

#### Comprendre le texte

Alex et moi avons conclu que pour tout événement de calendrier, les trois éléments cruciaux d'information sont :

* Horaire
* Titre
* Lieu

Le problème avec les dates est qu'elles sont écrites différemment dans différentes parties du monde. Par exemple, "05–07–2017" est le 7 mai aux États-Unis et le 5 juillet dans presque tous les autres pays. Des idées étranges impliquant des astuces avec la localisation géographique de l'utilisateur m'ont traversé l'esprit, mais cela ne semblait pas correct. De plus, dans des pays comme les États-Unis où des gens du monde entier sont présents, cette idée n'est pas infaillible.

En raison de ces complications, nous avons décidé de déduire le mois uniquement lorsqu'il est écrit en entier, comme "January" (ou sa forme abrégée "Jan."). Bien que ce ne soit pas toujours vrai, il est quelque peu sûr de supposer que la date et l'année seraient sur la même ligne que le mois.

Notre méthodologie pour détecter le titre et le lieu de l'événement est si terrible que je préfère ne pas en parler. Pour une ligne de texte donnée, je n'ai pas de stratégie fiable pour déterminer de manière concluante s'il s'agit d'un titre d'événement, d'un lieu ou d'une autre information.

Pour compenser cela, nous mettons chaque ligne de texte que nous détectons dans le champ de description de l'événement de calendrier.

#### Création de l'événement de calendrier

Une tâche triviale dans le grand schéma des choses.

Android stocke tous les événements de calendrier dans un dépôt central appelé le [Calendar Provider](https://developer.android.com/guide/topics/providers/calendar-provider.html). C'est pourquoi les événements de calendrier que vous créez en utilisant _n'importe quelle_ application de calendrier apparaissent sur toute autre application de calendrier que vous installez. Pensez-y de cette manière — tous les fichiers multimédias de votre téléphone apparaîtraient sur n'importe quel lecteur multimédia que vous installez.

Une fois que toutes les informations nécessaires à la création d'un événement de calendrier sont prêtes, il ne reste plus qu'à démarrer une activité pour créer l'événement de calendrier.

Nous avons choisi d'ouvrir l'application de calendrier avec les informations de l'événement pour donner aux utilisateurs l'opportunité de passer en revue l'événement avant qu'il ne soit enregistré. Sinon, il créerait silencieusement l'événement de calendrier en arrière-plan.

### Publication sur Google Play Store

Comme la plupart des autres choses de Google, les étapes pour publier une application Android sont bien documentées. Une fois que je me suis senti prêt à lancer l'application, j'ai suivi la [checklist de lancement officielle](https://developer.android.com/distribute/best-practices/launch/launch-checklist.html).

Ce n'était pas un processus rapide, cependant. Il leur a fallu plus de 24 heures pour vérifier mes frais d'inscription uniques de 25 $, et 6 heures de plus pour que mon application apparaisse sur le Google Play Store après avoir cliqué sur le bouton pour déployer et publier l'application.

### Ce que j'ai appris en développant cette application

* Programmation Android de base. Je suis maintenant confiant pour lire la documentation (ainsi que d'autres ressources) pour comprendre comment faire les choses. Maintenant, je peux créer des applications Android plus complexes à l'avenir.
* Comment publier réellement l'application Android.
* Comment utiliser la bibliothèque Glide pour afficher plusieurs images efficacement.
* Comment configurer et utiliser la bibliothèque Google Mobile Vision.

### Lacunes

J'ai déjà couvert de nombreuses lacunes de l'application dans la section [Développement de l'application](https://arjunkrishnababu96.github.io/Introducing-SnapEvent/#app-development) ci-dessus. Mais je vais résumer les problèmes ici :

* La détection de date ne se produit que si la date est écrite en entier.   
Dans le monde réel, les dates ne sont pas toujours écrites en entier. Cela limite sévèrement l'utilité de l'application.
* La détection de date échoue si elle contient des suffixes ordinaux comme "st", "nd", "rd" ou "th". Cependant, cela peut être rapidement corrigé.
* La détection du titre et du lieu de l'événement ne sont pas parfaites. J'envisage d'utiliser des modèles de machine learning pour accomplir cette tâche, mais c'est encore assez loin.
* Les images sont enregistrées sur le téléphone en utilisant une stratégie terrible dont j'ai honte de mentionner ici. Même si cela fonctionne parfaitement. Cela serait évident uniquement si vous lisez le code source.
* L'expérience utilisateur peut être améliorée.

### Et ensuite

Je vais corriger les choses relativement faciles que j'ai mentionnées dans la [section des lacunes](https://arjunkrishnababu96.github.io/Introducing-SnapEvent/#shortcomings). Mais je ne vais probablement pas poursuivre ce projet beaucoup plus loin pour des raisons que je mentionne ensuite.

#### Google Lens

Parmi les nombreuses choses passionnantes que Google a annoncées lors de [Google I/O](https://events.google.com/io/) 2017, il y a Google Lens. Google Lens fait exactement ce que notre application fait (ainsi qu'un tas d'autres choses cool). Et Google Lens le fait plutôt bien, beaucoup mieux que ce que j'ai créé avec Snap Event.

Et je suis heureux et excité par le fait que Google l'ait fait. Au moins, je m'attends à ce qu'il soit beaucoup plus fiable et utile.

### Obtenez Snap Event

* Comme mentionné, [Snap Event est maintenant disponible sur Google Play](https://play.google.com/store/apps/details?id=io.github.arjunkrishnababu96.snapevent).
* Le code source de l'application est disponible sur [GitHub](https://github.com/arjunkrishnababu96/snap-event).

Vous pouvez lire plus de mes projets [sur mon blog](https://arjunkrishnababu96.github.io/Introducing-SnapEvent/).