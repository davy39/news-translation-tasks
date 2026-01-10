---
title: Bibliothèques et API JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-07T14:27:39.000Z'
originalURL: https://freecodecamp.org/news/javascript-libraries-and-apis-e9d674dc5690
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Co2qNTU1Es6kAf3b9MSOqw.jpeg
tags:
- name: api
  slug: api
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: technology
  slug: technology
seo_title: Bibliothèques et API JavaScript
seo_desc: 'By Adam Recvlohe

  If you have written JavaScript for the DOM before, then you probably know how unwieldy
  it can get. I mean getElementById is seven syllables and 14 characters long for
  goodness sake. Isn’t there an easier way?

  Enter jQuery goodness. j...'
---

Par Adam Recvlohe

Si vous avez déjà écrit du JavaScript pour le DOM, alors vous savez probablement à quel point cela peut devenir encombrant. Je veux dire, _getElementById_ fait sept syllabes et 14 caractères de long, pour l'amour du ciel. N'y a-t-il pas une manière plus simple ?

Entrez dans la magie de jQuery. jQuery est une bibliothèque JavaScript.

Bibliothèque ? Comme celles où je peux emprunter des livres et louer des films des années 90 gratuitement ? Non. Une bibliothèque dans le sens de la programmation est une base de code qui simplifie la logique de programmation et est librement disponible pour que chacun puisse l'utiliser. Pas de frais de retard !

Cela n'a peut-être pas eu de sens pour vous, mais j'ai des exemples.

Hypothétiquement parlant, supposons que je veux changer l'arrière-plan d'un _div_ en rouge. J'ai donné à ce _div_ un _id_ de 'red' pour simplifier. En JavaScript, j'écrirais quelque chose comme ceci :

```
document.body.getElementById('red').style.backgroundColor = 'red';
```

Cela fonctionne et fait le travail, ce qui est tout ce dont nous avons vraiment besoin. Mais maintenant, regardons cette même fonctionnalité en jQuery.

```
$('#red').css('background-color', 'red');
```

Wow, c'est joli ! C'est tout ce que les programmeurs recherchent : une solution concise et succincte.

Maintenant, vous voyez clairement les avantages de jQuery. Il est conçu pour faciliter la programmation en JavaScript.

Mais il y a quelques inconvénients. Vous pourriez penser que jQuery peut tout faire, et que programmer en jQuery est la même chose qu'en JavaScript. **Ces deux notions sont fausses.**

De mon point de vue, travailler avec jQuery est comme utiliser Rails, le framework de développement web de Ruby on Rails. Vous pouvez aller assez loin avec Rails sans avoir à plonger profondément dans l'apprentissage de Ruby.

Cependant, mon argument est que vous ne pouvez pas vraiment comprendre ou apprécier JavaScript à moins de l'utiliser principalement pour exécuter vos programmes. Cela dit, il y a de grands avantages à utiliser jQuery que vous pouvez explorer. L'avantage dont nous allons discuter aujourd'hui est l'utilisation de jQuery pour faire des appels d'API.

API, hein ? API signifie Application Programming Interface. C'est un grand acronyme fantaisiste pour 'règles d'engagement'.

De nombreuses applications logicielles ont un ensemble de règles qui régissent la manière dont elles interagissent avec d'autres programmes. Je suis sûr que cela a du sens pour vous, mais je vais vous donner quelques exemples pour bonne mesure.

Par exemple, si vous voulez ajouter un paragraphe au corps d'une page HTML, vous pourriez écrire quelque chose comme ceci :

```
var paragraph = document.body.createElement('P');paragraph.textContent = 'J\'utilise une API, hourra !';document.body.appendChild(paragraph);
```

Dans l'exemple ci-dessus, j'ai utilisé les règles suivantes :

```
1. document.body pour accéder à l'objet body 2. méthode createElement pour créer un élément3. méthode textContent pour insérer du texte dans cet élément4. méthode appendChild pour ajouter ce paragraphe au body
```

Ici, nous utiliserions l'API DOM. DOM signifie Document Object Model, et c'est l'organisation des éléments HTML sur une page.

En termes profanes, l'API DOM 'fournit une représentation structurée' d'un site web. Cela devient le point d'entrée qui permet aux langages de programmation d'_interagir_ avec le HTML d'une page.

L'API DOM est ce qui fournit les méthodes telles que _createElement_ et _textContent_ afin que vous puissiez utiliser votre JavaScript sophistiqué pour manipuler le DOM.

Avez-vous remarqué que j'ai dit **langages de programmation** ? Vous pouvez en fait interagir en utilisant n'importe quel langage, mais vous voulez probablement utiliser le langage de facto du web — JavaScript. Je dis juste.

Maintenant que vous avez un peu de contexte, plongeons dans la création d'une application de recherche Giphy.

Ce sera amusant ! Et je le pense vraiment cette fois.

Nous commencerons par examiner un objet _response_. Un objet _response_ est les données retournées après qu'une requête a été faite à une API.

D'accord, laissez-moi décomposer cela. Lorsque vous tapez une URL dans votre barre de recherche — comme eyeluvkats.com — et que vous appuyez sur Entrée, une requête est envoyée à travers Internet à un serveur qui héberge le domaine eyeluvkats.com.

Ensuite, une réponse est envoyée à l'utilisateur avec le contenu du site web : HTML, CSS, JavaScript, images, vidéos, etc.

Maintenant, au lieu de demander eyeluvkats.com, nous allons faire une requête à l'API Giphy qui retournera un objet de données. Cette requête sera :

[http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=cat](http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=cat)

Votre premier appel d'API ! Hourra !

L'appel ici a été fait à l'API Giphy et dans les paramètres de l'URL, nous avons demandé un type particulier de gif :

gifs/**random**?api_key=dc6zaTOxFJmzC&**tag=cat**.

Nous avons demandé un gif de chat aléatoire en utilisant le paramètre random, et le paramètre de tag de chat. Je suis un tel millénial, désolé ! Ce que vous devriez maintenant voir dans votre navigateur est un objet JSON avec des données liées à un gif de chat aléatoire.

JSON signifie JavaScript Object Notation. C'est la manière dont JavaScript envoie des données à travers le web et est couramment utilisé comme l'objet de réponse par défaut pour de grands ensembles de données d'API. Avez-vous déjà créé un objet JSON auparavant ? Non ? Faisons cela maintenant pour que vous sachiez comment les objets fonctionnent en JavaScript.

Pour créer un objet JavaScript, également connu sous le nom de littéral d'objet, vous pouvez déclarer une variable égale à une paire d'accolades. Par exemple :

```
var object = {};
```

Ces objets sont généralement utilisés pour stocker des données, alors ajoutons votre bio. Les données dans les objets sont stockées sous forme de paires clé/valeur, c'est-à-dire _firstName: 'Adam'_, séparées par des virgules.

Passez en revue maintenant et ajoutez vos autres détails comme votre date de naissance, votre numéro de sécurité sociale et votre numéro de carte de crédit. Lorsque vous avez terminé, envoyez cet objet à adam@youjustgotscammed.com.

Pour moi, mes informations ressembleraient à ceci :

```
var me = {    firstName: 'Adam',    middleName: 'Elliott',    lastName: 'Recvlohe',    favoriteFood: 'Chipotle',    favoriteDrink: 'Kombucha: Gingerade',    race: 'Human',    favoriteVideo: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}
```

C'est bien et bon, mais comment accédons-nous à ces informations ? Eh bien, il y a quelques façons de le faire. Une façon est avec la notation par points et l'autre est en utilisant la notation par crochets.

```
var me = {    firstName: 'Adam',    middleName: 'Elliott',    lastName: 'Recvlohe',    favoriteFood: 'Mexican',    favoriteDrink: 'Kombucha',    race: 'Human'}// Notation par pointsvar myFirstName = me.firstName;// Notation par crochetsvar myLastName = me['lastName'];
```

Souvenez-vous, plus l'objet devient imbriqué, plus vous aurez besoin de points ou de crochets.

```
var data = {    address: {        city: 'Tampa',        state: 'Florida'    }}var myCity = data.address.cityvar myState = data['address']['state'];
```

_Note de bas de page : La norme JSON exige que les propriétés et les valeurs des objets soient entre guillemets doubles. Je vous ai montré les littéraux d'objets JavaScript car la manière dont vous accédez aux données de chacun est la même, la syntaxe de JSON étant seulement légèrement différente._

Maintenant que nous avons cela de côté, nous pouvons commencer à manipuler les données dans l'objet JSON, que nous avons obtenu en appelant l'API Giphy. L'objet est assez grand, mais tout ce que je veux vraiment, c'est l'URL du gif de chat aléatoire. Comment pourrais-je assigner cette URL à une variable ? Puisque vous êtes toujours ici, je vais vous montrer comment je le ferais :

```
var gifURL = object.data.url;
```

Cela ne fait rien pour le moment, mais ce que je voulais vous montrer en premier, c'est comment nous manipulerions les données pour les manipuler plus tard.

Nous avons maintenant les bases de la manipulation d'un objet de réponse. Passons aux vraies choses de la création d'une fonction pour appeler ces données pour nous, puis manipuler ces données à l'écran.

Jusqu'à présent, nous n'avons pas vraiment eu besoin de CodePen, mais nous en avons besoin maintenant. Si vous voulez continuer à suivre, je suggère d'ouvrir un compte [codepen.io](http://codepen.io) et de créer un nouveau pen.

Avec votre pen ouvert, nous devons faire quelques choses d'abord pour préparer le terrain. Nous devons ajouter la bibliothèque jQuery à notre pen. Dans l'onglet JavaScript, à gauche de **JavaScript**, vous devriez voir une icône d'engrenage. C'est le bouton des paramètres. Cliquez là et ce qui devrait s'ouvrir ensuite sont vos paramètres JavaScript. Sous **Add External JavaScript**, il y a une barre déroulante appelée **Quick-add**. Sélectionnez jQuery. D'accord, maintenant nous sommes prêts à partir.

Quand voulons-nous exécuter cet appel à l'API Giphy ? Eh bien, par convention, cela se fait généralement lorsque le document est prêt. Vous n'auriez probablement jamais deviné que nous allons utiliser la méthode _ready_ dans jQuery. Cela ressemble un peu à ceci :

```
$(document).ready(function() {})
```

En JavaScript, il y a quelques étapes différentes en ce qui concerne le chargement du contenu. Il y a _interactive_, _complete_, et quelques autres. Tout cela dit que lorsque le DOM est prêt, cette fonction sera exécutée.

Essayez-le ! Rafraîchissez le navigateur avec quelque chose d'unique, dans la fonction de rappel _ready_ comme console.log('Bonjour, le Monde !').

```
$(document).ready(function() {    console.log('Bonjour, le Monde !');})
```

Si vous regardez dans votre console, vous devriez voir imprimé _Bonjour, le Monde !_.

_En bas de votre fenêtre CodePen, vous devriez voir le mot **console.** Cliquez sur ce bouton et vous devriez voir la console s'ouvrir._

jQuery vient avec beaucoup d'autres fonctions pratiques. La suivante dont nous aurons besoin est la méthode _getJSON_. Ce que cela va faire, c'est retourner une réponse en JSON et nous donner une fonction de rappel pour faire quelque chose avec ces données. Cela sonne probablement un peu arbitraire. Laissez-moi vous donner un exemple concret.

```
$(document).ready(function() {  var url = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=cat';      $.getJSON(url, function(object) {    console.log(object);  });});
```

Je parie que vous ne pouvez pas deviner ce que cela fait ? D'accord, vous m'avez prouvé que j'avais tort. Bien sûr, vous savez que la méthode _getJSON_ envoie une requête à _url_ et retourne des données qui sont ensuite enregistrées dans la console. Vous êtes un malin, vous !

C'est bien et tout, mais nous pouvons faire mieux. Nous pouvons prendre cet objet et utiliser la propriété _url_ pour placer un gif dans le DOM. Esprit...Soufflé...Boom !

Nous allons continuer à utiliser jQuery et créer une image dynamiquement. Pour créer une image en jQuery, nous pouvons passer la balise image sous forme de chaîne avec toutes les informations nécessaires comme ceci :

```
var imageSource = object.data.image_original_url;var image = $('<img src=' + imageSource + ' />');
```

Maintenant, tout ce que nous avons à faire est d'ajouter cela au corps du DOM et nous sommes bons. Houston, tous les systèmes sont prêts !

```
$(document).ready(function() {  var url = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=cat';      $.getJSON(url, function(object) {    var imageSource = object.data.image_original_url;    var image = $('<img src=' + imageSource + ' />');    image.appendTo($('body'));  });});
```

Le voici sur codepen :

> Ma maman disait toujours : « La vie était comme une application Giphy. On ne sait jamais ce que l'on va obtenir. » — JS Gump

Maintenant, chaque fois que vous rafraîchissez la page, vous devriez obtenir un nouveau gif de chat. Je vous en prie !

Nous pouvons ajouter un peu plus de fonctionnalités à cela. Au lieu d'obtenir seulement un chat aléatoire à chaque fois, nous pouvons plutôt rechercher les gifs que nous voulons et en afficher certains sur la page. Cela semble beaucoup plus cool.

Avant de pouvoir faire cela, nous aurons besoin d'un champ de saisie. Le champ de saisie prendra votre terme de recherche et l'ajoutera en tant que paramètre à la requête envoyée à l'API Giphy. Dans votre HTML, ajoutez un champ de saisie.

```
<input type='text' />
```

Jusqu'à présent, nous avons fait des appels à l'API 'random'. Cette fois, nous voulons rechercher. Je me demande quelle est cette API ? Oh, je vois, elle s'appelle 'search'. Sur la page d'accueil de Giphy, nous avons un bel exemple d'URL :

[http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC](http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC)

C'est une quantité de données qui vaut bien une litière ! Par défaut, Giphy retournera 25 résultats. Comme vous pouvez le voir dans l'URL, la manière dont ces éléments sont recherchés utilise le paramètre _q_, qui dans ce cas est égal à _funny+cats_. Si nous voulons rechercher un autre ensemble de termes, alors tout ce que nous aurions à faire est de capturer la saisie de l'utilisateur et, lorsqu'il appuie sur Entrée, une nouvelle requête est envoyée à l'API. Faisons cela maintenant.

Pour capturer la saisie de l'utilisateur, nous devons utiliser la méthode _val_ de jQuery sur la saisie.

```
$(document).ready(function() {   var value = $('input').val();});
```

Mais comment obtenons-nous réellement cette valeur ? Nous devons ajouter un écouteur d'événement afin que lorsque l'utilisateur appuie sur Entrée, nous puissions capturer cette valeur et l'envoyer à la méthode _getJSON_. Dans jQuery, les écouteurs d'événement sont également plus courts. Nous écouterons l'événement _keypress_ mais seulement pour la touche Entrée, qui est désignée par 13. Souvenez-vous que les écouteurs d'événement fournissent une fonction de rappel qui passe l'événement du DOM. Il y a cependant un petit problème. La valeur que nous obtenons en retour sera une chaîne, ce qui signifie qu'elle n'aura pas l'opérateur '+' entre chaque mot. Comme jQuery est écrit en JavaScript, cela nous permet d'utiliser des méthodes JavaScript vanilla dans notre script. J'utiliserai la méthode _replace_ pour remplacer les espaces par l'opérateur '+'.

```
$(document).ready(function() {  $('input').keypress(function(event) {    if(event.which == 13) {      var value = $('input').val();      value = value.trim().replace(/\s+/g, '+');      console.log(value);      event.preventDefault();    }         }); });
```

La méthode _replace_, intégrée à JavaScript, prend deux paramètres : une expression régulière et ce que vous voulez remplacer par une correspondance. Dans mon expression régulière, j'utilise un caractère spécial, _\s_. Cela représente un espace blanc. J'ai ajouté un opérateur '+' à la fin pour signifier que je veux capturer n'importe quel nombre d'espaces blancs dans une chaîne, _\s+_. Mon raisonnement est qu'un utilisateur peut mettre plus d'un espace entre les mots et je veux corriger cette erreur si elle se produit.

C'est une solution très primitive mais pour nos besoins, cela fonctionne. Si vous regardez dans votre console, vous devriez voir votre texte de chaîne combiné avec des opérateurs '+'. Bien, nous avons compris cela. Maintenant, nous pouvons composer une URL de l'API de recherche et la valeur que nous recherchons.

```
$(document).ready(function() {  $('input').keypress(function(event) {    if(event.which == 13) {      var value = $('input').val();      value = value.trim().replace(/\s+/g, '+');      var url = 'http://api.giphy.com/v1/gifs/search?api_key=dc6zaTOxFJmzC&q=' + value;      console.log(url);      event.preventDefault();    }         }); });
```

Dans votre console, vous devriez voir la nouvelle URL que nous envoyons à l'API Giphy. Ensuite, nous pouvons réellement envoyer notre appel en utilisant _getJSON_.

```
$(document).ready(function() {  $('input').keypress(function(event) {    if(event.which == 13) {      var value = $('input').val();      value = value.trim().replace(/\s+/g, '+');      var url = 'http://api.giphy.com/v1/gifs/search?api_key=dc6zaTOxFJmzC&q=' + value;      $.getJSON(url, function(object) {        console.log(object);      });    event.preventDefault();    }         }); });
```

_L'objet de réponse JSON sera assez grand et vous ne pourrez pas le voir en utilisant la console CodePen. Au lieu de cela, en haut à droite où il est écrit **Change View**, cliquez et faites défiler vers le bas jusqu'à **Debug Mode**. Une nouvelle fenêtre s'ouvrira. Faites un clic droit sur la nouvelle fenêtre et faites défiler vers le bas jusqu'à **Inspect**. Un panneau sur la droite ou en bas de l'écran devrait s'afficher. Maintenant, cliquez sur l'onglet qui dit **console**. Si vous rafraîchissez le navigateur, mettez quelques mots dans le champ de saisie et cliquez sur Entrée, vous devriez voir l'objet de réponse s'afficher dans le journal._

Maintenant, si vous tapez quelques mots dans la saisie, vous devriez obtenir un objet de la taille d'une boule de poils avec un tableau de 25 objets. D'accord, nous avons nos données, mais elles ne s'affichent toujours pas à l'écran. Ce que nous devons faire, c'est itérer sur le tableau, obtenir chaque URL d'image, puis créer une balise _img_ pour chacune d'elles et ajouter chacune au DOM. Assez facile, hein ? D'accord, passons en revue cela.

```
object.data.forEach(function(gif) {  var url = gif.images.original.url;  var image = $('<img src=' + url + ' />');  image.appendTo($('body'));});
```

La méthode _forEach_, une méthode JavaScript vanilla, itérera à travers tous les tableaux et nous attribuons chaque objet de tableau à la variable _gif_. Dans chacun des objets _gif_, il y a la propriété _images.original.url_ qui est l'URL dont nous avons besoin pour définir l'attribut _src_ de chaque balise image.

Après avoir ces données, nous pouvons maintenant créer la balise _img_, en attribuant l'URL à l'attribut _src_. Nous ajoutons ensuite cette image au DOM.

Bada bing, bada boom, vous avez maintenant une source infinie de bonheur gif à portée de main.

Le projet terminé ressemble maintenant à quelque chose comme ceci :

Et le voici sur CodePen :

Vous n'auriez probablement pas pensé que l'accès et l'utilisation des API étaient si faciles. Mais comme vous pouvez le voir, à partir d'une simple ligne de code de la taille d'un chat, vous avez pu changer dynamiquement votre site d'une simple application d'image de chat aléatoire à une application de recherche Giphy beaucoup plus puissante.

Comme vous pouvez également le constater, les styles ont l'air tristes. Utilisez ce que vous avez appris en développement web jusqu'à présent pour faire de cela une application géniale avec vos styles supplémentaires. Soyez créatif avec cela, mais surtout, amusez-vous !

_Note de bas de page : La clé API que nous avons utilisée était destinée uniquement à des fins de développement, et non pour la production. Cela signifie que vous ne pouvez pas vous déchaîner et faire un million d'appels à l'API Giphy. Ils vous fermeront._

J'espère que vous avez passé un autre bon moment à apprendre le monde merveilleux de JavaScript. Jusqu'à la prochaine fois, que vous et les API alliez ensemble comme les petits pois et les carottes !