---
title: Comment déployer une application basée sur React Router sur Netlify
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-04-19T21:38:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-react-router-based-app-to-netlify
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/routing.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Netlify
  slug: netlify
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: Comment déployer une application basée sur React Router sur Netlify
seo_desc: 'In this article, we''ll learn the most popular ways of deploying a React
  app to Netlify. We''ll also learn the configuration changes you''ll need to make
  to deploy a Routing-based React app.

  The thing I love about Netlify is that it provides a lot of us...'
---

Dans cet article, nous allons apprendre les méthodes les plus populaires pour déployer une application React sur Netlify. Nous allons également apprendre les modifications de configuration nécessaires pour déployer une application React basée sur le routage.

Ce que j'aime chez [Netlify](https://www.netlify.com/), c'est qu'il offre de nombreuses fonctionnalités utiles gratuitement, telles que :

* Un moyen de déployer un site web statique en quelques secondes
* Le déploiement continu, ce qui signifie que lorsque vous connectez votre dépôt Github/Gitlab/Bitbucket, il déclenche automatiquement le déploiement lorsque de nouveaux commits sont poussés vers le dépôt
* L'assurance que votre site web ne tombe jamais en panne, même pendant les nouveaux déploiements
* Vous permet de revenir facilement à n'importe quelle version précédente fonctionnelle de votre site avec un seul clic
* Vous permet de prévisualiser rapidement n'importe quelle version précédemment déployée de l'application
* Changer le domaine ou le sous-domaine de votre site instantanément

et bien plus encore.

Alors, voyons comment déployer une application React sur Netlify.

> Vous voulez apprendre Redux depuis le début et créer une application de commande de nourriture à partir de zéro ? Consultez le cours [Mastering Redux](https://master-redux.yogeshchavan.dev/).

## Glisser-déposer le dossier de construction dans Netlify

La méthode la plus rapide et la plus facile pour déployer une application React est de glisser-déposer le dossier de construction dans Netlify.

Pour créer un dossier de construction, exécutez simplement la commande `npm run build` ou `yarn build` à partir de la ligne de commande depuis le dossier de votre projet.

Une fois le dossier de construction créé, il vous suffit de déposer le dossier dans la zone de dépôt sous le menu `sites`, comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/drag_drop.gif)

## Comment déployer une application sur Netlify à partir d'un dépôt GitHub

C'est ma méthode préférée pour déployer des applications sur Netlify.

Parce que chaque fois que vous poussez des modifications vers le dépôt GitHub, elles seront automatiquement déployées sur Netlify. Vous pouvez également voir toutes les versions déployées et revenir facilement à n'importe quelle version précédente du code avec un seul clic.

Si vous avez déjà un dépôt poussé sur GitHub, vous devez simplement le connecter.

Connectez-vous à votre compte Netlify. Dans le tableau de bord, cliquez sur le bouton `Nouveau site depuis Git`.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/netlify_home.png)

Cliquez sur le bouton `GitHub` pour connecter votre dépôt GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/git_provider.png)

Une nouvelle fenêtre s'ouvrira. Assurez-vous que les pop-ups sont activés dans votre navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/select_repository.png)

Recherchez le dépôt GitHub dans la zone de recherche `Rechercher des dépôts`. Si votre dépôt n'apparaît pas, cliquez sur le bouton `Configurer l'application Netlify sur GitHub` en bas de la page.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/configure_netlify.png)

Une fois cliqué, faites défiler vers le bas de la page et cliquez sur le menu déroulant `Sélectionner des dépôts`, recherchez votre dépôt et cliquez sur le bouton `Enregistrer`.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/select_repo.png)

Vous serez redirigé vers la page précédente affichant tous les dépôts disponibles.

Recherchez le dépôt que vous souhaitez déployer. Pour cet article, j'ai sélectionné le dépôt [react-book-management-app](https://github.com/myogeshchavan97/react-book-management-app) que nous avons créé dans mon [article précédent](https://www.freecodecamp.org/news/react-crud-app-how-to-create-a-book-management-app-from-scratch/).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/find_repository-1.png)

Une fois le dépôt sélectionné, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/deploy_repository.png)

Pour cette application, nous n'avons pas besoin de changer quoi que ce soit.

Votre `Commande de construction` et `Répertoire de publication` seront automatiquement remplis. Assurez-vous de remplir ces champs si vous avez une commande différente dans `package.json` pour construire votre application ou si ces champs ne sont pas remplis automatiquement.

Maintenant, cliquez sur le bouton `Déployer le site`. Une fois cliqué, vous verrez le message `Déploiement du site en cours`.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/deploying.png)

Vous devrez attendre un peu pendant le déploiement. Une fois le déploiement terminé, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/deployed.png)

Ouvrez le lien dans un nouvel onglet et vous verrez votre application déployée en direct.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/deployed_app.gif)

Super ! Maintenant, si vous apportez des modifications au code source et poussez ces modifications vers GitHub, Netlify détectera ces modifications et redéploiera votre application avec vos dernières modifications.

Si vous vérifiez l'application, vous verrez que l'application fonctionne parfaitement avec la navigation et que vous pouvez ajouter/modifier/supprimer un livre.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/working_app.gif)

**Mais il y a un problème.** Si vous accédez directement à la route `/add` ou actualisez la page de la route `/add`, vous obtiendrez une erreur de page non trouvée comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/page_not_found.gif)

Vous obtiendrez la même erreur si vous essayez d'actualiser la route de la page d'édition.

C'est parce que lorsque nous accédons à une route sur notre machine locale, React Router gère le routage. Mais lorsque nous déployons l'application sur un serveur, l'accès direct à la route enverra la demande au serveur lui-même (Netlify dans notre cas).

Mais comme il n'y a pas de gestionnaire de route `/add` côté serveur, vous verrez une erreur de page non trouvée. Mais Netlify offre un moyen de corriger cela.

Créez un nouveau fichier avec le nom `_redirects` à l'intérieur du dossier `public` de notre projet et ajoutez le contenu suivant à l'intérieur :

```js
/* /index.html 200

```

Ici, nous disons à Netlify de rediriger toutes les routes vers le fichier `index.html`.

Le fichier `index.html` contient tout le code de notre application React. Il est généré à l'intérieur du dossier `build` lorsque la commande `yarn build` est exécutée par Netlify lors du déploiement de l'application.

Et comme le routage est géré par notre application React qui est contenue dans le fichier `index.html`, notre application fonctionnera sans erreur de page non trouvée.

Maintenant, poussez les modifications vers le dépôt GitHub afin que Netlify déploie à nouveau l'application avec ces modifications.

Et une fois déployé, si vous vérifiez l'application déployée, vous verrez que l'application fonctionne correctement et que nous n'obtenons pas d'erreur de page non trouvée.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/no_page_not_found.gif)

C'est tout ! Nous avons terminé le déploiement de notre application sur Netlify.

## Comment changer facilement le nom d'un site dans Netlify

Si vous vérifiez le nom du site déployé, vous verrez qu'il n'est pas facile à retenir, surtout si vous avez beaucoup d'applications déployées. Mais Netlify offre un moyen de changer cela facilement.

Cliquez sur le bouton `Paramètres du site` affiché dans la section `Aperçu du site`.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/site_settings.png)

Ensuite, cliquez sur le bouton `Changer le nom du site` et entrez un nouveau nom. Cliquez sur le bouton `Enregistrer`, et maintenant vous pouvez accéder à votre application avec le nom modifié.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/changed_site_name.gif)

> J'aime généralement donner le même nom que le nom du dépôt afin qu'il soit facile de trouver une application particulière si vous avez beaucoup d'applications déployées sur Netlify.

Si vous voulez savoir comment déployer une application React + Node.js en production, consultez [cet article](https://dev.to/myogeshchavan97/how-to-deploy-react-node-js-application-to-heroku-4jb4).

### Merci d'avoir lu !

Vous pouvez trouver le code source complet de GitHub avec cette modification de redirection dans [ce dépôt](https://github.com/myogeshchavan97/netlify-react-book-management-app).

**Vous pouvez voir la démonstration en direct de l'application déployée [ici](https://react-book-management-app.netlify.app/).**

Vous voulez apprendre toutes les fonctionnalités ES6+ en détail, y compris let et const, les promesses, diverses méthodes de promesses, la déstructuration de tableaux et d'objets, les fonctions fléchées, async/await, import et export et bien plus encore à partir de zéro ?

Consultez mon livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/). Ce livre couvre tous les prérequis pour apprendre React et vous aide à devenir meilleur en JavaScript et React.

> Consultez les contenus de prévisualisation gratuits du livre [ici](https://www.freecodecamp.org/news/learn-modern-javascript/).

De plus, vous pouvez consulter mon cours **gratuit** [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour apprendre React Router à partir de zéro.

Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).

<a href="https://bit.ly/3w0DGum" target="_blank" rel="noreferrer noopener"><img src="https://gist.github.com/myogeshchavan97/98ae4f4ead57fde8d47fcf7641220b72/raw/c3e4265df4396d639a7938a83bffd570130483b1/banner.jpg"></a>