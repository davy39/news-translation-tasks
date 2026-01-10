---
title: Comment créer un site statique gratuit avec GitHub Pages en 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-15T21:45:00.000Z'
originalURL: https://freecodecamp.org/news/create-a-free-static-site-with-github-pages-in-10-minutes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f4a740569d1a4ca41d4.jpg
tags:
- name: github pages
  slug: github-pages
- name: jekyll
  slug: jekyll
seo_title: Comment créer un site statique gratuit avec GitHub Pages en 10 minutes
seo_desc: "By Travis Fantina\nStatic sites have become all the rage, and with good\
  \ reason – they are blazingly fast and, with an ever growing number of supported\
  \ hosting services, pretty easy to set up. \nI'm not going to go into all the who,\
  \ what, when, where or..."
---

Par Travis Fantina

Les sites statiques sont devenus très populaires, et pour de bonnes raisons – ils sont extrêmement rapides et, avec un nombre toujours croissant de services d'hébergement pris en charge, assez faciles à configurer. 

Je ne vais pas entrer dans tous les détails sur les sites statiques ici. Je suppose que vous avez au moins une vague idée de ce qu'ils sont _ou_ que vous voulez simplement créer votre propre site et ne vous souciez pas des autres détails. Dans les deux cas, cet article est pour vous.

Tout d'abord, je veux que vous sachiez que j'écris cela pour un public aussi large que possible ; vous n'avez besoin d'aucune connaissance en programmation pour suivre, mais une certaine familiarité avec la ligne de commande et Git sera très utile.

## Comment créer un site statique avec GitHub en 10 minutes ?

Nous allons travailler avec deux outils spécifiques : GitHub Pages, qui est spécialement conçu pour servir du contenu statique, et un générateur de contenu statique appelé Jekyll.

Jekyll est un gem Ruby pour créer des sites statiques facilement, vous devrez donc avoir Ruby installé sur votre ordinateur si vous voulez utiliser Jekyll. Si vous avez OSX, vous avez probablement déjà une version de Ruby (bien que vous deviez peut-être la mettre à jour). Si ce n'est pas le cas, ou si vous êtes sur un ordinateur Windows, vous pouvez en apprendre plus sur son installation ici : [Installing Ruby](https://www.ruby-lang.org/en/documentation/installation/).

Cela étant dit, ouvrez une nouvelle fenêtre de terminal et tapez `gem install bundler jekyll`. Cela installera Bundler (un outil de gestion de paquets Ruby) et Jekyll. 

Une fois ces gems (paquets Ruby) installés, tapez `Jekyll new my-static-site` (nommez-le comme vous voulez) ce qui exécutera le générateur de Jekyll pour créer votre projet dans un nouveau répertoire. Après la création de votre site, accédez à votre nouveau répertoire de site en tapant `cd my-static-site` (ou `cd` suivi du nom que vous avez donné à votre projet).

Ouvrez votre projet dans un éditeur de texte et vous verrez plusieurs fichiers et dossiers créés par Jekyll. Pour l'instant, vous n'avez besoin de vous soucier que du Gemfile (pas du Gemfile.lock). Le Gemfile est un fichier Ruby qui gère tous les paquets Ruby associés nécessaires à l'exécution d'un projet.

Le fichier contiendra une ligne avec la version de Jekyll, commentez-la :

```ruby
#gem "jekyll", "~> 4.0.0"

```

Puis ajoutez cette ligne :

```ruby
gem "github-pages", group: :jekyll_plugins

```

Il peut y avoir beaucoup de pièges lors de l'installation du gem GitHub Pages – parfois les gems dont il dépend sont obsolètes ou les gems que vous avez installés localement sont _trop_ modernes pour GitHub Pages. 

J'ai constaté que cela peut rendre difficile la construction et le test de mon site Jekyll localement. Il peut être plus facile de tester votre site localement et de ne le construire que lorsque vous êtes prêt à le déployer. Cependant, au moment de la rédaction de cet article, vous pouvez spécifier ces versions de dépendances dans votre Gemfile et Jekyll fonctionnera à la fois localement et avec GitHub Pages :

```ruby
gem "jekyll", "~> 3.8.5"
gem "github-pages","~> 202" , group: :jekyll_plugins
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.11.0"
end

```

Merci à [Alex Waibel](https://stackoverflow.com/users/6885157/alex-waibel) sur [StackOverflow](https://stackoverflow.com/questions/58598084/how-does-one-downgrade-jekyll-to-work-with-github-pages) pour cette configuration la plus récente.

Pour voir votre site en action, exécutez `bundle exec Jekyll serve` dans votre ligne de commande. Cela démarrera un serveur et vous pourrez voir votre site en tapant "localhost:4000" dans la barre d'URL d'un navigateur.

Et voilà ! Vous avez créé un site statique avec Jekyll et vous êtes dans le répertoire du projet. Vous avez terminé environ 50 %.

## Mettons cela en ligne


Allez sur GitHub.com et inscrivez-vous, ou si vous avez déjà un compte, sélectionnez le bouton "nouveau" et créez un dépôt. Il est important que vous nommiez votre dépôt d'après le lien que votre compte GitHub Pages servira, qui est votre_nom_dutilisateur.github.io. Par exemple, mon nom d'utilisateur GitHub est tfantina et mon blog est [tfantina.github.io](https://tfantina.github.io), donc mon dépôt GitHub est nommé : "tfantina.github.io".

De retour dans votre fenêtre de terminal, poussez votre site Jekyll de votre ordinateur vers GitHub en exécutant les commandes suivantes :

```shell
git init
git remote add origin git@github.com:<votre_nom_dutilisateur_github>/<nom_de_votre_depot_github>.git
git commit -am "Configuration de Jekyll !"
git push -u origin master

```

(En substituant votre nom d'utilisateur et le nom de votre projet, vous n'avez pas besoin des chevrons < et >).

Une fois vos modifications poussées vers votre dépôt, vous devriez avoir un site statique fonctionnel. Cela est dû au fait que vous utilisez le gem GitHub Pages et que vous avez nommé votre dépôt de manière à ce que GitHub comprenne que vous souhaitez le servir avec GitHub Pages. 

Vous pouvez confirmer cela soit en visitant votre site, soit en allant dans l'onglet des paramètres sur GitHub et en faisant défiler jusqu'à la section des pages. Vous devriez voir une boîte verte indiquant où votre site a été publié :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/DFAC66CE-C182-4ECA-9379-87843C730645.png)

Vous remarquerez également que vous pouvez facilement changer votre thème à partir d'ici. GitHub fournit quelques thèmes par défaut pour Jekyll, mais bien sûr vous pouvez aussi créer le vôtre.  
Si votre site indique qu'il est publié mais semble vide, vous devrez peut-être effectuer un rafraîchissement forcé ou essayer de regarder votre site dans une fenêtre privée. Cela peut sembler évident, mais cela m'arrive presque à chaque fois que je configure une nouvelle instance Jekyll.

Si tout s'est passé comme prévu, votre site devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/65F58F30-3000-44E5-96CF-DCC1CFEDF953.png)

---

Voilà – en quelques minutes seulement, vous avez créé et déployé un site web statique avec GitHub Pages. Mais vous voulez probablement pouvoir mettre du contenu sur votre page. 

J'ai promis que cela ne prendrait que dix minutes, donc je ne vais pas entrer dans tous les détails des pages, de la matière frontale, ou du langage de modélisation Liquid. C'est un sujet pour un autre jour. Mais je vais partager comment créer votre premier article.

De retour dans votre éditeur de texte, ouvrez le dossier "_posts". Il y a déjà un article vous souhaitant la bienvenue sur votre nouveau blog. Créez un nouveau fichier markdown et enregistrez-le avec un nom dans ce format : ANNEE-MOIS-JOUR-TITRE.markdown (voir ci-dessous) :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/B90755E4-B12A-4038-8DD7-AF945E73FE43.png)

Un article Jekyll contient deux sections : la matière frontale et le corps.

La matière frontale donne des instructions spécifiques à Jekyll telles que le titre de l'article, le modèle à utiliser et la date de rédaction de l'article. 

La matière frontale est hautement personnalisable. Par exemple, je voulais que mes articles aient des images héroïques, j'ai donc créé une balise `lead_image` et placé une syntaxe dans mon modèle pour vérifier spécifiquement la présence d'images principales dans la matière frontale de chaque article. Le langage de modélisation Liquid facilite l'extraction de contenu de la matière frontale dans votre thème.

Il y a beaucoup plus de choses que vous pouvez faire avec la matière frontale, mais commençons par un exemple générique.

La matière frontale par défaut ressemble à ceci :

```markdown
---
layout: post 
title:  "Bienvenue sur Jekyll !"
date:   2019-11-09 18:07:11 -0600
categories: jekyll update
---

```

* Layout indique à Jekyll quel modèle vous souhaitez utiliser pour afficher le contenu. Vous pouvez avoir plusieurs modèles pour différentes pages ou types d'articles.
* Le titre de l'article
* La date de l'article
* Les catégories, qui sont essentiellement des étiquettes. Vous pouvez en ajouter autant ou aussi peu que vous le souhaitez, séparées par des espaces.

Après la matière frontale, votre article peut être écrit en [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), ce qui vous donne beaucoup de flexibilité dans la rédaction du contenu de votre article.

Une fois votre article terminé, enregistrez-le et ouvrez votre fenêtre de terminal.

```shell
git commit -am "Publication du premier article"
git push
```

Après une minute (et peut-être un rafraîchissement), vous pourrez voir votre article.

Espérons que vous avez maintenant un site statique fonctionnel sur GitHub Pages créé avec Jekyll ! Si vous avez des problèmes ou des questions, n'hésitez pas à tweeter [@tfantina](https://twitter.com/tfantina), ou vous pouvez m'envoyer un email à [contact@travisfantina.com](mailto:contact@travisfantina.com).