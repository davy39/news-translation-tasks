---
title: Comment créer votre site portfolio en utilisant React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-29T12:45:23.000Z'
originalURL: https://freecodecamp.org/news/portfolio-app-using-react-618814e35843
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7snm7ve4mLm3kwrPl0r2ig.png
tags:
- name: JavaScript
  slug: javascript
- name: portfolio
  slug: portfolio
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer votre site portfolio en utilisant React.js
seo_desc: 'By Dhruv Barochiya

  After my friends canceled our weekend plans, I was looking for something to kill
  time. I finally ended up with a plan to create a portfolio website after going through
  my long pending list of ‘Wish-To-Do’ things.

  Many hours of sear...'
---

Par Dhruv Barochiya

Après que mes amis ont annulé nos plans de week-end, je cherchais quelque chose pour tuer le temps. J'ai finalement décidé de créer un site portfolio après avoir parcouru ma longue liste de choses « À faire ».

De nombreuses heures de recherche de technologies et de modèles plus tard, j'ai fini par créer [ce](https://dhruv34788.github.io/me/) site web en utilisant React.js et en le déployant avec GitHub Pages. Vous pouvez trouver le code du site web [ici](https://github.com/Dhruv34788/me) (techniquement, on l'appelle une « **web-app** », mais pour cet article, je vais l'appeler un « site web »... J'espère que c'est ok).

## Ce que vous allez apprendre

* Quelques concepts de base de React.js
* Comment utiliser create-react-app à partir d'un site web HTML
* Comment déployer votre site portfolio en utilisant « GitHub Pages »

## Quelques concepts que vous devez connaître avant de commencer...

> _Note — n'hésitez pas à sauter cette partie si vous êtes déjà familier avec les concepts de base de React.js et des composants React._
>
> _Ces points vous donneront une idée très basique du monde React. Je vous recommande vivement d'étudier davantage React à partir de la [documentation](https://reactjs.org/docs/getting-started.html) et de vous exercer avec l'aide de [freeCodeCamp](https://www.freecodecamp.org/)._

### Qu'est-ce que React.js ?

Pour l'instant, il suffit de savoir que React.js est la bibliothèque JavaScript utilisée pour construire des composants d'interface utilisateur. Elle a été créée par les ingénieurs de Facebook et, de nos jours, elle fait sensation dans le monde JavaScript.

### Qu'est-ce qu'un composant React ?

React vous permet de définir des composants comme une classe ou une fonction. Vous pouvez fournir des entrées optionnelles aux composants appelées « **props** ».

Les composants vous permettent de diviser l'interface utilisateur en sections **indépendantes** comme l'en-tête, le pied de page et le corps. Chaque composant fonctionnera indépendamment, donc n'importe quel composant individuel peut être rendu indépendamment dans le [ReactDOM](https://reactjs.org/docs/react-dom.html) sans affecter toute la page.

Il est également livré avec des « **méthodes de cycle de vie** » qui vous permettent de définir des morceaux de code que vous souhaitez exécuter selon l'état du composant comme le montage, le rendu, la mise à jour et le démontage.

Les composants React ont leurs propres compromis. Par exemple, nous pouvons réutiliser un composant en l'exportant vers d'autres composants, mais parfois il devient confus de gérer plusieurs composants qui communiquent et déclenchent des rendus les uns pour les autres.

Voici à quoi ressemble un composant !

```jsx
import React, { Component } from 'react'

export default class Component-name extends Component {
  render() {
    return (
      <div>
        {ce code sera rendu dans le DOM}
      </div>
    )
  }
}
```

### Qu'est-ce que [GitHub Pages](https://pages.github.com/) ?

Avec GitHub Pages, vous pouvez facilement déployer votre site en utilisant GitHub gratuitement et sans avoir besoin de configurer une infrastructure. Ils ont fourni des modules pour que vous n'ayez pas à vous soucier de nombreuses choses. Si vous restez jusqu'à la fin, vous verrez que cela fonctionne comme de la MAGIE !

## Avant de continuer, assurez-vous de...

### Décider du contenu que vous voulez mettre sur votre site web

Passez en revue votre dernier CV une fois (si vous n'en avez pas, alors [créez-en un maintenant](https://resumegenius.com/resume-templates) et reportez ce projet au week-end prochain ?). Cela vous aidera à avoir une idée claire du type d'informations que vous souhaitez mettre sur votre site portfolio.

### Trouver de l'inspiration

Parcourez les centaines de modèles de sites portfolio gratuits sur le web, voyez ce que vous pouvez utiliser — prenez un stylo et du papier et esquissez un diagramme approximatif pour avoir une idée de l'apparence de votre site web. J'utiliserai [ce](https://colorlib.com/preview/#jackson) modèle pour la démonstration.

### Rassembler quelques photos incroyables de vous-même

Bien sûr, vous ne voulez pas avoir l'air mal sur votre propre site portfolio. Alors fouillez dans vos archives de photos pour trouver les photos parfaites pour votre site.

### Écouter votre playlist préférée

La légende dit que **les bonnes choses n'arrivent qu'avec de la bonne musique...** _et_ vous ne voulez sûrement pas manquer de grandes choses.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7snm7ve4mLm3kwrPl0r2ig.png)
_[un aperçu de mon site portfolio](https://dbarochiya.github.io/me/" rel="noopener" target="_blank" title=")_

## Passons à la partie construction

Dans les sections suivantes, je vais décrire les étapes pour construire l'application portfolio, mais vous n'avez pas à suivre le même code que j'utilise. Concentrez-vous sur l'apprentissage des concepts et montrez un peu de créativité ! La lecture supplémentaire a été divisée en trois sections.

1. Configuration de l'application React
2. Décomposition de la page HTML en composants React
3. Déploiement de votre application sur GitHub Pages

### Configuration de l'application React

Nous allons utiliser `[create-react-app](https://facebook.github.io/create-react-app/docs/getting-started)` — un module fourni par Facebook — qui nous aide à créer des applications React.js facilement et sans nous soucier des outils de construction.

* Allez dans la console et exécutez `npm install create-react-app` pour installer ce module via npm (assurez-vous d'avoir installé `npm` avant de l'utiliser — suivez [ce](https://www.rosehosting.com/blog/install-npm-on-ubuntu-16-04/) lien pour plus d'informations).
* Exécutez maintenant `npm create-react-app ${project-name}` qui récupérera les scripts de construction et créera une structure de fichiers qui ressemblera à ceci.

```
my-portfolio-app
├── README.md (description du projet pour GitHub)
├── node_modules (stocke tous les modules dépendants du projet)
├── package.json (stocke toutes les méta-informations du projet comme les dépendances, la version, les révisions, etc.)
├── .gitignore (les fichiers déclarés ici seront ignorés lors du téléchargement sur GitHub comme node_modules
├── public (ici vous stockerez toutes les images, fichiers JS, CSS)
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src (notre code principal pour l'application se trouve ici)
    ├── {créer un dossier de composants ici}
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── serviceWorker.js
```

Créez un dossier `components` sous le répertoire `src`. C'est ici que nous stockerons nos composants à l'avenir.

* Copiez toutes les images, polices, fichiers HTML et CSS du modèle HTML que vous avez décidé d'utiliser dans le dossier `public`.

Maintenant, votre répertoire de projet devrait ressembler à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IcnlLThnGN65xfgkFpnnBg.png)
_structure des fichiers_

* Exécutez la commande `npm install` qui installera les modules dépendants sous le répertoire `node_module`.
* Si vous avez tout fait correctement jusqu'à présent, alors l'exécution de la commande `npm start` démarrera l'application React sur `localhost`. Allez sur `[https://localhost:3000](https://localhost:3000)` et vous devriez pouvoir voir la page de démarrage de l'application React.

### Décomposition de la page HTML en composants React...

Souvenez-vous du dossier `component` que nous avons créé sous le répertoire `src` à l'étape précédente, maintenant nous allons décomposer la page de modèle HTML en composants et combiner ces composants pour créer notre application React.

* Tout d'abord, vous devez identifier quels composants vous pouvez créer à partir du fichier HTML monolithique — comme l'en-tête, le pied de page et contactez-moi. Vous devez être un peu créatif ici !!
* Recherchez des balises comme _section/div_ qui ne sont pas imbriquées dans une autre _section/div_. Celles-ci doivent contenir le code concernant cette section particulière de la page qui est indépendante des autres sections. Essayez de regarder dans mon [_GitHub Repo_](https://github.com/Dhruv34788/me) pour avoir une meilleure idée de cela.
_Indice : Utilisez l'outil « **inspecter l'élément** » pour jouer avec le code et noter l'effet des changements dans le navigateur._
* Ces morceaux de code HTML seront utilisés dans la méthode `render()` du composant. La méthode `render()` retournera ce code chaque fois qu'un composant est rendu dans le ReactDOM. Jetez un coup d'œil aux blocs de code donnés ci-dessous pour référence.

```jsx
<section id="colorlib-hero" class="js-fullheight" data-section="home">
    <div class="flexslider js-fullheight">
        <ul class="slides">
        <li style="background-image: url(images/img_bg_1.jpg);">
            <div class="overlay"></div>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-6 col-md-offset-3 col-md-pull-3 col-sm-12 col-xs-12 js-fullheight slider-text">
                        <div class="slider-text-inner js-fullheight">
                            <div class="desc">
                                <h1>Salut ! <br>Je suis Jackson</h1>
                                <h2>100% html5 bootstrap templates Made by <a href="https://colorlib.com/" target="_blank">colorlib.com</a></h2>
                                    <p><a class="btn btn-primary btn-learn">Télécharger CV <em class="icon-download4"></em></a></p>
                                </div>
                        </div>
                    </div>
                </div>
            </div>
        </li>
        <li style="background-image: url(images/img_bg_2.jpg);">
            <div class="overlay"></div>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-6 col-md-offset-3 col-md-pull-3 col-sm-12 col-xs-12 js-fullheight slider-text">
                        <div class="slider-text-inner">
                            <div class="desc">
                                <h1>Je suis <br>un Designer</h1>
                                    <h2>100% html5 bootstrap templates Made by <a href="https://colorlib.com/" target="_blank">colorlib.com</a></h2>
                                    <p><a class="btn btn-primary btn-learn">Voir Portfolio <em class="icon-briefcase3"></em></a></p>
                                </div>
                        </div>
                    </div>
                </div>
            </div>
        </li>
        </ul>
    </div>
</section>
```

```jsx
import React, { Component } from 'react'

export default class Home extends Component {
  render() {
    return (
      <div>
        <section id="colorlib-hero" className="js-fullheight" data-section="home">
            <div className="flexslider js-fullheight">
                <ul className="slides">
                <li style={{backgroundImage: 'url(images/img_bg_1.jpg)'}}>
                    <div className="overlay" />
                    <div className="container-fluid">
                    <div className="row">
                        <div className="col-md-6 col-md-offset-3 col-md-pull-3 col-sm-12 col-xs-12 js-fullheight slider-text">
                        <div className="slider-text-inner js-fullheight">
                            <div className="desc">
                            <h1>Salut ! <br />Je suis Jackson</h1>
                            <h2>100% html5 bootstrap templates Made by <a href="https://colorlib.com/" target="_blank">colorlib.com</a></h2>
                            <p><a className="btn btn-primary btn-learn">Télécharger CV <em className="icon-download4" /></a></p>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </li>
                <li style={{backgroundImage: 'url(images/img_bg_2.jpg)'}}>
                    <div className="overlay" />
                    <div className="container-fluid">
                    <div className="row">
                        <div className="col-md-6 col-md-offset-3 col-md-pull-3 col-sm-12 col-xs-12 js-fullheight slider-text">
                        <div className="slider-text-inner">
                            <div className="desc">
                            <h1>Je suis <br />un Designer</h1>
                            <h2>100% html5 bootstrap templates Made by <a href="https://colorlib.com/" target="_blank">colorlib.com</a></h2>
                            <p><a className="btn btn-primary btn-learn">Voir Portfolio <em className="icon-briefcase3" /></a></p>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </li>
                </ul>
            </div>
        </section>
      </div>
    )
  }
}
```

Indice : Si les choses deviennent confuses du côté React — essayez de vous concentrer sur le concept de « comment identifier les futurs composants à partir de la base de code HTML ». Après vous être familiarisé avec React, l'implémentation sera un jeu d'enfant.

Avez-vous remarqué qu'il y a quelques changements dans le code HTML ? `class` est devenu `className`. Ces changements sont nécessaires car React ne supporte pas HTML ? — ils ont créé leur propre syntaxe HTML-like JS appelée [JSX](https://reactjs.org/docs/introducing-jsx.html). Donc, nous devons changer certaines parties du code HTML pour le rendre JSX.

Je suis tombé sur ce [converisseur HTML vers JSX](https://magic.reactjs.net/htmltojsx.htm) pendant ce projet, qui convertit le code HTML en JSX pour vous ?. Je recommande vivement d'utiliser cela plutôt que de changer votre code manuellement.

Après un certain temps, vous devriez obtenir quelques composants différents. Maintenant, la `FinDuJeu` est proche !! Combinez ces différents composants sous un seul composant `App.js` (OUI !! Vous pouvez rendre un composant à partir d'un autre composant !) et votre application portfolio sera prête.

```jsx
import React, { Component } from 'react';
import './App.css';
import Sidebar from './components/sidebar'
import Introduction from './components/introduction'
import About from './components/about'
import Projects from './components/projects'
import Blog from './components/blog'
import Timeline from './components/timeline'

class App extends Component {
  render() {
    return (
      <div id="colorlib-page">
        <div id="container-wrap">
		<Sidebar></Sidebar>
		<div id="colorlib-main">
			<Introduction></Introduction>
			<About></About>
			<Projects></Projects>
			<Blog></Blog>
			<Timeline></Timeline>
          	</div>
      	</div>
      </div>
    );
  }
}

export default App;
```

Remarquez dans le code ci-dessus que nous devons d'abord `importer` les composants pour pouvoir les utiliser dans la section `render()`. Et nous pouvons utiliser les composants simplement en ajoutant la balise `<nom-du-composant></nom-du-composant>` ou simplement `<nom-du-composant/>` dans la méthode de rendu.

* Exécutez `npm start` depuis votre terminal et vous devriez pouvoir voir les changements reflétés dans le site web. Vous n'avez pas besoin d'exécuter cette commande à nouveau si vous avez fait plus de changements dans le code, ils seront reflétés automatiquement lorsque vous enregistrerez ces changements. Vous pouvez faire un développement ultra-rapide grâce à la fonctionnalité de `[rechargement à chaud](https://facebook.github.io/react-native/blog/2016/03/24/introducing-hot-reloading)`.
* Jouez avec le HTML et le CSS pour changer le contenu selon votre CV et rendez votre portfolio encore plus cool en changeant le contenu, en essayant différentes polices, en changeant les couleurs et en ajoutant des photos de votre choix.

## Déployer l'application React sur GitHub Pages

D'accord, donc vous avez survécu jusqu'à ce point... prenez un moment pour apprécier votre travail acharné. Mais vous devez encore terminer votre déploiement afin de pouvoir partager votre travail cool avec vos amis qui ont annulé ces plans de week-end.

* Tout d'abord, vous devez installer la bibliothèque npm de GitHub Pages. Pour installer, exécutez cette commande `_npm install gh-pages_` sur votre terminal.

Maintenant, vous devez apporter les modifications suivantes à votre fichier `_manifest.json_` :

* Ajoutez le champ `_homepage_` — la valeur sera au format suivant — `[https://{github_id}.github.io/{github_repo}](https://{github_id}.github.io/{github_repo})`
* Ajoutez les champs `_predeploy_` et `_deploy_` sous `_scripts_`

Maintenant, votre manifest.json devrait ressembler à ceci :

```json
{
	"name": "portfolio-app",
	"version": "0.1.0",
	"private": true,
	"homepage": "https://Dhruv34788.github.io/me",
	"dependencies": {
		"gh-pages": "^2.0.1",
		"react": "^16.8.3",
		"react-dom": "^16.8.3",
		"react-scripts": "2.1.5",
		"yarn": "^1.13.0"},
	"scripts": {
		"start": "react-scripts start",
		"build": "react-scripts build",
		"predeploy": "yarn run build",
		"deploy": "gh-pages -d build",
		"test": "react-scripts test",
		"eject": "react-scripts eject"},
	"eslintConfig": {
		"extends": "react-app"},
	"browserslist": [
		">0.2%",
		"not dead",
		"not ie <= 11",
		"not op_mini all"
	]
}
```

Maintenant, allez dans le terminal, exécutez `npm run deploy` et attendez la magie !! Votre application sera déployée après l'exécution réussie des scripts de déploiement. Vérifiez si votre application a été déployée ou non en visitant le lien que vous avez fourni dans le champ `homepage`.

**_Attention_** : Veuillez être prudent lorsque vous déployez quoi que ce soit sur le web. Effectuez des vérifications de sécurité comme la suppression des liens internes, des mots de passe ou de tout ce que vous ne voulez pas voir entre les mains de personnes intelligentes.

## Si vous allez faire des changements souvent...

> _Note — Vous devez effectuer l'étape de déploiement chaque fois que vous changez quelque chose et si vous faites des changements dans la base de code — devinez qui va s'ennuyer bientôt !! (Pas de soucis, je vous couvre :P)_
>
> Vous pouvez automatiser le processus de déploiement en utilisant Travis-CI (outil d'automatisation), de sorte que si vous commitez quelque chose dans la branche master — les étapes de déploiement seront déclenchées et le nouveau site sera automatiquement disponible. Suivez cet article pour cela.
>
> [https://www.freecodecamp.org/news/learn-how-to-automate-deployment-on-github-pages-with-travis-ci/](https://www.freecodecamp.org/news/learn-how-to-automate-deployment-on-github-pages-with-travis-ci/)

## Devoirs pour vous...

Félicitations ! Vous avez enfin créé et déployé votre application portfolio. Si vous êtes intéressé, vous pouvez ajouter ces fonctionnalités à votre site web

* **Fonctionnalité de blog** : créez votre propre blog en utilisant Node.js et une base de données NoSQL comme MongoDB et fusionnez-le dans ce site portfolio.
* **Galerie** : ajoutez une section à la page où vous pouvez montrer le scénario des photos récentes de vos sites de médias sociaux.
* **Fil Twitter** : ajoutez une section montrant les tweets récents de vous.
* **Citation aléatoire** : ajoutez une section montrant quelques citations motivationnelles aléatoires.

Si vous implémentez l'une de ces fonctionnalités, partagez votre travail avec moi. Je serais plus qu'heureux de vous aider ? (si je peux ?)

## Conclusion...

Je voudrais prendre un moment pour reconnaître le travail des personnes qui m'ont donné l'inspiration et les connaissances pour compléter cet article.

* [**_Quincy_**](https://www.freecodecamp.org/news/portfolio-app-using-react-618814e35843/undefined) **_Larson, [Sahat Yalkabov](https://www.freecodecamp.org/news/portfolio-app-using-react-618814e35843/undefined) & communauté:_** Pour avoir créé **_freeCodeCamp —_** la plateforme où vous pouvez apprendre et acquérir des connaissances sur presque tout ce qui est lié aux technologies web ; en utilisant des tutoriels pratiques _et_ tout cela sans payer de frais. ?
* **_Colorlib:_** pour avoir fourni des modèles à la pointe de l'art qui ont été une énorme inspiration pour mon site portfolio. ?
* [**_Daniel Lo Nigro_**](https://www.freecodecamp.org/news/portfolio-app-using-react-618814e35843/undefined) **_& communauté:_** pour avoir créé [**_HTML to JSX_**](https://magic.reactjs.net/htmltojsx.htm) **_Compiler,_** qui s'est avéré pratique pour convertir des blocs HTML en code JSX. ?
* **_Mes amis les plus chers:_** qui m'ont aidé à corriger mes erreurs.
* **VOUS:** pour être resté jusqu'à la fin, j'espère que vous avez passé un moment productif. Continuez à explorer et à construire des choses incroyables !

![Image](https://cdn-media-1.freecodecamp.org/images/0*FgSZRsUOdqfFZJBY)
_Photo par [Unsplash](https://unsplash.com/@docrowdee?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Ruediger Theiselmann</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_