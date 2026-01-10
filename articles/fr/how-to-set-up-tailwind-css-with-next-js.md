---
title: Comment installer Tailwind CSS avec NextJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-07T21:37:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-tailwind-css-with-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Tutorials.png
tags:
- name: CSS
  slug: css
- name: Next.js
  slug: nextjs
- name: tailwind
  slug: tailwind
seo_title: Comment installer Tailwind CSS avec NextJS
seo_desc: "By Kelvin Moses\nTailwind CSS is a popular utility-first CSS framework\
  \ that offers a unique approach to building modern and responsive user interfaces.\
  \ \nUnlike traditional CSS frameworks that provide pre-designed components, Tailwind\
  \ CSS focuses on pr..."
---

Par Kelvin Moses

Tailwind CSS est un framework CSS populaire basé sur les utilitaires qui offre une approche unique pour construire des interfaces utilisateur modernes et réactives. 

Contrairement aux frameworks CSS traditionnels qui fournissent des composants préconçus, Tailwind CSS se concentre sur la fourniture d'un ensemble complet de classes utilitaires que vous pouvez appliquer directement à vos éléments HTML. 

Lorsqu'il est combiné avec Next.js, un puissant framework React pour construire des applications rendues côté serveur, vous pouvez débloquer une expérience de développement fluide et créer des applications web performantes et évolutives. 

Dans ce tutoriel, je vais vous guider à travers le processus d'installation de Tailwind CSS avec Next.js, afin que vous puissiez exploiter la puissance des classes utilitaires de Tailwind dans vos projets Next.js. 


### Prérequis

Avant de commencer, assurez-vous d'avoir les prérequis suivants :

1. Node.js installé sur votre machine
2. Connaissances de base en JavaScript et React
3. Familiarité avec Next.js


## Comment Tailwind CSS et les classes utilitaires fonctionnent

Tailwind CSS suit une approche basée sur les utilitaires pour le stylisme. Il fournit une vaste collection de petites classes utilitaires à usage unique que vous pouvez appliquer directement à vos éléments HTML. 

Chaque classe utilitaire représente une propriété CSS spécifique ou une combinaison de propriétés, ce qui facilite la création de composants UI complexes en composant ces classes ensemble. 

Par exemple, au lieu de définir une classe CSS personnalisée pour définir la couleur d'un bouton, vous pouvez simplement appliquer la classe utilitaire "text-blue-500" pour obtenir l'effet souhaité.

Les classes utilitaires dans Tailwind CSS sont conçues pour être hautement flexibles et personnalisables. Vous pouvez facilement ajuster des propriétés telles que la marge, le remplissage, la taille de la police, les couleurs, et plus encore en utilisant les conventions de nommage intuitives fournies par Tailwind. 

Cette approche offre un niveau de contrôle fin sur vos styles, éliminant le besoin d'écrire du CSS personnalisé pour la plupart des scénarios de stylisme courants.

## Pourquoi utiliser Tailwind CSS avec Next.js ?

Next.js est un framework puissant pour construire des applications React rendues côté serveur. Il offre une excellente expérience de développement et des fonctionnalités telles que le fractionnement automatique du code, le rendu côté serveur et la génération de sites statiques. 

Lorsque vous utilisez Next.js avec Tailwind CSS, cela vous permet d'intégrer sans effort les classes utilitaires de Tailwind dans votre flux de travail de développement d'applications.

Next.js optimise la livraison des styles CSS en supprimant automatiquement les CSS inutilisés lors du processus de construction. Cela signifie que même si Tailwind CSS fournit un ensemble complet de classes utilitaires, seuls les styles que vous utilisez réellement dans votre application seront inclus dans le bundle final. Cette approche garantit que votre application reste légère et performante.

En exploitant la combinaison de Tailwind CSS et Next.js, vous pouvez rapidement prototyper, concevoir et construire des interfaces utilisateur réactives tout en profitant des avantages d'un processus de développement rationalisé et de performances optimisées.

Maintenant que vous comprenez les avantages et la synergie entre Tailwind CSS et Next.js, plongeons dans le processus étape par étape de l'installation de Tailwind CSS avec Next.js.

## Étape 1 : Créer un nouveau projet Next.js

Pour commencer, créons un nouveau projet Next.js. Ouvrez votre terminal et exécutez la commande suivante :



``` bash 
npx create-next-app my-tailwind-project
```


Cela créera un nouveau projet Next.js nommé "my-tailwind-project" dans un répertoire du même nom.

## Étape 2 : Installer Tailwind CSS

Accédez au répertoire du projet en exécutant la commande suivante :

``` bash 
cd my-tailwind-project
```

Ensuite, installez Tailwind CSS et ses dépendances en exécutant la commande suivante :

``` bash 
    npm install tailwindcss postcss autoprefixer
```



## Étape 3 : Configurer Tailwind CSS

Après avoir installé Tailwind CSS, nous devons le configurer pour qu'il fonctionne avec Next.js. Créez un nouveau fichier nommé postcss.config.js dans le répertoire racine du projet et ajoutez le code suivant :

``` javascript 
module.exports = {
  plugins: [
    'tailwindcss',
    'postcss-flexbugs-fixes',
    'postcss-preset-env',
    [
      'postcss-normalize',
      {
        allowDuplicates: false,
      },
    ],
    [
      '@fullhuman/postcss-purgecss',
      {
        content: ['./pages/**/*.{js,jsx,ts,tsx}', './components/**/*.{js,jsx,ts,tsx}'],
        defaultExtractor: (content) => content.match(/[\\w-/:]+(?<!:)/g) || [],
      },
    ],
    'autoprefixer',
  ],
};


```

Cette configuration met en place Tailwind CSS, ajoute les plugins PostCSS nécessaires et inclut PurgeCSS pour supprimer le CSS inutilisé dans les builds de production.

## Étape 4 : Créer la configuration Tailwind CSS

Ensuite, nous devons générer un fichier de configuration par défaut pour Tailwind CSS. Ce fichier de configuration vous permet de personnaliser Tailwind CSS selon les besoins spécifiques de votre projet. Il définit la palette de couleurs, les paramètres de typographie, les utilitaires d'espacement, et plus encore.

Le fichier tailwind.config.js sert de hub de configuration central pour Tailwind CSS. Il fournit un objet JavaScript où vous pouvez définir vos personnalisations et étendre la configuration par défaut.

En générant le fichier de configuration par défaut, vous avez la flexibilité de modifier divers aspects de Tailwind CSS, y compris la personnalisation du thème, l'extension des classes utilitaires et la suppression du CSS inutilisé lors des builds de production.

La personnalisation du fichier de configuration vous permet d'adapter les classes utilitaires et le système de conception global pour les aligner sur les exigences de votre application et les directives de marque.


Générons maintenant le fichier de configuration par défaut pour Tailwind CSS. Exécutez la commande suivante :

``` bash 
npx tailwindcss init
```

Cela créera un fichier tailwind.config.js dans le répertoire racine de votre projet.

## Étape 5 : Personnaliser Tailwind CSS



Ouvrez le fichier tailwind.config.js et personnalisez Tailwind CSS selon les besoins de votre projet. Voici un exemple de ce à quoi un fichier tailwind.config.js personnalisé pourrait ressembler :

``` javascript

module.exports = {
  purge: ['./pages/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  darkMode: false,
  theme: {
    extend: {
      colors: {
        primary: '#FF0000',
        secondary: '#00FF00',
      },
      fontFamily: {
        sans: ['Roboto', 'Arial', 'sans-serif'],
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};

```



Dans cet exemple, nous personnalisons la configuration de Tailwind CSS en :

* Spécifiant les fichiers à purger à l'aide de l'option purge. Cela garantit que seules les classes CSS utilisées dans votre projet sont incluses dans le build final.
* Désactivant la fonctionnalité de mode sombre en définissant **darkMode** sur **false**.
* Étendant la palette de couleurs avec deux couleurs personnalisées : **primary** et **secondary**.
* Ajoutant une famille de polices personnalisée appelée **sans** qui inclut les polices Roboto, Arial et la police générique sans-serif de secours.
* Gardant les sections **variants** et **plugins** vides pour cette configuration de base.


Vous pouvez personnaliser davantage Tailwind CSS en explorant d'autres options de configuration disponibles dans la documentation officielle. Tailwind CSS offre une grande flexibilité, vous permettant d'adapter le framework aux exigences de conception spécifiques de votre projet.

Une fois que vous avez personnalisé le fichier tailwind.config.js, enregistrez-le et passez à l'étape suivante.

## Étape 6 : Importer les styles Tailwind CSS

Pour utiliser les styles Tailwind CSS dans votre projet Next.js, importez les styles dans votre fichier pages/_app.js. Ouvrez le fichier et ajoutez le code suivant :

``` javascript 
import 'tailwindcss/tailwind.css';

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

Cela importe les styles Tailwind CSS compilés et les applique à votre application entière.

## Étape 7 : Démarrer le serveur de développement

Maintenant, vous êtes prêt à démarrer le serveur de développement et à voir Tailwind CSS en action. Exécutez la commande suivante :

``` bash 
npm run dev
```

Visitez `http://localhost:3000` dans votre navigateur, et vous devriez voir votre application Next.js avec les styles Tailwind CSS appliqués.

Cela générera un build de votre application prêt pour la production, incluant uniquement les styles CSS nécessaires.

## Conclusion
Félicitations ! Vous avez réussi à installer Tailwind CSS avec Next.js. Vous pouvez maintenant commencer à exploiter les classes utilitaires de Tailwind pour construire rapidement de beaux composants UI réactifs dans vos projets Next.js. 

N'hésitez pas à explorer la documentation de Tailwind CSS pour découvrir la large gamme de classes utilitaires disponibles.


N'oubliez pas de mettre régulièrement à jour Tailwind CSS et ses dépendances pour bénéficier des dernières fonctionnalités et corrections de bugs.

Bon codage !😊
Connectons-nous [IamKelv](https://twitter.com/iam_kelvinjnr)