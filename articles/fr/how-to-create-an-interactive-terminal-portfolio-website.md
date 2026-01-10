---
title: Comment créer un site web de portfolio de terminal interactif
subtitle: ''
author: Jakub T. Jankiewicz
co_authors: []
series: null
date: '2024-04-29T14:49:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-interactive-terminal-portfolio-website
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730895455049/8fefc48c-761d-4ec5-8f60-b6eb2f97a42a.png
tags:
- name: portfolio
  slug: portfolio
- name: projects
  slug: projects
- name: terminal
  slug: terminal
seo_title: Comment créer un site web de portfolio de terminal interactif
seo_desc: 'In this article, you will learn how to create an interactive terminal-based
  portfolio and a résumé in JavaScript. We''ll use the jQuery Terminal library (and
  a few other tools) to create a website that looks like a real terminal.

  This article will sho...'
---

Dans cet article, vous apprendrez à créer un portfolio basé sur un terminal interactif et un curriculum vitæ en JavaScript. Nous utiliserons la bibliothèque [jQuery Terminal](https://terminal.jcubic.pl/) (et quelques autres outils) pour créer un site web qui ressemble à un vrai terminal.

Cet article montrera une utilisation plus avancée de la bibliothèque jQuery Terminal. Si vous voulez quelque chose de plus basique, vous pouvez consulter cet article : [Comment créer un site web interactif de type terminal avec JavaScript](https://itnext.io/how-to-create-interactive-terminal-like-website-888bb0972288) qui est écrit pour des programmeurs de niveau plus débutant. Vous pouvez également le lire (ou le parcourir) avant de commencer à lire celui-ci.

## Table des matières

* [Qu'est-ce que le terminal et son histoire ?](#heading-quest-ce-que-le-terminal-et-son-histoire)
    
* [Qu'est-ce que jQuery Terminal ?](#heading-quest-ce-que-jquery-terminal)
    
* [Fichier HTML de base](#heading-fichier-html-de-base)
    
* [Comment initialiser le terminal](#heading-comment-initialiser-le-terminal)
    
* [Message de bienvenue](#heading-message-de-bienvenue)
    
* [Espacements de ligne](#heading-espacements-de-ligne)
    
* [Comment ajouter des couleurs à l'art ASCII](#heading-comment-ajouter-des-couleurs-a-lart-ascii)
    
    * [Formatage du terminal](#heading-formatage-du-terminal)
        
    * [Comment utiliser la bibliothèque Lolcat](#heading-comment-utiliser-la-bibliotheque-lolcat)
        
    * [Salutations en art ASCII arc-en-ciel](#heading-salutations-en-art-ascii-arc-en-ciel)
        
    * [Comment rendre le texte de salutation blanc](#heading-comment-rendre-le-texte-de-salutation-blanc)
        
* [Comment créer votre première commande](#heading-comment-creer-votre-premiere-commande)
    
* [Commandes par défaut](#heading-commandes-par-defaut)
    
* [Comment rendre les commandes d'aide exécutables](#heading-comment-rendre-les-commandes-daide-executables)
    
* [Coloration syntaxique](#heading-coloration-syntaxique)
    
* [Complétion par tabulation](#heading-completion-par-tabulation)
    
* [Comment ajouter des commandes shell](#heading-comment-ajouter-des-commandes-shell)
    
* [Comment améliorer la complétion](#heading-comment-ameliorer-la-completion)
    
* [Commande d'animation de frappe](#heading-commande-danimation-de-frappe)
    
* [Commande de crédits](#heading-commande-de-credits)
    
* [Commandes préremplies](#heading-commandes-preremplies)
    
* [Partage de lien vers une session de terminal](#heading-partage-de-lien-vers-une-session-de-terminal)
    
* [Démonstration de portfolio de terminal fonctionnel](#heading-demonstration-de-portfolio-de-terminal-fonctionnel)
    
* [Ajout d'exécutables au répertoire personnel](#heading-ajout-dexecutables-au-repertoire-personnel)
    
* [Et ensuite ?](#heading-et-ensuite)
    
* [Partagez ce que vous avez créé](#heading-partagez-ce-que-vous-avez-cree)
    

## Qu'est-ce que le terminal et son histoire ?

Les terminaux ont une longue histoire. Tout a commencé comme une amélioration par rapport aux [cartes perforées](https://en.wikipedia.org/wiki/Punched_card). Les ordinateurs de l'époque utilisaient des télétypes, qui n'étaient qu'un clavier et une imprimante. Vous tapiez sur le clavier, et les frappes étaient envoyées à l'ordinateur (généralement un mainframe) et la sortie était imprimée sur une imprimante.

Plus tard, les télétypes ont été remplacés par des terminaux. Un terminal était comme l'ordinateur basique que nous voyons aujourd'hui. C'était un moniteur CRT avec un clavier. Ainsi, au lieu d'obtenir la sortie sur l'imprimante, elle était affichée sur le moniteur.

Aujourd'hui, nous utilisons toujours ce type d'interface (la ligne de commande) pour communiquer avec les ordinateurs.

La ligne de commande est un émulateur de terminal et fait partie intégrante des systèmes Unix, comme GNU/Linux ou MacOS. Sur Windows, vous avez PowerShell ou le fichier cmd.exe qui vous permet de taper des commandes et d'obtenir des réponses sous forme de texte. Vous pouvez également installer un système GNU/Linux sur Windows sous forme de WSL. Les interfaces CLI sont principalement utilisées par les utilisateurs avancés, les développeurs et les administrateurs système.

Si vous êtes nouveau dans le monde de la ligne de commande, vous pouvez lire cet article : [Ligne de commande pour débutants – Comment utiliser le terminal comme un pro \[Manuel complet\]](https://www.freecodecamp.org/news/command-line-for-beginners/).

## Qu'est-ce que jQuery Terminal ?

jQuery Terminal est une bibliothèque JavaScript. C'est un plugin pour la bibliothèque [jQuery](https://en.wikipedia.org/wiki/JQuery). jQuery Terminal est plus comme un framework qui a jQuery comme dépendance. Nous utiliserons principalement JavaScript et très peu jQuery dans cet article.

Créons notre portfolio basé sur un terminal en utilisant jQuery Terminal.

### Fichier HTML de base

La première chose à faire est d'inclure jQuery et la bibliothèque jQuery Terminal dans votre projet.

Voici un fichier HTML de base :

```html
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/jquery.terminal/css/jquery.terminal.min.css"/>
</head>
<body>
<script src="https://cdn.jsdelivr.net/npm/jquery"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery.terminal/js/jquery.terminal.min.js"></script>
<script src="my-terminal.js"></script>
</body>
</html>
```

Ensuite, à l'intérieur du fichier **my-terminal.js**, nous écrirons notre code en JavaScript.

### Comment initialiser le terminal

Pour créer un terminal de base, vous devez insérer ce code :

```javascript
const commands = {};

const term = $('body').terminal(commands);
```

La chaîne `'body'` indique le sélecteur CSS où le terminal doit être créé. Ici, nous utilisons `'body'` pour que le terminal soit la seule chose sur la page. Mais il n'a pas besoin d'être en plein écran. Vous pouvez créer un site web où le terminal n'est qu'une partie de la page, comme dans une fenêtre qui ressemble à une partie du système d'exploitation.

Le premier argument de la méthode terminal est appelé un interpréteur. C'est un moyen d'ajouter vos commandes. Un objet est le moyen le plus simple de les créer. Voir [création de l'interpréteur](https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#creating-the-interpreter) pour en savoir plus.

Si la police du terminal est trop petite, vous pouvez la rendre un peu plus grande avec des propriétés CSS personnalisées (également connues sous le nom de variables CSS) :

```css
:root {
    --size: 1.2;
}
```

### Message de bienvenue

La première chose à faire est de se débarrasser du message de salutation par défaut et de le remplacer par un bel art ASCII personnalisé. Nous utiliserons la bibliothèque [Filget](https://en.wikipedia.org/wiki/FIGlet) écrite en JavaScript pour cela.

Il existe quelques bibliothèques Figlet sur npm. Nous utiliserons un package nommé [figlet](https://www.npmjs.com/package/figlet).

La première chose à faire est de choisir la bonne police. Allez sur [figlet playground](https://patorjk.com/software/taag/) et écrivez le texte que vous voulez pour votre salutation. Nous utiliserons "Terminal Portfolio" et cliquons sur "Test All". Il devrait afficher votre texte avec toutes les polices. Faites défiler la liste et choisissez la police que vous aimez.

J'ai choisi une police "slant" qui ressemble à ceci :

![Art ASCII Terminal Portfolio](https://www.freecodecamp.org/news/content/images/2024/04/Przechwycenie-obrazu-ekranu_2024-04-26_22-18-26.png align="left")

Vous pouvez copier ce texte et le mettre dans une chaîne, mais vous aurez des problèmes comme avec le backslash qui doit être échappé en utilisant des caractères de guillemet.

```lisp
const greetings = `  ______                    _             __   ____             __  ____      ___     
 /_  __/__  _________ ___  (_)___  ____ _/ /  / __ \\____  _____/ /_/ __/___  / (_)___ 
  / / / _ \\/ ___/ __ \`__ \\/ / __ \\/ __ \`/ /  / /_/ / __ \\/ ___/ __/ /_/ __ \\/ / / __ \\
 / / /  __/ /  / / / / / / / / / / /_/ / /  / ____/ /_/ / /  / /_/ __/ /_/ / / / /_/ /
/_/  \\___/_/  /_/ /_/ /_/_/_/ /_/\\__,_/_/  /_/    \\____/_/   \\__/_/  \\____/_/_/\\____/`

const term = $('body').terminal(commands, {
    greetings
});
```

**NOTE** : Le deuxième argument de jQuery Terminal est un objet avec des options – nous avons utilisé une seule option `greetings`.

Cela ne semble pas bon et c'est difficile à modifier. De plus, si vous créez la salutation en codant en dur une chaîne, elle peut se déformer sur les petits écrans. C'est pourquoi nous utiliserons la bibliothèque figlet en JavaScript.

Tout d'abord, nous devons inclure la bibliothèque figlet dans HTML :

```html
<script src="https://cdn.jsdelivr.net/npm/figlet/lib/figlet.js"></script>
```

Pour initialiser la bibliothèque en JavaScript, nous devons charger les polices :

```javascript
const font = 'Slant';

figlet.defaults({ fontPath: 'https://unpkg.com/figlet/fonts/' });
figlet.preloadFonts([font], ready);
```

Ce code chargera la police `'Slant'` et appellera la fonction `ready` lorsque la police sera chargée.

Nous devons donc écrire cette fonction :

```javascript
function ready() {

}
```

Maintenant, nous pouvons faire deux choses, nous pouvons mettre l'initialisation de jQuery Terminal à l'intérieur de cette fonction :

```javascript
let term;

function ready() {
   term =  $('body').terminal(commands, {
      greetings
   });
}
```

Avec cela, nous pouvons utiliser l'option `greeting`. Mais nous pouvons également utiliser la méthode `echo` pour rendre la salutation, et lors de l'initialisation du terminal, nous mettrons `null` ou `false` comme `greetings` pour désactiver celui par défaut :

```javascript
const term = $('body').terminal(commands, {
    greetings: false
});

function ready() {
   term.echo(greetings);
}
```

Cela fonctionnera mieux car la bibliothèque initialisera le terminal immédiatement et n'aura pas besoin d'attendre le chargement des polices.

Notez que nous devons toujours définir les salutations en utilisant figlet. Pour cela, nous pouvons écrire cette fonction :

```javascript
function render(text) {
    const cols = term.cols();
    return figlet.textSync(text, {
        font: font,
        width: cols,
        whitespaceBreak: true
    });
}
```

Cette fonction utilise la méthode `figlet::textSync()` pour retourner une chaîne et utilise `terminal::cols()`, pour obtenir le nombre de caractères par ligne. Avec cela, nous pouvons rendre notre texte réactif.

Cette fonction peut être utilisée à l'intérieur de `ready`.

```javascript
function ready() {
   term.echo(render('Terminal Portfolio'));
}
```

Cela créera une chaîne et la passera à la méthode `echo`. Mais cela sera la même chose qu'avec :

```javascript
term.echo(greeting);
```

Et nos salutations codées en dur. Donc si vous redimensionnez le terminal, les salutations peuvent encore se déformer. Pour rendre le texte réactif, vous devez `echo` une fonction. Cette fonction sera appelée à chaque nouveau rendu du terminal, ce qui se produira lorsque vous redimensionnerez la page.

Nous pouvons utiliser la fonction fléchée pour cela :

```javascript
function ready() {
   term.echo(() => render('Terminal Portfolio'));
}
```

Si vous voulez ajouter du texte sous l'art ASCII, vous pouvez le faire en concaténant la chaîne après le rendu :

```javascript
function ready() {
   term.echo(() => {
     const ascii = render('Terminal Portfolio');
     return `${ascii}\nBienvenue dans mon Portfolio Terminal\n`;
   });
}
```

**NOTE** : Si vous exécutez ce code, vous remarquerez qu'il y a une ligne vide après l'art ASCII. Cela est dû au fait que la bibliothèque figlet ajoute des espaces après le texte.

Pour vous en débarrasser, vous pouvez utiliser `string::replace()` avec une expression régulière qui supprimera tous les espaces et les nouvelles lignes de la fin.

Nous ne pouvons pas utiliser `string::trim()`, car nous ne voulons pas supprimer les lignes de début :

```javascript
function render(text) {
    const cols = term.cols();
    return trim(figlet.textSync(text, {
        font: font,
        width: cols,
        whitespaceBreak: true
    }));
}

function trim(str) {
    return str.replace(/[\n\s]+$/, '');
}
```

Vous pouvez également mettre en pause le terminal lorsqu'il charge les polices :

```javascript
const term = $('body').terminal(commands, {
    greetings: false
});

term.pause();

function ready() {
   term.echo(() => render('Terminal Portfolio')).resume();
}
```

Vous pouvez enchaîner les méthodes du terminal, de la même manière qu'avec jQuery.

### Espacements de ligne

Si la police que vous choisissez crée des espaces entre les lignes, comme dans cette image avec la police ANSI Shadow :

![Image : Art ASCII avec des espaces entre les lignes](https://www.freecodecamp.org/news/content/images/2024/05/Przechwycenie-obrazu-ekranu_2024-05-08_14-06-41.png align="left")

Vous pouvez supprimer les espaces en ajoutant l'option `ansi` définie sur `true`. L'option a été ajoutée spécifiquement pour corriger un problème d'affichage de l'[ANSI Art](https://en.wikipedia.org/wiki/ANSI_art).

```javascript
term.echo(() => render('Terminal Portfolio'), { ansi: true });
```

L'art ASCII ci-dessus ressemblera à ceci :

![Image : Art ASCII avec les espaces supprimés](https://www.freecodecamp.org/news/content/images/2024/05/Przechwycenie-obrazu-ekranu_2024-05-08_14-57-16.png align="left")

## Comment ajouter des couleurs à l'art ASCII

Vous pouvez pimenter votre art ASCII en utilisant une bibliothèque appelée lolcat. lolcat est une commande Linux qui peut styliser le texte dans le terminal avec des couleurs arc-en-ciel. Il existe également une bibliothèque appelée [isomorphic-lolcat](https://www.npmjs.com/package/isomorphic-lolcat), que vous pouvez utiliser en JavaScript pour rendre votre art ASCII en couleurs arc-en-ciel.

### Formatage du terminal

Pour utiliser la bibliothèque lolcat, vous devez d'abord savoir comment changer les couleurs du terminal.

Vous pouvez le faire en utilisant un formatage de bas niveau qui ressemble à ceci :

```lisp
[[b;red;]some text]
```

L'ensemble du texte est enveloppé dans des crochets et le formatage du texte est dans des crochets supplémentaires, où chaque argument est séparé par un point-virgule. Pour en savoir plus sur la syntaxe, vous pouvez lire l'article Wiki : [Formatage et coloration syntaxique](https://github.com/jcubic/jquery.terminal/wiki/Formatting-and-Syntax-Highlighting).

Ici, nous n'utiliserons qu'un changement de couleur de base. Au lieu de rouge, vous pouvez utiliser des noms de couleurs CSS, des couleurs hexadécimales ou `rgb()`.

### Comment utiliser la bibliothèque Lolcat

Pour utiliser la bibliothèque, nous devons d'abord l'inclure dans HTML :

```html
<script src="https://cdn.jsdelivr.net/npm/isomorphic-lolcat"></script>
```

Pour formater la chaîne avec des couleurs, nous pouvons utiliser cette fonction :

```javascript
function rainbow(string) {
    return lolcat.rainbow(function(char, color) {
        char = $.terminal.escape_brackets(char);
        return `[[;${hex(color)};]${char}]`;
    }, string).join('\n');
}

function hex(color) {
    return '#' + [color.red, color.green, color.blue].map(n => {
        return n.toString(16).padStart(2, '0');
    }).join('');
}
```

Le `lolcat.rainbow` appellera une fonction pour chaque caractère de la chaîne d'entrée, et passera la couleur comme un objet avec des valeurs RGB et le caractère.

### Salutations en art ASCII arc-en-ciel

Pour utiliser ce code, vous devez envelopper l'appel à render avec `rainbow` :

```javascript
function ready() {
   term.echo(() => {
     const ascii = rainbow(render('Terminal Portfolio'));
     return `${ascii}\nBienvenue dans mon Portfolio Terminal\n`;
   }).resume();
}
```

Vous pouvez également utiliser deux appels à echo, puisque seul le message Figlet doit être exécuté à l'intérieur de la fonction :

```javascript
function ready() {
   term.echo(() => rainbow(render('Terminal Portfolio')))
       .echo('Bienvenue dans mon Portfolio Terminal\n').resume();
}
```

Vous remarquerez que lorsque vous redimensionnez la fenêtre, l'arc-en-ciel change aléatoirement. C'est le comportement par défaut de lolcat. Pour le changer, vous devez définir le [graine aléatoire](https://en.wikipedia.org/wiki/Random_seed).

```javascript
function rand(max) {
    return Math.floor(Math.random() * (max + 1));
}

function ready() {
   const seed = rand(256);
   term.echo(() => rainbow(render('Terminal Portfolio'), seed))
       .echo('Bienvenue dans mon Portfolio Terminal\n').resume();
}

function rainbow(string, seed) {
    return lolcat.rainbow(function(char, color) {
        char = $.terminal.escape_brackets(char);
        return `[[;${hex(color)};]${char}]`;
    }, string, seed).join('\n');
}
```

La fonction `rand` retourne un nombre pseudo-aléatoire de 0 à la valeur maximale. Ici, nous avons créé une valeur aléatoire de 0 à 256.

### Comment rendre le texte de salutation blanc

Comme nous l'avons montré précédemment, vous pouvez rendre le texte blanc avec le formatage du terminal. Vous pouvez utiliser :

* `[[;white;]Bienvenue dans mon Portfolio Terminal]`
    
* `[[;#fff;]Bienvenue dans mon Portfolio Terminal]`
    
* `[[;rgb(255,255,255);]Bienvenue dans mon Portfolio Terminal]`
    

De plus, si vous incluez un fichier supplémentaire de formatage XML, vous pouvez utiliser une syntaxe de type XML. Cela rend le formatage beaucoup plus facile.

```html
<script src="https://cdn.jsdelivr.net/npm/jquery.terminal/js/xml_formatting.js"></script>
```

Après avoir inclus le fichier ci-dessus dans HTML, vous pouvez utiliser les noms de couleurs CSS comme balises XML :

```xml
<white>Bienvenue dans mon Portfolio Terminal</white>
```

Le formatage XML prend en charge plus de balises comme les liens et les images. Voir [Extension XML Formatter](https://github.com/jcubic/jquery.terminal/wiki/Formatting-and-Syntax-Highlighting#extension-xml-formatter) pour plus d'informations.

**NOTE** : Le formateur XML est une fonction ajoutée à `$.terminal.defaults.formatters`, qui transforme le texte d'entrée de type XML en formatage de terminal. Vous pouvez ajouter la même chose à vos propres formateurs.

## Comment créer votre première commande

Après la salutation, nous pouvons écrire notre première commande. Elle sera utile et fonctionnera avec toutes les commandes que nous ajouterons plus tard.

```javascript
const commanns = {
    help() {

    }
};
```

Ce sera notre commande d'aide où nous ajouterons une liste de commandes disponibles pour notre portfolio de terminal. Nous utiliserons [Intl.ListFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat), qui crée une liste d'éléments avec et avant le dernier élément.

```javascript
const formatter = new Intl.ListFormat('en', {
  style: 'long',
  type: 'conjunction',
});
```

Pour créer une liste, nous devons utiliser `formatter.format()` et passer un tableau de commandes. Pour obtenir ce tableau, nous pouvons utiliser `Object.keys()` :

```javascript
const commands = {
    help() {
        term.echo(`Liste des commandes disponibles : ${help}`);
    }
};

const command_list = Object.keys(commands);
const help = formatter.format(command_list);
```

Lorsque vous tapez help, vous devriez voir :

```lisp
Liste des commandes disponibles : help
```

Vous devez également ajouter la commande `echo` :

```javascript
const commands = {
    help() {
        term.echo(`Liste des commandes disponibles : ${help}`);
    },
    echo(...args) {
        term.echo(args.join(' '));
    }
};
```

Maintenant, la commande help fonctionne :

```lisp
Liste des commandes disponibles : help et echo
```

Mais si vous essayez d'exécuter 'echo hello', vous obtiendrez une erreur :

```lisp
[Arity] Nombre incorrect d'arguments. La fonction 'echo' attend 0 arguments, mais en a reçu 1 !
```

Par défaut, jQuery Terminal vérifie le nombre d'arguments et le nombre de paramètres que la fonction accepte. Le problème est que l'opérateur `rest` rend tous les arguments optionnels et la propriété de longueur de la fonction est 0. Pour corriger le problème, nous devons désactiver la vérification `Arity` avec une option :

```javascript
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false
});
```

Maintenant, les commandes echo devraient fonctionner.

## Commandes par défaut

Par défaut, jQuery Terminal a deux commandes par défaut :

* `clear` : cette commande efface tout sur le terminal.
    
* `exit` : cette commande quitte les interpréteurs imbriqués.
    

Vous pouvez les désactiver en passant le nom à l'option et en le définissant sur false. Puisque nous n'utiliserons pas d'interpréteurs imbriqués, nous pouvons désactiver `exit` :

```javascript
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false,
    exit: false
});
```

Mais `clear` peut être utile. Nous pouvons donc l'ajouter à la liste des commandes :

```javascript
const command_list = ['clear'].concat(Object.keys(commands));
```

## Comment rendre les commandes d'aide exécutables

Nous pouvons améliorer l'UX en permettant de cliquer sur la commande et de l'exécuter comme si l'utilisateur l'avait tapée.

Nous aurons besoin de quelques choses pour cela. Tout d'abord, nous devons ajouter un formatage à chaque commande et ajouter un attribut de classe HTML. Nous pouvons également rendre la commande blanche pour qu'elle soit plus visible.

```javascript
const command_list = Object.keys(commands);
const formatted_list = command_list.map(cmd => {
    return `<white class="command">${cmd}</white>`;
});
const help = formatter.format(formatted_list);
```

Ensuite, nous devons ajouter une [affordance](https://en.wikipedia.org/wiki/Affordance). Pour indiquer que l'utilisateur peut cliquer sur la commande, nous devons changer le curseur en CSS :

```css
.command {
    cursor: pointer;
}
```

La dernière étape consiste à exécuter la commande lorsque l'utilisateur clique sur la commande. Nous devons ajouter un gestionnaire d'événements avec jQuery (dépendance de jQuery Terminal) ou nous pouvons utiliser l'[addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) natif du navigateur. Ici, nous utilisons jQuery :

```javascript
term.on('click', '.command', function() {
   const command = $(this).text();
   term.exec(command);
});
```

`terminal::exec()` est un moyen d'exécuter une commande par programme, comme si l'utilisateur l'avait tapée et avait appuyé sur entrée.

Vous pouvez le tester en tapant `help` et en cliquant à nouveau sur `help`.

Cliquer sur `echo` imprimera une ligne vide. Nous pouvons corriger cela en vérifiant si le tableau des arguments n'est pas vide, avant d'exécuter `terminal::echo()` :

```javascript
const commands = {
    echo(...args) {
        if (args.length > 0) {
            term.echo(args.join(' '));
        }
    }
};
```

Maintenant, cliquer sur `echo` ne montrera que la commande exécutée.

**NOTE** : Si pour une raison quelconque vous ne voulez pas afficher l'invite et la commande qui a été exécutée, vous pouvez silencier l'`exec` en passant `true` comme deuxième argument.

```javascript
term.exec('help', true);
```

## Coloration syntaxique

Comme nous l'avons discuté précédemment, nous pouvons utiliser une coloration syntaxique personnalisée de notre shell en poussant une fonction dans `$.terminal.defaults.formatters`. Nous pouvons également utiliser la fonction d'assistance `$.terminal.new_formatter`.

Rendons nos commandes blanches au fur et à mesure que nous les tapons. Le formateur peut être un tableau (de regex et de remplacement), ou une fonction. Nous avons un nombre fixe de commandes et nous voulons seulement rendre celles qui sont dans la liste en blanc. Nous pouvons faire cela en ajoutant une expression régulière :

```javascript
const any_command_re = new RegExp(`^\s*(${command_list.join('|')})`);
```

Cette expression régulière vérifiera si, au début de la chaîne, il y a un espace blanc optionnel et une des commandes. Pour l'instant, le regex ressemblera à ceci : `/^\s*(help|echo)/`. Voici comment créer un nouveau formateur :

```javascript
$.terminal.new_formatter([any_command_re, '<white>$1</white>']);
```

Si vous souhaitez rendre les arguments de commande dans des couleurs différentes, vous aurez besoin d'une fonction, où vous utiliserez [String::replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace).

```javascript
const re = new RegExp(`^\s*(${command_list.join('|')}) (.*)`);

$.terminal.new_formatter(function(string) {
    return string.replace(re, function(_, command, args) {
        return `<white>${command}</white> <aqua>${args}</aqua>`;
    });
});
```

Ce n'est qu'un exemple d'utilisation de `String::replace`. Si vous n'avez qu'un seul remplacement, vous pouvez utiliser un tableau. Ce sera la même chose :

```javascript
const re = new RegExp(`^\s*(${command_list.join('|')})(\s?.*)`);

$.terminal.new_formatter([re, function(_, command, args) {
    return `<white>${command}</white><aqua>${args}</aqua>`;
}]);
```

**NOTE** : Si vous ajoutez la classe `<white class="command">` au formateur, vous pourrez cliquer sur la commande tapée pour l'exécuter à nouveau.

## Complétion par tabulation

Une autre fonctionnalité que nous pouvons ajouter est de compléter la commande lorsque vous appuyez sur la touche de tabulation. C'est super facile – nous devons seulement ajouter l'option de complétion définie sur true :

```javascript
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false,
    exit: false,
    completion: true
});
```

Maintenant, lorsque vous tapez `h` et appuyez sur tabulation, il complétera la commande `help` pour vous.

## Comment ajouter des commandes shell

Maintenant, nous pouvons ajouter les commandes les plus importantes qui nous permettent de naviguer dans le portfolio. Nous implémenterons des répertoires comme point d'entrée principal afin que l'utilisateur doive taper la commande `ls` pour voir une liste de choses, `cd` dans ce répertoire, et `ls` à nouveau pour voir le contenu.

```javascript
const directories = {
    education: [
        '',
        '<white>education</white>',

        '* <a href="https://en.wikipedia.org/wiki/Kielce_University_of_Technology">Kielce University of Technology</a> <yellow>"Computer Science"</yellow> 2002-2007 / 2011-2014',
        '* <a href="https://pl.wikipedia.org/wiki/Szko%C5%82a_policealna">Post-secondary</a> Electronic School <yellow>"Computer Systems"</yellow> 2000-2002',
        '* Electronic <a href="https://en.wikipedia.org/wiki/Technikum_(Polish_education)">Technikum</a> with major <yellow>"RTV"</yellow> 1995-2000',
        ''
    ],
    projects: [
        '',
        '<white>Open Source projects</white>',
        [
            ['jQuery Terminal',
             'https://terminal.jcubic.pl',
             'library that adds terminal interface to websites'
            ],
            ['LIPS Scheme',
             'https://lips.js.org',
             'Scheme implementation in JavaScript'
            ],
            ['Sysend.js',
             'https://jcu.bi/sysend',
             'Communication between open tabs'
            ],
            ['Wayne',
             'https://jcu.bi/wayne',
             'Pure in browser HTTP requests'
            ],
        ].map(([name, url, description = '']) => {
            return `* <a href="${url}">${name}</a> &mdash; <white>${description}</white>`;
        }),
        ''
    ].flat(),
    skills: [
        '',
        '<white>languages</white>',

        [
            'JavaScript',
            'TypeScript',
            'Python',
            'SQL',
            'PHP',
            'Bash'
        ].map(lang => `* <yellow>${lang}</yellow>`),
        '',
        '<white>libraries</white>',
        [
            'React.js',
            'Redux',
            'Jest',
        ].map(lib => `* <green>${lib}</green>`),
        '',
        '<white>tools</white>',
        [
            'Docker',
            'git',
            'GNU/Linux'
        ].map(lib => `* <blue>${lib}</blue>`),
        ''
    ].flat()
};
```

C'est notre structure de base. Vous pouvez l'éditer et ajouter vos propres informations. Tout d'abord, nous ajouterons une commande `cd` qui change de répertoire.

```javascript
const root = '~';
let cwd = root;

const commands = {
    cd(dir = null) {
        if (dir === null || (dir === '..' && cwd !== root)) {
            cwd = root;
        } else if (dir.startsWith('~/') && dirs.includes(dir.substring(2))) {
            cwd = dir;
        } else if (dir.startsWith('../') && cwd !== root &&
                   dirs.includes(dir.substring(3))) {
            cwd = root + '/' + dir.substring(3);
        } else if (dirs.includes(dir)) {
            cwd = root + '/' + dir;
        } else {
            this.error('Wrong directory');
        }
    }
};
```

Cela gérera tous les cas de changement de répertoire. Ensuite, nous devons ajouter une invite.

Pour voir dans quel répertoire nous nous trouvons, nous devons ajouter une invite `prompt` personnalisée. Nous pouvons créer une fonction comme option `prompt` :

```javascript
const user = 'guest';
const server = 'freecodecamp.org';

function prompt() {
    return `<green>${user}@${server}</green>:<blue>${cwd}</blue>$ `;
}
```

Et l'utiliser comme option :

```javascript
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false,
    completion: true,
    exit: false,
    prompt
});
```

La couleur verte ne semble pas très bonne, nous pouvons donc utiliser une couleur d'Ubuntu pour rendre le terminal plus réaliste. Nous pouvons écraser les balises de couleur XML par défaut comme ceci :

```javascript
$.terminal.xml_formatter.tags.green = () => {
    return `[[;#44D544;]`;
};
```

Ensuite, nous avons la commande `ls`.

```javascript
function print_home() {
     term.echo(dirs.map(dir => {
         return `<blue class="directory">${dir}</blue>`;
     }).join('\n'));
}

const commands = {
    ls(dir = null) {
        if (dir) {
            if (dir.match(/^~\/?$/)) {
                // ls ~ ou ls ~/
                print_home();
            } else if (dir.startsWith('~/')) {
                const path = dir.substring(2);
                const dirs = path.split('/');
                if (dirs.length > 1) {
                    this.error('Invalid directory');
                } else {
                    const dir = dirs[0];
                    this.echo(directories[dir].join('\n'));
                }
            } else if (cwd === root) {
                if (dir in directories) {
                    this.echo(directories[dir].join('\n'));
                } else {
                    this.error('Invalid directory');
                }
            } else if (dir === '..') {
                print_home();
            } else {
                this.error('Invalid directory');
            }
        } else if (cwd === root) {
            print_home();
        } else {
            const dir = cwd.substring(2);
            this.echo(directories[dir].join('\n'));
        }
    }
};
```

De manière similaire au vert que nous avions auparavant, la couleur bleue n'est pas si géniale. Nous pouvons donc utiliser à nouveau la couleur d'Ubuntu. Pour cela, nous devons utiliser les mêmes balises XML personnalisées pour la couleur bleue :

```javascript
$.terminal.xml_formatter.tags.blue = (attrs) => {
    return `[[;#55F;;${attrs.class}]`;
};
```

Nous avons ajouté la classe HTML pour une raison. Changeons de répertoire lorsque l'utilisateur clique sur le répertoire. Tout comme nous l'avons fait avec les commandes, nous pouvons invoquer la commande `cd` de la même manière qu'un utilisateur la taperait.

```javascript
term.on('click', '.directory', function() {
    const dir = $(this).text();
    term.exec(`cd ~/${dir}`);
});
```

**NOTE** : si vous avez une commande longue et que vous voulez obtenir le texte de cette commande, il est préférable d'utiliser : `$(this).data('text')`. Lorsque le formatage unique est enveloppé (lorsque le texte est plus long que la largeur du terminal), le `.text()` n'aura plus le texte complet, mais le texte complet est toujours dans l'attribut HTML `data-text`.

Nous devons également mettre à jour notre CSS pour changer le curseur :

```css
.command, .directory {
    cursor: pointer;
}
```

## Comment améliorer la complétion

Notre complétion n'est pas parfaite car elle ne complète que les commandes. Si vous souhaitez avoir une complétion qui gère également les répertoires, vous devez utiliser une fonction :

```javascript
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false,
    completion(string) {
        // dans chaque fonction, nous pouvons utiliser `this` pour référencer l'objet term
        const cmd = this.get_command();
        // nous traitons la commande pour extraire le nom de la commande
        // et le reste de la commande (les arguments comme une seule chaîne)
        const { name, rest } = $.terminal.parse_command(cmd);
        if (['cd', 'ls'].includes(name)) {
            if (rest.startsWith('~/')) {
                return dirs.map(dir => `~/${dir}`);
            }
            if (rest.startsWith('../') && cwd != root) {
                return dirs.map(dir => `../${dir}`);
            }
            if (cwd === root) {
                return dirs;
            }
        }
        return Object.keys(commands);
    },
    prompt
});
```

**NOTE** : L'argument de chaîne a été laissé comme documentation. Il peut être utilisé si vous voulez compléter un seul mot.

## Commande d'animation de frappe

Une autre commande que nous ajouterons est une blague animée. Nous imprimerons des blagues aléatoires en utilisant une API qui ressemble à l'utilisateur en train de taper.

Nous utiliserons l'[API Joke](https://jokeapi.dev/) à cette fin.

L'API retourne du JSON avec deux types de réponses : `twopart` et `single`. Voici le code qui imprime le texte sur le terminal :

```javascript
// nous utilisons des blagues de programmation pour qu'elles correspondent mieux
// portfolio de développeur
const url = 'https://v2.jokeapi.dev/joke/Programming';
const commands = {
    async joke() {
        const res = await fetch(url);
        const data = await res.json();
        if (data.type == 'twopart') {
            // comme dit précédemment dans chaque fonction, passée directement
            // au terminal, vous pouvez utiliser l'objet `this`
            // pour référencer l'instance du terminal
            this.echo(`Q: ${data.setup}`);
            this.echo(`A: ${data.delivery}`);
        } else if (data.type === 'single') {
            this.echo(data.joke);
        }
    },
}
```

Pour ajouter une animation de frappe, vous devez ajouter une option à la méthode `echo` :

```javascript
this.echo(data.joke, { delay: 50, typing: true });
```

Il y a un piège : si vous avez une séquence d'animations de frappe, vous devez attendre que la précédente se termine (l'echo retournera une promesse lors de l'animation). Lors de la création d'une telle animation, vous pouvez envelopper votre code avec la méthode `animation` :

```javascript
// nous utilisons des blagues de programmation pour qu'elles correspondent mieux
// portfolio de développeur
const url = 'https://v2.jokeapi.dev/joke/Programming';
const commands = {
    async joke() {
        const res = await fetch(url);
        const data = await res.json();
        if (data.type == 'twopart') {
            // cette méthode permet de créer une séquence d'animations
            this.animation(async () => {
                // comme dit précédemment dans chaque fonction, passée
                // directement au terminal, vous pouvez utiliser l'objet `this`
                // pour référencer l'instance du terminal
                // et puisque nous utilisons une fonction fléchée, nous référençons
                // cela depuis la fonction/la commande de blague
                await this.echo(`Q: ${data.setup}`, {
                    delay: 50,
                    typing: true
                });
                await this.echo(`A: ${data.delivery}`, {
                    delay: 50,
                    typing: true
                });
            });
        } else if (data.type === 'single') {
            this.echo(data.joke, {
                delay: 50,
                typing: true
            });
        }
    }
};
```

Vous pouvez lire plus sur l'animation de frappe dans cet article : [Typing Animation](https://github.com/jcubic/jquery.terminal/wiki/Typing-Animation)[.](https://github.com/jcubic/jquery.terminal/wiki/Typing-Animation#sequence-of-animations)

## Commande de crédits

La dernière commande que nous ajouterons est une commande de crédits où nous listerons les bibliothèques JavaScript que nous avons utilisées :

```javascript
const commands = {
    credits() {
        return [
            '',
            '<white>Used libraries:</white>',
            '* <a href="https://terminal.jcubic.pl">jQuery Terminal</a>',
            '* <a href="https://github.com/patorjk/figlet.js/">Figlet.js</a>',
            '* <a href="https://github.com/jcubic/isomorphic-lolcat">Isomorphic Lolcat</a>',
            '* <a href="https://jokeapi.dev/">Joke API</a>',
            ''
        ].join('\n');
    }
};
```

C'est un exemple d'une autre façon d'imprimer quelque chose sur le terminal – si vous retournez quelque chose d'une fonction, il sera imprimé. Vous pouvez également retourner une [Promise](https://www.freecodecamp.org/news/javascript-promises-explained/), donc vous pouvez envoyer une requête [AJAX](https://en.wikipedia.org/wiki/Ajax_\(programming\)) au serveur et imprimer les résultats.

## Commandes préremplies

Vous pouvez faciliter la tâche des utilisateurs pour savoir quoi faire avec le terminal, surtout s'ils ne sont pas très familiers avec Unix. Vous pouvez le faire en exécutant des commandes d'exemple :

```javascript
term.exec(command)
```

Vous pouvez également utiliser l'animation avec `exec` :

```javascript
term.exec(command, { typing: true, delay: 50 });
```

## Partage de lien vers une session de terminal

Une autre chose cool que je vais vous montrer est l'enregistrement des commandes dans l'URL. Vous pouvez créer une session de terminal complète et la sauvegarder dans un [hash d'URL](https://developer.mozilla.org/en-US/docs/Web/API/URL/hash). Pour commencer à enregistrer une session, vous devez exécuter ce qui suit :

```javascript
term.history_state(true);
```

Lorsque vous exécutez la commande `echo x`, elle devrait créer un hash d'URL qui ressemble à ceci : `#[[0,1,"echo%20x"]]`.

Pour arrêter l'enregistrement, vous pouvez utiliser :

```javascript
term.history_state(false);
```

Vous pouvez écrire cela dans une commande `record start | stop`, afin qu'il soit plus facile d'enregistrer des sessions.

La dernière chose à faire pour restaurer la session est d'utiliser l'option `execHash: true`.

```javascript
const term = $('body').terminal(commands, {
    /* reste des options */
    execHash: true
});
```

Lorsque vous faites cela et que vous actualisez la page, tout en ayant le hash d'URL avec la session, elle devrait rejouer la session et vous devriez voir la même sortie que lorsque vous l'avez enregistrée.

Si vous voulez que l'`exec` soit animé, vous pouvez utiliser cette option :

```javascript
const term = $('body').terminal(commands, {
    /* reste des options */
    execHash: true,
    execAnimation: true
});
```

Pour partager le lien, il est préférable d'utiliser un raccourcisseur d'URL comme [**TinyURL**](https://tinyurl.com/)**.** Assurez-vous de tester l'URL raccourcie pour voir si elle fonctionne.

## Comment ajouter des exécutables au répertoire personnel

Une autre chose que vous pouvez faire pour améliorer le portfolio est d'aider votre visiteur à apprendre quelles commandes il peut utiliser, en introduisant des exécutables lors de l'exécution de ls. Ils ressembleront à des binaires sur le système Linux.

```javascript
// pas toutes les commandes doivent être des binaires
// nous avons choisi ces trois qui fonctionnent plus comme de vrais programmes
const files = [
    'joke',
    'credits',
    'record'
];

function print_home() {
     term.echo(dirs.map(dir => {
         return `<blue class="directory">${dir}</blue>`;
     }).join('\n'));
     term.echo(files.map(file => {
         return `<green class="command">${file}</green>`;
     }).join('\n'));
}
```

Avec cela, vous pourrez cliquer sur la commande et l'exécuter. Ainsi, vos visiteurs sauront qu'ils peuvent exécuter la commande `joke` sans avoir besoin de taper la commande `help`. Pour que cela fonctionne, nous avons besoin d'un dernier changement, ajouter une classe à la balise XML verte :

```javascript
$.terminal.xml_formatter.tags.green = (attrs) => {
    return `[[;#44D544;;${attrs.class}]`;
};
```

## Démonstration de portfolio de terminal fonctionnel

Voici une démonstration entièrement fonctionnelle de notre [site web de portfolio de terminal interactif](https://codepen.io/jcubic/full/ZEZPWRY).

## Et ensuite ?

Vous pouvez ajouter beaucoup de commandes à ce portfolio. La seule limitation est votre imagination.

Vous pouvez consulter ces exemples pour vous inspirer :

* Collection CodePen avec [Démos de jQuery Terminal](https://codepen.io/collection/LPjoaW).
    
* [Démo CodePen de terminal rétro (vintage)](https://codepen.io/jcubic/pen/BwBYOZ).
    
* [Page d'exemples de jQuery Terminal](https://terminal.jcubic.pl/examples.php).
    
* [Page d'erreur 404 du terminal](https://terminal.jcubic.pl/404).
    
* [Faux terminal GNU/Linux](https://fake.terminal.jcubic.pl/).
    

Si vous avez une idée qui n'est pas listée ici, vous pouvez demander sur [StackOverflow avec le tag jquery-terminal](https://stackoverflow.com/questions/tagged/jquery-terminal). Si vous avez quelque chose de plus chronophage, vous pouvez également demander un [support payant](https://support.jcubic.pl/).

## Partagez ce que vous avez créé

Si vous créez un portfolio de terminal cool, vous pouvez [le partager et me taguer sur Twitter](http://twitter.com/jcubic). J'adorerais y jeter un coup d'œil. Surtout si vous créez quelque chose de plus que ce qui est inclus dans le tutoriel. Vous pouvez également partager sur un [chat de terminal sur mon site web](https://jcu.bi/chat) (c'est un portfolio de terminal similaire, mais avec un chat).