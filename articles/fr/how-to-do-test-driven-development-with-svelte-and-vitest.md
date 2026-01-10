---
title: Comment faire du développement piloté par les tests avec Svelte et Vitest –
  Un tutoriel basé sur un projet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-19T17:20:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-do-test-driven-development-with-svelte-and-vitest
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/SvelteVitestTDDPoster.png
tags:
- name: Svelte
  slug: svelte
- name: TDD (Test-driven development)
  slug: tdd
- name: test driven development
  slug: test-driven-development
- name: vite
  slug: vite
seo_title: Comment faire du développement piloté par les tests avec Svelte et Vitest
  – Un tutoriel basé sur un projet
seo_desc: "By Sriram Thiagarajan\nTest Driven Development (TDD) is one of the best\
  \ ways to make sure your code is high quality and works like it's supposed to work.\
  \ It can also help you create reliable builds during continuous deployments. \n\
  In this post, we will..."
---

Par Sriram Thiagarajan

Le développement piloté par les tests (TDD) est l'une des meilleures façons de s'assurer que votre code est de haute qualité et fonctionne comme prévu. Il peut également vous aider à créer des builds fiables lors des déploiements continus. 

Dans cet article, nous allons apprendre à créer une application Svelte en utilisant les méthodes TDD.

## Ce que nous allons construire

Nous allons construire un composant d'onglets verticaux où nous pourrons basculer entre trois onglets. Nous allons construire ce composant en écrivant d'abord des cas de test, puis en développant la fonctionnalité du composant pour rendre les tests plus efficaces.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/FinalComponent-1.png)
_Implémentation finale_

## Prérequis

Je vais expliquer toutes les étapes nécessaires pour créer une application et vous pouvez suivre le code. Il est idéal d'avoir des connaissances de base en programmation et des connaissances fondamentales en HTML et CSS pour ce tutoriel.

De plus, vous devrez avoir Node.js installé. Vous pouvez [voir comment faire ici](https://nodejs.org/en/) si vous ne l'avez pas déjà.

## Qu'est-ce que le développement piloté par les tests ?

L'idée de base du développement piloté par les tests, ou TDD, est d'écrire le test avant d'implémenter la fonctionnalité réelle. Cela vous aide à déterminer clairement ce que vous développez et comment cela fonctionne. 

Vous regardez d'abord le test échouer, puis vous écrivez le code pour le faire passer. Cela garantit qu'il n'y a pas de tests faux positifs dans votre code.

Le TDD est une méthodologie que vous pouvez appliquer à n'importe quel langage de programmation. Il est plus courant lors du développement d'applications backend qui contiennent une logique métier que vous pouvez facilement tester. 

La bonne nouvelle est que vous pouvez appliquer des techniques similaires pour tester vos applications front-end également.

## Les trois étapes du TDD

Les trois étapes du TDD sont :

1. Étape rouge – Écrire le test et le voir échouer
2. Étape verte – Écrire le code minimum requis pour faire passer le test
3. Refactorisation – Nettoyer et refactoriser le code pour le rendre plus robuste

![Image](https://www.freecodecamp.org/news/content/images/2022/09/TDDStages.png)
_Trois étapes du TDD_

## Qu'est-ce que Vitest ?

Vitest est un framework de test en pleine croissance qui offre des fonctionnalités similaires à Jest. 

Puisque nous utilisons Vite comme outil de build pour Svelte dans ce tutoriel, Vitest s'intègre très bien avec Vite et offre un environnement de test similaire sans nécessiter de configuration supplémentaire.

## Comment créer une application Svelte

Nous allons créer une application Svelte en utilisant Vite comme outil de build. Vous pouvez le faire avec cette commande :

```
npm create vite@latest

```

Cela créera un nouveau projet, et vous pouvez suivre les étapes ci-dessous pour créer et configurer le projet :

1. Entrez le nom du projet. Cela créera également un nouveau dossier avec le nom du projet. Dans cet exemple, j'ajouterai le nom du projet comme `svelte-tdd-vitest`.
2. Vous pouvez sélectionner le framework à l'étape suivante. Choisissons `svelte` comme framework.
3. Ensuite, vous pouvez entrer la variante du framework. Nous pouvons choisir la variante `TypeScript` pour cet article. Si vous n'êtes pas à l'aise avec TypeScript, vous pouvez également choisir `JavaScript` dans cette option.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/ProjectInit.png)
_Initialiser le projet Svelte avec Vite_

Vous pouvez ensuite suivre les étapes utiles fournies dans le terminal pour installer les dépendances et démarrer l'application. Exécutez la commande suivante :

```
cd svelte-tdd-vitest
npm install
npm run dev
```

`npm install` installera les dépendances du projet. 

`npm run dev` démarrera le serveur de développement. Vous devriez voir l'application s'exécuter dans le port spécifié dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/ViteServerStartCmd.png)
_Serveur Vite démarré avec npm run dev_

Félicitations, vous pouvez maintenant voir l'application de démarrage s'exécuter dans votre navigateur. Vous pouvez ouvrir le projet dans votre éditeur de code préféré et commencer à travailler.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/SvelteViteStarter.png)

## Comment configurer Vitest

Vous pouvez ajouter Vitest au projet dès maintenant en tant que dépendance de développement. Cela signifie que Vitest ne sera pas inclus dans la build de production de l'application puisque vous exécuterez les tests dans votre environnement local.

```
npm install -D vitest
```

Vitest peut lire la configuration de Vite dans le fichier `vite.config.js` et préparer l'environnement de test similaire à l'environnement de build. Cela rend les tests plus fiables. Vous pouvez donc réutiliser le fichier de configuration Vite et ajouter plus d'options pour la configuration de Vitest.

Vous pouvez également remplacer la configuration pour Vitest en créant un nouveau fichier appelé `vitest.config.js` à la racine du projet. Créez donc un nouveau fichier appelé `vitest.config.js` :

```javascript
import { defineConfig } from 'vitest/config'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  plugins: [
    svelte({ hot: !process.env.VITEST }),
  ],
  test: {
    environment: 'jsdom',
  }
})

```

Il y a quelques configurations que nous ajoutons au fichier :

1. Nous désactivons le rechargement à chaud des modules Svelte lorsque les tests sont en cours d'exécution. 
2. Nous définissons l'environnement pour l'exécution des tests comme `jsdom`. Cela aide à simuler l'API DOM et à exécuter les tests de manière fiable.

Pour utiliser `jsdom`, vous devez l'ajouter en tant que dépendance de développement. Installez donc ce package en utilisant le terminal.

```
npm install -D jsdom
```

Après l'installation, ajoutons quelques scripts au fichier `package.json` pour démarrer le test Vitest à partir de la ligne de commande `npm` :

```json
"scripts": {
	...
	"test": "vitest",
    	"coverage": "vitest run --coverage"
}
```

## Comment créer le premier test

Vous avez maintenant tout ce qu'il faut pour écrire votre premier test. Créez un nouveau fichier appelé `sample.spec.ts` dans le répertoire `lib`.

```javascript
import {describe, test, expect } from 'vitest';

describe("Fichier d'exemple", () => {
    test("Test d'exemple", () => {
        expect(1 + 3).equal(4);
    });
});


```

Décomposons les différentes fonctions utilisées pour créer ce fichier de test :

1. `describe` – vous utilisez cela pour regrouper des tests similaires et benchmarker les tests lors de la génération de vos rapports. Il prend un nom et une fonction qui contient le groupe de tests.
2. `test` – Représente un seul test. Il peut contenir plusieurs attentes. Il est créé en passant un nom de test et la fonction pour exécuter le test.
3. `expect` – Représente l'expression que vous testez.

Il existe plusieurs façons différentes d'écrire votre test en fonction de ce que vous testez. Vous pouvez consulter l'API complète pour Vitest dans la [référence officielle de l'API](https://vitest.dev/api/).

Exécutons le test en utilisant la commande npm suivante :

```
npm run test
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/NpmRunFirstTest.png)
_Exécution du test_

## Comment ajouter la configuration globale des tests

Vous allez utiliser les fonctions `describe`, `test` et `expect` dans de nombreux fichiers de test, et il peut être verbeux de les importer dans tous les fichiers de test. Vitest a donc une configuration pratique où vous pouvez définir ces imports globaux et ainsi vous n'avez pas à les ajouter à chaque fichier. 

Mettons donc à jour le fichier `vitest.config.js` avec cette configuration :

```javascript
export default defineConfig({
  ...
  test: {
    ...
    globals: true
  }
})

```

Après avoir ajouté cette ligne `globals` égale à true dans votre configuration, vous pouvez maintenant supprimer les imports dans votre fichier de spécification. 

Si vous utilisez TypeScript, votre compilateur TypeScript se plaindra dans votre fichier de spécification. Vous pouvez résoudre cela en ajoutant la ligne suivante à votre fichier `tsconfig.json` :

```json
{
  "extends": "@tsconfig/svelte/tsconfig.json",
  "compilerOptions": {
    ...
    "types": ["vitest/globals"]
  },
}

```

Votre test peut maintenant ressembler à ceci. Ce n'est pas une énorme amélioration pour ce petit fichier, mais lorsque vous avez beaucoup de fichiers de spécification, ce changement de configuration est utile.

```javascript
describe("Fichier d'exemple", () => {
    it("Test d'exemple", () => {
        expect(1 + 3).equal(4);
    });
});

```

## Comment créer un composant Svelte

Nous allons créer un nouveau composant Svelte appelé `VerticalTabs.svelte`. Les exigences sont de créer un composant d'onglets verticaux qui peut contenir quelques éléments et permettre à l'utilisateur de sélectionner un onglet particulier pour afficher son contenu sur le côté droit.

Le composant sera divisé en deux parties. Le côté gauche affiche tous les onglets. Le côté droit affiche le contenu en fonction de l'onglet.

Créons le HTML et les styles CSS de base nécessaires pour le composant. Nous ajouterons la fonctionnalité pour basculer les onglets après avoir écrit les tests.

```html
<div class="vertical-tab-container">
    <ul class="vertical-tab">
        <li>Premier Onglet</li>
        <li>Deuxième Onglet</li>
        <li>Troisième Onglet</li>
    </ul>

    <div class="vertical-tab-content">
        <h2>Titre du Premier Onglet</h2>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem aut deserunt veniam tempora deleniti quos reprehenderit natus. Animi, obcaecati dolorum, culpa, maiores maxime ullam soluta unde rerum nihil temporibus quibusdam!</p>
    </div>
</div>

<style>
    .vertical-tab-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        border: 1px solid gray;
        border-radius: 1rem;
    }

    .vertical-tab {
        margin: 0px;
        padding: 3rem;
        list-style: none;
        border-right: 1px solid gray
    }

    .vertical-tab li {
        margin: 2rem 0;
    }

    .vertical-tab-content {
        flex:1
    }
</style>
```

Dans ce code, vous ajoutez des éléments simples comme une liste non ordonnée pour afficher la liste des onglets. Vous le stylez dans la balise `<style>` qui sera du CSS à portée locale pour ce composant.

Ensuite, vous ajoutez une balise `<h2>` pour afficher le titre de l'onglet et une balise de paragraphe `<p>` pour montrer plus de texte factice pour l'onglet. Vous utilisez `flex` pour afficher les deux éléments côte à côte et la propriété `flex: 1` sur le contenu fera en sorte que ce conteneur prenne tout l'espace restant disponible pour s'étendre.

Le composant devrait ressembler à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/VerticalTabInitial-1.png)
_Onglet vertical initial_

## Comment monter le composant Svelte dans le test

Maintenant, vous devez créer le premier test pour le composant en montant le composant Svelte, puis en vérifiant si vous pouvez trouver le texte "Titre du Premier Onglet" dans le composant. 

Créez donc un nouveau fichier de spécification appelé `VerticalTabs.spec.ts` :

```javascript
import VerticalTabs from "./VerticalTabs.svelte";

describe("Composant VerticalTabs", () => {

    test("devrait rendre le composant", () => {
        // Créer un nouveau conteneur pour le test
        const host = document.createElement('div');

        // Ajouter le nouveau conteneur dans le corps HTML
        document.body.appendChild(host);

        // Créer une instance de l'onglet vertical
        const instance = new VerticalTabs({ target: host });

        // Vérifier si l'instance a une valeur
        expect(instance).toBeTruthy()

        // Tester si nous pouvons trouver le "Titre du Premier Onglet"
        expect(host.innerHTML).toContain("Titre du Premier Onglet")

    });

})
```

Pour monter le composant Svelte, vous devez d'abord créer un conteneur `div` et attacher ce `div` au `body` du document HTML. Ensuite, vous devez attacher votre composant au `div`. Vous pouvez ensuite tester le `innerHTML` du conteneur principal pour voir si vous avez le contenu requis.

Ce test devrait maintenant passer puisque vous avez le contenu "Titre du Premier Onglet" affiché dans le composant.

Passer par ce long processus à toutes les étapes peut s'avérer difficile. Ajoutons donc un autre package pour faciliter le travail. Le package est `testing-library/svelte` et il fournit plus de fonctionnalités pour rendre les assertions faciles et moins verbeuses.

## Comment utiliser la bibliothèque de test Svelte

Tout d'abord, vous devrez installer la bibliothèque :

```
npm install -D @testing-library/svelte
```

Mettons à jour le test précédent pour le rendre moins verbeux et laissons `testing-library` gérer tout le travail difficile pour nous. Vous pouvez utiliser la fonction `render` pour ajouter le composant à la page de test.

```
import VerticalTabs from "./VerticalTabs.svelte";
import { render, screen } from '@testing-library/svelte';

describe("Composant VerticalTabs", () => {

    test("devrait rendre le composant", () => {

        render(VerticalTabs);

        const firstTabNode = screen.getByText(/Titre du Premier Onglet/i)

        expect(firstTabNode).toBeTruthy()
    });

})
```

Après la fonction `render`, ajoutez le composant à la page de test. Vous pouvez utiliser l'objet `screen` importé de la bibliothèque pour interroger les nœuds qui sont rendus.

Il existe plusieurs méthodes dans cet objet pour faciliter les tests, et vous utiliserez l'une des méthodes pour obtenir le texte dans le composant.

`getByText` retournera l'instance d'un texte donné. Vous attendez que le nœud contienne une certaine valeur.

Il existe trois façons principales de récupérer l'élément dans la bibliothèque de test, et chacune sert un but différent :

1. getByText – Cela lancera une erreur lorsque le texte n'est pas trouvé et le test échouera
2. queryByText – Cela retournera null lorsque le texte n'est pas trouvé
3. findByText – Cela lancera également une erreur lorsque le texte n'est pas trouvé et vous pouvez l'utiliser lors de tests asynchrones où l'élément prendra un certain temps à apparaître/disparaître

Vous pouvez trouver un résumé utile de ces fonctions d'assistance dans la [page de documentation officielle](https://testing-library.com/docs/queries/about).

![Image](https://www.freecodecamp.org/news/content/images/2022/09/QueriesSummary.png)
_Capture d'écran du résumé des documents officiels de la bibliothèque de test_

Vous pouvez trouver plus de détails sur cette API dans cette [page officielle](https://testing-library.com/docs/svelte-testing-library/api).

## Comment construire la fonctionnalité de basculement d'onglets

Nous allons commencer à ajouter la fonctionnalité pour basculer les onglets dans le composant et tester le composant en écrivant d'abord le test.

### Étape rouge

Écrivons un test pour basculer vers un onglet différent en cliquant sur l'élément de liste "Deuxième Onglet". 

Puisque nous n'avons pas encore implémenté cette fonctionnalité, nous allons d'abord échouer ce test et c'est normal. Une fois que nous avons échoué le test, nous devrions écrire la logique pour le faire passer à l'étape suivante. 

Écrivons donc un test qui échoue :

```
test("devrait basculer les onglets", async () => {
        render(VerticalTabs);

        const secondTabElement = screen.getByText(/Deuxième Onglet/i);

        fireEvent.click(secondTabElement)

        await screen.findByText(/Titre du Deuxième Onglet/i);
})
```

Nous utilisons `fireEvent` de la bibliothèque de test pour simuler le clic sur l'élément. Nous pouvons rendre le test `async` et `await` pour l'élément puisque le texte changera après que l'élément ait été cliqué.

Vous devriez maintenant avoir un test qui échoue :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/TestFailing.png)
_Test échouant, impossible de trouver le contenu_

### Étape verte

Ajoutons la logique pour changer l'onglet dans le composant Svelte. Nous pouvons le faire facilement en créant une variable `selectedIndex` et en changeant sa valeur en fonction de l'onglet sélectionné.

```
<script lang="ts">
    let selectedIndex = 0;

    const changeSecondTab = () => {
        selectedIndex = 1;
    }
</script>

<div class="vertical-tab-container">
    <ul class="vertical-tab">
        <li>Premier Onglet</li>
        <li on:click={() => changeSecondTab()}>Deuxième Onglet</li>
        <li>Troisième Onglet</li>
    </ul>

    <div class="vertical-tab-content">
        {#if selectedIndex == 0}
            <h2>Titre du Premier Onglet</h2>
            <p>...</p>
        {:else if selectedIndex == 1}
            <h2>Titre du Deuxième Onglet</h2>
            <p>...</p>
        {/if}
    </div>
</div>

```

**Note : Ce n'est pas la meilleure implémentation.** Elle est uniquement destinée à montrer que vous pouvez faire un travail minimal pour faire passer le test. Nous allons la nettoyer à l'étape suivante.

Nous avons une méthode `changeSecondTab` qui changera la valeur de `selectedIndex` à 1, ce qui fera que la condition `#if` changera l'onglet. Même si ce n'est pas la meilleure solution pour gérer tous les cas, nous avons un point de départ.

Regardons le test maintenant. Il devrait fonctionner :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/TestPassed.png)

### Refactorisation

Améliorons l'implémentation pour la rendre plus générique et la faire fonctionner pour les trois onglets. Nous pouvons également ajouter un indicateur pour montrer quel onglet est actuellement sélectionné.

```javascript
<script lang="ts">
    let selectedIndex = 0;

    const changeTab = (index: number) => {
        selectedIndex = index;
    }
</script>

<div class="vertical-tab-container">
    <ul class="vertical-tab">
        <li class:selected={selectedIndex == 0} 
        	on:click={() => changeTab(0)}>Premier Onglet</li>
            
        <li class:selected={selectedIndex == 1} 
        	on:click={() => changeTab(1)}>Deuxième Onglet</li>
            
        <li class:selected={selectedIndex == 2} 
        	on:click={() => changeTab(2)}>Troisième Onglet</li>
    </ul>

    <div class="vertical-tab-content">
        {#if selectedIndex == 0}
            <h2>Titre du Premier Onglet</h2>
            <p>...</p>
        {:else if selectedIndex == 1}
            <h2>Titre du Deuxième Onglet</h2>
            <p>...</p>
        {:else}
            <h2>Titre du Troisième Onglet</h2>
            <p>...</p>
        {/if}
    </div>
</div>

<style>
    ...
    .selected {
        color: blue;
    }
</style>
```

Nous avons créé une méthode `changeTab` qui sera appelée au clic sur chaque élément et changera ensuite `selectedIndex`. Cela provoquera la logique `#if` pour changer l'onglet en fonction de sa valeur.

Nous avons également `class:selected` suivi d'une expression et lorsque l'expression devient vraie, la classe `selected` est ajoutée à l'élément. Nous avons donc ajouté une classe CSS supplémentaire et nous avons rendu la couleur du texte bleue pour montrer l'onglet sélectionné.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/FinalComponent.png)
_Composant d'onglets verticaux terminé_

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-375.png)
_Test après la fin de la refactorisation_

Nous avons maintenant confirmé que le test passe également après la refactorisation. Vous pouvez continuer ce processus pour ajouter plus de tests et de fonctionnalités à votre composant.

## Comment ajouter une animation

Svelte facilite l'ajout d'animations lorsque le contenu est modifié. Vous pouvez utiliser la directive `transition` pour ajouter une animation pré-construite à votre application.

Ajoutons donc une animation de vol lorsque le contenu change. Vous pouvez importer l'animation de vol depuis `svelte/transition`, puis l'ajouter à l'élément en utilisant `transition:fly`. Cela ajoutera l'animation de vol par défaut lorsque le contenu disparaît et que le nouveau contenu apparaît. Un effet si soigné avec une seule ligne de code !

```javascript
import { fly } from 'svelte/transition';

<div class="vertical-tab-content" >
        {#if selectedIndex == 0}
            <div transition:fly>
                <h2>Titre du Premier Onglet</h2>
                <p>...</p>
            </div>
        {:else if selectedIndex == 1}
            <div transition:fly>
                <h2>Titre du Deuxième Onglet</h2>
                <p>...</p>
            </div>
        {:else}
            <div transition:fly>
                <h2>Titre du Troisième Onglet</h2>
                <p>...</p>
            </div>
        {/if}
    </div>
```

L'animation donne vie à votre application et l'aide à se démarquer. Je suis un grand fan du système de transition d'animation simple dans Svelte.

## Conclusion

Dans ce tutoriel, vous avez appris à créer un nouveau composant en utilisant la méthodologie de développement piloté par les tests. Veuillez partager vos commentaires sur cet article et me faire savoir vos pensées.

Merci d'avoir lu ! Vous pouvez me contacter sur Twitter [@sriram_thiagar](https://twitter.com/sriram_thiagar). Je publie régulièrement des articles sur mon blog [eternaldev.com](https://www.eternaldev.com/) si vous souhaitez lire plus d'articles de ma part.

Bonjour à tous. Je suis Sriram, et je travaille en tant que développeur Full Stack. J'aime partager mes apprentissages avec les autres. Je blogue depuis plus d'un an maintenant sur mon site web.