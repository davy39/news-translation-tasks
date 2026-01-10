---
title: Comment ajouter des CHAPEAUX DE LEPRECHAUN à votre site web avec la VISION
  PAR ORDINATEUR
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-07T20:56:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-drop-leprechaun-hats-into-your-website-with-computer-vision-b0d115a0f1ad
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kfqTx__agnemI2s0kRd3rw.gif
tags:
- name: Computer Vision
  slug: computer-vision
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment ajouter des CHAPEAUX DE LEPRECHAUN à votre site web avec la VISION
  PAR ORDINATEUR
seo_desc: 'By Shen Huang

  Automatically leprechaun-hat people on your website for St. Patrick’s Day.


  !!! — WARNING — !!!

  Giving a person a green hat can be considered OFFENSIVE to some Chinese people,
  as it has the same meaning as cheating in a relationship. So...'
---

Par Shen Huang

#### Ajoutez automatiquement des chapeaux de leprechaun aux personnes sur votre site web pour la Saint-Patrick.

> **!!! — AVERTISSEMENT — !!!**

> Donner un chapeau vert à une personne peut être considéré comme [**OFFENSANT**](https://mspoweruser.com/microsoft-removes-green-hat-from-vs-2019-installer-after-offending-users-in-china/) pour certains Chinois, car cela a la même signification que de tromper dans une relation. Utilisez donc cela **PRUDEMMENT** lorsque vous servez une base d'utilisateurs chinois.

> **!!! — AVERTISSEMENT — !!!**

Dans ce tutoriel, nous allons voir comment ajouter un chapeau de leprechaun aux images de votre site web qui contiennent des personnes. Le processus sera réalisé à l'aide de certains frameworks de **Vision par Ordinateur**, donc cela représentera la même quantité de travail même si vous avez des millions de portraits à traiter. Une démonstration peut être trouvée [**ici**](https://shenhuang.github.io/demo_projects/tracking.js-master/TEAM%20MEMBERS%20_%20Teamwebsite.html) grâce à la permission de mes coéquipiers.

Ce tutoriel est destiné à un public plus avancé. Je suppose que vous pouvez comprendre beaucoup des fondamentaux par vous-même. J'ai également réalisé quelques tutoriels pour les débutants complets, que j'ai joints à la fin sous forme de liens.

![Image](https://cdn-media-1.freecodecamp.org/images/oKTeBIcRIikaGpEVv0zWVOjoUNVQU43ms4XW)
_Chapeaux de Leprechaun tombant sur les têtes dans les portraits_

### 1. Installation initiale

Avant de commencer ce tutoriel, nous devons d'abord effectuer quelques configurations.

Tout d'abord, nous utilisons **tracking.js** pour nous aider dans ce projet, et donc, nous devons télécharger et extraire les fichiers nécessaires pour **tracking.js** depuis [**ici**](https://github.com/eduardolundgren/tracking.js/archive/master.zip).

Pour ce tutoriel, nous commençons avec un modèle de site web que j'ai pris de notre équipe **WiX**, qui est un **Système de Gestion de Contenu (CMS)** permettant de construire des sites web avec beaucoup moins d'efforts. Le modèle peut être téléchargé depuis [**ici**](https://github.com/shenhuang/shenhuang.github.io/raw/master/tracking.js-master/site_template.zip). Extrayez les fichiers dans le dossier "tracking.js-master" de l'étape précédente.

Pour que tout fonctionne, nous avons également besoin d'un serveur. Nous utiliserons un serveur Python simple pour ce tutoriel. Au cas où vous n'auriez pas Python ou Homebrew (qui aide à installer Python), vous pouvez utiliser les commandes bash suivantes pour les installer.

Installation de Homebrew :

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Installation de Python :

```
brew install python
```

Maintenant que tout est prêt, nous allons exécuter la commande suivante sous notre dossier "tracking.js-master" pour démarrer le serveur Python.

```
python -m SimpleHTTPServer
```

Pour tester, allez à ce [**lien**](http://localhost:8000/examples/face_hello_world.html) de votre hôte local pour voir une page d'exemple. Vous devriez également pouvoir visualiser la page d'exemple extraite depuis [**ici**](http://localhost:8000/TEAM%20MEMBERS%20_%20Teamwebsite.html). Et c'est tout ce que vous avez à faire pour la configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/E3njCktFKMne4zqeC-1t6ljhser9k4Ay8Xhx)
_Configuration d'un serveur Python simple._

### 2. Création du chapeau

Contrairement à mes autres tutoriels, nous allons utiliser une image en ligne pour ce tutoriel plutôt que d'essayer de tout recréer avec **CSS**.

J'ai trouvé un chapeau de leprechaun sur **kisspng** et il peut être trouvé [**ici**](https://github.com/shenhuang/shenhuang.github.io/raw/master/tracking.js-master/leprechaunhat_kisspng.png). Enregistrez l'image dans le dossier racine de notre site web. En ajoutant le code suivant à la fin au-dessus de la balise `</html>`, nous devrions pouvoir visualiser l'image dans notre site web d'exemple après avoir enregistré et rechargé.

```
<body>
  <img id = "hat" class = "leprechaunhat" src = "./leprechaunhat_kisspng.png" >
</body>
```

![Image](https://cdn-media-1.freecodecamp.org/images/FDncTXccdZYyRY8TG3fF1jaCjtMHsI9WyQEa)
_Image du chapeau ajoutée en bas du site web_

Maintenant, nous devons concevoir une animation de chute avec CSS, et placer le code au-dessus de la déclaration du chapeau. Le code permet essentiellement au chapeau de tomber puis de trembler un peu.

```html
<style>
 @keyframes shake {
  0% {
   transform : translateY(-30px);
  }
  40% {
   transform : rotate(10deg);
  }
  60% {
   transform : rotate(-10deg);
  }
  80% {
   transform : rotate(10deg);
  }
  100% {
   transform : rotate(0deg);
  }
 }
 .leprechaunhat {
  animation : shake 1s ease-in;
 }
</style>
```

![Image](https://cdn-media-1.freecodecamp.org/images/niLdZDtnM566OnXKvebFQ-kC96UrllOgVuQv)
_Animation de chute du chapeau._

### 3. Déposer des chapeaux sur les portraits

Maintenant, nous allons voir comment déposer des chapeaux précisément sur les portraits. Tout d'abord, nous devons référencer les fichiers JavaScript de "tracking.js" avec le code suivant.

```html
<script src = "build/tracking-min.js" type = "text/javascript" ></script>
<script src = "build/data/face-min.js" type = "text/javascript" ></script>
```

Le code nous fournit une classe `Tracker` dans laquelle nous pouvons alimenter des images. Ensuite, nous pouvons écouter une réponse indiquant un rectangle délimitant les visages à l'intérieur de l'image.

![Image](https://cdn-media-1.freecodecamp.org/images/19eUYAEHlwvb6ycxU58Xv1ZnIWQoV--GvHDZ)
_Tracker Expliqué_

Nous commençons par définir une fonction qui s'exécute lorsque la page est chargée. Cette fonction peut être attachée ailleurs si nécessaire. La `yOffsetValue` est un décalage alignant le chapeau dans une position plus appropriée.

```js
const yOffsetValue = 10;
window.onload = function() {
};
```

À l'intérieur, nous définissons notre fonction de création de chapeau, lui permettant de créer des chapeaux avec des tailles et des positions arbitraires.

```js
function placeHat(x, y, w, h, image, count) {
 hats[count] = hat.cloneNode(true);
 hats[count].style.display = "inline";
 hats[count].style.position = "absolute";
 hats[count].style.left = x + "px";
 hats[count].style.top = y + "px";
 hats[count].style.width = w + "px";
 hats[count].style.height = h + "px";
 image.parentNode.parentNode.appendChild(hats[count]);
}
```

Nous devons également modifier légèrement notre script de déclaration d'image pour le cacher, car nous l'affichons maintenant avec JavaScript.

```html
<img id = "hat" class = "leprechaunhat" src = "./leprechaunhat_kisspng.png" style = "display : none" >
```

Ensuite, nous ajoutons le code suivant pour créer les chapeaux au-dessus des visages, avec la taille correspondant au visage.

```js
var hat = document.getElementById("hat");
var images = document.getElementsByTagName('img');
var trackers = [];
var hats = [];
for(i = 0; i < images.length; i++)
{
 (function(img)
 {
  trackers[i] = new tracking.ObjectTracker('face');
  tracking.track(img, trackers[i]);
  trackers[i].on('track', function(event) {
   event.data.forEach(function(rect) {
    var bcr = img.getBoundingClientRect();
    placeHat(rect.x, rect.y + yOffsetValue - rect.height, rect.width, rect.height, img, i);
   });
  });
 })(images[i]);
}
```

Maintenant, tandis que notre serveur Python est toujours en cours d'exécution, l'appel de l'adresse suivante devrait nous montrer des chapeaux de leprechaun tombant sur les portraits.

```
http://localhost:8000/TEAM%20MEMBERS%20_%20Teamwebsite.html
```

![Image](https://cdn-media-1.freecodecamp.org/images/3lHrFCf6hT-qFaANYfSA7kyK9KzSS9BYG-N8)
_Démonstration de la chute des chapeaux de leprechaun_

Félicitations ! Vous venez d'apprendre comment déposer des chapeaux de leprechaun sur tous les portraits d'un site web avec la vision par ordinateur. Je vous souhaite, à vous, vos amis et votre audience une excellente Saint-Patrick !!!

### En conclusion

J'ai lié quelques-uns de mes guides précédents ci-dessous sur des projets similaires. Je crois qu'il existe certaines tendances dans la conception front-end. Malgré l'émergence de nouveaux frameworks .js et les mises à jour d'ES, les animations par ordinateur et l'intelligence artificielle peuvent faire des merveilles à l'avenir pour le front-end, améliorant l'expérience utilisateur avec élégance et efficacité.

**Débutant :**

* [Comment remplir votre site web avec de jolis COEURS DE LA SAINT-VALENTIN](https://medium.com/front-end-weekly/how-to-fill-your-website-with-lovely-valentines-hearts-d30fe66d58eb)
* [Comment ajouter des FEUX D'ARTIFICE à votre site web](https://medium.com/front-end-weekly/how-to-add-some-fireworks-to-your-website-18b594b06cca)
* [Comment ajouter des BULLES à votre site web](https://medium.com/front-end-weekly/how-to-add-some-bubbles-to-your-website-8c51b8b72944)

**Avancé :**

* [Comment créer de belles LANTERNES qui S'ORGANISENT en mots](https://medium.freecodecamp.org/how-to-create-beautiful-lanterns-that-arrange-themselves-into-words-da01ae98238)

Je suis passionné par la programmation et j'adorerais apprendre de nouvelles choses. Je crois que le savoir peut rendre le monde meilleur et je suis donc motivé à partager. Faites-moi savoir si vous êtes intéressé par la lecture de quelque chose en particulier.

Si vous cherchez le code source de ce projet, il peut être trouvé [**ici**](https://github.com/shenhuang/shenhuang.github.io/tree/master/tracking.js-master). Merci encore à mes coéquipiers qui m'ont permis d'utiliser leurs portraits pour ce projet et **soyez prudent avant d'utiliser cela sur un site web avec une base d'utilisateurs chinois**.