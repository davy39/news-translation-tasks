---
title: Ces outils vous aideront à écrire du code propre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T00:27:37.000Z'
originalURL: https://freecodecamp.org/news/these-tools-will-help-you-write-clean-code-da4b5401f68e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3OpyAlDBIinyME_ro6wq3A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Ces outils vous aideront à écrire du code propre
seo_desc: 'By Adeel Imran

  A look at Prettier, ESLint, Husky, Lint-Staged and EditorConfig

  Learning to write good code, but you don’t know where to start… Going through style-guides
  like Airbnb’s Javascript Style Guide… Trying to write code with best practices.....'
---

Par Adeel Imran

#### Un aperçu de Prettier, ESLint, Husky, Lint-Staged et EditorConfig

Apprendre à écrire du bon code, mais vous ne savez pas par où commencer... Parcourir des guides de style comme [Airbnb's Javascript Style Guide](https://github.com/airbnb/javascript)... Essayer d'écrire du code avec les meilleures pratiques...

Supprimer du code mort ? Trouver des variables inutilisées dans la base de code ? Essayer de trouver des motifs problématiques dans votre code ? Comme, est-ce qu'il `return` ou non ?

Tout cela vous semble familier ?

Avec tant de choses à apprendre et à faire en même temps, c'est juste trop chaotique.

Êtes-vous un Team Lead gérant une équipe diverse ? Avez-vous de nouveaux développeurs dans l'équipe ? Craignez-vous qu'ils n'écrivent pas du code à la hauteur des standards ? Passez-vous toute votre journée en revues de code, où la revue porte plus sur les standards de code que sur la mise en œuvre réelle de la logique ?

J'ai été là et fait cela, et c'est juste si fatigant et chaotique.

Promettons de ne plus jamais nous soucier de l'apparence du code ou d'amener toute notre équipe à écrire du code d'une certaine manière qui est lintée et formatée correctement.

Tout au long de ce tutoriel, si vous êtes bloqué, voici le [dépôt de code](https://github.com/adeelibr/react-starter-kit). Les pull requests sont les bienvenues, si vous avez des suggestions d'améliorations.

Ce tutoriel est plus adapté aux applications React, mais le même peut être appliqué à n'importe quel projet web.

De plus, l'éditeur que j'utilise pour ce tutoriel est [VS Code](https://code.visualstudio.com/). C'est par [Microsoft](https://www.microsoft.com/en-us/) et depuis qu'ils sont passés à l'open source, je suis en ❤️ avec cette entreprise (bien qu'il y ait eu une époque où je ne l'étais pas).

### Agenda

* Prettier
* ESLint
* Automatiser le formatage et le linting à la sauvegarde
* Husky
* Lint-staged
* Avec Husky et Lint-staged combinés
* EditorConfig

### Commençons par Prettier

#### **_Qu'est-ce que Prettier ?_**

[Prettier](https://prettier.io/) est un formateur de code opinionné. Il formate le code pour vous d'une manière spécifique.

Ce GIF l'explique assez bien :

![Image](https://cdn-media-1.freecodecamp.org/images/1*opcd-o83ElQvQNP84oDgyQ.gif)
_Prettier formatant mon code, comme un boss !_

#### **_Pourquoi en avons-nous besoin ?_**

* **Nettoie la base de code existante** : en une seule commande. Imaginez nettoyer une base de code avec plus de 20 000 lignes de code.
* **Facile à adopter** : Prettier utilise le style de codage le moins controversé tout en formatant votre code. Puisqu'il est open source, de nombreuses personnes ont travaillé sur plusieurs itérations pour corriger certains cas particuliers et polir l'expérience.
* **Écrire du code** : Ce que les gens ne réalisent pas, c'est qu'ils passent beaucoup de temps à formater du code et à gaspiller leur énergie mentale à le faire. Laissez Prettier s'en occuper pendant que _vous_ vous concentrez sur la logique métier principale. Sur une note personnelle, Prettier a augmenté mon efficacité de 10 %.
* **Aider les développeurs débutants** : Si vous êtes un nouveau développeur travaillant côte à côte avec de grands ingénieurs et que vous voulez avoir l'air _cool_ en écrivant du code propre, soyez intelligent ! Utilisez Prettier.

#### **_Comment le configurer ?_**

Créez un dossier appelé `app` et à l'intérieur de ce dossier, tapez sur la ligne de commande :

```
npm init -y
```

Cela créera un fichier `package.json` pour vous à l'intérieur du dossier `app`.

Maintenant, je vais utiliser `yarn` tout au long de ce tutoriel, mais vous pouvez utiliser `npm` également.

Installons notre première dépendance :

```
yarn add --dev prettier
```

Cela installera une dépendance de développement dans votre `package.json` qui ressemblera à ceci :

```json
{
  "name": "react-boiler-plate",
  "version": "1.0.0",
  "description": "A react boiler plate",
  "main": "src/index.js",
  "author": "Adeel Imran",
  "license": "MIT",
  "scripts": {
    "prettier": "prettier --write src/**/*.js"
  },
  "devDependencies": {
    "prettier": "^1.14.3"
  }
}
```

Je vais parler dans une seconde de ce que fait ce `"prettier": "prettier --write src/**/*.js"`, mais d'abord, créons un dossier `src/` à l'intérieur de notre dossier `app`. Et à l'intérieur du dossier `src/`, créons un fichier appelé `index.js` — vous pouvez l'appeler comme vous voulez.

Dans le fichier `index.js`, collez ce code tel quel :

```javascript
let person =                     {
  name: "Yoda",
                designation: 'Jedi Master '
                };


              function trainJedi (jediWarrion) {
if (jediWarrion.name === 'Yoda') {
  console.log('No need! already trained');
}
console.log(`Training ${jediWarrion.name} complete`)
              }

trainJedi(person)
              trainJedi({ name: 'Adeel',
              designation: 'padawan' 
  });
```

Donc, jusqu'à présent, nous avons un fichier `src/app/index.js` avec du code mal écrit.

Il y a 3 choses que nous pouvons faire à ce sujet :

* Indenter et formater manuellement ce code
* Utiliser un outil automatisé
* Laisser les choses aller et passer à autre chose (Veuillez ne pas choisir cette option)

Je vais opter pour la deuxième option. Donc maintenant nous avons une dépendance installée et un script Prettier écrit dans notre `package.json`.

Créons un fichier `prettier.config.js` dans notre dossier racine `app`, et ajoutons-y quelques règles Prettier :

```javascript
module.exports = {
  printWidth: 100,
  singleQuote: true,
  trailingComma: 'all',
  bracketSpacing: true,
  jsxBracketSameLine: false,
  tabWidth: 2,
  semi: true,
};
```

`printWidth` garantira que votre code ne dépasse pas 100 caractères.

`singleQuote` convertira toutes vos doubles quotes en simples quotes.
Lisez plus dans le guide de style JavaScript d'Airbnb [ici](https://github.com/airbnb/javascript). Ce guide est mon livre de jeu pour écrire du bon code et impressionner mes collègues.

`trailingComma` garantira qu'il y a une virgule finale à la fin de la dernière propriété de l'objet. [Nik Graf](https://twitter.com/nikgraf) explique cela de manière si cool [ici](https://medium.com/@nikgraf/why-you-should-enforce-dangling-commas-for-multiline-statements-d034c98e36f8).

`bracketSpacing` imprime des espaces entre les littéraux d'objet :

```
Si bracketSpacing est vrai - Exemple : { foo: bar }
Si bracketSpacing est faux - Exemple : {foo: bar}
```

`jsxBracketSameLine` placera `>` d'un élément JSX multiline sur la dernière ligne :

```javascript
// exemple vrai

<button
  className="prettier-class"
  id="prettier-id"
  onClick={this.handleClick}>
  Click Here
</button>

// exemple faux

<button
  className="prettier-class"
  id="prettier-id"
  onClick={this.handleClick}
>
  Click Here
</button>
```

`tabWidth` spécifie le nombre d'espaces par niveau d'indentation.

`semi` si vrai, imprimera `;` à la fin des instructions.

Voici une liste de toutes les [options](https://prettier.io/docs/en/options.html) que vous pouvez donner à Prettier.

Maintenant que nous avons la configuration mise en place, parlons de ce script :

```
"prettier": "prettier --write src/**/*.js"
```

Dans le script ci-dessus, j'exécute `prettier` et lui dis de trouver tous les fichiers `.js` dans mon dossier `src/`. Le drapeau `--write` indique à `prettier` de sauvegarder les fichiers formatés au fur et à mesure qu'il parcourt chaque fichier et trouve toute anomalie dans la formation du code.

Exécutons ce script dans votre terminal :

```
yarn prettier
```

Voici ce qui arrive à mon code lorsque je l'exécute :

![Image](https://cdn-media-1.freecodecamp.org/images/1*XLy2nZkWeQz7gghWtweGKA.gif)
_Cool, non ?_

Si vous êtes bloqué, n'hésitez pas à jeter un œil au [dépôt](https://github.com/adeelibr/react-starter) pour cela.

Cela conclut assez bien notre discussion sur Prettier. Parlons des linters.

### ESLint

#### **_Qu'est-ce qu'un linter de code ?_**

> Le [linting](https://en.wikipedia.org/wiki/Lint_(software)) de code est un type d'analyse statique qui est fréquemment utilisé pour trouver des motifs problématiques ou du code qui n'adhère pas à certaines directives de style. Il existe des linters de code pour la plupart des langages de programmation, et les compilateurs incorporent parfois le linting dans le processus de compilation. — [ESLint](https://eslint.org/docs/about/)

#### **_Pourquoi en avons-nous besoin pour JavaScript ?_**

Puisque JavaScript est dynamique et un langage à typage faible [language](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures), il est sujet aux erreurs des développeurs. Sans le bénéfice d'un processus de compilation, les fichiers `.js` sont généralement exécutés afin de trouver des erreurs de syntaxe ou autres.

Les outils de linting comme [ESLint](https://eslint.org/) permettent aux développeurs de trouver des problèmes avec leur code JavaScript sans l'exécuter.

#### **_Qu'est-ce qui rend ESLint si spécial ?_**

Bonne question ! Tout dans ESLint est pluggable. Vous pouvez ajouter des règles à l'exécution — les règles et le formateur n'ont pas besoin d'être regroupés pour être utilisés. Chaque règle de linting que vous ajoutez est autonome, toute règle peut être activée ou désactivée. Chaque règle peut être définie comme un avertissement ou une erreur. Votre choix.

En utilisant ESLint, vous obtenez une personnalisation complète de l'apparence de votre guide de style.

Il existe actuellement 2 guides de style populaires :

* [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)
* [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript#table-of-contents)

J'ai personnellement utilisé le guide de style d'Airbnb. Cela m'a été recommandé par mon responsable technique dans mon ancienne entreprise lorsque je commençais ma carrière professionnelle, et cela a été l'actif le plus précieux à ma disposition.

Ce guide de style est activement maintenu — consultez leur [dépôt GitHub](https://github.com/airbnb/javascript). J'utiliserai les ensembles de règles inspirés par le guide de style d'Airbnb tout au long de ce tutoriel. Alors commençons.

Mettons d'abord à jour notre fichier `package.json` :

```json
{
  "name": "react-boiler-plate",
  "version": "1.0.0",
  "description": "A react boiler plate",
  "main": "src/index.js",
  "author": "Adeel Imran",
  "license": "MIT",
  "scripts": {
    "lint": "eslint --debug src/",
    "lint:write": "eslint --debug src/ --fix",
    "prettier": "prettier --write src/**/*.js"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*.(js|jsx)": ["npm run lint:write", "git add"]
  },
  "devDependencies": {
    "babel-eslint": "^8.2.3",
    "eslint": "^4.19.1",
    "eslint-config-airbnb": "^17.0.0",
    "eslint-config-jest-enzyme": "^6.0.2",
    "eslint-plugin-babel": "^5.1.0",
    "eslint-plugin-import": "^2.12.0",
    "eslint-plugin-jest": "^21.18.0",
    "eslint-plugin-jsx-a11y": "^6.0.3",
    "eslint-plugin-prettier": "^2.6.0",
    "eslint-plugin-react": "^7.9.1",
    "husky": "^1.1.2",
    "lint-staged": "^7.3.0",
    "prettier": "^1.14.3"
  }
}
```

Avant de continuer avec la configuration, je crois fermement que les gens devraient savoir ce qui entre dans leurs dépendances. Alors parlons de ce que fait chaque package, puis nous pourrons continuer avec les configurations.

`babel-eslint` : ce package vous permet d'utiliser le lint sur toutes les fonctionnalités de [Babel](https://babeljs.io/) facilement. Vous n'avez pas nécessairement besoin de ce plugin si vous n'utilisez pas [Flow](https://flow.org/) ou des fonctionnalités expérimentales qui ne sont pas encore supportées par ESLint.

`eslint` : c'est l'outil principal nécessaire pour linting votre code.

`eslint-config-airbnb` : ce package fournit toute la configuration ESLint d'Airbnb en tant que configuration partagée extensible, que vous pouvez modifier.

`eslint-plugin-babel` : un plugin compagnon `eslint` pour `babel-eslint`.
`babel-eslint` fait un excellent travail pour adapter `eslint` à l'utilisation avec Babel.

`eslint-plugin-import` : ce plugin vise à supporter le linting de la syntaxe `import/export` de `ES2015+ (ES6+)`, et à prévenir les problèmes de fautes de frappe dans les chemins de fichiers et les noms d'importation. [Lire plus](https://github.com/benmosher/eslint-plugin-import).

`eslint-plugin-jsx-a11y` : règles de linting en place pour les règles d'accessibilité sur les éléments JSX. Parce que **l'accessibilité est importante !**

`eslint-plugin-prettier` : cela aide ESLint à fonctionner en douceur avec Prettier. Ainsi, lorsque Prettier formate le code, il le fait en gardant à l'esprit nos règles ESLint.

`eslint-plugin-react` : règles de linting spécifiques à React pour ESLint.

Ce tutoriel ne parle pas beaucoup des tests unitaires pour [Jest/Enzyme](https://airbnb.io/enzyme/docs/guides/jest.html). Mais si vous les utilisez, ajoutons également des règles de linting pour eux :

`eslint-config-jest-enzyme` : cela aide avec les variables spécifiques à React et Enzyme qui sont globalisées. Cette configuration de lint permet à ESLint de connaître ces globaux et de ne pas avertir à leur sujet — comme les assertions `it` et `describe`.

`eslint-plugin-jest` : plugin ESLint pour Jest.

`husky` : plus d'informations à ce sujet plus tard dans la section automatisation.

`lint-staged` : plus d'informations à ce sujet plus tard dans la section automatisation.

Maintenant que nous avons une compréhension de base, commençons ;

Créez un fichier `.eslintrc.js` dans votre dossier racine `app/` :

```
module.exports = {
	env: {
		es6: true,
		browser: true,
		node: true,
	},
	extends: ['airbnb', 'plugin:jest/recommended', 'jest-enzyme'],
	plugins: [
		'babel',
		'import',
		'jsx-a11y',
		'react',
		'prettier',
	],
	parser: 'babel-eslint',
	parserOptions: {
		ecmaVersion: 6,
		sourceType: 'module',
		ecmaFeatures: {
			jsx: true
		}
	},
	rules: {
		'linebreak-style': 'off', // Ne fonctionne pas bien avec Windows.

		'arrow-parens': 'off', // Incompatible avec prettier
		'object-curly-newline': 'off', // Incompatible avec prettier
		'no-mixed-operators': 'off', // Incompatible avec prettier
		'arrow-body-style': 'off', // Pas à notre goût ?
		'function-paren-newline': 'off', // Incompatible avec prettier
		'no-plusplus': 'off',
		'space-before-function-paren': 0, // Incompatible avec prettier

		'max-len': ['error', 100, 2, { ignoreUrls: true, }], // airbnb permet certains cas particuliers
		'no-console': 'error', // airbnb utilise warn
		'no-alert': 'error', // airbnb utilise warn

		'no-param-reassign': 'off', // Pas à notre goût ?
		"radix": "off", // parseInt, parseFloat radix désactivé. Pas à mon goût.

		'react/require-default-props': 'off', // airbnb utilise error
		'react/forbid-prop-types': 'off', // airbnb utilise error
		'react/jsx-filename-extension': ['error', { extensions: ['.js'] }], // airbnb utilise .jsx

		'prefer-destructuring': 'off',

		'react/no-find-dom-node': 'off', // Je ne sais pas
		'react/no-did-mount-set-state': 'off',
		'react/no-unused-prop-types': 'off', // Toujours bogué
		'react/jsx-one-expression-per-line': 'off',

		"jsx-a11y/anchor-is-valid": ["error", { "components": ["Link"], "specialLink": ["to"] }],
		"jsx-a11y/label-has-for": [2, {
			"required": {
				"every": ["id"]
			}
		}], // pour l'erreur htmlFor de label imbriqué

		'prettier/prettier': ['error'],
	},
};
```

Ajoutez également un fichier `.eslintignore` dans votre répertoire racine `app/` :

```
/.git
/.vscode
node_modules
```

Commençons par discuter de ce que fait un fichier `.eslintrc.js`.

Décomposons-le :

```javascript
module.exports = { 
   env:{}, 
   extends: {}, 
   plugin: {}, 
   parser: {}, 
   parserOptions: {}, 
   rules: {},
};
```

* `env:` Un environnement définit des variables globales qui sont prédéfinies. Les environnements disponibles — dans notre cas, il s'agit de `es6`, `browser` et `node`.
`es6` activera toutes les fonctionnalités ECMAScript 6 sauf les modules (cela définit automatiquement l'option `ecmaVersion` du parser à 6).
`browser` ajoutera toutes les variables globales du navigateur telles que `Windows`.
`node` ajoutera les variables globales de Node et la portée de Node, telles que `global`. Vous pouvez [lire plus](https://eslint.org/docs/user-guide/configuring#specifying-environments) sur la spécification des environnements.
* `extends:` Un tableau de chaînes — chaque configuration supplémentaire étend les configurations précédentes.
Actuellement, nous utilisons les règles de linting de `airbnb` qui sont étendues à `jest` puis étendues à `jest-enzyme`.
* `plugins:` les plugins sont essentiellement des règles de linting que nous voulons utiliser.
Actuellement, nous utilisons `babel, import, jsx-a11y, react, prettier`, que j'ai tous expliqués ci-dessus.
* `parser:` Par défaut, ESLint utilise [Espree](https://github.com/eslint/espree), mais puisque nous utilisons `babel`, nous devons utiliser [Babel-ESLint](https://www.npmjs.com/package/babel-eslint).
* `parserOptions:` Lorsque nous changeons le parser par défaut de `Espree` à `babel-eslint`, nous devons spécifier `parserOptions` — c'est requis.
Dans les options, je dis à ESLint que `ecmaVersion` va lint la version `6`. Puisque nous écrivons notre code dans un module EcmaScript et non dans un `script`, nous spécifions `sourceType` comme `module`.
Puisque nous utilisons React qui apporte JSX, dans `ecmaFeatures`, je lui passe une option de `jsx` et la définis à `true`.
* `rules:` C'est la partie que j'aime le plus chez ESLint, la personnalisation.
Toutes les règles que nous avons étendues et ajoutées avec nos plugins, nous pouvons les changer ou les remplacer. `rules` est l'endroit où vous le faites. J'ai déjà mis des commentaires dans le Gist contre chaque règle et pour votre compréhension.

Maintenant que c'est clarifié, parlons de `.eslintignore`

`.eslintignore` prend une liste de chemins que nous ne voulons pas que ESLint lint. Ici, je spécifie seulement trois :

* `/.git` Je ne veux pas que mes fichiers liés à Git soient lintés.
* `/.vscode` Puisque j'utilise VS Code, cet éditeur vient avec sa propre configuration que vous pouvez définir pour chaque projet. Je ne veux pas que ma/mes configuration(s) soit/soient lintée(s). J'utilise VS Code parce qu'il est léger et open source.
* `node_modules` Je ne veux pas que mes dépendances soient lintées. Donc je l'ai ajouté à la liste.

Maintenant que nous avons terminé cela, parlons des nouveaux scripts ajoutés à notre `package.json`

```
"lint": "eslint --debug src/"
"lint:write": "eslint --debug src/ --fix"
```

* `$ yarn lint` en exécutant cette commande, il parcourra tous vos fichiers dans `src/` et vous donnera un journal détaillé dans chaque fichier où il trouve des erreurs, que vous pouvez ensuite corriger manuellement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yfvCg7YG_IpFFbZYzBv8IA.gif)
_exécution de **yarn lint | npm run lint**_

* `$ yarn lint:write` en exécutant la commande, il fera la même chose que ce que fait la commande ci-dessus. La seule addition est que s'il peut corriger une des erreurs qu'il voit, il va les corriger et essayer de supprimer autant de mauvaises odeurs de code que possible.

Si vous êtes bloqué, n'hésitez pas à jeter un œil au [**dépôt**](https://github.com/adeelibr/react-starter) pour cela.

C'était un peu chaotique et si vous avez suivi jusqu'à présent :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pi2nGW17A7cFXX2hc6apPA.gif)
_Le professeur Snape est fier de vous. Bon travail._

### Automatisons un peu plus

Jusqu'à présent, nous avons configuré `prettier` et `eslint`, mais chaque fois que nous devons exécuter un script. Faisons quelque chose à ce sujet.

* Formater et Linter le code en appuyant sur `ctrl+s` dans votre éditeur.
* Chaque fois que vous commitez votre code, exécutez automatiquement une pré-commande qui lint et formate votre code.

#### Formater et Linter le code à la sauvegarde

Pour cela, vous devez utiliser un éditeur comme [VS Code](https://code.visualstudio.com/) :

* Installez un plugin appelé extension ESLint.
[Téléchargez ici](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) ou appuyez sur `ctrl+shift+x` dans votre éditeur VS Code. Cela ouvrira le module d'extensions. Là, tapez `eslint`. Une liste de plugins apparaîtra. Installez celui de `Dirk Baeumer`. Une fois installé, appuyez sur le bouton `reload` pour redémarrer votre éditeur.

Une fois ce plugin installé, dans votre dossier racine `app/`, créez un dossier appelé `.vscode/` — le (point) est important dans le nom de fichier.

À l'intérieur du dossier, créez un fichier `settings.json` comme ci-dessous :

```json
{
  "editor.formatOnSave": false,
  "eslint.autoFixOnSave": true,
}
```

* `editor.formatOnSave` J'ai défini la valeur à `false` ici car je ne veux pas que la configuration par défaut de l'éditeur pour le format de fichier entre en conflit avec ESLint et Prettier.
* `eslint.autoFixOnSave` J'ai défini la valeur à `true` ici car je veux que le plugin installé fonctionne chaque fois que j'appuie sur sauvegarder. Puisque ESLint est configuré avec les configurations de Prettier, chaque fois que vous appuyez sur `sauvegarder`, il formatera et lintera votre code.

Une chose importante à noter ici est que lorsque vous exécutez le script
`yarn lint:write`, il lintera et embellira votre code en même temps.

Imaginez simplement si vous aviez une base de code de 20k lignes de code à auditer et à améliorer. Maintenant, imaginez le faire manuellement. Améliorer un code inconnu. Maintenant, imaginez le faire avec une seule commande. L'approche manuelle pourrait prendre 30 jours... tandis que l'approche automatique vous prendra 30 secondes.

Donc les scripts sont configurés, et chaque fois que vous appuyez sur `sauvegarder`, l'éditeur fera la magie pour vous pour ce fichier spécifique. Mais tout le monde dans votre équipe n'optera pas pour VS Code et c'est très bien. Alors automatisons un peu plus.

### Husky

#### Qu'est-ce que Husky ?

[Husky](https://github.com/typicode/husky) vous permet essentiellement de Git hook. Cela signifie que vous pouvez effectuer certaines actions lorsque vous êtes sur le point de commiter ou lorsque vous êtes sur le point de pousser du code vers une branche.

Tout ce que vous avez à faire est d'installer Husky :

```
yarn add --dev husky
```

et dans votre fichier `package.json`, ajoutez le snippet :

```
"husky": {    
   "hooks": {      
     "pre-commit": "YOUR_COMMAND_HERE", 
     "pre-push": "YOUR_COMMAND_HERE"   
   }  
},
```

Ainsi, chaque fois que vous commitez ou poussez, il exécutera un certain script ou commande — comme exécuter des cas de test ou formater votre code.

Vous pouvez lire plus sur Husky [ici](https://github.com/typicode/husky#install).

### Lint-staged

#### **_Qu'est-ce que Lint-staged ?_**

[Lint-staged](https://github.com/okonet/lint-staged) vous aide à exécuter des linters sur des fichiers staged, afin que du mauvais code ne soit pas poussé vers votre branche.

#### **_Pourquoi Lint-staged ?_**

Le linting a plus de sens lorsqu'il est exécuté avant de commiter votre code. En faisant cela, vous pouvez vous assurer qu'aucune erreur ne pénètre dans le dépôt et faire respecter le style de code. Mais exécuter un processus de lint sur un projet entier est lent et les résultats de linting peuvent être irrélevants. En fin de compte, vous ne voulez linter que les fichiers qui seront commités.

Ce projet contient un script qui exécutera des tâches shell arbitraires avec une liste de fichiers staged comme argument, filtrée par un motif glob spécifié. Vous pouvez [lire plus ici](https://github.com/okonet/lint-staged#why).

Tout ce que vous avez à faire est d'installer Lint-staged :

```
yarn add --dev lint-staged
```

puis dans votre fichier `package.json`, ajoutez ceci :

```
"lint-staged": {    
   "*.(js|jsx)": ["npm run lint:write", "git add"]  
},
```

Ce que cette commande fera, c'est exécuter la commande `lint:write` en premier, puis l'ajouter dans la zone de staging. Elle exécutera cette commande uniquement pour les fichiers `.js` et `.jsx`, mais vous pouvez faire de même pour d'autres fichiers si vous le souhaitez.

#### Avec Husky et Lint-staged combinés

Chaque fois que vous commitez votre code, avant de commiter votre code, il exécutera un script appelé `lint-staged` qui exécutera `npm run lint:write` qui lintera et formatera votre code — puis l'ajoutera à la zone de staging et ensuite committera. Cool, non ?!

Votre fichier `package.json` final devrait ressembler à ceci. Il s'agit du même snippet que j'ai partagé ci-dessus :

```json
{
  "name": "react-boiler-plate",
  "version": "1.0.0",
  "description": "A react boiler plate",
  "main": "src/index.js",
  "author": "Adeel Imran",
  "license": "MIT",
  "scripts": {
    "lint": "eslint --debug src/",
    "lint:write": "eslint --debug src/ --fix",
    "prettier": "prettier --write src/**/*.js"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*.(js|jsx)": ["npm run lint:write", "git add"]
  },
  "devDependencies": {
    "babel-eslint": "^8.2.3",
    "eslint": "^4.19.1",
    "eslint-config-airbnb": "^17.0.0",
    "eslint-config-jest-enzyme": "^6.0.2",
    "eslint-plugin-babel": "^5.1.0",
    "eslint-plugin-import": "^2.12.0",
    "eslint-plugin-jest": "^21.18.0",
    "eslint-plugin-jsx-a11y": "^6.0.3",
    "eslint-plugin-prettier": "^2.6.0",
    "eslint-plugin-react": "^7.9.1",
    "husky": "^1.1.2",
    "lint-staged": "^7.3.0",
    "prettier": "^1.14.3"
  }
}
```

Maintenant, chaque fois que vous faites ceci :

```
$ git add .$ git commit -m "some descriptive message here"
```

Il lintera et formatera votre code en fonction de toutes les règles mises dans le fichier `.eslintrc.js`. Avec cela, vous pouvez être sûr qu'aucun mauvais code ne sera jamais poussé en production.

Avec cette section conclue, vous avez maintenant `prettier`, `eslint` et `husky` intégrés dans votre base de code.

### Parlons de EditorConfig

Tout d'abord, créez un fichier `.editorconfig` dans votre dossier racine `app/`, et dans ce fichier, collez le code ci-dessous :

```
# EditorConfig est génial : http://EditorConfig.org

# fichier EditorConfig le plus haut
root = true

[*.md]
trim_trailing_whitespace = false

[*.js]
trim_trailing_whitespace = true

# Sauts de ligne de style Unix avec un saut de ligne à la fin de chaque fichier
[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
insert_final_newline = true
max_line_length = 100
```

#### **_Alors, qu'est-ce que EditorConfig ?_**

Tout le monde n'utilisera pas VS Code — et vous ne pouvez pas l'imposer, ni ne devriez-vous le faire. Afin de garder tout le monde sur la même page en termes de ce que les valeurs par défaut, comme `espace de tabulation` ou `fin de ligne`, devraient être, nous utilisons `.editorconfig`. Cela aide en fait à faire respecter certains ensembles de règles.

Voici la liste de tous les éditeurs qui supportent [EditorConfig](https://editorconfig.org/). La liste des éditeurs inclut Web storm, App code, Atom, eclipse, emacs, bbedit et bien d'autres.

La configuration ci-dessus fera ce qui suit :

* supprimer les espaces blancs de fin des fichiers `.md` et `.js`
* définir le style d'indentation à `espace` au lieu de `tabulation`
* taille d'indentation à `2`
* fin de ligne à `lf` afin que tout le monde, indépendamment de leur système d'exploitation, ait la même fin de ligne. [Lire plus ici](https://stackoverflow.com/questions/1552749/difference-between-cr-lf-lf-and-cr-line-break-types).
* il devrait y avoir une nouvelle ligne à la fin du fichier
* et la longueur maximale de ligne devrait être de `100` caractères

Avec toute cette configuration faite et en place, vous êtes maintenant prêt. Si vous voulez voir le [**code source**](https://github.com/adeelibr/react-starter-kit/) le voici.

Les pull requests sont également les bienvenues si vous pensez pouvoir améliorer quelque chose dans ce dépôt.

Si vous avez aimé mon article, vous devriez également consulter mon autre article : [**Comment combiner Webpack 4 et Babel 7 pour créer une application React fantastique**](https://medium.freecodecamp.org/how-to-combine-webpack-4-and-babel-7-to-create-a-fantastic-react-app-845797e036ff) dans lequel je parle de la configuration de Webpack et Babel pour React.