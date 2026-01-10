---
title: Extraits de code Visual Studio Code – le guide définitif des extraits VS Code
  pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-24T18:00:00.000Z'
originalURL: https://freecodecamp.org/news/definitive-guide-to-snippets-visual-studio-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/harry-hd.png
tags:
- name: Productivity
  slug: productivity
- name: Snippet
  slug: snippet
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: Extraits de code Visual Studio Code – le guide définitif des extraits VS
  Code pour débutants
seo_desc: 'By Rob O''Leary

  Snippets can add a touch of magic to your editor. It''s like an incantation. Utter
  a short phrase (type a prefix), wave your wand (press Enter or Tab), and presto!
  A wonderful event unfolds in front of you. ✨

  Most code editors support s...'
---

Par Rob O'Leary

Les extraits de code peuvent ajouter une touche de magie à votre éditeur. C'est comme une incantation. Prononcez une courte phrase (tapez un préfixe), agitez votre baguette (appuyez sur `Entrée` ou `Tab`), et presto ! Un merveilleux événement se déroule devant vous. ✨

La plupart des éditeurs de code supportent les extraits de code dès leur installation. L'éditeur de code que je vais utiliser pour présenter les extraits est Visual Studio Code (VS Code), l'éditeur le plus populaire du moment.

De plus, il existe certaines applications "d'expansion de texte" qui vous permettent d'utiliser des extraits de code globalement (dans toutes les applications). Je vais brièvement expliquer comment vous pouvez utiliser ces applications pour tirer encore plus parti des extraits de code.

Plongeons dans l'univers des extraits de code. ?

## Définition

> Un extrait de code est un modèle qui peut être inséré dans un document. Il est inséré par une commande ou via un texte déclencheur.

Avec les extraits de code, vous pouvez créer un fichier modèle, et insérer des blocs de texte couramment utilisés. L'idée générale est de vous éviter de taper encore et encore les mêmes choses. ?

## Pourquoi utiliser des extraits de code ?

Je ne vais pas vous choquer avec cette affirmation : Internet est le foyer de nombreuses opinions contradictoires ! Les extraits de code n'échappent pas à cette ignominie, mais je ne pense pas que ce soit un sujet qui fasse monter la tension artérielle des gens !

Pour l'équilibre, je vais présenter ici un échantillon de ces opinions.

Vous n'avez pas à choisir un camp et être totalement pour ou contre les extraits de code. Je vous suggère de les adopter dans une mesure qui vous sert le mieux.

### Camp du Oui ?

- Les extraits de code peuvent augmenter votre productivité, en vous faisant économiser des frappes et en réduisant les erreurs de saisie.
- Les extraits de code me laissent plus de CPU mental et de plaisir à dépenser pour écrire le code qui m'intéresse et sur lequel je veux me concentrer.
- Les extraits de code peuvent vous aider à vous souvenir d'inclure quelque chose d'important !
- Intégrer des extraits de code dans votre flux de travail vous encourage implicitement à utiliser moins souvent la souris. Les extraits de code bien écrits offrent un chemin logique que vous pouvez parcourir avec la touche Tab, en vous arrêtant pour éditer en cours de route afin de compléter le modèle exactement comme vous le souhaitez, et lorsque vous avez terminé, vous arrivez de l'autre côté prêt à écrire votre prochaine ligne.

### Camp du Non ?

- Je m'abstiens de les utiliser, principalement parce que je n'aime pas dépendre d'un outil donné.
- Je n'utilise jamais d'extraits de code. Je préfère investir du temps à éviter la répétition plutôt qu'à la faciliter.
- J'ai remarqué qu'à un moment donné, j'ai oublié comment écrire le code sans utiliser l'extrait. Pour des choses triviales que je comprends, c'est OK, mais je ne veux pas oublier d'autres choses !
- La plupart, sinon tous, les extraits de code que j'ai vus en ligne, pour le code que je cherche, contiennent des erreurs. Je n'ai jamais trouvé un algorithme numérique qui n'avait pas d'erreurs de virgule flottante. Je ne peux pas imaginer qu'il existe une ressource d'extraits de code parfaitement propres.

## Quand utiliser des extraits de code ?

Donald Knuth, l'un des grands sorciers de l'informatique, a dit que "l'optimisation prématurée [du code] est la racine de tous les maux".

Je pense que cela est également pertinent pour les extraits de code. Les extraits de code sont une optimisation de la production de code. Si vous ne connaissez pas bien un langage ou un framework, implémenter une série d'extraits de code pour ce langage ou ce framework est probablement une démarche prématurée.

Si vous êtes à l'aise, alors essayez-en quelques-uns !

## À quoi j'utilise les extraits de code

Personnellement, j'utilise souvent des extraits de code, mais avec discernement. J'utilise un ensemble d'extraits pour Markdown et la plupart des langages avec lesquels je travaille.

Je n'ai pas beaucoup utilisé d'extraits pour les frameworks. J'ai commencé à utiliser quelques extraits pour Vue récemment, mais je n'utilise que l'extrait de modèle. J'adopterai probablement plus d'extraits une fois que mon QI Vue aura augmenté. 

Je n'ai pas utilisé d'extraits pour les algorithmes.

## Types d'extraits de code

Les extraits de code peuvent être classés selon l'étendue de l'interactivité entre l'extrait et l'éditeur.

#### Extraits statiques

Vous pouvez le considérer comme un copier-coller de quelque texte source en une seule commande.

#### Extraits dynamiques

Un extrait dynamique peut être personnalisé pour offrir une expérience de type assistant pour la complétion d'un extrait.

Il peut inclure :

- *Arrêts de tabulation* : Vous pouvez numéroter des arrêts que vous pouvez parcourir avec la touche Tab,
- *Arrêts de tabulation miroir* : Il arrive que vous deviez fournir la même valeur à plusieurs endroits dans le texte inséré. Vous pouvez miroir un arrêt de tabulation pour y parvenir, et toute modification sera reflétée instantanément dans les arrêts de tabulation associés.
- *Espaces réservés* : C'est un arrêt de tabulation avec une valeur par défaut qui peut être écrasée lors de la mise au point.
- *Choix* : À un arrêt de tabulation, vous êtes présenté avec une liste déroulante de valeurs parmi lesquelles choisir.
- *Variables* : Valeurs d'entrée de l'environnement telles que : le texte sélectionné dans l'éditeur, les dates système, ou le contenu du presse-papiers.

Voici un exemple d'extrait Markdown qui ajoute une liste de tâches avec 2 tâches. Il utilise des *arrêts de tabulation*, des *espaces réservés* et des *choix* pour cocher une tâche.

![tâche](https://www.freecodecamp.org/news/content/images/2020/09/task.gif)

#### Macro extraits

Le niveau supérieur de sorcellerie est d'avoir la capacité de transformer l'entrée. Les transformations vous permettent de modifier la valeur d'une variable avant qu'elle ne soit insérée, ou de modifier un espace réservé après avoir fait une édition.

Par exemple, vous pouvez vouloir mettre en majuscule un nom de classe une fois qu'il est entré.

Tout ce que vous pouvez imaginer faire avec une regex est généralement possible. Certains éditeurs offrent des possibilités de script plus avancées.

## Extraits de code dans Visual Studio Code

Dans VS Code, les extraits de code apparaissent dans **IntelliSense** (`Ctrl+Espace` vous donne une liste de suggestions), ils sont mélangés avec d'autres suggestions.

Vous pouvez également y accéder dans un sélecteur d'extraits dédié en utilisant la commande **'Insérer un extrait'**. Cela combine tous les extraits utilisateur, d'extension et intégrés pour ce langage en une seule liste.

![liste-insertion-extrait](https://www.freecodecamp.org/news/content/images/2020/09/insert-snippet-list.png)

[Emmet](https://www.emmet.io/) est intégré à VS Code et possède sa propre syntaxe inspirée des sélecteurs CSS pour insérer des extraits HTML et CSS.

Emmet est vraiment une chose à part, mais les mécanismes sont les mêmes. Vous pouvez en apprendre davantage sur Emmet avec le [guide Emmet dans Visual Studio Code](https://code.visualstudio.com/docs/editor/emmet).

### Paramètres utilisateur associés

Les extraits de code apparaissent comme des **suggestions rapides** si le paramètre `editor.quickSuggestions` est défini sur vrai pour le langage avec lequel vous travaillez. Les suggestions rapides sont activées par défaut pour la plupart des langages, sauf pour Markdown.

![suggestions-rapides-js](https://www.freecodecamp.org/news/content/images/2020/09/quick-suggestions-js.png)

Les extraits de code supportent la **complétion par tabulation**. Vous pouvez taper un préfixe d'extrait (le texte déclencheur), et appuyer sur `Tab` pour insérer un extrait. Vous pouvez l'activer avec le paramètre `editor.tabCompletion`.

Les valeurs sont :

- `on` : La complétion par tabulation est activée pour toutes les sources.
- `off` : Désactive les complétions par tabulation. C'est la *valeur par défaut*.
- `onlySnippets` : Complétion par tabulation uniquement pour les extraits de code.

```json
"editor.tabCompletion": "onlySnippets",
```

Si vous souhaitez contrôler la manière dont les **suggestions d'extraits** sont affichées, vous pouvez modifier le paramètre `editor.snippetSuggestions`.

Les valeurs sont :

- `top` : Afficher les suggestions d'extraits en haut des autres suggestions. J'utilise cette valeur.
- `bottom` : Afficher les suggestions d'extraits en bas des autres suggestions.
- `inline` : Afficher les suggestions d'extraits avec les autres suggestions. C'est la *valeur par défaut*.
- `none` : Ne pas afficher les suggestions d'extraits.

```json
"editor.snippetSuggestions": "top",
```

Ce sont les paramètres les plus importants pour les extraits de code, mais il y en a quelques autres. Vous pouvez consulter cette [liste des paramètres par défaut](https://code.visualstudio.com/docs/getstarted/settings#_default-settings) pour en explorer davantage, ou effectuer une recherche dans l'interface utilisateur des paramètres.

### Y a-t-il des extraits intégrés ?

Oui !

Ils ne sont pas documentés dans la documentation de VS Code, cependant. Et à l'intérieur de VS Code, il n'y a pas de point central pour les parcourir. Donc, vous ne savez peut-être pas ce qu'ils sont.

Alors, comment pouvez-vous savoir quels langages ont des extraits intégrés ?

En bref, j'étais frustré par ce scénario, alors j'ai écrit une extension appelée [**Snippets Ranger**](https://marketplace.visualstudio.com/items?itemName=robole.snippets-ranger) pour offrir une belle interface utilisateur pour explorer facilement les extraits. Pensez-y comme à une *Carte du Maraudeur* pour les extraits !

![snippets-ranger](https://www.freecodecamp.org/news/content/images/2020/09/snippets-ranger.png)

#### Mais je veux trouver les extraits par moi-même ?

Vous pouvez, cela demande juste un peu plus d'efforts.

Comme je l'ai mentionné plus tôt, la commande **'Insérer un extrait'** vous montrera tous les extraits pour le langage du document actif.

Souvenez-vous cependant, ceci est une *agrégation* de tous les extraits utilisateur, d'extension et intégrés. Donc, si vous voulez savoir si un langage particulier a des extraits intégrés, vous devez ouvrir un fichier pour ce langage, et exécuter la commande pour voir cette liste.

Si vous avez une extension d'extraits installée pour ce langage qui rend trop difficile l'identification de chacun, vous pourriez la désactiver pour vous assurer que seuls les extraits intégrés sont affichés. ?

Si vous voulez retrouver le fichier source vous-même, les extraits intégrés se trouvent à l'intérieur de chaque répertoire d'extension de langage individuel. Le fichier est situé à `app root\resources\app\extensions\language\snippets\language.code-snippets` sur Windows. L'emplacement est similaire pour Mac et Linux.

### Extensions d'extraits

Le Visual Studio Marketplace possède une [catégorie d'extraits](https://marketplace.visualstudio.com/search?target=VSCode&category=Snippets&sortBy=Installs) où vous pouvez trouver des extraits pour presque tout.

Beaucoup d'extensions de packs de langages de programmation incluent également des extraits (Python, C#, Go, Java, et C/C++ parmi d'autres).

### Comment écrire les miens ?

Les fichiers d'extraits sont écrits en JSON. Vous pouvez également ajouter des commentaires de style C si vous le souhaitez (techniquement, il s'agit du format "JSONC" de Microsoft).

Vous pouvez créer des extraits pour différentes portées : globale, espace de travail, et pour un langage particulier.

Pour créer le fichier d'extraits, exécutez la commande **'Préférences : Configurer les extraits utilisateur'**, qui ouvre une boîte de dialogue de sélection rapide comme ci-dessous. Votre sélection ouvrira un fichier pour l'édition.

![extraits-utilisateur](https://www.freecodecamp.org/news/content/images/2020/09/user-snippets.png)

Si vous préférez écrire un extrait dans une interface graphique, vous pouvez utiliser l'application web [générateur d'extraits](https://snippet-generator.app).

![générateur-extrait](https://www.freecodecamp.org/news/content/images/2020/09/snippet-generator.png)

Examinons un exemple pour nous familiariser avec la syntaxe.

#### Exemple

Voici un extrait Markdown qui vient avec VS Code.

```json
{
    "Insérer un titre de niveau 1": {
       "prefix": "heading1",
       "body": ["# ${1:${TM_SELECTED_TEXT}}$0"],
       "description" : "Insérer un titre de niveau 1"
    }
}
```

Cet extrait insère un titre de niveau 1 qui enveloppe le Markdown autour de la sélection actuelle (si elle existe).

Un extrait possède les propriétés suivantes :

1. "Insérer un titre de niveau 1" est le nom de l'extrait. C'est la valeur qui est affichée dans la liste de suggestions IntelliSense si aucune `description` n'est fournie.
2. La propriété `prefix` définit la phrase déclencheur pour l'extrait. Elle peut être une chaîne ou un tableau de chaînes (si vous voulez plusieurs phrases déclencheurs). La correspondance de sous-chaîne est effectuée sur les préfixes, donc dans ce cas, taper "h1" correspondrait à notre exemple d'extrait.
3. La propriété `body` est le contenu qui est inséré dans l'éditeur. C'est un tableau de chaînes, qui est une ou plusieurs lignes de contenu. Le contenu est joint avant l'insertion.
4. La propriété `description` peut fournir plus d'informations sur l'extrait. Elle est facultative.
5. La propriété `scope` vous permet de cibler des langages spécifiques, et vous pouvez fournir une liste séparée par des virgules dans la chaîne. Elle est facultative. Bien sûr, elle est redondante pour un fichier d'extraits spécifique à un langage.

Le corps de cet extrait a 2 arrêts de tabulation et utilise la variable `${TM_SELECTED_TEXT}`.

Plongeons dans la syntaxe pour comprendre cela pleinement.

#### Syntaxe des extraits

La syntaxe des extraits de VS Code est la même que la [syntaxe des extraits de TextMate](https://manual.macromates.com/en/snippets). Cependant, elle ne supporte pas le 'code shell interpolé' et l'utilisation de la transformation `\u`.

Le `body` d'un extrait supporte les fonctionnalités suivantes :

#### 1. Arrêts de tabulation

Les arrêts de tabulation sont spécifiés par un signe dollar et un nombre ordinal, par exemple `$1`. `$1` sera le premier emplacement, `$2` sera le deuxième emplacement, et ainsi de suite. `$0` est la position finale du curseur, qui quitte le mode extrait.

Par exemple, disons que nous voulons créer un extrait HTML *div* et que nous voulons que le premier arrêt de tabulation soit entre les balises d'ouverture et de fermeture. Nous voulons également permettre à l'utilisateur de tabuler en dehors des balises pour terminer l'extrait.

Alors nous pourrions créer un extrait comme ceci :

```json
{
    "Insérer div": {
        prefix: "div",
        body: ["<div>","$1","</div>", "$0"]
    }
}
```

#### 2. Arrêts de tabulation miroir

Il arrive que vous deviez fournir la même valeur à plusieurs endroits dans le texte inséré. Dans ces situations, vous pouvez réutiliser le même nombre ordinal pour les arrêts de tabulation afin de signaler que vous souhaitez qu'ils soient miroir. Vos modifications sont alors synchronisées.

Un exemple typique est une boucle *for* qui utilise une variable *index* plusieurs fois. Ci-dessous se trouve un exemple JavaScript d'une boucle *for*.

```json
{
    "Boucle For": {
        "prefix": "for",
        "body": [
            "for (let ${1:index} = 0; ${1:index} < ${2:array}.length; ${1:index}++) {",
            "\tconst ${3:element} = ${2:array}[${1:index}];",
            "\t$0",
            "}"
        ]
	}
}
```

#### 3. Espaces réservés

Les espaces réservés sont des arrêts de tabulation avec des valeurs par défaut. Ils sont enveloppés dans des accolades, par exemple `${1:default}`. Le texte de l'espace réservé est sélectionné lors de la mise au point de sorte qu'il peut être facilement édité. Les espaces réservés peuvent être imbriqués, comme ceci : `${1:first ${2:second}}`.

#### 4. Choix

Les choix présentent à l'utilisateur une liste de valeurs à un arrêt de tabulation. Ils sont écrits comme une liste de valeurs séparées par des virgules, enfermées dans des caractères pipe, par exemple `${1|yes,no|}`.

Voici le code pour l'exemple Markdown montré précédemment pour insérer une liste de tâches. Les choix sont 'x' ou un espace vide.

```json
{
  "Insérer une liste de tâches": {
    "prefix": "task",
    "body": ["- [${1| ,x|}] ${2:text}", "${0}"]
}
```

#### 5. Variables

Il existe une bonne sélection de variables que vous pouvez utiliser. Vous ajoutez simplement le nom avec un signe dollar pour les utiliser, par exemple `$TM_SELECTED_TEXT`.

Par exemple, cet extrait créera un commentaire de bloc pour n'importe quel langage avec la date d'aujourd'hui :

```json
{
    "Insérer un commentaire de bloc avec date": {
        prefix: "date comment",
        body: ["${BLOCK_COMMENT_START}",
               "${CURRENT_YEAR}/${CURRENT_MONTH}/${CURRENT_DATE} ${1}",
               "${BLOCK_COMMENT_END}"]
    }
}
```

Vous pouvez spécifier une valeur par défaut pour une variable si vous le souhaitez, comme `${TM_SELECTED_TEXT:default}`. Si une variable n'a pas de valeur assignée, la valeur par défaut ou une chaîne vide est insérée.

Si vous faites une erreur et incluez un nom de variable qui n'est pas défini, le nom de la variable est transformé en espace réservé.

Les variables d'espace de travail suivantes peuvent être utilisées :

- `TM_SELECTED_TEXT` : Le texte actuellement sélectionné ou la chaîne vide,
- `TM_CURRENT_LINE` : Le contenu de la ligne actuelle,
- `TM_CURRENT_WORD` : Le contenu du mot sous le curseur ou la chaîne vide,
- `TM_LINE_INDEX` : Le numéro de ligne basé sur zéro,
- `TM_LINE_NUMBER` : Le numéro de ligne basé sur un,
- `TM_FILENAME` : Le nom de fichier du document actuel,
- `TM_FILENAME_BASE` : Le nom de fichier du document actuel sans ses extensions,
- `TM_DIRECTORY` : Le répertoire du document actuel,
- `TM_FILEPATH` : Le chemin complet du fichier du document actuel,
- `CLIPBOARD` : Le contenu de votre presse-papiers,
- `WORKSPACE_NAME` : Le nom de l'espace de travail ou du dossier ouvert.

Les variables suivantes liées au temps peuvent être utilisées :

- `CURRENT_YEAR` : L'année en cours,
- `CURRENT_YEAR_SHORT` : Les deux derniers chiffres de l'année en cours,
- `CURRENT_MONTH` : Le mois sous forme de deux chiffres (exemple '07'),
- `CURRENT_MONTH_NAME` : Le nom complet du mois (exemple 'Juillet'),
- `CURRENT_MONTH_NAME_SHORT` : Le nom court du mois (exemple 'Jul'),
- `CURRENT_DATE` : Le jour du mois,
- `CURRENT_DAY_NAME` : Le nom du jour (exemple 'Lundi'),
- `CURRENT_DAY_NAME_SHORT` : Le nom court du jour (exemple 'Lun'),
- `CURRENT_HOUR` : L'heure actuelle au format 24 heures,
- `CURRENT_MINUTE` : La minute actuelle,
- `CURRENT_SECOND` : La seconde actuelle,
- `CURRENT_SECONDS_UNIX` : Le nombre de secondes depuis l'époque Unix.

Les variables de commentaire suivantes peuvent être utilisées. Elles respectent la syntaxe du langage du document :

- `BLOCK_COMMENT_START` : Par exemple, `<!--` en HTML,
- `BLOCK_COMMENT_END` : Par exemple, `-->` en HTML,
- `LINE_COMMENT` : Par exemple, `//` en JavaScript.

#### 6. Transformations

Les transformations peuvent être appliquées à une variable ou à un espace réservé. Si vous êtes familier avec les expressions régulières (regex), la plupart de cela devrait vous être familier.

Le format d'une transformation est : `${variable ou espace réservé/regex/chaîne de remplacement/drapeaux}`. Il est similaire à [String.protoype.replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace) en JavaScript. Les "paramètres" font ce qui suit :

- `regex` : Il s'agit d'une expression régulière qui est comparée à la valeur de la variable ou de l'espace réservé. La syntaxe des regex JavaScript est supportée.
- `chaîne de remplacement` : Il s'agit de la chaîne que vous souhaitez remplacer par le texte original. Elle peut référencer des groupes de capture de `regex`, effectuer un formatage de casse (en utilisant les fonctions spéciales : `/upcase`, `/downcase`, et `/capitalize`), et effectuer des insertions conditionnelles. Voir [Syntaxe de la chaîne de remplacement TextMate](https://macromates.com/manual/en/regular_expressions#replacement_string_syntax_format_strings) pour plus d'informations approfondies.
- `drapeaux` : Drapeaux qui sont passés à l'expression régulière. Les [drapeaux regex JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Advanced_searching_with_flags_2) peuvent être utilisés :
  - `g` : Recherche globale,
  - `i` : Recherche insensible à la casse,
  - `m` : Recherche multi-ligne,
  - `s` : Permet à `.` de correspondre aux caractères de nouvelle ligne,
  - `u` : Unicode. Traite le motif comme une séquence de points de code Unicode,
  - `y` : Effectue une recherche "collante" qui correspond en commençant à la position actuelle dans la chaîne cible.

Pour référencer un groupe de capture, utilisez `$n` où `n` est le numéro du groupe de capture. Utiliser `$0` signifie la correspondance entière.

Cela peut être un peu confus puisque les arrêts de tabulation ont la même syntaxe. Il suffit de se souvenir que si elle est contenue dans des barres obliques, alors elle référence un groupe de capture.

Le moyen le plus simple de comprendre pleinement la syntaxe est de consulter quelques exemples.

| Corps de l'extrait                                               | Entrée                  | Sortie                 | Explication                                                  |
| ------------------------------------------------------------ | ---------------------- | ---------------------- | ------------------------------------------------------------ |
| `["${TM_SELECTED_TEXT/^.+$/\u2022 $0/gm}"]`                       | ligne1<br>ligne2         | \u2022 ligne1<br>\u2022 ligne2     | Mettre un point de puce avant chaque ligne non vide du texte sélectionné. |
| `["${TM_SELECTED_TEXT/^(\\w+)/${1:/capitalize}/}"]`          | the cat is on the mat. | The cat is on the mat. | Mettre en majuscule le premier mot du texte sélectionné.                  |
| `["${TM_FILENAME/.*/${0:/upcase}/}"]`                        | example.js             | EXAMPLE.JS             | Insérer le nom de fichier du fichier actuel en majuscules.          |
| `[`<br>` "[",`<br>` "${CLIPBOARD/^(.+)$/'$1',/gm}",`<br>` "]"`<br>`]` | ligne1<br>ligne2         | ['ligne1', 'ligne2',]    | Transformer le contenu du presse-papiers en un tableau de chaînes. Chaque ligne non vide est un élément. |

Comme vous pouvez le voir dans le deuxième exemple ci-dessus, les séquences de métacaractères doivent être échappées, par exemple insérer `\\w` pour un caractère de mot.

#### Transformations d'espaces réservés

**Les transformations d'espaces réservés ne permettent <u>pas</u> de valeur par défaut ou de choix** ! Peut-être est-il plus approprié de les appeler transformations d'arrêts de tabulation.

L'exemple ci-dessous mettra en majuscules le texte du premier arrêt de tabulation.

![transformation-espace-réservé](https://www.freecodecamp.org/news/content/images/2020/09/placeholder-transform.gif)

```json
{
  "Mettre en majuscules le premier arrêt de tabulation": {
    "prefix": "up",
    "body": ["${1/.*/${0:/upcase}/}", "$0"]
  }
}
```

Vous pouvez avoir un espace réservé et effectuer une transformation sur une instance miroir. La transformation ne sera pas effectuée sur l'espace réservé initial. ?

Utiliseriez-vous ce comportement quelque part ? Je le trouve déroutant au début, donc il peut avoir le même effet sur les autres.

```json
{
  "Mettre en majuscules uniquement la deuxième instance de l'arrêt de tabulation": {
    "prefix": "up",
    "body": ["${1:title}", "${1/(.*)/${1:/upcase}/}", "$0"]
  }
}
```

### Comment assigner des raccourcis clavier pour les extraits ?

En ajoutant vos raccourcis à `keybindings.json`. Vous pouvez ouvrir le fichier en exécutant la commande **'Préférences : Ouvrir le fichier des raccourcis clavier (JSON)'**.

Par exemple, pour ajouter un raccourci pour l'extrait Markdown intégré "Insérer un titre de niveau 1" :

```json
{
    "key": "ctrl+m ctrl+1",
    "command": "editor.action.insertSnippet",
    "when": "editorTextFocus && editorLangId == markdown",
    "args": {
        "langId": "markdown",
        "name": "Insérer un titre de niveau 1"
    }
}
```

Vous définissez un raccourci en spécifiant la combinaison de touches que vous souhaitez utiliser, l'ID de la commande, et un contexte de clause [when](https://code.visualstudio.com/docs/getstarted/keybindings#_when-clause-contexts) facultatif pour le contexte lorsque le raccourci clavier est activé.

Via l'objet `args`, vous pouvez cibler un extrait existant en utilisant les propriétés `langId` et `name`. L'argument `langId` est l'[ID de langage](https://code.visualstudio.com/docs/languages/identifiers#_known-language-identifiers) du langage pour lequel les extraits ont été écrits. Le `name` est le nom de l'extrait tel qu'il est défini dans le fichier d'extraits.

Vous pouvez définir un extrait en ligne si vous le souhaitez en utilisant la propriété `snippet`.

```json
[
  {
    "key": "ctrl+k 1",
    "command": "editor.action.insertSnippet",
    "when": "editorTextFocus",
    "args": {
      "snippet": "${BLOCK_COMMENT_START}${CURRENT_YEAR}/${CURRENT_MONTH}/${CURRENT_DATE} ${1} ${BLOCK_COMMENT_END}"
    }
  }
]
```

Vous pouvez également utiliser l'*interface utilisateur des raccourcis clavier*, mais elle n'a pas la capacité d'ajouter un nouveau raccourci.

Un autre inconvénient de l'interface utilisateur est qu'elle n'affiche pas l'objet `args`, ce qui rend plus difficile la recherche et l'édition de vos raccourcis personnalisés. ?

![interface-utilisateur-raccourcis](https://www.freecodecamp.org/news/content/images/2020/09/shortcuts-ui.png)

## Une question de style

Quelque chose que j'ai trouvé déroutant au début avec les extraits de code était la propension des gens à créer des extraits avec des préfixes abrégés. Dois-je apprendre une grande liste d'acronymes incompréhensibles pour utiliser les extraits de quelqu'un d'autre ?

Que veux-je dire par préfixes abrégés ? Le tableau ci-dessous liste quelques-uns des extraits de l'extension [JavaScript (ES6) code snippets](https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets) de VS Code. Vous pouvez voir dans la colonne *Déclencheur*, les préfixes listés sont des abréviations, par exemple *fre* pour représenter une boucle "for each".

![extraits-es6](https://www.freecodecamp.org/news/content/images/2020/09/es6-snippets-excerpt.png)

Cela est inutile à deux égards.

Premièrement, les suggestions rapides offertes par VS Code sont produites à partir d'une **recherche de sous-chaîne floue**. Si je tape "fe" et que le préfixe d'un extrait est "foreach", cela correspondra et sera offert comme suggestion rapide.

Comme vous pouvez le voir ci-dessous, c'est la deuxième correspondance.

![suggestion-rapide-fe](https://www.freecodecamp.org/news/content/images/2020/09/fe-quick-suggestion.png)

La première correspondance est *fre*, qui est un extrait de l'extension. Quelle suggestion est la plus descriptive ? ?

Si vous utilisez la commande "Insérer un extrait" pour les extraits, cela ne fait pas une grande différence. Le champ de description compense ce manque. Je n'utilise pas les extraits de cette manière, donc je préférerais un préfixe plus descriptif.

![insérer-extrait-foreach](https://www.freecodecamp.org/news/content/images/2020/09/insertsnippet-foreach.png)

Deuxièmement, *fre* est un **doublon** de l'extrait intégré *foreach*.

Certaines personnes désactivent les suggestions rapides pour les extraits et utilisent uniquement la complétion par tabulation. Dans ce cas, vous devez taper un préfixe sans obtenir de retour visuel. Certaines personnes peuvent préférer utiliser un préfixe abrégé pour économiser des frappes ici.

La même recherche de sous-chaîne floue est effectuée en arrière-plan, donc le premier extrait correspondant est inséré lorsque vous appuyez sur tab.

![complétion-extrait-tab](https://www.freecodecamp.org/news/content/images/2020/09/snippet-tab-completion.gif)

En regardant l'exemple ci-dessus, vous pouvez voir que taper "fr" et appuyer sur *tab* insère l'extrait *fre*. Taper "fore" et appuyer sur tab insère l'extrait *foreach*.

Donc, vous n'avez pas besoin de taper le préfixe entier, si vous ne le souhaitez vraiment pas ! ? Si vous avez de nombreux préfixes d'extraits similaires pour un langage, cela serait probablement impraticable.

Il est plus pratique d'apprendre les préfixes correctement et de les taper entièrement avant d'appuyer sur tab.

Il y a quelques compromis en fonction de vos préférences pour l'utilisation des extraits.

Personnellement, j'aime utiliser les suggestions rapides car j'aime le retour visuel. J'ai configuré les extraits pour qu'ils soient les premières suggestions, de cette façon je peux taper des versions abrégées des préfixes sans avoir besoin de les mémoriser.

Certains auteurs d'extraits ont des motifs rigides pour surmonter cela, mais c'est quelque chose que je ne peux pas facilement adopter.

Si vous utilisez beaucoup d'extraits pour un langage, vous pouvez vouloir choisir des extraits écrits dans un style similaire.

Si vous utilisez des extraits pour différents frameworks et bibliothèques dans un langage, ils peuvent s'accumuler et se chevaucher. Je n'ai pas eu besoin de le faire, mais vous pourriez devoir le faire éventuellement.

## Extraits globaux

En dehors de votre éditeur de code, vous pouvez également bénéficier des extraits de code. Avoir des extraits disponibles dans chaque application offre plus de possibilités.

Les cas d'utilisation courants sont :

- réponses préenregistrées pour les messages,
- autocorrection des fautes de frappe courantes,
- ajout d'informations de contact ou de signatures aux documents,
- insertion de dates,
- mise en forme du texte sélectionné et du texte collé,
- insertion de phrases de recherche pour votre moteur de recherche ou application,
- extraits HTML disponibles dans votre client de messagerie,
- ajout de différents modèles aux documents.

La plupart des applications pour les extraits sont présentées comme des "expandeurs de texte", mais plusieurs applications de tâches et de productivité incluent également des fonctionnalités similaires à des extraits.

Les extraits globaux sont **un peu plus limités que les extraits d'éditeur de code**, car vous ne pouvez pas utiliser les arrêts de tabulation et les espaces réservés. Dans la plupart des applications, vous pouvez utiliser certaines variables dynamiques comme les dates.

### Revue des applications

#### Autohotkey (Windows)

[AutoHotkey](https://www.autohotkey.com/) est un **langage de script gratuit et open-source pour Windows** permettant d'effectuer toutes sortes de tâches.

Il a sa propre syntaxe unique. Vous pouvez installer l'[extension AutoHotKey](https://marketplace.visualstudio.com/items?itemName=slevesque.vscode-autohotkey) pour ajouter la prise en charge du langage à VS Code pour une meilleure expérience d'édition.

Pour définir des préfixes afin de déclencher l'insertion d'un extrait, vous utilisez le format suivant : `::<<prefix>>::<<texte à insérer>>`. Le script suivant insérera l'adresse e-mail de Rob lorsque vous tapez "robmail" et appuyez sur *espace* ou *tab* ou *entrée*.

```
::robmail::rob@someservername.com
```

Le script suivant insérera le texte "Ceci est le texte de l'extrait" lorsque vous appuyez sur `Ctrl+D`.

```
^d::  Send Ceci est le texte de l'extrait
```

Vous pouvez lire la [documentation](https://www.autohotkey.com/docs/AutoHotkey.htm) pour en savoir plus.

#### PhraseExpress (Windows, Mac, iOS)

[PhraseExpress](https://www.phraseexpress.com/) est "un logiciel d'expansion de texte, qui gère des modèles de texte fréquemment utilisés pour insertion dans n'importe quel programme".

C'est une **application freemium, basée sur une interface graphique**. Elle est destinée à un public plus large que *AutoHotKey*.

Elle est assez polie et facile à utiliser. Vous la configurez pour qu'elle s'exécute au démarrage et elle sera active en arrière-plan.

Vos extraits peuvent être organisés dans des dossiers personnalisés et synchronisés à l'aide de services cloud.

![phrase-express](https://www.freecodecamp.org/news/content/images/2020/09/phrase-express.png)

#### Espanso (Windows, Mac, Linux)

Il s'agit d'un **expandeur de texte open-source, multiplateforme écrit en Rust**.

Il utilise une **approche de configuration basée sur des fichiers**. Les fichiers de configuration sont écrits en [YAML](https://en.wikipedia.org/wiki/YAML).

Le fichier `default.yml` contient la configuration principale. La configuration ci-dessous insérera l'adresse e-mail de Rob lorsque vous tapez "robmail".

```yaml
matches:
 - trigger: ":robmail"
   replace: "rob@someservername.com"
```

Vous pouvez **spécifier la position initiale du curseur**, cependant vous ne pouvez pas définir d'arrêts de tabulation.

Vous pouvez **ajouter des extensions** pour augmenter les capacités d'Espanso. Il existe des extensions pour exécuter des scripts externes, inclure des dates, générer du texte aléatoire et inclure des données du presse-papiers.

Et c'est à peu près tout ! J'espère que vous avez appris quelque chose sur les extraits de code aujourd'hui, et que vous pouvez les utiliser pour vous rendre plus productif.