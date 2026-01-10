---
title: Un premier regard sur GitHub Actions avec Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-14T16:30:37.000Z'
originalURL: https://freecodecamp.org/news/a-first-look-at-github-actions-with-heroku-a6b4239d556
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GsbQnrSIRn8-MkyfFGXJHw.jpeg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: GitHub
  slug: github
- name: Heroku
  slug: heroku
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Un premier regard sur GitHub Actions avec Heroku
seo_desc: 'By Pedro Mendonça

  In October, GitHub announced that their latest big feature — GitHub Actions — was
  going in public beta. At the time I wasn’t quite sure about what it was, but after
  taking a look at their blog post it looked pretty simple to me. Git...'
---

Par Pedro Mendonça

En octobre, GitHub a annoncé que leur dernière grande fonctionnalité — GitHub Actions — passait en [bêta publique](https://github.blog/changelog/2018-10-16-github-actions-limited-beta/). À l'époque, je n'étais pas tout à fait sûr de ce que c'était, mais après avoir jeté un coup d'œil à leur article de blog, cela m'a semblé assez simple. GitHub Actions est une réponse à l'une des fonctionnalités clés de leur principal concurrent : la fonctionnalité [Auto DevOps](https://docs.gitlab.com/ee/topics/autodevops/) de GitLab.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GsbQnrSIRn8-MkyfFGXJHw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/PqRvLsjD_TU?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Saad Salim</a> sur <a href="https://unsplash.com/search/photos/pipeline?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Récemment, j'ai créé mon propre compte GitLab personnel simplement parce que GitLab m'offrait un moyen facile d'automatiser le processus de construction et de déploiement d'une application React single page en utilisant un seul fichier `.gitlab-ci.yml`.

Cependant, lorsque j'ai obtenu l'accès à la bêta de GitHub Actions, j'ai dû l'essayer. J'ai donc décidé de construire quelque chose de similaire.

#### Montrez-moi le code !

Si vous avez une bonne idée de ce que sont les actions et que vous voulez simplement voir le code, n'hésitez pas à explorer le dépôt pour cet article ici : [https://github.com/pedsm/tryGithubActions](https://github.com/pedsm/tryGithubActions)

#### Un petit avertissement

Toute mon expérience avec les actions GitHub jusqu'à présent est basée sur leur version bêta, alors tenez-en compte. Beaucoup des choses dont je parle ici peuvent ne pas être incluses dans leur version finale, et je vais ignorer tous les bugs ou comportements _'bizarres'_ que j'ai trouvés.

### Qu'est-ce que c'est ?

GitHub Actions vous permet d'automatiser des tâches à effectuer lorsqu'un événement se produit dans l'un de vos dépôts (comme des pushes, des issues, des releases et plus encore). Cela signifie que vous pouvez configurer votre dépôt pour qu'il soit automatiquement testé et déployé chaque fois que vous poussez un nouveau commit, et c'est exactement ce que j'ai fait.

Comme je l'ai mentionné précédemment, la seule raison pour laquelle j'ai décidé de créer un compte GitLab est d'avoir un workflow où tout push vers master serait déployé directement sur un site web en direct, alors j'ai décidé de recréer exactement cela.

### L'installation

Une fois que vous avez accès à GitHub Actions, vous verrez un nouvel onglet nommé `Actions` dans tous vos dépôts. Là, vous pourrez créer votre premier workflow. Un workflow est un fichier `.workflow` qui réside dans le dossier `.github`, déjà utilisé pour d'autres choses comme les templates de PR et d'autres configurations spécifiques au dépôt.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zUZtwIE2WjvlpS4DqcLxBw.png)
_L'onglet 'Actions'_

GitHub Actions est livré avec un éditeur graphique complet pour vos workflows. C'est un bol d'air frais si vous pensiez devoir apprendre un nouveau schéma YAML ou un langage spécifique à une technologie comme un `Jenkinsfile`. Cependant, si vous ne souhaitez pas utiliser les outils graphiques, vous pouvez éditer vos fichiers .workflow comme vous le souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gk2BNOWyKfD-50-1CrgTHw.png)
_Le visualisateur graphique .workflow._

Les fichiers de workflow utilisent le langage de configuration HashiCorp (également connu sous le nom de HCL). Si vous êtes familier avec Terraform, cela devrait vous sembler familier.

### Les différences

Si vous avez implémenté un type de test automatisé, tout cela peut vous sembler très similaire. Peut-être à part le fait que vous avez accès à un éditeur graphique. Cependant, il y a moins de similitudes au fur et à mesure que nous avançons.

GitHub Actions, comme son nom l'indique, est une série d'`actions` qui sont des exécutions de commandes uniques — ce qui est très inhabituel. Si vous avez prêté attention au fichier _workflow_, vous avez peut-être remarqué que la définition des actions a un paramètre `uses`. Si vous utilisez une action `npm`, vous pouvez alors effectuer une seule tâche NPM telle que `npm install` puis utiliser une autre action pour faire le `npm test`. Cela est inhabituel car certaines tâches logiques comme 'installer les dépendances' peuvent nécessiter plus d'une commande et sont généralement regroupées dans des '_Stages_' dans d'autres solutions d'intégration continue.

Lorsque vous utilisez l'éditeur graphique et ajoutez une nouvelle action, vous êtes d'abord invité avec une liste des actions disponibles ([que vous pouvez trouver ici si vous êtes curieux](https://github.com/actions)). Ensuite, un simple formulaire apparaît où vous pouvez uniquement remplir le libellé, un champ '_args_' et un champ '_runs_'.

Le libellé, comme vous vous en doutez, est simplement un nom convivial pour ce que fait votre action, comme '_Testing_'. L'action effectue ensuite un '_runs args_' dans le terminal, où 'runs' ne vaut généralement pas la peine d'être remplacé. Cela signifie que pour exécuter un `npm install` dans l'action npm, vous laisseriez 'runs' par défaut et 'args' comme `install`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*N6uwl7UCYhFb-xmcU5RBUg.png)
_La fenêtre de configuration de l'action pour l'éditeur GUI._

Pour l'instant, cela me semble être une grande déception, car GitHub semble verrouiller la fonctionnalité de cette fonction pour ne faire que ce qu'elle veut faire. Npm est disponible pour le moment, mais si vous utilisez pip pour votre projet python, vous devrez implémenter votre propre action ou trouver une alternative open-source. Il est déjà possible de créer vos propres [actions personnalisées](https://developer.github.com/actions/creating-github-actions/creating-a-new-action/), mais comme cela est en bêta, il est très peu probable que vous trouviez beaucoup de choses pour le moment. Du côté positif, ils avaient les deux choses dont j'avais besoin, NPM et Heroku.

### Le projet

L'idée du projet était très simple : je voulais construire une application Vue (car c'est ce que j'apprends actuellement) et la déployer automatiquement sur un service d'hébergement.

Ensuite, je voulais faire en sorte que le contenu du site web reflète un fichier `json` avec une série de noms d'utilisateurs GitHub. De cette façon, n'importe qui pourrait soumettre une PR avec son identifiant GitHub pour que je puisse cliquer sur un bouton et tout déployer magiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J55Yixev7q9A4LPcY_jyDg.png)
_Vous pouvez le consulter ici [https://try-github-action.herokuapp.com/](https://try-github-action.herokuapp.com/" rel="noopener" target="_blank" title=")_

Je vais sauter tout le contenu Vue.js et passer directement aux Actions. Après avoir construit l'application simple, je n'avais plus qu'à faire ce qui suit en utilisant les actions :

1. Installer les dépendances
2. Exécuter les linters (Important pour s'assurer que l'entrée JSON n'est pas corrompue)
3. Construire le code prêt pour la production
4. Déployer quelque part (J'ai choisi Heroku car cela semblait le plus facile pour ne pas avoir à penser aux serveurs et les actions sont disponibles)

Les trois premières étapes ont été l'expérience la plus intuitive que j'ai jamais eue avec l'automatisation de quoi que ce soit. Cela m'a presque donné des vibrations IFTTT. Vous cliquez simplement sur l'action NPM puis choisissez ce que vous voulez que NPM fasse. Je sais que j'ai dit que cela semblait un peu restrictif de n'avoir qu'une série d'actions, mais la réalité est que je n'ai jamais eu à me soucier de la distribution Linux que j'utilisais, si NPM était bundlé avec l'installation de Node.js, et surtout si la syntaxe HCL était correcte. Quelques clics sur l'interface utilisateur et c'est fait. Le processus entier a pris 4 actions, donc moins de 5 minutes.

Ensuite, je suis passé à la partie déploiement. Je savais que cela allait être plus difficile, car bien que je sache comment Heroku fonctionnait, je ne l'avais jamais utilisé auparavant. Cependant, le dépôt [actions/heroku](https://github.com/actions/heroku#github-deployer-for-heroku) avait des instructions claires pour que je puisse faire exactement ce que je voulais faire. En fin de compte, ce n'était qu'une question de quelques clics supplémentaires et c'était fait.

### Secrets

Je pense que c'est le moment parfait pour parler de ce qui est peut-être ma fonctionnalité préférée dans GitHub Actions, à savoir _Secrets_. Comme vous vous en doutez, Heroku nécessite une clé API pour permettre à quelqu'un de déployer l'application. Sinon, n'importe qui lisant cet article pourrait remplacer mon application par ce qu'il veut. Habituellement, cela est pénible à gérer sur les projets open-source car vous ne pouvez pas vraiment le garder dans le dépôt. [AWS a même un service entier dédié à ce genre de chose](https://aws.amazon.com/secrets-manager/). Cependant, GitHub a implémenté une solution élégante à ce problème.

Les Secrets sont des valeurs que vous pouvez stocker au niveau du dépôt, qui sont automatiquement chiffrées puis transmises en tant que variables d'environnement aux actions que vous définissez comme ayant accès.

Si vous avez jeté un coup d'œil au dépôt des actions Heroku, vous verrez qu'ils listent `HEROKU_API_KEY` comme un secret requis. Le processus pour configurer cela dans l'éditeur est aussi simple que de cliquer sur _*nouveau secret*_, et de lui donner un nom et une valeur. À partir de là, vous pouvez simplement cocher la case pour toutes les actions auxquelles vous souhaitez donner accès à cette information.

Comme il s'agit de variables d'environnement, elles n'ont pas besoin d'être verrouillées aux actions. Par exemple, votre framework de test pourrait recevoir des identifiants pour une base de données en direct afin de garder une trace des résultats des tests, vous pourriez donc transmettre ce secret à l'action `npm test`.

#### Env

Env est une autre option dans l'éditeur graphique qui fait essentiellement la même chose que Secrets mais saute toutes les étapes lorsque vous chiffrez vos données. Ce n'est pas vraiment un gros problème, car les informations non sensibles peuvent simplement être stockées dans un fichier `.env` dans le dépôt lui-même.

### Mes réflexions sur les Actions

GitHub Actions ne fait rien de nouveau. Il existe des dizaines, voire des centaines de solutions commerciales, gratuites et personnalisées pour faire ce que font les Actions. GitHub a même une catégorie entière de [marketplace](https://github.com/marketplace/category/continuous-integration) pour automatiser les tâches dans vos dépôts.

Cependant, je n'ai personnellement jamais eu une aussi bonne expérience utilisateur lors de la configuration d'un pipeline CI/CD. GitHub Actions ne réinvente pas la roue, il la rend simplement moins chère.

En tant que développeurs, nous devons souvent trouver un équilibre entre la facilité d'utilisation et le nombre de fonctionnalités que nous voulons intégrer dans quelque chose. Le problème éternel du '_git cli vs. git gui_'. Cependant, GitHub est bien conscient de ce que le marché a à offrir et ils ne cherchent pas à aller contre les grands noms. Non, vous ne vous débarrasserez pas de Jenkins, Circle ou de ce que votre entreprise utilise actuellement. Mais si vous avez un petit projet personnel, cela vaut définitivement le coup d'œil.

**Contribuer**

Tout le code de cet article est open source et disponible à l'adresse [https://github.com/pedsm/tryGithubActions](https://github.com/pedsm/tryGithubActions). Si vous souhaitez signaler un problème et ajouter votre identifiant GitHub au projet, n'hésitez pas à soumettre une PR.