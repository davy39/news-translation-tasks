---
title: 'Les Réseaux de Neurones pour les Nuls : une introduction rapide à ce domaine
  fascinant'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-30T17:16:24.000Z'
originalURL: https://freecodecamp.org/news/neural-networks-for-dummies-a-quick-intro-to-this-fascinating-field-795b1705104a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_j9oKKsbiCW9BnID.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: beginner
  slug: beginner
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
seo_title: 'Les Réseaux de Neurones pour les Nuls : une introduction rapide à ce domaine
  fascinant'
seo_desc: 'By Dalya Gartzman

  Have you ever wondered what are all these neural networks that everyone is talking
  about, and were too afraid to ask? Well, fear no more! By the end of this post you’ll
  be able to walk into any conference and dazzle the lunch table ...'
---

Par Dalya Gartzman

Vous êtes-vous déjà demandé ce que sont tous ces réseaux de neurones dont tout le monde parle, et avez-vous eu trop peur de demander ? Eh bien, n'ayez plus peur ! À la fin de cet article, vous pourrez entrer dans n'importe quelle conférence et impressionner la table du déjeuner avec vos nouveaux mots à la mode nouvellement acquis !

Si vous avez ouvert votre navigateur au cours des dernières années, vous devez avoir vu l'expression « Réseaux de Neurones » à quelques (centaines) de reprises.

Dans cette courte lecture, je vais vous donner un peu de contexte sur le domaine et sur la chose elle-même. Vous ne deviendrez pas l'expert mondial du domaine dans les 5 prochaines minutes, mais vous passerez l'étape non triviale d'intégration. Vous apprendrez également quelques mots à la mode pour impressionner la famille à la table du dîner, surtout si vous suivez la liste de lecture à la fin.

### Qu'est-ce que l'Apprentissage Automatique ?

Pour comprendre les Réseaux de Neurones, nous devons d'abord comprendre l'Apprentissage Automatique. Et pour comprendre l'Apprentissage Automatique, parlons d'abord de l'Apprentissage Humain, ou de la « programmation classique ».

Dans la programmation classique, moi, le développeur, je dois comprendre les aspects du problème que j'essaie de résoudre, et connaître exactement toutes les règles pour parvenir à la solution.

Par exemple, disons que je veux que mon programme sache faire la différence entre un carré et un cercle. Alors une façon de le gérer est d'écrire un programme qui peut détecter les coins, puis de l'appliquer pour compter les coins. Si mon programme voit 4 coins, alors cette forme est un carré, et s'il n'en voit aucun, alors cette forme est un cercle.

Et l'Apprentissage Automatique ? **Très généralement parlant, l'Apprentissage Automatique = apprendre à partir d'exemples.**

Dans l'Apprentissage Automatique, face au même problème de distinguer les cercles et les carrés, nous concevrions un système d'apprentissage qui prendrait en entrée de nombreux exemples de formes et de leur classe (carré ou cercle). Nous espérerions que la machine apprenne par elle-même les propriétés qui les distinguent.

Et puis, mes amis, une fois que la machine a appris toutes ces propriétés, je peux lui donner une nouvelle image d'un cercle ou d'un carré, une qu'elle n'a jamais vue auparavant, et elle la classera, espérons-le, correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/TzDZm36n7DCAuD4YdHm-YzCxVA9qOdbvDOVc)

### Qu'est-ce qu'un Neurone ?

Un neurone, dans le contexte des Réseaux de Neurones, est un nom sophistiqué que les gens intelligents utilisent lorsqu'ils sont trop sophistiqués pour dire fonction. Une fonction, dans le contexte des mathématiques et de l'informatique, est un nom sophistiqué pour quelque chose qui prend une entrée, applique une logique et produit un résultat.

Plus précisément, un neurone peut être considéré comme une unité d'apprentissage.

Par conséquent, nous devons comprendre ce qu'est une unité d'apprentissage, dans le contexte de l'Apprentissage Automatique. Ensuite, nous comprendrons également le bloc de construction le plus basique d'un Réseau de Neurones, qui est le neurone.

Pour illustrer, disons que j'essaie de comprendre la relation entre le nombre de mots dans un article de blog et le nombre de mots que les gens lisent réellement dans cet article de blog. Souvenez-vous - nous sommes dans le domaine de l'Apprentissage Automatique, où nous apprenons à partir d'exemples.

Je collecte donc de nombreux exemples de nombre de mots dans des articles de blog, notés x, et combien de mots les gens lisent réellement dans ces articles, y, et j'imagine qu'il existe une certaine relation entre eux, notée f.

Cependant, l'astuce est que je dois simplement dire à la machine (le programme) à peu près quelle est la relation que je m'attends à voir (par exemple une ligne droite), et la machine comprendra la ligne réelle qu'elle doit tracer.

![Image](https://cdn-media-1.freecodecamp.org/images/cVa-MTHf7LBMontSsqooC9eUqw8DnDet-7Jy)

Qu'ai-je gagné ici ?

La prochaine fois que je veux écrire un article de blog qui contient x mots, la machine peut appliquer la relation f qu'elle a trouvée et me dire combien de mots je peux m'attendre à ce que les gens lisent réellement, y.

![Image](https://cdn-media-1.freecodecamp.org/images/emFUjxqiaaHdFNoui8lIcwJ6MXEQ8SqxwAS-)

### Donc, un Réseau de Neurones est...

Eh bien, si un neurone est une fonction, alors un Réseau de Neurones est un réseau de fonctions ! Cela signifie que nous avons de nombreuses (très nombreuses) fonctions de ce type, de telles unités d'apprentissage, et toutes leurs entrées et sorties sont entrelacées et s'alimentent les unes les autres.

En tant que concepteur de ce réseau, c'est à moi de répondre à certaines questions :

* Comment modéliser les entrées et les sorties ? (par exemple, si l'entrée est un texte, puis-je le modéliser en lettres ? [nombres](https://www.nltk.org/api/nltk.tokenize.html) ? [vecteurs](https://en.wikipedia.org/wiki/Word2vec) ?...)
* Quelles sont les fonctions dans chaque neurone ? (sont-elles linéaires ? [exponentielles](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6) ?...)
* Quelle est l'architecture du réseau ? (c'est-à-dire, quelle est la sortie de quelle fonction qui est l'entrée de quelle fonction ?)
* Quels sont les [mots à la mode](https://becominghuman.ai/cheat-sheets-for-ai-neural-networks-machine-learning-deep-learning-big-data-678c51b4b463) que je peux utiliser pour décrire mon réseau ?

Une fois que j'ai répondu à ces questions, je peux « montrer » au réseau de nombreux (très nombreux) exemples d'entrées et de sorties correctes, dans l'espoir que lorsque je lui « montrerai » une nouvelle entrée d'exemple qu'il n'a jamais vue auparavant, il saura donner la sortie correcte.

Comment ce processus d'apprentissage fonctionne est au-delà de la portée de cet article, mais pour en savoir plus, vous pouvez [regarder ceci](https://www.youtube.com/watch?v=ov_RkIJptwE). Vous pouvez également aller sur ce [Neural Network Playground](https://playground.tensorflow.org/) incroyablement cool pour mieux comprendre ce que cela signifie.

![Image](https://cdn-media-1.freecodecamp.org/images/v0kZcySrDQqyjcSIrWez1vzuqeUdQeOsMsYy)

### Réseaux de Neurones - L'Histoire sans Fin

Comme ce domaine est littéralement en explosion, la quantité de nouveau contenu (et de haute qualité !) qui sort chaque minute est impossible à suivre pour tout humain. (OMG, pensez-vous qu'il viendra un temps où les humains pourront construire une IA capable de suivre les avancées humaines dans le domaine de l'IA ?)

En entrant dans ce domaine, la première chose à savoir est que PERSONNE ne sait tout. Alors sentez-vous à l'aise là où vous êtes, et continuez à être curieux :)

Par conséquent, je veux que mes derniers mots dans cet article soient une référence à certaines de mes ressources préférées pour apprendre :

* [Gal Yona](https://www.freecodecamp.org/news/neural-networks-for-dummies-a-quick-intro-to-this-fascinating-field-795b1705104a/undefined) - l'une de mes blogueuses préférées dans le domaine. Ses articles vont des [explications techniques hard-core](https://towardsdatascience.com/do-gans-really-model-the-true-data-distribution-or-are-they-just-cleverly-fooling-us-d08df69f25eb) aux [revues semi-philosophiques](https://towardsdatascience.com/the-tale-of-1001-black-boxes-62d12b5886aa).
* [Siraj Raval](https://www.freecodecamp.org/news/neural-networks-for-dummies-a-quick-intro-to-this-fascinating-field-795b1705104a/undefined) - un [youtubeur](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A) avec une énorme collection de vidéos, allant des [explications théoriques](https://www.youtube.com/watch?v=xRJCOz3AfYY) aux [tutoriels pratiques](https://www.youtube.com/watch?v=pY9EwZ02sXU), tous super amusants aussi !
* [Christopher Olah](http://colah.github.io/) - un chercheur passionné et perspicace, tient un blog visuellement attrayant, avec des articles allant des [concepts de base](http://colah.github.io/posts/2015-09-Visual-Information/) aux [plongées profondes](https://distill.pub/2017/feature-visualization/).
* [Towards Data Science](https://towardsdatascience.com/) est la plus grande publication Medium spécifique au domaine, et ce que j'aime à son sujet, c'est que les éditeurs sont d'excellents curateurs. Chaque fois que vous avez quelques minutes/heures à perdre, allez simplement sur leur page d'accueil et commencez à explorer tout, des [outils pratiques](https://towardsdatascience.com/exploring-the-census-income-dataset-using-bubble-plot-cfa1b366313b) au [contenu algorithmique profond](https://towardsdatascience.com/https-medium-com-talperetz24-mastering-the-new-generation-of-gradient-boosting-db04062a7ea2).