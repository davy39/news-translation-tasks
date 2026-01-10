---
title: Qu'est-ce que les grammaires hors contexte ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-14T09:39:14.000Z'
originalURL: https://freecodecamp.org/news/context-free-grammar
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Lee
seo_title: Qu'est-ce que les grammaires hors contexte ?
---

Company.png
tags:
- name: compilers
  slug: compilers
- name: finite state machine
  slug: finite-state-machine
- name: linguistics
  slug: linguistics
- name: programming languages
  slug: programming-languages
seo_title: null
seo_desc: 'Par Aditya

  Avez-vous déjà remarqué que, lorsque vous écrivez du code dans un éditeur de texte comme VS code,
  il reconnaît des choses comme les accolades non appariées ? Et il vous avertit parfois, avec
  un surlignage rouge irritant, de la syntaxe incorrecte que vous avez écr...'
---

Par Aditya

Avez-vous déjà remarqué que, lorsque vous écrivez du code dans un éditeur de texte comme VS code, il reconnaît des choses comme les accolades non appariées ? Et il vous avertit parfois, avec un surlignage rouge irritant, de la syntaxe incorrecte que vous avez écrite ?

Si ce n'est pas le cas, alors réfléchissez-y. Après tout, c'est un morceau de code. Comment pouvez-vous écrire du code pour une telle tâche ? Quelle serait la logique sous-jacente ?

Ce sont le genre de questions auxquelles vous serez confronté si vous devez écrire un compilateur pour un langage de programmation. Écrire un compilateur n'est pas une tâche facile. C'est un travail volumineux qui demande une quantité significative de temps et d'efforts.

Dans cet article, nous ne allons pas parler de la façon de construire des compilateurs. Mais nous allons parler d'un concept qui est un composant central du compilateur : les grammaires hors contexte.

## Introduction

Toutes les questions que nous avons posées précédemment représentent un problème significatif pour la conception de compilateurs appelé Analyse Syntaxique. Comme le nom le suggère, le défi est d'analyser la syntaxe et de voir si elle est correcte ou non. C'est là que nous utilisons les grammaires hors contexte. Une grammaire hors contexte est un ensemble de règles qui définissent un langage.

Ici, j'aimerais établir une distinction entre les grammaires hors contexte et les grammaires pour les langues naturelles comme l'anglais.

Les grammaires hors contexte ou CFG définissent un langage formel. Les langues formelles fonctionnent strictement selon les règles définies et leurs phrases ne sont pas influencées par le contexte. Et c'est de là que vient le nom _hors contexte_.

Les langues comme l'anglais tombent dans la catégorie des langues informelles puisqu'elles sont affectées par le contexte. Elles ont de nombreuses autres caractéristiques qu'une CFG ne peut pas décrire.

Même si les CFG ne peuvent pas décrire le contexte dans les langues naturelles, elles peuvent encore définir la syntaxe et la structure des phrases dans ces langues. En fait, c'est la raison pour laquelle les CFG ont été introduites en premier lieu.

Dans cet article, nous allons tenter de générer des phrases anglaises en utilisant des CFG. Nous allons apprendre comment décrire la structure des phrases et écrire des règles pour cela. Pour ce faire, nous allons utiliser une bibliothèque JavaScript appelée Tracery qui générera des phrases sur la base des règles que nous avons définies pour notre grammaire.

Avant de plonger dans le code et de commencer à écrire les règles pour la grammaire, discutons simplement de quelques termes de base que nous allons utiliser dans notre CFG.

**Terminaux** : Ce sont les caractères qui constituent le contenu réel de la phrase finale. Ceux-ci peuvent inclure des mots ou des lettres selon lequel de ces éléments est utilisé comme bloc de construction de base d'une phrase.

Dans notre cas, nous utiliserons des mots comme blocs de construction de base de nos phrases. Donc nos terminaux incluront des mots tels que "to", "from", "the", "car", "spaceship", "kittens" et ainsi de suite.

**Non-Terminaux** : Ceux-ci sont également appelés variables. Ceux-ci agissent comme un sous-langage au sein du langage défini par la grammaire. Les non-terminaux sont des espaces réservés pour les terminaux. Nous pouvons utiliser des non-terminaux pour générer différents motifs de symboles terminaux.

Dans notre cas, nous utiliserons ces non-terminaux pour générer des phrases nominales, des phrases verbales, différents noms, adjectifs, verbes et ainsi de suite.

**Symbole de départ** : un symbole de départ est un non-terminal spécial qui représente la chaîne initiale qui sera générée par la grammaire.

Maintenant que nous connaissons la terminologie, commençons à apprendre les règles grammaticales.

Lors de l'écriture des règles de grammaire, nous commencerons par définir l'ensemble des terminaux et un état de départ. Comme nous l'avons appris précédemment, ce symbole de départ est un non-terminal. Cela signifie qu'il appartiendra à l'ensemble des non-terminaux.

```
T: ("Monkey", "banana", "ate", "the")
S: État de départ.

```

Et les règles sont :

```
S --> nounPhrase verbPhrase
nounPhrase --> adj nounPhrase | adj noun
verbPhrase --> verb nounPhrase
adjective  --> the
noun --> Monkey | banana
verb --> ate
```

Les règles grammaticales ci-dessus peuvent sembler quelque peu cryptiques au premier abord. Mais si nous regardons attentivement, nous pouvons voir un motif qui est généré à partir de ces règles.

Une meilleure façon de penser aux règles ci-dessus est de les visualiser sous la forme d'une structure d'arbre. Dans cet arbre, nous pouvons mettre _S_ à la racine et _nounPhrase_ et _verbPhrase_ peuvent être ajoutés comme enfants de la racine. Nous pouvons procéder de la même manière avec _nounPhrase_ et _verbPhrase_ également. L'arbre aura des terminaux comme ses nœuds feuilles car c'est là que nous mettons fin à ces dérivations.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/parsetree.png)

Dans l'image ci-dessus, nous pouvons voir que _S_ (un non-terminal) dérive deux non-terminaux _NP_ (_nounPhrase_) et _VP_ (_verbPhrase_). Dans le cas de _NP_, il a dérivé deux non-terminaux, _Adj_ et _Noun_.

Si vous regardez la grammaire, _NP_ aurait également pu choisir _Adj_ et _nounPhrase_. Lors de la génération de texte, ces choix sont faits aléatoirement.

Et enfin, les nœuds feuilles ont des terminaux qui sont écrits en texte gras. Donc si vous vous déplacez de gauche à droite, vous pouvez voir qu'une phrase est formée.

Le terme souvent utilisé pour cet arbre est un arbre d'analyse. Nous pouvons créer un autre arbre d'analyse pour une phrase différente générée par cette grammaire de manière similaire.

Maintenant, procédons à la partie code. Comme je l'ai mentionné précédemment, nous allons utiliser une bibliothèque JavaScript appelée Tracery pour la génération de texte en utilisant des CFG. Nous allons également écrire du code en HTML et CSS pour la partie front-end.

## Le Code

Commençons par obtenir la bibliothèque tracery. Vous pouvez cloner la bibliothèque depuis GitHub [ici](https://github.com/galaxykate/tracery). J'ai également laissé le lien vers le dépôt GitHub de galaxykate à la fin de l'article.

Avant d'utiliser la bibliothèque, nous devrons l'importer. Nous pouvons faire cela simplement dans un fichier HTML comme ceci.

```html
<html>
    <head>
        <script src="tracery-master/js/vendor/jquery-1.11.2.min.js"></script>
		<script src="tracery-master/tracery.js"></script>
		<script src="tracery-master/js/grammars.js"></script>
        <script src='app.js'></script>
    </head>
    
</html>
```

J'ai ajouté le fichier tracery cloné comme un script dans mon code HTML. Nous devrons également ajouter JQuery à notre code car tracery dépend de JQuery. Enfin, j'ai ajouté _app.js_ qui est le fichier où j'ajouterai des règles pour la grammaire.

Une fois cela fait, créez un fichier JavaScript où nous définirons nos règles de grammaire.

```javascript
var rules = {
    	"start": ["#NP# #VP#."],
    	"NP": ["#Det# #N#", "#Det# #N# that #VP#", "#Det# #Adj# #N#"],
    	"VP": ["#Vtrans# #NP#", "#Vintr#"],
    	"Det": ["The", "This", "That"],
    	"N": ["John Keating", "Bob Harris", "Bruce Wayne", "John Constantine", "Tony Stark", "John Wick", "Sherlock Holmes", "King Leonidas"],
    	"Adj": ["cool", "lazy", "amazed", "sweet"],
    	"Vtrans": ["computes", "examines", "helps", "prefers", "sends", "plays with", "messes up with"],
    	"Vintr": ["coughs", "daydreams", "whines", "slobbers", "appears", "disappears", "exists", "cries", "laughs"]
    }
    
```

Ici, vous remarquerez que la syntaxe pour définir les règles n'est pas très différente de la façon dont nous avons défini notre grammaire précédemment. Il y a des différences très mineures telles que la façon dont les non-terminaux sont définis entre les symboles de hachage. Et aussi la façon dont les différentes dérivations sont écrites. Au lieu d'utiliser le symbole "|" pour les séparer, ici nous mettrons toutes les différentes dérivations comme différents éléments d'un tableau. Autre que cela, nous utiliserons les points-virgules au lieu des flèches pour représenter la transition.

Cette nouvelle grammaire est un peu plus compliquée que celle que nous avons définie précédemment. Celle-ci inclut de nombreuses autres choses telles que les déterminants, les verbes transitifs et les verbes intransitifs. Nous faisons cela pour que le texte généré semble plus naturel.

Appelons maintenant la fonction tracery "createGrammar" pour créer la grammaire que nous venons de définir.

```javascript
let grammar = tracery.createGrammar(rules);
```

Cette fonction prendra l'objet de règles et générera une grammaire sur la base de ces règles. Après avoir créé la grammaire, nous voulons maintenant générer un résultat final à partir de celle-ci. Pour cela, nous utiliserons une fonction appelée "flatten".

```javascript
let expansion = grammar.flatten('#start#');
```

Cela générera une phrase aléatoire basée sur les règles que nous avons définies précédemment. Mais n'arrêtons pas là. Construisons également une interface utilisateur pour cela. Il n'y a pas grand-chose à faire pour cette partie – nous avons juste besoin d'un bouton et de quelques styles de base pour l'interface.

Dans le même fichier HTML où nous avons ajouté les bibliothèques, nous ajouterons quelques éléments.

```html
<html>
    <head>
        <title>Phrases Étranges</title>
        <link rel="stylesheet" href="style.css"/>
        <link href="https://fonts.googleapis.com/css?family=UnifrakturMaguntia&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Harmattan&display=swap" rel="stylesheet">
        
        <script src="tracery-master/js/vendor/jquery-1.11.2.min.js"></script>
		<script src="tracery-master/tracery.js"></script>
		<script src="tracery-master/js/grammars.js"></script>
        <script src='app.js'></script>
    </head>
    <body>
        <h1 id="h1">Phrases Étranges</h1>
        <button id="generate" onclick="generate()">Donnez-moi une phrase !</button>
        <div id="sentences">

        </div>
    </body>
</html>
```

Et enfin, nous ajouterons quelques styles.

```css
body {
    text-align: center;
    margin: 0;
    font-family: 'Harmattan', sans-serif;
}

#h1 {
    font-family: 'UnifrakturMaguntia', cursive;
    font-size: 4em;
    background-color: rgb(37, 146, 235);
    color: white;
    padding: .5em;
    box-shadow: 1px 1px 1px 1px rgb(206, 204, 204);
}

#generate {
    font-family: 'Harmattan', sans-serif;
    font-size: 2em;
    font-weight: bold;
    padding: .5em;
    margin: .5em;
    box-shadow: 1px 1px 1px 1px rgb(206, 204, 204);
    background-color: rgb(255, 0, 64);
    color: white;
    border: none;
    border-radius: 2px;
    outline: none;
}

#sentences p {
    box-shadow: 1px 1px 1px 1px rgb(206, 204, 204);
    margin: 2em;
    margin-left: 15em;
    margin-right: 15em;
    padding: 2em;
    border-radius: 2px;
    font-size: 1.5em;
}
```

Nous devrons également ajouter un peu plus de JavaScript pour manipuler l'interface.

```javascript
let sentences = []
function generate() {
    var data = {
    	"start": ["#NP# #VP#."],
    	"NP": ["#Det# #N#", "#Det# #N# that #VP#", "#Det# #Adj# #N#"],
    	"VP": ["#Vtrans# #NP#", "#Vintr#"],
    	"Det": ["The", "This", "That"],
    	"N": ["John Keating", "Bob Harris", "Bruce Wayne", "John Constantine", "Tony Stark", "John Wick", "Sherlock Holmes", "King Leonidas"],
    	"Adj": ["cool", "lazy", "amazed", "sweet"],
    	"Vtrans": ["computes", "examines", "helps", "prefers", "sends", "plays with", "messes up with"],
    	"Vintr": ["coughs", "daydreams", "whines", "slobbers", "appears", "disappears", "exists", "cries", "laughs"]
    }
    
    let grammar = tracery.createGrammar(data);
    let expansion = grammar.flatten('#start#');

    sentences.push(expansion);

    printSentences(sentences);
}

function printSentences(sentences) {
    let textBox = document.getElementById("sentences");
    textBox.innerHTML = "";
    for(let i=sentences.length-1; i>=0; i--) {
        textBox.innerHTML += "<p>"+sentences[i]+"</p>"
    }
}

```

Une fois que vous avez terminé d'écrire le code, exécutez votre fichier HTML. Cela devrait ressembler à quelque chose comme ceci.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/ws2.png)

Chaque fois que vous cliquez sur le bouton rouge, il générera une phrase. Certaines de ces phrases peuvent ne pas avoir de sens. Cela est dû, comme je l'ai dit précédemment, au fait que les CFG ne peuvent pas décrire le contexte et certaines autres caractéristiques que possèdent les langues naturelles. Il est utilisé uniquement pour définir la syntaxe et la structure des phrases.

Vous pouvez consulter la version live de cela [ici](https://aditya2000.github.io/weird-sentences/).

## Conclusion

Si vous êtes arrivé jusqu'ici, j'apprécie grandement votre résilience. Cela peut être un nouveau concept pour certains d'entre vous, et d'autres peuvent en avoir appris dans leurs cours universitaires. Mais encore, les grammaires hors contexte ont des applications intéressantes qui vont de l'informatique à la linguistique.

J'ai fait de mon mieux pour présenter les idées principales des CFG ici, mais il y a beaucoup plus que vous pouvez apprendre à leur sujet. Ici, j'ai laissé des liens vers quelques excellentes ressources :

* [Context Free Grammars](https://youtu.be/C3EwsSNJeOE) par Daniel Shiffman.
* [Context Free Grammars Examples](https://youtu.be/R_OVyFrBhiU) par Fullstack Academy
* [Tracery](https://github.com/galaxykate/tracery) par Galaxykate