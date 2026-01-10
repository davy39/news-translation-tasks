---
title: Comment créer vos propres extraits de code personnalisés directement dans votre
  éditeur de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-14T18:46:57.000Z'
originalURL: https://freecodecamp.org/news/create-your-own-custom-code-snippets
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/20220114_210958_0000.png
tags:
- name: editor
  slug: editor
- name: json
  slug: json
- name: Productivity
  slug: productivity
- name: Snippet
  slug: snippet
- name: Visual Studio Code
  slug: vscode
- name: Web Development
  slug: web-development
seo_title: Comment créer vos propres extraits de code personnalisés directement dans
  votre éditeur de code
seo_desc: "By Timonwa Akintokun\nA code Snippet is a programming term that refers\
  \ to a small portion of re-usable source code, machine code, or text. \nSnippets\
  \ help programmers reduce the time it takes to type in repetitive information while\
  \ coding. Code Snippet..."
---

Par Timonwa Akintokun

Un extrait de code (ou snippet) est un terme de programmation qui fait référence à une petite portion de code source, de code machine ou de texte réutilisable. 

Les extraits de code aident les programmeurs à réduire le temps nécessaire pour taper des informations répétitives lors du codage. Les extraits de code sont une fonctionnalité présente dans la plupart des éditeurs de texte, des éditeurs de code et des IDE.

Dans ce tutoriel, nous allons apprendre à écrire nos propres extraits de code personnalisés.

## Prérequis
Pour ce tutoriel, je supposerai que vous pouvez écrire une quantité décente de code dans le langage pour lequel vous souhaitez créer un extrait de code.

Et avec cela confirmé...

![lady saying lets get started](https://www.freecodecamp.org/news/content/images/2022/01/gtL8MNgSES.gif)

## Pourquoi les extraits de code sont utiles

Quand j'ai commencé à apprendre à coder, le premier extrait de code que j'ai utilisé était **Ctrl + ! et entrer** pour obtenir un modèle de document HTML5. (Je doute que quelqu'un sache le écrire par cœur.) C'était cool et je me sentais comme un ninja du code. 

(PS : si vous ne voulez pas lire l'histoire et voulez plonger directement dans le tutoriel, alors [passez directement à la section](#creation-d-extraits-de-code-personnalises).)

En explorant davantage le codage, j'ai découvert des extensions VSCode qui rendaient le codage plus rapide – en particulier les extraits de code – et je me suis lancé dans une frénésie de téléchargements.

Tout allait bien jusqu'à ce que je commence à utiliser fréquemment des frameworks et des bibliothèques dans mes projets. Cela impliquait que je devais me souvenir de la manière de lier mes documents à leurs packages et d'utiliser des réinitialisations CSS personnalisées et des variables. 

De plus, j'oubliais toujours de lier mes feuilles de style à mes pages HTML, ce qui me faisait perdre un temps déraisonnable à essayer de comprendre pourquoi mes pages n'étaient pas stylisées correctement. (J'oublie encore de le faire de temps en temps.)

Cela m'a amené à réfléchir à la création de mes propres modèles HTML et CSS personnalisés, qui contiendraient tout le code de base que j'utilisais toujours dans mes projets.

Au début, j'ai simplement créé les modèles et les ai enregistrés sur mon système pour pouvoir copier le code chaque fois que je commençais un nouveau projet. Mais cela devenait également stressant, et je voulais simplement taper quelques lettres, appuyer sur entrer, et voir mes modèles apparaître à l'écran. C'est à ce moment-là que j'ai découvert les extraits de code VSCode.

Je ne savais pas que cela s'appelait des extraits de code à l'époque, alors j'ai passé plus de 2 semaines à essayer de trouver un outil qui pourrait m'aider à faire cela et j'ai presque abandonné. Jusqu'à ce que je tombe par hasard sur la vidéo de Brad Travesty lors de mes pérégrinations nocturnes sur les rues de YouTube sans chercher activement.

C'était un sauveur, et de temps en temps, j'ajoute de nouveaux extraits de code personnalisés à ma collection. Vous pouvez consulter mes modèles HTML et CSS personnalisés [ici](https://github.com/timonwa/my-templates.git).

Vous avez probablement souvent souhaité avoir un extrait de code personnalisé pour un morceau de code particulier que vous utilisez tout le temps, mais vous ne saviez pas comment le créer ou le trouver. Eh bien, ne souhaitez plus, car je vais vous montrer comment créer facilement le vôtre.

## Comment créer des extraits de code personnalisés
Créer votre propre extrait de code personnalisé est assez facile. Et avec l'aide d'un autre outil appelé **Snippet Generator** (dont je vais vous montrer comment l'utiliser bientôt), cela devient encore plus facile.

### Étape 1 : Vérifiez si votre éditeur vous permet de créer des extraits de code personnalisés
Vous pouvez consulter la documentation de votre éditeur de code pour savoir si la fonctionnalité est disponible et comment y accéder. 

J'utilise VsCode pour ce tutoriel. Vous pouvez le télécharger [ici](https://code.visualstudio.com/download).

Pour accéder à ce paramètre, vous pouvez soit cliquer sur l'**icône des paramètres** dans la barre latérale, puis cliquer sur **user snippets**, soit ouvrir la palette de commandes en utilisant Ctrl + Maj + P sur Windows ou CMD + Maj + P sur Mac, taper "snippet" et cliquer sur **Preferences: Configure User Snippets**.

Cela vous donnera une liste déroulante avec différentes sélections de langues parmi lesquelles choisir.

![video1-open-code-snippet](https://www.freecodecamp.org/news/content/images/2022/01/video1-open-code-snippet.gif)

### Étape 2 : Décidez de la portée de votre extrait de code
Vous pouvez soit créer un extrait de code global que vous pouvez utiliser dans tous les langages, soit créer un extrait de code local limité à un langage particulier.

Ainsi, dans la liste déroulante, vous pouvez voir **New Global Snippet File** puis une série de langages dans l'ordre alphabétique.
 
Faites défiler jusqu'au langage pour lequel vous souhaitez écrire votre extrait de code et cliquez dessus (ou sélectionnez **New Global Snippet File** si vous souhaitez utiliser vos extraits de code dans plusieurs langages).

Si vous avez sélectionné un langage particulier, par exemple HTML, le fichier s'ouvrira automatiquement. Mais si vous avez choisi un extrait de code global, vous serez invité à taper le nom du fichier d'extrait de code avant qu'il ne s'ouvre.

Pour cet exemple, j'utiliserai un extrait de code global.

![video2-enter-snippet-name](https://www.freecodecamp.org/news/content/images/2022/01/video2-enter-snippet-name.gif)

### Étape 3 : Comprendre la syntaxe
La syntaxe pour les extraits de code est en fait assez simple. Elle est écrite au format JSON et chaque fichier peut contenir un nombre illimité d'extraits de code.

```json
{
// Extrait de code 1
  "Nom de l'extrait": {
    "scope": "langage1, langage2", 
    "prefix": "mot déclencheur 1",
    "body": ["votre extrait de code"],
    "description": "description du code"
  },
// Extrait de code 2
  "Nom de l'extrait": {
    "scope": "langage1, langage2", 
    "prefix": ["mot déclencheur 1, mot déclencheur 2"],
    "body": ["votre extrait de code"],
    "description": "description du code"
  }
}
```

Voyons ce qui se passe dans ce code :

#### Nom de l'extrait
Le nom de l'extrait est le nom de l'extrait de code. C'est aussi ce qui sera affiché via IntelliSense si aucune description n'est fournie.

#### Portée
Cela détermine quels langages sont autorisés à utiliser l'extrait de code. Entrez le nom du ou des langages séparés par une virgule. Si vous le laissez vide ou l'omettez, l'extrait de code peut être accessible par n'importe quel langage. Cette partie est incluse uniquement dans les extraits de code globaux, car les fichiers d'extraits de code locaux sont déjà limités localement. 

#### Préfixe
Cela décrit un ou plusieurs mots déclencheurs qui inciteront IntelliSense à afficher l'extrait de code.

#### Corps
Cela peut être une chaîne de caractères si c'est un code d'une seule ligne ou un tableau de chaînes de caractères si c'est un code multilingue.

#### Description
Cela décrit l'extrait de code et ce qu'il fait. Si cela est omis, le nom de l'extrait de code sera utilisé à la place.

Exemple d'extrait de code 1 :

```json
{
// journaliser dans la console
  "Imprimer dans la console": {
    "scope": "javascript, typescript",
    "prefix": "log",
    "body": "console.log();",
    "description": "Journaliser la sortie dans la console"
  }
}
```

Dans l'exemple ci-dessus, le nom de notre extrait de code est **Imprimer dans la console**, et il ne peut être utilisé que dans un **fichier JavaScript et TypeScript**. Si vous deviez taper **log** dans un fichier JavaScript ou TypeScript, IntelliSense l'afficherait avec la description **Journaliser la sortie dans la console**. Une fois que vous l'avez sélectionné et que vous cliquez sur entrer, vous verrez **console.log()** à l'écran.

![video3-log](https://www.freecodecamp.org/news/content/images/2022/01/video3-log.gif)

### Étape 4 : Ajouter des arrêts de tabulation
Les arrêts de tabulation vous permettent de déplacer le curseur de l'éditeur à l'intérieur d'un extrait de code. $1, $2, ..., $n spécifient les emplacements du curseur où il doit se déplacer séquentiellement lorsque vous appuyez sur la touche de tabulation. $0 représente la position finale où le curseur doit s'arrêter.

Exemple d'extrait de code 2 :

```json
// fonction nommée
{
  "Fonction nommée": {
    "scope": "javascript, typescript",
    "prefix": "nfn",
    "body": [
      "function $1($2){",
      "  $0",
      "}"
    ],
    "description": ""
  }
}
```

Dans cet exemple, lorsque vous tapez **nfn**, notre extrait de code de fonction nommée apparaît. Une fois que vous l'avez sélectionné, vous verrez votre extrait de code à l'écran. Vous remarquerez également que le curseur est maintenant avant la parenthèse au lieu d'être à la fin du code.

Tapez le nom de la fonction, par exemple "GetUsers", puis appuyez sur la touche de tabulation. Vous remarquerez que le curseur s'est maintenant déplacé à l'intérieur de la parenthèse. 

Vous pouvez taper le paramètre s'il y en a un et appuyer à nouveau sur la touche de tabulation pour déplacer le curseur vers le prochain arrêt de tabulation qui se trouve entre les accolades où ira le corps de notre fonction.

![vide04-tabstop](https://www.freecodecamp.org/news/content/images/2022/01/vide04-tabstop.gif)

Remarque : Lorsque vous écrivez du code multilingue, vous ne pouvez pas utiliser une tabulation pour indenter votre code dans la syntaxe JSON. Vous ne pouvez utiliser que 2 espaces pour indenter votre code, ou quel que soit le nombre d'espaces d'indentation que vous utilisez pour écrire votre code.

### Étape 5 : Utiliser des espaces réservés
Ce sont des arrêts de tabulation avec des valeurs. Ils aident l'utilisateur à identifier ou à comprendre facilement ce qu'il est censé taper à cet arrêt de tabulation particulier. 

L'espace réservé sera automatiquement mis en surbrillance afin que vous puissiez immédiatement taper ce que vous voulez pour le remplacer.

Exemple d'extrait de code 3 :

```json
// fonction nommée
{
  "Fonction nommée": {
    "scope": "javascript, typescript",
    "prefix": "nfn",
    "body": [
      "function ${1:nomFonction}(${2:paramètre}){",
      "  ${0:corpsFonction}",
      "}"
    ],
    "description": ""
  }
}
```

![video5-placeholders](https://www.freecodecamp.org/news/content/images/2022/01/video5-placeholders.gif)

### Étape 6 : Créer des choix
Les espaces réservés peuvent avoir des choix comme valeurs. Cela signifie qu'au lieu de taper votre valeur, vous pouvez choisir parmi une sélection déroulante.

Pour en créer un, vous écrivez les valeurs qui sont séparées par une virgule entre deux caractères pipe, par exemple, ${1|un, deux, trois|}.

Exemple d'extrait de code 4 :

```json
// méthode de tableau
{
"Méthode de tableau": {
    "scope": "javascript, typescript",
    "prefix": "arrmth",
    "body": [
      "${1|forEach, map, filter, reduce|}((${2:item}) => {",
      "  $0",
      "})"
    ],
    "description": ""
  }
}
```

![video6-choices](https://www.freecodecamp.org/news/content/images/2022/01/video6-choices.gif)

Ici, une fois que vous tapez `arrmth`, sélectionnez-le dans IntelliSense et appuyez sur entrer. Le premier arrêt de tabulation sera une liste déroulante de choix de tableaux parmi lesquels sélectionner. Le prochain arrêt de tabulation est le paramètre et le dernier arrêt est le code de la fonction.

## Générateurs d'extraits de code
À mesure que vos extraits de code grandissent en lignes et en taille, il devient difficile de les taper et de les créer dans votre éditeur de code. C'est là qu'intervient un générateur d'extraits de code.

Un générateur d'extraits de code prendra votre code régulier et le transformera en un extrait de code.

Je vais utiliser [Snippet Generator](https://snippet-generator.app/) pour ce tutoriel. Avec ce générateur d'extraits de code particulier, vous pouvez écrire des extraits de code pour VsCode, Sublime Text et Atom.

![image1-snippet-generator](https://www.freecodecamp.org/news/content/images/2022/01/image1-snippet-generator.png)

### Comment utiliser le générateur d'extraits de code
Dans le champ **description**, entrez le nom de l'extrait de code qui sera utilisé comme nom et description de l'extrait de code.

Dans le champ **tab trigger**, entrez le préfixe de votre extrait de code.

Dans le champ **your snippet..**, entrez votre code dans sa forme naturelle comme vous le feriez sans l'écrire comme un tableau de chaînes de caractères.

Après cela, vous pouvez ajouter des arrêts de tabulation, des espaces réservés et des choix comme expliqué ci-dessus.

Exemple d'extrait de code 5 :

```js
// fonction nommée
function ${1:nomFonction}(${2: paramètre}) {
  ${0:corpsFonction}
}
```

![image2-arrow-function](https://www.freecodecamp.org/news/content/images/2022/01/image2-arrow-function.png)

Exemple d'extrait de code 6 :

```js
// méthode de tableau
${1|forEach, map, filter, reduce,|}((${2:item}) => {
 $0
)}

```

![image3-array-method](https://www.freecodecamp.org/news/content/images/2022/01/image3-array-method.png)

## Code final de l'extrait de code
```json
{
  // journaliser dans la console
  "Imprimer dans la console": {
    "scope": "javascript, typescript",
    "prefix": "log",
    "body": "console.log();",
    "description": "Journaliser la sortie dans la console"
  },
  // fonction nommée
  "Fonction nommée": {
    "scope": "javascript, typescript",
    "prefix": "nfn",
    "body": [
      "function ${1:nomFonction}(${2:paramètre}){",
      "  ${0:corpsFonction}",
      "}"
    ],
    "description": ""
  },
  // méthode de tableau
  "Méthode de tableau": {
    "scope": "javascript, typescript",
    "prefix": "arrmth",
    "body": [
      "${1|forEach, map, filter, reduce|}((${2:item}) => {",
      "  $0",
      "})"
    ],
    "description": ""
  }
}
```

Et voilà. Facile comme bonjour.

## Récapitulatif
Faisons un récapitulatif. Nous avons appris que :

- un extrait de code est une petite portion de code source, de code machine ou de texte réutilisable qui aide les programmeurs à réduire le temps nécessaire pour taper des codes répétitifs lors de la programmation.
- un fichier d'extrait de code peut contenir un nombre illimité d'extraits de code.
- vous pouvez avoir un extrait de code à portée locale utilisé uniquement dans un fichier de langage ou un extrait de code à portée globale utilisé dans deux fichiers de langage ou plus.
- les extraits de code sont écrits en syntaxe JSON.
- vous pouvez ajouter des arrêts de tabulation, des espaces réservés et des choix à vos extraits de code.
- vous pouvez également utiliser un générateur d'extraits de code pour générer vos extraits de code.

Merci d'avoir lu mon article. Vous pouvez me contacter sur [Twitter](https://twitter.com/timonwa_), [LinkedIn](https://linkedIn.com/in/pelumi-akintokun) ou [mon Blog](https://blog.timonwa.com). 

J'aimerais savoir si vous allez créer vos propres extraits de code personnalisés et ce qu'ils pourraient être. Et n'hésitez pas à partager cet article avec d'autres personnes qui pourraient le trouver utile. Au revoir !

![Mr Beans disant au revoir](https://www.freecodecamp.org/news/content/images/2022/01/HoDL1vbXj.gif)

## Ressources
- [Vidéo de Brad sur les extraits de code personnalisés](https://youtu.be/JIqk9UxgKEc)
- [Documentation sur les extraits de code VsCode](https://code.visualstudio.com/docs/editor/userdefinedsnippets)
- [Générateur d'extraits de code](https://snippet-generator.app/)
- [Voir mes modèles HTML et CSS personnalisés](https://github.com/timonwa/my-templates.git)