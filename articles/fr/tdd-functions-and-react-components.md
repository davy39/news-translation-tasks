---
title: Développement piloté par les tests, fonctions et composants React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-30T17:18:39.000Z'
originalURL: https://freecodecamp.org/news/tdd-functions-and-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/tdd.jpeg
tags:
- name: React
  slug: react
- name: test driven development
  slug: test-driven-development
seo_title: Développement piloté par les tests, fonctions et composants React
seo_desc: 'By TK

  This article is part of my studies on how to build sustainable and consistent software.
  In this post, we will talk about the thinking behind the testing driven development
  and how to apply this knowledge to simple functions, web accessibility, ...'
---

Par TK

Cet article fait partie de mes études sur la manière de construire des logiciels durables et cohérents. Dans cet article, nous parlerons de la réflexion derrière le développement piloté par les tests et de la manière d'appliquer ces connaissances à des fonctions simples, à l'accessibilité web et aux composants React, principalement avec Jest et React Testing Library.

Les tests automatisés font partie intégrante du développement logiciel. Ils nous donnent, en tant que développeurs, la confiance nécessaire pour livrer du code, mais ils augmentent également la confiance que le logiciel sera opérationnel et fonctionnera correctement.

J'ai commencé ma carrière dans le développement logiciel dans la communauté Ruby en écrivant des tests dès le premier jour où j'ai appris le langage. La communauté Ruby (et Rails) a toujours été forte dans le domaine de l'automatisation des tests. Cela a aidé à façonner mon état d'esprit sur la manière d'écrire de bons logiciels.

Ainsi, en utilisant Ruby et Rails, j'ai fait beaucoup de travail backend comme des jobs en arrière-plan, la modélisation de structures de données, la construction d'API, et ainsi de suite. Dans ce contexte, l'utilisateur est toujours le même : l'utilisateur développeur. Si je construis une API, l'utilisateur sera le développeur qui consomme l'API. Si je construis des modèles, l'utilisateur sera le développeur qui utilisera ce modèle.

Maintenant, en faisant également beaucoup de travail frontend, après 1 année intense de construction de PWAs en utilisant principalement React et Redux, certaines pensées me sont venues à l'esprit au début :

* Le TDD est impossible lors de la construction d'interfaces utilisateur. Comment savoir si c'est une div ou un span ?
* Les tests peuvent être "complexes". Dois-je utiliser shallow ou mount ? Tester tout ? Vérifier que chaque div est à la bonne place ?

J'ai donc commencé à repenser à ces pratiques de test et à la manière de les rendre productives.

Le TDD est possible. Si je me demande si je dois m'attendre à une div ou à un span, je teste probablement la mauvaise chose. Souvenez-vous : les tests doivent nous donner la confiance de livrer, pas nécessairement de couvrir chaque détail ou chaque détail d'implémentation. Nous approfondirons ce sujet plus tard !

Je veux construire des tests qui :

* Assurent que le logiciel fonctionne correctement
* Donnent la confiance de livrer du code en production
* Nous font réfléchir à la conception du logiciel

Et des tests qui rendent le logiciel :

* Facile à maintenir
* Facile à refactoriser

## Développement piloté par les tests

Le TDD ne devrait pas être complexe. C'est simplement un processus en 3 étapes :

* Écrire un test
* Le faire fonctionner
* Le rendre correct

Nous commençons par écrire un test simple pour couvrir comment nous attendons que le logiciel fonctionne. Ensuite, nous faisons la première implémentation du code (classe, fonction, script, etc.). Maintenant, le logiciel se comporte comme prévu. Il fonctionne comme attendu. Il est temps de le rendre correct. Il est temps de l'améliorer.

Le but est un code propre qui fonctionne. Nous résolvons d'abord le problème "ça fonctionne" puis nous rendons le code propre.

C'est assez simple. Et ça devrait l'être. Je n'ai pas dit que c'était facile. Mais c'est simple, direct, juste 3 étapes. Chaque fois que vous exercez ce processus d'écrire les tests d'abord, le code ensuite, puis la refactorisation, vous vous sentez plus confiant.

Une bonne technique lorsque vous écrivez vos tests en premier est de penser aux cas d'utilisation et de simuler comment il devrait être utilisé (en tant que fonction, composant, ou utilisé par un utilisateur réel).

## Fonctions

Appliquons cette approche TDD à des fonctions simples.

Il y a quelque temps, j'implémentais une fonction de brouillon pour un flux d'enregistrement immobilier. Une partie de la fonction consistait à afficher une modale si l'utilisateur avait un bien immobilier non terminé. La fonction que nous allons implémenter est celle qui répond si l'utilisateur a au moins un brouillon de bien immobilier.

Première étape : écrire le test ! Pensons aux cas d'utilisation de cette fonction. Elle répond toujours par un booléen : vrai ou faux.

* N'a pas de brouillon de bien immobilier non enregistré : `false`
* A au moins un brouillon de bien immobilier non enregistré : `true`

Écrivons les tests qui représentent ce comportement :

```javascript
describe('hasRealEstateDraft', () => {
  describe('avec des brouillons de biens immobiliers', () => {
    it('retourne vrai', () => {
      const realEstateDrafts = [
        {
          address: 'São Paulo',
          status: 'UNSAVED'
        }
      ];

      expect(hasRealEstateDraft(realEstateDrafts)).toBeTruthy();
    });
  });

  describe('sans brouillons', () => {
    it('retourne faux', () => {
      expect(hasRealEstateDraft([])).toBeFalsy();
    });
  });
});

```

Nous avons écrit les tests. Mais en les exécutant, ils deviennent rouges : 2 tests échoués car nous n'avons pas encore implémenté la fonction.

Deuxième étape : faire en sorte que ça fonctionne ! Dans ce cas, c'est assez simple. Nous devons recevoir cet objet de tableau et retourner s'il a ou non au moins un brouillon de bien immobilier.

```javascript
const hasRealEstateDraft = (realEstateDrafts) => realEstateDrafts.length > 0;

```

Super ! Fonction simple. Tests simples. Nous pourrions passer à l'étape 3 : la rendre correcte ! Mais dans ce cas, notre fonction est vraiment simple et nous l'avons déjà correcte.

Mais maintenant, nous avons besoin que la fonction obtienne les brouillons de biens immobiliers et les passe à `hasRealEstateDraft`.

À quel cas d'utilisation pouvons-nous penser ?

* Une liste vide de biens immobiliers
* Seulement des biens immobiliers enregistrés
* Seulement des biens immobiliers non enregistrés
* Mixte : biens immobiliers enregistrés et non enregistrés

Écrivons les tests pour les représenter :

```javascript
describe('getRealEstateDrafts', () => {
  describe('avec une liste vide', () => {
    it('retourne une liste vide', () => {
      const realEstates = [];

      expect(getRealEstateDrafts(realEstates)).toMatchObject([]);
    });
  });

  describe('avec seulement des biens immobiliers non enregistrés', () => {
    it('retourne les brouillons', () => {
      const realEstates = [
        {
          address: 'São Paulo',
          status: 'UNSAVED'
        },
        {
          address: 'Tokyo',
          status: 'UNSAVED'
        }
      ];

      expect(getRealEstateDrafts(realEstates)).toMatchObject(realEstates);
    });
  });

  describe('avec seulement des biens immobiliers enregistrés', () => {
    it('retourne une liste vide', () => {
      const realEstates = [
        {
          address: 'São Paulo',
          status: 'SAVED'
        },
        {
          address: 'Tokyo',
          status: 'SAVED'
        }
      ];

      expect(getRealEstateDrafts(realEstates)).toMatchObject([]);
    });
  });

  describe('avec des biens immobiliers enregistrés et non enregistrés', () => {
    it('retourne les brouillons', () => {
      const realEstates = [
        {
          address: 'São Paulo',
          status: 'SAVED'
        },
        {
          address: 'Tokyo',
          status: 'UNSAVED'
        }
      ];

      expect(getRealEstateDrafts(realEstates)).toMatchObject([{
        address: 'Tokyo',
        status: 'UNSAVED'
      }]);
    });
  });
});

```

Super ! Nous exécutons les tests. Cela ne fonctionne pas... encore ! Maintenant, implémentons la fonction.

```javascript
const getRealEstatesDrafts = (realEstates) => {
  const unsavedRealEstates = realEstates.filter((realEstate) => realEstate.status === 'UNSAVED');
  return unsavedRealEstates;
};

```

Nous filtrons simplement par le statut du bien immobilier et le retournons. Super, les tests passent, la barre est verte ! Et le logiciel se comporte comme prévu, mais nous pouvons l'améliorer : étape 3 !

Que diriez-vous d'extraire la fonction anonyme dans la fonction `filter` et de faire en sorte que `'UNSAVED'` soit représenté par une énumération ?

```javascript
const STATUS = {
  UNSAVED: 'UNSAVED',
  SAVED: 'SAVED',
};

const byUnsaved = (realEstate) => realEstate.status === STATUS.UNSAVED;

const getRealEstatesDrafts = (realEstates) => realEstates.filter(byUnsaved);

```

Les tests passent toujours et nous avons une meilleure solution.

Une chose à garder à l'esprit ici : j'ai isolé la source de données de la logique. Que signifie-t-il ? Nous obtenons les données du stockage local (source de données), mais nous testons uniquement les fonctions responsables de la logique pour obtenir les brouillons et voir s'il y a au moins un brouillon. Les fonctions avec la logique, nous nous assurons qu'elles fonctionnent et que le code est propre.

Si nous obtenons le `localStorage` à l'intérieur de nos fonctions, cela devient difficile à tester. Nous séparons donc la responsabilité et rendons les tests faciles à écrire. Les fonctions pures sont plus faciles à maintenir et plus simples à tester.

## Composants React

Maintenant, parlons des composants React. Dans l'introduction, nous avons parlé de l'écriture de tests qui testent les détails d'implémentation. Et maintenant, nous allons voir comment nous pouvons l'améliorer, le rendre plus durable et avoir plus de confiance.

Il y a quelques jours, je prévoyais de construire les nouvelles informations d'intégration pour le propriétaire de biens immobiliers. Il s'agit essentiellement d'un ensemble de pages avec le même design, mais l'icône, le titre et la description des pages changent.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/ui.png)

Je voulais construire un seul composant : `Content` et passer les informations nécessaires pour rendre l'icône, le titre et la description corrects. Je passerais `businessContext` et `step` en tant que props et il rendrait le contenu correct pour la page d'intégration.

Nous ne voulons pas savoir si nous allons rendre une balise div ou paragraph. Notre test doit s'assurer que pour un contexte métier et une étape donnés, le contenu correct sera là. J'ai donc imaginé ces cas d'utilisation :

* La première étape du contexte métier de location
* La dernière étape du contexte métier de location
* La première étape du contexte métier de vente
* La dernière étape du contexte métier de vente

Voyons les tests :

```javascript
describe('Content', () => {
  describe('dans le contexte de location', () => {
    const defaultProps = {
      businessContext: BUSINESS_CONTEXT.RENTAL
    };

    it('rend le titre et la description pour la première étape', () => {
      const step = 0;
      const { getByText } = render(<Content {...defaultProps} step={step} />);

      expect(getByText('the first step title')).toBeInTheDocument();
      expect(getByText('the first step description')).toBeInTheDocument();
    });

    it('rend le titre et la description pour la quatrième étape', () => {
      const step = 3;
      const { getByText } = render(<Content {...defaultProps} step={step} />);

      expect(getByText('the last step title')).toBeInTheDocument();
      expect(getByText('the last step description')).toBeInTheDocument();
    });
  });

  describe('dans le contexte de vente', () => {
    const defaultProps = {
      businessContext: BUSINESS_CONTEXT.SALE
    };

    it('rend le titre et la description pour la première étape', () => {
      const step = 0;
      const { getByText } = render(<Content {...defaultProps} step={step} />);

      expect(getByText('the first step title')).toBeInTheDocument();
      expect(getByText('the first step description')).toBeInTheDocument();
    });

    it('rend le titre et la description pour la dernière étape', () => {
      const step = 6;
      const { getByText } = render(<Content {...defaultProps} step={step} />);

      expect(getByText('the last step title')).toBeInTheDocument();
      expect(getByText('the last step description')).toBeInTheDocument();
    });
  });
});

```

Nous avons un bloc `describe` pour chaque contexte métier et un bloc `it` pour chaque étape. J'ai également créé un test d'accessibilité pour m'assurer que le composant que nous construisons est accessible.

```javascript
it('n\'a pas de violations d\'accessibilité', async () => {
  const props = {
    businessContext: BUSINESS_CONTEXT.SALE,
    step: 0,
  };

  const { container } = render(<Content {...props} />);
  const results = await axe(container);

  expect(results).toHaveNoViolations();
});

```

Maintenant, nous devons le faire fonctionner ! Essentiellement, la partie UI de ce composant est simplement l'icône, le titre et la description. Quelque chose comme :

```javascript
<Fragment>
  <Icon />
  <h1>{title}</h1>
  <p>{description}</p>
</Fragment>

```

Nous devons simplement construire la logique pour obtenir toutes ces données correctes. Comme j'ai le `businessContext` et le `step` dans ce composant, je voulais simplement faire quelque chose comme

```javascript
content[businessContext][step]

```

Et il obtient le contenu correct. J'ai donc construit une structure de données pour fonctionner de cette manière.

```javascript
const onboardingStepsContent = {
  alugar: {
    0: {
      Icon: Home,
      title: 'first step title',
      description: 'first step description',
    },
    // ...
  },
  vender: {
    0: {
      Icon: Home,
      title: 'first step title',
      description: 'first step description',
    },
    // ...
  },
};

```

Ce n'est qu'un objet avec les premières clés en tant que données de contexte métier et pour chaque contexte métier, il a des clés qui représentent chaque étape de l'intégration. Et notre composant serait :

```javascript
const Content = ({ businessContext, step }) => {
  const onboardingStepsContent = {
    alugar: {
      0: {
        Icon: Home,
        title: 'first step title',
        description: 'first step description',
      },
      // ...
    },
    vender: {
      0: {
        Icon: Home,
        title: 'first step title',
        description: 'first step description',
      },
      // ...
    },
  };

  const { Icon, title, description } = onboardingStepsContent[businessContext][step];

  return (
    <Fragment>
      <Icon />
      <h1>{title}</h1>
      <p>{description}</p>
    </Fragment>
  );
};

```

Cela fonctionne ! Maintenant, améliorons-le. Je voulais rendre l'obtention du contenu plus résiliente. Que se passe-t-il si elle reçoit une étape qui n'existe pas, par exemple ? Voici les cas d'utilisation :

* La première étape du contexte métier de location
* La dernière étape du contexte métier de location
* La première étape du contexte métier de vente
* La dernière étape du contexte métier de vente
* Étape inexistante du contexte métier de location
* Étape inexistante du contexte métier de vente

Voyons les tests :

```javascript
describe('getOnboardingStepContent', () => {
  describe('quand il reçoit un businessContext et une étape existants', () => {
    it('retourne le contenu correct pour l\'étape dans le contexte métier "alugar"', () => {
      const businessContext = 'alugar';
      const step = 0;

      expect(getOnboardingStepContent({ businessContext, step })).toMatchObject({
        Icon: Home,
        title: 'first step title',
        description: 'first step description',
      });
    });

    it('retourne le contenu correct pour l\'étape dans le contexte métier "vender"', () => {
      const businessContext = 'vender';
      const step = 5;

      expect(getOnboardingStepContent({ businessContext, step })).toMatchObject({
        Icon: ContractSign,
        title: 'last step title',
        description: 'last step description',
      });
    });
  });

  describe('quand il reçoit une étape inexistante pour un businessContext donné', () => {
    it('retourne la première étape du contexte métier "alugar"', () => {
      const businessContext = 'alugar';
      const step = 7;

      expect(getOnboardingStepContent({ businessContext, step })).toMatchObject({
        Icon: Home,
        title: 'first step title',
        description: 'first step description',
      });
    });

    it('retourne la première étape du contexte métier "vender"', () => {
      const businessContext = 'vender';
      const step = 10;

      expect(getOnboardingStepContent({ businessContext, step })).toMatchObject({
        Icon: Home,
        title: 'first step title',
        description: 'first step description',
      });
    });
  });
});

```

Super ! Maintenant, construisons notre fonction `getOnboardingStepContent` pour gérer cette logique.

```javascript
const getOnboardingStepContent = ({ businessContext, step }) => {
  const content = onboardingStepsContent[businessContext][step];

  return content
    ? content
    : onboardingStepsContent[businessContext][0];
};

```

Nous essayons d'obtenir le contenu. Si nous l'avons, nous le retournons simplement. Si nous ne l'avons pas, nous retournons la première étape de l'intégration.

Propre ! Mais nous pouvons l'améliorer. Que diriez-vous d'utiliser l'opérateur `||` ? Pas besoin d'assigner à une variable, pas besoin d'utiliser un ternaire.

```javascript
const getOnboardingStepContent = ({ businessContext, step }) =>
  onboardingStepsContent[businessContext][step] ||
  onboardingStepsContent[businessContext][0];

```

Si le contenu est trouvé, il est simplement retourné. Si le contenu n'est pas trouvé, il retourne la première étape du contexte métier donné.

Maintenant, notre composant est uniquement UI.

```javascript
const Content = ({ businessContext, step }) => {
  const {
    Icon,
    title,
    description,
  } = getOnboardingStepContent({ businessContext, step });

  return (
    <Fragment>
      <Icon />
      <h1>{title}</h1>
      <p>{description}</p>
    </Fragment>
  );
};

```

---

## Réflexions finales

J'aime réfléchir en profondeur aux tests que j'écris. Et je pense que tous les développeurs devraient en faire de même. Cela doit nous donner la confiance de livrer plus de code et d'avoir un impact plus important sur le marché sur lequel nous travaillons.

Comme tout code, lorsque nous écrivons des tests mal conçus, cela influence les autres développeurs à suivre le "modèle". Cela empire dans les grandes entreprises. Cela ne se développe pas bien. Mais nous sommes toujours capables de nous arrêter, de réfléchir au statu quo et de prendre des mesures pour l'améliorer.

J'ai partagé quelques ressources que j'ai trouvées intéressantes à lire et à apprendre. Si vous voulez une excellente introduction au TDD, je recommande vivement TDD par l'exemple, un livre de Kent Beck.

J'écrirai davantage sur les tests, le TDD et React. Et comment nous pouvons rendre nos logiciels plus cohérents et nous sentir en sécurité lorsque nous livrons du code en production.

## Dépendances

* [jest-axe](https://github.com/nickcolley/jest-axe): correspondances jest pour tester l'accessibilité
* [testing-library/react-testing-library](https://github.com/testing-library/react-testing-library): utilitaires de test pour aider à tester react
* [testing-library/jest-dom](https://github.com/testing-library/jest-dom): correspondances jest pour tester l'état du DOM

## Ressources

* [Cours JavaScript pour débutants](https://BeginnerJavaScript.com/friend/LEANDRO)
* [Cours React pour débutants](https://ReactForBeginners.com/friend/LEANDRO)
* [Cours avancé React](https://AdvancedReact.com/friend/LEANDRO)
* [Cours ES6](https://ES6.io/friend/LEANDRO)
* [La route pour apprendre React](https://www.educative.io/courses/the-road-to-learn-react?aff=x8bV)
* [Fondamentaux JavaScript avant d'apprendre React](https://www.educative.io/courses/javascript-fundamentals-before-learning-react?aff=x8bV)
* [Réintroduction à React : V16 et au-delà](https://www.educative.io/courses/reintroducing-react-v16-beyond?aff=x8bV)
* [Modèles avancés React avec Hooks](https://www.educative.io/courses/advanced-react-patterns-with-hooks?aff=x8bV)
* [Redux pratique](https://www.educative.io/courses/practical-redux)
* [Cours JavaScript par OneMonth](https://mbsy.co/lFtbC)
* [Livre Développement piloté par les tests par l'exemple par Kent Beck](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530)
* [Livre JavaScript testable par Mark Ethan Trostler](https://www.amazon.com/Testable-JavaScript-Ensuring-Reliable-Code/dp/1449323391/ref=sr_1_8?dchild=1&keywords=testing+javascript&qid=1585274935&s=books&sr=1-8)
* [Code source de l'article de blog](https://github.com/tk-notes/blog/tree/master/tdd-functions-and-react-components)
* [Tester les applications React avec jest, jest-axe et react-testing-library](https://medium.com/hackernoon/testing-react-with-jest-axe-and-react-testing-library-accessibility-34b952240f53)
* [Tests React modernes, partie 3 : Jest et React Testing Library](https://blog.sapegin.me/all/react-testing-3-jest-and-react-testing-library/)
* [Ce que nous avons trouvé lorsque nous avons testé des outils sur la page web la moins accessible au monde](https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/)
* [Tester les détails d'implémentation](https://kentcdodds.com/blog/testing-implementation-details)
* [Apprendre React en construisant une application](https://alterclass.io/?ref=5ec57f513c1321001703dcd2)

Vous pouvez trouver d'autres articles comme celui-ci [sur mon blog](https://leandrotk.github.io/tk/2020/03/closure-currying-and-cool-abstractions/index.html).