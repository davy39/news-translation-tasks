---
title: Comment intégrer DangerJS dans les pipelines GoCD
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-01T12:52:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-dangerjs-into-gocd-pipelines-7f930932ea07
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rOWdHY7akUNLQOGIh5VtoQ.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: dangerjs
  slug: dangerjs
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment intégrer DangerJS dans les pipelines GoCD
seo_desc: 'By Leonardo Lima

  At my current company, we have recently migrated our CI infra from CircleCI to GoCD.
  After a few months using the new CI platform, I was comfortable enough to juice
  it up. One of the things that I was planning was integrating DangerJ...'
---

Par Leonardo Lima

Dans mon entreprise actuelle, nous avons récemment migré notre infrastructure CI de CircleCI vers [GoCD](https://www.gocd.org/). Après quelques mois d'utilisation de la nouvelle plateforme CI, je me sentais suffisamment à l'aise pour l'optimiser. L'une des choses que je prévoyais était d'intégrer [DangerJS](http://danger.systems/js) — un outil incroyable pour accélérer les revues de pull request en effectuant des vérifications automatiques configurables sur le nouveau code. Que signifie-t-il ? Plus de temps perdu à écrire des commentaires de PR comme : « Oh, je crois que vous avez oublié X… Y… Z… ».

Mon objectif avec cet article est d'aider la prochaine personne poursuivant cette mission à améliorer les processus de qualité de code et de revue de PR de leur équipe.

### Contexte

J'ai déjà utilisé les pouvoirs de Danger (bien qu'intégré avec Ruby) et je savais déjà que la configuration initiale serait assez simple… si seulement nous utilisions encore CircleCI !

Lors de ma première tentative d'intégration, j'ai essayé de rechercher « Integrating DangerJS with GoCD » sans succès. De plus, après avoir lu la documentation de DangerJS, j'ai constaté qu'il n'existait pas d'intégration native et directe avec GoCD que je pouvais utiliser.

Cela signifiait que je ne pourrais pas intégrer facilement les vérifications de Danger dans mon flux CI. J'avais donc quelques options :

1. Essayer de faire en sorte que les développeurs incorporent des exécutions manuelles locales des commandes DangerJS ;
2. Construire un pipeline spécifique dans (CircleCI/CodeShip/FooBar) pour exécuter uniquement DangerJS ;
3. Abandonner.

Aucune de ces options ne me plaisait, et j'étais vraiment frustré après avoir passé quelques heures sur les paramètres de Danger et GoCD. Puis je suis tombé sur la section « [Using danger and fake being on a CI](https://danger.systems/js/guides/the_dangerfile.html#using-danger-and-faking-being-on-a-ci) » dans la documentation de DangerJS. C'est ça ! Si je peux simuler un environnement CI sur ma machine locale, quelle est la différence avec la simulation d'un CI sur une machine GoCD ?

Ensuite, il ne restait plus qu'à comprendre comment émuler le même comportement local à l'intérieur de l'infrastructure de GoCD.

### Premières étapes

Avant toute chose, vous devez suivre la [documentation officielle](https://danger.systems/js/guides/getting_started.html#setting-up-danger-to-run-on-your-ci) afin de configurer et commencer à utiliser DangerJS.

En résumé, vous avez besoin de :

* Créer votre fichier dangerfile.js. Il y a quelques [exemples ici](https://danger.systems/js/guides/the_dangerfile.html#examples).
* [Créer un compte bot](https://danger.systems/js/guides/getting_started.html#creating-a-bot-account-for-danger-to-use) sur GitHub/BitBucket pour que Danger l'utilise
* Ouvrir une PR avec des fichiers modifiés pour vérifier vos changements
* Exécuter DangerJS localement contre un lien de PR (celui que vous venez d'ouvrir)
* Essayer de [simuler un environnement CI](https://danger.systems/js/guides/the_dangerfile.html#using-danger-and-faking-being-on-a-ci) sur votre machine locale

Dans la section suivante, je vais approfondir cette dernière étape, car c'est la partie critique pour faire fonctionner DangerJS avec GoCD.

### Configurer un faux CI dans l'environnement de GoCD

Tout d'abord, si vous n'avez pas encore de pipeline GoCD détacher pour exécuter uniquement les builds de Pull Requests, je vous recommande fortement de le faire. [Voici un guide](https://docs.gocd.org/current/configuration/quick_pipeline_setup.html) si vous avez besoin d'aide pour le configurer.

Deuxièmement, après avoir créé votre pipeline de PR, créez un nouveau Job uniquement pour Danger :

![Image](https://cdn-media-1.freecodecamp.org/images/qmTP33WaR1bR5hpRzWag5D35amrOh5O6LmMW)

Maintenant, pour pouvoir simuler un CI en utilisant Danger, vous devez définir un ensemble de variables d'environnement telles que :

```
export DANGER_FAKE_CI="YEP"
export DANGER_TEST_REPO="username/reponame"
```

Dans les paramètres du Job du Pipeline GoCD, accédez à l'onglet Variables d'environnement et définissez ces deux variables d'environnement en remplaçant les espaces réservés **username/reponame** par vos propres paramètres.

![Image](https://cdn-media-1.freecodecamp.org/images/iVqne-VCmoSnzmKOXDbZijdURv2QYyqmjwqQ)
_Je recommande de placer le DANGER_GITHUB_API_TOKEN généré lors des premières étapes de configuration de DangerJS dans la section Variables sécurisées._

Après cette première série de configurations, afin d'exécuter réellement les tests de Danger dans GoCD, vous pouvez utiliser un script shell qui exécute les mêmes commandes utilisées pour simuler un CI dans un environnement local. Appelons ce fichier danger-build.sh.

```
# danger-build.sh

echo '─ ─ DÉBUT VÉRIFICATION DANGER JS ─'

echo Test contre les commits sur PR : ${GO_SCM_PIPELINE_PR_URL}

DANGER_TEST_PR=${GO_SCM_PIPELINE_PR_ID} npx yarn danger ci

echo '─ ─ FIN VÉRIFICATION DANGER JS ─'
```

Veuillez noter que vous aurez besoin de node, npm/yarn préalablement installés sur la machine disponible de GoCD.

**Avez-vous remarqué ces deux variables GO_SCM** ? Elles sont la clé qui vous permet d'exécuter vos vérifications Danger à l'intérieur d'une machine GoCD.

Veuillez porter une attention particulière à la variable PR_ID, car c'est celle qui fournit la référence de PR pour permettre à Danger de lire, interpréter les changements, puis écrire des suggestions dans la Pull Request.

Si vous êtes curieux, ces variables d'environnement ont été générées par les machines de GoCD. Elles peuvent être évaluées en exécutant la commande UNIX `/usr/bin/printenv` dans un build et en inspectant la sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/TOzoSEn6HBEnOOVKEJZQTefZKKCd6rsQSMOt)

Et c'est tout !

Après avoir mappé les variables d'environnement appropriées dans votre script Shell, les vérifications DangerJS commenceront à s'exécuter dans les pipelines de GoCD à côté de votre suite de tests actuelle.

Pour résumer les étapes :

1. Configurer les premiers fichiers et paramètres locaux de DangerJS

2. Créer un Pipeline/Job spécifique dans GoCD

3. Découvrir puis mapper les variables d'environnement appropriées dans un script shell pour permettre à GoCD d'exécuter DangerJS

J'espère que vous avez trouvé ce guide utile. Si vous avez aimé l'article, partagez-le avec vos collègues développeurs et managers et aidez à diffuser l'information.

Pour toute question, n'hésitez pas à demander dans la section des commentaires !

PS : Danger dispose également de nombreuses options de plugins, [découvrez-les](https://danger.systems/js/) !