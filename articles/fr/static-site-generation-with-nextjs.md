---
title: Qu'est-ce que la génération de site statique ? Comment Next.js utilise SSG
  pour les applications web dynamiques
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-11-18T17:49:33.000Z'
originalURL: https://freecodecamp.org/news/static-site-generation-with-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/static-generation.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: Static Site Generators
  slug: static-site-generators
seo_title: Qu'est-ce que la génération de site statique ? Comment Next.js utilise
  SSG pour les applications web dynamiques
seo_desc: "Static websites are as old as the web itself. But the rise of JavaScript\
  \ has opened the door to make those static sites more dynamic. \nWhile that can\
  \ include building an HTML file by hand, how can we leverage static generation to\
  \ build apps with mode..."
---

Les sites web statiques existent depuis aussi longtemps que le web lui-même. Mais l'essor de JavaScript a ouvert la porte pour rendre ces sites statiques plus dynamiques. 

Bien que cela puisse inclure la création d'un fichier HTML à la main, comment pouvons-nous utiliser la génération statique pour construire des applications avec des outils modernes ?

* [Qu'est-ce que la génération statique ?](#heading-questce-que-la-generation-statique)
* [Que se passe-t-il pendant la génération statique ?](#heading-que-se-passe-t-il-pendant-la-generation-statique)
* [Comment Next.js utilise la génération statique ?](#heading-comment-nextjs-utilise-la-generation-statique)
* [Générer statiquement une application avec Next.js](#generer-statiquement-une-application-avec-nextjs)

%[https://www.youtube.com/watch?v=6ElI2J4Uro]

## Qu'est-ce que la génération statique ?

La génération statique décrit le processus de compilation et de rendu d'un site web ou d'une application au moment de la construction. Le résultat est un ensemble de fichiers statiques, y compris le fichier HTML lui-même et les ressources comme JavaScript et CSS.

Si vous n'avez pas entendu parler de la génération statique mais que ce concept vous semble familier, vous avez peut-être entendu parler de son nom complet, Génération de Site Statique, ou de son acronyme SSG.

## Que se passe-t-il pendant la génération statique ?

Les applications web basées sur JavaScript, telles que nous les connaissons traditionnellement, fonctionnent en exécutant des bibliothèques comme React ou des scripts au moment de l'exécution dans le navigateur. 

Lorsque le navigateur reçoit la page, il s'agit généralement de HTML simple sans beaucoup de contenu. Cela charge ensuite les scripts pour extraire le contenu dans la page, un processus également connu sous le nom d'hydratation.

Avec la génération statique, des outils comme Next.js tentent de rendre cette page principalement comme elle le ferait dans le navigateur, mais au moment de la compilation. Cela nous donne la possibilité de servir l'ensemble du contenu au premier chargement. Les scripts hydratent toujours la page pendant ce processus, mais idéalement avec moins de changements ou aucun changement du tout.

## Comment Next.js utilise la génération statique ?

Dès sa sortie, Next.js tentera de générer statiquement toutes les pages qu'il peut. Il le fait en détectant comment une application récupère ses données.

Next.js fournit [plusieurs API différentes pour récupérer des données](https://nextjs.org/docs/basic-features/data-fetching) incluant `getStaticProps` et `getServerSideProps`, qui, selon leur utilisation, déterminent comment Next.js construira votre application.

Si vous utilisez uniquement `getStaticProps` pour récupérer des données, Next.js récupérera ces données au moment de la construction, vous laissant avec une page complètement statique. 

Si vous utilisez `getServerSideProps`, Next.js saura que l'application nécessite un serveur pour rendre ces pages. 

Avec une solution de déploiement comme Vercel qui [configurera automatiquement un serveur](https://vercel.com/solutions/nextjs), Next.js chargera toutes les données lorsqu'une personne demandera la page depuis le serveur.

Bien qu'il ne le fasse pas par défaut, Next.js fournit également la possibilité d'exporter l'application en fichiers statiques dans un répertoire séparé après la construction de l'application.

Tout d'abord, vous exécuteriez la commande `next build` pour construire l'application, puis vous exécuteriez `next export` qui, par défaut, rend l'application disponible sous forme de fichiers statiques dans le répertoire `out`.

## Comment générer statiquement une application avec Next.js

Pour avoir une idée de comment cela fonctionne, nous pouvons rapidement créer une nouvelle application Next.js.

Les seules exigences pour cela sont que vous ayez [Node](https://nodejs.org/en/) installé avec npm et la capacité d'utiliser un terminal pour exécuter des commandes.

### Comment créer une application Next.js

Pour commencer, il suffit d'exécuter une seule ligne dans le terminal.

Ouvrez le répertoire dans lequel vous souhaitez créer votre projet et exécutez :

```
npx create-next-app mon-application-nextjs-statique

```

Une fois l'installation terminée, vous pouvez naviguer vers votre nouveau répertoire de projet :

```
cd mon-application-nextjs-statique

```

Une fois là, démarrez votre serveur de développement :

```
npm run dev

```

Et une fois le serveur prêt, vous pouvez ouvrir [http://localhost:3000](http://localhost:3000) dans votre navigateur où vous pouvez maintenant voir votre nouvelle application Next.js !

![Image](https://www.freecodecamp.org/news/content/images/2020/11/new-nextjs-app.jpg)
_Nouvelle application Next.js_

### Comment construire une application Next.js

Maintenant que nous avons notre application disponible, essayons de la construire.

Dans le même répertoire, exécutez la commande :

```
npm run build

```

Si vous regardez la sortie dans le terminal, nous voyons quelques choses importantes se produire.

Tout d'abord, Next.js nous informe qu'il exécute son processus de construction, y compris l'optimisation de l'application pour les performances, la compilation de l'application et la collecte de données.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/nextjs-build.jpg)
_Construction avec Next.js_

Ensuite, nous voyons que Next.js nous montre une ventilation de la façon dont il a construit chaque page.

Le modèle de démarrage par défaut de Next.js inclut quelques pages statiques et un exemple de route API. 

En utilisant la légende en bas, nous pouvons voir que toutes les pages et les ressources ont été générées statiquement avec une route marquée comme nécessitant un serveur, ce qui serait notre route API.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/nextjs-static-generation.jpg)
_Next.js générant des pages_

_Note : Pour les besoins de ce guide, nous pouvons ignorer la route API, mais Next.js, ainsi que Vercel, fournit la possibilité de construire des fonctions lambda dans le cadre de l'API Next.js._

### Comment construire une application Next.js statique

Avec notre sortie de construction Next.js, nous savons que nous venons de construire quelques pages statiques, mais nous pourrions avoir du mal à les trouver. Si nous regardons les dossiers et les fichiers dans notre projet, il n'est pas immédiatement clair où se trouvent ces fichiers.

Lorsque Next.js construit une application, par défaut, il ne sort cette application que dans le répertoire `.next`. Cela inclut les fichiers de configuration que des outils comme Vercel peuvent utiliser et comprendre pour déployer l'application.

Techniquement, ce répertoire inclut toute notre application, mais ce n'est pas quelque chose que nous pouvons facilement déployer sur un hébergement statique.

Next.js fournit également la possibilité d'exporter une application. Cela prendra l'application que nous avons construite et produira un ensemble de fichiers statiques que nous pourrons ensuite utiliser pour déployer notre application.

Dans le fichier `package.json`, mettez à jour le script `build` pour inclure `next export` :

```
"build": "next build && next export",

```

Une fois mis à jour, exécutez à nouveau la commande de construction dans le répertoire du projet :

```
npm run build

```

Et maintenant nous pouvons voir que non seulement nous avons construit l'application comme nous l'avons fait dans notre dernière étape, Next.js nous informe également que nous exportons l'application que nous avons construite en fichiers statiques.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/nextjs-exporting-static-app.jpg)
_Exportation de l'application statique Next.js_

Si nous regardons à l'intérieur de notre dossier de projet, nous devrions maintenant voir un nouveau répertoire appelé `out`.

Si nous regardons à l'intérieur de ce dossier, nous pouvons maintenant voir notre application entière compilée statiquement, y compris le fichier `index.html` ainsi que tous les CSS et JS nécessaires pour utiliser l'application !

![Image](https://www.freecodecamp.org/news/content/images/2020/11/nextjs-static-output.jpg)

## Où pouvons-nous aller à partir de là ?

Nous avons appris que nous pouvons utiliser Next.js et le concept de Génération Statique pour compiler statiquement une application. 

Des outils comme Next.js peuvent le faire en compilant notre code, similaire à ce que nous pourrions voir dans un navigateur, de sorte que lorsque notre application atteint le navigateur, elle est prête à être utilisée.

Avec une simple commande, nous pouvons également construire et compiler notre application, ainsi que l'exporter en fichiers statiques. Nous pouvons déployer ces fichiers statiques sur n'importe quel service de stockage statique comme Vercel ou AWS S3. Cela nous fournit un moyen facile de créer des applications web dynamiques qui sont rapides et économiques.

Apprenez-en plus sur la façon dont Next.js utilise ses différentes API pour fournir à la fois des expériences statiques et dynamiques en [visitant la documentation de Next.js](https://nextjs.org/docs/basic-features/data-fetching).

<div id="colbyfayock-author-card">
  <p style="margin: 1em 0;">
    <a href="https://jamstackhandbook.com/" style="display: block;">
      <img src="https://www.freecodecamp.org/news/content/images/size/w1600/2020/11/jamstack-handbook-banner.jpg" alt="Jamstack Handbook" style="width:100%;display: block;margin: 0;border: solid 1px #d2dee9;">
    </a>
  </p>
</div>

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">🐦 Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">📺 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">📫 Inscrivez-vous à ma newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">💝 Sponsorisez-moi</a>
    </li>
  </ul>
</div>