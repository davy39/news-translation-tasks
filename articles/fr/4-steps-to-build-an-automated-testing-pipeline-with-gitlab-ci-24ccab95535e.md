---
title: 'Attraper les bugs systématiquement : comment construire un pipeline de test
  GitLab CI en 4 étapes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-14T20:05:02.000Z'
originalURL: https://freecodecamp.org/news/4-steps-to-build-an-automated-testing-pipeline-with-gitlab-ci-24ccab95535e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3HCwOHLXPebHuA-2oe_FMA.jpeg
tags:
- name: Continuou
  slug: continuou
- name: Docker
  slug: docker
- name: GitLab
  slug: gitlab
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: 'Attraper les bugs systématiquement : comment construire un pipeline de
  test GitLab CI en 4 étapes'
seo_desc: 'By Joyz

  Your first app is a hit the day it’s launched. But one week later, you realize that
  it has no retention. You discover that this is because whenever a user clicks the
  “send” button, their comments get posted twice.

  The bug was so minor, but it...'
---

Par Joyz

Votre première application est un succès dès son lancement. Mais une semaine plus tard, vous réalisez qu'elle n'a aucune rétention. Vous découvrez que cela est dû au fait que chaque fois qu'un utilisateur clique sur le bouton "envoyer", leurs commentaires sont publiés deux fois.

Le bug était si mineur, mais il a tué votre élan. Mais ce n'est pas grave. Pour votre deuxième application, vous et votre partenaire vérifiez plus soigneusement. Vous cliquez, cliquez, cliquez sur votre application jour et nuit pour empêcher les petits bugs comme celui-ci de se reproduire.

Pour une application, c'est acceptable. Mais après un an, vous avez une entreprise qui construit 7 applications sur différentes plateformes, y compris le web, iOS et Android. Votre équipe fait maintenant une revue de code avant tout lancement d'application. Vous testez les applications et faites vos clics avant qu'elles ne soient livrées. Mais votre cauchemar de l'application #1 revient : les utilisateurs abandonnent l'application et cette fois, c'est parce que leurs publications affichent des caractères étranges lorsqu'ils tapent un emoji. Vous vous retrouvez avec des évaluations de 1 étoile après le lancement.

Il existe 3 types d'entreprises qui fabriquent des produits : celles qui ne testent pas, celles qui testent, et celles qui testent rapidement, avec précision et fréquemment.

Un système de test automatisé avec intégration continue (CI) est-il juste un rêve ? La CI semble être un "plus", surtout puisque les services qui exécutent des tests et génèrent des rapports comme [Sauce Labs](https://saucelabs.com/), [BrowserStack](https://www.browserstack.com/), [Test Complete](https://support.smartbear.com/testcomplete/) sont coûteux. La bonne nouvelle est qu'il existe de nombreux outils gratuits et populaires que vous pouvez mixer et associer pour mettre en place un système de test automatisé gratuit. En tant que testeur QA, j'ai découvert une configuration de pipeline de test gratuite, alors je la partage pour vous faire gagner du temps et de l'argent.

Pourquoi ma société voulait-elle mettre en place un système automatisé ? Voici quelques raisons ci-dessous :

* Nous détestons les travaux manuels répétitifs sujets aux erreurs humaines.
* Nous voulons un processus plus fluide (tester lorsqu'il y a une mise à jour de code), et réduire le temps d'attente.
* Nous voulons planifier les tests et les maîtriser.

### Installation des tests UI

Cet article présente une configuration de pipeline pratique qui peut exécuter des tests UI (Interface Utilisateur) basés sur le web automatiquement et en continu. La partie suivante peut être un peu technique, mais c'est assez amusant à construire !

J'ai configuré l'ensemble du système avec ces outils gratuits et open-source :

* [Selenium](http://www.seleniumhq.org/) — pour scripter et automatiser les navigateurs afin d'effectuer des tests
* [Docker](https://www.docker.com/) — pour construire une image pour l'environnement de test et la déployer rapidement
* [Gitlab CI](https://about.gitlab.com/gitlab-ci/) — pour déclencher, construire et exécuter le test lors des mises à jour de code
* [Skygear](https://skygear.io/) — pour sauvegarder les résultats de test pour un rapport à la demande

![Image](https://cdn-media-1.freecodecamp.org/images/1*3HCwOHLXPebHuA-2oe_FMA.jpeg)
_L'installation se fait en 4 étapes. C'est parti !_

### Étape #1 : Écrire le script et l'exécuter localement

Tout d'abord, nous écrivons le script de test, pour que notre test manuel original s'exécute automatiquement. [Selenium](http://www.seleniumhq.org/) est un outil bien connu pour l'automatisation web. Il supporte différents langages clients, y compris Java, Ruby, Python, etc.

Voici un exemple de clic sur un bouton sur un site web en Python.

> Mise à jour : Ajout de l'utilisation du mode headless officiel de Chrome (détails [ici](https://medium.com/@joyzoursky/recent-updates-6264d1e5d42f)).

Avec l'idée d'un modèle de test unitaire de base, nous pouvons facilement identifier ces trois composants majeurs dans le script :

* Configuration
* Exécution du cas de test
* Nettoyage

Dans ce script, il exécutera `test_case_1` et `test_case_2` respectivement, tous deux avec `setUp` avant le test et `tearDown` après le test. Nous utilisons [unittest](https://docs.python.org/3/library/unittest.html) comme framework de test dans cet exemple. N'hésitez pas à utiliser ce que vous préférez, comme [pytest](http://doc.pytest.org/en/latest/) ou [nose](http://nose.readthedocs.io/en/latest/) en Python.

Vous pouvez ajouter plus de cas de test, comme le remplissage de formulaires et le clic sur des éléments, en fonction de l'interface de votre site web.

### Étape #2 : Construire une image avec votre environnement de test

L'exécution des tests nécessite un environnement propre. Pour créer un environnement propre, nous ne voulons certainement pas configurer une machine réelle à chaque fois et attendre des heures pour installer tous les logiciels nécessaires. Le concept de conteneur aide.

[Docker](https://www.docker.com/) vous aide à construire votre environnement de test dans une image. L'image inclut tous les logiciels qui doivent être préinstallés et exécutés sur ce conteneur comme une machine virtuelle. Avec Docker, vous pouvez simplement créer un nouveau conteneur et tirer la même image à chaque fois que vous voulez recommencer à partir de votre environnement par défaut.

Pour effectuer notre test avec le client Python Selenium, nous voulons que notre image préinstalle les éléments suivants :

* Python
* Google Chrome
* Chrome driver
* [Xvfb](https://en.wikipedia.org/wiki/Xvfb)

Xvfb est un serveur d'affichage virtuel qui vous aide à lancer un navigateur en [mode headless](http://elementalselenium.com/tips/38-headless) (sans affichage). Il est nécessaire d'exécuter les tests UI dans un conteneur. Il ne peut pas se connecter à une sortie d'affichage pour montrer le navigateur visuellement.

Ensuite, nous installerons également le package Selenium à l'intérieur du conteneur. Tous les projets n'ont pas besoin de la même liste de packages.

Nous créons un [Dockerfile](https://docs.docker.com/engine/reference/builder/), construisons l'image et la téléchargeons sur notre [Docker Cloud](https://cloud.docker.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6O2QhCEpjoALjK1nzo0N7g.png)

Vous pouvez trouver cette image via ce [lien](https://hub.docker.com/r/joyzoursky/python-chromedriver/), ou directement tirer cette image avec cette commande :

```
docker pull joyzoursky/python-chromedriver:3.6-xvfb
```

Ensuite, vous aurez un environnement prêt pour effectuer les tests UI.

> Mise à jour : Ajout d'une nouvelle image Docker construite avec Xvfb obsolète (détails [ici](https://medium.com/@joyzoursky/recent-updates-6264d1e5d42f)).

### Étape #3 : Configurer GitLab CI

[GitLab](https://about.gitlab.com/) fournit une fonctionnalité de pipelines CI/CD, pour construire et exécuter vos projets en continu. La configuration est similaire à d'autres outils CI tels que [Travis CI](https://travis-ci.org/) ou [Jenkins](https://jenkins.io/). Cela nécessite un fichier `.gitlab-ci.yml` pour configurer votre processus de construction.

Jetez un coup d'œil à cet exemple :

> Mise à jour : Ajout d'un exemple avec Xvfb obsolète (détails [ici](https://medium.com/@joyzoursky/recent-updates-6264d1e5d42f)).

Lorsque de nouveaux codes sont poussés vers le dépôt, GitLab recherchera `.gitlab-ci.yml` à partir du répertoire racine, et déclenchera une construction selon vos paramètres.

Dans ce script, il tire l'image de l'environnement de `joyzoursky/python-chromedriver:3.6-xvfb` dans la première ligne. Ensuite, il installe les packages requis comme Selenium, définit les variables nécessaires, et puis il démarre le processus.

Notez qu'il y a 2 étapes du processus de construction dans cet exemple : `test` et `report`. Dans chaque étape, les travaux de cette étape seront exécutés **concurremment.** Vous pouvez définir des tests dans la même étape s'ils peuvent s'exécuter en synchronisation.

Allez sur la page Pipelines pour voir le flux et l'achèvement ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yEi8rtmbGz0JYottZ188oA.png)

Alors, où exécutons-nous nos tests réellement ?

GitLab héberge certains runners partagés qui sont gratuits. En regardant le journal de construction, nous pouvons trouver les informations du conteneur dans les premières lignes :

```
Running with gitlab-ci-multi-runner 1.10.4 (b32125f)Using Docker executor with image joyzoursky/python-chromedriver:3.5 ...Pulling docker image joyzoursky/python-chromedriver:3.5 ...Running on runner-4e4528ca-project-2749300-concurrent-0 via runner-4e4528ca-machine-1489737516-5e0de836-digital-ocean-4gb...
```

Il montre le nom du conteneur s'exécutant sur [Digital Ocean](https://www.digitalocean.com/).

Bien sûr, vous pouvez également créer vos propres runners pour exécuter le test sur vos machines auto-hébergées. GitLab supporte les runners sur différentes plateformes, y compris [Docker](https://www.docker.com/) et [Kubernetes](https://kubernetes.io/). Mais, comme GitLab est une nouvelle plateforme, elle subit de nombreuses mises à jour. Donc, les runners spécifiques peuvent parfois ne plus fonctionner lorsqu'ils sont obsolètes. Vous devriez toujours vous référer au [dépôt officiel](https://gitlab.com/gitlab-org/gitlab-ci-multi-runner/tree/master) lors de la configuration de la mise en place.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JZJwNUSlvVrA-mF2noJiLQ.png)

### Étape #4 : Exécuter et rapporter périodiquement

Vous pouvez vouloir que vos tests s'exécutent périodiquement. Vous pouvez y parvenir en configurant des [cron jobs](https://en.wikipedia.org/wiki/Cron), mais vous ne voulez peut-être pas configurer un serveur juste pour exécuter un cron job d'une ligne. Le serveur open source sans serveur de ma société est [Skygear](http://skygear.io). Nous pouvons l'utiliser pour écrire une simple fonction de code cloud avec le décorateur [@every](https://docs.skygear.io/guides/cloud-function/scheduled-tasks/python/) et déclencher le pipeline de test à intervalles de temps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yuASEuatDfLkSD3sfmKaqA.png)
_[Portail des développeurs de Skygear](https://skygear.io/" rel="noopener" target="_blank" title="). Recherchez votre URL Git de Cloud Code._

* Connectez-vous à votre [portail Skygear](https://portal.skygear.io)
* Trouvez votre URL Git de Cloud Code
* Clonez les codes de démarrage rapide
* Modifiez pour ajouter le petit morceau de code ci-dessous
* Poussez les codes et le cron job déclenchera le test toutes les heures

> Mise à jour : Utilisation du planificateur de pipeline GitLab 10.0 au lieu du cron job (détails [ici](https://medium.com/@joyzoursky/recent-updates-6264d1e5d42f)).

Supposons que vous avez déjà écrit du code pour générer des rapports de test. Souhaitez-vous recevoir et lire les rapports de test toutes les heures ? Bien sûr que non. Donc, nous relions également le service [Cloud DB gratuit de Skygear](https://docs.skygear.io/guides/cloud-db/basics/js/) pour stocker les résultats des tests. Le système n'envoie des alertes que lorsqu'un cas de test passe de PASS à FAIL, ou de FAIL à PASS. Cette approche de notification peut varier selon les besoins du projet.

Pour sauvegarder et récupérer des données de la base de données Skygear, nous pouvons utiliser le SDK existant. Ou si vous êtes un utilisateur Python, vous pouvez utiliser ce petit [client DB Python](https://github.com/skygear-demo/python-db-client) pour vous aider à écrire votre gestionnaire de données. Nous l'utilisons pour sauvegarder les résultats des tests après chaque cas de test, et récupérer les rapports après avoir exécuté toutes les suites de test.

Enfin, nous pouvons avoir les alertes de résultats de test envoyées à la demande.

P.S. Nous utilisons l'API de messagerie en temps réel [Slack](https://slack.com/) [real time messaging API](https://api.slack.com/rtm) pour faire les rapports, afin que nous puissions recevoir des notifications dans les canaux de projet correspondants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xHr_ezmVEBYRVZ4oOLJq3Q.png)

### Conclusion

Maintenant, chaque fois qu'il y a une mise à jour de code sur la branche de production, ce test UI automatisé est déclenché et les tests sont effectués automatiquement. Les résultats de failure seront poussés vers notre canal Slack pour notifier nos développeurs.

Le plus grand obstacle à la mise en place d'un test UI automatisé gratuit est probablement la recherche des outils si vous n'êtes pas déjà un testeur QA professionnel. Puisque le QA est mon travail à temps plein, j'espère que le partage de notre stack de test UI améliorée vous aidera également à libérer votre temps !

Si vous avez trouvé cela utile, veuillez cliquer sur le ? ci-dessous pour que d'autres personnes puissent le voir aussi. Merci !