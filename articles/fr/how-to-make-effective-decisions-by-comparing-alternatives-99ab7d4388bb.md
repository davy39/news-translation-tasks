---
title: Comment prendre des décisions efficaces en comparant des alternatives
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-19T23:41:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-effective-decisions-by-comparing-alternatives-99ab7d4388bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D1a3wrXwc0gWi65Na_fdyg.jpeg
tags:
- name: decision making
  slug: decision-making
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: teamwork
  slug: teamwork
- name: 'tech '
  slug: tech
seo_title: Comment prendre des décisions efficaces en comparant des alternatives
seo_desc: 'By Alon Kiriati

  Not better, not worse… just different

  “React.js is so much better than Angular”. “Java sucks, no one uses it anymore…
  we should use Golang”. “Pineapple is the worst pizza topping”. You’ve probably heard
  one of these very straight opin...'
---

Par Alon Kiriati

### Ni meilleur, ni pire… juste différent

« React.js est bien mieux qu'Angular ». « Java est nul, plus personne ne l'utilise… nous devrions utiliser Golang ». « L'ananas est la pire garniture de pizza ». Vous avez probablement entendu l'une de ces opinions très tranchées. Une option est la meilleure, l'autre est la pire, X est mieux que Y, et ainsi de suite. Mais Java reste l'un des langages les plus populaires au monde. Angular donne une bonne lutte à React.js. La pizza à l'ananas… eh bien, c'est Beurk.

Cela signifie-t-il que plus de la moitié des gens sont sans discernement ? Ou ne savent pas comment dire quelle technologie est meilleure ou faire les bons choix ? Peut-être devrions-nous arrêter d'utiliser des termes comme « meilleur », « pire », « le meilleur » et les comparaisons superficielles lors de l'évaluation des alternatives. Au lieu de cela, nous devrions nous concentrer sur les avantages de chaque solution, les inconvénients et celle qui est la mieux adaptée à notre problème spécifique.

### Évaluer les alternatives

Une façon de faire cela est de créer un tableau de comparaison des alternatives :

* Écrivez les différentes alternatives dans l'en-tête. Utilisez chaque colonne pour évaluer une alternative. Choisissez 2 à 5 alternatives.
* Écrivez les différentes propriétés que vous pensez importantes pour évaluer les différentes alternatives. Choisissez 2 à 5 propriétés de comparaison les plus importantes.
* Gardez la dernière ligne pour le résumé. Il n'y a pas de solution meilleure/pire, concentrez-vous sur la raison pour laquelle chaque alternative résout le problème.

### « Que devriez-vous croire pour choisir cette approche ? »

Par exemple, supposons que nous avons un problème qui peut être résolu de deux manières. L'une est [S.O.L.I.D](https://en.wikipedia.org/wiki/SOLID) et l'autre est plus bricolée. Certains pourraient dire que nous devrions toujours utiliser une solution S.O.L.I.D, quelles que soient les circonstances. Cela signifie-t-il que quiconque utilise du code bricolé est un mauvais développeur ? J'en doute.

Mettons les alternatives dans un tableau :

![Image](https://cdn-media-1.freecodecamp.org/images/X3S5prczYyEXy32GLl6iID3nPJ1yqrK18z4O)

Après avoir composé ce tableau, nous pouvons nous concentrer sur la ligne du bas et la lier directement à notre objectif.

Un exemple de cas pour « livrer le plus rapidement possible, et nous sommes d'accord pour compromettre la qualité future » pourrait être :

* Un bug grave qui existe dans le système. Chaque jour qui passe sans solution peut causer des dommages à long terme.
* Nous avons un contrat avec un client pour livrer la solution à une date spécifique. Si nous manquons la date limite, il peut y avoir des conséquences légales.
* L'entreprise a des problèmes de trésorerie. Livrer la solution tôt peut avoir un énorme impact sur la stabilité de notre entreprise.

Comme vous pouvez le voir, utiliser S.O.L.I.D n'est pas toujours la meilleure approche. Si nous nous soucions de la qualité du code, nous devrions définitivement l'utiliser par défaut, mais nous devons nous assurer que nous connaissons les compromis. Choisissez une solution plutôt qu'une autre parce que vous croyez que c'est le meilleur chemin pour atteindre vos objectifs. Ne le faites pas simplement parce que [Uncle Bob](https://blog.cleancoder.com/) ou quelqu'un dans votre entreprise a dit que c'était mieux.

### Ne faites pas de revues uniquement pour obtenir le « tampon »

![Image](https://cdn-media-1.freecodecamp.org/images/sfygBlLlFvenZwXI2tSWo06x7eoAbkYSxpzD)
_Photo par [Unsplash](https://unsplash.com/photos/hgITU7cj7k8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Hello Lightbulb</a> sur <a href="https://unsplash.com/search/photos/stamp?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Dans de nombreuses entreprises, les revues (revues de conception, revues de produit, etc.) suivent le même rituel. Le propriétaire de la fonctionnalité écrit la spécification. Leur manager la révise ensuite. Le groupe planifie une réunion pour examiner la spécification. Plus d'une fois, il y a un sentiment que le but de ces réunions est d'obtenir le tampon des parties prenantes plutôt que de s'engager réellement dans une discussion ouverte. Les raisons pour lesquelles cela peut se produire :

* Si vous avez déjà une spécification prête, pourquoi auriez-vous besoin de 7 personnes ou plus pour se réunir dans une salle et « passer en revue » ?
* Les réunions tendent à être ennuyeuses et peuvent devenir un monologue lorsque le propriétaire de la fonctionnalité lit la spécification qu'il a écrite.
* Parfois, ces réunions tendent à être pointilleuses. La conversation peut se concentrer sur des choses qui ne sont pas cruciales pour le succès de la fonctionnalité (« pourquoi utilisons-nous int32 et non int16 ? », « chaînes ou énumérations ? », « tabulations ou espaces ? »).
* Certaines personnes sont plus introverties que d'autres. Toutes les voix sont-elles entendues, ou n'y a-t-il que quelques personnes qui participent à la conversation ?
* La conversation sur certains détails peut prendre plus de temps que prévu. Le temps s'épuise alors avant que le propriétaire de la fonctionnalité ne puisse couvrir toute la spécification, parfois même moins de la moitié. Cela peut être frustrant. De plus, si une réunion de suivi est nécessaire, cela peut également retarder la prise de décision et le calendrier du projet.

### Soyez préparé avec des alternatives et des objectifs, pas avec la solution

Dans mon entreprise actuelle, nous adoptons une approche différente. Les revues sont faites hors ligne, en utilisant [Paper](https://paper.dropbox.com/) (bénéficiant de ses fonctionnalités comme le partage, les commentaires, les tâches qui rendent la collaboration plus efficace). Tout autre éditeur en ligne peut fonctionner.

Pour les réunions de conception, nous utilisons un modèle différent. Le décideur choisit les 3 à 4 questions ouvertes les plus importantes qui sont critiques pour le succès de la fonctionnalité. Ils composent ensuite un tableau d'alternatives comme nous l'avons vu précédemment. Ils peuvent également recommander une alternative, mais ne devraient pas être très opinés à ce sujet. Le but de la réunion **est** de choisir l'approche appropriée en fonction des objectifs du projet.

La réunion passe alors d'un monologue axé sur le « tamponnage » d'une solution à une conversation ouverte sur la meilleure approche. Le public passe d'approbateurs à conseillers. Le propriétaire de la fonctionnalité n'a pas besoin de « défendre » sa solution sélectionnée. Il devient un décideur qui base sa solution sur les conseils des parties prenantes. En fixant un temps (10 à 15 min) pour chaque question, vous pouvez vous assurer de couvrir toutes les questions ouvertes. Une décision est prise par le propriétaire de la fonctionnalité lorsque le temps est écoulé.

S'assurer que la voix de chacun est entendue, même celle des introvertis, est aussi simple que « Hé Jane, nous n'avons pas entendu ton opinion, quelle option penses-tu servira nos objectifs ? X, Y ou Z ? »

Alors, la prochaine fois que vous voulez comparer deux alternatives ou plus, remplacez « React.js est mieux qu'Angular » par « React.js est plus facile à apprendre, plus flexible et est mis à jour plus fréquemment, donc si nous visons à former rapidement de nouveaux ingénieurs et à avancer plus vite avec les technologies les plus récentes, ce devrait être notre choix entre ces deux-là ».

Quant à « L'ananas est la pire garniture de pizza » — peut-être que certaines choses ne sont pas destinées à avoir des alternatives. ?

Merci d'avoir consacré 4 minutes de votre temps, à la prochaine.

-Alon

_Remerciements spéciaux à :_

* _Eric Suh qui a dirigé la création du processus de revue d'ingénierie chez Dropbox_
* _Pierpaolo Baccichet, Steve Eisner, Gal Zellermayer, James Cowling et Devdatta Akhawe, tous ceux qui ont donné des commentaires précieux, à la fois en tant que premiers testeurs du processus et en tant que réviseurs_
* [Rina Artstain](https://www.freecodecamp.org/news/how-to-make-effective-decisions-by-comparing-alternatives-99ab7d4388bb/undefined) & [Keren](https://www.freecodecamp.org/news/how-to-make-effective-decisions-by-comparing-alternatives-99ab7d4388bb/undefined) _pour la relecture, la révision de cet article et les excellents commentaires techniques_