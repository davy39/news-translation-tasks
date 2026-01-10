---
title: Comment créer un Starter Next.js pour démarrer facilement une nouvelle application
  React
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-08-18T15:33:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-nextjs-starter-to-easily-bootstrap-a-new-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/nextjs-starter.jpg
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: react
- name: Sass
  slug: sass
seo_title: Comment créer un Starter Next.js pour démarrer facilement une nouvelle
  application React
seo_desc: "Getting started with a new React app is easier than ever with frameworks\
  \ like Next.js. But those frameworks don’t always include all of the tools you want\
  \ to use. \nHow can we use Starters to become super productive when starting a new\
  \ project with ou..."
---

Démarrer une nouvelle application React est plus facile que jamais avec des frameworks comme Next.js. Mais ces frameworks n'incluent pas toujours tous les outils que vous souhaitez utiliser. 

Comment pouvons-nous utiliser les Starters pour devenir super productifs lors du démarrage d'un nouveau projet avec nos outils préférés ?

* [Qu'est-ce que Next.js ?](#heading-questce-que-nextjs)
* [Qu'est-ce qu'un Starter ?](#heading-questce-quun-starter)
* [Que allons-nous construire ?](#heading-que-allonsnous-construire)
* [Ajout de Sass à un Starter Next.js](#heading-ajout-de-sass-a-un-starter-nextjs)
* [Configuration de la documentation du Starter Next.js pour une installation facile](#heading-configuration-de-la-documentation-du-starter-nextjs-pour-une-installation-facile)
* [Quelques autres choses à considérer](#heading-quelques-autres-choses-a-considerer)

%[https://www.youtube.com/watch?v=oFGs_x7kxZg]

## Qu'est-ce que Next.js ?

[Next.js](https://nextjs.org/) est un framework d'application de [Vercel](https://vercel.com/) qui vous permet de démarrer très rapidement une nouvelle application [React](http://reactjs.org/).

Certaines fonctionnalités de base incluent la création de [pages](https://nextjs.org/docs/basic-features/pages) et la [récupération de données](https://nextjs.org/docs/basic-features/data-fetching), et elles vous permettent de générer un site statique ou d'utiliser le rendu côté serveur pour charger dynamiquement votre application. 

En plus de cela, vous pouvez tirer parti de ses fonctionnalités avancées comme le [Routing](https://nextjs.org/docs/routing/introduction) ou la création d'une [API](https://nextjs.org/docs/api-routes/introduction) à côté de votre UI.

## Qu'est-ce qu'un Starter ?

Les Starters sont essentiellement un dépôt git sous forme de modèle qui vous permet de créer facilement une application préconfigurée.

Il n'y a rien de particulièrement spécial dans un Starter. À sa base, c'est une application Next.js qui a déjà été configurée d'une manière spécifique et généralement généralisée afin que tout le monde puisse l'utiliser.

Par exemple, si vous avez tendance à construire beaucoup d'applications de la même manière à chaque fois, vous devrez peut-être répéter les mêmes étapes de configuration chaque fois que vous créez une nouvelle application. 

Au lieu de cela, vous pouvez créer un Starter à partir duquel vous lancerez vos projets – et cela éliminera le besoin de répéter ces premières étapes à chaque fois.

## Que allons-nous construire ?

Nous allons construire un Starter Next.js de base qui vous permettra, à vous ou à toute autre personne, de créer rapidement et facilement un nouveau projet avec ce Starter comme point de départ.

Bien que nous n'irons pas trop loin dans les fonctionnalités, car le but ici est d'apprendre sur les Starters, nous testerons cela en ajoutant [Sass](https://sass-lang.com/) à Next.js afin que quelqu'un puisse facilement commencer avec les superpouvoirs CSS.

Vous pouvez consulter le [Starter](https://github.com/colbyfayock/next-sass-starter) sur GitHub : [github.com/colbyfayock/next-sass-starter](https://github.com/colbyfayock/next-sass-starter).

## Création d'un nouveau Starter Next.js

Pour commencer à créer un Starter, nous devons commencer par une application Next.js.

Nous pouvons faire cela en exécutant la commande suivante dans le répertoire où vous souhaitez créer cela :

```
yarn create next-app
# ou
npx create-next-app

```

Une fois que vous avez exécuté cela, Next.js vous demandera un nom de projet. Bien que vous puissiez utiliser ce que vous voulez, les Starters Next.js ont généralement un modèle de nom de `next-[nom]-starter`.

Donc, parce que nous créons un Starter Sass, je pourrais l'appeler `next-sass-starter`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/command-line-new-nextjs-app.jpg)
_Nouvelle application Next.js dans le terminal_

Une fois que Next.js a installé toutes nos dépendances, vous serez prêt à naviguer vers ce dossier et à exécuter la commande pour démarrer votre serveur de développement.

```
yarn dev
# ou
npm run dev

```

Et une fois que le serveur de développement est démarré, nous devrions être prêts à partir !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/new-nextjs-app-browser.jpg)
_Nouvelle application Next.js dans le navigateur_

À ce stade, nous avons pratiquement un Starter de base. Comme mentionné précédemment, il n'y a vraiment pas grand-chose de spécial avec un Starter Next.js. Donc si nous poussions cela sur Github, nous pourrions immédiatement commencer à l'utiliser "tel quel".

Vous pouvez tester cela en exécutant ce qui suit :

```
yarn create next-app [nom-du-projet] -e [URL GitHub]
# ou
npx create-next-app [nom-du-projet] -e [URL GitHub]

```

Après avoir exécuté cela, vous devriez être configuré avec un nouveau répertoire qui contient un projet créé à partir de votre Starter avec toutes les dépendances installées.

Mais nous voulons faire plus que cela. Notre objectif est d'ajouter des fonctionnalités qui aident à démarrer une application avec plus que la configuration par défaut, alors ajoutons Sass.

[Suivez le commit !](https://github.com/colbyfayock/next-colbyfayock-starter/commit/ed87ce9d6585b2b642adf7e6878d0fc01bba05ef)

## Ajout de Sass à un Starter Next.js

Note : Pour notre exemple, nous allons créer un Starter Sass comme le nom ci-dessus l'a peut-être impliqué. N'hésitez pas à ajouter les fonctionnalités que vous voulez à ce stade, qu'elles incluent Sass ou non. 

Rappelez-vous – le but ici sera de fournir quelque chose que nous pourrons utiliser lors de la création d'un nouveau projet avec ce Starter.

Ensuite, nous voulons réellement ajouter Sass à notre projet. Pour commencer, nous voulons installer sass comme dépendance :

```
yarn add sass
# ou
npm install sass

```

Ensuite, parce que Next.js recherche déjà `.scss` comme extension de fichier, nous pouvons simplement mettre à jour nos deux fichiers CSS sous le répertoire `styles` en `.scss`.

Donc, changez les fichiers suivants :

```
styles/globals.css => styles/globals.scss
styles/Home.module.css => styles/Home.module.scss

```

Ensuite, nous devons configurer nos instructions d'importation pour reconnaître nos nouvelles extensions de fichier.

Dans `pages/_app.js`, mettez à jour l'importation des styles en haut à :

```scss
import '../styles/globals.scss'

```

Et dans `pages/index.js`, mettez à jour l'importation des styles à :

```scss
import styles from '../styles/Home.module.scss'

```

À ce stade, vous pouvez démarrer votre serveur de développement et nous devrions toujours voir la page par défaut de Next.js.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/new-nextjs-app-browser.jpg)
_L'application Next.js devrait avoir la même apparence_

Pour voir notre Sass en action, nous pouvons mettre à jour certaines de nos classes pour utiliser des styles imbriqués au lieu de sélecteurs individuels.

Mettez à jour tous les sélecteurs `.footer` à l'intérieur de `styles/Home.module.scss` comme suit :

```scss
.footer {

  width: 100%;
  height: 100px;
  border-top: 1px solid #eaeaea;
  display: flex;
  justify-content: center;
  align-items: center;

  img {
    margin-left: 0.5rem;
  }

  a {
    display: flex;
    justify-content: center;
    align-items: center;
  }

}

```

Vous pouvez utiliser la même structure d'imbrication pour mettre à jour `.title` et `.card`.

Nous pouvons également ajouter ce qui suit en haut de notre fichier `styles/Home.module.css` :

```scss
$color-primary: #0070f3;

```

Et mettre à jour toutes les instances de la couleur dans ce fichier de `#0070f3` à `$color-primary` :

```scss
.title {
  ...
  a {
    color: $color-primary;

```

Si vous rechargez la page, rien ne changera. Mais mettez à jour cette variable avec votre couleur préférée comme :

```scss
$color-primary: blueviolet;

```

Et maintenant toutes les couleurs changent.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nextjs-app-updated-colors.jpg)
_Couleurs mises à jour dans l'application Next.js_

Enfin, puisque nous avons maintenant un Starter Sass, mettons à jour le titre de la page. Remplacez "Welcome to Next.js!" dans `pages/index.js` par :

```jsx
<h1 className={styles.title}>
  <a href="https://nextjs.org">Next.js</a> Sass Starter
</h1>

```

Et maintenant nous avons un point de départ Sass !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nextjs-app-updated-title.jpg)
_Titre mis à jour dans l'application Next.js_

Similaire à avant, vous pouvez tester cela en créant un nouveau projet avec votre Starter une fois que tous les changements sont sur GitHub.

```
yarn create next-app [nom-du-projet] -e [URL GitHub]
# ou
npx create-next-app [nom-du-projet] -e [URL GitHub]

```

[Suivez le commit !](https://github.com/colbyfayock/next-sass-starter/commit/56c5b67e8a383d8dc89c72d88cbe86adbac3edb8)

## Configuration de la documentation du Starter Next.js pour une installation facile

Arguablement, l'une des choses les plus importantes à propos d'un Starter est la documentation. 

Cela peut ne pas être aussi important si vous l'utilisez uniquement pour vous-même. Mais si vous voulez que d'autres personnes l'utilisent, vous voulez qu'elles sachent comment l'utiliser, sinon elles seront bloquées et deviendront frustrées.

La partie la plus importante est de configurer le Starter. Configurer votre Starter dans un dépôt GitHub est une excellente première étape. Mais si quelqu'un veut utiliser ce Starter, il devrait cloner ou télécharger ce dépôt et ensuite supprimer l'historique git.

Au lieu de cela, vous pouvez ajouter la commande que nous avons utilisée ci-dessus dans votre fichier `README.md` pour donner aux gens des instructions sur la façon de commencer rapidement, comme :

```mdx
## Getting Started

Run the following command to create a new project with this Starter:

```
yarn create next-app [project-name] -e https://github.com...
# or
npx create-next-app [project-name] -e https://github.com...
```

```

Cela empêchera les personnes qui ne savent peut-être pas comment faire certaines de ces choses manuellement de rester bloquées.

Il est également important d'ajouter toute documentation des options de configuration que vous avez ajoutées.

Si vous ajoutez des variables qui vous permettent de changer certaines fonctionnalités à l'échelle du site, assurez-vous d'ajouter des notes à ce sujet. 

Vous voulez finalement que les gens comprennent comment utiliser les fonctionnalités que vous avez ajoutées pour faciliter leur vie. S'ils ne les comprennent pas, ils pourraient simplement supprimer ce code et le faire manuellement.

En fin de compte, la création et la publication d'un Starter visent à faciliter la vie des gens. Que ce soit vous revenant à votre Starter quelques mois plus tard ou une foule de nouvelles personnes cherchant à être productives, vous leur offrez une meilleure expérience de développement en ajoutant une bonne documentation.

## Quelques autres choses à considérer

### Généralisation des fonctionnalités et ajout de configuration pour un Starter Next.js

Ajouter des fonctionnalités est un excellent moyen de rendre un Starter plus susceptible d'être utilisé. Si j'utilisais un Starter pour créer un nouveau blog, j'adorerais que ce Starter inclue mon nom en tant qu'auteur et peut-être même une page À propos de moi.

Mais ce que je ne voudrais pas, c'est devoir remplacer le nom de quelqu'un d'autre 100 fois dans tout le code pour mettre à jour mon propre projet. Sans parler, voir ce nom sur le Starter pourrait me faire sentir que c'est plus leur blog que un modèle que je peux utiliser pour mon projet.

Envisagez de commencer par utiliser un nom généralisé dans tout le projet. Au lieu d'utiliser Le Blog de Colby Fayock dans tout le Starter, faites-en Mon Blog, ce qui le rendra moins personnel pour le créateur pour la personne utilisant le Starter.

Ajoutez également quelques options de configuration. Il est beaucoup plus facile de pouvoir mettre à jour une seule variable qui ferait inclure Colby Fayock dans mon projet au lieu de Mon Blog que de rechercher tous les fichiers pour faire ce changement manuellement.

### Choisissez judicieusement où être opinionné

Lors de l'utilisation d'un outil comme Sass, il y a plus d'une façon d'utiliser cet outil. Si vous configurez une structure de projet incroyablement spécifique et opinionnée, vous alienez les personnes utilisant votre Starter. 

Cela les forcera soit à retravailler tout le projet, soit à vouloir supprimer un tas de code, ce qui pourrait les amener à éviter de vouloir l'utiliser à l'avenir.

Vous pouvez créer des Starters opinionnés, mais choisissez judicieusement où vous injectez ces opinions. Cela rendra votre travail utilisable par un plus grand groupe de personnes qui veulent être productives.

Si vous voulez créer quelque chose de très opinionné, envisagez de le nommer différemment et d'utiliser l'outil comme partie du nom. Par exemple, je pourrais créer un Starter Sass opinionné appelé Le Starter Next.js Sassy de Colby.

## Avez-vous créé un nouveau Starter ?

[Partagez-le avec moi sur Twitter !](https://twitter.com/colbyfayock)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">4E93FF Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsor Me</a>
    </li>
  </ul>
</div>