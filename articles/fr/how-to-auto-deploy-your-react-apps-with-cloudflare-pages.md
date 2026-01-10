---
title: Comment déployer automatiquement vos applications React avec Cloudflare Pages
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-21T18:26:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-auto-deploy-your-react-apps-with-cloudflare-pages
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/autodeploy-your-react-apps.png
tags:
- name: cloudflare
  slug: cloudflare
- name: GitHub
  slug: github
- name: React
  slug: react
seo_title: Comment déployer automatiquement vos applications React avec Cloudflare
  Pages
seo_desc: "In this article, I'm going to show you how to very quickly deploy any React\
  \ application with the help of Cloudflare pages. \nYou'll see how to not only build\
  \ and deploy your app within minutes using just a few tools, but also how to auto-deploy\
  \ any fu..."
---

Dans cet article, je vais vous montrer comment déployer très rapidement n'importe quelle application React à l'aide de Cloudflare Pages. 

Vous verrez comment non seulement construire et déployer votre application en quelques minutes en utilisant seulement quelques outils, mais aussi comment déployer automatiquement toute modification future que vous faites via votre compte GitHub. 

## Comment commencer

Pour commencer, vous aurez besoin des outils suivants : 

1. Le gestionnaire de paquets npm et le logiciel de contrôle de version Git
2. Votre propre compte GitHub (gratuit) et compte Cloudflare

## Créer notre projet React

Pour déployer une application React, nous devons d'abord en créer une. 

Créons une application React sur notre ordinateur à l'aide de Create React App. Nous pouvons le faire en lui donnant le nom "cloudflare-react" :

```bash
npx create-react-app cloudflare-react
```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cloudflare-react-1.gif)

## Créer notre dépôt GitHub

Une fois notre projet créé avec succès, créons un dépôt GitHub pour celui-ci. 

Nous utilisons GitHub pour pouvoir garder une trace en ligne et facile à gérer de nos projets individuels. GitHub permet également à d'autres utilisateurs d'apporter des améliorations à notre code via des pull requests. 

Cloudflare utilise GitHub pour suivre tout notre code et chaque fois que nous apportons des modifications. 

Pour suivre notre nouvelle application React, nous créons un nouveau dépôt GitHub en allant sur [github.com/new](https://github.com/new). 

Ensuite, nous pouvons simplement ajouter tous nos fichiers et les commiter avec un message indiquant ce que nous faisons :

```bash
git add .
git commit -m "Déployer sur Cloudflare Pages"
```

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cloudflare-react-2.gif)

Ensuite, nous devons ajouter le remote Git approprié, utilisé pour pousser notre code commité en amont vers notre nouveau dépôt GitHub. 

GitHub vous indiquera la commande à inclure pour votre nouveau dépôt. Cela devrait ressembler à ceci :

```bash
git remote add origin someurl
```

Et enfin, nous pouvons simplement exécuter `git push -u origin master`. 

Après avoir actualisé la page de notre dépôt GitHub, nous devrions voir tout notre code de projet React, poussé vers GitHub. 

C'est la première exigence principale pour déployer une application sur Cloudflare Pages : avoir une application React hébergée sur GitHub. 

## Créer un compte Cloudflare

Ensuite, nous allons sur Cloudflare pour déployer notre projet React. 

Si vous n'avez pas encore de compte Cloudflare gratuit, vous pouvez aller sur [pages.cloudflare.com](https://pages.cloudflare.com/) et cliquer sur "S'inscrire" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cloudflare-react-8.png)

Une des principales raisons pour lesquelles vous et la plupart des autres développeurs seriez intéressés par l'utilisation de Cloudflare Pages, est que Cloudflare dispose d'un CDN mondial. Cela permet une livraison plus rapide de notre application déployée. 

Cloudflare dispose également de ressources telles que la gestion DNS, ce qui est particulièrement utile si vous souhaitez que votre application ait son propre domaine personnalisé. 

## Lier GitHub à Cloudflare Pages

La première fois que vous visitez Cloudflare Pages, vous serez invité à créer un projet à partir de votre dépôt GitHub, vous sélectionnerez donc le bouton Connecter le compte GitHub :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cloudflare-react-5.png)

Ensuite, vous serez invité à installer et autoriser Cloudflare Pages. 

Cette étape nous permet de choisir à quoi Cloudflare a accès : si nous voulons lui donner accès à tous nos dépôts ou seulement à des dépôts sélectionnés : 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cloudflare-react-6.png)

Si vous souhaitez déployer plusieurs projets à l'avenir, je vous recommande de sélectionner tous les dépôts. 

En conséquence, Cloudflare aura la capacité d'accéder à tout code et déploiement que nous avons effectués afin qu'ils puissent être déployés sur le web. 

## Déployer notre projet React sur Cloudflare Pages

Une fois que nous avons donné à Cloudflare l'autorisation de le faire, nous verrons un écran où nous pouvons choisir quel projet de notre dépôt GitHub nous voulons déployer : 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cloudflare-react-7.png)

Dans notre cas, nous choisirons notre dépôt "cloudflare-react", après quoi nous cliquerons sur Begin setup. 

À partir de là, nous pouvons choisir le nom de projet que nous voulons donner à notre application React avec Cloudflare. Ce nom de projet est important car il détermine le sous-domaine auquel il sera déployé. 

Puisque nous avons choisi "cloudflare-react", il sera déployé sur cloudflare-react.pages.dev : 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cloudflare-react-3.gif)

Nous pouvons choisir quelle branche déployer, ainsi que les paramètres de construction. 

Notez que tout ce que nous devons vraiment faire est de choisir quel préréglage de framework nous utilisons. Cloudflare a une option préréglée pour notre framework : Create React App. 

Lorsque nous le choisissons, il inclura les paramètres par défaut pour tout projet Create React App : déployer le projet en exécutant la commande de construction "npm run build" et le répertoire de sortie (le dossier dans lequel notre code React sera construit lors de l'exécution de cette commande de construction) est nommé "build". 

Il existe d'autres préréglages utiles pour toute application React créée avec un framework comme Next.js ou Gatsby. Vous pouvez utiliser Cloudflare Pages pour déployer presque tout type d'application React auquel vous pouvez penser. 

Enfin, nous pouvons cliquer sur le bouton de déploiement. Le processus de déploiement prendra environ quatre à cinq minutes la première fois. Soyez patient, mais sachez que tout déploiement ultérieur prendra beaucoup moins de temps. 

Nous voyons quelques logs utiles sur la construction de notre projet et la progression de notre déploiement. Si une erreur survenait lors de ce processus, nous la verrions dans les logs et obtiendrions une indication sur ce que nous devons corriger. 

Pour voir notre projet déployé, nous pouvons cliquer sur le bouton Continue to Project, puis sur "Visiter le site" et nous pouvons voir notre application fonctionner sur l'URL : votre-nom-de-projet.pages.dev. 

## Apporter des modifications avec des déploiements automatiques

Bien qu'il ait été très facile de déployer instantanément notre application React sur le web après l'avoir poussée sur GitHub, l'étape suivante consiste à apporter des modifications à notre application et à la redéployer. 

Comme vous le verrez, cette fonctionnalité de déploiement automatique (intégration continue) a déjà été configurée. 

Dans le cas de mon application, j'ai décidé d'installer React Router DOM pour ajouter une page à propos. Sur la page d'accueil, j'ai également ajouté un lien vers la page à propos : 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cloudflare-react-4.gif)

Après avoir terminé cette modification que vous pouvez voir dans la vidéo ci-dessus, je suis passé par le même processus d'exécution de `git add .`, `git commit` avec un message sur les modifications que j'ai apportées, puis `git push`. 

Après avoir fait cela, si nous retournons à notre tableau de bord Cloudflare Pages, nous pouvons voir que Cloudflare a immédiatement détecté ce nouveau déploiement car il est lié à notre compte GitHub et peut voir tous les déploiements ou pull requests effectués sur notre dépôt. 

En conséquence, il redéploie instantanément notre application avec les modifications que nous avons apportées. Pendant que notre déploiement est en cours, nous pouvons cliquer sur "Voir la construction" et voir des informations spécifiques sur ce déploiement, ainsi que les logs. 

Comme vous le verrez, toute modification apportée après le déploiement initial prend beaucoup moins de temps (il ne faut qu'environ une minute au total pour que le déploiement se termine avec succès). Vous verrez également qu'il est donné un hash de déploiement unique au début de notre URL. Cela nous permet de référencer de manière unique chaque déploiement. 

Si nous supprimons le hash, nous voyons que les modifications que nous avons apportées sont également déployées sur notre nom de projet choisi : cloudflare-react.pages.dev. 

## Conclusion

J'espère que ce tutoriel vous montre à quel point il est facile de commencer avec les nouvelles Cloudflare Pages. Vous pouvez commencer à déployer vos applications React dès aujourd'hui pour profiter de leur CDN mondial et de toutes les fonctionnalités supplémentaires que Cloudflare a à offrir. 

Cloudflare Pages est encore assez nouveau, mais il offre déjà de nombreux outils qui valent la peine d'être explorés. Je le recommande vivement comme service de déploiement pour la prochaine application React que vous souhaitez partager avec le monde. 

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même. 

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*