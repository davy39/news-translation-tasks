---
title: 8 idées de projets React.js pour commencer à apprendre en pratiquant
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-08-12T17:31:37.000Z'
originalURL: https://freecodecamp.org/news/8-reactjs-project-ideas-to-start-learning-by-doing
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/50-react-projects.jpg
tags:
- name: projects
  slug: projects
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: 8 idées de projets React.js pour commencer à apprendre en pratiquant
seo_desc: "One of the best ways to learn is by doing. But often developers struggle\
  \ with the big question \"what should I build?\" \nHere are 8 project ideas, complete\
  \ with project briefs and layout ideas, to get you started learning by doing.\n\n\
  Business & Real-Wor..."
---

L'une des meilleures façons d'apprendre est de pratiquer. Mais souvent, les développeurs se demandent "que devrais-je construire ?".

Voici 8 idées de projets, complètes avec des briefs et des idées de mise en page, pour commencer à apprendre en pratiquant.

* [Entreprise & Monde Réel : Tableau de Bord Statistique Cartographique](#heading-tableau-de-bord-statistique-cartographique)
* [Amusant & Intéressant : Instrument de Musique](#heading-instrument-de-musique)
* [Personnel & Portfolio : Blog](#heading-blog)
* [Productivité : Carnet de Notes](#heading-carnet-de-notes)
* [Puzzles & Jeux : Space Invaders](#heading-space-invaders)
* [Outils & Bibliothèques : Thème de Framework](#heading-theme-de-framework)
* [Extensions de Projet : Webmentions](#heading-webmentions)
* [Clones : Product Hunt](#heading-product-hunt)

_Ceci est un aperçu de l'ebook gratuit [50 Projets pour React & le Web Statique](https://50reactprojects.com/). Vous pouvez trouver les 50 idées de projets, y compris ces 8, sur [50reactprojects.com](https://50reactprojects.com/)._

## Tableau de Bord Statistique Cartographique

**Catégorie : Entreprise & Monde Réel**

Créez un tableau de bord cartographique qui montre les statistiques et les informations géographiques sur le COVID-19.

### Brief

Faire face à une pandémie mondiale signifie que des virus comme le Coronavirus impactent le monde différemment selon la localisation géographique. 

Avoir une carte avec une répartition des statistiques de chaque pays est un moyen utile de déterminer des choses comme quels pays ont été les plus impactés.

### Niveau 1

Le moyen le plus simple de voir les statistiques pays par pays est d'avoir une carte que vous pouvez parcourir avec les statistiques de chaque pays disponibles à côté de ce pays.  
  
Créez une application de cartographie qui utilise l'API Coronavirus de disease.sh pour ajouter des marqueurs à la carte pour chaque pays ainsi que le nombre de cas de COVID-19.

### Niveau 2

Bien que les statistiques pour chaque pays soient utiles, il pourrait être utile de pouvoir comparer ces statistiques au nombre de cas dans le monde entier.  
  
Ajoutez un tableau de bord statistique qui montre le nombre de cas de COVID-19 dans le monde ainsi que toute autre statistique utile de l'API.

### Niveau 3

Obtenir des statistiques actuelles est un bon moyen de comprendre l'état actuel du monde, mais comment cela se compare-t-il historiquement ?  
  
Utilisez l'API de données historiques pour afficher des graphiques sur le tableau de bord qui fournissent un contexte à la croissance et à la propagation du virus.

### À Faire

* Créer une nouvelle application de cartographie
* Récupérer les données des pays de l'API
* Ajouter des marqueurs à la carte
* Ajouter des statistiques aux marqueurs
* Récupérer les données mondiales de l'API
* Créer un tableau de bord statistique
* Ajouter des statistiques mondiales
* Récupérer les données historiques de l'API
* Ajouter des graphiques à la carte

### Boîte à Outils

* [Open Disease Data API](https://disease.sh/) (disease.sh)
* [React Leaflet](https://react-leaflet.js.org/) (react-leaflet.js.org)
* [Gatsby Leaflet Starter](https://github.com/colbyfayock/gatsby-starter-leaflet) (github.com)

### Tutoriels

* [Comment créer un tableau de bord et une application cartographique Coronavirus (COVID-19) dans React avec Gatsby et Leaflet](https://www.freecodecamp.org/news/how-to-create-a-coronavirus-covid-19-dashboard-map-app-in-react-with-gatsby-and-leaflet/) (freecodecamp.org)
* [Comment ajouter des statistiques de cas de Coronavirus (COVID-19) à votre tableau de bord cartographique React avec Gatsby](https://www.freecodecamp.org/news/how-to-add-coronavirus-covid-19-case-statistics-to-your-map-dashboard-in-gatsby-and-react-leaflet/) (freecodecamp.org)
* [Cartographie avec React Leaflet](https://egghead.io/playlists/mapping-with-react-leaflet-e0e0?af=atzgap) (egghead.io)

### Inspiration

* [Tableau de bord COVID-19 par le Centre pour la Science et l'Ingénierie des Systèmes (CSSE) de l'Université Johns Hopkins (JHU)](https://coronavirus.jhu.edu/map.html) (coronavirus.jhu.edu)
* [Démonstration du Tableau de Bord Coronavirus (COVID-19)](https://coronavirus-map-dashboard.netlify.app/) (coronavirus-map-dashboard.netlify.app)

### Idée de Mise en Page  


![Image](https://www.freecodecamp.org/news/content/images/2020/08/Coronavirus---Layout.jpg)
_Idée de mise en page du Tableau de Bord Statistique Cartographique_

## Instrument de Musique

**Catégorie : Amusant & Intéressant**

Créez un piano interactif que vous pouvez utiliser pour jouer de la musique avec votre clavier.

### Brief

Tout le monde n'a pas le luxe de posséder un instrument de musique, mais peut-être que ces personnes ont un ordinateur portable, un téléphone ou une tablette. Avoir un piano est un moyen puissant de laisser les gens jouer de la musique même s'ils n'en ont pas eu l'opportunité auparavant.

### Niveau 1

En utilisant le navigateur et les API audio web, nous pouvons créer des sons qui, lorsqu'ils sont assemblés, peuvent réellement ressembler à de la musique.  
  
Créez un ensemble de boutons qui jouent les notes d'une gamme lorsqu'ils sont cliqués.

### Niveau 2

Bien que tout le monde n'ait pas joué d'un instrument auparavant, le concept et l'interface d'un instrument comme un piano sont généralement plus intuitifs qu'un ensemble de boutons.  
  
Créez une disposition de piano en utilisant des boutons qui fonctionnent soit en cliquant sur le bouton, soit en utilisant le clavier physique.

### Niveau 3

Nous pouvons avoir un espace limité dans le navigateur, mais il existe une large gamme de notes, de gammes et de sons qu'un clavier électrique pourrait être capable de produire avec quelques effets ajoutés.  
  
Créez des bascules d'effet qui changent le son des notes lorsqu'elles sont activées.

### À Faire

* Créer des boutons
* Jouer un son lorsqu'ils sont cliqués
* Disposer les notes dans une gamme
* Créer une disposition de piano
* Définir les événements de clavier
* Créer une disposition d'effets
* Basculer les effets audio

### Boîte à Outils

* [React HotKeys](https://github.com/greena13/react-hotkeys) (github.com)

### Tutoriels

* [Construire un Piano avec les Hooks React](https://dev.to/ganeshmani/building-a-piano-with-react-hooks-3mih) (dev.to)
* [Comment Construire un Clavier de Piano en Utilisant JavaScript Vanilla](https://www.freecodecamp.org/news/javascript-piano-keyboard/) (freecodecamp.org)
* [Construire un piano avec tone.js!](https://dev.to/shimphillip/building-a-piano-with-tone-js-5c2f) (dev.to)
* [Comment J'ai Fabriqué un Piano en seulement 1kb de JavaScript](https://frankforce.com/?p=7617#pianostory) (frankforce.com)

### Inspiration

* [React Guitar](https://react-guitar.com/) (react-guitar.com)

### Idée de Mise en Page

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Musical-Instrument---Layout.jpg)
_Idée de mise en page de l'Instrument de Musique_

## Blog

**Catégorie : Personnel & Portfolio**

Créez un blog que vous pouvez utiliser pour partager vos expériences professionnelles et vos projets.

### Brief

Dans toute carrière, avoir un blog pour partager vos expériences est un bon moyen de faire savoir aux gens sur quoi vous travaillez et d'aider les autres à apprendre de vos expériences. 

C'est aussi un moyen de renforcer ce que vous avez appris afin de pouvoir vous y référer à l'avenir.

### Niveau 1

Pour pouvoir partager vos expériences, vous avez besoin d'une structure de site web qui vous permettra de créer du nouveau contenu et de gérer le contenu existant. 

Une façon de faire cela est de créer des fichiers markdown que votre site web utilise pour créer de nouvelles pages et afficher les publications.  
  
Créez un blog en utilisant des fichiers markdown comme source de contenu.

### Niveau 2

Avoir votre contenu dans des fichiers markdown est un bon moyen de gérer du contenu statique, mais vous ne voulez peut-être pas avoir à éditer du code chaque fois que vous écrivez ou éditez une publication.  
  
Intégrez un système de gestion de contenu qui vous permet d'ajouter du nouveau contenu ou d'éditer l'existant avec une interface utilisateur agréable.

### Niveau 3

Si vous partagez du code sur votre blog, HTML prend nativement en charge les balises code et pre qui vous aident à formater le code de manière lisible. Mais cela n'inclut pas la coloration syntaxique qui aide à améliorer la lisibilité.  
  
Intégrez un surligneur de syntaxe qui rend les blocs de code plus lisibles.

### À Faire

* Créer un blog
* Ajouter le premier contenu statique
* Source de contenu statique
* Intégrer un CMS
* Ajouter du code au contenu
* Ajouter la coloration syntaxique

### Boîte à Outils

* [Netlify CMS](https://www.netlifycms.org/) (netlifycms.org)
* [Prism.js](https://prismjs.com/) (prismjs.com)

### Tutoriels

* [Créer un Blog Gatsby avec Netlify CMS](https://www.gatsbyjs.org/tutorial/blog-netlify-cms-tutorial/) (gatsbyjs.org)
* [Comment Construire Votre Blog de Codage à partir de Zéro en Utilisant Gatsby et MDX](https://www.freecodecamp.org/news/build-a-developer-blog-from-scratch-with-gatsby-and-mdx/) (freecodecamp.org)

### Inspiration

* [Gatsby Netlify CMS Starter](https://gatsby-netlify-cms.netlify.app/) (gatsby-netlify-cms.netlify.app)

### Idée de Mise en Page

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Blog---Layout.jpg)
_Idée de mise en page du Blog_

## Carnet de Notes

**Catégorie : Productivité**

Créez une application de carnet de notes pour ajouter, gérer et organiser un groupe de notes.

### Brief

Prendre des notes est un excellent moyen de s'assurer que nous gardons une trace de nos pensées ou de nous souvenir des points importants d'une réunion. Pouvoir les gérer et les organiser facilement est important pour les retrouver plus tard !

### Niveau 1

La première exigence d'un carnet de notes est de pouvoir prendre des notes. Cela peut être assez simple au début, où vous avez vraiment besoin d'une sorte d'entrée qui collecte ce que vous écrivez et le stocke quelque part pour plus tard.  
  
Créez un formulaire pour ajouter de nouvelles notes et les afficher dans une liste.

### Niveau 2

Pour retrouver vos notes plus tard, vous voulez un moyen d'organiser ces notes et un moyen de les rechercher. Cela inclut l'ajout de catégories ou d'un système de balises ainsi qu'une interface utilisateur pour effectuer des recherches.  
  
Ajoutez la possibilité de baliser ou de catégoriser les notes et une entrée pour les rechercher.

### Niveau 3

Que nous en soyons conscients ou non, nous pouvons trouver des connexions entre nos pensées et, plus important encore, nos notes, où nous pouvons tirer parti de ce réseau de pensées pour notre carnet de notes.  
  
Ajoutez un lien de notes inspiré de Roam Research pour créer un réseau de pensées.

### À Faire

* Créer un formulaire
* Stocker de nouvelles notes
* Lister les notes
* Ajouter des balises ou des catégories
* Ajouter une recherche de notes
* Ajouter un réseau de notes

### Boîte à Outils

* [Gatsby Brain Theme](https://github.com/aengusmcmillin/gatsby-theme-brain) (github.com)
* [Fuse.js](https://fusejs.io/) (fusejs.io)

### Tutoriels

* [Comment Ajouter une Recherche à une Application React avec Fuse.js](https://www.freecodecamp.org/news/how-to-add-search-to-a-react-app-with-fuse-js/) (freecodecamp.org)

### Inspiration

* [Foam](https://foambubble.github.io/foam/) (foambubble.github.io)
* [Roam Research](https://roamresearch.com/) (roamresearch.com)
* [Gatsby Garden Theme](https://github.com/mathieudutour/gatsby-digital-garden) (github.com)

### Idée de Mise en Page

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Notebook---Layout.jpg)
_Idée de mise en page du Carnet de Notes_

## Space Invaders

**Catégorie : Puzzles & Jeux**

Créez un jeu de tir spatial Space Invaders pour tirer sur plusieurs vagues de vaisseaux ennemis.

### Brief

Space Invaders est un classique des salles d'arcade qui vous met aux commandes d'un vaisseau spatial face à une invasion extraterrestre. Alors que vous essayez de les abattre, ils tirent en retour, et vous n'avez qu'une quantité limitée de protection avant d'être vulnérable aux impacts.

### Niveau 1

La partie centrale du jeu est que vous déplacez un vaisseau spatial en essayant de toucher un groupe d'extraterrestres avec vos armes. Bien qu'il n'y ait qu'un seul vous, il y en a beaucoup d'eux.  
  
Créez un vaisseau spatial qui peut se déplacer et tirer sur des extraterrestres qui ne bougent pas.

### Niveau 2

Ce qui rend le jeu difficile, c'est que les extraterrestres bougent constamment. Chaque fois qu'ils atteignent le bord de la zone de jeu, ils descendent et accélèrent, se rapprochant de votre vaisseau.  
  
Ajoutez un mouvement aux extraterrestres allant de côté à côté sur la zone de jeu. Chaque fois que les extraterrestres atteignent un côté, ils doivent descendre d'un niveau. Ils doivent également accélérer à certains intervalles.

### Niveau 3

Vous êtes seul, mais heureusement, vous pouvez obtenir une certaine protection. Vous avez des boucliers derrière lesquels vous pouvez vous cacher et qui vous protègent tant qu'ils durent.  
  
Créez plusieurs boucliers devant le vaisseau spatial du joueur qui peuvent absorber une quantité limitée de dégâts.

### À Faire

* Créer un nouveau jeu
* Créer des extraterrestres statiques
* Créer un vaisseau spatial joueur
* Ajouter des contrôles de vaisseau spatial
* Ajouter une arme de vaisseau spatial
* Configurer les dégâts des extraterrestres
* Faire tirer les extraterrestres en retour
* Faire bouger les extraterrestres
* Ajouter des intervalles d'extraterrestres
* Ajouter des boucliers

### Tutoriels

* [Apprendre JavaScript en construisant 7 jeux](https://www.freecodecamp.org/news/learn-javascript-by-building-7-games-video-course/) (freecodecamp.org)

### Inspiration

* [Space Invaders](https://codepen.io/adelciotto/pen/BHuGL) (codepen.io)

### Idée de Mise en Page

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Space-Invaders---Layout.jpg)
_Idée de mise en page de Space Invaders_

## Thème de Framework

**Catégorie : Outils & Bibliothèques**

Créez un thème Gatsby qui configure un projet avec le framework Tailwind CSS.

### Brief

En tant que développeurs, nous devons souvent effectuer une série d'étapes similaires chaque fois que nous créons un nouveau projet. Mais des outils comme les thèmes nous permettent d'abstraire ces étapes et de les regrouper dans un moyen facile à utiliser qui peut fonctionner pour tout nouveau projet.

### Niveau 1

Les thèmes Gatsby sont un système similaire à des plugins où nous pouvons tirer parti du pipeline Gatsby pour partager des fonctionnalités sous forme de package sur npm. 

Cela ouvre la porte à tout ce que nous pourrions faire dans un site Gatsby, mais en le rendant réutilisable pour tout site Gatsby.  
  
Créez un nouveau thème Gatsby qui, lorsqu'il est utilisé, crée une nouvelle page de guide de style sur tout projet auquel il est ajouté.

### Niveau 2

Le but des thèmes n'est pas seulement de créer des pages, mais d'ajouter des fonctionnalités qui nous rendent productifs. Cela inclut des choses comme des frameworks et des configurations de projet.  
  
Ajoutez un framework CSS au thème Gatsby qui permet au projet auquel il est ajouté d'utiliser ce framework.

### Niveau 3

Parfois, les thèmes sont meilleurs en tant qu'outils, parfois il est utile d'être prescriptif. Une façon d'ajouter des fonctionnalités utiles à un framework CSS est de créer des composants standard.  
  
Créez des composants React réutilisables en utilisant le framework CSS qui peuvent être utilisés dans le projet auquel le thème est ajouté.

### À Faire

* Créer un nouveau thème
* Ajouter à un projet d'exemple
* Créer une nouvelle page de style
* Ajouter un framework CSS
* Utiliser le CSS dans l'exemple
* Créer des composants
* Utiliser des composants

### Boîte à Outils

* [Gatsby Themes](https://www.gatsbyjs.org/docs/themes/) (gatsbyjs.org)
* [Tailwind](https://tailwindcss.com/) (tailwindcss.com)

### Tutoriels

* [Construire un Thème](https://www.gatsbyjs.org/tutorial/building-a-theme/) (gatsbyjs.org)
* [Qu'est-ce que Tailwind CSS et comment puis-je l'ajouter à mon site web ou à mon application React ?](https://www.freecodecamp.org/news/what-is-tailwind-css-and-how-can-i-add-it-to-my-website-or-react-app/) (freecodecamp.org)

### Inspiration

* [Gatsby Tailwind Theme](https://github.com/talensjr/gatsby-theme-tailwindcss) (github.com)

### Idée de Mise en Page

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Framework-Theme---Layout.jpg)
_Idée de mise en page du Thème de Framework_

## Webmentions

**Catégorie : Extensions de Projet**

Ajoutez une intégration de webmentions à un site web qui montre les interactions Twitter avec le site web.

### Brief

L'interaction sociale est un moyen impactant d'apporter plus d'audience et de conversation aux sujets sur lesquels nous écrivons. 

Avoir quelque chose sur un site web qui montre cette interaction peut être utile à la fois pour inspirer les gens à vouloir s'impliquer ou pour faire sentir aux gens qu'ils peuvent en faire partie.

### Niveau 1

Pour utiliser les Webmentions, un site web doit être configuré avec des balises méta pour fournir des informations.  
  
Ajoutez les balises méta appropriées à un site web et validez son utilisation avec webmention.io.

### Niveau 2

L'API Webmentions est un moyen de voir programmatiquement les connexions dans les interactions sociales à partir d'une URL de votre site web. Elle vous permet d'obtenir le type d'interaction et même l'avatar du profil de la personne.  
  
Connectez un site web aux Webmentions et ajoutez une liste d'interactions sociales aux pages de publication de blog.

### Niveau 3

Maintenant que le site web montre toutes les interactions, il devrait y avoir un moyen facile de rejoindre la conversation.  
  
Ajoutez un lien social qui, lorsqu'il est cliqué, crée un tweet avec un lien vers la page.

### À Faire

* Ajouter des balises méta au site web
* Valider les balises méta
* Se connecter à Webmention
* Connecter le social à Bridgy
* Lister les interactions
* Ajouter un bouton de tweet

### Boîte à Outils

* [Webmention.io](https://webmention.io/) (webmention.io)
* [Bridgy](https://brid.gy/) (brid.gy)
* [Gatsby Plugin Webmention](https://github.com/ChristopherBiscardi/gatsby-plugin-webmention) (github.com)

### Tutoriels

* [Indieweb pt2 : Utilisation des Webmentions dans Eleventy](https://mxb.dev/blog/using-webmentions-on-static-sites/) (mxb.dev)
* [Webmentions Côté Client](https://www.swyx.io/writing/clientside-webmentions/) (swyx.io)
* [Commencer avec les Webmentions dans Gatsby](https://www.knutmelvaer.no/blog/2019/06/getting-started-with-webmentions-in-gatsby/) (knutmelvaer.no)
* [Construire le Plugin Gatsby Webmentions](https://www.christopherbiscardi.com/post/building-gatsby-plugin-webmentions) (christopherbiscardi.com)

### Inspiration

* [Knut Melvær](https://www.knutmelvaer.no/blog/) (knutmelvaer.no)
* [Swyx](https://swyx.io/) (swyx.io)

### Idée de Mise en Page

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Webmentions---Layout.jpg)
_Idée de mise en page des Webmentions_

## Product Hunt

**Catégorie : Clones**

Créez un clone de Product Hunt qui permet aux gens de publier un nouveau produit avec des évaluations.

### Brief

Nous vivons tous pour les produits, qu'il s'agisse de nos téléphones mobiles ou des applications que nous utilisons sur nos ordinateurs portables. 

Bien qu'il existe des tonnes de produits dans le monde, il peut être difficile de naviguer entre les bons et les mauvais. Des outils comme Product Hunt fournissent une plateforme pour découvrir de nouveaux outils et obtenir des réactions et des avis d'autres personnes.

### Niveau 1

La partie la plus importante pour découvrir de nouveaux produits est le produit lui-même. Nous voulons savoir ce qu'est le produit, à quoi il ressemble et comment il fonctionne.  
  
Créez une page qui permet d'ajouter un nouveau produit à un site web avec un titre, une image et une description.

### Niveau 2

Lors de la découverte de produits, les avis sont un moyen de faire confiance à un produit avant de l'acheter. Cela nous aide à gagner en confiance dans ce sur quoi nous allons dépenser notre argent ou notre temps.  
  
Ajoutez la possibilité pour les gens d'ajouter des avis sur chaque produit.

### Niveau 3

Les gens adorent les produits, donc il y en a des tonnes dans le monde. Il y en a trop pour essayer de les trier manuellement, donc nous avons besoin d'un mécanisme pour rechercher et naviguer.  
  
Ajoutez la possibilité de rechercher des produits et de naviguer par catégorie.

### À Faire

* Créer un site web de produits
* Créer une base de données
* Ajouter un formulaire de produit
* Ajouter un produit à la base de données
* Demander un produit pour la page
* Ajouter un formulaire d'avis
* Ajouter des avis à la base de données
* Ajouter des avis au produit
* Ajouter une recherche de produits
* Ajouter des catégories de produits

### Boîte à Outils

* [Hasura](https://hasura.io/) (hasura.io)

### Tutoriels

* [Construire une application clone de Product Hunt en utilisant Hasura et Next.js](https://blog.logrocket.com/building-a-product-hunt-clone-app-using-hasura-and-next-js/) (logrocket.com)
* [Comment construire une version basique de Product Hunt en utilisant React](https://www.freecodecamp.org/news/how-to-build-a-basic-version-of-product-hunt-using-react-f87d016fedae/) (freecodecamp.org)

### Idée de Mise en Page

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Product-Hunt---Layout.jpg)
_Idée de mise en page de Product Hunt_

## Plus de Projets

Si vous voulez plus d'idées de projets, consultez [50 Projets pour React & le Web Statique](https://50reactprojects.com/) !

<p style="text-align: center;">
    <a href="https://50reactprojects.com/">
    	<img src="https://www.freecodecamp.org/news/content/images/2020/08/Twitter-Post---1.jpg" alt="Arrêtez de vous demander ce que je devrais construire ?" style="
		    max-width: 840px;
		    border: solid 5px #0A64EC;
		">
    	<button style="
    		background-color: #9162BB;
	    	color: white;
		    font-weight: bold;
    		padding: .5em 1em;
    		border-radius: .2em;
		    box-shadow: 0 2px 4px rgba(0,0,0,.25);
		">Télécharger gratuitement sur 50reactprojects.com</button>
    </a>
</p>



<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? fe0f Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Inscrivez-vous à ma Newsletter</a>
    </li>
  </ul>
</div>