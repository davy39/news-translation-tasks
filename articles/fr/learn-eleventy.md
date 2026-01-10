---
title: Apprendre le générateur de site statique Eleventy en construisant et en déployant
  un site web de portfolio
subtitle: ''
author: Gerard Hynes
co_authors: []
series: null
date: '2022-09-06T16:26:13.000Z'
originalURL: https://freecodecamp.org/news/learn-eleventy
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/learn-eleventy.png
tags:
- name: eleventy
  slug: eleventy
- name: JavaScript
  slug: javascript
- name: Static Site Generators
  slug: static-site-generators
seo_title: Apprendre le générateur de site statique Eleventy en construisant et en
  déployant un site web de portfolio
seo_desc: 'What is Eleventy?

  Eleventy (also called 11ty) is a simple yet powerful static site generator. It uses
  JavaScript to transform data and templates into HTML pages.

  It’s beginner-friendly, has fast build times, and generates fast sites by default.
  It al...'
---

## Qu'est-ce qu'Eleventy ?

Eleventy (également appelé 11ty) est un générateur de site statique simple mais puissant. Il utilise JavaScript pour transformer des données et des templates en pages HTML.

Il est adapté aux débutants, a des temps de construction rapides et génère des sites rapides par défaut. Il dispose également d'une communauté très active et amicale.

Eleventy excelle dans les sites axés sur le contenu et est utilisé par [Google](https://web.dev/), [Netlify](https://www.netlify.com/), [MIT](https://digitalhumanities.mit.edu/), [CERN](https://worldwideweb.cern.ch/), [the A11y Project](https://www.a11yproject.com/), [ESLint](https://eslint.org/), et bien d'autres.

Puisque les pages sont générées à l'avance, elles peuvent être servies aussi rapidement que possible depuis un Content Delivery Network (CDN). Eleventy ne génère également aucun JavaScript côté client, ce qui aide votre site à se charger plus rapidement.

Dans ce tutoriel, nous allons construire un site de portfolio de développeur simple pour démontrer certaines des principales fonctionnalités d'Eleventy.

![Page d'accueil du portfolio Eleventy](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-29-at-17-46-26-Eleventy-Portfolio.png align="left")

*Page d'accueil du portfolio Eleventy*

Nous allons apprendre :

1. Configurer et configurer un projet Eleventy
   
2. Les templates et les layouts
   
3. Gérer le CSS et les images
   
4. Travailler avec les collections et les fichiers de données
   
5. Les shortcodes et les plugins Eleventy
   
6. Déployer le site sur Netlify
   

Le site de portfolio comprendra :

* Une page d'accueil
   
* Une page À propos
   
* Une page Contact (avec formulaire de contact)
   
* Une page Projets
   
* Une page pour chaque projet (avec étude de cas)
   

Eleventy peut récupérer des données depuis des APIs, un Content Management System (CMS), ou depuis des fichiers locaux. Pour garder les choses simples, nous allons stocker nos données de projet dans des fichiers Markdown.

Le code complet pour le portfolio terminé est [disponible sur GitHub](https://github.com/gerhynes/eleventy-portfolio). Si vous êtes bloqué à une étape, veuillez vérifier votre code par rapport au site terminé.

## Table des matières :

1. [Prérequis - Installer Node.js](#heading-prerequis-installer-nodejs)
   
2. [Configuration initiale du projet](#heading-configuration-initiale-du-projet)
   
3. [Comment configurer le projet](#heading-comment-configurer-le-projet)
   
4. [Comment ajouter un template](#heading-comment-ajouter-un-template)
   
5. [Comment utiliser les templates dans Eleventy](#heading-comment-utiliser-les-templates-dans-eleventy)
   
6. [Comment utiliser les layouts dans Eleventy](#heading-comment-utiliser-les-layouts-dans-eleventy)
   
7. [Comment configurer le CSS et les images](#heading-comment-configurer-le-css-et-les-images)
   
8. [Comment utiliser les partials dans Eleventy](#heading-comment-utiliser-les-partials-dans-eleventy)
   
9. [Comment utiliser les collections dans Eleventy](#heading-comment-utiliser-les-collections-dans-eleventy)
   
10. [Comment utiliser les fichiers de données de répertoire](#heading-comment-utiliser-les-fichiers-de-donnees-de-repertoire)
   
11. [Comment utiliser les collections dans les templates](#heading-comment-utiliser-les-collections-dans-les-templates)
   
12. [Comment utiliser les shortcodes](#heading-comment-utiliser-les-shortcodes)
   
13. [Comment utiliser le plugin Eleventy Image](#heading-comment-utiliser-le-plugin-eleventy-image)
   
14. [Comment construire un formulaire de contact avec Netlify Forms](#heading-comment-construire-un-formulaire-de-contact-avec-netlify-forms)
   
15. [Comment déployer sur Netlify](#heading-comment-deployer-sur-netlify)
   
16. [Où aller à partir de là](#heading-ou-aller-a-partir-de-la)
   

### Prérequis - Installer Node.js

Si vous n'avez pas déjà Node.js installé, allez sur [nodejs.org](https://nodejs.org/en/) et suivez les instructions pour votre système d'exploitation.

Ouvrez un terminal et utilisez `node --version` pour vous assurer qu'il est installé. Tant qu'il s'agit de la version 12 ou plus récente, vous êtes prêt à partir.

## Configuration initiale du projet

Tout d'abord, créez un répertoire pour votre portfolio. Vous pouvez l'appeler `eleventy-portfolio` ou ce que vous voulez.

Ouvrez ce répertoire dans un terminal et exécutez `npm init -y` pour créer un fichier `package.json` avec les paramètres par défaut.

Ensuite, installez Eleventy en utilisant `npm install --save-dev @11ty/eleventy`.

Dans le répertoire racine du projet, créez un fichier `.gitignore` avec le contenu suivant afin que Git ne suive pas les fichiers indésirables :

```python
node_modules
/public
```

## Comment configurer le projet

Eleventy est "zero-config" par défaut. Si vous ne changez rien, Eleventy prendra tous les fichiers dans votre répertoire racine, exécutera un processus de construction et sortira les fichiers résultants dans un répertoire `_site`.

Mais Eleventy dispose également d'options de configuration flexibles qui vous permettent de personnaliser votre processus de construction, de surveiller les changements dans certains types de fichiers et de manipuler le contenu avec des filtres et des shortcodes.

Votre configuration Eleventy se trouve dans un fichier `.eleventy.js` à la racine de votre projet.

Par exemple, le répertoire d'entrée par défaut est le répertoire racine de votre projet, tandis que le répertoire de sortie par défaut est `_site`. Certaines personnes préfèrent changer cela, avec `src` et `public` étant des choix courants.

Si vous souhaitez cette structure, créez des répertoires `src` et `public` à la racine de votre projet, puis définissez-les comme répertoires d'entrée et de sortie dans `.eleventy.js`.

```javascript
module.exports = function (eleventyConfig) {
  return {
    dir: {
      input: "src",
      output: "public"
    }
  };
};
```

Au cas où vous vous poseriez la question, l'argument `eleventyConfig` qui est passé à la fonction est l'objet de configuration par défaut qu'Eleventy fournit. Bientôt, nous allons utiliser cet objet pour personnaliser notre processus de construction Eleventy.

## Comment ajouter un template

Ajoutons notre premier template. Nous allons garder les choses aussi simples que possible en utilisant un fichier Markdown.

Dans le répertoire `src`, créez un `index.md` avec `# Hello World from Eleventy` comme contenu. C'est votre premier template Eleventy.

Pour construire et visualiser le site, nous pouvons utiliser le serveur de développement qui vient avec Eleventy.

Dans votre terminal, assurez-vous d'être dans le répertoire racine de votre projet et exécutez `eleventy --serve`. Cela démarre le serveur de développement, qui surveillera votre répertoire `src` et rechargera automatiquement votre site chaque fois que vous modifierez votre code.

Après un moment, vous verrez :

```python
[Browsersync] Access URLs:
 ----------------------------------
    Local: http://localhost:8080
 External: http://your_ip_address:8080
 ----------------------------------
[Browsersync] Serving files from: public
```

Ouvrez un navigateur web et allez sur [`http://localhost:8080`](http://localhost:8080). Félicitations, vous avez créé un site Eleventy (très simple) ! 🎉🎉

À ce stade, votre projet aura la structure suivante :

```python
node_modules/
public/
src/
.eleventy.js
.gitignore
package.lock.json
package.json
```

La plupart des sites ont besoin de plus d'une page, nous allons donc devoir en apprendre davantage sur les **templates**.

Avant de faire cela, nous pouvons personnaliser nos commandes de construction si nous le souhaitons. Cette étape est entièrement facultative.

### Étape facultative – Comment créer des commandes de construction personnalisées

La commande par défaut pour exécuter le serveur de développement est `eleventy --serve`, tandis que la commande par défaut pour construire le site est `eleventy`.

Si vous souhaitez remplacer celles-ci par des commandes différentes, telles que `start` et `build`, ouvrez `package.json` et sous `scripts`, remplacez la commande "test" par vos commandes préférées :

```json
"scripts": {
    "start": "eleventy --serve",
    "build": "eleventy"
  },
```

Maintenant, nous pouvons utiliser `npm start` dans le terminal pour démarrer le serveur de développement et `npm run build` pour générer une version de notre site.

Vous pouvez utiliser `ctrl/cmd` + `c` pour arrêter le serveur de développement chaque fois que vous en avez besoin.

## Comment utiliser les templates dans Eleventy

Transformer des fichiers Markdown en HTML est pratique, mais jusqu'à présent, vous ne tirez pas vraiment beaucoup d'avantages par rapport à l'écriture de votre site en HTML simple. C'est là que les **templates** entrent en jeu.

Tout d'abord, nous devons clarifier quelques termes :

* **Template** – Un fichier de contenu qu'Eleventy transformera en une page, ou des pages, dans le site construit
   
* **Layout** – Un template qui enveloppe un autre template, généralement pour fournir une structure pour présenter le contenu
   
* **Partial** – Un template qui fait partie d'un autre template
   

Les templates vous permettent de combiner du contenu et des données pour générer le HTML dont votre site a besoin.

Les layouts vous permettent de donner à plusieurs templates la même structure de base.

Les partials vous permettent de construire de petits composants réutilisables que vous pouvez utiliser dans des templates plus grands.

Eleventy prend en charge dix langues différentes pour les templates, y compris : HTML, Markdown, JavaScript, Liquid, Nunjucks, Handlebars, Mustache, EJS, Haml et Pug. (Dans la version 1.0, Eleventy a ajouté la prise en charge des templates personnalisés utilisant n'importe quelle extension de fichier arbitraire, mais cela est probablement mieux réservé pour des cas d'utilisation plus personnalisés/avancés).

Vous pouvez même mélanger différentes langues de templating dans le même fichier, comme Markdown et Nunjucks, si vous le souhaitez.

Dans ce projet, nous allons utiliser [Nunjucks](https://mozilla.github.io/nunjucks/). C'est un langage de templating pour JavaScript créé par Mozilla, et il est assez populaire dans la communauté Eleventy.

Dans le répertoire `src`, supprimez `index.md` et créez un fichier `index.njk`. Si vous utilisez VS Code, tapez `!` + `tab` pour générer la structure HTML de base de la page. Changez le titre en "Eleventy Portfolio" et dans l'élément `<body>`, ajoutez `<h1>Home Page</h1>`.

Votre page devrait ressembler à ceci :

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Eleventy Portfolio</title>
</head>
<body>
  <h1>Home Page</h1>
</body>
</html>
```

Ensuite, toujours dans `src`, créez les fichiers `about.njk` et `contact.njk`. Vous pouvez copier le contenu de `index.njk` dans ceux-ci et remplacer le `<h1>` par `<h1>About Page</h1>` et `<h1>Contact Page</h1>` respectivement.

Démarrez votre serveur de développement s'il n'est pas déjà en cours d'exécution. Allez sur [`http://localhost:8080`](http://localhost:8080) pour voir la page d'accueil, `http://localhost:8080/about` pour la page À propos, et `http://localhost:8080/contact` pour la page Contact.

Dans notre site de portfolio, chacune de ces pages aura la même structure de base. Au lieu d'écrire le même code dans chaque template de page, nous allons utiliser les **layouts** d'Eleventy.

## Comment utiliser les layouts dans Eleventy

Les layouts sont des templates qui enveloppent d'autres templates, présentant le contenu de manière cohérente.

À l'intérieur du répertoire `src`, créez un répertoire `_includes`. Celui-ci contiendra tous nos layouts et partials.

À l'intérieur de `_includes`, créez un fichier `base.njk`. Celui-ci fournira un layout standard pour chaque page de notre site.

Copiez le code suivant dans `base.njk` :

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Je suis un développeur logiciel frontend qui construit des sites et des applications qui aident les gens à atteindre leurs objectifs personnels et professionnels."/>
  <title>{{ title }}</title>
</head>
<body>
  <div class="content">
    <header class="header container">
    <h1 class="header__title">
      <a href="/">Marie Jackson</a>
    </h1>
    <ul class="header__links">
      <li>
        <a class="header__link" href="/about">À propos</a>
      </li>
      <li>
        <a class="header__link" href="/projects">Projets</a>
      </li>
      <li>
        <a class="header__link" href="/contact">Contact</a>
      </li>
    </ul>	</header>
    <main class="main container">
      {{ content | safe }}
    </main>
  </div>
  <footer class="footer">
  	<p>&copy; Marie Jackson 2022</p>
  </footer>
</body>
</html>
```

La valeur `content` sera le contenu principal du template que nous utilisons avec `base.njk` comme layout. `safe` est un filtre qui empêche ce contenu d'être échappé (avoir des caractères potentiellement dangereux remplacés).

Maintenant, changez `index.njk` pour qu'il soit :

```python
---
title: "Eleventy Portfolio"
layout: "base.njk"
---

<h1>{{ title }} Home Page</h1>
```

Remarquez comment le template a des données de frontmatter en haut du fichier. Par défaut, cela est écrit en YAML, mais vous pouvez utiliser d'autres langues aussi.

Ce frontmatter vous permet de définir des valeurs pour vos templates. Dans ce cas, la valeur `layout` indique au template d'utiliser le layout `base.njk` et la valeur `title` fournit un titre que nous utilisons dans la balise `<h1>` de notre template.

Ensuite, supprimez tout de `about.njk` et collez le contenu suivant :

```python
---
title: "Eleventy Portfolio"
layout: "base.njk"
---

<section class="bio prose">
  <h2 class="heading--main">Mon histoire</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aliquet risus feugiat in ante metus dictum.</p>
 
  <p>Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Turpis egestas integer eget aliquet. Vestibulum morbi blandit cursus risus at ultrices mi tempus. Ut lectus arcu bibendum at. Integer enim neque volutpat ac tincidunt.</p>
 
  <p>Commodo ullamcorper a lacus vestibulum sed arcu. Et tortor consequat id porta nibh venenatis cras sed. Nulla pharetra diam sit amet nisl. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis a. Nec sagittis aliquam malesuada bibendum.</p>
 
  <p>Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Turpis egestas integer eget aliquet. Vestibulum morbi blandit cursus risus at ultrices mi tempus. Ut lectus arcu bibendum at. Integer enim neque volutpat ac tincidunt.</p>
 
  <p>Commodo ullamcorper a lacus vestibulum sed arcu. Et tortor consequat id porta nibh venenatis cras sed. Nulla pharetra diam sit amet nisl. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis a. Nec sagittis aliquam malesuada bibendum.</p>
</section>
```

Maintenant, supprimez tout de `contact.njk` et collez ce contenu :

```python
---
title: "Eleventy Portfolio"
layout: "base.njk"
---

<h2 class="heading--main text-center">Vous voulez entrer en contact ?</h2>
<p class="contact__sub-heading text-center">Je suis toujours ouvert à de nouvelles opportunités et projets. </p>

<form class="form" name="contact" action="/success" method="POST" data-netlify="true">
  <div class="form__section">
    <label class="form__label" for="yourName">Nom</label>
    <input class="form__input" name="name" type="text" id="yourName" required="true">
  </div>
  <div class="form__section">
    <label class="form__label" for="yourEmail">Email</label>
    <input class="form__input" name="email" type="email"  id="yourEmail" required="true">
  </div>
  <div class="form__section">
    <label class="form__label" for="message">Message</label>
    <textarea class="form__input" name="message" id="message" rows="4" required="true"></textarea>
  </div>
    <button class="form__button" type="submit">Parlons</button>
</form>
```

Nous allons apprendre comment ce formulaire de contact fonctionnera plus tard dans le tutoriel.

Notre portfolio commence à prendre forme, même si les choses semblent encore très simples. Continuons avec notre CSS et nos images.

## Comment configurer le CSS et les images

Bien qu'Eleventy puisse comprendre les langues de templating prises en charge dès la sortie de la boîte, il doit être configuré pour traiter les fichiers CSS et les images. Heureusement, cela ne nécessite pas beaucoup de configuration. Pendant que nous y sommes, nous allons également ajouter un favicon au site.

À l'intérieur du répertoire `src`, créez trois dossiers : `css`, `images` et `favicons`.

![Structure du répertoire src](https://www.freecodecamp.org/news/content/images/2022/08/src.PNG align="left")

*Structure du répertoire src*

À l'intérieur du répertoire `css`, créez un fichier `style.css`. Puisque ce n'est pas un tutoriel CSS, je vais fournir le CSS dans [le dépôt GitHub du projet](https://github.com/gerhynes/eleventy-portfolio/tree/main/src). Vous pouvez le copier et le coller à partir de là, mais je ne vais pas couvrir le CSS en profondeur.

Les images pour ce portfolio sont également disponibles dans le répertoire `images` du dépôt GitHub. Copiez ces images dans le répertoire `images` de votre projet.

Enfin, copiez les fichiers du répertoire `favicons` du dépôt GitHub dans le répertoire `favicons` de votre projet.

Dans `base.njk`, ajoutez ces lignes à l'élément `<head>` :

```python
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{'/css/style.css' | url | safe}}">
```

Les deux premiers liens incluent le favicon, les trois suivants récupéreront la police Inter depuis Google Fonts, et le dernier connectera `style.css` à `base.njk`.

Maintenant, si nous rechargeons notre page d'accueil, nous verrons que... absolument rien n'a changé.

Par défaut, Eleventy ne traitera que les fichiers de template. Pour lui dire d'inclure les fichiers CSS et les images, nous devons ajouter quelques lignes de configuration.

Ajoutez ces lignes à la fonction de configuration dans `.eleventy.js` :

```javascript
module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("./src/css/");
  eleventyConfig.addWatchTarget("./src/css/");
  eleventyConfig.addPassthroughCopy("./src/images/");
  eleventyConfig.addPassthroughCopy({ "./src/favicons": "/" });

  return {
    dir: {
      input: "src",
      output: "public"
    }
  };
};
```

`addPassthroughCopy` indique à Eleventy de transmettre les fichiers CSS, favicons et images à la construction finale.

`addWatchTarget` indique au serveur de développement Eleventy de surveiller le répertoire `css` et de recharger le site si les fichiers de ce répertoire changent.

Avec les favicons, nous indiquons également à Eleventy de sortir ces fichiers à la racine du contenu généré afin que les liens dans `base.njk` fonctionnent.

Redémarrez le serveur et vous verrez que le CSS est enfin appliqué et que le favicon apparaît. Nous inclurons les images sous peu.

![Page d'accueil avec les styles appliqués](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-17-19-57-Eleventy-Portfolio.png align="left")

*Page d'accueil avec les styles appliqués*

![Page À propos avec les styles appliqués.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-18-16-28-Eleventy-Portfolio.png align="left")

*Page À propos avec les styles appliqués*

![Page Contact avec les styles appliqués.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-18-17-08-Eleventy-Portfolio.png align="left")

*Page Contact avec les styles appliqués*

La page À propos et la page Contact sont assez autonomes. Mais la page d'accueil de notre site aura plusieurs parties. Elle se composera d'un en-tête et d'un pied de page, ainsi que d'une section de profil, d'une section de technologies et d'une section de projets. Chacune de ces parties utilisera un **partial**.

![Disposition de la page d'accueil du portfolio.](https://www.freecodecamp.org/news/content/images/2022/08/layout.png align="left")

*Disposition de la page d'accueil du portfolio*

## Comment utiliser les partials dans Eleventy

Les partials sont des templates qui font partie d'un autre template. Les partials nous aident à penser à notre site en termes de composants réutilisables que nous pouvons inclure chaque fois que nous en avons besoin.

Dans le répertoire `_includes`, créez un fichier `header.njk` et `footer.njk`.

Coupez l'élément header de `base.njk` et collez-le dans `header.njk`.

Coupez l'élément footer de `base.njk` et collez-le dans `footer.njk`.

Dans `base.njk`, ajoutez `{% include "header.njk" %}` où se trouvait l'élément header et `{% include "footer.njk" %}` où se trouvait l'élément footer.

`base.njk` devrait maintenant avoir ce contenu à l'intérieur de sa balise `<body>` :

```python
<div class="content">
    {% include "header.njk" %}
    <main class="main container">
      {{ content | safe }}
    </main>
</div>
{% include "footer.njk" %}
```

Le site n'aura pas l'air différent, mais notre layout de base devient déjà plus modulaire.

Ensuite, toujours dans le répertoire `_includes`, créez un fichier `profile.njk` avec le contenu suivant :

```python
<section class="profile">
  <div class="profile__image-wrapper">
    <img class="profile__image" src="/images/profile.jpg" alt="Marie Jackson, Développeuse Logiciel">
  </div>
  <div class="profile__card">
    <p class="profile__text">Salut ! Je suis <span class="profile__text--highlight">Marie</span>, une mathématicienne devenue développeuse logiciel de Hampton, Virginie.</p>
    <p class="profile__text">En tant que <span class="profile__text--highlight">Développeuse Frontend</span>, j'adore construire des sites et des applications qui aident les gens à atteindre leurs objectifs personnels et professionnels.</p>
    <p class="profile__text">Je me concentre sur la vitesse, la sécurité et la scalabilité, en utilisant React.js et Firebase pour créer des expériences riches et dynamiques.</p>
    <p class="profile__text">Je suis toujours ouverte à de nouvelles opportunités et projets. Alors n'hésitez pas à <a class="profile__link" href="/contact">entrer en contact</a>.<p>
  </div>
</section>
```

Ensuite, créez un fichier `technologies.njk` avec ce contenu :

```python
<section class="technologies">
  <h2 class="technologies__heading">Technologies que j'aime utiliser</h2>
  <ul class="technologies__list">
    <li class="technologies__item">
      <div class="technologies__logo">
      <img src="/images/javascript.svg" alt="Logo JavaScript">
      </div>
      <h3 class="technologies__title">JavaScript</h3>
    </li>
    <li class="technologies__item">
      <div class="technologies__logo">
      <img src="/images/react.svg" alt="Logo React.js">
      </div>
      <h3 class="technologies__title">React.js</h3>
    </li>
    <li class="technologies__item">
      <div class="technologies__logo">
        <img src="/images/tailwindcss.svg" alt="Logo Tailwind CSS">
      </div>
      <h3 class="technologies__title">Tailwind CSS</h3>
    </li>
    <li class="technologies__item">
      <div class="technologies__logo">
        <img src="/images/firebase.svg" alt="Logo Firebase">
      </div>
      <h3 class="technologies__title">Firebase</h3>
    </li>
  </ul>
</section>
```

Dans `index.njk`, remplacez la balise `<h1>` par :

```python
{% include "profile.njk" %}
{% include "technologies.njk" %}
```

![Page d'accueil du portfolio avec les sections profil et technologies.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-18-15-11-Eleventy-Portfolio.png align="left")

*Page d'accueil du portfolio avec les sections profil et technologies*

Notre page d'accueil commence à prendre forme, mais le site a encore besoin de la partie la plus importante de tout portfolio : les projets.

Pour garder les données de projet organisées, nous allons utiliser des **collections**.

## Comment utiliser les collections dans Eleventy

Les collections vous permettent de regrouper du contenu lié. Dans notre portfolio, nous allons créer une collection `projects` en utilisant des fichiers Markdown pour stocker des informations sur chaque projet individuel.

À l'intérieur du répertoire `src`, créez un répertoire `projects`. Nous aurons besoin d'un fichier Markdown pour chaque projet. En tant que placeholders, nous utiliserons trois projets que j'ai eu l'intention de construire.

Josh W Comeau a quelques excellents conseils sur [la construction d'un portfolio de développeur efficace](https://www.joshwcomeau.com/effective-portfolio/) et il recommande fortement de décrire vos projets personnels avec des études de cas détaillées. Donc pour chacun de nos projets, nous allons avoir une étude de cas exposant :

* Quel problème nous avons résolu
   
* Pourquoi nous avons choisi ces technologies spécifiques
   
* Quels défis nous avons rencontrés
   
* Quelles leçons nous avons apprises
   

Copiez les trois projets d'exemple suivants dans le répertoire `projects` :

`catch-up.md`

```markdown
---
title: "Catch Up"
summary: "Parfois, il est difficile de rester en contact avec ses amis et sa famille. J'ai créé cette application pour me rappeler de planifier un appel si nous n'avons pas parlé depuis un moment."
image: /images/catch-up.jpg
imageAlt: "Captures d'écran de l'application catch up"
tech:
  - "Next.js"
  - "Firebase"
  - "Tailwind CSS"
siteUrl: "#"
repoUrl: "#"
---

### Problème résolu

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tincidunt tortor aliquam nulla facilisi. Feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit. Condimentum lacinia quis vel eros donec ac odio tempor orci.

### Technologies utilisées

Scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Diam sit amet nisl suscipit adipiscing bibendum est ultricies. Consequat ac felis donec et odio pellentesque diam volutpat commodo.

### Défis rencontrés

Eget mauris pharetra et ultrices. Molestie nunc non blandit massa enim nec. Ut tortor pretium viverra suspendisse potenti nullam ac tortor vitae. Nulla at volutpat diam ut venenatis. Volutpat ac tincidunt vitae semper quis lectus nulla at.

### Leçons apprises

Non blandit massa enim nec. Tempor commodo ullamcorper a lacus vestibulum sed. Et netus et malesuada fames ac turpis egestas integer eget. In ante metus dictum at tempor commodo. Eu scelerisque felis imperdiet proin fermentum leo.
```

`sourdough-sensei.md`

```markdown
---
title: "Sourdough Sensei"
summary: "Comme beaucoup de gens, je me suis vraiment mis au pain au levain en 2020. J'ai créé cette application pour m'aider à cuire du pain délicieux en mettant toutes mes recettes et mes plannings au même endroit."
image: /images/sourdough-sensei.jpg
imageAlt: "Captures d'écran de l'application de pain au levain"
tech:
  - "React.js"
  - "Firebase"
  - "Tailwind CSS"
siteUrl: "#"
repoUrl: "#"
---

### Problème résolu

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tincidunt tortor aliquam nulla facilisi. Feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit. Condimentum lacinia quis vel eros donec ac odio tempor orci.

### Technologies utilisées

Scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Diam sit amet nisl suscipit adipiscing bibendum est ultricies. Consequat ac felis donec et odio pellentesque diam volutpat commodo.

### Défis rencontrés

Eget mauris pharetra et ultrices. Molestie nunc non blandit massa enim nec. Ut tortor pretium viverra suspendisse potenti nullam ac tortor vitae. Nulla at volutpat diam ut venenatis. Volutpat ac tincidunt vitae semper quis lectus nulla at.

### Leçons apprises

Non blandit massa enim nec. Tempor commodo ullamcorper a lacus vestibulum sed. Et netus et malesuada fames ac turpis egestas integer eget. In ante metus dictum at tempor commodo. Eu scelerisque felis imperdiet proin fermentum leo.
```

`spellbook.md`

```markdown
---
title: "Spellbook"
summary: "Je suis un grand fan de Donjons et Dragons, mais garder mes sorts en ordre a toujours été un défi. J'ai construit cette application pour mettre toutes les informations dont j'ai besoin à portée de main."
image: /images/spellbook.jpg
imageAlt: "Captures d'écran du projet DnD"
tech:
  - "Next.js"
  - "Firebase"
  - "Tailwind CSS"
siteUrl: "#"
repoUrl: "#"
---

### Problème résolu

Oui, j'aurais pu simplement utiliser DnD Beyond. Mais où est le plaisir dans tout ça ? Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tincidunt tortor aliquam nulla facilisi. Feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit. Condimentum lacinia quis vel eros donec ac odio tempor orci.

### Technologies utilisées

Scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Diam sit amet nisl suscipit adipiscing bibendum est ultricies. Consequat ac felis donec et odio pellentesque diam volutpat commodo.

### Défis rencontrés

Eget mauris pharetra et ultrices. Molestie nunc non blandit massa enim nec. Ut tortor pretium viverra suspendisse potenti nullam ac tortor vitae. Nulla at volutpat diam ut venenatis. Volutpat ac tincidunt vitae semper quis lectus nulla at.

### Leçons apprises

Non blandit massa enim nec. Tempor commodo ullamcorper a lacus vestibulum sed. Et netus et malesuada fames ac turpis egestas integer eget. In ante metus dictum at tempor commodo. Eu scelerisque felis imperdiet proin fermentum leo.
```

Tout comme avec les templates, le frontmatter en haut de ces fichiers rend les valeurs disponibles que vous pouvez injecter dans vos templates.

Puisque ces fichiers Markdown sont finalement à l'intérieur du répertoire `src`, Eleventy les traitera comme des templates et créera une page HTML à partir de chaque fichier. Leur URL sera au format `/nom_sous_repertoire/nom_fichier`, par exemple `/projects/sourdough-sensei`.

Mais Eleventy ne saura pas quel layout utiliser pour ces pages puisqu'elles n'ont pas encore de valeur `layout` dans leur frontmatter.

![Page sourdough-sensei sans layout ou données de frontmatter](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-19-08-18-Screenshot.png align="left")

*Page sourdough-sensei sans layout ou données de frontmatter*

Pour l'instant, ces fichiers ne font pas partie d'une collection. Les collections sont définies par le partage d'une valeur `tags`, comme `"tags": "projects"`.

Chaque fichier avec le tag `projects` sera inclus dans la collection `projects`.

Puisque nous n'avons que trois projets, nous pourrions inclure une valeur `tags` dans le frontmatter de nos trois fichiers Markdown.

Mais si nous avions un site avec beaucoup de contenu – par exemple, des dizaines d'articles de blog, des conférences enregistrées et des tutoriels qui partagent tous des dizaines de tags entre eux – cela pourrait devenir difficile à gérer. C'est là que les **fichiers de données de répertoire** sont utiles.

### Comment utiliser les fichiers de données de répertoire

Si vous avez certaines valeurs qui sont partagées par chaque fichier dans un dossier, vous pouvez mettre ces valeurs dans un fichier de données de répertoire.

À l'intérieur du répertoire `projects`, créez un fichier `projects.json`. Un fichier de données de répertoire doit avoir le même nom que la collection à laquelle il est attaché.

Tous les champs de frontmatter qui sont partagés par tous les fichiers de projets doivent aller dans le fichier de données de répertoire `projects.json` :

```json
{
  "layout": "project.njk",
  "tags": "projects"
}
```

La valeur `layout` signifie que chaque projet utilisera le même layout (nous allons créer ce fichier `project.njk` dans un instant). La valeur `tags` est ce qui les transforme en collection `projects` que nous pouvons utiliser dans nos templates.

## Comment utiliser les collections dans les templates

Nous allons maintenant utiliser la collection `projects` pour :

* Ajouter une section projets à notre page d'accueil
   
* Créer une page Projets
   
* Créer une page d'étude de cas pour chaque projet
   

Pour inclure des données d'une collection sur une page de votre site, vous devez référencer l'objet `collections` dans un template.

Nous pouvons utiliser Nunjucks pour parcourir la collection et afficher son contenu. Pour accéder à une valeur de frontmatter d'un `project` dans la collection `projects`, nous utilisons `project.data`.

Par exemple :

```python
{% for project in collections.projects %}
{{ project.data.title }}
{% endfor %}
```

Dans le répertoire `_includes`, créez les fichiers `project.njk`, `project-card.njk` et `project-grid.njk`.

![Structure du répertoire _includes.](https://www.freecodecamp.org/news/content/images/2022/08/includes.PNG align="left")

*Structure du répertoire _includes*

Nous allons utiliser `project.njk` pour créer une page pour chacun de nos projets.

Puisque ces pages sont générées à partir de templates, nous pouvons accéder directement à leurs valeurs de frontmatter, telles que `title`, `image`, `imageAlt`, et `content` pour le contenu principal du fichier Markdown.

```python
---
layout: "base.njk"
---

<div class="project">
  <h2 class="project__heading">{{ title }}</h2>
  <div class="project__image-wrapper">
      <img class="project__image" src="{{ image }}" alt="{{ imageAlt }}">
  </div>
  <div class="project__content prose">
    {{ content | safe }}
  </div>
</div>
```

`project-grid.njk` et `project-card.njk` formeront la liste des projets sur notre page d'accueil de portfolio et la page Projets.

`project-grid.njk` parcourra la collection `projects` et insérera un partial `project-card` pour chaque projet dans la collection.

Ajoutez le contenu suivant à `project-grid.njk` :

```python
<section class="projects">
  <h2 class="project__heading">Projets récents</h2>
  <div class="project-grid">
    {% for project in collections.projects %}
      {% include "project-card.njk" %}
    {% endfor %}
  </div>
</section>
```

Ajoutez le contenu suivant à `project-card.njk` :

```python
<article class="project-card">
  <div class="project-card__image-wrapper">
    <img class="project__image" src="{{ project.data.image }}" alt="{{ project.data.imageAlt }}">
  </div>
  <div class="project-card__body">
    <div class="project-card__tags">
      {% for tag in project.data.tech %}
        <span class="project-card__tag">{{ tag }}</span>
      {% endfor %}
    </div>
    <h3 class="project-card__title">
      <a href="{{ project.url }}">{{ project.data.title }}</a>
    </h3>
    <p class="project-card__summary">{{ project.data.summary }}</p>
    <a class="project-card__link" href="{{ project.url }}">Lire l'étude de cas du projet
      <svg xmlns="http://www.w3.org/2000/svg" class="project-card__link-icon" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
      </svg>
    </a>
  </div>
</article>
```

Puisque `project-card.njk` accède aux valeurs de frontmatter d'un membre d'une collection, nous devons utiliser `project.data` pour accéder à ces valeurs dans le template. Eleventy génère également une valeur `project.url` que nous pouvons utiliser pour lier à la page générée du projet.

Dans `index.njk`, ajoutez `{% include "project-grid.njk" %}` sous les partials de profil et de technologies.

```python
---
title: "Eleventy Portfolio"
layout: "base.njk"
---

{% include "profile.njk" %}
{% include "technologies.njk" %}
{% include "project-grid.njk" %}
```

![Grille de cartes de projet sur la page d'accueil.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-19-41-45-Eleventy-Portfolio.png align="left")

*Grille de cartes de projet sur la page d'accueil*

Ensuite, nous allons créer une page Projets. Dans le répertoire `src`, créez un fichier `projects.njk` avec le contenu suivant :

```python
---
title: "Eleventy Portfolio"
layout: "base.njk"
---

<h2 class="projects__heading">Projets récents</h2>
<div class="project-list">
  {% for project in collections.projects %}
    {% include "project-card.njk" %}
  {% endfor %}
</div>
```

![Page Projets.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-19-25-32-Eleventy-Portfolio.png align="left")

*Page Projets*

Les projets sont maintenant affichés sur notre page d'accueil ainsi que sur la page des projets, et chaque projet a maintenant sa propre page avec son étude de cas.

Nous pourrions nous arrêter ici, mais il y a quelques fonctionnalités supplémentaires d'Eleventy qui rendront notre site de portfolio encore meilleur, à savoir les **shortcodes** et les **plugins**.

### Comment utiliser les shortcodes

Un shortcode est un moyen d'injecter du contenu réutilisable (souvent un littéral de modèle de chaîne JavaScript) dans vos templates.

Nous allons créer un simple shortcode `year` qui affiche l'année en cours afin que le pied de page de notre site de portfolio soit toujours à jour.

Ajoutez la ligne suivante à la fonction de configuration dans `.eleventy.js`.

```javascript
eleventyConfig.addShortcode("year", () => `${new Date().getFullYear()}`);
```

Lorsque vous utilisez le shortcode dans un template, la fonction sera exécutée et la valeur `year` sera injectée dans le template.

Dans `footer.njk`, utilisez `{% year %}` pour accéder au shortcode `year`.

```python
<footer class="footer">
  <p>&copy; Marie Jackson {% year %}</p>
</footer>
```

Vous devrez peut-être redémarrer votre serveur de développement pour qu'il reconnaisse le shortcode.

Maintenant, chaque fois que vous déclencherez une construction de votre site à l'avenir, votre pied de page affichera toujours l'année correcte.

Les shortcodes peuvent faire bien plus que cela. Ensuite, nous allons utiliser le plugin Eleventy Image, qui utilise des shortcodes, pour optimiser les images de notre site et améliorer la vitesse de chargement de nos pages.

### Comment utiliser le plugin Eleventy Image

Eleventy dispose de plusieurs plugins officiels, allant de ceux qui vérifient votre écriture pour un langage inclusif à d'autres qui vous permettent de tirer parti des fonctions Serverless.

Le plugin Image est particulièrement utile puisque les images sont souvent la ressource la plus volumineuse que votre site charge. Il optimise vos images afin que votre site utilise la taille et le format appropriés pour le navigateur de l'utilisateur, économisant de la bande passante pour votre utilisateur et rendant votre site plus rapide à charger.

Tout d'abord, nous devons installer le plugin Image depuis npm. À la racine de votre projet, exécutez :

```python
npm install @11ty/eleventy-img
```

En haut de `.eleventy.js`, nous allons importer le plugin Image et configurer le shortcode que le plugin utilisera pour optimiser nos images.

```javascript
const Image = require("@11ty/eleventy-img");

async function imageShortcode(src, alt, sizes) {
  let metadata = await Image(`./src${src}`, {
    widths: [300, 800, null],
    formats: ["avif", "jpeg"],
    urlPath: "/images/",
    outputDir: "./public/images/"
  });

  let imageAttributes = {
    alt,
    sizes,
    loading: "lazy",
    decoding: "async"
  };

  return Image.generateHTML(metadata, imageAttributes);
}
```

Le shortcode d'image prend en arguments `src`, `alt` et `sizes`. Ce seront l'URL de l'image, le texte pour la balise alt de l'image, et les tailles utilisées pour afficher différentes tailles d'images à différentes tailles d'écran.

La propriété `widths` spécifie la taille des images que le plugin générera. Dans ce cas, 300px, 800px, et la taille originale de l'image.

La propriété `formats` spécifie les formats d'image à générer. Ici, nous utilisons avif (qui produit des images de haute qualité à faible taille de fichier) avec jpeg comme solution de repli pour les navigateurs qui ne supportent pas avif.

`urlPath` et `outputDir` indiquent au plugin où obtenir les images et où sortir les images optimisées.

Le plugin ajoute les attributs `loading` et `decoding` au HTML généré pour charger les images de manière paresseuse et les décoder de manière asynchrone, ce qui aidera à améliorer les temps de chargement des pages.

Ensuite, nous allons inclure le shortcode dans notre fonction de configuration. Nous l'appellerons `EleventyImage` pour plus de clarté.

```javascript
eleventyConfig.addNunjucksAsyncShortcode("EleventyImage", imageShortcode);
```

Remarquez que nous utilisons `addNunjucksAsyncShortcode` plutôt que `addShortcode`. Cela est dû au fait que le processus de génération d'images est asynchrone. Il faudra un certain temps pour générer différentes tailles et formats d'images et nous voulons que notre shortcode attende que toutes ces images soient générées avant d'injecter le HTML final dans nos templates.

Puisque notre shortcode est asynchrone, nous allons rencontrer un problème lors de l'utilisation de ce shortcode à l'intérieur d'une boucle for de Nunjucks. Nous devons utiliser `asyncEach`, la version asynchrone de `for` de Nunjucks.

Dans `projects.njk` et `project-grid.njk`, remplacez ceci :

```python
{% for project in collections.projects %}
{% include "project-card.njk" %}
{% endfor %}
```

par ceci :

```python
{% asyncEach project in collections.projects %}
{% include "project-card.njk" %}
{% endeach %}
```

Maintenant, dans `project.njk`, nous pouvons remplacer ceci :

```python
<img class="project__image" src="{{ image }}" alt="{{ imageAlt }}">
```

par ceci :

```python
{% EleventyImage image, imageAlt, "(min-width: 30em) 50vw, 100vw" %}
```

Les valeurs `image`, `imageAlt` et `"(min-width: 30em) 50vw, 100vw"` sont les paramètres `src`, `alt` et `sizes` pour le shortcode Image.

Ensuite, dans `project-card.njk`, nous pouvons remplacer ceci :

```python
<img class="project-card__image" src="{{ project.data.image }}" alt="{{ project.data.imageAlt }}">
```

par ceci :

```python
{% EleventyImage project.data.image, project.data.imageAlt, "(min-width: 30em) 50vw, 100vw" %}
```

Enfin, dans `profile.njk`, nous pouvons remplacer ceci :

```python
<img class="profile__image" src="/images/profile.jpg" alt="Marie Jackson, Développeuse Logiciel">
```

par ceci :

```python
{% EleventyImage "/images/profile.jpg", "Marie Jackson, Développeuse Logiciel", "(min-width: 16em) 50vw, 100vw" %}
```

Lorsque notre site est construit, le plugin Eleventy Image fera quelques choses :

* il y aura plusieurs formats et tailles pour chaque image dans `public/images`
   
* notre HTML généré utilisera maintenant l'élément `<picture>`
   
* les balises `<img>` auront les attributs `loading="lazy"` et `decode="async"`
   

Maintenant, notre site servira le format et la taille d'image optimaux en fonction du navigateur et de la taille de l'écran du visiteur du site. Et les images seront chargées de manière paresseuse lorsqu'elles sont sur le point d'entrer dans la zone de visualisation.

Si nous utilisons l'onglet réseau dans les outils de développement d'un navigateur, nous pouvons tester la différence. Sur un iPhone 12, l'image non optimisée sur l'une de nos pages de projet serait de 30,37 Ko, tandis que l'image optimisée par le plugin Image n'est que de 6,01 Ko, une économie de 80 % !

![Image non optimisée sur mobile - 30,37 Ko.](https://www.freecodecamp.org/news/content/images/2022/08/unoptimized.PNG align="left")

*Image non optimisée sur mobile - 30,37 Ko*

![Image optimisée sur mobile 6,01 Ko.](https://www.freecodecamp.org/news/content/images/2022/08/optimized.PNG align="left")

*Image optimisée sur mobile 6,01 Ko*

Nous sommes presque prêts à déployer notre site. Mais avant de le faire, nous devons compléter notre formulaire de contact.

## Comment construire un formulaire de contact avec Netlify Forms

![Page de contact](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-18-17-08-Eleventy-Portfolio-1.png align="left")

*Page de contact*

Eleventy est un générateur de site **statique**. Mais Eleventy fonctionne très bien avec l'architecture Jamstack, où vous générez statiquement autant de site que possible à l'avance et utilisez des APIs et des services tiers pour ajouter du contenu dynamique et des fonctionnalités.

Dans le passé, si vous vouliez avoir un formulaire de contact sur votre site web, vous auriez besoin d'une sorte de serveur, comme une application PHP, pour traiter la soumission du formulaire.

Nous allons utiliser Netlify Forms pour ajouter un formulaire de contact à notre portfolio sans avoir besoin de gérer un serveur pour traiter les formulaires soumis.

Pour que cela fonctionne, nous devons nous assurer que notre formulaire a deux attributs. Le plus important est `data-netlify="true"`. L'autre est `action="/success"`.

```python
<form class="form" name="contact" action="/success" method="POST" data-netlify="true">
  <div class="form__section">
    <label class="form__label" for="yourName">Nom</label>
    <input class="form__input" name="name" type="text" id="yourName" required="true">
  </div>
  <div class="form__section">
    <label class="form__label" for="yourEmail">Email</label>
    <input class="form__input" name="email" type="email"  id="yourEmail" required="true">
  </div>
  <div class="form__section">
    <label class="form__label" for="message">Message</label>
    <textarea class="form__input" name="message" id="message" rows="4" required="true"></textarea>
  </div>
    <button class="form__button" type="submit">Parlons</button>
</form>
```

En ayant un attribut `data-netlify="true"` sur notre formulaire de contact, lorsque le site est déployé sur Netlify, Netlify le reconnaîtra et prendra en charge la soumission du formulaire.

Par défaut, lorsqu'une personne remplit un formulaire Netlify, elle reçoit un message de succès générique avec un lien vers la page du formulaire. Mais nous pouvons les diriger vers une page personnalisée en incluant un attribut `action` sur notre formulaire.

L'attribut `action="/success"` signifie que lorsque le formulaire est soumis, l'utilisateur sera redirigé vers une page "success" sur votre site (vous pouvez donner un autre nom à cette page si vous le souhaitez). Donc, nous ferions mieux de construire cette page maintenant.

Dans le répertoire `src`, créez un fichier `success.njk` avec le contenu suivant :

```python
---
title: "Eleventy Portfolio"
layout: "base.njk"
---

<div class="container text-center">
  <h2 class="heading--main">Merci d'avoir pris contact !</h2>
  <p>Je répondrai dès que possible.<p>
</div>
```

Une fois que nous déployons le site sur Netlify, tous les formulaires soumis apparaîtront dans l'interface Netlify. Alors, déployons enfin notre site de portfolio.

## Comment déployer sur Netlify

Vous pouvez déployer un site Eleventy sur n'importe quelle plateforme d'hébergement statique : Netlify, Vercel, GitHub Pages, même un bucket AWS S3.

Je vais vous montrer comment déployer sur Netlify puisque nous utilisons Netlify Forms pour notre formulaire de contact. Sur une autre plateforme d'hébergement, vous pourriez utiliser une fonction Serverless pour gérer la soumission du formulaire et envoyer un email.

Si vous n'avez pas déjà un compte Netlify, allez sur [netlify.com](https://www.netlify.com/) et créez-en un gratuitement.

Netlify vous donnera l'option de :

1. Importer un projet existant
   
2. Commencer à partir d'un template
   
3. Déployer manuellement
   

Nous avons déjà notre site de portfolio, donc nous n'avons pas besoin d'un template.

Je vais vous guider à travers les deux autres options.

![Écran de démarrage du projet Netlify.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-21-25-15-Deploy-your-first-project-Netlify.png align="left")

*Écran de démarrage du projet Netlify*

### Option 1 – Comment déployer manuellement

Si vous n'êtes pas à l'aise avec Git et GitHub, Netlify vous permet de glisser-déposer pour télécharger un projet dans leur interface.

Sur votre ligne de commande, exécutez `npm run build` ou `eleventy` pour construire votre site.

Maintenant, téléchargez le répertoire `public` du site dans l'interface de téléchargement de fichiers de Netlify. En quelques instants, Netlify aura le site en ligne sur une URL que vous pourrez visiter.

Si vous souhaitez apporter des modifications futures à votre site déployé, cliquez sur "Deploys" et faites défiler vers le bas pour trouver le téléchargeur de fichiers.

Vous pouvez reconstruire votre site localement et télécharger la nouvelle version de votre dossier `public` sur Netlify chaque fois que vous le souhaitez.

### Option 2 – Comment importer un projet depuis Git

Si vous êtes familier avec Git et GitHub, commitez votre code et poussez-le sur GitHub. Ensuite, cliquez sur le bouton "Import from Git".

Netlify vous demandera de connecter un fournisseur Git. Choisissez GitHub et autorisez Netlify à accéder à vos dépôts GitHub.

Choisissez le dépôt qui contient votre site de portfolio. Vous pouvez rechercher "eleventy", ou le nom que vous lui avez donné.

![Interface d'importation de projet Netlify.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-21-44-56-Import-an-existing-project-from-a-Git-repository-Netlify.png align="left")

*Interface d'importation de projet Netlify*

Netlify détectera qu'il s'agit d'un projet Eleventy et vous demandera de confirmer les paramètres de construction de base.

Assurez-vous que la commande de construction est soit `npm run build` soit `eleventy`.

Sous "Publish directory", entrez `public` au lieu de `_site`.

Maintenant, cliquez sur le bouton "Deploy site".

![Page des paramètres de construction de Netlify.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-21-46-55-Import-an-existing-project-from-a-Git-repository-Netlify.png align="left")

*Page des paramètres de construction de Netlify*

En quelques instants, Netlify vous informera que votre site est en ligne et vous donnera une URL pour celui-ci.

Une fois votre site en ligne, si vous allez sur la page Contact, remplissez le formulaire et soumettez-le. Vous serez redirigé vers la page de succès personnalisée que vous avez créée.

Si vous cliquez sur "Forms" dans l'interface Netlify, vous serez dirigé vers le tableau de bord Netlify Forms.

Le formulaire portera le nom que vous avez utilisé dans l'attribut `name` de votre formulaire de contact, dans ce cas "contact".

![Tableau de bord des formulaires Netlify.](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-30-at-21-55-09-Forms-remarkable-blini-2319ee.png align="left")

*Tableau de bord des formulaires Netlify*

Félicitations, vous avez construit et déployé un site de portfolio Eleventy. 🎉🎉🎉

N'hésitez pas à utiliser ce projet comme modèle pour votre propre portfolio et à le personnaliser comme vous le souhaitez. Tant de portfolios se ressemblent, il est donc toujours bon qu'un portfolio montre votre personnalité et vos passions.

## Où aller à partir de là

Ce tutoriel vous a, espérons-le, appris les bases d'Eleventy, et comment combiner des données et des templates pour créer des sites rapides sans beaucoup d'outils ou de configuration.

Si vous souhaitez aller plus loin dans votre voyage avec Eleventy, la [documentation d'Eleventy](https://www.11ty.dev/docs/) est très bonne. Il y a beaucoup plus à apprendre sur la manipulation des données, sans parler de l'ajout de contenu personnalisé et d'interactivité dynamique avec les fonctions Serverless et Edge.

[11ty.rocks](https://11ty.rocks/) par Stephanie Eckles est également une excellente ressource, avec des conseils pratiques et des tutoriels utiles sur toutes sortes de fonctionnalités d'Eleventy.

J'espère que ce guide a été utile et vous a donné envie d'en apprendre davantage sur Eleventy, les générateurs de sites statiques et le Jamstack.