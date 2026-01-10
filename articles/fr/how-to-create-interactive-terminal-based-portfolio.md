---
title: Comment créer un site web de portfolio interactif basé sur un terminal
date: 2024-08-19T12:31:24.305Z
author: Jakub T. Jankiewicz
authorURL: https://www.freecodecamp.org/news/author/jcubic/
originalURL: https://www.freecodecamp.org/news/how-to-create-interactive-terminal-based-portfolio/
posteditor: ""
proofreader: ""
---

Dans cet article, vous apprendrez comment créer un portfolio et un CV interactifs basés sur un terminal en JavaScript. Nous utiliserons la [bibliothèque jQuery Terminal][1] (ainsi que quelques autres outils) pour créer un site web qui ressemble à un véritable terminal.

<!-- more -->

Cet article présentera une utilisation plus avancée de la bibliothèque jQuery Terminal. Si vous souhaitez quelque chose de plus basique, vous pouvez consulter cet article : [Comment créer un site web de type terminal interactif avec JavaScript][2], qui est écrit pour des programmeurs de niveau débutant. Vous pouvez également le lire avant de commencer celui-ci.

## Table des matières

-   [Table des matières][3]
-   [Qu'est-ce que le terminal ?][4]
-   [Qu'est-ce que jQuery Terminal ?][5]
-   [Fichier HTML de base][6]
-   [Comment initialiser le terminal][7]
-   [Salutations][8]
    -   [Espaces entre les lignes][9]
    -   [Comment ajouter des couleurs à l'art ASCII][10]
    -   [Formatage du terminal][11]
    -   [Comment utiliser la bibliothèque lolcat][12]
    -   [Salutations en art ASCII arc-en-ciel][13]
    -   [Comment mettre le texte de salutation en blanc][14]
-   [Comment créer votre première commande][15]
-   [Commandes par défaut][16]
-   [Comment rendre les commandes d'aide exécutables][17]
-   [Coloration syntaxique][18]
-   [Complétion par tabulation][19]
-   [Comment ajouter des commandes shell][20]
-   [Comment améliorer la complétion][21]
-   [Commande d'animation de frappe][22]
-   [Commande de crédits][23]
-   [Commandes pré-remplies][24]
-   [Et ensuite ?][25]

## Qu'est-ce que le terminal ?

Les terminaux ont une longue histoire. Tout a commencé comme une amélioration des [cartes perforées][26]. À l'époque, les ordinateurs utilisaient des téléscripteurs (teletypes), qui n'étaient qu'un clavier et une imprimante. Vous tapiez sur le clavier, les frappes étaient envoyées à l'ordinateur (généralement un mainframe) et la sortie était imprimée sur papier.

Plus tard, les téléscripteurs ont été remplacés par des terminaux. Un terminal était comme l'ordinateur passif que nous voyons aujourd'hui. C'était un moniteur CRT avec un clavier. Ainsi, au lieu d'obtenir la sortie sur l'imprimante, elle s'affichait sur le moniteur.

Aujourd'hui, nous utilisons toujours ce type d'interface (ligne de commande) pour communiquer avec les ordinateurs.

Ce sont des émulateurs de terminal et ils constituent une partie importante des systèmes Unix, comme GNU/Linux ou MacOS. Sur Windows, vous avez PowerShell ou le fichier cmd.exe qui vous permet de taper des commandes et d'obtenir des réponses sous forme de texte. Vous pouvez également installer un système GNU/Linux sur Windows via WSL. Les interfaces CLI sont principalement utilisées par les utilisateurs avancés, les développeurs et les administrateurs système.

Si vous débutez avec la ligne de commande, vous pouvez lire cet article : [Ligne de commande pour les débutants – Comment utiliser le terminal comme un pro \[Guide complet\]][27].

## Qu'est-ce que jQuery Terminal ?

jQuery Terminal est une bibliothèque JavaScript. C'est un plugin pour la [bibliothèque jQuery][28]. jQuery Terminal ressemble davantage à un framework qui a jQuery comme dépendance. Nous utiliserons principalement du JavaScript et très peu de jQuery dans cet article.

Créons notre portfolio basé sur un terminal en utilisant jQuery Terminal.

## Fichier HTML de base

La première chose à faire est d'inclure jQuery et la bibliothèque jQuery Terminal.

Voici un fichier HTML de base :

```
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

## Comment initialiser le terminal

Pour créer un terminal de base, vous devez insérer ce code :

```
const commands = {};

const term = $('body').terminal(commands);
```

La chaîne `'body'` indique le sélecteur CSS où le terminal doit être créé. Ici, nous utilisons `'body'` pour que le terminal soit le seul élément de la page. Mais il n'est pas nécessaire qu'il soit en plein écran. Vous pouvez créer un site web où le terminal n'est qu'une partie de la page, par exemple dans une fenêtre qui ressemble à une partie du système d'exploitation.

Le premier argument de la méthode terminal est appelé un interpréteur. C'est un moyen d'ajouter vos commandes. Un objet est la manière la plus simple de les créer. Consultez [création de l'interpréteur][29] pour en savoir plus.

Si la police du terminal est trop petite, vous pouvez l'agrandir un peu avec des propriétés personnalisées CSS (également appelées variables CSS) :

```
:root {
    --size: 1.2;
}
```

## Salutations

La première chose que nous devons faire est de supprimer le message de salutation par défaut et de le remplacer par un bel [art ASCII][30] personnalisé. Nous utiliserons la [bibliothèque Figlet][31] écrite en JavaScript.

Il existe plusieurs bibliothèques figlet sur npm. Nous utiliserons le package nommé [figlet][32].

La première chose à faire est de choisir la bonne police. Allez sur le [figlet playground][33] et écrivez le texte que vous voulez pour votre salutation. Nous utiliserons "Terminal Portfolio" et cliquerons sur "Test All". Cela devrait afficher votre texte avec toutes les polices. Parcourez la liste et choisissez la police qui vous plaît.

Nous avons choisi la police "slant" qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/Przechwycenie-obrazu-ekranu_2024-04-26_22-18-26.png) _Art ASCII Terminal Portfolio_

Vous pouvez copier ce texte et le mettre dans une chaîne de caractères, mais vous rencontrerez des problèmes comme la nécessité d'échapper les barres obliques inverses (`\`) et les caractères de citation.

```
const greetings = `  ______                    _             __   ____             __  ____      ___     
 /_  __/__  _________ ___  (_)___  ____ _/ /  / __ \\____  _____/ /_/ __/___  / (_)___ 
  / / / _ \\/ ___/ __ \`__ \\/ / __ \\/ __ \`/ /  / /_/ / __ \\/ ___/ __/ /_/ __ \\/ / / __ \\
 / / /  __/ /  / / / / / / / / / / /_/ / /  / ____/ /_/ / /  / /_/ __/ /_/ / / / /_/ /
/_/  \\___/_/  /_/ /_/ /_/_/_/ /_/\\__,_/_/  /_/    \\____/_/   \\__/_/  \\____/_/_/\\____/`

const term = $('body').terminal(commands, {
    greetings
});
```

**NOTE** : Le deuxième argument de jQuery Terminal est un objet d'options – nous avons utilisé une seule option `greetings`.

Cela ne rend pas très bien et c'est difficile à modifier. De plus, si vous créez la salutation en codant une chaîne en dur, elle peut être déformée sur les petits écrans. C'est pourquoi nous utiliserons la bibliothèque figlet en JavaScript.

Tout d'abord, nous devons inclure la bibliothèque figlet dans le HTML :

```
<script src="https://cdn.jsdelivr.net/npm/figlet/lib/figlet.js"></script>
```

Pour initialiser la bibliothèque en JavaScript, nous devons charger les polices :

```
const font = 'Slant';

figlet.defaults({ fontPath: 'https://unpkg.com/figlet/fonts/' });
figlet.preloadFonts([font], ready);
```

Ce code chargera la police `'Slant'` et appellera la fonction `ready` une fois la police chargée.

Nous devons donc écrire cette fonction :

```
function ready() {

}
```

Maintenant, nous pouvons faire deux choses : nous pouvons placer l'initialisation de jQuery Terminal à l'intérieur de cette fonction :

```
let term;

function ready() {
   term =  $('body').terminal(commands, {
      greetings
   });
}
```

Avec cela, nous pouvons utiliser l'option `greetings`, mais nous pouvons aussi utiliser la méthode `echo` pour afficher la salutation. Lors de l'initialisation du terminal, nous mettrons `null` ou `false` pour `greetings` afin de désactiver celui par défaut :

```
const term = $('body').terminal(commands, {
    greetings: false
});

function ready() {
   term.echo(greetings);
}
```

Cela fonctionnera mieux car la bibliothèque initialisera le terminal immédiatement sans avoir besoin d'attendre le chargement des polices.

Notez que nous devons toujours définir les salutations en utilisant figlet. Pour ce faire, nous pouvons écrire cette fonction :

```
function render(text) {
    const cols = term.cols();
    return figlet.textSync(text, {
        font: font,
        width: cols,
        whitespaceBreak: true
    });
}
```

Cette fonction utilise la méthode `figlet::textSync()` pour renvoyer une chaîne et utilise `terminal::cols()` pour obtenir le nombre de caractères par ligne. Grâce à cela, nous pouvons rendre notre texte responsive.

Cette fonction peut être utilisée à l'intérieur de `ready`.

```
function ready() {
   term.echo(render('Terminal Portfolio'));
}
```

Cela créera une chaîne et la passera à la méthode `echo`. Mais ce sera la même chose qu'avec :

```
term.echo(greeting);
```

Et nos salutations codées en dur. Ainsi, si vous redimensionnez le terminal, les salutations peuvent toujours être déformées. Pour rendre le texte responsive, vous devez passer une fonction à `echo`. Cette fonction sera appelée à chaque nouveau rendu du terminal, ce qui se produira lorsque vous redimensionnerez la page.

Nous pouvons utiliser une fonction fléchée pour cela :

```
function ready() {
   term.echo(() => render('Terminal Portfolio'));
}
```

Si vous souhaitez ajouter du texte sous l'art ASCII, vous pouvez le faire en concaténant la chaîne après le rendu :

```
function ready() {
   term.echo(() => {
     const ascii = render('Terminal Portfolio');
     return `${ascii}\nWelcome to my Terminal Portfolio\n`;
   });
}
```

**NOTE** : Si vous exécutez ce code, vous remarquerez qu'il y a une ligne vide après l'art ASCII. C'est parce que la bibliothèque figlet ajoute des espaces après le texte. Pour s'en débarrasser, vous pouvez utiliser `string::replace` avec une expression régulière qui supprimera tous les espaces et sauts de ligne à la fin.

Nous ne pouvons pas utiliser `string::trim()`, car nous ne voulons pas supprimer les lignes de tête :

```
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

D'autres choses que vous pouvez faire consistent à mettre le terminal en pause pendant le chargement des polices :

```
const term = $('body').terminal(commands, {
    greetings: false
});

term.pause();

function ready() {
   term.echo(() => render('Terminal Portfolio')).resume();
}
```

Tout comme avec jQuery, vous pouvez chaîner les méthodes du terminal.

## Espaces entre les lignes

Si la police que vous choisissez crée des espaces entre les lignes – comme sur cette image avec la police ANSI Shadow :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Przechwycenie-obrazu-ekranu_2024-05-08_14-06-41.png) _Art ASCII avec des espaces entre les lignes_

Vous pouvez supprimer ces espaces en ajoutant l'option `ansi` définie sur `true`. Cette option a été ajoutée spécifiquement pour corriger un problème d'affichage de l'[art ANSI][34].

```
term.echo(() => render('Terminal Portfolio'), { ansi: true });
```

L'art ASCII ci-dessus ressemblera alors à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Przechwycenie-obrazu-ekranu_2024-05-08_14-57-16.png) _Art ASCII avec les espaces supprimés_

## Comment ajouter des couleurs à l'art ASCII

Vous pouvez pimenter un grand art ASCII en utilisant une bibliothèque appelée lolcat. lolcat est une commande Linux qui peut styliser le texte dans le terminal avec des couleurs arc-en-ciel. Il existe une bibliothèque appelée [isomorphic-lolcat][35], que vous pouvez utiliser en JavaScript pour colorer votre art ASCII.

### Formatage du terminal

Pour utiliser la bibliothèque lolcat, vous devez d'abord savoir comment changer les couleurs du terminal.

Vous pouvez le faire en utilisant le formatage de bas niveau qui ressemble à ceci :

```
[[b;red;]some text]
```

L'ensemble du texte est enveloppé dans des crochets et le formatage du texte est dans des crochets supplémentaires, où chaque argument est séparé par un point-virgule. Pour en savoir plus sur la syntaxe, vous pouvez lire l'article du Wiki : [Formatage et coloration syntaxique][36].

Ici, nous n'utiliserons qu'un changement de couleur basique. Au lieu de `red`, vous pouvez utiliser des noms de couleurs CSS, des codes hexadécimaux ou `rgb()`.

### Comment utiliser la bibliothèque lolcat

Pour utiliser la bibliothèque, nous devons d'abord l'inclure dans le HTML :

```
<script src="https://cdn.jsdelivr.net/npm/isomorphic-lolcat"></script>
```

Pour formater la chaîne avec des couleurs, nous pouvons utiliser cette fonction :

```
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

`lolcat.rainbow` appellera une fonction pour chaque caractère de la chaîne d'entrée et passera la couleur sous forme d'objet avec des valeurs RGB ainsi que le caractère.

### Salutations en art ASCII arc-en-ciel

Pour utiliser ce code, vous devez envelopper l'appel à render avec rainbow :

```
function ready() {
   term.echo(() => {
     const ascii = rainbow(render('Terminal Portfolio'));
     return `${ascii}\nWelcome to my Terminal Portfolio\n`;
   }).resume();
}
```

Vous pouvez également utiliser deux appels à echo, puisque seul le message Figlet doit être exécuté à l'intérieur de la fonction :

```
function ready() {
   term.echo(() => rainbow(render('Terminal Portfolio')))
       .echo('Welcome to my Terminal Portfolio\n').resume();
}
```

Vous remarquerez que lorsque vous redimensionnez la fenêtre, l'arc-en-ciel change de manière aléatoire. C'est le comportement par défaut de lolcat. Pour le changer, vous devez définir la [graine aléatoire (random seed)][37].

```
function rand(max) {
    return Math.floor(Math.random() * (max + 1));
}

function ready() {
   const seed = rand(256);
   term.echo(() => rainbow(render('Terminal Portfolio'), seed))
       .echo('Welcome to my Terminal Portfolio\n').resume();
}

function rainbow(string, seed) {
    return lolcat.rainbow(function(char, color) {
        char = $.terminal.escape_brackets(char);
        return `[[;${hex(color)};]${char}]`;
    }, string, seed).join('\n');
}
```

La fonction `rand` renvoie un nombre pseudo-aléatoire de 0 à la valeur max. Ici, nous avons créé une valeur aléatoire de 0 à 256.

### Comment mettre le texte de salutation en blanc

Comme nous l'avons montré précédemment, vous pouvez mettre le texte en blanc avec le formatage du terminal.
Vous pouvez utiliser :

-   `[[;white;]Welcome to my Terminal Portfolio]`
-   `[[;#fff;]Welcome to my Terminal Portfolio]`
-   `[[;rgb(255,255,255);]Welcome to my Terminal Portfolio]`

De plus, si vous incluez le fichier supplémentaire de formatage XML, vous pouvez utiliser une syntaxe de type XML. Cela rend le formatage beaucoup plus facile.

```
<script src="https://cdn.jsdelivr.net/npm/jquery.terminal/js/xml_formatting.js"></script>
```

Après avoir inclus le fichier ci-dessus dans le HTML, vous pouvez utiliser les couleurs nommées CSS comme balises XML :

```
<white>Welcome to my Terminal Portfolio</white>
```

Le formatage XML prend en charge davantage de balises comme les liens et les images, voir [Extension XML Formatter][38] sur le Wiki.

**NOTE** : Le formateur XML est une fonction ajoutée à `$.terminal.defaults.formatters`, qui transforme le texte d'entrée de type XML en formatage terminal. Vous pouvez ajouter la même chose à vos propres formateurs.

## Comment créer votre première commande

Après la salutation, nous pouvons écrire notre première commande. Elle sera utile et fonctionnera avec toutes les commandes que nous ajouterons plus tard.

```
const commanns = {
    help() {

    }
};
```

Ce sera notre commande d'aide où nous ajouterons une liste de commandes disponibles pour notre portfolio terminal. Nous utiliserons [Intl.ListFormat][39], qui crée une liste d'éléments avec un "et" avant le dernier élément.

```
const formatter = new Intl.ListFormat('en', {
  style: 'long',
  type: 'conjunction',
});
```

Pour créer une liste, nous devons utiliser `formatter.format()` et passer un tableau de commandes.
Pour obtenir ce tableau, nous pouvons utiliser `Object.keys()` :

```
const commands = {
    help() {
        term.echo(`List of available commands: ${help}`);
    }
};

const command_list = Object.keys(commands);
const help = formatter.format(command_list);
```

Lorsque vous tapez help, vous devriez voir :

```
List of available commands: help
```

Vous devez également ajouter la commande `echo` :

```
const commands = {
    help() {
        term.echo(`List of available commands: ${help}`);
    },
    echo(...args) {
        term.echo(args.join(' '));
    }
};
```

Maintenant, la commande help fonctionne :

```
List of available commands: help and echo
```

Mais si vous essayez d'exécuter 'echo hello', vous obtiendrez une erreur :

```
[Arity] Wrong number of arguments. The function 'echo' expects 0 got 1!
```

Par défaut, jQuery Terminal vérifie le nombre d'arguments et le nombre de paramètres que la fonction accepte. Le problème est que l'opérateur `rest` rend tous les arguments optionnels et la propriété de longueur de la fonction est 0. Pour résoudre le problème, nous devons désactiver la vérification d'arité avec une option :

```
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false
});
```

Maintenant, les commandes echo devraient fonctionner.

## Commandes par défaut

Par défaut, jQuery Terminal possède deux commandes par défaut :

-   `clear` : cette commande efface tout dans le terminal.
-   `exit` : cette commande permet de sortir des interpréteurs imbriqués.

Vous pouvez les désactiver en passant le nom à l'option et en le définissant sur false. Comme nous n'utiliserons pas d'interpréteurs imbriqués, nous pouvons désactiver `exit` :

```
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false,
    exit: false
});
```

Mais `clear` peut être utile. Nous pouvons donc l'ajouter à la liste des commandes :

```
const command_list = ['clear'].concat(Object.keys(commands));
```

## Comment rendre les commandes d'aide exécutables

Nous pouvons améliorer l'expérience utilisateur (UX) en permettant de cliquer sur la commande pour l'exécuter, exactement comme si l'utilisateur l'avait tapée. Nous aurons besoin de quelques éléments. Tout d'abord, nous devons ajouter du formatage à chaque commande et ajouter un attribut de classe HTML. Nous pouvons également mettre la commande en blanc pour qu'elle soit plus visible.

```
const command_list = Object.keys(commands);
const formatted_list = command_list.map(cmd => {
    return `<white class="command">${cmd}</white>`;
});
const help = formatter.format(formatted_list);
```

L'étape suivante consiste à ajouter de l'[affordance][40]. Pour indiquer que l'utilisateur peut cliquer sur la commande, nous devons changer le curseur en CSS :

```
.command {
    cursor: pointer;
}
```

La dernière étape consiste à exécuter la commande lorsque l'utilisateur clique dessus. Nous devons ajouter un gestionnaire d'événements avec jQuery (dépendance de jQuery Terminal) ou nous pouvons utiliser le `addEventListener` natif du navigateur. Ici, nous utilisons jQuery :

```
term.on('click', '.command', function() {
   const command = $(this).text();
   term.exec(command);
});
```

`terminal::exec()` est un moyen d'exécuter une commande par programmation, exactement comme si l'utilisateur la tapait et appuyait sur entrée.

Vous pouvez le tester en tapant `help` et en cliquant à nouveau sur `help`.

Cliquer sur `echo` affichera une ligne vide. Nous pouvons corriger cela en vérifiant si le tableau d'arguments n'est pas vide avant d'exécuter `terminal::echo()` :

```
const commands = {
    echo(...args) {
        if (args.length > 0) {
            term.echo(args.join(' '));
        }
    }
};
```

Désormais, cliquer sur `echo` n'affichera que la commande exécutée.

**NOTE** : Si, pour une raison quelconque, vous ne souhaitez pas afficher l'invite et la commande qui a été exécutée, vous pouvez rendre l'`exec` silencieux en passant `true` comme second argument.

```
term.exec('help', true);
```

## Coloration syntaxique

Comme nous l'avons vu précédemment, nous pouvons utiliser une coloration syntaxique personnalisée de notre shell en poussant une fonction dans `$.terminal.defaults.formatters`. Nous pouvons également utiliser la fonction utilitaire `$.terminal.new_formatter`.

Faisons en sorte que nos commandes deviennent blanches au fur et à mesure que nous les tapons. Le formateur peut être un tableau (de regex et de remplacement) ou une fonction. Nous avons un nombre fixe de commandes et nous voulons seulement mettre en blanc celles qui sont dans la liste. Nous pouvons le faire en ajoutant une expression régulière :

```
const any_command_re = new RegExp(`^\s*(${command_list.join('|')})`);
```

Cette expression régulière vérifiera si, au début de la chaîne, il y a un espace optionnel et l'une des commandes. Actuellement, la regex ressemblera à ceci : `/^\s*(help|echo)/`.

```
$.terminal.new_formatter([any_command_re, '<white>$1</white>']);
```

Si vous souhaitez mettre les arguments de commande dans des couleurs différentes, vous aurez besoin d'une fonction où vous utiliserez [String::replace][41].

```
const re = new RegExp(`^\s*(${command_list.join('|')}) (.*)`);

$.terminal.new_formatter(function(string) {
    return string.replace(re, function(_, command, args) {
        return `<white>${command}</white> <aqua>${args}</aqua>`;
    });
});
```

Ceci n'est qu'un exemple d'utilisation de `String::replace`. Si vous n'avez qu'un seul remplacement, vous pouvez utiliser un tableau. Ce sera la même chose :

```
const re = new RegExp(`^\s*(${command_list.join('|')})(\s?.*)`);

$.terminal.new_formatter([re, function(_, command, args) {
    return `<white>${command}</white><aqua>${args}</aqua>`;
}]);
```

**NOTE** : Si vous ajoutez la classe `<white class="command">` au formateur, vous pourrez cliquer sur la commande tapée pour l'exécuter à nouveau.

## Complétion par tabulation

Une autre fonctionnalité que nous pouvons ajouter est la complétion de la commande lorsque vous appuyez sur la touche tabulation. C'est super facile – il suffit d'ajouter l'option completion définie sur true :

```
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false,
    exit: false,
    completion: true
});
```

Désormais, lorsque vous tapez `h` et appuyez sur tabulation, il complétera la commande `help` pour vous.

## Comment ajouter des commandes shell

Nous pouvons maintenant ajouter les commandes les plus importantes qui nous permettent de naviguer dans le portfolio. Nous allons implémenter des répertoires comme point d'entrée principal afin que l'utilisateur doive taper la commande `ls` pour voir la liste des éléments, `cd` pour entrer dans ce répertoire, et encore `ls` pour voir le contenu.

```
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

C'est notre structure de base. Vous pouvez la modifier et y mettre vos informations. Tout d'abord, nous allons ajouter une commande `cd` qui change de répertoire.

```
const root = '~';
let cwd = root;

const commands = {
    cd(dir = null) {
        if (dir === null || (dir === '..' && cwd !== root)) {
            cwd = root;
        } else if (dir.startsWith('~/') && dirs.includes(dir.substring(2))) {
            cwd = dir;
        } else if (dirs.includes(dir)) {
            cwd = root + '/' + dir;
        } else {
            this.error('Wrong directory');
        }
    }
};
```

Cela gérera tous les cas de changement de répertoire. L'étape suivante consiste à ajouter une invite (prompt).

Pour voir dans quel répertoire nous nous trouvons, nous devons ajouter un `prompt` personnalisé.
Nous pouvons créer une fonction :

```
const user = 'guest';
const server = 'freecodecamp.org';

function prompt() {
    return `<green>${user}@${server}</green>:<blue>${cwd}</blue>$ `;
}
```

Et l'utiliser comme option :

```
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false,
    completion: true,
    exit: false,
    prompt
});
```

La couleur verte ne rend pas très bien, nous pouvons utiliser la couleur d'Ubuntu pour rendre le terminal plus réaliste.

```
$.terminal.xml_formatter.tags.green = (attrs) => {
    return `[[;#44D544;]`;
};
```

Ensuite, la commande `ls`.

```
function print_dirs() {
     term.echo(dirs.map(dir => {
         return `<blue class="directory">${dir}</blue>`;
     }).join('\n'));
}

const commands = {
    ls(dir = null) {
        if (dir) {
            if (dir.match(/^~\/?$/)) {
                // ls ~ or ls ~/
                print_dirs();
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
                print_dirs();
            } else {
                this.error('Invalid directory');
            }
        } else if (cwd === root) {
            print_dirs();
        } else {
            const dir = cwd.substring(2);
            this.echo(directories[dir].join('\n'));
        }
    }
```

Tout comme pour le vert, la couleur bleue n'est pas géniale, nous pouvons donc utiliser la couleur d'Ubuntu. Pour ce faire, nous devons utiliser des balises XML personnalisées dans le formatage XML :

```
$.terminal.xml_formatter.tags.blue = (attrs) => {
    return `[[;#55F;;${attrs.class}]`;
};
```

Nous avons ajouté la classe HTML pour une raison. Changeons de répertoire lorsque l'utilisateur clique sur le répertoire. Tout comme nous l'avons fait avec les commandes, nous pouvons invoquer la commande `cd` de la même manière que si l'utilisateur la tapait :

```
term.on('click', '.directory', function() {
    const dir = $(this).text();
    term.exec(`cd ~/${dir}`);
});
```

Nous devons également mettre à jour notre CSS pour changer le curseur :

```
.command, .directory {
    cursor: pointer;
}
```

## Comment améliorer la complétion

Notre complétion n'est pas parfaite car elle ne complète que les commandes. Si vous souhaitez avoir une complétion qui gère également les répertoires, vous devez utiliser une fonction :

```
const term = $('body').terminal(commands, {
    greetings: false,
    checkArity: false,
    completion(string) {
        // dans chaque fonction, nous pouvons utiliser `this` pour référencer l'objet term
        const cmd = this.get_command();
        // nous traitons la commande pour extraire le nom de la commande
        // et le reste de la commande (les arguments sous forme d'une seule chaîne)
        const { name, rest } = $.terminal.parse_command(cmd);
        if (['cd', 'ls'].includes(name)) {
            if (rest.startsWith('~/')) {
                return dirs.map(dir => `~/${dir}`);
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

**NOTE** : L'argument string a été laissé pour la documentation. Il peut être utilisé si vous souhaitez seulement compléter un seul mot.

## Commande d'animation de frappe

Une autre commande que nous allons ajouter est une blague animée. Nous allons afficher des blagues aléatoires en utilisant une API avec un effet de frappe de l'utilisateur.

Nous utiliserons [Joke API][42].

L'API renvoie du JSON avec deux types de réponses : `twopart` et `single`. Voici le code qui affiche le texte sur le terminal :

```
// nous utilisons des blagues de programmation pour que cela corresponde mieux
// au portfolio de développeur
const url = 'https://v2.jokeapi.dev/joke/Programming';
const commands = {
    async joke() {
        const res = await fetch(url);
        const data = await res.json();
        if (data.type == 'twopart') {
            // comme dit précédemment, dans chaque fonction passée directement
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

Pour ajouter l'animation de frappe, vous devez ajouter une option à la méthode `echo` :

```
this.echo(data.joke, { delay: 50, typing: true });
```

Il y a une mise en garde : si vous avez une séquence d'animations de frappe, vous devez attendre que la précédente se termine (l'écho renverra une promesse lors de l'animation). Vous devez envelopper le code dans une fonction `async` et vous devez effacer l'invite pour ne pas avoir de flash entre les animations. Par défaut, l'invite est utilisée pour l'effet de frappe. Le code complet devrait donc ressembler à ceci :

```
// nous utilisons des blagues de programmation pour que cela corresponde mieux
// au portfolio de développeur
const url = 'https://v2.jokeapi.dev/joke/Programming';
const commands = {
    async joke() {
        const res = await fetch(url);
        const data = await res.json();
        (async () => {
            if (data.type == 'twopart') {
                // nous effaçons l'invite pour ne pas avoir de
                // clignotement entre les animations
                const prompt = this.get_prompt();
                this.set_prompt('');
                // comme dit précédemment, dans chaque fonction passée directement
                // au terminal, vous pouvez utiliser l'objet `this`
                // pour référencer l'instance du terminal
                await this.echo(`Q: ${data.setup}`, {
                    delay: 50,
                    typing: true
                });
                await this.echo(`A: ${data.delivery}`, {
                    delay: 50,
                    typing: true
                });
                // nous restaurons l'invite
                this.set_prompt(prompt);
            } else if (data.type === 'single') {
                await this.echo(data.joke, {
                    delay: 50,
                    typing: true
                });
            }
        })();
    },
}
```

Vous pouvez en savoir plus sur l'animation de frappe dans l'article du wiki : [Typing Animation][43][.][44]

## Commande de crédits

La dernière commande que nous ajouterons est une commande de crédits où nous listerons les bibliothèques JavaScript utilisées :

```
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

Ceci est un exemple d'une autre façon d'afficher quelque chose sur le terminal : si vous retournez quelque chose d'une fonction, cela sera affiché. Vous pouvez également retourner une [Promise][45], ce qui vous permet d'envoyer une requête [AJAX][46] au serveur et d'afficher les résultats.

## Commandes pré-remplies

Vous pouvez aider les utilisateurs à savoir quoi faire avec le terminal, surtout s'ils ne sont pas familiers avec Unix, en exécutant des commandes d'exemple :

```
term.exec(command)
```

Vous pouvez également utiliser l'animation avec `exec` :

```
term.exec(command, { typing: true, delay: 50 });
```

Voici une démo fonctionnelle de notre [site web de portfolio terminal interactif][47].

## Et ensuite ?

Vous pouvez ajouter de nombreuses commandes à ce portfolio. La seule limite est votre imagination.

Vous pouvez consulter ces exemples pour vous inspirer :

-   Collection CodePen avec des [Démos jQuery Terminal][48].
-   [Démo CodePen de terminal rétro (Vintage)][49].
-   [Page d'exemples jQuery Terminal][50].
-   [Page d'erreur 404 Terminal][51].
-   [Faux terminal GNU/Linux][52].

Si vous avez une idée qui n'est pas répertoriée ici, vous pouvez poser votre question sur [StackOverflow avec le tag jquery-terminal][53]. Si vous avez un projet plus chronophage, vous pouvez également demander un [support payant][54].

Si vous aimez cet article, vous pouvez [consulter mon site web][55] (qui possède un portfolio terminal similaire à celui-ci, ainsi qu'un chat), et me [suivre sur Twitter/X][56] et [LinkedIn][57].

[1]: https://terminal.jcubic.pl/
[2]: https://itnext.io/how-to-create-interactive-terminal-like-website-888bb0972288
[3]: #heading-table-des-matieres
[4]: #heading-qu-est-ce-que-le-terminal
[5]: #heading-qu-est-ce-que-jquery-terminal
[6]: #heading-fichier-html-de-base
[7]: #heading-comment-initialiser-le-terminal
[8]: #heading-salutations
[9]: #heading-espaces-entre-les-lignes
[10]: #heading-comment-ajouter-des-couleurs-a-l-art-ascii
[11]: #heading-formatage-du-terminal
[12]: #heading-comment-utiliser-la-bibliotheque-lolcat
[13]: #heading-salutations-en-art-ascii-arc-en-ciel
[14]: #heading-comment-mettre-le-texte-de-salutation-en-blanc
[15]: #heading-comment-creer-votre-premiere-commande
[16]: #heading-commandes-par-defaut
[17]: #heading-comment-rendre-les-commandes-d-aide-executables
[18]: #heading-coloration-syntaxique
[19]: #heading-completion-par-tabulation
[20]: #heading-comment-ajouter-des-commandes-shell
[21]: #heading-comment-ameliorer-la-completion
[22]: #heading-commande-d-animation-de-frappe
[23]: #heading-commande-de-credits
[24]: #heading-commandes-pre-remplies
[25]: #heading-et-ensuite
[26]: https://en.wikipedia.org/wiki/Punched_card
[27]: https://www.freecodecamp.org/news/command-line-for-beginners/
[28]: https://en.wikipedia.org/wiki/JQuery
[29]: https://github.com/jcubic/jquery.terminal/wiki/Getting-Started#creating-the-interpreter
[30]: https://en.wikipedia.org/wiki/ASCII_art
[31]: https://en.wikipedia.org/wiki/FIGlet
[32]: https://www.npmjs.com/package/figlet
[33]: https://patorjk.com/software/taag/
[34]: https://en.wikipedia.org/wiki/ANSI_art
[35]: https://www.npmjs.com/package/isomorphic-lolcat
[36]: https://github.com/jcubic/jquery.terminal/wiki/Formatting-and-Syntax-Highlighting
[37]: https://en.wikipedia.org/wiki/Random_seed
[38]: https://github.com/jcubic/jquery.terminal/wiki/Formatting-and-Syntax-Highlighting#extension-xml-formatter
[39]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat
[40]: https://en.wikipedia.org/wiki/Affordance
[41]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace
[42]: https://jokeapi.dev/
[43]: https://github.com/jcubic/jquery.terminal/wiki/Typing-Animation
[44]: https://github.com/jcubic/jquery.terminal/wiki/Typing-Animation#sequence-of-animations
[45]: https://www.freecodecamp.org/news/javascript-promises-explained/
[46]: https://en.wikipedia.org/wiki/Ajax_(programming)
[47]: https://codepen.io/jcubic/full/ZEZPWRY
[48]: https://codepen.io/collection/LPjoaW
[49]: https://codepen.io/jcubic/pen/BwBYOZ
[50]: https://terminal.jcubic.pl/examples.php
[51]: https://terminal.jcubic.pl/404
[52]: https://fake.terminal.jcubic.pl/
[53]: https://stackoverflow.com/questions/tagged/jquery-terminal
[54]: https://support.jcubic.pl/
[55]: https://jakub.jankiewicz.org/
[56]: https://twitter.com/jcubic
[57]: https://www.linkedin.com/in/jakubjankiewicz/