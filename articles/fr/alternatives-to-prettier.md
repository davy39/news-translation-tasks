---
title: Alternatives à Prettier – Outils populaires de Linting et de Formatage de Code
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2023-03-15T17:43:50.000Z'
originalURL: https://freecodecamp.org/news/alternatives-to-prettier
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Alternatives-to-Prettier.png
tags:
- name: clean code
  slug: clean-code
- name: eslint
  slug: eslint
- name: Prettier
  slug: prettier
seo_title: Alternatives à Prettier – Outils populaires de Linting et de Formatage
  de Code
seo_desc: "Many programmers hate code formatting because it is tedious and time-consuming.\
  \ You can spend hours making sure everything is perfect and well-indented. \nThis\
  \ is why code formatters are so useful.\nA code formatter is a tool that formats\
  \ code accordin..."
---

Beaucoup de programmeurs détestent le formatage de code parce que c'est fastidieux et chronophage. Vous pouvez passer des heures à vous assurer que tout est parfait et bien indenté. 

C'est pourquoi les formateurs de code sont si utiles.

Un formateur de code est un outil qui formate le code selon certaines normes. Il fait en sorte que vous n'ayez plus à vous soucier autant du formatage du code. Au lieu de cela, vous pouvez vous concentrer sur l'écriture d'un bon code. Cela permet de gagner du temps et de réduire votre stress.

Dans ce guide, nous parlerons du formateur de code Prettier. Nous parlerons également d'alternatives à Prettier comme JsFmt, StandardJS, ESLint + EditorConfig, et JS Beautifier. J'espère que vous en retirerez quelque chose que vous pourrez utiliser pour améliorer votre formatage de code.

## Aperçu rapide de Prettier

[Prettier](https://prettier.io/) est un formateur de code populaire capable de gérer des structures de code complexes et de formater votre code de manière lisible.

Il fonctionne sur le principe de l'absence de configuration requise et est conçu pour produire un code lisible et cohérent.

Prettier est un outil aux avis tranchés (opinionated) qui encourage les programmeurs à suivre ses règles de formatage. Il analyse également le code et le réimprime de manière uniforme.

## Pourquoi explorer des alternatives à Prettier ?

L'utilisation de Prettier présente de nombreux avantages. Mais comme pour tout autre outil, explorer des alternatives est parfois une bonne idée. Voici quelques-unes des raisons d'explorer des alternatives à Prettier :

1. **Guides de style rigides** : Prettier adopte un ensemble strict de règles de formatage et ne permet pas beaucoup de personnalisation. Certains programmeurs veulent un outil offrant de nombreuses configurations.
2. **Vitesse** : Bien que Prettier soit rapide, vous pourriez avoir besoin d'un outil offrant des performances plus rapides et meilleures dans de grandes bases de code ou pour un formatage en temps réel.
3. **Support des langages** : Prettier peut ne pas supporter (ou offrir un support inadéquat) pour le langage que vous utilisez.
4. **Plus de fonctionnalités** : Bien que Prettier soit open source, vous pourriez préférer un formateur de code payant possédant plus de fonctionnalités et une meilleure intégration avec d'autres outils.

Dans ce guide, nous parlerons de quatre alternatives à Prettier. Elles sont :

* JsFmt
* StandardJS
* ESLint + EditorConfig
* JS Beautifier

## Aperçu de JsFmt

[JsFmt](https://rdio.github.io/jsfmt/) est un formateur de code qui utilise esformatter comme outil de formatage. Il reformate automatiquement le code JavaScript selon un ensemble de règles prédéfinies. Il est disponible spécifiquement pour réécrire, formater, rechercher et valider du code JavaScript.

Pour installer JsFmt, exécutez cette commande :

```
npm install -g jsfmt
```

Un fichier .jsfmtrc, qui peut être au format JSON ou INI, peut écraser n'importe laquelle des options de formatage d'esformatter.

```json
{
  "indent": 4,
  "line_ending": "unix",
  "quote": "single"
}

```

Dans cet exemple, nous avons spécifié que les espaces pour l'indentation soient de quatre, nous avons choisi unix pour les fins de ligne, et nous avons choisi single (simple) comme style de guillemets pour les chaînes de caractères.

Vous pouvez utiliser la méthode rewrite de jsfmt pour changer des valeurs dans votre code JavaScript. Voici un exemple de la marche à suivre :

```javascript
const x = 5;
const y = 10;
const z = x + y;
console.log(z);

// La sortie changera pour le code ci-dessous après l'écriture : npx jsfmt --rewrite '5 -> 20' reduce.js

const x = 20;
const y = 10;
const z = x + y;
console.log(z);

```

Pour en savoir plus sur JsFmt, vous pouvez lire sa documentation [ici](https://github.com/rdio/jsfmt).

### Fonctionnalités de JsFmt

1. Formatage : JsFmt peut formater le code selon un ensemble de règles prédéfinies.
2. Intégrations : vous pouvez intégrer JsFmt avec des éditeurs de code populaires comme Visual Studio Code, Sublime Text et Atom, ce qui facilite le formatage de votre code directement dans votre éditeur.
3. Interface de ligne de commande : JsFmt vous permet de formater votre code dans le cadre de votre processus de build ou de votre flux de travail de développement dans la ligne de commande.

### Règles de formatage de JsFmt

Certaines des règles de formatage adoptées par JsFmt sont les suivantes :

1. Définir l'indentation : Avec l'option `--indent`, JsFmt indente votre code avec deux espaces par niveau.
2. Guillemets : Dans JsFmt, les guillemets simples sont par défaut pour les chaînes, mais vous pouvez changer cela avec l'option `--double-quote`.
3. Habillage (Wrapping) : vous pouvez utiliser `--linene-width` pour changer le paramètre par défaut de retour à la ligne dans JsFmt.
4. Points-virgules : JsFmt ajoute des points-virgules à la fin de chaque instruction par défaut. Vous pouvez désactiver cela en utilisant l'option `--no-semi`.

### Avantages de JsFmt

1. Formatage, recherche et réécriture de JavaScript.
2. Personnalisable : La flexibilité de JsFmt en fait un choix populaire pour de nombreuses équipes de développement. C'est un outil hautement personnalisable que vous pouvez configurer pour correspondre aux exigences spécifiques d'un projet.

### Inconvénient de JsFmt

1. Manque de flexibilité : malgré le fait qu'il soit personnalisable, certaines parties de JsFmt peuvent ne pas toujours être configurables pour répondre aux besoins de votre projet.

## Aperçu de StandardJS

[StandardJS](https://standardjs.com/) est un linter, formateur et guide de style JavaScript open source, sans configuration. Il vérifie le code pour les erreurs probables avec le linter. Il formate également le code automatiquement et vous aide à écrire un code facile à lire et à comprendre.

C'est l'option la plus populaire, avec 27 905 étoiles sur GitHub pour un linter de code propre. C'est aussi un outil puissant pour assurer la qualité et la cohérence de votre code JavaScript.

Vous pouvez l'installer soit globalement, soit localement sur votre machine. Pour l'installer globalement, utilisez la première commande, tandis que la seconde commande sert à l'installation locale. Notez que pour l'installer, vous devez avoir Node et npm installés sur votre ordinateur.

Pour installer globalement : `$ npm install standard --global`

Pour installer localement : `$ npm install standard --save-dev`

Alternativement, vous pouvez ajouter StandardJS au package JSON.

```json
{
  "name": "my-cool-package",
  "devDependencies": {
    "standard": "*"
  },
  "scripts": {
    "test": "standard && node my-tests.js"
  }
}

```

Les styles sont vérifiés automatiquement lorsque vous lancez la commande :

```
npm test
```

Pour illustrer son fonctionnement, vérifiez le code JavaScript ci-dessous :

```javascript!
let number = 10;
if (number == 10) {
  alert("yes");
} else {
  alert("no");
}

// La sortie après avoir exécuté npm test dans le terminal

> test
> standard && node my-tests.js

standard: Use JavaScript Standard Style (https://standardjs.com)
  C:\Users\hp\Desktop\pretier\Js\script.js:5:5: Parsing error: Unexpected token else (null)

```

StandardJS montre que le code contient une erreur d'analyse.

Pour corriger la plupart des problèmes, lancez le code suivant :

```
standard --fix
```

### Fonctionnalités de StandardJS

1. Communauté : Une communauté de contributeurs guide le développement de StandardJS en fournissant des corrections de bugs et de nouvelles fonctionnalités.
2. Linting : Le linting de StandardJS détecte tôt les problèmes de style et les erreurs de programmation.
3. Formatage automatique du code : StandardJS élimine le code désordonné et incohérent.
4. Intégration en ligne de commande : Il dispose d'une interface de ligne de commande pour exécuter des vérifications de linter et formater automatiquement le code.

### Règles de formatage de StandardJS

Certaines des règles de formatage StandardJS les plus utilisées sont listées ci-dessous :

1. Indentation : StandardJS impose un niveau d'indentation cohérent de 2 espaces par défaut. Pour implémenter cela strictement, vous devez ajouter l'option `--fix`.
2. Retour à la ligne : StandardJS n'impose pas la règle de la longueur de ligne, mais il recommande de garder les lignes de moins de 80 caractères. Utilisez `$ myfile.js | standard --stdin` pour vérifier manuellement la longueur du fichier.
3. Points-virgules : StandardJS recommande d'utiliser des points-virgules pour plus de clarté et pour éviter des problèmes potentiels. Mais l'outil ne l'impose pas. Pour imposer l'usage des points-virgules, utilisez ceci :

```json
{
  "extends": "standard"
}

```

1. Espaces autour des opérateurs : StandardJS recommande d'utiliser des espaces autour des opérateurs, tels que + et -, mais il n'impose pas cette règle.

### Avantages de StandardJS

1. Zéro configuration : Aucune décision à prendre. StandardJS est le moyen le plus simple d'imposer la qualité du code dans votre projet.
2. Installation facile : StandardJS est facile à installer et vous pouvez l'utiliser avec la plupart des éditeurs et IDE.
3. Améliore la productivité : StandardJS fait gagner du temps aux développeurs et augmente la productivité en formatant le code selon ses règles.
4. Large support : La plupart des éditeurs et IDE supportent StandardJS via des plugins et des intégrations.
5. Cohérence : StandardJS favorise la cohérence entre les projets en imposant un ensemble strict de règles de codage.

### Inconvénients de StandardJS

1. Avis tranchés (Opinionated) : Certains développeurs peuvent trouver l'outil trop directif. Si c'est le cas, vous préférerez peut-être utiliser d'autres outils de linting qui permettent plus de personnalisation.
2. Flexibilité limitée : StandardJS impose un ensemble strict de règles et de conventions, ce dont certains développeurs peuvent se sentir limités, préférant une approche plus personnalisable.

## Aperçu de ESLint + EditorConfig

[ESlint](https://eslint.org/) fournit des règles configurables que vous pouvez adapter selon les besoins spécifiques de votre projet. C'est l'un des linters JavaScript les plus populaires qui analyse les erreurs de programmation, les bugs et les constructions suspectes.

Vous pouvez étendre sa fonctionnalité en ajoutant des plugins, qui peuvent fournir des analyseurs personnalisés et des règles supplémentaires.

Vous aurez besoin de Node installé avant d'installer ESLint. Pour l'installer, utilisez la commande ci-dessous :

```
npm init @eslint/config
```

Alternativement, vous pouvez créer cela manuellement sur votre machine :

```
npm install --save-dev eslint
```

Pour les deux installations, vous devez avoir un fichier package.json installé. Sinon, lancez cette commande :

```
npx eslint --init
```

La commande posera une série de questions sur votre projet, votre style de codage et vos préférences pour générer votre fichier de configuration.

Vous pouvez exécuter ESLint sur n'importe lequel de vos répertoires ou fichiers avec cette commande :

```
npx eslint yourfile.js
```

Les règles peuvent être désactivées et vous pouvez exécuter l'outil uniquement avec une validation de syntaxe de base, car ESLint est configurable et flexible selon votre cas d'utilisation.

Une fois que vous avez généré le fichier de configuration, vous pouvez le personnaliser selon vos besoins. Le fichier de configuration est un fichier JavaScript qui exporte un objet avec les paramètres de configuration.

Par exemple, vous pouvez spécifier les règles que vous voulez, les plugins à utiliser et les environnements pour votre code :

```json
{
  "rules": {
    "semi": ["error", "always"],
    "quotes": ["error", "double"],
    "indent": ["error", 4]
  }
}

```

semi, quotes et indent sont les noms des règles dans ESLint, tandis que le niveau d'erreur de la règle est la première valeur. Il n'y a que trois sorties pour les premières valeurs. Ce sont :

* "off" ou 0 - désactive la règle
* "warn" ou 1 - active la règle comme un avertissement (n'affecte pas le code de sortie)
* "error" ou 2 - active la règle comme une erreur (le code de sortie sera 1).

```json
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": "eslint: recommended",
  "overrides": [],
  "parserOptions": {
    "ecmaVersion": "latest"
  },
  "rules": {
    "indent": ["error", 4],
    "quotes": ["error", "single"],
    "semi": ["error", "never"]
  }
}

```

Dans cet exemple, vous spécifiez que votre code doit s'exécuter dans un environnement de navigateur. Activez la syntaxe ECMAScript 2018 et suivez les règles ESLint. Vous avez également activé trois règles spécifiques : indent, quotes et semi.

La règle indent détermine qu'une erreur d'alerte sera levée si l'indentation est supérieure à 4 espaces. De même, si vous utilisez des guillemets doubles au lieu de simples, il y aura une erreur. Vous avez également spécifié de ne pas utiliser de points-virgules.

Pour corriger la plupart des problèmes dans ESLint, utilisez cette commande :

```
npx eslint yourfile.js --fix
```

Voici un exemple :

```javascript
const numbers = [1, 3, 5, 2, 6, 78, 8];
let peoples = ["shola", "kamal"];
console.log(peoples);

// La sortie

 error  'numbers' is assigned a value but never used  no-unused-vars
   error  Extra semicolon                               semi

✖ 2 problems (2 errors, 0 warnings)
  1 error and 0 warnings potentially fixable with the `--fix` option.

```

### Aperçu d'EditorConfig

[EditorConfig](https://editorconfig.org/#file-format-details) est un format de fichier open source. Il fournit des moyens standard de définir et de maintenir les styles de codage dans un projet.

Il maintient des styles de codage cohérents, ce qui est particulièrement utile lorsque vous avez de nombreux développeurs travaillant sur le même projet à travers divers éditeurs et IDE. L'outil consiste en une collection de plugins pour éditeurs de texte qui permettent aux éditeurs de lire le format de fichier et d'adhérer aux styles définis.

Vous devrez créer un fichier nommé .editorconfig dans le répertoire. Les plugins EditorConfig chercheront le fichier dans le répertoire du fichier ouvert et dans chaque répertoire parent.

Les fichiers sont lus de haut en bas, et une recherche de fichiers .editorconfig s'arrêtera si le chemin du fichier racine est atteint.

Créer un fichier EditorConfig est simple. Ouvrez un nouveau fichier et enregistrez-le sous .editorconfig comme indiqué ci-dessous.

![fichier editorconfig](https://i.imgur.com/SHEafBl.png)

À l'intérieur du fichier .editorconfig, les motifs génériques (wildcards) suivants sont utilisés :

```javascript
root = true

[*]
 
indent_size = 4
indent_style = space
end_of_line = lf
insert_final_newline = true

 // Définir root sur true : Une recherche de fichiers .editorconfig s'arrêtera si le chemin du fichier racine est atteint ou si un fichier EditorConfig avec root=true est trouvé.
 
 //[*]: Sauf pour les sélecteurs de chemin, il correspond à n'importe quelle chaîne de caractères.
 
 //indent_size: La taille de l'indentation est fixée à 4. 
 //indent_style: défini sur space (espace)
 //end_of_line: Défini sur lf
//insert_final_newline: Défini sur true

```

Pour en savoir plus sur les motifs génériques, visitez la [documentation d'EditorConfig](https://editorconfig.org/#file-format-details).

Utiliser ESLint et EditorConfig ensemble peut aider à repérer les problèmes potentiels tôt. Cela garantit également que votre code est cohérent, maintenable et de haute qualité.

La combinaison d'ESLint et d'EditorConfig vous fait gagner du temps sur la maintenance du code et le débogage.

### Fonctionnalités d'ESLint

1. Configurable : ESLint vous permet de personnaliser et d'ajouter vos propres règles au fichier de configuration.
2. Support ECMAScript : ESLint garantit que votre code est compatible avec les dernières fonctionnalités du langage.
3. Supporte de nombreux formats de fichiers : ESLint peut analyser le code JavaScript dans une variété de formats de fichiers, y compris, mais sans s'y limiter, .js, .jsx et .vue.
4. Intégration : ESLint s'intègre parfaitement avec Webpack et Gulp, qui sont des outils de build populaires.

### Règles de formatage d'ESLint

Certaines des règles de formatage populaires dans ESLint sont listées ci-dessous :

1. Indentation : ESLint attend par défaut une indentation de quatre espaces par niveau. Mais vous pouvez personnaliser cela en utilisant l'option populaire `--fix`.
2. Points-virgules : ESLint impose l'utilisation de points-virgules à la fin de chaque instruction. Cette règle est définie sur "always" par défaut. Utilisez l'option populaire `--fix` pour la réinitialiser sur "never".
3. Retour à la ligne : Utilisez la règle `max-len` pour changer la longueur maximale de ligne de la valeur par défaut de 80 à votre valeur préférée.
4. Guillemets : La règle des guillemets peut être changée de la valeur par défaut "single" à "double" en utilisant l'option `--fix`.

### Avantages d'ESLint

1. Gain de temps : ESLint fait gagner du temps en réduisant le temps passé sur les revues de code manuelles et le débogage.
2. Communauté active : ESLint dispose d'une base communautaire large et active qui contribue au développement de l'outil et de son écosystème.
3. Analyseur de code : ESLint analyse votre code pour trouver rapidement des problèmes.
4. Cohérence : ESLint aide à maintenir un code propre et lisible en imposant un style de codage cohérent.

### Inconvénients d'ESLint

1. Conflits de règles : Avec un grand ensemble de règles, les règles d'ESLint peuvent parfois entrer en conflit les unes avec les autres, entraînant plus de configuration et de réglages fins.
2. Courbe d'apprentissage plus raide : ESLint a une courbe d'apprentissage assez raide, car il possède de nombreuses règles et apprendre à les configurer peut prendre du temps.
3. Faux positifs : ESLint peut parfois signaler du code comme problématique même lorsqu'il est correct, ce qui peut être frustrant pour les développeurs.

## Aperçu de JS Beautifier

[JavaScript Beautifier](https://beautifier.io/), également connu sous le nom de js-beautify, est un outil de ligne de commande open source et multiplateforme. C'est un embellisseur pour reformater et réindenter les bookmarklets, le JavaScript illisible (ugly), et il désobscurcit partiellement les scripts.

Vous pouvez installer JS Beautifier localement et globalement.

Exécutez `npm -g install js-beautify` pour l'installer globalement, et `npm install js-beautify` pour l'installer localement.

Vous pouvez le configurer via l'option de ligne de commande.

Après l'installation locale, vous pouvez importer et appeler les méthodes d'embellissement appropriées pour JS, CSS ou HTML. Un exemple d'appel des méthodes ressemble à ceci : beautify (`code`, `options`).

Alors que `code` est la chaîne de caractères du code à embellir, `options` est un objet avec les paramètres que vous aimeriez utiliser pour embellir le code. Voir l'exemple ci-dessous pour un fichier de script JavaScript :

```
npx beautify("script.js",{indent_size:4})

```

Vous pouvez également le configurer via un fichier de configuration :

```json
{
  "indent_size": 4,
  "indent_char": " ",
  "indent_with_tabs": false,
  "brace_style": "collapse"
}

```

Créez un fichier `.jsbeautifyrc` dans le répertoire racine de votre projet. Cette option écrasera l'option par défaut de JS Beautifier. Vous pouvez également utiliser Beautifier sur votre navigateur web. En savoir plus sur [JSbeautifer d'après sa documentation ici](https://www.npmjs.com/package/js-beautify).

### Fonctionnalités de JS Beautifier

1. Formatage : Vous pouvez personnaliser JS Beautifier pour l'adapter à vos préférences personnelles et à votre style de codage car il offre une variété d'options de formatage, telles que la taille de l'indentation et le style des accolades.
2. Version en ligne : Vous pouvez embellir le JavaScript en utilisant JS Beautifier dans votre navigateur web, tout comme vous le pouvez sur la ligne de commande.

### Règles de formatage de JS Beautifier

1. Indentation : L'indentation par défaut dans JS Beautifier est de 4 espaces, mais vous pouvez la changer à 2 ou 8 espaces, ou utiliser des tabulations à la place. Utilisez l'option `indent_size` pour spécifier le nombre d'espaces à utiliser pour l'indentation.
2. Points-virgules : Vous pouvez modifier vos paramètres de points-virgules dans JS Beautifier avec l'option `semicolon`. Vous changez cela en alternant la valeur de l'option semicolon entre "true" (vrai) ou "false" (faux).
3. Retour à la ligne : Utilisez l'option `max_char` pour limiter chaque ligne à 80 caractères. Vous pouvez définir la valeur de max_char à 80 ou tout autre nombre préféré.

### Avantages de JS Beautifier

1. Gain de temps : JS Beautifier fait gagner du temps. Il automatise les nombreuses étapes de formatage et d'organisation du code.
2. Présence en ligne : La présence en ligne de JS Beautifier change la donne, car beaucoup de non-développeurs pourront l'utiliser.
3. Détecte les erreurs : JS Beautifier aide à repérer de petites erreurs qui peuvent être difficiles à remarquer autrement.
4. Intégration : La compatibilité de JS Beautifier avec une variété d'éditeurs de code et d'IDE en fait un outil polyvalent.

### Inconvénients de JS Beautifier

1. Complexité : Malgré l'existence d'une version en ligne, JS Beautifier est quelque peu complexe pour les débutants.
2. Risque de sur-formatage : Dans certains cas, JS Beautifier peut rendre le code plus difficile à lire à cause d'un formatage excessif.

## Résultats de tous les outils de formatage

Nous utiliserons l'échantillon de code ci-dessous pour tester comment ces quatre outils populaires formatent le code :

```javascript
const numbers = [2,3,8,9,7]

          let peoples = ['kamal', 'lawal', "shola", "olaide"];


```

Comme vous pouvez le voir, ce code n'est pas correctement formaté. Voyons donc comment les outils aident.

### Exemple de formatage avec JsFmt

En utilisant le code ci-dessus comme échantillon, la commande `npx jsfmt --write "Votre fichier"` formatera le code ainsi :

```javascript
const numbers = [2, 3, 8, 9, 7]

let peoples = ['kamal', 'lawal', "shola", "olaide"];

```

Comme vous pouvez le voir, il y a un changement notable dans le code, et vous pouvez configurer cela selon vos goûts.

### Exemple de formatage avec StandardJS

En lançant la célèbre commande `npx standard --fix` depuis le terminal, vous obtiendrez le résultat suivant.

```javascript
const numbers = [2, 3, 8, 9, 7]

const peoples = ['kamal', 'lawal', 'shola', 'olaide']

```

Remarquez que le code a été correctement formaté, tout particulièrement les éléments avec des guillemets doubles à l'intérieur du tableau `peoples`.

### Exemple de formatage avec ESLint

En utilisant le même code que ci-dessus, la commande `npx eslint "Nom de votre fichier --fix"` formatera rapidement ainsi :

```javascript
const numbers = [2,3,8,9,7]

let peoples = ['kamal','lawal','shola','olaide']

```

Vous pouvez également changer la configuration de l'outil, en modifiant les éléments du tableau `peoples` pour qu'ils soient à l'intérieur de guillemets doubles :

```javascript
const numbers = [2,3,8,9,7]

let peoples = ["kamal","lawal","shola","olaide"];

```

Vous pouvez le faire en allant dans le fichier .eslintrc et en manipulant les règles comme ceci :

```json
{
  "quotes": ["error", "double"],
  "semi": ["off", "always"]
}

```

### Exemple de formatage avec JS Beautifier

Voici le résultat de JS Beautifier pour le même code :

```javascript
const numbers = [2, 3, 8, 9, 7]
let peoples = ['kamal', 'lawal', "shola", "olaide"];

```

Vous pouvez le configurer davantage depuis votre fichier JSON si vous le souhaitez.

Maintenant, vous avez vu ces formateurs en action !

## Conclusion

Dans ce guide, nous avons parlé de quelques alternatives à l'utilisation de Prettier. Nous avons discuté de JsFmt, ESLint, StandardJS et JS Beautifier, ainsi que de leurs fonctionnalités, avantages et inconvénients.

J'espère que vous êtes maintenant mieux équipé pour choisir le bon linter/formateur pour vos projets de codage.