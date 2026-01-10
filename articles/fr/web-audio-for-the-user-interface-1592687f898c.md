---
title: Améliorez votre interface utilisateur avec l'audio web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-14T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/web-audio-for-the-user-interface-1592687f898c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gP_PX-doi7ZB6_UDKkNwtg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: UI
  slug: ui
- name: UX
  slug: ux
- name: Web Audio API
  slug: web-audio-api
- name: Web Development
  slug: web-development
seo_title: Améliorez votre interface utilisateur avec l'audio web
seo_desc: 'By Nick Frazier

  When people my age hear the phrase “web audio”, they probably think of Geocities
  sites of the 90’s with irritating sound loops playing in the background.

  The possibilities then were limited, and sound was quickly abandoned as a compon...'
---

Par Nick Frazier

Lorsque les gens de mon âge entendent l'expression « audio web », ils pensent probablement aux sites Geocities des années 90 avec des boucles sonores irritantes jouant en arrière-plan.

Les possibilités étaient alors limitées, et le son a rapidement été abandonné en tant que composant de la plupart des expériences web. À part le site « expérimental » occasionnel ou la page d'un groupe, le son sur le web depuis lors a été l'exception plutôt que la règle.

L'audio web a parcouru un long chemin depuis. Avec ces avancées, nous avons maintenant l'opportunité de commencer à considérer le son comme une réelle possibilité pour le web.

Et pas seulement pour les sites riches en médias. Les concepteurs de jeux vidéo comprennent depuis des années la valeur de la conception sonore, même dans les menus les plus banals et les interactions de l'interface utilisateur. Voir par exemple la riche conception sonore des [menus des personnages de Destiny](https://www.youtube.com/watch?v=W17KKFf9GRE).

Bien que les interactions web ne soient pas tout à fait les mêmes, avec l'accent continu sur l'expérience utilisateur, il y a toutes les raisons de considérer l'engagement du sens auditif comme faisant partie du package.

Cela ne signifie pas que nous devrions commencer à ajouter des explosions de feux d'artifice et des trompettes retentissantes à notre page d'accueil simplement parce que nous le pouvons. [Le son inattendu et indésirable est un facteur rédhibitoire](http://webpropelled.com/2012/5-reasons-your-website-should-never-autoplay-sound/).

La première question à poser pourrait donc bien être : « Mes utilisateurs s'attendent-ils à du son ? » Dans le cas d'un jeu, de la musique ou d'un site similaire, ils s'y attendent probablement. Si c'est le cas, l'ajout de son à votre interface utilisateur pourrait être un domaine de développement bienvenu. (Vous voulez probablement toujours ajouter un bouton de désactivation générale du son, cependant.)

C'est avec cet état d'esprit que j'ai commencé à explorer l'ajout d'une conception sonore subtile dans certaines de mes interfaces utilisateur web. J'avais quelques objectifs :

* La capacité de jouer un son sur un événement (par exemple, survol, clic)
* Bonne performance, faible latence
* Bonne couverture des navigateurs
* Peu ou pas d'effets secondaires distractifs ou d'ennuis (pour éviter le syndrome Geocities)

Ce qui suit est un aperçu des meilleures pratiques que j'ai rencontrées lors de mes expérimentations, basées sur l'état actuel du web.

Gardez à l'esprit que l'audio sur le web est encore un territoire relativement inexploré, il y a donc encore beaucoup à créer et à découvrir dans ce domaine.

#### L'élément audio HTML

Jusqu'à l'avènement de HTML5, l'audio sur le web était mieux décrit comme « primitif ». La seule façon d'incorporer du son dans un site était avec un plug-in comme Flash.

HTML5 a apporté avec lui la balise _<audio>_ — une étape modeste mais importante. Cette balise a été conçue pour permettre aux développeurs de diffuser facilement des sons et de la musique directement depuis la page avec une seule ligne de code. Des contrôles simples pouvaient être intégrés en ajoutant un seul attribut :

```
<audio id="snare" src="snare-2.mp3" controls></audio>
```

Le résultat :

En soi, l'utilité de cette balise est limitée. Mais HTML5 a également introduit une API JavaScript, [HTMLAudioElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement), qui offre la possibilité de jouer des sons de manière programmatique.

L'ajout de sons aux événements en utilisant cette interface ressemble à ceci :

```
function playSound () {   document.getElementById("snare").play(); }
```

Cela vous permet de déclencher un son en utilisant JavaScript.

Voici un exemple de cela en utilisation :

Essayez de cliquer deux fois, cependant, et vous allez immédiatement rencontrer l'un des principaux inconvénients de l'audio HTML.

Avec l'audio HTML, jouer un son plus d'une fois est délicat. Si vous utilisez uniquement la fonction _play()_ et une seule source, le navigateur attendra jusqu'à ce qu'il ait fini de jouer le son avant de vous permettre de déclencher un autre son. En fait, même avec plusieurs sources, l'audio HTML a une capacité limitée à jouer plusieurs sons en même temps.

Un truc que j'ai trouvé pour permettre un déclenchement plus rapide (en utilisant une seule source) est d'arrêter toujours le son avant de le jouer. Notez que l'API n'inclut pas de fonction « stop », mais recharger le fichier fait l'affaire :

```
function playSound () {   document.getElementById("snare").load();  document.getElementById("snare").play();}
```

Maintenant, nous devrions pouvoir frapper ces caisses claires en rafale comme le prochain 9th Wonder :

Choisir le meilleur format audio pour une utilisation web était autrefois une tâche délicate. La compatibilité multi-navigateurs des formats était très variable. Vous deviez généralement avoir plusieurs versions des mêmes fichiers, avec différentes extensions, prêtes à être utilisées pour faire face à n'importe quel navigateur que votre site pourrait rencontrer.

Maintenant, c'est plus simple : utilisez des MP3.

![Image](https://cdn-media-1.freecodecamp.org/images/0*WdCSk691xrcoiVab.jpg)
_Couverture actuelle des navigateurs pour le format mp3, de [caniuse.com](http://caniuse.com/#feat=mp3" rel="noopener" target="_blank" title=")_

À l'exception d'Internet Explorer 8 (qui est presque mort) et d'Opera Mini (qui ne supporte pas l'audio de toute façon), les fichiers MP3 devraient fonctionner presque partout.

Ils sont également compacts. Si vous n'avez que des fichiers wav ou un autre format, utilisez un utilitaire de conversion (j'utilise [MH Audio Converter](http://www.mediahuman.com/audio-converter/)) et standardisez tout en mp3.

#### Web Audio API : Un Bond de Géant

L'audio HTML offre une solution passable pour le son. En particulier, j'ai trouvé que son utilisation via une bibliothèque JavaScript appelée [Buzz](http://buzz.jaysalvat.com/) en faisait une option flexible et simple.

Mais il y a encore de nombreux inconvénients :

* Jouer plusieurs sons en succession rapide est une expérience médiocre
* La capacité à manipuler le son est limitée
* Synchroniser les sons est un casse-tête

Voici l'[API Web Audio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API). Web Audio est le véritable successeur de l'Audio HTML, et résout certains des problèmes de ce dernier tout en ajoutant une grande quantité de flexibilité.

Avec Web Audio, les développeurs disposent désormais d'un ensemble robuste d'outils pour créer des moteurs sonores au niveau des jeux de plateforme et des synthétiseurs logiciels professionnels.

En utilisant Web Audio au lieu de l'Audio HTML, nous pouvons créer un son de clic de bouton qui se superpose plutôt que de se couper, comme le démontre cette visualisation :

Il y a quelques pièges, cependant, dont l'un que j'ai rencontré immédiatement : Web Audio est compliqué. Si vous ouvrez l'un des nombreux excellents tutoriels sur l'API en ligne (je recommande le livre de Boris Smus [Web Audio API](http://chimera.labs.oreilly.com/books/1234000001552), dont le texte entier est disponible gratuitement sur le site O'Reilly), la première chose que vous remarquerez est que le simple fait de jouer un seul son peut nécessiter une vingtaine de lignes de code.

La solution que j'ai trouvée à cela est [SoundJS](http://www.createjs.com/soundjs). SoundJS, faisant partie de la suite d'outils CreateJS, est une puissante bibliothèque sonore avec une courbe d'apprentissage douce. Une partie de sa puissance réside dans l'abstraction de nombreux détails des API audio de bas niveau, de sorte que le même code peut être exécuté sur HTML Audio, Web Audio, ou même Flash audio, selon ce que le navigateur de l'utilisateur supporte.

Mais j'ai trouvé que là où il excelle vraiment, c'est dans sa gestion de Web Audio. Maintenant, au lieu d'écrire une page de code pour jouer un son, vous pouvez écrire ceci :

```
function loadSound () {   createjs.Sound.registerSound("snare-2.mp3", soundID); } 
```

```
function playSound () {   createjs.Sound.play(soundID); }
```

Essayez-le et écoutez la différence (et l'amélioration sonore) :

L'autre piège majeur est que la norme Web Audio est encore en évolution — c'est actuellement un projet de travail, et il n'y a pas de support dans Internet Explorer.

![Image](https://cdn-media-1.freecodecamp.org/images/0*X_2zqf2P5wZ1Rp-w.jpg)
_Couverture actuelle des navigateurs pour l'API Web Audio, de [caniuse.com](http://caniuse.com/#feat=audio-api" rel="noopener" target="_blank" title=")_

À un niveau plus fin, il y a actuellement quelques limitations supplémentaires à l'audio en général, notamment sur les appareils mobiles :

* Avec les appareils iOS, le son est initialement verrouillé et ne se jouera pas tant qu'un événement initié par l'utilisateur ne se produira pas. Cela est apparemment une mesure pour réduire la bande passante.
* Avec les appareils Android, il n'y a pas de contrôle sur le volume audio, et vous ne pouvez jouer l'audio que dans le cadre d'un événement initié par l'utilisateur.

Ces limitations peuvent ne pas avoir autant d'importance avec les événements de clic, comme je l'ai démontré jusqu'à présent, mais elles peuvent entrer en jeu une fois qu'une conception sonore d'UI plus sophistiquée est employée. Ce qui nous amène à notre dernière étape.

#### Aller plus loin avec Web Audio

Lorsque j'ai commencé à réfléchir à la « Conception Sonore d'UI », ma première pensée a été les événements de clic. Mais une fois cela résolu, je me suis demandé à propos d'autres possibilités. Qu'en est-il des événements de survol ? Ou des événements de défilement ? Ou quelque chose de complètement différent ? Avec Web Audio, j'ai trouvé qu'il y a un monde de possibilités.

Web Audio vous permet d'ajouter plusieurs types différents d'effets de niveau professionnel à votre chaîne audio. Par exemple :

* Les [BiquadFilterNodes](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode) peuvent être utilisés comme filtres passe-haut/passe-bas/coupe-bande
* Les [ConvolverNodes](https://developer.mozilla.org/en-US/docs/Web/API/ConvolverNode) peuvent être utilisés pour la réverbération
* Les [DelayNodes](https://developer.mozilla.org/en-US/docs/Web/API/DelayNode) peuvent être utilisés pour les effets de retard
* Les [StereoPannerNodes](https://developer.mozilla.org/en-US/docs/Web/API/StereoPannerNode) permettent de panoramiquer à gauche et à droite
* Les [AnalyserNodes](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode) permettent l'analyse des données et la visualisation

Et si, ai-je pensé, vous utilisiez un BiquadFilterNode en conjonction avec un gestionnaire d'événements qui suit la proximité de la souris avec un bouton ? Vous pourriez changer un son en fonction de la proximité de votre pointeur de souris avec le bouton. Des [balayages de filtre style Moog](https://www.youtube.com/watch?v=HieClHTxid0) dans votre UI — à quel point ce serait cool ?

Il s'avère que SoundJS rend cela, aussi, relativement facile (bien que le réglage du contexte Web Audio de la bibliothèque ne soit pas aussi bien documenté que le reste de l'API). En utilisant certaines des parties plus [avancées](http://createjs.com/docs/soundjs/classes/WebAudioPlugin.html) de l'API, j'ai trouvé que vous pouvez « insérer » un filtre dans la configuration Web Audio de SoundJS, et ajuster à votre guise. Ajustez le filtre en fonction des mouvements de la souris, et voilà, un filtre de proximité :

Si vous voulez expérimenter vous-même, consultez le code SoundJS dans le [stylo ci-dessus](http://codepen.io/fraziern/pen/oLVvdg). L'algorithme de proximité est basé sur [ce](https://css-tricks.com/snippets/jquery/calculate-distance-between-mouse-and-element/) extrait de CSS-Tricks de Chris Coyier.

#### Le Ciel est la Limite

Avec Web Audio, les développeurs web semblent enfin avoir une boîte à outils profonde et puissante pour concevoir et manipuler l'audio. C'est également propice au développement de nouvelles idées et techniques, car il commence vraiment à être intégré dans les expériences utilisateur web modernes.

Mes propres explorations effleurent la surface. Je continue à chercher de nouvelles façons d'engager les autres avec le son, et j'ai hâte de voir où les choses iront ensuite.

#### Ressources supplémentaires

[Démonstration du Visualiseur SoundJS](http://createjs.com/demos/soundjs/webaudionodeinsertion) : Le code source de cette démonstration est la meilleure ressource si vous voulez commencer à décomposer le graphe Web Audio de SoundJS

[Designing Sound](http://designingsound.org/) : Inspiration pour la conception sonore des maîtres.

[Chrome Experiments](https://www.chromeexperiments.com/) : Une autre collection incroyable d'inspiration de design (visuel et auditif).

_Une version de cette histoire a été publiée à l'origine sur [fraziern.github.io](https://fraziern.github.io/javascript/audio/ui/2016/08/14/js-sound-libraries.html) le 14 août 2016._