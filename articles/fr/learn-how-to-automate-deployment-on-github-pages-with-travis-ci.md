---
title: Comment automatiser le déploiement sur GitHub Pages avec Travis CI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-21T16:18:58.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-automate-deployment-on-github-pages-with-travis-ci
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Druhv-article-image.png
tags:
- name: automation
  slug: automation
- name: continuous deployment
  slug: continuous-deployment
- name: Devops
  slug: devops
- name: React
  slug: react
- name: Travis CI
  slug: travis-ci
seo_title: Comment automatiser le déploiement sur GitHub Pages avec Travis CI
seo_desc: 'By Dhruv Barochiya


  Disclaimer: This story is not sponsored by any of the tools that has been described
  into the article (Travis-CI, Github, Github-Pages)


  You have created a project in React.js and deployed it on the GitHub-pages (not
  yet ?? — creat...'
---

Par Dhruv Barochiya

> Avertissement : Cet article n'est pas sponsorisé par l'un des outils décrits dans l'article (Travis-CI, Github, Github-Pages)

Vous avez créé un projet en React.js et l'avez déployé sur GitHub Pages (pas encore ?? — [créez votre premier projet en React.js](https://medium.com/free-code-camp/portfolio-app-using-react-618814e35843)). Mais que faire si vous apportez des modifications fréquentes au code et souhaitez également garder la version déployée à jour avec la dernière version ? Vous vous retrouverez dans le processus fastidieux d'exécuter les scripts de déploiement encore et encore !!!

> Et si le processus de déploiement pouvait être automatisé ??

Après une rapide session de recherche sur Google, j'ai découvert que c'était possible et réalisable avec Travis CI — un outil open source qui peut être utilisé pour automatiser le déploiement de divers types de projets.

## Ce que vous allez apprendre >

Dans cet article, vous apprendrez à mettre en place un système qui déclenchera les scripts de déploiement React en utilisant Travis CI pour déployer le projet sur GitHub Pages dès qu'il y a des modifications dans la branche master du dépôt de code.

* Configuration du déploiement automatisé du projet **[« react-portfolio »](https://medium.com/free-code-camp/portfolio-app-using-react-618814e35843)**
* Découvrir certaines erreurs fréquentes rencontrées lors du processus
* Apprendre quelques concepts liés au « déploiement continu »

## Apprenons quelques bases

> Passez cette section si vous savez que vous n'êtes pas ce type de personne !!

### Intégration Continue (CI) et Livraison Continue (CD) >

> « En [ingénierie logicielle](https://en.wikipedia.org/wiki/Software_engineering), l'intégration continue (CI) est la pratique consistant à fusionner toutes les copies de travail des développeurs vers une ligne principale [partagée](https://en.wikipedia.org/wiki/Trunk_%28software%29) plusieurs fois par jour » — [wikipedia](https://en.wikipedia.org/wiki/Continuous_integration)

En d'autres termes, les développeurs essaieront de fusionner leur code de fonctionnalité dans la branche master aussi fréquemment que possible. Suivre cette pratique permet aux développeurs et aux chefs de produit de publier le produit plus fréquemment.

Il existe des versions étendues des pipelines CI dans lesquelles ces modifications sont également testées automatiquement, ce qui rend le code déployable à tout moment, c'est ce qu'on appelle la « Livraison Continue ». Une extension supplémentaire de ce pipeline est appelée pipeline de « Déploiement Continu », où ces modifications de code testées sont poussées automatiquement vers les serveurs de production. (Nous mettrons en place le pipeline de déploiement continu dans notre cas)

### Travis CI >

**Travis CI** est un service d'intégration continue hébergé utilisé pour construire et tester des projets logiciels hébergés sur GitHub. Les projets open source peuvent être testés sans aucun frais !!

Travis CI peut être configuré en ajoutant un fichier `.travis.yml` au dépôt. Lorsque Travis CI a été activé pour un dépôt donné, GitHub notifiera chaque fois que de nouveaux commits sont poussés vers le dépôt ou qu'une pull request est soumise, puis, selon les règles définies dans le fichier `.travis.yml`, Travis CI exécutera les étapes qui peuvent être n'importe quoi — de l'exécution de tests, de la construction de l'application ou des scripts de déploiement. Travis CI offre une large gamme d'options pour construire le logiciel et, bien sûr, notre bien-aimé `javascript` en fait partie.

> **NOTE_** : _GitHub propose un_ [_pack développeur étudiant_](https://education.github.com/pack) _avec un ensemble de fonctionnalités premium de différentes plateformes (Travis CI en fait partie) gratuitement pour les étudiants qui souhaitent apprendre de nouvelles choses — obtenez votre pack étudiant maintenant !!_

### DevOps >

**DevOps** est un ensemble de pratiques de développement logiciel qui combine le [développement logiciel](https://en.wikipedia.org/wiki/Software_development) (_Dev_) et les [opérations technologiques de l'information](https://en.wikipedia.org/wiki/Information_technology_operations) (_Ops_) pour raccourcir le [cycle de vie du développement des systèmes](https://en.wikipedia.org/wiki/Systems_development_life_cycle) tout en [livrant des fonctionnalités, des corrections et des mises à jour](https://en.wikipedia.org/wiki/Continuous_delivery) fréquemment. Le concept de DevOps est fondé sur la construction d'une culture de collaboration entre les équipes.

> « DevOps est plus qu'une pratique — c'est une question de culture »

L'intégration continue, la livraison continue et le déploiement continu sont quelques-unes des pratiques clés du DevOps. En dehors de celles-ci, les ingénieurs DevOps utilisent largement la puissance de l'infrastructure cloud pour rendre le processus de déploiement transparent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9pVLG4BzEWIcMnfhFp9ULQ.png)

---

## Assez parlé !!! Passons à l'action

Comme vous avez déjà déployé sur GitHub Pages en utilisant le module node `gh-pages`, il y aura une branche appelée `gh-pages` sur le dépôt qui contient les fichiers déployés sur les serveurs GitHub Pages. Après l'intégration de Travis CI, nous pourrons mettre en place le système où toute modification apportée par l'utilisateur sur la branche `master` déclenchera automatiquement une construction. Si la construction est réussie, les scripts de construction seront déclenchés et mettront à jour la branche `gh-pages`. L'utilisateur sera informé de l'état de la construction via des notifications par e-mail de Travis CI.

![Image](https://cdn-media-1.freecodecamp.org/images/1*athThq_0-5cg1foDqt0v5w.png)

### Créer un compte sur Travis-CI >

* Allez sur [Travis-ci.com](https://travis-ci.com/) et [_inscrivez-vous avec GitHub_](https://travis-ci.com/signin).
* Acceptez les termes et conditions de Travis CI. Vous serez redirigé vers GitHub.
* Cliquez sur le bouton _Activer_, et sélectionnez les dépôts que vous souhaitez utiliser avec Travis CI.
* Ajoutez un jeton d'autorisation (cela sera fait automatiquement lorsque vous vous connectez avec GitHub)

### Ajouter le fichier travis.yml au dépôt >

Ce fichier contient les instructions qui indiquent à Travis-CI — quoi ?.. comment ?.. quand ?

> **NOTE** : Lorsque vous déclenchez un travail dans Travis-CI, il démarrera une machine virtuelle avec l'environnement de déploiement approprié configuré dans le fichier `_.travis.yml_`

Décomposons le code —

```yml
language: node_js
node_js:
  - "stable"
cache:
  directories:
  - node_modules
script:
  - npm run build
deploy:
  provider: pages
  skip_cleanup: true
  github_token: $github_token
  local_dir: build
  on:
    branch: master
```

`on` : Travis-CI déclenchera automatiquement un travail chaque fois qu'il y a des modifications sur la branche spécifiée dans ce champ.

`deploy` : Dans ce champ, nous avons déclaré que nous utiliserons le fournisseur de déploiement pour [GitHub Pages](https://docs.travis-ci.com/user/deployment/pages/) fourni par Travis-CI, qui n'est rien d'autre que les instructions de configuration pour mettre en place l'environnement de déploiement.

`script` : Ce champ contient les scripts de construction qui seront exécutés lors de l'exécution du travail. Dans ce cas, il s'agit du script de construction, mais vous pouvez également ajouter des scripts de test (couverture de code, test de fusion, etc.) avant la construction.

`cache` : Travis-CI offre une option pour mettre en cache les fichiers de bibliothèque et les modules qui seront constants pour toutes les constructions. Les fichiers mis en cache peuvent être réutilisés par les travaux de construction ultérieurs, ce qui diminue le temps d'exécution de bout en bout du travail.

## Tout est prêt >

D'accord, tout est en place, maintenant, si vous commettez quelque chose sur la branche master, cela déclenchera un travail de construction Travis-CI qui ressemblera à quelque chose comme dans les captures d'écran ci-dessous. Vous pouvez également déclencher une construction manuellement depuis le tableau de bord Travis-CI lui-même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W34g38dx2jy5wxP4yS5y3w.png)
_Travail Travis-CI (en cours)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*V6MOHQiV2agPnAtfo6Wyjw.png)
_Travail Travis-CI (réussi)_

## Mais… (il y a toujours un mais !! huh!!)

Je suis presque sûr que votre tableau de bord de construction ne ressemblera pas à celui ci-dessus, tout comme la vie n'a pas été aussi simple qu'on nous l'avait dit ? Il peut y avoir une infinité de raisons pour lesquelles votre tableau de bord Travis-CI est rempli de constructions échouées (je sais… j'ai vécu cela).

![Image](https://cdn-media-1.freecodecamp.org/images/1*xoGfeAu4sb-_l7ggTbjC7Q.png)

C'est le moment où vos compétences les plus précieuses en matière de « googling » seront utiles. Je vais expliquer quelles sont les erreurs que j'ai rencontrées lorsque j'ai essayé de créer un pipeline.

* Erreurs de sécurité
* Erreurs de jeton
* Juste des erreurs aléatoires (vous devez vous salir les mains et trouver la solution !!)

### Erreurs de jeton >

Si vos constructions échouent en raison d'erreurs de permissions, il y a de fortes chances qu'il y ait un [problème avec les jetons](https://docs.travis-ci.com/user/deployment/pages/#setting-the-github-token). Vous devez aller à l'URL du jeton [https://github.com/settings/tokens](https://github.com/settings/tokens) et voir quand il a été utilisé récemment, s'il indique **_jamais_**, alors vous avez trouvé votre coupable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9NrQnLn0Mrp7Oex9H_F-Og.png)

Suivez les étapes ci-dessous,

* Supprimez et créez un nouveau jeton
* Ajoutez-le aux variables d'environnement Travis (allez dans les paramètres du travail)
* Réessayez la construction

![Image](https://cdn-media-1.freecodecamp.org/images/1*5CtnigPrV0L3ylole9kvVw.png)

### Erreurs de sécurité >

Il y a beaucoup de pratiques de sécurité que nous ignorons lors du codage et de la construction d'applications web. Lorsque nous exécutons en local, ces erreurs de sécurité ne sont pas très importantes et sont souvent ignorées comme des messages d'avertissement, mais lorsque nous essayons de déployer le service en utilisant Travis-CI, ces avertissements provoqueront l'échec de la construction.

Je vais mentionner les erreurs que j'ai rencontrées en travaillant sur mon projet (je vous encourage à mentionner les erreurs que vous avez rencontrées). La bonne chose est que la plupart d'entre elles ont leurs propres pages web dédiées qui expliquent le problème sous-jacent et offrent des solutions/contournements (contournements — nous les aimons tous même en sachant que nous ne devrions pas !!).

* **Utilisation de target=_blank dans la balise HTML <href> :** Il s'agit d'une faille de sécurité plus grave qu'il n'y paraît. Vous pouvez en apprendre davantage à ce sujet [ici](https://mathiasbynens.github.io/rel-noopener/).
* **Redondance dans le code HTML :** Il y avait de nombreuses balises/noms de classe redondants qui faisaient ressembler le code à du junk.

La meilleure façon de prévenir ces erreurs est d'installer le plug-in `es-lint` dans l'éditeur de texte que vous utilisez.

---

## Vous avez construit un projet ? — Partagez-le

J'essaie de construire une communauté de développeurs où les gens peuvent partager leurs idées, leurs connaissances, travailler avec d'autres et trouver d'autres personnes avec une idéologie similaire pour construire des choses ensemble. Donc, si vous avez construit un projet et que vous souhaitez le partager, publiez-le sur le canal.

* Canal Gitter : [https://gitter.im/weekend-devs/community](https://gitter.im/weekend-devs/community)
* Organisation GitHub : [https://github.com/weekend-developers](https://github.com/weekend-developers)

---

## Conclusion

Je voudrais prendre un moment pour reconnaître le travail des personnes qui m'ont inspiré et donné les connaissances pour compléter cet article.

* **Communauté Travis CI :** pour fournir des outils géniaux gratuitement.
* **Mes chers amis :** qui m'ont aidé à corriger mes erreurs.
* **VOUS :** pour être resté, j'espère que vous avez passé un moment productif. Continuez à explorer et à construire des choses incroyables !

---

![Image](https://cdn-media-1.freecodecamp.org/images/0*vNXcdsgZAeulGy1r)
_Photo par [Unsplash](https://unsplash.com/@clemensvanlay?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com/@clemensvanlay?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-creator noopener noopener noopener" target="_blank">Clemens van Lay</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" data-href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" class="markup--anchor markup--figure-anchor" rel="photo-source noopener noopener noopener" target="_blank)_