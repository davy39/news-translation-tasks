---
title: Voici pourquoi votre boucle read-eval-print est si incroyable
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-16T17:49:27.000Z'
originalURL: https://freecodecamp.org/news/this-is-why-your-read-eval-print-loop-is-so-amazing-cf0362003983
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wOeV-wURvl_DeuBPreGGcg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: psychology
  slug: psychology
- name: 'tech '
  slug: tech
seo_title: Voici pourquoi votre boucle read-eval-print est si incroyable
seo_desc: 'By IObert

  One of the things that makes the tech community so special is that we are always
  looking for ways to work more efficiently. Everyone has their favorite set of tools
  which makes them run better. As a professional UI dev, the Chrome DevTools ...'
---

Par IObert

L'une des choses qui rendent la communauté technologique si spéciale est que nous cherchons toujours des moyens de travailler plus efficacement. Chacun a son ensemble d'outils préférés qui lui permettent de mieux fonctionner. En tant que développeur UI professionnel, les Chrome DevTools et la boucle read-eval-print (REPL) de Node.js sont rapidement devenus mes outils préférés. J'ai remarqué qu'ils me permettaient de travailler plus efficacement et d'apprendre de nouvelles choses plus rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/QyirbrnboR992KJY6hdvrkmnqTwS4FGnVuja)
_Les trois phases du processus REPL_

Cela m'a en fait donné envie d'enquêter sur les raisons pour lesquelles cet outil est si utile. J'ai facilement trouvé de nombreux articles de blog expliquant **ce que** sont les REPL et **comment** les utiliser, par exemple [ici](https://clojure.org/guides/repl/introduction) ou [ici](http://blogish.nomistech.com/repl-based-development/). Mais cet article est dédié au **pourquoi** (c'est-à-dire pourquoi les REPL sont-ils un si bon outil pour les développeurs).

> « La raison numéro un pour laquelle les écoles s'éloignent de Java comme langage d'enseignement est la barre élevée pour les programmes Hello-world. »

> — Stuart Halloway

### Qu'est-ce qu'un REPL ?

REPL signifie _read-evaluate-print-loop_ et c'est essentiellement tout ce qu'il y a à savoir.

Votre runtime d'application est dans un état spécifique et le REPL vous aide à interagir avec lui. Le REPL va _lire_ et _évaluer_ les commandes et _afficher_ le résultat, puis revenir au début pour lire votre prochaine entrée. L'étape _évaluer_ peut changer votre runtime. Ce processus peut être vu comme un entretien avec votre application pour interroger son état actuel.

En d'autres termes, le REPL rend votre **runtime plus tangible** et vous permet de **tester des hypothèses** à son sujet.

[Selon Stuart Halloway,](https://vimeo.com/223309989) l'absence d'un REPL en Java est la raison la plus significative pour laquelle les écoles ont commencé à passer à d'autres langages pour enseigner la programmation. Certaines personnes utilisent même le REPL pour [écrire de meilleurs tests unitaires](https://danlebrero.com/2018/11/26/repl-driven-development-immediate-feedback-for-you-backend/).

### Est-ce que j'utilise déjà un REPL (ou un outil similaire) aujourd'hui ?

Cette explication de base vous a peut-être rappelé certains outils que vous utilisez tous les jours. Si vous connaissez et utilisez l'un des outils suivants, la réponse est « oui » :

* Les outils de développement de votre navigateur (comme [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/))
* Votre terminal/shell
* Les Jupyter Notebooks
* Le processus REPL en Clojure
* Repl.it, jsfiddle.net, ou jsbin.com
* Les validateurs de regex en ligne

### Pourquoi le REPL est-il si utile ?

Cette question m'a tenu éveillé la nuit parce que je ne comprenais pas ce qui nous rend inefficaces en premier lieu. J'ai commencé à rechercher certains effets psychologiques courants et j'ai essayé de les lier à mes interactions quotidiennes avec le REPL. Voici mes trois principales hypothèses :

#### Être dans le flow

> Le flow est l'état mental d'opération dans lequel une personne effectuant une activité est complètement immergée dans un sentiment de concentration énergisée, d'implication totale et de plaisir dans le processus de l'activité. ([source](https://en.wikipedia.org/wiki/Flow_(psychology)))

Je pense que nous sommes tous familiers avec cet état, il nous rend extrêmement productifs et [le temps file](https://www.verywellmind.com/what-is-flow-2794768) essentiellement. Malheureusement, il est assez facile de « perdre » le flow, par exemple lorsque vous êtes interrompu ou lorsque vous devez attendre pendant une certaine période. J'ai appris que cela peut arriver très vite : [les chercheurs ont découvert](https://psychology.stackexchange.com/questions/1664/what-is-the-threshold-where-actions-are-perceived-as-instant) qu'une seconde est à peu près la limite pour que le flux de pensée de l'utilisateur reste ininterrompu.

Le REPL n'a pas besoin de compiler ou de déployer votre code. Cela conduit à un temps de réponse très court (<100ms). Ainsi, vous êtes en mesure de tester vos hypothèses sans perdre le flow.

![Image](https://cdn-media-1.freecodecamp.org/images/89s3maIoDGdbPFnt8JKJSGA0foZrdSklK-PT)
_Ce que nous voulons éviter (source : [XKCD](https://xkcd.com/303/" rel="noopener" target="_blank" title="))_

#### Renforcement positif

> Le renforcement positif implique l'ajout d'un stimulus renforçateur suivant un comportement qui rend plus probable la répétition de ce comportement. ([source](https://www.verywellmind.com/what-is-positive-reinforcement-2795412))

C'est l'effet qui m'attire le plus. Votre cerveau apprend à favoriser certaines actions lorsqu'elles ont été récompensées dans le passé. Cette récompense pourrait être un bonus de votre patron après un mois exceptionnel ou un simple « Bon travail ! » de votre moniteur de ski.

Chaque fois que votre expérience REPL réussit et que vous résolvez une énigme/un problème, votre cerveau se sent également récompensé ! Cela se produit également lorsque vous codez dans un IDE commun. Mais le REPL répond beaucoup plus rapidement et vous permet d'itérer plus souvent. Ainsi, plus d'expériences mènent à plus de renforcement. Cet effet vous fait utiliser le REPL plus souvent et garde votre attention sur l'objectif (au lieu de vous distraire en vérifiant vos emails).

#### Amnésie numérique

> La tendance à oublier les informations qui peuvent être facilement trouvées en ligne en utilisant des moteurs de recherche Internet. ([source](https://en.wikipedia.org/wiki/Google_effect))

Je dois admettre que je mélange souvent la syntaxe de Java, Python et JavaScript, car ces informations peuvent être trouvées partout sur Internet. Je me demanderais « Dois-je utiliser _add()_, _append()_ ou _push()_ pour ajouter un nouvel élément à un tableau en JavaScript ? ». Ainsi, pour moi, un exemple de cet effet est le rappel des noms de méthodes des API et des références de langage.

Dans le REPL, je peux voir les fonctions disponibles immédiatement avec l'autocomplétion :

![Image](https://cdn-media-1.freecodecamp.org/images/zjpzMLtOwLZHgDHMmBRremTlLJ-Hv4VDHJON)
_La fonction d'autocomplétion du code du REPL Node.js_

Le plus génial, c'est que cela fonctionne au-delà des objets standard des langages de programmation. Cela fonctionne **pour tous les frameworks et modules**, ce qui rend le REPL plus puissant que votre IDE ! Il n'est plus nécessaire de comparer les numéros de version des modules et des références d'API :

> « La vérité ne peut être trouvée qu'à un seul endroit : le code. »

> — Robert C. Martin, Clean Code

![Image](https://cdn-media-1.freecodecamp.org/images/QAfs4XNxxCuoF6IEEHVxi2Nqs6td8SY42BJ2)
_source : [arungupta.me](http://blog.arungupta.me/jdk9-repl-getting-started/" rel="noopener" target="_blank" title=")_

J'espère que cet article vous a aidé à comprendre comment fonctionne votre cerveau et comment le REPL peut vous aider à être plus productif.

Je suis curieux de voir si vous êtes d'accord avec mes hypothèses ou si vous connaissez d'autres outils pour être un développeur plus efficace.

Mise à jour du 13/02/2019 :

J'ai également écrit [un article de blog](https://blogs.sap.com/2019/02/04/cloudfoundryfun-upgrade-cloud-foundry-with-a-new-repl-feature/) sur l'utilisation des REPL dans les environnements Cloud Foundry.

Consultez [cette vidéo](https://www.twitch.tv/videos/379997882) par [DJ Adams](https://people.sap.com/dj.adams.sap) si vous souhaitez voir le REPL en action 😊