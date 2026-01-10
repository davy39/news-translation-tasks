---
title: Introduction à Chrome Lighthouse
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-06-13T12:29:44.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-chrome-lighthouse
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/0_ya6nIPxZPogtSBxt.png
tags:
- name: Google Chrome
  slug: chrome
- name: Developer Tools
  slug: developer-tools
- name: Lighthouse
  slug: lighthouse
- name: optimization
  slug: optimization
seo_title: Introduction à Chrome Lighthouse
seo_desc: 'Chrome Lighthouse has been around for a while now, but what if I ask you
  to explain what it does can you explain vividly?

  I discovered that a lot of web developers, including beginners, have not heard about
  this tool and those who have, have not trie...'
---

Chrome Lighthouse existe depuis un certain temps, mais si je vous demande d'expliquer ce qu'il fait, pouvez-vous l'expliquer vivement ?

J'ai découvert que beaucoup de développeurs web, y compris les débutants, n'ont pas entendu parler de cet outil et ceux qui en ont entendu parler ne l'ont pas encore essayé, ce n'est pas cool :(.

Dans cet article, je vais vous présenter Chrome Lighthouse, ce qu'il fait et comment commencer à l'utiliser.

> PS : Cet article a été publié pour la première fois sur mon [blog](https://bolajiayodeji.com/introduction-to-chrome-lighthouse-cjx7x1kwe00367vs1qic3jfoi)

Commençons :)

> *Selon Wikipedia, un* ***phare*** *est une tour, un bâtiment ou une autre structure conçue pour émettre de la lumière à partir d'un système de lampes et de* [*lentilles*](https://en.wikipedia.org/wiki/Lens_%28optics%29) *et pour servir d'*[*aide à la navigation*](https://en.wikipedia.org/wiki/Navigational_aid) *pour les* [*pilotes maritimes*](https://en.wikipedia.org/wiki/Maritime_pilot) *en mer ou sur les voies navigables intérieures.*

D'accord, transformons cela en un terme technique ;

> *Lighthouse est une tour, un bâtiment ou une autre structure conçue pour émettre de la lumière à partir d'un système sous le panneau "Audits" dans les outils de développement Chrome et pour servir de guide aux développeurs*

Cela a-t-il un sens ? :)

Eh bien, Lighthouse est un outil développé par Google qui analyse les applications web et les pages web, collectant des métriques de performance modernes et des informations sur les meilleures pratiques des développeurs.

Pensez à Lighthouse comme au compteur de vitesse dans une voiture qui vérifie et équilibre la limite de vitesse de la voiture.

En gros, Lighthouse fonctionne avec les meilleures pratiques des développeurs et les métriques de performance. Il exécute des vérifications sur une application web et vous donne des commentaires sur les erreurs, les pratiques en dessous des normes, des conseils pour de meilleures performances et comment les corriger.

Selon la documentation des développeurs Google

> *Lighthouse est un outil* [*open-source*](https://github.com/GoogleChrome/lighthouse)*, automatisé pour améliorer la qualité des pages web. Vous pouvez l'exécuter contre n'importe quelle page web, publique ou nécessitant une authentification. Il dispose d'audits pour la performance, l'accessibilité, les applications web progressives, et plus encore.*

> *Vous pouvez exécuter Lighthouse dans Chrome DevTools, à partir de la ligne de commande, ou en tant que module Node. Vous donnez à Lighthouse une URL à auditer, il exécute une série d'audits contre la page, puis il génère un rapport sur la performance de la page. À partir de là, utilisez les audits échoués comme indicateurs pour améliorer la page. Chaque audit dispose d'une documentation de référence expliquant pourquoi l'audit est important, ainsi que comment le corriger.*

C'est à peu près tout ce qu'il y a à savoir sur Lighthouse. Il audite l'URL d'une application web et génère un rapport vous indiquant à quel point votre application web est mauvaise ou bonne selon les normes web et les meilleures pratiques des développeurs. De plus, chaque section du rapport est accompagnée d'une documentation expliquant pourquoi cette partie de votre application a été auditée, pourquoi vous devriez améliorer cette partie de votre application et comment la corriger.

Voici une démonstration du rapport d'audit de Lighthouse pour ce blog [https://bolajiayodeji.com](https://bolajiayodehi.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UDPKsgsImqhawyB_shQfHw.png align="left")

*G : Mon blog :) D : Rapport d'audit de Lighthouse*

Plutôt cool, non ? :)

Ce que vous devez noter, c'est que je n'ai pas obtenu de si bons scores dès mon premier audit. J'ai dû utiliser mon premier rapport pour corriger et améliorer les performances et la qualité de mon application.

C'est l'idée derrière Lighthouse, identifier et corriger les problèmes courants qui affectent les performances, l'accessibilité et l'expérience utilisateur de votre site.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qvGmdP7ZMfvGT9Acj1Sdgg.png align="left")

---

Maintenant, passons à la partie intéressante, **COMMENT COMMENCER !!**

LightHouse est disponible dans trois workflows

* Chrome Developer Tools

* Ligne de commande (Node)

* Une extension Chrome

Je préfère personnellement utiliser LightHouse dans Dev Tools. Utiliser l'extension n'a pas de sens car Dev Tool et l'extension fonctionnent dans le même navigateur Chrome, mais nos préférences varient, utilisez ce qui fonctionne le mieux pour vous.

Lighthouse était initialement disponible uniquement avec l'extension Chrome avant d'être ajouté aux Chrome DevTools.

Utiliser lighthouse en ligne de commande est vraiment cool aussi, (pour les geeks :))

*Commençons !!*

---

**\[1\] Exécuter Lighthouse dans Chrome DevTools**

* Téléchargez le navigateur web Google Chrome [ici](https://www.google.com/chrome/browser/desktop/)

> *Notez que Lighthouse ne peut être exécuté que sur un bureau et non sur mobile*

* Allez à l'URL que vous souhaitez auditer dans Google Chrome.

> *Vous pouvez auditer n'importe quelle URL sur le web.*

* Ouvrez Chrome DevTools

```bash
Command+Option+C (Mac)
Control+Shift+C (Windows, Linux, Chrome OS).
```

* Cliquez sur le panneau **Audits**

![Image](https://cdn-media-1.freecodecamp.org/images/1*ACdyR8_RoTjoPNE4mNDeEw.png align="left")

À gauche se trouve la fenêtre d'affichage de la page qui sera auditée, ici c'est mon blog :). À droite se trouve le **panneau Audits** de Chrome DevTools, qui est maintenant alimenté par Lighthouse

* Cliquez sur **Exécuter les audits**

> *DevTools vous montre une liste de catégories d'audit. Assurez-vous de les laisser toutes cochées. Si vous souhaitez personnaliser la partie de votre application à auditer, vous pouvez le faire en cochant les catégories que vous souhaitez auditer.*

* Après 60 à 90 secondes — selon la force de votre connexion internet, Lighthouse vous donne un rapport sur la page.

> *Notez que votre vitesse internet et les extensions préinstallées peuvent affecter les audits de Lighthouse. Pour une meilleure expérience, exécutez les audits en* [*mode Incognito*](https://support.google.com/chrome/answer/95464?co=GENIE.Platform%3DDesktop&hl=en) *pour éviter toute interférence*

**\[2\] Exécuter Lighthouse en ligne de commande**

* Téléchargez le navigateur web Google Chrome [ici](https://www.google.com/chrome/browser/desktop/)

* Téléchargez node [ici](https://nodejs.org/en/), si vous l'avez déjà installé, passez cette étape !

* Installez Lighthouse

```bash
npm install -g lighthouse
# ou utilisez yarn :
yarn global add lighthouse
```

> *Le drapeau* `-g` *l'installe en tant que module global.*

* Exécutez vos audits

```python
lighthouse <url>
```

Exemple :

```bash
lighthouse https://bolajiayodeji.com/
```

Par défaut, Lighthouse écrit le rapport dans un fichier HTML. Vous pouvez contrôler le format de sortie en passant des drapeaux.

Le rapport peut être affiché en format **HTML** ou **JSON**

Exemples de sortie :

```bash
lighthouse
# sauvegarde `./<HOST>_<DATE>.report.html`

lighthouse --output json
# sortie json envoyée à stdout

lighthouse --output html --output-path ./report.html
# sauvegarde `./report.html`

# NOTE : spécifier un chemin de sortie avec plusieurs formats ignore votre extension spécifiée pour *TOUS* les formats
lighthouse --output json --output html --output-path ./myfile.json
# sauvegarde `./myfile.report.json` et `./myfile.report.html`

lighthouse --output json --output html
# sauvegarde `./<HOST>_<DATE>.report.json` et `./<HOST>_<DATE>.report.html`

lighthouse --output-path=~/mydir/foo.out --save-assets
# sauvegarde `~/mydir/foo.report.html`
# sauvegarde `~/mydir/foo-0.trace.json` et `~/mydir/foo-0.devtoolslog.json`

lighthouse --output-path=./report.json --output json
# sauvegarde `./report.json`
```

Exécutez `$ lighthouse --help` pour les options CLI

**\[3\] Exécuter Lighthouse avec l'extension Chrome**

*Comme je l'ai dit plus tôt, le workflow DevTools est le meilleur car il offre les mêmes avantages que le workflow Extension, avec l'avantage supplémentaire de ne nécessiter aucune installation.*

*Pour utiliser cette méthode, vous devez installer l'extension, mais si vous avez vos raisons, voici le guide ;*

* Téléchargez le navigateur web Google Chrome [ici](https://www.google.com/chrome/browser/desktop/)

* Installez l'[extension Chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) depuis le Chrome Webstore.

* Accédez à la page que vous souhaitez auditer

* Cliquez sur **l'icône Lighthouse**.

> *Elle devrait être à côté de la barre d'adresse de Chrome. Si ce n'est pas le cas, ouvrez le menu principal de Chrome (les trois points en haut à droite) et accédez-y en haut du menu. Après avoir cliqué, le menu Lighthouse s'étend.*

* Cliquez sur **Générer un rapport**.

> *Lighthouse exécute ses audits contre la page ouverte, puis ouvre un nouvel onglet avec un rapport des résultats.*

Bingo ! Vous l'avez fait

---

C'est à peu près tout, Lighthouse est un excellent outil, surtout pour les débutants.

C'est un outil très utile lorsqu'il s'agit d'auditer des applications web progressives.

J'ai vraiment appris beaucoup de choses sur l'optimisation et les normes de performance lorsque j'ai commencé à utiliser Lighthouse. En peu de temps, vous deviendrez un expert dans la création d'applications web entièrement optimisées avec de grandes performances, accessibilité et expérience utilisateur. :)

> *Lighthouse n'est pas magique, il a été créé par des humains. Il est open source et* [*les contributions sont les bienvenues*](https://github.com/GoogleChrome/lighthouse/blob/master/CONTRIBUTING.md)*. Consultez le* [*suivi des problèmes*](https://github.com/GoogleChrome/lighthouse/issues) *du dépôt pour trouver des bugs que vous pouvez corriger, ou des audits que vous pouvez créer ou améliorer. Le suivi des problèmes est également un bon endroit pour discuter des métriques d'audit, des idées pour de nouveaux audits, ou de tout autre sujet lié à Lighthouse.*

Merci d'avoir lu ceci, après avoir installé et utilisé Lighthouse, partagez vos histoires de succès dans les commentaires !

> *De plus, je viens de lancer* [*mon blog*](https://bolajiayodeji.com) *où j'écris des articles sur le développement web et frontend, n'oubliez pas de visiter et de partager !!!*