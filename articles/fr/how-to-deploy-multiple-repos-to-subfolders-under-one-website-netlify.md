---
title: Comment déployer plusieurs dépôts dans des sous-dossiers sous un seul site
  web avec Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-13T14:57:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-multiple-repos-to-subfolders-under-one-website-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-xxss-is-back-777001.jpg
tags:
- name: documentation
  slug: documentation
- name: Netlify
  slug: netlify
- name: Next.js
  slug: nextjs
- name: React
  slug: reactjs
seo_title: Comment déployer plusieurs dépôts dans des sous-dossiers sous un seul site
  web avec Netlify
seo_desc: 'By Abdulmalik Salawu

  Hi there! 👋 You''re probably here because you are trying to deal with hosting two
  separate websites or repositories under one website using Netlify.

  And maybe you''ve checked out the answers on the Netlify community page, but you
  ...'
---

Par Abdulmalik Salawu

Bonjour ! 👋 Vous êtes probablement ici parce que vous essayez de gérer l'hébergement de deux sites web ou dépôts séparés sous un seul site web en utilisant Netlify.

Et peut-être avez-vous consulté les réponses sur la page communautaire de Netlify, mais vous êtes toujours confus.

La même confusion et le même mal de tête m'ont conduit à écrire ce tutoriel pour que vous n'ayez pas à lutter autant que moi.

C'est un peu délicat, mais ça marche : la solution à ce problème est le fichier `netlify.toml` ou `_redirects`.

Commençons.

Je travaille sur un projet avec quelques collègues, et nous avons divisé les tâches de sorte que je m'occupe de la documentation.

<h2>Technologies que nous utiliserons ici</h2>

* [Docusaurus](https://docusaurus.io/docs/) pour créer des sites de documentation magnifiques en un rien de temps.
* Next.js/React.js pour notre site web principal

Commençons et voyons comment nous pouvons héberger la documentation. Nous pouvons faire cela de deux manières :

1. En utilisant un sous-domaine, docs.mainsite.dev
2. En utilisant le domaine principal mainsite.dev et en hébergeant les docs comme un sous-répertoire sur mainsite.dev/docs.

D'après ce que j'ai vu être mis en œuvre par d'autres projets dans leur documentation, je voulais l'héberger comme un sous-dossier via Netlify aussi. 

Je pense que cela aiderait nos docs à avoir cet aspect professionnel.

Si vous allez héberger Docusaurus comme sous-dossier aussi, vous devez faire quelques configurations.

## Étape 1 – Mettre à jour l'URL de base

Changez le **baseUrl** dans votre fichier docusaurus.config.js en "**/docs/"** avec le code suivant :

```javascript
  title: 'Titre de vos docs',
  tagline: 'Slogan de vos docs',
  url: 'my-docs-site.netlify.app',
  baseUrl: "/docs/",
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: '/favicon.ico',
```

En changeant votre URL de base en **/docs/**, cela fait en sorte que votre site web se rende exactement comme **https://mainsite.dev/docs/**, qui est le chemin des docs.

Si vous deviez définir le **baseUrl** à "/", il y aurait une erreur. Cela signifie également que nous n'avons pas à gérer la proxyfication de notre site de docs.

## Étape 2 – Mettre à jour le routeBasePath

Vous devrez également vous assurer que les contenus de la documentation sont servis depuis votre domaine racine en changeant le **routeBasePath** en **'/'**. 

Tout comme vous le voyez dans l'extrait ci-dessous :

```javascript
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
        },
      }),
    ],
  ],
```

Cela vous aidera à activer le mode docs uniquement sur Docusaurus. De cette façon, vos docs seront servis depuis votre domaine racine mais avec le chemin '/docs/' comme chemin de base.

Après cela, vous pouvez exécuter `npx docusaurus start` sur votre localhost pour voir si votre site de docs se construira et se rendra bien sans problèmes. 

Si vous n'avez pas de problèmes, alors vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/docusaurus-run-localhost-1.jpg)
_Votre site Docusaurus devrait se rendre comme ceci sur le chemin '/docs/' comme chemin de base._

Pour en savoir plus sur la configuration du mode docs uniquement de Docusaurus, vous pouvez lire [ceci](https://docusaurus.io/docs/docs-introduction#docs-only-mode).

## Étape 3 – Déployer sur Netlify

Maintenant, il est temps de déployer votre site de docs sur Netlify. Si vous ne savez pas déjà comment faire cela, vous pouvez vous référer à ce [guide](https://docusaurus.io/docs/deployment#deploying-to-netlify).

Une fois que vous avez terminé le déploiement, l'URL de votre site web Netlify devrait déjà être disponible comme ceci : // my-docs-site.netlify.app.

## Étape 4 – Proxyfication

Voici la partie où vous allez faire la proxyfication.

Vous avez déjà hébergé votre site web principal sur Netlify et votre site de docs a été déployé sur Netlify aussi.

Maintenant, vous devez créer un fichier _netlify.toml_ à la racine de votre projet/dépôt de votre site web principal, et y ajouter les lignes suivantes :

```markdown
[[redirects]]
from = "/docs/*"
to = "https://my-docs-site.netlify.app/:splat"
status = 200
force = false
```

La règle ci-dessus garantit que, chaque fois que le chemin /docs/ est interrogé sur votre site principal, votre site de docs se charge normalement sur votre chemin main-website.netlify.app/docs/.

Alternativement, vous pouvez faire cette proxyfication via votre site de docs/dépôt. Il suffit de créer un fichier netlify.toml à la racine de votre site de docs/dépôt, et y ajouter les lignes suivantes :

```toml
[[redirects]]
from = "/*"
to = "https://main-website.netlify.app/docs/:splat"
status = 301
force = true
```

La règle ci-dessus garantit que chaque fois que le chemin /* est interrogé sur votre site de docs, il se chargera normalement sur votre chemin main-website.netlify.app/docs/.

Vous remarquerez également que votre site de docs sur le site Netlify est cassé – mais il fonctionne parfaitement sur votre site principal. 

Puisque cela fonctionne et que nous avons atteint nos objectifs, alors laissons-le tel quel 😁.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/docs-site-netlify-error.jpg)
_Site Docusaurus cassé pour la documentation en sous-dossier_

**REMARQUE :** Ne ajoutez jamais les règles à votre site de docs et à votre site principal en même temps, car cela provoquera un conflit d'erreurs "TOO MANY REDIRECTS".

Donc, vous ajoutez soit les règles à votre site de docs, soit à votre site principal, mais pas aux deux.

## Répondons à quelques questions

**Q :** Pourquoi choisirais-je d'utiliser le fichier _netlify.toml_, et non le fichier __redirects_ ?

Oui, je suis d'abord allé pour l'option facile et j'ai essayé le fichier _redirects aussi. Mais ce n'était pas si facile car vous devrez toujours copier le fichier __redirects_ dans votre dossier **build/** ou **public/** lors de la construction de votre site Netlify.

Cela vous oblige à modifier vos paramètres de construction Netlify pour quelque chose comme ceci :

```txt
npm run build && cp _redirects public/
```

Vous pouvez également réaliser la proxyfication en utilisant le fichier __redirects_. Les règles seront dans le format suivant pour le site principal :

```txt
/docs/* https://my-docs-site.netlify.app/:splat 200
```

et dans ce format pour votre site de docs :

```txt
/* https://main-website.netlify.app/docs/:splat 301!
```

**Q :** Pourquoi choisirais-je d'utiliser les URL Netlify dans toutes les règles de proxyfication au lieu de notre URL de domaine personnalisé ?

Eh bien, la communauté Netlify conseille d'utiliser les URL Netlify, car c'est une méthode plus fiable pour faire la proxyfication.

## Conclusion

Félicitations 🎉, content que vous soyez arrivé à la fin de ce guide. 

Je crois que vous avez appris quelque chose de nouveau aujourd'hui.

Il est temps d'aller implémenter et de faire en sorte que votre documentation de projet ait également l'air professionnelle en l'hébergeant dans le sous-dossier de votre site principal. 👍.

Vous pouvez également partager cet article, afin que d'autres puissent le voir.

## Ressources :

* [Netlify Rules Playground](https://play.netlify.com/redirects)
* [[Guide de support] Puis-je déployer plusieurs dépôts dans un seul site ?](https://answers.netlify.com/t/support-guide-can-i-deploy-multiple-repositories-in-a-single-site/179)