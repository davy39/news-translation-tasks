---
title: Comment automatiser les tests d'accessibilité avec Cypress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-14T19:00:42.000Z'
originalURL: https://freecodecamp.org/news/automating-accessibility-tests-with-cypress
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cypress-io-logo-social-share-8fb8a1db3cdc0b289fad927694ecb415-1.png
tags:
- name: Accessibility
  slug: accessibility
- name: Testing
  slug: testing
seo_title: Comment automatiser les tests d'accessibilité avec Cypress
seo_desc: "By Leonardo Faria\nIn my previous post, I covered how to add screenshot\
  \ testing in Cypress to ensure components don't unintentionally change over time.\
  \ \nNow, I will share how to automate accessibility tests with Cypress.\nWhy should\
  \ we care about acces..."
---

Par Leonardo Faria

Dans mon [précédent article](https://www.freecodecamp.org/news/how-to-add-screenshot-testing-with-cypress-to-your-project/), j'ai expliqué comment ajouter des tests de capture d'écran dans Cypress pour s'assurer que les composants ne changent pas involontairement au fil du temps. 

Maintenant, je vais partager comment automatiser les tests d'accessibilité avec Cypress.

## Pourquoi devrions-nous nous soucier de l'accessibilité ? 

Réponse courte : parce que c'est la bonne chose à faire.

Réponse longue : un web accessible peut aider les personnes handicapées à améliorer leur vie. 

Il existe différents types de handicaps, notamment auditifs, cognitifs, neurologiques, physiques, de la parole et visuels. Et notre objectif en tant que créateurs de produits, ingénieurs et designers est de créer des expériences qui incluent toutes les personnes. 

Il est également important de mentionner que l'accessibilité du web bénéficie également aux personnes _sans_ handicaps. 

Par exemple, les sites accessibles aident les personnes dont les capacités changent en raison du vieillissement ou les personnes ayant des connexions Internet lentes ou celles utilisant des appareils avec de petits écrans. 

Et un handicap peut également être temporaire. Par exemple, quelqu'un avec un bras cassé ne peut pas taper et utiliser une souris en même temps.

Si vous souhaitez vous éduquer sur le sujet, je peux recommander l'[Initiative pour l'accessibilité du Web du W3C (W3C WAI)](https://www.w3.org/WAI/) et [The A11Y Project](https://www.a11yproject.com/).

## Techniques de test d'accessibilité

Il existe différentes façons de tester si votre site web/application est accessible. Le W3C WAI dispose d'une [liste de 140+ outils](https://www.w3.org/WAI/ER/tools/) pour vous aider à déterminer si votre site web/application respecte les directives d'accessibilité. 

Vous pouvez également ajouter à votre stratégie :

- Tests utilisateurs réels : des entreprises comme [Fable](https://www.makeitfable.com/) vous mettent en contact avec des personnes handicapées afin que vos recherches et tests utilisateurs puissent vous aider à atteindre vos objectifs de conformité.
- Extensions de navigateur : [axe](https://www.deque.com/axe/browser-extensions/) est une extension recommandée pour Chrome, Firefox et Edge qui aide à identifier et résoudre les problèmes d'accessibilité courants.

Le [moteur d'accessibilité de axe est open-source](https://github.com/dequelabs/axe-core) et il peut être utilisé de différentes manières, comme le montrera cet article.

## Avant de commencer

J'ai créé un [site web d'exemple](https://cypress-accessibility-example.vercel.app/) pour imiter une bibliothèque de composants. Il s'agit d'un site web très simple créé avec Tailwind CSS et hébergé sur Vercel, et il documente 2 composants : [badge](https://cypress-accessibility-example.vercel.app/badge.html) et [button](https://cypress-accessibility-example.vercel.app/button.html).

Vous pouvez consulter le [code source](https://github.com/leonardofaria/cypress-accessibility-example) sur GitHub. Le site web est statique et se trouve dans le dossier `public`. Vous pouvez voir le site web localement en exécutant `npm run serve` et en vérifiant dans le navigateur [http://localhost:8000](http://localhost:8000).

![Site web d'exemple](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-sample-website.png)

## Ajout de Cypress et cypress-axe

Commencez par cloner le [dépôt d'exemple](https://github.com/leonardofaria/cypress-example). Ensuite, créez une nouvelle branche et installez [cypress-axe](https://www.npmjs.com/package/cypress-axe), le package responsable de lier le moteur axe à Cypress.

```bash
git checkout -b add-cypress
npm install -D cypress cypress-axe
```

Ensuite, créez un fichier `cypress/support/index.js` contenant :

```
import 'cypress-axe'
```

Cette importation injectera toutes les fonctions dont nous avons besoin pour nos tests.

## Création du test d'accessibilité

Il est temps de créer le test d'accessibilité. Voici le plan :

1. Cypress visitera chaque page (badge et button) du projet.
2. Cypress testera chaque exemple de la page. La [page Badge](https://cypress-example.vercel.app/badge.html) a 2 exemples (Default et Pill), tandis que la [page Button](https://cypress-example.vercel.app/badge.html) a 3 exemples (Default, Pill et Outline). 

Tous ces exemples sont à l'intérieur d'un élément `<div>` avec une classe `cypress-wrapper`. Cette classe a été ajoutée dans le seul but d'identifier ce qui doit être testé.

La première étape consiste à créer le fichier de configuration de Cypress (`cypress.json`) :

```json
{
  "baseUrl": "http://localhost:8000/",
  "video": false
}
```

L'URL de base est le site web en cours d'exécution localement. Comme je l'ai mentionné précédemment, `npm run serve` servira le contenu du dossier `public`. La deuxième option, `video`, désactive l'enregistrement vidéo de Cypress, qui ne sera pas utilisé dans le projet.

Il est temps de créer le test. Dans `cypress/integration/accessibility.spec.js`, ajoutez :

```js
const routes = ['badge.html', 'button.html'];

describe('Test d\'accessibilité des composants', () => {
  routes.forEach((route) => {
    const componentName = route.replace('.html', '');
    const testName = `${componentName} n\'a pas de violations d\'accessibilité détectables au chargement`;

    it(testName, () => {
      cy.visit(route);
      cy.injectAxe();
      
      cy.get('.cypress-wrapper').each((element, index) => {
        cy.checkA11y(
          '.cypress-wrapper',
          {
            runOnly: {
              type: 'tag',
              values: ['wcag2a'],
            },
          }
        );
      });
    });
  });
});
```

Dans le code ci-dessus, je crée des tests dynamiques basés sur le tableau `routes`. Le test vérifiera chaque élément `.cypress-wrapper` par rapport aux règles WCAG 2.0 Niveau A. 

Il existe différentes normes / objectifs, comme le montre le tableau ci-dessous : 

| Nom de la balise         | Norme d'accessibilité / Objectif                     |
| ---------------- | ---------------------------------------------------- |
| `wcag2a`         | WCAG 2.0 Niveau A                                     |
| `wcag2aa`        | WCAG 2.0 Niveau AA                                    |
| `wcag21a`        | WCAG 2.1 Niveau A                                     |
| `wcag21aa`       | WCAG 2.1 Niveau AA                                    |
| `best-practice`  | Bonnes pratiques d'accessibilité courantes                  |
| `wcag***`        | Critère de succès WCAG, par exemple, wcag111 correspond au SC 1.1.1 |
| `ACT`            | Règles de test de conformité d'accessibilité approuvées par le W3C |
| `section508`     | Anciennes règles de la Section 508                                |
| `section508.*.*` | Exigence dans l'ancienne Section 508                       |

Vous pouvez trouver plus d'informations à ce sujet dans la [documentation axe-core](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md#axe-core-tags).

Enfin, créons dans le fichier `package.json` la commande pour déclencher les tests :

```json
{
  "test": "cypress"
}  
```

À partir de là, il y a 2 options : exécuter Cypress en mode headless avec `npm run cypress run` ou utiliser le Cypress Test Runner avec `npm run cypress open`.

### Option headless

En utilisant `npm run test run`, la sortie devrait être similaire à l'image suivante :

![Sortie du premier test](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-accessibility-first-test.jpg)

Les tests passeront puisque les composants n'ont pas de problèmes d'accessibilité.

### Option Test Runner

En utilisant `npm run test open`, le Cypress Test Runner s'ouvrira et vous pourrez suivre étape par étape les tests.

![Capture d'écran du Cypress Test Runner](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-accessibility-test-runner.jpg)

Notre première étape est terminée. Fusionnons cette branche avec master. Si vous souhaitez voir le travail effectué jusqu'à présent, consultez ma [Pull Request](https://github.com/leonardofaria/cypress-accessility-example/pull/1/files). 

## Test en situation réelle

Imaginons que nous mettons à jour le site web et que nous voulons identifier les boutons avec des ids. La propriété `id` doit être unique dans le document, car nous ne pouvons pas avoir 2 éléments avec le même id. Mais nous avons oublié cela et 3 boutons ont le même id.

Cypress échouera et la sortie ressemblera à ceci : 

![Sortie du test échoué](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-accessibility-failed-test.jpg)

Améliorons la sortie de nos tests en affichant un tableau des problèmes trouvés. Tout d'abord, créons une nouvelle branche :

```bash
git checkout -b improve-cypress-tests
```

Ensuite, créez le fichier `cypress/plugins/index.js` avec le contenu suivant : 

```js
module.exports = (on, config) => {
  on('task', {
    log(message) {
      console.log(message)
 
      return null
    },
    table(message) {
      console.table(message)
 
      return null
    }
  })
}
```

Cela exécutera du code dans Node via l'événement de plugin `task` de Cypress. Ensuite, retournons au fichier `accessibility.spec.js` et ajoutons la fonction suivante en haut du fichier :

```js
const terminalLog = (violations) => {
  cy.task(
    'log',
    `${violations.length} violation${violations.length === 1 ? '' : 's'} d\'accessibilité ${violations.length === 1 ? 'a été' : 'ont été'} détectée${violations.length === 1 ? '' : 's'}`
  )
  // extraire des clés spécifiques pour garder le tableau lisible
  const violationData = violations.map(
    ({ id, impact, description, nodes }) => ({
      id,
      impact,
      description,
      nodes: nodes.length
    })
  )
 
  cy.task('table', violationData)
}
```

Le tableau `violations` contient toutes les informations sur les éléments en échec. Vous pouvez ajuster ce code pour inclure, par exemple, le code source de l'élément dans la sortie du test.

Enfin, appelons la fonction à l'intérieur des tests. Modifiez la fonction `checkA11y` pour : 

```js
cy.checkA11y(
  '.cypress-wrapper',
  {
    runOnly: {
      type: 'tag',
      values: ['wcag2a'],
    },
  },
  terminalLog,
);
```

Lorsque vous exécutez le test à nouveau, vous obtiendrez un tableau contenant les problèmes signalés par axe :

![Sortie du test échoué avec un beau tableau](https://leonardofaria.net/wp-content/uploads/2020/08/cypress-accessibility-failed-test-table.jpg)

Si vous avez des questions, veuillez consulter la [Pull request](https://github.com/leonardofaria/cypress-accessibility-example/pull/2/files) sur GitHub. 

## Prochaines étapes

À partir de là, vous pouvez continuer votre chemin vers la création de produits plus accessibles. En tant que prochaines étapes, je recommanderais :

- Ajouter ces tests dans votre solution CI - J'ai écrit sur [l'intégration de Cypress dans Semaphore](https://www.freecodecamp.org/news/2020/08/03/adding-screenshot-testing-with-cypress-in-your-project/#adding-ci)
- Trouver la meilleure façon de personnaliser la sortie des tests pour améliorer le dépannage des problèmes
- Apprendre davantage sur le fonctionnement de axe.

J'espère que vous avez appris que les tests d'accessibilité ne sont pas difficiles et qu'ils ne nécessitent pas beaucoup pour commencer. L'automatisation alimentée par axe peut définitivement nous aider à créer de meilleures expériences utilisateur pour toutes les personnes.

--

Des questions ? Des commentaires ? Cet article est également disponible sur [mon blog](https://leonardofaria.net/2020/08/13/automating-accessibility-tests-with-cypress/). Si vous aimez ce contenu, suivez-moi sur [Twitter](https://twitter.com/leozera) et [GitHub](https://github.com/leonardofaria).