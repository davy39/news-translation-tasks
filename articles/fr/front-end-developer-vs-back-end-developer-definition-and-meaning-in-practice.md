---
title: Développeur Front End vs Développeur Back End – Définition et Signification
  en Pratique
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-18T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/front-end-developer-vs-back-end-developer-definition-and-meaning-in-practice
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/front-end-back-end.jpg
tags:
- name: 'Back end development '
  slug: back-end-development
- name: backend
  slug: backend
- name: Backend Development
  slug: backend-development
- name: Cloud Computing
  slug: cloud-computing
- name: code
  slug: code
- name: coding
  slug: coding
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Développeur Front End vs Développeur Back End – Définition et Signification
  en Pratique
seo_desc: 'Websites and applications are complex! Buttons and images are just the
  tip of the iceberg. With this kind of complexity, you need people to manage it,
  but which parts are the front end developers and back end developers responsible
  for?


  [The many la...'
---

Les sites web et les applications sont complexes ! Les boutons et les images ne sont que la partie émergée de l'iceberg. Avec ce niveau de complexité, il faut des personnes pour le gérer, mais quelles parties sont de la responsabilité des développeurs front end et des développeurs back end ?

* [Les nombreuses couches du développement](#les-nombreuses-couches-du-developpement)
* [Mais nous ne sommes pas tous full stack](#heading-nous-ne-sommes-pas-tous-full-stack)
* [Quelle est donc la différence entre le Développement Front End et le Développement Back End ?](#heading-quelle-est-donc-la-difference-entre-le-developpement-front-end-et-le-developpement-back-end)
* [Qu'est-ce que le Développement Front End ?](#heading-quest-ce-que-le-developpement-front-end)
* [Qu'est-ce que le Développement Back End ?](#heading-quest-ce-que-le-developpement-back-end)
* [Là où les choses deviennent floues](#heading-la-ou-les-choses-deviennent-floues)
* [Ressources pour apprendre](#heading-ressources-pour-apprendre)

## Les nombreuses couches du développement

Que vous travailliez sur un site web ou une application native iOS, tous les environnements de développement partagent un thème commun — il y a un front end et un back end à une application.

Cette ligne peut devenir floue, surtout avec l'essor de JavaScript et du monde [serverless](https://en.wikipedia.org/wiki/Serverless_computing). Avec les outils se fusionnant quelque peu, nous pouvons parfois nous demander si nous sommes un [développeur full stack](https://www.colbyfayock.com/2020/02/how-to-become-a-full-stack-web-developer-in-2020/).

%[https://twitter.com/holtbt/status/977419276251430912]

## Mais nous ne sommes pas tous full stack

Autant nous pourrions tous [vouloir l'être](https://full-stack.netlify.app/), nous ne sommes pas tous des développeurs full stack. Personnellement, je me trouve capable d'être productif dans le back end d'une application, mais ce n'est pas mon point fort et je préfère de loin être concentré sur la construction d'interfaces utilisateur.

Et certaines personnes sont l'inverse, où elles sont les plus à l'aise pour construire des APIs dans le back end d'une application et, bien qu'elles puissent construire une interface utilisateur, cela pourrait être plus une expérience de type prototype qu'une application complète.

## Quelle est donc la différence entre le Développement Front End et le Développement Back End ?

Même si vous êtes un développeur full stack, cela ne signifie pas qu'il n'y a pas de division des responsabilités.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/front-end-vs-back-end-engineer-2.jpg)
_Ingénieur Front End vs Ingénieur Back End_

À quoi ressemblent donc ces responsabilités ?

## Qu'est-ce que le Développement Front End ?

Le front end d'une application fait généralement référence à la couche qui représente l'interface utilisateur (UI). Cela peut inclure tout, d'un site statique avec HTML et CSS à une application [React](https://reactjs.org/) complète qui alimente l'interface utilisateur.

### À quoi ressemblait traditionnellement le Développement Front End ?

JavaScript domine actuellement le front end web, mais ce n'était pas toujours le cas. Bien qu'il ait pu être utilisé pour ajouter de petites interactions à un site, les front ends étaient traditionnellement rendus à l'aide de langages de templating côté serveur comme [PHP](https://www.php.net/) et [Template Toolkit](http://www.template-toolkit.org/) ([Perl](https://www.perl.org/)).

Cela est devenu super populaire en pratique avec des frameworks maison ou des outils comme [Wordpress](https://wordpress.org/) qui utilisaient PHP pour alimenter une massive communauté de développeurs qui construisaient leurs sites web avec ces outils.

Le fonctionnement était le suivant : le langage de templating pouvait obtenir ses données directement du serveur au moment du rendu. Lorsqu'un navigateur demandait la page directement de l'origine (le serveur lui-même), les données dont le template avait besoin étaient fournies par la logique de l'application à ce moment-là.

Certains des outils front end plus traditionnels incluent :

* Bibliothèques comme [jQuery](https://jquery.com/) ou [MooTools](https://mootools.net/)
* Frameworks de sites web comme [Wordpress](https://wordpress.com/)
* CSS simple [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* Utilisation abondante des éléments [Table](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)

Mais avec le temps, JavaScript est devenu de plus en plus mature en tant que langage et les navigateurs de plus en plus puissants, ce qui a conduit à l'idée que nous pouvions déplacer plus de ce travail vers le navigateur pour construire des expériences plus rapides et plus interactives.

### À quoi ressemble le Développement Front End maintenant ?

Il est maintenant courant de voir des sites web et des applications riches en JavaScript construits à l'aide de frameworks UI comme [React](https://reactjs.org/), [Vue](https://vuejs.org/), et [Angular](https://angular.io/). Ces outils fournissent des abstractions qui permettent aux développeurs de construire des interfaces utilisateur complexes avec des motifs réutilisables comme les composants.

Lorsque le navigateur charge la page, la page reçoit un document HTML initial qui inclut également la balise script pour le JavaScript (comme toujours). Mais une fois que ce JavaScript est chargé, il atteint les APIs en utilisant des requêtes navigateur qui, une fois complétées, mettent à jour la page pour remplir tout type de données dynamiques que vous obtiendriez typiquement avec ce premier document HTML.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/building-website-with-more-steps.jpg)
_C'est comme construire un site web... avec plus d'étapes_

Bien que cela semble être plus d'étapes, cela fournit généralement un chargement et un rendu de page initiaux plus rapides, sans compter qu'il offre une excellente expérience développeur. En livrant moins sur cette première requête et en priorisant ce qui se charge après, cela se traduit généralement par une meilleure expérience utilisateur.

Certains des outils front end qui sont plus courants et gagnent en popularité incluent :

* Frameworks UI comme [React](https://reactjs.org/) ou [Vue](https://vuejs.org/)
* Frameworks web comme [Gatsby](https://www.gatsbyjs.org/)
* Compilateurs comme [Babel](https://babeljs.io/)
* Bundlers comme [Webpack](https://webpack.js.org/)
* Outils CSS comme [Sass](https://sass-lang.com/)

Mais ces APIs, qu'elles soient payantes ou créées par nous-mêmes, doivent être construites _quelque part_. C'est là que le back end entre en jeu.

## Qu'est-ce que le Développement Back End ?

La couche back end est généralement là où se trouve la logique métier. Cela peut être super complexe comme les règles qui déterminent les revenus pour une entreprise de commerce électronique ou quelque chose de plus courant comme un profil utilisateur.

### À quoi ressemblait traditionnellement le Développement Back End ?

Les back ends des applications étaient historiquement construits en utilisant des langages côté serveur comme [PHP](https://www.php.net/) ou [Ruby](https://www.ruby-lang.org/en/). L'idée est que vous avez un serveur qui doit effectuer des opérations complexes, donc la façon de le faire est avec un langage que le serveur comprendrait.

À chaque requête vers le serveur, le back end effectuait la pile complète des opérations, y compris le rendu du front end. En utilisant des frameworks ou des architectures DIY, le back end acceptait la requête, déterminait ce qu'il devait faire avec cette requête, exécutait toute logique métier nécessaire avec la requête, et fournissait au front end les données dont il avait besoin pour afficher une réponse à cette requête.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/front-end-back-end-500-error.jpg)
_Back end donnant au front end une erreur 500 Internal Server Error_

Certains des outils back end plus traditionnels incluent :

* Serveurs sur site ou gérés à distance comme [Rackspace](https://www.rackspace.com/)
* Serveurs HTTP utilisant [Apache](https://httpd.apache.org/)
* Bases de données comme [MySQL](https://www.mysql.com/)
* Langages côté serveur comme [PHP](https://www.php.net/) ou [Perl](https://www.perl.org/)
* Frameworks d'application comme [Ruby on Rails](https://rubyonrails.org/)

### À quoi ressemble le Développement Back End maintenant ?

Les stacks back end ressemblent quelque peu à ce qu'elles étaient avant, à part les nouveaux motifs de code, sauf que plus souvent vous verrez les back ends fournir des données via des requêtes HTTP au lieu de directement aux templates sur lesquels l'équipe front end travaille.

Bien que la fondation ne soit pas super différente, elle devient en réalité de plus en plus complexe car vous devez gérer différentes implications de sécurité qui pourraient compromettre votre système si elles ne sont pas correctement configurées, comme laisser une API ouverte au public qui retourne des données utilisateur sensibles.

Mais aussi, la façon dont le serveur fonctionne peut être complètement différente. Alors qu'auparavant, nous pouvions exécuter notre Python sur notre propre serveur géré (nous pouvons toujours le faire), nous pouvons maintenant utiliser des fonctions serverless avec des outils comme [AWS Lambda](https://aws.amazon.com/lambda/) qui simplifient la façon dont nous gérons le code.

Bien que "[serverless](https://en.wikipedia.org/wiki/Serverless_computing)" ne signifie pas nécessairement qu'il n'y a littéralement aucun serveur, cela signifie qu'en tant que service, le développeur n'a pas à se soucier de la maintenance de ce serveur et peut se concentrer uniquement sur le code qu'il doit exécuter.

Certains des outils back end qui sont plus courants et gagnent en popularité incluent :

* Serveurs cloud comme [AWS EC2](https://aws.amazon.com/ec2/)
* Services serverless comme [AWS Lambda](https://aws.amazon.com/lambda/)
* Bases de données NoSQL comme [MongoDB](https://www.mongodb.com/)
* Langages comme [Python](https://www.python.org/) ou JavaScript via [NodeJS](https://nodejs.org/)
* Frameworks d'application web comme [Serverless Framework](https://www.serverless.com/)

## Là où les choses deviennent floues

Une partie du twist avec les back ends est que vous pouvez maintenant écrire votre back end avec JavaScript. Avec l'avènement de [Node.js](https://nodejs.org/en/), les développeurs ont eu la possibilité d'utiliser leur langage de navigateur préféré pour faire la plupart des mêmes choses auxquelles ils étaient habitués et familiers, mais maintenant sur un serveur.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/nodejs-never-stopped-to-think-if-should.jpg)
_Nous ne nous sommes jamais arrêtés pour penser si nous devrions écrire du JS sur un serveur_

Bien que tout le monde ne soit pas fan d'exécuter JavaScript en tant que langage côté serveur, il est devenu un peu plus facile d'utiliser le même langage pour écrire la pile complète d'une application. Cela a changé un peu la donne en ce qui concerne les front ends et les back ends.

Mais cela a aussi commencé à faire un cercle complet où vous voyez maintenant des systèmes qui construisent des APIs juste [à côté du front end](https://redwoodjs.com/tutorial/redwood-file-structure) similaire à ce que vous pourriez voir dans une stack traditionnelle.

## Front End vs Back End

Quelle que soit la stack, il y aura toujours une séparation des préoccupations. L'interface utilisateur et toutes les interactions, qu'elles soient rendues sur le serveur ou dans le navigateur, sont ce qui fait que le front end est le front end et les données et la logique métier, qu'elles proviennent du serveur dans le placard de votre entreprise ou d'une fonction gérée, sont ce qui fait que le back end est le back end.

Que vous préfériez travailler sur les fonctionnalités orientées utilisateur ou construire la logique qui leur permet de faire des choses, il y a beaucoup de ressources pour commencer.

## Ressources pour apprendre

### Front End

* [Certification Responsive Web Design de freecodecamp.org](https://www.freecodecamp.org/learn/) (freecodecamp.org)
* [Beginner Javascript](https://beginnerjavascript.com/) (beginnerjavascript.com - Wes Bos)
* [Tutoriel React pour Débutants](https://www.youtube.com/watch?v=Ke90Tje7VS0) (youtube.com - Programming with Mosh)
* [Front End Masters](https://frontendmasters.com/) (frontendmasters.com)

### Back End

* [Certification APIs et Microservices de freecodecamp.org](https://www.freecodecamp.org/learn) (freecodecamp.org)
* [Super simple start to serverless](https://kentcdodds.com/blog/super-simple-start-to-serverless/) (kentcdodds.com)
* [Formation AWS Certified Cloud Practitioner 2019 - Un Cours Vidéo Gratuit de 4 heures](https://www.freecodecamp.org/news/aws-certified-cloud-practitioner-training-2019-free-video-course/) (freecodecamp.org)
* [Introduction à l'Informatique de CS50](https://www.edx.org/course/cs50s-introduction-to-computer-science) (edx.org)

### Tout ce qui précède

* [Comment Devenir un Développeur Web Full Stack en 2020](https://www.colbyfayock.com/2020/02/how-to-become-a-full-stack-web-developer-in-2020/) (colbyfayock.com)
* [Egghead.io](https://egghead.io/?af=atzgap) (egghead.io)
* [100 Days of Code](https://www.100daysofcode.com/) (100daysofcode.com)
* [The Web Developer Bootcamp](https://www.udemy.com/course/the-web-developer-bootcamp/) (udemy.com - Colt Steele)

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e8f4f9 Inscrivez-vous à ma newsletter</a>
    </li>
  </ul>
</div>