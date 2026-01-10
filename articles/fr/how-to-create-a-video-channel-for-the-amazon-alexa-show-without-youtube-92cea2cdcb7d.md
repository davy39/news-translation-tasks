---
title: Comment créer une chaîne vidéo pour l'Amazon Alexa Show sans YouTube
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T13:04:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-video-channel-for-the-amazon-alexa-show-without-youtube-92cea2cdcb7d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yF98uEJJ2R1z3sxd8eAZ6Q.png
tags:
- name: Alexa
  slug: alexa
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: videos
  slug: videos
- name: youtube
  slug: youtube
seo_title: Comment créer une chaîne vidéo pour l'Amazon Alexa Show sans YouTube
seo_desc: 'By Terren Peterson

  I’m a software engineer that has published more than twenty custom skills on the
  Alexa platform. I’ve been recognized as an Alexa Champion, and have won multiple
  hackathons using the technology. The following highlights how I built...'
---

Par Terren Peterson

Je suis un ingénieur logiciel qui a publié plus de vingt compétences personnalisées sur la plateforme Alexa. J'ai été reconnu comme un [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson), et j'ai remporté plusieurs hackathons en utilisant cette technologie. Ce qui suit met en lumière comment j'ai construit une compétence vidéo personnalisée pour l'Echo Show en utilisant la technologie native d'Amazon.

### L'Histoire de la Consommation Vidéo

La diffusion vidéo a été un medium réussi depuis plus de [soixante ans](https://en.wikipedia.org/wiki/History_of_television). Les téléviseurs ont dominé l'industrie du divertissement pendant des décennies avec des signaux de diffusion envoyés directement dans les salons. En [1990,](https://www.ncta.com/cables-story) la télévision par câble avait atteint 57% des foyers américains. Cela a rapidement élargi la variété de contenu consommé par les téléspectateurs.

Le streaming en direct a officiellement commencé en [1995](https://www.theguardian.com/media-network/media-network-blog/2013/mar/01/history-streaming-future-connected-tv), mais ce n'est qu'en 2007 que le streaming basé sur internet a commencé à utiliser le protocole standard HTTP. Les smartphones comme l'iPhone ont été ajoutés peu après en utilisant des méthodes de communication similaires. Avec la poussée vers le mobile, les petits écrans ont commencé à prendre plus de notre temps. YouTube a été un énorme succès pendant cette phase, et diffuse maintenant [5 milliards de vidéos par jour](https://www.bluleadz.com/blog/25-eye-opening-youtube-statistics-infographic).

En 2015, [Amazon a lancé](https://www.androidcentral.com/amazon-echo-now-available-everyone-buy-17999-shipments-start-july-14) le premier appareil contrôlé uniquement par la voix de l'utilisateur. Les plateformes vocales comme Alexa ont rapidement ajouté un autre appareil à la maison, avec une [estimation de 35 millions](https://techcrunch.com/2017/11/08/voice-enabled-smart-speakers-to-reach-55-of-u-s-households-by-2022-says-report/) déjà utilisés aux États-Unis. En [2017](https://www.macrumors.com/2017/05/09/amazon-echo-show-june/), Amazon a officiellement lancé leur première version d'Alexa avec un écran, appelée l'Echo Show. Les [nouveaux appareils Amazon Fire TV](https://www.theverge.com/circuitbreaker/2017/9/11/16287812/amazon-new-fire-tv-2017-alexa) ont également Alexa intégré, permettant de contrôler le streaming vidéo sur un écran plat par la voix.

L'Echo Show incluait initialement la capacité de lire des vidéos depuis YouTube, mais récemment, Google et Amazon [se sont disputés](http://variety.com/2017/digital/news/amazon-echo-show-sales-down-youtube-1202582660/) concernant sa disponibilité. Cela a impacté la popularité du produit étant donné l'importance de la fonction de lecture vidéo.

Lors du [CES 2018](https://www.cnet.com/news/google-home-assistant-smart-displays-echo-show-lenovo-lg-sony-jbl-ces-2018/), plusieurs entreprises d'électronique grand public ont annoncé qu'elles lançaient un appareil compatible avec Google Home avec un écran. Cela rend le marché de la voix encore plus compétitif. Une solution au défi de compatibilité avec YouTube est d'héberger le contenu vidéo directement sur Amazon. Ce qui suit décrit comment créer une compétence personnalisée pour l'Echo Show qui fait exactement cela.

### Comment Créer une Compétence Vidéo Personnalisée sur Alexa

Créer votre propre chaîne vidéo est surprenamment facile en utilisant Alexa et quelques services AWS. Voici l'architecture mettant en vedette une compétence Alexa personnalisée qui package le contenu à lire sur un Echo Show. Le service de stockage AWS (S3) stocke les médias et les diffuse vers l'appareil en fonction des instructions données par la compétence personnalisée.

![Image](https://cdn-media-1.freecodecamp.org/images/2xU4Q2AmV3qQfrKVwBMppDWKgmt1hUjJmWGz)
_Architecture de Niveau Composant pour une Compétence Vidéo Personnalisée_

Produire du contenu pour cela est comparable à ce qui est requis pour une chaîne YouTube. La version actuelle de l'Echo Show (ainsi que l'Echo Spot) a des spécifications autour du type de média à suivre. Par exemple, la vidéo doit utiliser une extension mp4 et un format de compression standard [H.264](https://en.wikipedia.org/wiki/H.264/MPEG-4_AVC). La résolution de la qualité vidéo ne doit pas être supérieure à 1280x720 en taille de pixel. Ces contraintes fournissent un flux vidéo de haute qualité sur l'écran de sept pouces du Show, comparable à celui d'un lecteur vidéo HD.

### Construction de la Compétence Vidéo Personnalisée

Créer une chaîne vidéo nécessite de rédiger une compétence personnalisée pour Alexa et de la publier dans le magasin de compétences public. Il y a un certain nombre de fonctionnalités nécessaires pour naviguer dans le contenu de la chaîne et lire les vidéos. Cette section couvrira ces étapes en détail. Pour un exemple fonctionnel, essayez la compétence Piano Teacher qui est déjà dans le [magasin Alexa](https://www.amazon.com/Piano-Teacher-video-Echo-Show/dp/B078M9843X/). Il s'agit d'une compétence qui contient des vidéos courtes avec des leçons pour débutants sur la façon de jouer du piano, ainsi que des instructions vidéo note par note sur la façon de jouer des chansons simples. [Voici](https://github.com/terrenjpeterson/pianoplayer) le dépôt qui contient tout le code source nécessaire, ainsi que des instructions détaillées pour configurer et déployer.

Il y a trois fonctionnalités requises pour créer une chaîne vidéo.

1 — Rendre une image de fond lorsque la compétence est initialement lancée. Cela établit la marque de la chaîne.  
2 — Construire des contrôles de navigation pour parcourir et sélectionner quelle vidéo lire. Cela inclut la gestion des gestes tactiles sur l'écran de l'Echo Show.  
3 — Déléguer le contrôle à l'appareil pour lire une vidéo une fois le contenu sélectionné.

#### 1 — Marque avec une Image de Fond

Pour faciliter la construction de compétences vidéo personnalisées, Alexa fournit une série de modèles. J'utilise le modèle « BodyTemplate1 » pour rendre l'image de fond lorsque la compétence est invoquée pour la première fois. Lors de la génération des métadonnées dans la console de développement Alexa, cochez les deuxième et troisième cases sur l'écran des champs globaux (Video App & Render Template).

![Image](https://cdn-media-1.freecodecamp.org/images/8sZgyh5SKjVkQhGa7z0VXsUsfTy40xsVyG1T)

La définition de ces attributs active des API supplémentaires dans la compétence personnalisée. Des intentions standard supplémentaires sont requises pour utiliser les API. Elles sont créées lors de la construction du modèle d'intention dans le kit de compétences. Elles sont les suivantes :

* AMAZON.NavigateSettingsIntent
* AMAZON.NextIntent
* AMAZON.PageDownIntent
* AMAZON.PageUpIntent
* AMAZON.PreviousIntent
* AMAZON.ScrollDownIntent
* AMAZON.ScrollLeftIntent
* AMAZON.ScrollRightIntent
* AMAZON.ScrollUpIntent

Aucun codage dans la fonction Lambda n'est requis pour ces événements, car l'appareil les gérera nativement. Ils doivent simplement être inclus dans le modèle d'intention de vos compétences personnalisées.

Le rendu d'une image de fond nécessite deux méthodes utilitaires qui sont déjà distribuées dans le SDK Alexa standard. La compétence crée deux identifiants pour illustrer comment elles sont utilisées.

```js
// méthodes utilitaires pour créer des objets Image et TextField

const makePlainText = Alexa.utils.TextUtils.makePlainText;
const makeImage     = Alexa.utils.ImageUtils.makeImage;
```

Ensuite, j'ajoute un identifiant pour l'emplacement de votre fichier jpg/png qui sert d'image de fond. Cet objet doit être publiquement disponible. La taille en pixels est de 1024x600 basée sur les dimensions de l'Echo Show. Vous n'avez pas besoin de fournir une image séparée pour le plus petit Echo Spot. Alexa crée l'image plus petite basée sur le fichier d'origine dimensionné pour le Show.

```js
// Il s'agit d'un point de terminaison public - le moyen le plus simple est de l'héberger dans S3
// Il doit être activé SSL (ce que S3 fait pour vous)

const backgroundImage = 'https://s3.amazonaws.com/.../image.jpg';
```

Ensuite, ajoutez le code suivant pour rendre l'image de fond lorsque la compétence est lancée, ainsi que tout autre message audio.

```js
'LaunchRequest': function () { 
  const builder = new Alexa.templateBuilders.BodyTemplate1Builder();
  const template = builder.setTitle('Votre Professeur Personnel')
      .setBackgroundImage(makeImage(backgroundImage))
      .setTextContent(makePlainText('Professeur de Piano')) 
      .build();
      
  // vérifier si l'appareil a un écran vidéo
  if (this.event.context.System.device.supportedInterfaces.Display){      
    this.response.speak(welcomeMessage)
        .listen(repeatWelcomeMessage).renderTemplate(template);
    this.emit(':responseReady');
  } else {
    // gérer l'erreur de ne pas avoir d'écran vidéo pour lire
    this.emit(':tell', nonVideoMessage);
  } 
},
```

#### 2 — Navigation du Contenu

La navigation pour le contenu tire parti de la flexibilité de la plateforme Alexa. Le spectateur peut utiliser soit sa voix soit ses doigts pour naviguer dans le catalogue de contenu, en sélectionnant exactement ce qu'il souhaite voir. Cela nécessite l'utilisation du modèle de liste dans le SDK Alexa, ainsi que la gestion des événements déclenchés par l'utilisateur touchant l'écran.

Voici les différentes options que l'utilisateur peut demander en utilisant soit sa voix soit en touchant l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1DKSPxIQBKi6Zz8ile8GVUV4YzQL26Xh1Wr1)

Le rendu d'une liste de ce qui est disponible est central pour l'expérience utilisateur. J'utilise 'ListTemplate1' du SDK Alexa pour rendre la liste des vidéos. Le défilement vers le haut et vers le bas peut être fait soit par la voix soit par le toucher, et est géré par l'appareil sans codage requis.

L'objet de réponse envoyé pour lister le contenu contient un tableau listant ce qui est disponible sur la chaîne. Dans ma compétence, cette liste est lue par la voix d'Alexa et est rendue visuellement sur l'écran. Voici un exemple de ce à quoi cela ressemble.

![Image](https://cdn-media-1.freecodecamp.org/images/ULRD5TKnXiNO4c35VuKDNOYhHO55e8jzUzEX)
_Capture d'écran de la Compétence Piano Teacher sur un Alexa Show_

Dans le code, le contenu est externalisé dans un objet de tableau (songs.json) qui contient une liste de vidéos, ainsi que des métadonnées sur l'emplacement de chaque fichier média. Chaque élément de la liste a un jeton unique attribué. Voici un échantillon de la disposition écrite en notation standard d'objet Javascript :

```json
[ 
  { "requestName": "Silent Night", 
    "listSong":true, 
    "token":"song001", 
    "difficulty":"Moderate", 
    "videoObject": "SilentNight.mp4", 
    "audioObject": "SilentNight.mp3" 
  }, 
  { "requestName": "Mary Had a Little Lamb", 
    "listSong":true, 
    "token":"song002", 
    "difficulty":"Easy", 
    "videoObject": "MaryHadLittleLamb.mp4", 
    "audioObject": "MaryHadLittleLamb.mp3" 
  },
...
]
```

Voici le code qui convertit le tableau en la réponse nécessaire pour Alexa. Inclus est l'intégration du jeton pour chaque élément du tableau.

```js
// ce sont les chansons pour lesquelles des enregistrements ont été faits
var songs = require("data/songs.json");

// créer une liste
const itemImage = null; 
const listItemBuilder = new Alexa.templateBuilders.ListItemBuilder(); 
const listTemplateBuilder = new Alexa.templateBuilders.ListTemplate1Builder();

// construire un tableau de toutes les chansons disponibles 
for (i = 0; i < songs.length; i++ ) { 
  if (songs[i].listSong) { 
    // extraire les attributs du tableau de chansons et les appliquer à la liste
    listItemBuilder.addItem(null, songs[i].token,
      makePlainText(songs[i].requestName),
      makePlainText(songs[i].difficulty)); 
     message = message + songs[i].requestName + " ";
  } 
} 
message = message + "Il suffit de sélectionner sur l'écran une chanson, ou de demander en disant quelque chose comme, Apprends-moi à jouer " + songs[0].requestName + ".";

// maintenant créer l'objet de réponse en utilisant le SDK
const listItems = listItemBuilder.build(); 
const imageLoc = pianoStrings; 
const listTemplate = listTemplateBuilder.setToken('listToken')
  .setTitle('Liste des Chansons Disponibles') .setListItems(listItems)
  .setBackgroundImage(makeImage(imageLoc)) 
  .build(); this.response.speak(message).listen(noSongRepeatMessage).renderTemplate(listTemplate); 
this.emit(':responseReady');
```

La fonction Lambda gère l'événement 'ElementSelected' invoqué par l'Echo Show. L'objet de requête envoyé par l'appareil à la compétence personnalisée contient le jeton utilisé pour traduire ce qui a été sélectionné par l'utilisateur.

```js
// cette fonction est invoquée à partir de l'événement 'ElementSelected'
'ScreenSongSelected': function() { 
  console.log("Element Selected:" + this.event.request.token);
  var videoName = "";
  // faire correspondre le jeton au nom de la chanson et trouver l'objet vidéo à lire 
  for (i = 0; i < songs.length; i++ ) { 
    if (songs[i].token === this.event.request.token) { 
      console.log("Play " + songs[i].requestName);
      videoName = songs[i].videoObject;
    } 
  } 
  const videoClip = videoLoc + videoName;
  this.response.playVideo(videoClip); this.emit(':responseReady'); 
},
```

La fonction Lambda utilise le jeton qu'elle reçoit et trouve le fichier média correspondant à l'identifiant unique. Le contrôle est ensuite transféré à l'appareil avec la vidéo appropriée.

#### 3 — Déléguer le Contrôle au Lecteur Vidéo

Une fois que la vidéo à lire est trouvée, le point de terminaison du média est ajouté à la réponse. Cela nécessite quelques lignes de code dans la fonction Lambda.

Tout d'abord, identifiez un dossier dans le bucket S3 où les fichiers vidéo seront stockés.

```js
// Ce sont les dossiers où se trouvent les fichiers mp4

const videoLoc = 'https://s3.amazonaws.com/.../media/';
```

Ensuite, spécifiez le fichier exact en fonction de ce qui a été identifié par l'utilisateur. Des métadonnées sont ajoutées contenant plus d'informations sur la vidéo.

```js
if (this.event.context.System.device.supportedInterfaces.VideoApp) {
  const videoClip = videoLoc + videoObject; // point de terminaison du fichier
  // ceci sera rendu lorsque l'utilisateur sélectionne les contrôles vidéo
  const metadata = { 
    'title': slots.SongName.value 
  };
  this.response.playVideo(videoClip, metadata);
  this.emit(':responseReady');
} else {
  // gérer l'erreur - et fermer la session
  this.emit(':tell', nonVideoMessage);
}
```

Après l'exécution de ce code, l'appareil Alexa prendra en charge la navigation pour lire la vidéo. L'utilisateur peut utiliser sa voix ou toucher l'écran pour mettre en pause, rembobiner, avancer rapidement, etc. Voici à quoi ressemble l'écran lors de la lecture d'une vidéo, y compris le titre des métadonnées en haut.

![Image](https://cdn-media-1.freecodecamp.org/images/KK4CNJ0uzgbElT7u2Lr-CJ2lWJJLWlrDkLzy)
_Capture d'écran de la Compétence Piano Teacher sur un Alexa Show_

Lorsque la lecture de la vidéo sur l'appareil est terminée, la compétence peut être utilisée à nouveau pour sélectionner plus de contenu.

### Résumé

La construction de la compétence personnalisée peut être réalisée en utilisant l'exemple ci-dessus comme modèle en seulement quelques heures. Le processus de certification Alexa prend seulement un jour ou deux, puis la compétence (et le contenu qu'elle contient) sera disponible pour toute personne disposant d'un Echo Show. En tant que fan de YouTube, j'espère pouvoir l'utiliser bientôt sur mon appareil Alexa, mais il existe également un moyen pour les éditeurs de contenu de le contourner.