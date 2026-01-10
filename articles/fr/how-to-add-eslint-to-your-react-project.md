---
title: Comment ajouter ESLint à votre projet React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-08-08T16:36:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-eslint-to-your-react-project
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/How-To-Add-ESLint-To-Your-React-Project-1.png
tags:
- name: Code Quality
  slug: code-quality
- name: eslint
  slug: eslint
- name: React
  slug: react
seo_title: Comment ajouter ESLint à votre projet React
seo_desc: "By Jacob Isah \nAs a React developer, maintaining code quality is essential\
  \ for building robust and maintainable applications. Fortunately, there's a powerful\
  \ tool called ESLint that can significantly improve the quality of your React projects.\n\
  In thi..."
---

Par Jacob Isah

En tant que développeur React, maintenir la qualité du code est essentiel pour construire des applications robustes et maintenables. Heureusement, il existe un outil puissant appelé ESLint qui peut améliorer considérablement la qualité de vos projets React.

Dans cet article, nous allons explorer comment fonctionne ESLint et créer un composant de bouton d'inscription pour démontrer ses avantages.

## Qu'est-ce qu'ESLint ?

ESLint est un utilitaire de linting JavaScript open-source populaire. Il analyse votre code pour détecter les erreurs potentielles, et impose des normes de codage tout en améliorant la qualité du code.

Il peut également vous aider en tant que développeur à identifier et corriger les erreurs courantes, à utiliser les meilleures pratiques et à maintenir la cohérence dans votre base de code.

Vous pouvez intégrer ESLint de manière transparente dans vos projets React, en fournissant des commentaires en temps réel et en améliorant la qualité globale de votre code.

## Comment configurer votre projet

Commençons par configurer un nouveau projet React et installer ESLint. Pour démontrer cela, nous allons créer une application d'inscription en React.

Imaginons que nous voulons stocker notre projet sur le bureau, alors commençons par configurer notre structure de fichiers. Commençons par créer un répertoire racine pour notre projet sur le bureau (`eslintExample` dans ce cas).

```javascript
mkdir eslintExample
cd eslintExample
```

### Installer l'application React

Nous allons maintenant utiliser create-react-app pour configurer notre application React.

```javascript
npx create-react-app signup-app
```

### Installer ESLint

Et vous pouvez utiliser la commande suivante pour configurer ESLint :

```javascript
npm install eslint eslint-plugin-react eslint-plugin-react-hooks --save-dev
```

Votre structure de répertoire devrait ressembler à ceci :

```javascript
eslintExample/
  └── signup-app/
      └── node_modules/
      └── public/
      └── src/
          └── App.css
          └── App.js
          └── App.test.js
          └── SignupButton.js
          └── index.css
          └── logo.svg
          └── reportWebVitals.js
          └── setupTests.js
      └── .eslintrc.json
      └── .gitignore
      └── package-lock.json
      └── package.json
      └── README.md

```

## Comment configurer ESLint dans un projet React

Pour travailler avec ESLint dans notre projet React, nous devons le configurer. Pour ce faire, la première étape consiste à créer un fichier **.eslintrc.json** dans le répertoire racine du projet et à ajouter le code suivant :

```javascript
{
    "env": {
      "browser": true,
      "es2021": true
    },
    "extends": ["eslint:recommended", "plugin:react/recommended", "plugin:react-hooks/recommended"],
    "parserOptions": {
      "ecmaVersion": 12,
      "sourceType": "module",
      "ecmaFeatures": {
        "jsx": true
      }
    },
    "plugins": ["react", "react-hooks"],
    "rules": {
      // ajoutez des règles personnalisées ici selon les besoins de votre projet
    }
}
```

La configuration ci-dessus configure ESLint pour qu'il fonctionne avec React et React Hooks en utilisant les configurations recommandées. Vous pouvez ajouter ou personnaliser des règles selon les exigences spécifiques de votre projet.

![Comment ajouter ESLint à votre projet React](https://lh5.googleusercontent.com/nEAJArNZ75TidB33XK-0_p4BQea9aTppnnFrk0u7znVKIpsmCortCwaZ0KFYbw_1OOkz_QcXC0cr1WGih89a1OY2REUCSIWKckpaGESNchz8xakqTAntBbpgDXabbrcf6kWZzwxpAZ14PC5xQb9h_A)
_Création du fichier .eslintrc.json et ajout de la configuration qui permet à ESLint de fonctionner avec React._

## Comment créer le composant de bouton d'inscription

Maintenant, créons un simple composant de bouton d'inscription (SignupButton.js) à l'intérieur du dossier "src".

À l'intérieur du fichier src, créez le fichier SignupButton.js. Il devrait ressembler à ceci : `src/SignupButton.js`. À l'intérieur de votre SignupButton.js, collez le code suivant :

```javascript
import React from "react";

const SignupButton = () => {
  const handleSignup = () => {
    alert("Inscription réussie !");
  };

  return (
    <button onClick={handleSignup} className="signup-button">
      S'inscrire
    </button>
  );
};
```

Le composant ci-dessus est un bouton de base qui déclenche une alerte lorsqu'il est cliqué, simulant le processus d'inscription. Vous pouvez maintenant exécuter cette commande :

```javascript
npm start
```

Cela démarrera notre application React à la racine du projet. Vous devriez alors voir cette erreur ci-dessous :

![Comment ajouter ESLint à votre projet React](https://lh3.googleusercontent.com/O1FnEf68qsAo7FOqdNzFrcauVoHs3oKnQsbV4cNUAwFQbAjZZ9XhIHVhDSNiyZ3buIVF4-uCKnrkLjru6xRgjJo3tLJVq8vXn5s_GcdgnMoHCPPnDk0H2IGnhXVGPBZYABP3fbaoOe_GtYA60hU6Hw)
_Nous avons démarré le serveur local, et nous voyons une erreur provenant du fichier app.js. React doit être importé dans le fichier app.js. Nous devons exporter notre composant de bouton._

Cette erreur pourrait vous confondre, car vous ne savez peut-être pas d'où elle vient. Nous voyons cette erreur parce que nous avons configuré ESLint dans notre projet, et il analyse notre projet pour nous dire que React doit être importé dans le fichier **app.js**.

Mais exécutons ESLint pour voir d'où vient exactement l'erreur.

## Comment exécuter ESLint

Avec ESLint configuré, exécutons-le pour analyser notre composant SignupButton pour détecter les problèmes potentiels. Ouvrez votre terminal et exécutez la commande suivante à la racine de votre projet :

```javascript
npx eslint src/SignupButton.js
```

ESLint analysera le fichier SignupButton.js et affichera les problèmes qu'il trouve ci-dessous.

![Comment ajouter ESLint à votre projet React](https://www.freecodecamp.org/news/content/images/2023/08/image-101.png)
_Nous exécutons la commande `eslint` pour nous montrer où nous avons des erreurs : dans le bouton d'inscription et app.js_

## Comment corriger les problèmes ESLint

D'après ce qui précède, vous pouvez voir qu'ESLint identifie où nous avons des erreurs. Nous n'avons pas importé React dans notre fichier App.js, et nous n'avons pas exporté notre composant de bouton d'inscription. Corrigons cela.

![Comment ajouter ESLint à votre projet React](https://www.freecodecamp.org/news/content/images/2023/08/image-100.png)
_Nous avons importé React dans le fichier app.js et exporté le composant SignupButton._

Comme vous pouvez le voir, notre code a maintenant été compilé avec succès.

Nous avons pu exporter notre composant SignupButton et importer React dans le composant App.js. Cela résout notre problème.

Si ESLint identifie d'autres problèmes dans notre composant SignupButton, il les affichera avec des suggestions sur la façon de les corriger.

Par exemple, ESLint pourrait détecter des points-virgules manquants, des variables inutilisées ou des violations des meilleures pratiques React comme l'import React from "react" dans le fichier app.js.

En traitant les problèmes mis en évidence par ESLint, nous pouvons nous assurer que notre code respecte les meilleures pratiques, est plus facile à lire et contient moins de bugs potentiels.

## Conclusion

ESLint est un outil indispensable pour les développeurs React afin de maintenir la qualité du code et d'améliorer la productivité. En intégrant ESLint dans vos projets React, vous pouvez détecter les erreurs tôt, suivre les normes de codage et favoriser la collaboration au sein de votre équipe.

Dans cet article, j'ai expliqué comment configurer ESLint dans un projet React et démontrer ses avantages avec un simple composant de bouton d'inscription. En utilisant ESLint efficacement, vous pouvez écrire un code plus propre, plus cohérent et livrer des applications React de meilleure qualité.

Alors, pourquoi attendre ? Commencez à utiliser ESLint dans vos projets React et regardez la qualité de votre code s'envoler. Bon codage ! 🚀

Vos commentaires sont grandement appréciés.
Vous pouvez me suivre sur [twitter](https://twitter.com/_jayky) et [linkedIn](https://www.linkedin.com/in/isahjacob/)