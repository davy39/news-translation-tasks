---
title: 'Comment créer votre premier blog Hugo : un guide pratique'
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2020-01-08T08:44:58.000Z'
originalURL: https://freecodecamp.org/news/your-first-hugo-blog-a-practical-guide
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Screen-Shot-2020-01-03-at-20.05.40.png
tags:
- name: blog
  slug: blog
- name: Hugo
  slug: hugo
- name: technical writing
  slug: technical-writing
seo_title: 'Comment créer votre premier blog Hugo : un guide pratique'
seo_desc: 'Hugo is a great tool to use if you want to start a blog.

  I use Hugo myself for my blog, flaviocopes.com, and I''ve been using it for more
  than two years. I have a few reasons for loving Hugo.

  First of all, it is simple, boring, flexible, and fast.

  The...'
---

Hugo est un excellent outil à utiliser si vous souhaitez démarrer un blog.

J'utilise moi-même Hugo pour mon blog, [flaviocopes.com](https://flaviocopes.com/), et je l'utilise depuis plus de deux ans. J'ai quelques raisons d'aimer Hugo.

Tout d'abord, il est **simple**, **ennuyeux**, **flexible** et **rapide**.

La principale raison est qu'il est **simple**. Il n'y a pas grand-chose à apprendre pour commencer.

Vous écrivez du contenu en Markdown, un format qui me permet d'utiliser mon éditeur préféré (Bear) pour écrire des articles.

Hugo est **ennuyeux**. Ne vous méprenez pas, c'est une très bonne chose. En tant que développeur, je suis tenté de modifier des choses ici et là tout le temps. Il n'y a pas de technologie sophistiquée sous-jacente à Hugo. Il est construit en utilisant Go, l'un des langages que j'aime le plus, mais cela ne signifie pas que je veux plonger dans les rouages internes de Hugo et changer son fonctionnement.

Et il ne présente aucune fonctionnalité cool ou de nouvelle génération comme le font de nombreux frameworks JavaScript.

D'où son côté ennuyeux, ce qui me donne beaucoup de temps pour faire ce qui est vraiment utile lorsque je travaille sur un blog : **écrire du contenu**. Je me concentre sur le contenu, pas sur le conteneur de contenu.

Cela dit, Hugo est assez **flexible**. J'ai commencé mon propre blog avec un thème open source, puis je l'ai complètement modifié au fil du temps. Parfois, je veux faire des choses sur mon site web qui vont au-delà du cadre d'un simple blog, et Hugo me permet de créer ces choses.

Enfin, une autre raison pour laquelle j'aime Hugo est qu'il est **rapide**. Pourquoi ? Tout d'abord, il est basé sur Go, qui est connu pour être un langage très rapide. Et dans l'écosystème Go, il n'y a pas de concept de dépendances de 100 mégaoctets. Les choses sont conçues pour être aussi rapides que possible. De plus, Hugo n'a pas besoin de faire certaines des choses sophistiquées qui sont nécessaires lorsque l'on utilise une technologie sophistiquée. C'est un sous-produit du fait d'être ennuyeux.

Bref, assez parlé.

Hugo est incroyable, surtout si vous êtes un développeur et que vous êtes prêt à écrire en Markdown. Les non-techniciens peuvent simplement refuser d'utiliser Markdown, et c'est parfaitement compréhensible.

De plus, vous devez être prêt pour un flux de travail centré sur Git pour que les choses fonctionnent vraiment.

Voici le processus pour écrire un blog :

* écrire un article en utilisant Markdown,
* puis valider vos modifications dans un dépôt Git, le plus souvent sur GitHub,
* et ensuite une technologie de liaison déploie les modifications sur le serveur qui héberge le site.

## Héberger un site web Hugo

Un blog Hugo est complètement **statique**. Cela signifie que vous n'avez pas besoin d'héberger votre propre serveur, ou d'utiliser un service spécial pour cela.

Netlify, Now et GitHub Pages sont trois excellents endroits où vous pouvez héberger un blog Hugo, gratuitement.

Le seul coût est celui que vous devez supporter pour le nom de domaine. Je ne peux pas assez insister sur l'importance d'avoir votre propre nom de domaine. Pas de sites `.github.io` ou `.netlify.com` ou `.now.sh`, s'il vous plaît.

Mes propres sites Hugo sont hébergés sur Netlify.

## Choisir un domaine

Placez votre blog sous votre propre domaine. Choisissez-en un. Utilisez votre propre nom. Et utilisez `.com` ou `.blog`. N'essayez pas d'être malin en utilisant un domaine localisé - par exemple, n'utilisez pas `.io`. `.com` donne simplement une meilleure impression et il est réutilisable pour tous vos projets futurs, pas seulement pour héberger votre blog. J'ai choisi celui-ci.

Oh, et si vous avez un ancien domaine qui traîne, utilisez-le simplement. Pourquoi ? Plus votre domaine est ancien, mieux c'est.

Note sur les sous-domaines : chaque sous-domaine, pour Google, est un site web différent. Donc si votre domaine est `flaviocopes.com`, et que vous créez votre blog dans `blog.flaviocopes.com`, alors c'est un site web complètement nouveau pour Google, et il aura son propre classement séparé du domaine principal.

Ma suggestion est d'éviter complètement les sous-domaines.

## Installer Hugo

Pour installer Hugo sur macOS, depuis votre terminal, exécutez

```bash
brew install hugo

```

_La commande `brew` n'existe pas sur votre Mac ? Consultez le [guide Homebrew](https://flaviocopes.com/homebrew/)._

Pour Windows et Linux, consultez le [guide d'installation officiel](https://gohugo.io/getting-started/installing/).

## Créer un site Hugo

Une fois Hugo installé, vous pouvez créer un site Hugo en exécutant

```bash
hugo new site myblog

```

Je vous suggère d'exécuter cette commande dans un dossier `www` dans votre répertoire personnel, car la commande créera un nouveau dossier `myblog` là où vous l'exécutez.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/hugo-cmd-tool.png)

## Choisir un thème

Maintenant, avant de pouvoir commencer, vous devez choisir un thème. Je souhaite que Hugo inclue un thème par défaut pour simplifier les choses, mais ce n'est pas le cas.

Il y a beaucoup de choix sur [https://themes.gohugo.io](https://themes.gohugo.io/). Ma recommandation personnelle est de commencer avec [https://themes.gohugo.io/ghostwriter/](https://themes.gohugo.io/ghostwriter/) et de le modifier plus tard.

Je recommande également d'éviter le flux de travail `git clone` qu'ils suggèrent sur cette page. Vous allez sûrement modifier le thème à l'avenir, et je trouve qu'il est préférable d'avoir un seul dépôt pour le contenu et le thème. Cela simplifie le déploiement.

Alors, allez sur [https://github.com/jbub/ghostwriter/archive/master.zip](https://github.com/jbub/ghostwriter/archive/master.zip) pour télécharger la version actuelle du thème.

Ensuite, décompressez-le dans le dossier `themes/ghostwriter` de votre nouveau site Hugo :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/ghostwriter-theme.png)

Remarquez qu'il y a un dossier `exampleSite` dans `themes/ghostwriter`. Ouvrez-le, et ouvrez son sous-dossier `content`. Vous y verrez les sous-dossiers `page`, `post` et `project`.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/page-post-and-projects-subfolders.png)

Copiez `page` et `post` dans le dossier `content` du site :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/copy-page-and-post-directories.png)

## La configuration

Les données d'exemple fournissent également un fichier `config.toml` d'exemple dans `themes/ghostwriter/exampleSite/config.toml`. Il s'agit du fichier de configuration de Hugo, qui indique à Hugo certains détails de la configuration sans que vous ayez à coder en dur les informations dans le thème.

Je vous recommande de ne pas copier cela, car il contient trop de choses, et d'utiliser plutôt ceci :

```toml
baseurl = "/"
title = "Mon blog"
theme = "ghostwriter"

[Params]
    mainSections = ["post"]
    intro = true
    headline = "Mon titre"
    description = "Ma description"
    github = "https://github.com/XXX"
    twitter = "https://twitter.com/XXX"
    email = "XXX@example.com"
    opengraph = true
    shareTwitter = true
    dateFormat = "Mon, Jan 2, 2006"

[Permalinks]
    post = "/:filename/"

```

Vous pouvez librement personnaliser les informations dans ce fichier plus tard.

Maintenant, depuis la ligne de commande, exécutez :

```bash
hugo serve

```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/hugo-serve-output.png)

Ouvrez `http://localhost:1313` dans votre navigateur, et vous devriez pouvoir voir le site en direct !

![Image](https://www.freecodecamp.org/news/content/images/2024/04/live-site-localhost.png)

C'est la page d'accueil du site.

Il y a une liste d'articles qui est prise depuis le dossier `content/post` de votre site web :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/content-post-samples.png)

Cliquez sur le premier, appelé « Creating a New Theme » :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/creating-a-new-theme-post.png)

Vous pouvez ouvrir le fichier `content/post/creating-a-new-theme.md` pour changer quoi que ce soit dans l'article.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/updating-markdown-of-post.png)

Si vous enregistrez, le site web se mettra automatiquement à jour avec le nouveau contenu.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/updated-post-live.png)

C'est assez génial, n'est-ce pas ?

Vous pouvez créer un nouvel article en créant un nouveau fichier `.md`, en le préfixant avec ce que vous voulez. Vous pouvez utiliser des nombres incrémentiels, si vous préférez. Ou utiliser une date.

Si quelque chose ne vous plaît pas, vous pouvez ouvrir le dossier `themes/ghostwriter/layouts` et le modifier.

Le modèle « post » est défini dans `themes/ghostwriter/layouts/post/single.html` :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/post-template.png)

Hugo utilise des modèles Go. La syntaxe peut être assez inhabituelle, mais le site web de Hugo fait un très bon travail pour les expliquer dans cette [introduction aux modèles Go](https://gohugo.io/templates/introduction/).

Cependant, essayez de ne pas regarder la personnalisation de votre modèle pour l'instant.

Si vous voulez ajuster les couleurs, ajoutez une balise `<style>` avec un peu de CSS dans le fichier `themes/ghostwriter/layouts/partials/header.html`.

Par exemple, rendez les liens noirs :

```html
<style>
.site-title a, .button-square {
    background: black;
}
a {
    color: black;
}
</style>

```

Concentrez-vous sur le contenu à la place.

Supprimez les fichiers existants, et écrivez 2-3 articles pour commencer.

Il est trop facile de se laisser piéger à faire les choses parfaitement comme vous le souhaitez, mais l'important est le contenu.

Et plus votre site est propre, mieux c'est pour vos lecteurs.

Permettez-moi maintenant d'écrire un peu sur le déploiement.

## Déployer le site Hugo sur Netlify

Je veux montrer comment déployer un site Hugo sur 2 des services que j'apprécie le plus : Netlify et Now.

Tout d'abord, je vais créer un dépôt GitHub pour héberger le site.

J'ouvre GitHub Desktop, une application que j'utilise tous les jours et qui fait partie de mon flux de travail. C'est le moyen le plus simple d'utiliser Git.

Depuis le menu Fichier, j'ai appuyé sur l'option « New Repository » :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/netlify-new-repository.png)

Le même écran peut être généré en faisant simplement glisser le dossier `myblog` dans l'application.

J'ai donné le nom `myblog` au dépôt, et j'ai choisi le bon chemin pour le dépôt.

Le processus fait automatiquement le premier commit :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/netlify-first-commit.png)

Maintenant, nous pouvons cliquer sur le bouton « Publish repository » pour pousser le dépôt vers GitHub :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/publish-repo.png)

Vous pouvez bien sûr garder le dépôt privé.

Une fois le dépôt dans GitHub :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/private-repo-on-github.png)

nous pouvons passer à Netlify.

Depuis mon tableau de bord Netlify, j'ai appuyé sur le bouton « New site from Git » :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/new-site-from-git.png)

J'ai appuyé sur GitHub, autorisé Netlify à accéder à mes dépôts privés, puis j'ai choisi le dépôt que je viens de créer :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/access-to-private-repos.png)

Netlify a automatiquement identifié qu'il s'agissait d'un dépôt Hugo, et a entré la commande de construction automatiquement :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/netlify-enter-build-command.png)

En cliquant sur « Deploy site », le processus de déploiement commence :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/netlify-deploy-site.png)

Sur un vrai site, je configurerais un domaine personnalisé. Netlify propose l'option d'acheter un domaine via eux, et c'est un processus très (TRÈS) simple. Je le recommande vivement. Le site peut être en ligne en quelques minutes après l'achat du domaine.

Un sous-domaine aléatoire `.netlify.com` est attaché au site, dans ce cas `pedantic-engelbart-500c9a.netlify.com`, et HTTPS est automatiquement activé.

Nous pouvons donc voir immédiatement le site en direct :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/preview-netlify-subdomain.png)

Maintenant, si vous essayez de modifier quelque chose dans votre version locale, vous poussez simplement les modifications vers GitHub, et Netlify mettra automatiquement à jour le site. Vous pouvez voir la construction du site dans le panneau « Overview » du site :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/automatic-build.png)

Pour en savoir plus sur Netlify, je vous recommande de consulter mon [tutoriel Netlify](https://flaviocopes.com/netlify/).

## Déployer le site Hugo sur Zeit Now

Une autre plateforme incroyable que vous pouvez utiliser pour votre blog Hugo est Zeit Now.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now.png)

Une fois inscrit, depuis le tableau de bord, vous appuyez sur le bouton **Nouveau Projet**.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-new-project.png)

La première fois que vous déployez depuis GitHub, vous devez d'abord installer l'application GitHub en cliquant sur « Install Now For GitHub » :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-install-now-from-github.png)

Cela vous amène à la page GitHub de l'application, où vous pouvez l'autoriser pour tous vos dépôts, ou seulement pour certains :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-authorize.png)

Une fois de retour, cliquez sur le bouton « New Project From GitHub » :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-new-project-from-github.png)

Sélectionnez le projet et cliquez sur « Import » :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-import.png)

En attendant, allez dans le dossier principal de `mysite` et ajoutez un fichier `package.json` avec ce contenu :

```json
{
  "scripts": {
    "build": "hugo"
  }
}

```

Cela indique à Now comment déployer le site.

Lorsque vous revenez au tableau de bord, le nouveau déploiement devrait commencer bientôt, et vous verrez le site fonctionner en direct :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-deployed.png)

![Image](https://www.freecodecamp.org/news/content/images/2024/04/zeit-now-live-site.png)

Notez que dans Now, vous avez trois URL que vous pouvez utiliser pour accéder au site :

* `myblog.flaviocopes.now.sh`
* `myblog-alpha-swart.now.sh`
* `myblog-git-master.flaviocopes.now.sh`

Vous pouvez choisir celle que vous préférez.

De plus, chaque déploiement a sa propre URL. Dans ce cas, j'avais `myblog-h8xks5jhn.now.sh`, mais cela change avec chaque déploiement.

Et bien sûr, vous pouvez ajouter votre domaine. Zeit propose un excellent service pour acheter votre domaine directement auprès d'eux, disponible à l'adresse [https://zeit.co/domains](https://zeit.co/domains).

Et si vous préférez travailler avec la ligne de commande, la commande `now` vous permet d'acheter des domaines à partir de là également.

Je vous recommande vivement de consulter mon [tutoriel Zeit Now](https://flaviocopes.com/zeit-now/) pour en savoir plus sur cette plateforme.

## Conclusion

J'espère que ce tutoriel peut vous donner un peu de guidance si vous prévoyez de démarrer un nouveau blog. Hugo est ma plateforme préférée, mais elle n'est bien sûr pas unique. Ghost (la plateforme qui alimente freeCodeCamp) est également génial, ainsi que WordPress bien sûr, et Gatsby.

Choisissez votre préféré. À mon avis, la plateforme n'a pas autant d'importance que votre contenu. Alors, choisissez-en une et commencez à écrire !