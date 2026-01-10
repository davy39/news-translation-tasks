---
title: Comment créer un tableau de scores de football en direct avec React, Vite et
  Vitest
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2023-04-13T20:41:33.000Z'
originalURL: https://freecodecamp.org/news/react-project-with-vite-and-vitest
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-13-at-5.15.35-PM.png
tags:
- name: React
  slug: react
- name: vite
  slug: vite
seo_title: Comment créer un tableau de scores de football en direct avec React, Vite
  et Vitest
seo_desc: 'Welcome to yet another tutorial where you will learn how to build a ⚽ scoreboard
  app in React. This time we will use Vite as our next generation frontend tooling
  and Vitest as a Vite-native unit testing framework.

  You will also learn how to leverage ...'
---

Bienvenue dans ce [tutoriel](https://www.mihailgaberov.com/) où vous apprendrez à créer une application de tableau de scores ⚽ en React. Cette fois, nous utiliserons Vite comme notre [outil de frontend de nouvelle génération](https://vitejs.dev/) et [Vitest](https://vitest.dev/) comme framework de test unitaire natif pour Vite.

Vous apprendrez également à utiliser les [hooks React](https://react.dev/learn/reusing-logic-with-custom-hooks), construits comme une abstraction des timeouts et intervalles de temps natifs de JavaScript. Pour le style de l'application, nous utiliserons les [modules CSS](https://github.com/css-modules/css-modules) avec [SASS](https://sass-lang.com/).

Voici ce que nous allons construire :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-04-at-09.11.31.png align="left")

*Tableau de scores de football en direct - écran des matchs en cours*

📢 Si vous souhaitez passer la lecture, 🔗 [ici](https://github.com/mihailgaberov/scoreboard) se trouve le dépôt GitHub, et voici le [démo](https://scoreboard-mihailgaberov.vercel.app/) en direct 📹.

## Qu'est-ce qu'un tableau de scores ?

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-04-at-11.58.35.png align="left")

*Tableau de scores de football*

Un tableau de scores en direct est un tableau de scores sportif numérique qui affiche automatiquement les scores et les données à la minute près d'un certain jeu – par exemple un match de football. Ainsi, il est beaucoup plus facile pour les utilisateurs de suivre le jeu, de faire des prédictions ou des paris, et ainsi de suite.

Notre application va refléter un tel tableau, mais dans le navigateur.

## Le Projet

Notre application a très peu de dépendances et plusieurs composants. Elle utilise également les timeouts et intervalles JavaScript pour simuler les mises à jour de scores en temps réel.

### ⚒️ Fonctionnalités de l'application

Avant de passer à la partie technique du tutoriel, parlons des fonctionnalités de l'application que nous allons implémenter.

Il est toujours préférable (si possible, bien sûr) d'avoir des exigences de projet claires avant d'écrire une seule ligne de code. Mais les personnes ayant une certaine expérience dans le monde de l'ingénierie et du développement logiciel savent que la réalité est souvent complètement différente.

La beauté de tels petits projets que vous construisez à des fins éducatives est exactement cela – vous avez la liberté de définir vos propres exigences et de les satisfaire de manière réalisable.

Voici donc le résumé des exigences/fonctionnalités :

**Tableau de scores de la Coupe du Monde de Football en direct** qui montre les matchs et les scores.

Le tableau prend en charge les opérations suivantes :

1. Démarrer un jeu. Lorsque le jeu commence, il doit capturer l'équipe à domicile et l'équipe à l'extérieur (avec un score initial de 0 - 0).

2. Terminer le jeu. Il supprimera un match du tableau de scores.

3. Mettre à jour le score. Recevoir le score de la paire. Lorsque l'équipe à domicile ou l'équipe à l'extérieur marque, il met à jour le score du jeu.

4. Obtenir un résumé des jeux par score total. Ces jeux avec le même score total seront retournés dans l'ordre du plus récemment ajouté à notre système.

✍️ Par exemple, si ce sont les données actuelles dans le système :

`a. Mexique - Canada : 0 - 5`  
`b. Espagne - Brésil : 10 – 2`  
`c. Allemagne - France : 2 – 2`  
`d. Uruguay - Italie : 6 – 6`  
`e. Argentine - Australie : 3 - 1`

Le résumé nous donnerait les informations suivantes :

`1. Uruguay 6 - Italie 6`  
`2. Espagne 10 - Brésil 2`  
`3. Mexique 0 - Canada 5`  
`4. Argentine 3 - Australie 1`  
`5. Allemagne 2 - France 2`

### ⚽ Structure du projet

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-04-at-15.08.38.png align="left")

*Structure du projet*

Permettez-moi de passer en revue chacun des fichiers et de donner une brève explication de ce qu'ils sont et pourquoi nous en avons besoin :

* [package.json](https://github.com/mihailgaberov/scoreboard/blob/main/package.json) – le fichier de configuration de chaque application Node.js, créé avec npm ou yarn, ou tout autre gestionnaire de paquets utilisant la même approche.

* [README.md](https://github.com/mihailgaberov/scoreboard/blob/main/README.md) – pas grand-chose à dire ici – c'est un simple fichier texte qui utilise Markdown et contient la description du projet, plus toute autre information que vous souhaitez y mettre.

* [vite.config.js](https://github.com/mihailgaberov/scoreboard/blob/main/vite.config.js) – le fichier de configuration principal que Vite utilise, que vous obtenez lorsque vous faites l'installation à partir de l'étape précédente. Le contenu de ce fichier par défaut ressemble à ceci :

```jsx
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// <https://vitejs.dev/config/>
export default defineConfig({
  plugins: [react()],
})
```

Mais dans mon cas, j'ai dû ajouter les configurations de `test` pour que nous puissions exécuter les tests. Vous en lirez plus à ce sujet plus tard dans l'article.

* [setupTests.js](https://github.com/mihailgaberov/scoreboard/blob/main/setupTests.js) – celui-ci est utilisé pour configurer les tests unitaires. Nous y mettons toutes les choses que nous aimerions avoir disponibles dans les tests que nous écrivons.

Par exemple, afin de pouvoir utiliser des clés uniques lors du rendu de plusieurs éléments ([parce que React en a besoin](https://react.dev/learn/rendering-lists#where-to-get-your-key)), j'utilise la méthode `randomUUID()` de l'interface [Crypto](https://developer.mozilla.org/en-US/docs/Web/API/Crypto) pour générer un UUID v4 en utilisant un générateur de nombres aléatoires cryptographiquement sécurisé. Et pour le rendre disponible dans mes tests, je dois l'ajouter ici, comme ceci :

```jsx
import { expect, afterEach } from 'vitest';
import { cleanup } from '@testing-library/react';
import matchers from '@testing-library/jest-dom/matchers';
import {randomUUID} from 'node:crypto';

// étend la méthode expect de Vitest avec des méthodes de react-testing-library
expect.extend(matchers);

// exécute un nettoyage après chaque cas de test (par exemple, effacer jsdom)
afterEach(() => {
    cleanup();
});

window.crypto.randomUUID = randomUUID;
```

* [yarn.lock](https://github.com/mihailgaberov/scoreboard/blob/main/yarn.lock) – ceci est généré automatiquement lors de l'exécution de l'installation de yarn et verrouille la version des paquets utilisés.

* [.gitignore](https://github.com/mihailgaberov/scoreboard/blob/main/.gitignore) – provient de l'installation de Vite. Ici, vous définissez les fichiers et dossiers que vous souhaitez que Git ignore, c'est-à-dire ne pas les commiter dans votre dépôt.

* [index.html](https://github.com/mihailgaberov/scoreboard/blob/main/index.html) – c'est le point d'entrée de l'application. C'est un simple document HTML qui contient quelques balises meta, et inclut le logo et le fichier de script principal.

* /src – contient quelques éléments différents dont nous devons discuter :

1. Tout d'abord, il contient le fichier [main.jsx](https://github.com/mihailgaberov/scoreboard/blob/main/src/main.jsx), où React et ReactDOM entrent en jeu. Nous chargeons également ici le fichier de styles par défaut dont j'ai parlé précédemment.

2. Il contient également [index.css](https://github.com/mihailgaberov/scoreboard/blob/main/src/index.css) que j'ai déjà expliqué.

3. Ensuite, nous avons [App.jsx](https://github.com/mihailgaberov/scoreboard/blob/main/src/App.jsx) où commence le code réel de notre application. Ce fichier peut être considéré comme le composant principal de notre application, car il contient toutes les parties 'internes' de notre application.

4. Ensuite, nous avons [app.module.scss](https://github.com/mihailgaberov/scoreboard/blob/main/src/app.module.scss) qui contient les styles pour le composant App, en utilisant la convention des modules CSS pour nommer les fichiers avec le préfixe 'module' et l'extension 'scss'.

5. Enfin, nous avons [App.test.jsx](https://github.com/mihailgaberov/scoreboard/blob/main/src/App.test.jsx) qui contient un simple test pour le composant App, en utilisant [Vitest](https://vitest.dev) comme framework de test.

### 🏗️ Composants

Permettez-moi de vous présenter rapidement chacun des composants de l'application. Ils sont situés dans le dossier [components](https://github.com/mihailgaberov/scoreboard/tree/main/src/components).

#### Contenu du dossier /components :

* [Footer](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/Footer) – explicite, contient la partie pied de page de l'application.

* [GameStatus](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/GameStatus) – utilisé pour montrer si un jeu a commencé, c'est-à-dire s'il est en cours de jeu.

* [Header](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/Header) – explicite, contient la partie en-tête de l'application.

* [MessageBoard](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/MessageBoard) – un petit composant utilisé pour afficher des messages textuels indiquant quand les jeux commencent ou si nous regardons l'écran « Résumé » ou les « Jeux en cours ».

* [Result](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/Result) – un autre petit composant montrant les scores des jeux.

* [Scoreboard](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/Scoreboard) – un composant *parent*, servant de conteneur qui maintient tous les petits composants en place.

* [ScoreboardGrid](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/ScoreboardsGrid) – c'est le composant le plus important de l'application, car il contient toute la logique liée aux temporisateurs. Il contient tous les composants enfants et est responsable de la transmission des données nécessaires via leurs props.

* [TeamView](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/TeamView) – un autre petit composant servant de représentation d'une équipe, qui montre le drapeau et le nom de l'équipe.

### ⏱️ Timeouts

Les timeouts – ou plus précisément les intervalles de temps – dans l'application sont implémentés à l'aide de plusieurs hooks React. Ils sont tous situés dans le dossier [hooks](https://github.com/mihailgaberov/scoreboard/tree/main/src/hooks). Je les ai empruntés à un homme très compétent et assez célèbre nommé Josh W Comeau. Je posterai les liens à la fin de l'article.

Donc, nous utilisons essentiellement trois hooks, un par type d'intervalle de temps ou de timeout dont nous avons besoin.

1. [useInterval](https://github.com/mihailgaberov/scoreboard/blob/main/src/hooks/useInterval.js) – ceci est basé sur la fonction JavaScript intégrée `setInterval` et est utilisé pour le compte à rebours initial, avant que les jeux ne commencent

2. [useRandomInterval](https://github.com/mihailgaberov/scoreboard/blob/main/src/hooks/useRandomInterval.js) – ceci est une version améliorée de la précédente, et elle est utilisée pour mettre à jour aléatoirement le score des jeux, ainsi que pour les démarrer et les arrêter aléatoirement

3. [useTimeout](https://github.com/mihailgaberov/scoreboard/blob/main/src/hooks/useTimeout.js) – ceci est basé sur la fonction JavaScript intégrée `setTimeout` et est utilisé pour décider quand arrêter le temps de jeu des jeux et commencer à les finaliser

## 🧑‍💻 Comment construire le projet

À ce stade, vous devriez avoir une compréhension décente de ce qu'est notre application et de la manière dont ses différentes parties sont assemblées.

Permettez-moi maintenant de vous guider, étape par étape, dès le début, et de vous montrer comment je l'ai construite. J'ajouterai des images lorsque cela sera nécessaire, afin que ce soit plus facile pour vous de suivre.

### 📋 Dépendances

Les dépendances que nous avons sont très peu nombreuses. En plus de Vite et Vitest, j'ai installé uniquement SASS et la React Testing Library. Voici à quoi ressemble mon fichier [package.json](https://github.com/mihailgaberov/scoreboard/blob/main/package.json) :

```jsx
{
  "name": "scoreboard",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "author": "Mihail Gaberov",
  "scripts": {
    "dev": "vite",
    "test": "vitest",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^14.0.0",
    "@types/react": "^18.0.28",
    "@types/react-dom": "^18.0.11",
    "@vitejs/plugin-react": "^3.1.0",
    "jsdom": "^21.1.1",
    "sass": "^1.59.3",
    "vite": "^4.2.0",
    "vitest": "^0.29.7"
  }
}
```

### 👨‍💻 Installation

Dans cette étape, je suppose que vous partez de zéro. Nous allons utiliser Vite pour échafauder le projet. Pour cela, vous devez avoir Node.js installé sur votre système – au moins la version 14..18. Je vous suggère de le mettre à jour vers la dernière version stable. Et comme gestionnaire de paquets, vous pouvez choisir soit [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) soit [yarn](https://classic.yarnpkg.com/lang/en/docs/install/). Dans mon cas, j'utilise yarn.

Dans votre terminal, exécutez la commande suivante :

```jsx
yarn create vite
```

Puis suivez les instructions.

Certains d'entre vous pourraient demander « Pourquoi Vite ? ». Voici un [petit éloge](https://cloudfour.com/thinks/in-praise-of-vite/) de Vite qui devrait répondre à cette question.

Après avoir fait l'installation, nous avons le squelette de base d'une application React sur lequel nous pouvons commencer à construire. Voici à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/default-vite-project.png align="left")

*Projet Vite par défaut*

📢 Lorsque je commence de tels projets, je supprime généralement ce qui s'y trouve par défaut. Cela signifie que je supprime les fichiers que je ne prévois pas d'utiliser, je nettoie App.jsx et je mets à jour le fichier index.html.

Une autre chose que vous avez peut-être déjà remarquée est que le seul fichier CSS pur que j'ai conservé est [index.css](https://github.com/mihailgaberov/scoreboard/blob/main/src/index.css). C'est l'un des fichiers qui vient par défaut de l'installation de Vite. Je l'ai conservé tel quel car il contient un style de base que je ne voulais pas déplacer ailleurs.

Après le nettoyage initial et l'ajout des fichiers pour le style et les tests de App.jsx, le projet ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/first-steps.png align="left")

*Premières étapes du projet dans App.jsx*

Sur la capture d'écran ci-dessus, vous pouvez voir à quoi ressemble le fichier App.jsx après mes modifications. J'ai placé des commentaires comme marqueurs pour les composants que je dois créer.

Nous sommes maintenant prêts à commencer à construire les composants en question. Habituellement, il existe plusieurs approches différentes que vous pouvez adopter lorsque vous décidez par où commencer. Dans ce cas, nous commencerons par le haut, créerons le composant d'en-tête, puis passerons au composant de tableau de scores, et enfin nous construirons le composant de pied de page.

Vous pourriez également décider de construire d'abord la partie essentielle de l'application, c'est-à-dire le tableau de scores, et à la fin d'ajouter le « chapeau » et les « chaussures ».

Mais dans tous les cas, ce que je recommande est de créer des composants vides pour chacun des marqueurs que nous avons placés, en fonction de l'idée que nous avons en tête de ce que sera notre application.

Habituellement, j'utilise quelque chose appelé « Live Templates » dans mon [IDE](https://www.jetbrains.com/webstorm/) (au cas où vous utiliseriez un IDE différent, je suis sûr qu'il existe une alternative) qui peut générer différents types de code de base.

Dans notre cas, je l'utilise pour générer des composants fonctionnels React vides. Cela s'avère très pratique à ce stade du processus de développement, car nous pouvons rapidement créer les composants de notre projet, en les laissant vides. Ensuite, nous pouvons commencer à les remplir de contenu.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/live-templates-webstorm.png align="left")

*Live Templates dans Webstorm*

![Image](https://www.freecodecamp.org/news/content/images/2023/04/generate-boilerplate.png align="left")

*Génération de code de base pour les composants que nous allons créer*

Et voici à quoi ressemble le résultat de ce qui précède :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/generated-boilerplate.png align="left")

*Code de base généré pour un composant fonctionnel dans React*

### 🧑‍💻 Comment construire l'en-tête

Pour que l'application ressemble davantage à une application réelle, j'ai décidé d'ajouter un petit logo dans la partie gauche de l'en-tête, et un titre à côté. Voyons à quoi cela ressemblera dans le navigateur, puis comment l'implémenter avec du code :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/header-1.png align="left")

*En-tête de l'application*

Tout d'abord, j'ai fait une recherche rapide sur Google et j'ai choisi une image appropriée (la coupe). Je me suis assuré de choisir un fichier SVG pour plusieurs raisons.

La première et la plus importante est la performance et l'ajustabilité qui en découlent. Et deuxièmement, dans les paramètres par défaut de Vite, il y a déjà un logo SVG ajouté. Donc la seule chose que vous devez faire est de remplacer celui existant par le vôtre. Et ensuite ajouter un peu de style si nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/replace-svg-logo.png align="left")

*Logo SVG*

Regardons maintenant le code de notre tout nouveau composant d'en-tête :

```jsx
import './header.module.scss'
const Header = () => {
    return (
        <header>
            <img src='./logo.svg' alt='Tableau de scores de la Coupe du Monde de la FIFA'/>
            <h2>Tableau de scores de la Coupe du Monde de la FIFA</h2>
        </header>
    );
};

export default Header
```

Si vous gardez le fichier de logo dans le dossier `public`, vous n'avez pas à vous soucier du chemin vers l'image. C'est géré par Vite et vous y faites référence comme indiqué dans le code ci-dessus. L'instruction d'importation au début applique tous les styles à l'en-tête qui le font ressembler à l'image.

```scss
header {
  display: flex;
  background-color: #fdbe11;
  justify-content: flex-start;
  align-items: center;

  img {
    width: 3rem;
    height: auto;
    margin: 1rem;
  }
}
```

Après avoir ajouté quelques tests, le contenu du dossier du composant ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/header-component-directory.png align="left")

*Dossier du composant Header*

J'ai mentionné au début de l'article que nous allons utiliser Vitest et React Testing Library pour écrire les tests unitaires/composants pour cette application. Voici à quoi ressemblent les tests pour l'en-tête :

```scss
import { render, screen } from '@testing-library/react'
import { beforeEach, describe, expect, it } from 'vitest'
import Header from "./index"

describe('Header', () => {
    beforeEach(() => {
        render(<Header />)
    })
    it('affiche correctement le titre de l\'application', async () => {
        expect(screen.getByText(/Tableau de scores de la Coupe du Monde de la FIFA/i)).toBeVisible()
    })

    it('affiche correctement le logo de l\'application', async () => {
        const logo = screen.getByAltText('Tableau de scores de la Coupe du Monde de la FIFA');
        expect(logo).toHaveAttribute('src', './logo.svg')
    })
})
```

Comme vous pouvez probablement le deviner en lisant les tests, ce que nous faisons ici est de vérifier le titre de l'application puis le logo que nous avons vu à gauche.

Félicitations 🎉 Vous venez de terminer l'implémentation du premier bloc de construction de votre application. Continuons maintenant avec la zone principale. C'est ici que se trouvera la fonctionnalité essentielle du tableau de scores.

### 🧑‍💻 Comment construire le tableau de scores

Le tableau de scores prend en charge deux écrans : l'un montrant les scores des jeux actuellement en cours, et un autre montrant un résumé des résultats finaux.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/current-games-screen.png align="left")

*Écran des jeux en cours*

![Image](https://www.freecodecamp.org/news/content/images/2023/04/summary-screen.png align="left")

*Écran de résumé*

Lorsque je vois ce type de conception de mise en page, je commence généralement à penser à une grille. Parce que, qu'est-ce qu'une grille si ce n'est que des lignes et des colonnes ?

Le langage CSS moderne prend en charge les systèmes de grille avec seulement quelques lignes de code, comme vous le verrez un peu plus tard dans cette section. Par exemple, pour obtenir ce résultat, j'ai utilisé les styles suivants :

```scss
.grid {
  list-style-type: none;
  margin: 1rem;
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}
```

Chaque fois que je suis sur le point d'implémenter une interface utilisateur comme celle-ci dans une bibliothèque basée sur des composants telle que React, j'ai tendance à la diviser mentalement en blocs séparés. Ceux-ci se transformeront en composants.

Permettez-moi de vous montrer visuellement ce que je veux dire par là :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/thinking-components.png align="left")

*Réflexion sur les composants - représentation visuelle*

J'espère que vous pouvez comprendre ce que je vous montre sur l'image ci-dessus.

C'est ainsi que je divise mentalement la mise en page de conception que nous avons en place en composants de représentation.

Après avoir défini les parties constitutives de notre application, il est temps de passer à l'étape suivante et de les implémenter en code.

Tout d'abord, nous avons besoin du composant `ScoreboardsGrid` qui contiendra tous les plus petits et contiendra la logique de gestion des différents événements basés sur le temps.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/scoreboards-grid-directory.png align="left")

*Dossier du composant ScoreboardsGrid*

Comme vous l'avez peut-être remarqué, en plus des fichiers habituels, nous en avons un autre ici - [ScoresReducer.js](https://github.com/mihailgaberov/scoreboard/blob/main/src/components/ScoreboardsGrid/ScoresReducer.js). C'est là que réside notre logique de réducteur. Il est responsable de la manipulation de l'état de l'application, en fonction des actions qui sont déclenchées. En d'autres termes, c'est là que nous mettons à jour le score lorsqu'une équipe marque, et aussi là où nous commençons et terminons les jeux.

Dans l'instruction de retour du composant, nous utilisons le reste des composants que nous avons définis précédemment.

```jsx
...
...
...
return (
        <>
            {timeElapsed === 0 ?
                <>
                    <MessageBoard message={getScoreBoardStateMessage()}/>
                    <div className={classes.grid}>
                        {gamesToRender?.map(pairScore => (
                            <Scoreboard
                                key={crypto.randomUUID()}
                                pairScore={pairScore}
                                status={getGameStatus(pairScore.startedGame)}/>))}
                    </div>
                </> :
                <MessageBoard message={`Les jeux vont commencer dans ${timeElapsed} secondes.`}/>
            }
        </>
    );
```

[Le reste du code](https://github.com/mihailgaberov/scoreboard/blob/main/src/components/ScoreboardsGrid/index.jsx) se compose de quelques méthodes auxiliaires, de méthodes `dispatch`, et de la logique pour démarrer et arrêter les temporisateurs.

À partir de là, les choses deviennent encore plus faciles. Nous allons simplement utiliser nos petits composants pour afficher différentes choses dans notre application de tableau de scores.

Par exemple, le composant `MessageBoard` est simplement un conteneur qui affiche de manière stylistique une chaîne de caractères, passée via ses props. Voici l'implémentation :

```jsx
import classes from "./message-board.module.scss";

const Index = ({ message }) => {
    return (
        <div className={classes.message}>
            {message}
        </div>
    );
};

export default Index;
```

Il en va de même pour les composants `[GameStatus](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/GameStatus)` et `[Result](https://github.com/mihailgaberov/scoreboard/tree/main/src/components/Result)`. La différence entre ces derniers est que `Result` reçoit deux arguments – le nom de chaque équipe dans un jeu – et les affiche avec un tiret ('-') au milieu. `GameStatus` affiche simplement ce que nous passons via ses props, qui s'avère être une chaîne de caractères indiquant qu'un jeu est en cours.

Le seul composant qui est un peu différent est `TeamView`, car il contient à la fois une image et du texte, représentant les équipes. Le code lui-même est loin d'être compliqué. Voyez par vous-même :

```jsx
import classes from "./team-view.module.scss";

const TeamView = ({teamData}) => {
    return (
        <div className={classes.team}>
            <img src={`https://flagcdn.com/${teamData.countryCode}.svg`} width="50" alt={`${teamData.name}`}/>
            <span>{teamData.name}</span>
        </div>
    );
};

export default TeamView;
```

Ici, j'ai utilisé une balise `img` HTML régulière, en définissant la largeur à l'aide du style en ligne. Le reste est assez simple.

Avec cela, notre travail de codage est plus ou moins terminé. Comme vous l'avez probablement vu, tous les composants ont des tests. Ceux-ci, dans la plupart des cas, sont simplement des vérifications pour voir si le composant est rendu correctement.

Peut-être que les tests les plus intéressants à discuter sont ceux que nous avons ajoutés pour le composant [ScoreboardGrid](https://github.com/mihailgaberov/scoreboard/blob/main/src/components/ScoreboardsGrid/index.jsx).

C'est parce que nous utilisons le support d'asynchronisme de [React Testing Library](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library#using-waitfor-to-wait-for-elements-that-can-be-queried-with-find) pour tester l'état du composant à différents moments. De cette manière, nous sommes capables de tester le tic initial du temporisateur, avant que les jeux ne commencent. Et après son expiration, nous pouvons l'utiliser pour vérifier que notre écran de jeux en cours est affiché correctement. Je colle le code ici aussi, pour une lecture plus facile.

```jsx
import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import ScoreboardsGrid from "./index"

describe('ScoreboardsGrid', () => {
    it('affiche correctement tous les tableaux de scores disponibles', async () => {
        render(<ScoreboardsGrid />)

        expect(await screen.findByText(/Les jeux vont commencer dans 3 secondes./i)).toBeVisible()
        expect(await screen.findByText(/Les jeux vont commencer dans 2 secondes./i)).toBeVisible()
        expect(await screen.findByText(/Les jeux vont commencer dans 1 secondes./i)).toBeVisible()
        expect(await screen.findByText(/Argentine/i)).toBeVisible()
        expect(await screen.findByText(/Australie/i)).toBeVisible()
        expect(await screen.findByText(/Espagne/i)).toBeVisible()
        expect(await screen.findByText(/Brésil/i)).toBeVisible()
    })
})
```

Après avoir terminé l'implémentation de l'ensemble de l'application et avoir pris une tasse de ☕ ou un verre de 🥃, il est temps de penser aux améliorations possibles.

Par exemple, si nous avons plus de temps pour travailler sur ce projet, que pourrions-nous ajouter ou changer pour en faire une application de tableau de scores encore meilleure ?

### 🧑‍💻 Comment construire le pied de page

Pour donner à l'application un aspect plus complet, j'ai décidé d'ajouter également un composant de pied de page. Voici à quoi il ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/footer-component.png align="left")

*Composant de pied de page*

Son implémentation est également assez simple. Nous avons deux liens vers des plateformes sociales et un peu de texte de copyright. Voici comment je l'ai codé :

```jsx
import classes from "./footer.module.scss";
import packageJson from '../../../package.json';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
      <footer className={classes.footer} data-cy="footer">
        <ul>
          <li className={classes.footerLinks}>
            <a
                href="<https://twitter.com/mihailgaberov>"
                target="_blank"
                rel="noopener noreferrer"
                data-cy="twitterLink"
            >
              twitter
            </a>{" 