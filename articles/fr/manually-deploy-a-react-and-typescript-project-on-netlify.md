---
title: Comment déployer manuellement un projet React et TypeScript sur Netlify
subtitle: ''
author: Losalini Rokocakau
co_authors: []
series: null
date: '2024-04-12T18:02:59.000Z'
originalURL: https://freecodecamp.org/news/manually-deploy-a-react-and-typescript-project-on-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/cover-image-4.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Netlify
  slug: netlify
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Comment déployer manuellement un projet React et TypeScript sur Netlify
seo_desc: 'In this tutorial, I''ll teach you how to manually deploy a React and TypeScript
  project with Vite on Netlify. I will show you a few quick and simple steps to get
  live versions of your projects up and running.

  To follow along with this tutorial, there ...'
---

Dans ce tutoriel, je vais vous apprendre comment déployer manuellement un projet React et TypeScript avec Vite sur Netlify. Je vais vous montrer quelques étapes rapides et simples pour mettre en ligne des versions de vos projets.

Pour suivre ce tutoriel, voici quelques prérequis :

1. Un projet React et TypeScript existant avec Vite que vous souhaitez déployer.
2. L'éditeur Visual Studio Code (VSCode) ou tout autre éditeur de code tel que Sublime.
3. Optionnellement, vous pouvez simplement utiliser une ligne de commande/terminal au lieu du terminal intégré de votre éditeur de code.
4. Un compte Netlify existant auquel vous êtes déjà connecté.

Passons maintenant au déploiement !

### À quoi s'attendre

Vous allez déployer votre projet manuellement sur Netlify, renommer votre site sur la plateforme et pouvoir avoir une version en ligne de votre projet.

## Comment déployer votre projet React et TypeScript

### 1. Ouvrez votre projet existant sur VSCode

Ouvrez votre projet dans l'éditeur de code de votre choix.

### 2. Construisez le projet

Ouvrez le terminal dans VSCode et utilisez le code ci-dessous pour construire votre projet :

```
npm run build
```

Cela devrait générer un dossier _dist_ dans votre répertoire racine où la version minifiée de votre projet est créée et stockée.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/fig-2-0.png)
_**Figure 2.0** Exécution du projet dans le terminal qui crée le dossier dist dans la structure du projet._

### 3. Glissez-déposez votre dossier Dist dans Netlify

Sur Netlify, sous l'onglet Team Overview, cliquez sur le bouton Add New Site. Il devrait y avoir trois options :

1. Importer un projet existant
2. Commencer à partir d'un modèle
3. Déployer manuellement

Sélectionnez la troisième option pour déployer manuellement.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/fig-3-0.png)
_**Figure 3.0** Cliquer sur le bouton Add new site montre les trois options parmi lesquelles choisir. Sélectionnez "Deploy Manually"._

Cela devrait vous mener à la page comme illustré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/fig-3-1.png)
_**Figure 3.1** Vue de glisser-déposer lors du choix de déployer manuellement._

Cliquez sur la page et naviguez dans le chemin de fichier de votre projet.

Téléchargez le dossier dist qui a été précédemment généré dans votre projet sur Netlify.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/fig-3-2.png)
_**Figure 3.2** Navigation dans le dossier du projet et téléchargement du dossier dist sur Netlify._

Cela prendra quelques secondes ou minutes pour déployer votre projet.

Une fois le déploiement réussi, vous verrez une page similaire à celle ci-dessous. Par défaut, elle donne un nom de sous-domaine généré aléatoirement à l'URL de votre site. Par exemple, dans mon cas, c'est _delightful-pie-bba293._

![Image](https://www.freecodecamp.org/news/content/images/2024/04/fig-3-3.png)
_**Figure 3.3** Le déploiement est réussi._

Le nom de votre site est le sous-domaine du domaine de Netlify.

```
https://<nom-de-votre-site>.netlify.app
```

### 4. Renommez votre site

Cliquez sur la configuration du site qui se trouve dans la barre latérale de gauche.

Dans les informations du site sous les détails du site, cliquez sur le bouton Change Site Name.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/fig-4-0.png)
_**Figure 4.0** Vue des détails du site sous la configuration du site._

Cela devrait vous donner une fenêtre contextuelle pour changer le nom de votre site.

Changez le nom de votre site comme vous le souhaitez :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/fig-4-1-1.png)
_**Figure 4.1** Changement du nom de votre site._

Retournez à l'aperçu du site où vous pouvez trouver l'URL de votre site. L'URL de votre site se trouve juste sous le nom de votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/figure-4-2.png)
_**Figure 4.2** Aperçu du site où vous pouvez trouver l'URL de votre site._

Cliquez sur l'URL pour voir votre site !

![Image](https://www.freecodecamp.org/news/content/images/2024/04/fig-4-3-1.png)
_**Figure 4.3** Visualisation de mon site depuis la nouvelle URL créée._

## Conclusion

Maintenant, vous avez des versions en ligne de vos projets et vous êtes capable de les déployer manuellement sur Netlify.

Il y a des étapes supplémentaires à suivre pour ajouter un domaine personnalisé, mais nous n'aborderons pas cela dans ce tutoriel.

Cela facilite également la référence à vos projets en attendant sur vos CV, site portfolio ou ailleurs.

Merci d'avoir suivi cet article et bon codage ! 🧙🏻

### 📝 Ressources supplémentaires :

1. Cet article est une version résumée de cette [vidéo](https://www.youtube.com/watch?v=7T4w0QJtL-o). Si vous préférez regarder et suivre, alors c'est la vidéo à regarder.
2. Il existe de nombreuses autres plateformes telles que [Cloudflare](https://www.cloudflare.com/en-gb/), [Heroku](https://www.heroku.com/), ou [Vercel](https://vercel.com/) pour déployer vos projets. Cette [vidéo](https://www.youtube.com/watch?v=gcwQg8-wqQ0), par exemple, vous montre comment déployer vos projets sur Vercel.

### 🔍 Connectez-vous avec moi !

Suivez-moi sur [X](https://twitter.com/chelmerrox) et [LinkedIn](http://www.linkedin.com/in/losalini-rokocakau) si vous aimez mon travail et souhaitez rester informé pour plus de contenu.