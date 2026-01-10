---
title: Tutoriel React + Ink CLI – Comment créer une application en ligne de commande
  pour navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-29T18:41:08.000Z'
originalURL: https://freecodecamp.org/news/react-js-ink-cli-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/freehero.png
tags:
- name: api
  slug: api
- name: command line
  slug: command-line
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: React
  slug: react
seo_title: Tutoriel React + Ink CLI – Comment créer une application en ligne de commande
  pour navigateur
seo_desc: "By Amazing Enyichi Agu\nReact is a popular front-end JavaScript development\
  \ library. It ranks #1 in awareness and usage according to the State Of JS 2021\
  \ survey. \nThis means that a majority of JavaScript developers likely are aware\
  \ of or use React. \nE..."
---

Par Amazing Enyichi Agu

React est une bibliothèque populaire de développement JavaScript front-end. Elle se classe #1 en termes de notoriété et d'utilisation selon l'enquête [State Of JS 2021](https://2021.stateofjs.com/en-US/libraries/front-end-frameworks/).

Cela signifie qu'une majorité de développeurs JavaScript connaissent probablement ou utilisent React.

Même si React est populaire pour construire des interfaces utilisateur (UI) d'applications web, vous pouvez également utiliser la bibliothèque principale React pour d'autres choses. En fait, la bibliothèque `[react-dom](https://reactjs.org/docs/react-dom.html)` est ce qui rend l'UI sur une page web – pas React lui-même. React est plus comme un moteur qui peut être porté dans n'importe quel environnement.

Une des raisons pour lesquelles les développeurs aiment React est son approche de la construction des interfaces utilisateur. Vous n'avez qu'à décrire à quoi l'interface devrait ressembler et le moteur React s'occupe du placement et des changements sur la page.

Il existe certaines bibliothèques qui utilisent React pour aider les développeurs à créer d'autres types d'applications en dehors des applications web. Elles incluent :

* [React 360](https://github.com/facebookarchive/react-360) : Pour construire des applications de réalité virtuelle 3D
* [React Desktop](https://github.com/gabrielbull/react-desktop) : Pour construire des applications de bureau
* [React Native](https://github.com/facebook/react-native) : Pour construire des applications mobiles
* [Ink](https://github.com/vadimdemedes/ink) : Pour construire des applications en ligne de commande

Dans ce tutoriel, nous allons explorer les interfaces en ligne de commande. Nous allons également construire une application qui affiche les prix en direct de quelques cryptomonnaies et tokens sélectionnés. Pour obtenir les prix des tokens, nous utiliserons l'API [CoinGecko](https://www.coingecko.com/en/api).

Une version fonctionnelle du projet peut être trouvée [ici sur GitHub](https://github.com/enyichiaagu/crypto-cli).

**NOTE :** Cet article suppose que vous pouvez utiliser React pour construire des applications web front-end basiques. Si ce n'est pas le cas, voici un [cours freeCodeCamp sur React JS](https://www.freecodecamp.org/news/free-react-course-2022/). L'article suppose également que vous pouvez consommer des API REST et connaître les commandes de base de la ligne de commande, car celles-ci ne sont pas couvertes dans cet article.

Très bien, commençons.

## Qu'est-ce qu'une interface en ligne de commande (CLI) ?

Une interface en ligne de commande est un moyen d'interagir avec un ordinateur via du texte. Elle fonctionne en tapant des commandes spéciales dans un prompt de commande.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/command.PNG)
_Interface en ligne de commande dans le système d'exploitation Windows_

C'était la manière dont les développeurs interagissaient avec les ordinateurs avant la création des [interfaces graphiques (GUI)](https://en.wikipedia.org/wiki/Graphical_user_interface). Les interfaces en ligne de commande sont toujours utiles pour [automatiser des tâches](https://opensource.com/article/19/12/automation-bash-scripts) et dans le développement logiciel en général.

## Qu'est-ce qu'Ink ?

[Ink](https://github.com/vadimdemedes/ink) est une bibliothèque JavaScript qui apporte React à la ligne de commande. Elle aide à développer des applications CLI en utilisant le concept d'éléments d'interface utilisateur basés sur des composants.

Ink vous permet d'utiliser toutes les fonctionnalités de React, y compris les composants basés sur des classes, les méthodes de cycle de vie, les composants fonctionnels, les hooks, et ainsi de suite pour construire des outils en ligne de commande.

La bibliothèque `ink` dispose également de plugins appelés [Useful Components](https://github.com/vadimdemedes/ink#useful-components). Ces composants utiles ne sont pas intégrés à la bibliothèque `ink`, mais sont des composants personnalisés construits par d'autres développeurs que vous pouvez importer dans un projet Ink.

## Comment installer Ink

Il existe deux façons d'installer Ink. Elles sont :

* [Installation manuelle d'Ink avec Babel](https://github.com/vadimdemedes/ink#getting-started)
* Utilisation de la commande `create-ink-app`

Dans cet article, nous utiliserons la méthode `create-ink-app` pour démarrer rapidement un projet Ink.

Sur la ligne de commande, naviguez jusqu'au dossier ou répertoire où vous souhaitez héberger votre projet ink, puis exécutez la commande suivante :

```bash
npx create-ink-app crypto-cli
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/install-1.PNG)
_Installation d'Ink_

Cette commande installe les fichiers nécessaires pour construire un projet Ink à l'intérieur du dossier où nous avons exécuté la commande. Dans notre cas, le dossier et le nom du projet sont les mêmes ( `crypto-cli`).

`create-ink-app` génère également une commande exécutable pour notre projet afin que nous puissions exécuter notre application en appelant son nom sur la CLI.

Avec cela, Ink 3 (qui est la dernière version d'Ink au moment de la rédaction de cet article) a été installé et nous sommes prêts à commencer à construire des applications en ligne de commande.

Lorsque nous exécutons la commande `crypto-cli`, nous obtenons cette sortie.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/hello.PNG)
_Sortie de l'exécution de `crypto-cli`_

Pourquoi avons-nous cette sortie ? Explorons les fichiers installés par `create-ink-app`.

## Examen des fichiers installés par Ink

La structure des fichiers du projet ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/files.PNG)
_Fichiers et dossiers fournis par create-ink-app_

À quoi servent ces fichiers et ce dossier ?

* `node_modules` : ce dossier contient tous les packages nécessaires au bon fonctionnement de notre application. Les packages incluent `react` et `ink`, mais aussi les dépendances de `react` et `ink` si elles existent. `node-modules` inclut également des packages que les créateurs de `ink` ont jugés utiles pour une bonne expérience de développement.
* `.editor-config` : ce fichier aide à maintenir la cohérence du code. Beaucoup de développeurs peuvent travailler sur ce projet avec différents IDE. Afin de s'assurer que le style de codage est le même, vous pouvez utiliser `.editor-config`. Vous pouvez trouver plus d'informations à ce sujet [ici](https://editorconfig.org/).
* `.gitattributes` : nous l'utiliserons pour configurer les attributs de nos fichiers qui seront utilisés par le programme de contrôle de version [Git](https://www.freecodecamp.org/news/what-is-git-learn-git-version-control/). Vous pouvez trouver plus d'informations [ici](https://git-scm.com/docs/gitattributes). Nous n'avons pas besoin d'ajouter ou de supprimer quoi que ce soit dans ce fichier pour ce projet.
* `cli.js` : dans ce fichier, nous utiliserons `ink` pour rendre notre application.
* `package-lock.json` : nous l'utilisons pour verrouiller les dépendances de notre application à une version particulière afin que d'autres puissent reproduire notre projet facilement n'importe où et n'importe quand.
* `package.json` : contient les métadonnées de notre application, y compris le nom, la version et les dépendances.
* `readme.md` : un fichier readme en markdown pour notre projet.
* `test.js` : pour écrire des tests dans notre application. Nous n'éditerons pas ce fichier dans notre projet.
* `ui.js` : ceci est synonyme de `App.js` pour le développement web front-end avec React. Il importe et contient tous les composants que notre projet aura.

Un coup d'œil dans le `package.json` nous montre les dépendances que nous avons installées :

```json
...,
"dependencies": {
    "import-jsx": "^4.0.1",
    "ink": "^3.2.0",
    "meow": "^9.0.0",
    "react": "^17.0.2"
},
...
```

Vous n'êtes peut-être pas familier avec `import-jsx` et `meow`. Voyons ce qu'ils font.

* `import-jsx` : vous utilisez cette bibliothèque pour importer et transpiler des fichiers JSX dans `ink`.
* `meow` : les commandes CLI acceptent des arguments. `meow` nous aide à implémenter cela dans `ink`.

Assez parlé. Construisons.

## Comment construire l'application CLI

Dans ce tutoriel, comme je l'ai mentionné précédemment, nous allons construire une application qui affiche les prix de certaines cryptomonnaies et tokens en utilisant l'API [CoinGecko](https://www.coingecko.com/en/api).

### Comment créer l'en-tête

Nous allons importer un package npm appelé `ink-big-text`. C'est l'un des "composants utiles" que fournit Ink. Nous l'utiliserons pour créer un grand en-tête dans la ligne de commande.

Nous allons également installer `ink-gradient` pour embellir notre en-tête. C'est un autre "composant utile" que fournit Ink.

```bash
npm install ink-big-text ink-gradient
```

Ensuite, nous allons éditer notre `ui.js` qui doit contenir tous nos composants.

```javascript
// ui.js

const React = require('react');
const Gradient = require('ink-gradient');
const BigText = require('ink-big-text');

const App = () => (
	<Gradient name="summer">
		<BigText text="crypto cli" align='center' font='chrome'/>
	</Gradient>
);

module.exports = App;

```

Et le code se traduit par cet en-tête magnifique lorsque nous exécutons `crypto-cli`.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/header.PNG)
_Sortie de l'en-tête_

### Comment afficher nos données

Pour afficher nos données, nous devons créer un élément `Box` qui les organise sous forme de tableau. `Box` fonctionne comme un conteneur de `display: flex;` sur le web. Vous le stylez comme un élément Flexbox.

Avant de récupérer les données de CoinGecko, nous allons créer des données fictives pour l'instant. Un fichier `data.json` à l'intérieur de `src` contiendra nos données fictives. Vous pouvez trouver les données fictives [ici](https://github.com/enyichiaagu/crypto-cli/blob/main/data.json).

Ensuite, nous allons créer un dossier appelé `components` à l'intérieur du dossier `src`. Nous allons également créer un fichier appelé `Table.js` à l'intérieur du dossier `components`.

Le code suivant va ensuite dans `Table.js` :

```javascript
// Table.js

const React = require('react');

const { useState, useEffect } = React;
// Déstructuration de useState et useEffect de React

const { Box, Text, Newline } = require('ink');
// Déstructuration des composants dont nous avons besoin depuis ink

const cryptoData = require('../data.json');
// Récupération des données fictives

const Table = () => {

    const [data, setData] = useState([]);

    useEffect(()=>{
        setData(cryptoData);
    });

    return (
        <Box borderStyle='single' padding={2} flexDirection='column'>
            <Box>
                <Box width='25%'><Text>COIN</Text></Box>
                <Box width='25%'><Text>PRIX (USD)</Text></Box>
                <Box width='25%'><Text>CHANGEMENT 24 HEURES</Text></Box>
                <Box width='25%'><Text>PLUS HAUT HISTORIQUE</Text></Box>
            </Box>
            <Newline/>
            {
                data.map(({id, name, current_price, price_change_percentage_24h, ath}) => (
                    <Box key={id}>
                        <Box width='25%'><Text>{name}</Text></Box>
                        <Box width='25%'><Text>{current_price}</Text></Box>
                        <Box width='25%'><Text>{price_change_percentage_24h}</Text></Box>
                        <Box width='25%'><Text>{ath}</Text></Box>
                    </Box>
                ))
            }
        </Box>
    )
}

module.exports = Table;
```

Maintenant, nous allons importer le composant Table dans notre application.

```javascript
// ui.js

const React = require('react');
const Gradient = require('ink-gradient');
const BigText = require('ink-big-text');
const importJsx = require('import-jsx');
const Table = importJsx('./components/Table')

const App = () => (
	<>
		<Gradient name="summer">
			<BigText 
				text="crypto cli" 
				align='center' 
				font='chrome'
			/>
		</Gradient>
		<Table/>
	</>
);

module.exports = App;
(peut-être, supprimer le 'use strict')
```

L'exécution de `crypto-cli` donnera ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/output.png)
_Sortie utilisant des données fictives_

J'aime avoir une certaine décoration dans mon application CLI. Nous allons donc utiliser les couleurs que `ink` nous fournit.

```javascript
// Table.js

const React = require('react');

const { useState, useEffect } = React;

const { Box, Text, Newline } = require('ink');

const cryptoData = require('../data.json');

const Table = () => {

    const [data, setData] = useState([]);

    useEffect(()=>{
        setData(cryptoData);
    })

    return (
        <Box borderStyle='single' padding={2} flexDirection='column'>
            <Box>
                <Box width='25%'><Text>COIN</Text></Box>
                <Box width='25%'><Text>PRIX ACTUEL (USD)</Text></Box>
                <Box width='25%'><Text>CHANGEMENT 24 HEURES</Text></Box>
                <Box width='25%'><Text>PLUS HAUT HISTORIQUE</Text></Box>
            </Box>
            <Newline/>
            {
                data.map(({id, name, current_price, price_change_percentage_24h, ath}) => (
                    <Box key={id}>
                        <Box width='25%'>
                            <Text>{name}</Text>
                        </Box>
                        <Box width='25%'>
                            <Text color='cyan'>{'$' + current_price.toLocaleString()}</Text>
                        </Box>
                        <Box width='25%'>
                            <Text backgroundColor={Math.sign(price_change_percentage_24h) < 0 ? 'red' : 'green'}>
                                {price_change_percentage_24h.toFixed(2) + '%'}
                            </Text>
                        </Box>
                        <Box width='25%'>
                            <Text color='green'>{'$' + ath.toLocaleString()}</Text>
                        </Box>
                    </Box>
                ))
            }
        </Box>
    )
}

module.exports = Table;
```

Pour être clair, afin d'ajouter de la couleur aux composants de texte dans `ink`, nous avons utilisé la prop (attribut) `color`. Afin d'ajouter une couleur de fond, nous avons utilisé l'attribut `backgroundColor`. Ensuite, nous avons ajouté une logique qui vérifie si le changement sur 24 heures était négatif ou positif.

Si le changement était positif, nous nous sommes assurés que la couleur de fond était verte, sinon la couleur de fond sera rouge.

Lorsque nous exécutons `crypto-cli`, nous avons la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/colored.png)
_Sortie après ajout de styles_

Et la négation manuelle de la valeur pour la deuxième valeur `CHANGEMENT 24 HEURES` dans `data.json` produit la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/negate.PNG)
_Sortie après négation d'une valeur_

### Comment récupérer les données de l'API CoinGecko

Cette étape consiste à récupérer les données réelles de l'API CoinGecko. Voici les étapes que nous devons suivre :

* Allez sur [https://www.coingecko.com/en/api/documentation](https://www.coingecko.com/en/api/documentation)

![Image](https://www.freecodecamp.org/news/content/images/2022/06/coingecko.PNG)
_Page de l'API CoinGecko_

* Naviguez jusqu'à la section "coins" et cliquez sur `/coins/markets`

![Image](https://www.freecodecamp.org/news/content/images/2022/06/coins.PNG)
_navigation vers /coins/markets_

* Cliquez sur le bouton "Try it out".
* Saisissez "usd" comme `vs_currency`. Saisissez également l'`id` de vos cryptomonnaies et tokens préférés (j'ai utilisé bitcoin, litecoin, matic-network, ethereum, tether, binancecoin, solana, aave, cardano et tron). N'oubliez pas de ne pas ajouter d'espace lors de la saisie des identifiants des pièces.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/vs.PNG)
_Valeurs du formulaire de saisie_

* Cliquez sur le bouton execute
* Copiez le lien qu'il génère. Pour moi, voici le lien que j'utiliserai pour effectuer mes appels API. Le lien dépend des cryptomonnaies ou tokens que vous avez sélectionnés.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/gecko-link.PNG)
_Copiez le lien mis en évidence_

```
https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Clitecoin%2Cmatic-network%2Cethereum%2Ctether%2Cbinancecoin%2Csolana%2Caave%2Ccardano%2Ctron&order=market_cap_desc&per_page=100&page=1&sparkline=false
```

Nous allons maintenant passer à notre `Table.js` et effectuer l'appel API.

Installez `[axios](https://github.com/axios/axios)` qui est une bibliothèque npm utile pour récupérer les données de l'API.

```bash
npm install axios
```

Et ensuite, en utilisant `axios`, nous récupérons nos données.

```javascript
const React = require('react')
const { useState, useEffect } = React;
const { Box, Text, Newline } = require('ink')
const axios = require('axios')

const url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Clitecoin%2Cmatic-network%2Cethereum%2Ctether%2Cbinancecoin%2Csolana%2Caave%2Ccardano%2Ctron&order=market_cap_desc&per_page=100&page=1&sparkline=false'

const Table = () => {

    const [data, setData] = useState([])

    useEffect(()=>{
        axios.get(url)
        .then(response => setData(response.data))
        .catch(e => console.log(e))
    },[])
    // Récupération des données et interception des erreurs possibles

    return (
        <Box borderStyle='single' padding={2}>
            {
                data.length === 0 ?
                <Box>
                    <Text>Chargement ...</Text>
                </Box> :
                <Box flexDirection='column'>
                    <Box>
                        <Box width='25%'><Text>COIN</Text></Box>
                        <Box width='25%'><Text>PRIX ACTUEL (USD)</Text></Box>
                        <Box width='25%'><Text>CHANGEMENT 24 HEURES</Text></Box>
                        <Box width='25%'><Text>PLUS HAUT HISTORIQUE</Text></Box>
                    </Box>
                    <Newline/>
                    {
                        data.map(({id, name, current_price, price_change_percentage_24h, ath}) => (
                            <Box key={id}>
                                <Box width='25%'>
                                    <Text>{name}</Text>
                                </Box>
                                <Box width='25%'>
                                    <Text color='cyan'>{'$' + current_price.toLocaleString()}</Text>
                                </Box>
                                <Box width='25%'>
                                    <Text backgroundColor={Math.sign(price_change_percentage_24h) < 0 ? 'red' : 'green'}>
                                        {price_change_percentage_24h.toFixed(2) + '%'}
                                    </Text>
                                </Box>
                                <Box width='25%'>
                                    <Text color='green'>{'$' + ath.toLocaleString()}</Text>
                                </Box>
                            </Box>
                        ))
                    }
                </Box>
            }
        </Box>
    )
}

module.exports = Table;

```

Et avec les pièces que nous avons sélectionnées, nous devrions voir la sortie suivante (avec des valeurs probablement différentes car le marché des cryptomonnaies est volatile) :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/display.PNG)
_Sortie finale_

## Conclusion

Dans ce tutoriel, nous avons appris comment construire une application en ligne de commande avec React et Ink.

Nous avons également utilisé l'API CoinGecko et Axios pour récupérer nos données.

Ink offre plus de composants et vous pouvez les combiner de plusieurs manières pour créer des programmes en ligne de commande vraiment utiles.

Merci d'avoir lu et je vous retrouverai bientôt.