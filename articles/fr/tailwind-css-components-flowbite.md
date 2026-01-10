---
title: Tutoriel sur les composants Tailwind CSS – Comment commencer avec Flowbite
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-27T00:53:05.000Z'
originalURL: https://freecodecamp.org/news/tailwind-css-components-flowbite
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/flowbite.png
tags:
- name: CSS
  slug: css
- name: tailwind
  slug: tailwind
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Tutoriel sur les composants Tailwind CSS – Comment commencer avec Flowbite
seo_desc: 'By Zoltán Szőgyényi

  Flowbite is an open-source library of web components built with the utility-first
  classes from Tailwind CSS. It also includes interactive elements such as dropdowns,
  modals, datepickers.

  Tailwind CSS is a framework that I''ve been ...'
---

Par Zoltán Szőgyényi

Flowbite est une bibliothèque open-source de composants web construits avec les classes utilitaires de Tailwind CSS. Elle inclut également des éléments interactifs tels que des menus déroulants, des modales, des sélecteurs de date.

Tailwind CSS est un framework que j'ai beaucoup utilisé récemment dans mes projets liés au web en raison de la rapidité avec laquelle il est possible de construire des pages en utilisant les classes utilitaires.

Un problème que j'ai rencontré, cependant, est que _le framework ne comprend pas un ensemble de base de composants_ pour commencer. J'ai donc dû les reconstruire encore et encore pour chaque projet.

Mais ensuite, j'ai trouvé une [bibliothèque de composants basée sur Tailwind CSS appelée Flowbite](https://flowbite.com/docs/getting-started/introduction/). Elle comprend les composants web les plus couramment utilisés, tels que des boutons, des barres de navigation, des cartes, des éléments de formulaire, et plus encore, qui sont commodément construits avec les _classes utilitaires de Tailwind CSS_.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-26-at-13.54.41.png)
_Flowbite - Bibliothèque de composants Tailwind CSS_

Aujourd'hui, je veux vous montrer comment vous pouvez commencer avec cette bibliothèque et commencer à construire des sites web encore plus rapidement avec Tailwind CSS et les composants de Flowbite.

Le projet est [disponible sur Github](https://github.com/themesberg/flowbite) et il est open source sous la licence MIT.

## Commencer avec Flowbite

Tout d'abord, vous devez comprendre comment fonctionne Flowbite. Cette bibliothèque n'est pas un autre framework. Il s'agit plutôt d'un ensemble de composants basés sur Tailwind CSS que vous pouvez simplement copier-coller à partir de la documentation.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-26-at-11.08.55.png)
_Flowbite - Composants de formulaire Tailwind CSS_

Elle inclut également un fichier JavaScript qui active les composants interactifs, tels que les modales, les menus déroulants et les sélecteurs de date, que vous pouvez optionnellement inclure dans votre projet via CDN ou NPM.

Vous pouvez consulter le [guide de démarrage rapide](https://flowbite.com/docs/getting-started/quickstart/) pour explorer les éléments en incluant les fichiers CDN dans votre projet. Mais si vous souhaitez construire un projet avec Flowbite, je vous recommande de suivre les étapes des [outils de construction](https://flowbite.com/docs/getting-started/build-tools/) afin de pouvoir purger et minifier le CSS généré.

Pour une configuration plus rapide, nous inclurons tout en utilisant un CDN.

## Comment inclure Flowbite et Tailwind CSS via CDN

Commençons par inclure le fichier CSS à l'intérieur de la balise `head` de votre HTML :

```html
<link rel="stylesheet" href="https://unpkg.com/flowbite@latest/dist/flowbite.min.css" />
```

Ensuite, incluez également le fichier JavaScript qui active les éléments interactifs avant la fermeture de la balise `body` :

```html
<script src="https://unpkg.com/flowbite@latest/dist/flowbite.bundle.js"></script>
```

Si vous avez suivi ces deux étapes correctement, vous devriez maintenant avoir à la fois Tailwind CSS et Flowbite inclus dans votre projet et les composants de Flowbite devraient tous fonctionner maintenant.

## Explorer les composants de Flowbite

L'étape suivante consiste à consulter les composants de la documentation, qui sont tous construits en utilisant les classes utilitaires de Tailwind CSS.

Vous pouvez trouver tout, des alertes, boutons et badges, jusqu'aux barres de navigation, modales, menus déroulants et même des sélecteurs de date.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-26-at-11.34.53.png)
_Composants Flowbite - Tailwind CSS_

Voici la liste complète des composants :

* Alertes
* Badges
* Fil d'Ariane
* Boutons
* Groupe de boutons
* Cartes
* Menus déroulants
* Formulaires
* Groupe de listes
* Typographie
* Modale
* Barre de navigation
* Pagination
* Barre de progression
* Tableaux
* Info-bulles
* Sélecteur de date

Vous pouvez consulter [tous les composants](https://flowbite.com/#components) sur la page d'accueil et ils seront accessibles depuis chaque page de la documentation.

Tout ce que vous avez à faire maintenant est de copier-coller l'élément de votre choix dans votre projet et de l'utiliser comme bon vous semble.

Créons une page d'authentification utilisateur en utilisant les composants de Flowbite et les classes utilitaires de Tailwind CSS pour vous montrer le flux de travail de cette bibliothèque.

Voici à quoi elle ressemblera à la fin :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-26-at-11.38.56.png)
_Page d'authentification construite avec Flowbite_

## Comment construire une page d'authentification utilisateur avec Flowbite

La première exigence est d'inclure Flowbite dans la page HTML avec laquelle vous allez travailler, soit via CDN ou NPM. Je vous ai déjà montré comment faire cela dans cet article, donc je suppose que vous l'avez déjà fait.

Commençons par construire l'élément wrapper auquel nous ajouterons plus tard le logo et l'élément de carte principal.

```html
<div class="mx-auto md:h-screen flex flex-col justify-center items-center px-6 pt-8 pt:mt-0">
    <!-- le contenu ira ici -->
</div>
```

Cet élément garantit que tout sera centré horizontalement et verticalement sur les grands écrans.

Ajoutons maintenant le logo, ce qui est bon pour le branding et que les utilisateurs peuvent également cliquer pour revenir à la page d'accueil.

```html
<div class="mx-auto md:h-screen flex flex-col justify-center items-center px-6 pt-8 pt:mt-0">
    <a href="#" class="text-2xl font-semibold flex justify-center items-center mb-8 lg:mb-10">
      <img src="https://flowbite.com/application-ui/demo/images/logo.svg" class="h-11 mr-4" alt="Logo FlowBite">
      <span>Flowbite</span>
    </a>
</div>
```

Ensuite, nous devons créer l'élément de carte principal qui vient juste après le logo que nous avons ajouté et également ajouter l'image à l'intérieur de la carte.

```html
<div class="bg-white shadow rounded-lg lg:flex items-center justify-center md:mt-0 w-full lg:max-w-screen-lg 2xl:max:max-w-screen-lg xl:p-0">
	<div class="hidden lg:flex w-2/3">
		<img class="rounded-l-lg" src="https://flowbite.com/application-ui/demo/images/authentication/login.jpg" alt="image de connexion">
	</div>
	<div class="w-full p-6 sm:p-8 lg:p-16 lg:py-0 space-y-8">
		<!-- Le formulaire d'authentification va ici -->
	</div>
</div>
```

Si vous avez suivi les étapes correctement, vous devriez avoir une carte d'authentification vide avec une image à l'intérieur et le logo au-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-26-at-11.54.14.png)
_Carte d'authentification vide_

### Comment utiliser l'élément de formulaire Flowbite Tailwind CSS

C'est là que Flowbite entre en jeu, car nous devons construire un élément de formulaire qui inclut deux champs de saisie de texte, une case à cocher et un bouton. Nous n'avons pas à le construire nous-mêmes car nous pouvons utiliser les [éléments de formulaire Tailwind CSS](https://flowbite.com/docs/components/forms/) de Flowbite.

Ajoutons le titre suivant et l'élément de formulaire à l'intérieur du deuxième élément `div` de la carte.

```html
<h2 class="text-2xl lg:text-3xl font-bold text-gray-900">
   Connectez-vous à la plateforme
</h2>
<form class="mt-8 space-y-6" action="#">
   <div>
      <label for="email" class="text-sm font-medium text-gray-900 block mb-2">Votre email</label>
      <input type="email" name="email" id="email"
         class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
         placeholder="nom@entreprise.com" required>
   </div>
   <div>
      <label for="password" class="text-sm font-medium text-gray-900 block mb-2">Votre mot de passe</label>
      <input type="password" name="password" id="password" placeholder=""
         class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
         required>
   </div>
   <div class="flex items-start">
      <div class="flex items-center h-5">
         <input id="remember" aria-describedby="remember" name="remember" type="checkbox"
            class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded" required>
      </div>
      <div class="text-sm ml-3">
         <label for="remember" class="font-medium text-gray-900">Se souvenir de moi</label>
      </div>
      <a href="#" class="text-sm text-blue-700 hover:underline ml-auto">Mot de passe perdu ?</a>
   </div>
   <button type="submit"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-base px-5 py-3 w-full sm:w-auto text-center">Se connecter
   à votre compte</button>
   <div class="text-sm font-medium text-gray-500">
      Pas encore inscrit ? <a class="text-blue-700 hover:underline">Créer un compte</a>
   </div>
</form>
```

Le résultat final devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-26-at-11.38.56-1.png)
_Page d'authentification construite avec Flowbite et Tailwind CSS_

Félicitations ! Vous avez construit votre première page en utilisant à la fois Tailwind CSS et Flowbite. Imaginez combien cela vous aidera dans vos projets de ne pas avoir à reconstruire tous les composants web couramment utilisés encore et encore.

## Conclusion

J'espère que ce tutoriel vous a aidé à comprendre ce qu'est Flowbite et comment vous pouvez l'utiliser pour alimenter et accélérer votre flux de développement Tailwind CSS encore plus.

Il y a une vidéo sur [l'essai de Flowbite sur YouTube](https://www.youtube.com/watch?v=4bnJG2UDr9A) que vous pouvez consulter si vous voulez voir un développeur expérimenté travailler avec la bibliothèque.

Il existe également une [version pro de Flowbite](https://flowbite.com/pro/) pour ceux qui veulent améliorer encore plus leur boîte à outils Tailwind CSS, car elle inclut un [kit de design Figma pour Tailwind CSS](https://flowbite.com/figma/) que vous pouvez utiliser pour prototyper le design de votre site web avant de le coder.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-26-at-12.10.03.png)
_Aperçu de Flowbite Pro_

Vous recevrez également beaucoup d'UI d'application utiles, d'UI marketing et de pages e-commerce qui peuvent vous aider à démarrer vos projets encore plus rapidement. Vous pouvez consulter ce [tableau comparatif](https://flowbite.com/pro/#pricing) pour mieux comprendre les différences entre les versions open-source et pro de Flowbite.