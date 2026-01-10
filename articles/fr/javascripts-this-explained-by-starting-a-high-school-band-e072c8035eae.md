---
title: Le "this" de JavaScript expliqué en créant un groupe de lycée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-12T02:59:10.000Z'
originalURL: https://freecodecamp.org/news/javascripts-this-explained-by-starting-a-high-school-band-e072c8035eae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sQcxkf5QH-TA29tcMGDHGA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Le "this" de JavaScript expliqué en créant un groupe de lycée
seo_desc: 'By Kevin Kononenko

  If you have ever been in a band, had a friend that started a band, or seen a corny
  80s movie about starting a band, then you can understand the concept of “this” in
  JavaScript.

  When you are reading over some JavaScript, and you com...'
---

Par Kevin Kononenko

Si vous avez déjà été dans un groupe, eu un ami qui a créé un groupe, ou vu un film des années 80 sur la création d'un groupe, alors vous pouvez comprendre le concept de "this" en JavaScript.

Lorsque vous lisez du JavaScript et que vous tombez sur le mot-clé _this_, les étapes à suivre pour déterminer sa valeur peuvent sembler évidentes.

Vous pourriez penser : « Je dois simplement trouver la fonction qui contient _this_, et alors je saurai à quoi il fait référence ! »

```
let band= {  name: "myBand",  playGig:function() {    console.log("Please welcome to the stage" + this.name);  }}
```

Dans l'exemple ci-dessus, par exemple, _this.name_ fait référence au nom « myBand ». Cela semble facile !

Mais, à mesure que vous apprenez davantage de concepts JavaScript, comme les fermetures et les rappels, vous constaterez rapidement que _this_ ne se comporte pas comme vous pourriez vous y attendre.

Ainsi, j'ai voulu créer une explication visuelle de la manière dont _this_ fonctionne en JavaScript. Voici le scénario : Vous êtes de retour au lycée et vous créez un groupe avec vos amis (ou peut-être êtes-vous actuellement au lycée ?)

* Votre groupe compte quatre membres
* Vous jouez trois types de concerts : vous jouez dans des bars, des compétitions scolaires et des événements publics en ville.
* Votre équipe peut jouer tous les types de musique, donc vous essayez de choisir les bonnes chansons pour correspondre au public. Vous ne voulez pas de mots grossiers ou de références sexuelles lors des événements familiaux, par exemple.

Comme vous le verrez bientôt, le plus grand concept que vous devez comprendre avec _this_ est le **contexte d'exécution**. C'est ce qui détermine la valeur de _this_.

Avant d'utiliser ce tutoriel, vous devez comprendre les [objets](https://blog.codeanalogies.com/2017/04/29/javascript-arrays-and-objects-are-just-like-books-and-newspapers/) et les [variables](https://blog.codeanalogies.com/2017/12/20/a-visual-guide-to-understanding-the-sign-in-javascript/). Consultez mes tutoriels sur chacun de ces sujets si vous avez besoin de les réviser.

Si vous êtes intéressé par une version plus technique de ce tutoriel, consultez le [guide de JavaScriptIsSexy](http://javascriptissexy.com/understand-javascripts-this-with-clarity-and-master-it/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*vkmneQ0bjkfUKE4A.)

### Le Contexte d'Exécution Global

Supposons que votre groupe doive faire un concert familial au parc local dans le cadre d'une foire locale. Vous devez choisir le bon type de musique qui gardera les parents heureux et ne choquera personne.

Supposons que vous choisissiez de jouer quelques chansons de [Billy Joel](https://en.wikipedia.org/wiki/Billy_Joel) (un célèbre artiste américain), et même si ce n'est pas votre préféré, vous savez que c'est ce que vous devez faire pour être payé.

Voici à quoi cela ressemble en code.

```
//Les chansons que vous allez jouer var artist= "Billy Joel"; 
```

```
function playGig(){   //instruments que votre groupe va utiliser   let instruments= ["piano", "microphone", "acousticGuitar", "harmonica"]; 
```

```
  console.log("Nous allons jouer de la musique de " + this.artist + "ce soir !"); } 
```

```
playGig();
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*nDmTsWSyhway3yRK.)

Dans l'exemple ci-dessus, nous avons une variable **artist** qui indique le type de musique que nous allons jouer. Et nous avons un tableau rempli d'_instruments_ qui seront utilisés pour jouer cette musique dans la fonction playGig.

Dans la dernière ligne, nous appelons la fonction playGig. Alors, qu'est-ce que _this.artist_, dans ce cas ?

Eh bien, nous devons d'abord déterminer le **contexte d'exécution** pour cette fonction. Le contexte d'exécution est déterminé par **l'objet sur lequel la fonction est appelée**.

Dans ce cas, il n'y a aucun objet listé, ce qui signifie que la fonction est appelée sur l'objet _window_. Elle pourrait également être appelée comme ceci :

```
window.playGig(); "Nous allons jouer de la musique de Billy Joel ce soir !"
```

C'est le contexte d'exécution **global**. La fonction est appelée au niveau de l'objet global, _window_. Et la variable _artist_ est disponible en tant que propriété de l'objet _window_ ([voir cette note sur la spécification JavaScript](https://stackoverflow.com/questions/19855823/are-global-variables-just-properties-on-the-window-object)).

Ainsi, dans la ligne 1 de l'extrait ci-dessus, nous disons également :

```
//ancienne version- let artist = "Billy Joel"; this.artist="Billy Joel";
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*pR8LAtC76p1kvE5s.)

Votre groupe exécute le concert dans le contexte global en jouant de la musique qui plaît à tout le monde (sauf s'il y a des haters de Billy Joel par là).

![Image](https://cdn-media-1.freecodecamp.org/images/0*19QcrhPgf38OU00_.)

### Contexte d'Exécution au Niveau de l'Objet

Supposons que votre groupe ait obtenu un concert dans un bar local. C'est génial ! Maintenant, vous n'avez pas besoin de jouer de la musique qui satisfait tout le monde en ville. Vous devez simplement jouer de la musique à laquelle les gens peuvent danser.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_djQrnI4NQ5nDzD2.)

Supposons que vous choisissiez [Coldplay](https://en.wikipedia.org/wiki/Coldplay), puisque la plupart de leurs chansons récentes sont de la musique pop. Vous avez besoin d'un piano, d'un microphone, d'une batterie et d'une guitare pour ce concert.

Créons un objet bar avec le même modèle que celui que nous avons créé pour le concert au parc public.

```
//Les chansons que vous allez jouer dans le parc public/foire var artist= "Billy Joel"; 
```

```
function playGig(){   //instruments que votre groupe va utiliser   let instruments= ["piano", "microphone", "acousticGuitar", "harmonica"];   console.log("Nous allons jouer de la musique de " + this.artist + "ce soir !"); } 
```

```
//NOUVELLE PARTIE let bar = {  artist:"coldplay",  playGig: function(){     //instruments que votre groupe va utiliser     let instruments= ["piano", "microphone", "guitar", "drumset"];         console.log("Nous allons jouer de la musique de " + this.artist + "ce soir !");    } }
```

Voici le diagramme pour le code ci-dessus :

![Image](https://cdn-media-1.freecodecamp.org/images/0*hfc66VpcvHZZueNz.)

Ainsi, supposons que nous voulons écrire le code pour commencer le concert au bar. Nous devons surveiller notre **contexte d'exécution**, qui est l'objet _bar_ dans ce cas. Voici à quoi cela ressemblerait :

```
bar.playGig(); //"Nous allons jouer de la musique de coldplay ce soir !"
```

Et nous pouvons toujours exécuter la fonction playGig au niveau global — mais nous obtiendrons une sortie différente. C'est une bonne nouvelle, puisque nous ne voulons pas jouer Billy Joel ou Coldplay au mauvais endroit...

```
playGig(); //"Nous allons jouer de la musique de Billy Joel ce soir !"
```

Jusqu'à présent, cela a été la partie facile. Chaque fois que nous avons appelé une fonction, l'objet qui fournit le **contexte d'exécution** a été assez simple. Mais cela est sur le point de changer à mesure que nous devenons plus complexes.

![Image](https://cdn-media-1.freecodecamp.org/images/0*F1hheXRD2SSTmszz.)

### Changer le Contexte d'Exécution en utilisant jQuery

C'est le grand événement qui a été couvert dans chaque film des années 1980 : La Bataille des Groupes ! Oui, chaque groupe de votre lycée va entrer en compétition pour voir qui est le meilleur.

Vous allez jouer quelques chansons de [AC/DC](https://en.wikipedia.org/wiki/AC/DC), probablement le groupe le plus cool de la planète. Mais pour cela, vous avez besoin d'un mélange d'instruments différent de celui d'avant :

* Un microphone
* Une guitare électrique
* Une basse
* Une batterie

Appelons cela l'objet **battle**. Voici à quoi cela ressemble en code.

```
let battle = {  artist:"acdc",  playGig: function(){     //instruments que votre groupe va utiliser     let instruments= ["microphone", "electricguitar", "bass", "drumset"]; 
```

```
    console.log("Nous allons jouer de la musique de " + this.artist + "ce soir !");   } }
```

Puisque c'est un événement annuel, nous allons utiliser un événement **click** de jQuery pour commencer votre spectacle. Voici à quoi cela ressemble :

```
$('#annualBattle').click(battle.playGig);
```

Mais si vous exécutiez réellement ce code... cela ne fonctionnerait pas. Votre groupe oublierait les paroles et les notes, puis quitterait lentement la scène.

Pour comprendre pourquoi, revenons au contexte d'exécution. Nous faisons référence à un élément DOM appelé _#annualBattle_, alors voyons où cela s'insère dans l'objet _window_.

Puisque _#annualBattle_ est un élément du DOM, il fait partie de l'objet _document_ dans l'objet _window_. Il n'a aucune propriété appelée _artist_. Donc si vous exécutiez le code, vous obtiendriez :

```
$('#annualBattle').click(battle.playGig); //"Nous allons jouer de la musique de undefined ce soir !"
```

Dans ce cas, le **contexte d'exécution** est un élément du DOM. C'est ce qui a déclenché la méthode click(), qui a utilisé la fonction playGig comme **rappel**. Ainsi, _this_ aura une valeur indéfinie.

Dans notre analogie, cela signifie que votre groupe est arrivé à la compétition avec tous leurs instruments, s'est mis en position pour jouer, puis a regardé la foule comme si elle allait leur dire quoi faire. Cela signifie que vous avez oublié le contexte de pourquoi vous étiez là en premier lieu.

Pour résoudre cela, nous devons utiliser la [méthode bind()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) pour nous assurer que la méthode playGig fait toujours référence à l'objet _battle_, même lorsque nous l'appelons depuis le contexte d'un autre objet ! Cela ressemble à ceci :

```
$('#annualBattle').click(battle.playGig.bind(battle)); //"Nous allons jouer de la musique de acdc ce soir !"
```

Maintenant, nous obtenons la bonne sortie, même si le contexte était un élément DOM.

### Extraire une Fonction de son Contexte

Supposons que nous voulions écrire le code qui nous permettra de répéter pour l'événement Battle of the Bands. Nous allons créer une variable séparée appelée _practice_, et assigner la **méthode** playGig de l'objet _battle_.

```
var artist= "Billy Joel"; 
```

```
function playGig(){  //instruments que votre groupe va utiliser   let instruments= ["piano", "microphone", "acousticGuitar", "harmonica"]; 
```

```
  console.log("Nous allons jouer de la musique de " + this.artist + "ce soir !"); } 
```

```
let battle = {  artist:"acdc",   playGig: function(){     //instruments que votre groupe va utiliser     let instruments= ["microphone", "electricguitar", "bass", "drumset"]; 
```

```
    console.log("Nous allons jouer de la musique de " + this.artist + "ce soir !");   } } 
```

```
let practice = battle.playGig; //exécuter une répétition practice();
```

Vous vous demandez probablement : quel est le contexte d'exécution de la dernière ligne ?

Eh bien, cela rencontrera un problème similaire à l'exemple précédent. Lorsque nous créons la variable _practice_, nous stockons maintenant une instance de la méthode playGig dans le **contexte global** ! Elle n'est plus dans le contexte de l'objet battle.

![Image](https://cdn-media-1.freecodecamp.org/images/0*nsh11uuf9M7miGMI.)

Si nous exécutions le code ci-dessus, nous obtiendrions :

```
practice(); 
```

```
//"Nous allons jouer de la musique de Billy Joel ce soir !"
```

Pas ce que nous voulons. Nous essayons de répéter AC/DC, et nous répétons Billy Joel à la place. Oups.

Au lieu de cela, nous devons utiliser la méthode bind() comme ci-dessus. Cela nous permettra de lier le contexte de l'objet _battle_.

```
let practice = battle.playGig.bind(battle); 
```

```
practice(); //"Nous allons jouer de la musique de AC/DC ce soir !"
```

### Comment les Fonctions Anonymes Affectent le Contexte

Supposons que votre concert touche à sa fin, et que vous voulez donner un coup de projecteur à tout le monde dans votre groupe afin que la foule puisse applaudir chaque personne.

Pour ce faire, nous allons utiliser la méthode forEach() pour itérer à travers chaque élément dans la valeur de la propriété _instruments_. (Vous verrez pourquoi nous l'avons changée d'une variable à une propriété dans un instant). Cela ressemblera à ceci :

```
let battle = {  artist:"acdc",
```

```
  //instruments que votre groupe va utiliser  instruments: ["microphone", "electricguitar", "bass", "drumset"],
```

```
  shoutout: function(){ 
```

```
    this.instruments.forEach(function(instrument){      console.log("Donnez un coup de projecteur à mon ami pour avoir couvert le " + instrument + " de " + this.artist + "!");     }   } } 
```

```
battle.shoutout();
```

Mais encore une fois, si nous exécutions ce code, cela ne fonctionnerait pas.

Tout tourne autour de la ligne où nous déclarons une fonction anonyme à utiliser sur chaque élément dans _instruments_. Lorsque cette fonction est exécutée, le premier _this_ conservera le bon contexte : l'objet _battle_.

Mais, lorsque nous arrivons à _this.artist_ dans l'instruction console.log, nous obtiendrons... « Billy Joel ». Cela est dû à la fonction anonyme qui est utilisée comme rappel dans la méthode forEach(). Elle réinitialise la portée au contexte global.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BACZfoonzMUUwpfNzi9jIw.png)

Dans ce cas, cela signifie que nous affirmerions à la fin jouer Billy Joel... d'oh !

Mais voici ce que nous pouvons faire. Nous pouvons créer une nouvelle variable appelée _that_ pour stocker _this_ dans le bon contexte. Ensuite, lorsque nous faisons référence à l'artiste que nous avons joué dans ce concert spécifique, nous pouvons faire référence au contexte stocké, plutôt que d'être forcés de revenir au contexte global.

```
let battle = {  artist:"acdc",  //instruments que votre groupe va utiliser   instruments: ["microphone", "electricguitar", "bass", "drumset"],   shoutout: function(){
```

```
    //stocker le contexte de this     let that = this;
```

```
    this.instruments.forEach(function(instrument){      console.log("Donnez un coup de projecteur à mon ami pour avoir couvert le " + instrument + " de " + that.artist + "!");    }   } }
```

```
battle.shoutout();
```

### Obtenez les Derniers Tutoriels

Avez-vous apprécié ce tutoriel ? Si oui, donnez-lui un applaudissement ou inscrivez-vous aux derniers tutoriels visuels de CodeAnalogies ici :