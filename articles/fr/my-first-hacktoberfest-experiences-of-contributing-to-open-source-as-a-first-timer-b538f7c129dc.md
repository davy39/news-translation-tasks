---
title: Mon premier Hacktoberfest — Expériences de contribution à l'Open Source en
  tant que débutant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T23:26:06.000Z'
originalURL: https://freecodecamp.org/news/my-first-hacktoberfest-experiences-of-contributing-to-open-source-as-a-first-timer-b538f7c129dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RAY-ZG2pcG1IOHrNuj__-A.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Mon premier Hacktoberfest — Expériences de contribution à l'Open Source
  en tant que débutant
seo_desc: 'By Sibylle Sehl

  Contributing to Open Source and projects can seem like a daunting process. Your
  favorite search engine will return a ton of results on guides and repositories to
  get started. But many times, your search does not yield the result you w...'
---

Par Sibylle Sehl

Contribuer à l'Open Source et aux projets peut sembler un processus intimidant. Votre moteur de recherche préféré retournera une tonne de résultats sur les guides et les dépôts pour commencer. Mais souvent, votre recherche ne donne pas le résultat souhaité, vous ne savez toujours pas comment contribuer à l'Open Source même après avoir lu plusieurs articles de blog. La réputation imposante de certains projets et un ton dur n'aident pas non plus et peuvent compliquer encore plus les choses.

J'ai été là moi-même. J'ai parcouru des pages pour trouver de grands dépôts Open Source auxquels contribuer, pour réaliser que je ne savais pas comment commencer.

Frustrée et un peu déçue, j'ai commencé à me concentrer sur d'autres projets à la place.

Mais tout a changé quand j'ai vu un autocollant Hacktoberfest sur l'ordinateur portable d'un collègue. J'étais intriguée — était-ce un vestige d'un autre Hackathon ?

Hacktoberfest s'est avéré très différent.

### Alors, qu'est-ce que Hacktoberfest exactement ?

Indice : cela n'a rien à voir avec la bière, le piratage ou l'Oktoberfest (qui a en fait lieu en septembre, bien sûr !).

[Hacktoberfest](https://hacktoberfest.digitalocean.com/) est une célébration d'un mois de contribution à l'Open Source, du 1er octobre au 31 octobre. Il a été initié par DigitalOcean en collaboration avec GitHub. Pendant le mois d'octobre, vous êtes encouragé à contribuer et à faire des pull requests à vos dépôts préférés sur GitHub. Si vous arrivez à en faire quatre au total, vous êtes éligible pour recevoir un T-shirt élégant comme celui-ci !

![Image](https://cdn-media-1.freecodecamp.org/images/tvLihMaZR91TmZNQd32VhntPuvtTg3HY0PYw)
_Ce magnifique T-shirt est ce que vous recevez après avoir complété Hacktoberfest (Crédit : @mahsinger sur Twitter)_

### Étiquettes, étiquettes, étiquettes

Hacktoberfest s'est avéré être un excellent mois pour se lancer dans l'Open Source. GitHub était rempli de problèmes étiquetés _Hacktoberfest_ qui avaient besoin de votre aide. Il y avait suffisamment de projets parmi lesquels choisir — allant de la documentation à Python en passant par RUST. Pendant cette période, j'ai appris à rechercher des problèmes sur GitHub par _étiquettes_ et à trouver de bons problèmes auxquels contribuer.

Pour des personnes comme moi, qui n'avaient aucune expérience, des étiquettes telles que _first-timers-only_, _easy_ ou _good-first-issue_ se sont avérées être mes amies. Il existe également quelques bons sites qui visent à faciliter le processus de recherche de ces problèmes. Par exemple, [up-for-grabs.net](http://up-for-grabs.net/) ou [code-triage](https://www.codetriage.com/) — il y en a probablement beaucoup d'autres.

Allez vous inscrire à quelques-uns de ces sites ou consultez leurs problèmes !

### Apprendre à contribuer

En essayant de faire mes premières contributions, j'ai réalisé que mon plus grand inconnu n'était pas comment ajouter des liens en markdown ou styliser une page. Mais comment faire une _bonne_ pull request en utilisant git et la ligne de commande.

J'ai trouvé le [guide gratuit de Kent C. Dodds sur egghead.io](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github) utile et j'ai pris des notes des commandes de ligne de commande que j'ai exécutées en suivant le guide.

Les instructions pouvaient être résumées à quelque chose d'aussi simple que ceci :

```
// D'abord, vous devez trouver un dépôt auquel vous voulez contribuer et le fork ! 
```

```
// Ensuite, vous devez cloner le dépôt forké git clone git@github.com:yourusername/contributing-repo.git
```

```
// Changez votre répertoire pour le nouveau dépôt que vous avez cloné cd contributing-repo
```

```
// Définissez le dépôt upstream vers le dépôt original (pas celui que vous venez de cloner) git remote add upstream git@github.com:the-owners-username/contributing-repo.git
```

```
// Mettez à jour les changements git fetch upstream
```

```
// Définissez notre branche master pour qu'elle soit la même que la branche upstream git branch --set-upstream-to=upstream/master master
```

```
// Créez votre propre nouvelle branche pour votre pull request git checkout -b pr/my-new-cool-contribution
```

```
// Faites les changements dans votre éditeur de texte préféré et sauvegardez
```

```
// Vérifiez le statut (doit montrer les fichiers modifiés) git status
```

```
// Regardez les changements et réévaluez votre travail git diff
```

```
// Ajoutez les changements à votre zone de staging ( . pour tous les fichiers) git add .
```

```
// Validez tous les changements et ajoutez un message pour le mainteneur du dépôt git commit -m "J'ai ajouté ce texte cool à votre dépôt de guide"
```

```
// Poussez vers le dépôt source et créez une pull request git push origin pr/my-new-cool-contribution
```

Cela m'a vraiment aidée à comprendre le but d'une pull request et à comprendre le processus de contribution. [Cet article de blog](https://medium.com/@mscccc/jr-developers-1-pull-requests-you-39a11c3bdd94) m'a également aidée à comprendre que être descriptif est votre meilleure arme — ainsi vous pouvez obtenir du soutien et indiquer si une pull request est toujours en cours. Peu de temps après, j'ai fait une autre contribution de pratique, mais pour recevoir un T-shirt, je devais améliorer mon jeu et trouver deux autres problèmes.

### Un match fait au paradis — contribuer aux guides freeCodeCamp

J'ai ouvert Medium un jour et j'ai vu que Quincy Larson avait fourni un [guide complet sur la manière dont les gens pouvaient facilement contribuer au dépôt des guides freeCodeCamp](https://medium.freecodecamp.org/i-just-got-my-free-hacktoberfest-shirt-heres-a-quick-way-you-can-get-yours-fa78d6e24307). Une source de connaissances partagées à travers le développement, le produit, le design et la science des données. Contribuer à ce dépôt n'était pas seulement fortement encouragé, mais aussi super facile. Vous pouviez faire les contributions dans votre navigateur.

Trouver un sujet n'était pas difficile car le dépôt des guides couvrait tout, de l'accessibilité à HTML en passant par le développement de jeux.

Ce qui m'a le plus intriguée, c'est la facilité avec laquelle freeCodeCamp a rendu le processus pour permettre aux nouveaux comme moi de faire des contributions significatives. Partager des connaissances avec les autres.

Vous appreniez toujours à faire des pull requests, à avoir vos contributions fusionnées et à adhérer aux normes et aux directives de contribution. Le processus était légèrement moins intimidant. C'était parfait pour un débutant. En fait, c'était si rationalisé que freeCodeCamp avait réussi à faire un gif qui résume le processus :

![Image](https://cdn-media-1.freecodecamp.org/images/S6Pfccsc7EvGQR8n4xv720Z4leIRBKKeGhs2)
_Crédit : freeCodeCamp — Contribuer au dépôt des guides freeCodeCamp_

Après quelques délibérations, j'ai décidé de faire une petite contribution sur différentes distributions Linux. Et d'écrire une section complètement nouvelle sur le développement de jeux pour compléter mes quatre pull requests. J'ai fait un jeu pendant l'été dans le cadre de mon projet de dissertation. Écrire sur le développement de jeux et les outils semblait être un bon moyen de partager mes nouvelles connaissances avec les autres.

Dans leurs [directives Contributing.md](https://github.com/freeCodeCamp/guides/blob/master/CONTRIBUTING.md), freeCodeCamp avait donné beaucoup de détails et un moyen de s'assurer que votre écriture était concise. J'ai fait toutes mes recherches, je les ai soutenues avec des sources et je les ai passées à travers l'[application Hemingway](http://www.hemingwayapp.com/). La voix active et les phrases courtes pour la victoire !

J'ai fait ma pull request et j'étais aux anges quand elle a été fusionnée. Les commentaires encourageants étaient également un grand plus de la part de la communauté freeCodeCamp.

![Image](https://cdn-media-1.freecodecamp.org/images/-HBwPGWrDEYvOti1MsfsXcmgk7kxwFhH2oMt)
_Pull Request pour la section sur le développement de jeux que j'ai écrite pour les guides freeCodeCamp_

### Que pouvons-nous retenir de cela ?

Je vous conseillerais de vous libérer de l'idée que vous devez contribuer un code parfait et bien structuré dès la première fois. Votre première contribution n'a pas besoin d'être révolutionnaire (ou même d'être du code à proprement parler).

Les mainteneurs de projets savent que cela pourrait être votre première contribution Open Source s'ils ont étiqueté le problème comme _first-timers-only_ ou similaire. Votre contribution peut être n'importe quoi, comme corriger une faute d'orthographe, ajouter des hyperliens ou un petit projet d'apprentissage. Commencez petit pour vous familiariser avec le processus.

De nombreux mainteneurs de projets qui étiquetent leurs problèmes comme adaptés aux débutants sont également heureux de répondre à vos questions et de fournir un soutien. Alors, n'hésitez pas à demander des éclaircissements si vous ne comprenez pas quelque chose.

Quand le T-shirt Hacktoberfest est enfin arrivé à la mi-décembre, expédié depuis l'Amérique, j'ai eu l'impression que Noël était arrivé tôt. Le tenir dans mes mains m'a fait réaliser que j'avais aidé à créer et à étendre quelque chose qui comptait. Un sentiment que je crois que beaucoup de personnes contribuant régulièrement à l'Open Source ressentent. Le porter me rappelle toujours de partager mes connaissances et cette année, j'essaierai aussi de faire le saut pour contribuer plus de code, après tout, je ne suis plus une débutante !