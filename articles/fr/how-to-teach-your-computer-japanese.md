---
title: Comment entraîner un classificateur d'images et apprendre l'ordinateur à lire
  le japonais
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-21T16:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-teach-your-computer-japanese
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/kmnist.png
tags:
- name: AI
  slug: ai
- name: algorithms
  slug: algorithms
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Computer Vision
  slug: computer-vision
- name: Deep Learning
  slug: deep-learning
- name: 'fastai, '
  slug: fastai
- name: Machine Learning
  slug: machine-learning
seo_title: Comment entraîner un classificateur d'images et apprendre l'ordinateur
  à lire le japonais
seo_desc: 'By Ajay Uppili Arasanipalai

  Introduction

  Hi. Hello. こんにちは

  Those squiggly characters you just saw are from a language called Japanese. You’ve
  probably heard of it if you’ve ever watched Dragon Ball Z.


  _Source_

  Here’s the problem though: you know thos...'
---

Par Ajay Uppili Arasanipalai

## Introduction

Bonjour. Salut. F30E

Ces caractères sinueux que vous venez de voir proviennent d'une langue appelée japonais. Vous en avez probablement entendu parler si vous avez déjà regardé Dragon Ball Z.

![Image](https://assets.website-files.com/5ac6b7f2924c652fd013a891/5d2951d9e7d17d10d2b65c0b_100881-dragon-ball-z-dragon-ball-fight.gif)
_<a data-w-id="12ba22ef-4763-8b29-10e7-8485aca3fe22" href="http://fanaru.com/dragon-ball-z/image/100881-dragon-ball-z-dragon-ball-fight.gif" target="_blank" data-rt-link-type="external">Source</a>_

Voici le problème : vous connaissez ces anciens parchemins japonais qui vous donnent l'air de pouvoir déclencher une attaque ultime de seigneur samouraï ninja.

Oui, ceux-là. Je ne peux pas exactement les lire, et il s'avère que très peu de gens le peuvent.

Heureusement, un groupe de personnes intelligentes comprend à quel point il est important que je maîtrise le Bijudama-Rasenshuriken, alors ils ont inventé une chose appelée l'apprentissage profond.

Alors préparez vos ramen et soyez prêts. Dans cet article, je vais vous montrer comment entraîner un réseau de neurones qui peut prédire avec précision les caractères japonais à partir de leurs images.

Pour garantir que nous obtenons de bons résultats, je vais utiliser une bibliothèque d'apprentissage profond incroyable appelée fastAI, qui est un wrapper autour de PyTorch qui facilite la mise en œuvre des meilleures pratiques de la recherche moderne. Vous pouvez en lire plus sur leur [documentation](https://docs.fast.ai).

Cela dit, commençons.

## KMNIST

D'accord, donc avant de pouvoir créer des sous-titres d'anime, nous allons avoir besoin d'un ensemble de données. Aujourd'hui, nous allons nous concentrer sur KMNIST.

Cet ensemble de données prend des exemples de caractères du script japonais Kuzushiji, et les organise en 10 classes étiquetées. Les images mesurent 28x28 pixels, et il y a 70 000 images au total, reflétant la structure de MNIST.

Mais pourquoi KMNIST ? Eh bien, premièrement, il a "MNIST" dans son nom, et nous savons tous à quel point les gens en apprentissage automatique adorent MNIST.

![Image](https://assets.website-files.com/5ac6b7f2924c652fd013a891/5d2951dabfaf722c2f74abc4_kmnist.png)
_<a data-w-id="e984a878-5844-3c91-d6c5-b8abca1100d6" href="http://codh.rois.ac.jp/img/kmnist.png" target="_blank" data-rt-link-type="external">Source</a>_

Donc, en théorie, vous pourriez simplement changer quelques lignes de ce code Keras que vous avez copié-collé depuis Stack Overflow et BOOM ! Vous avez maintenant du code informatique qui peut [ressusciter un ancien script japonais](https://www.wandb.com/articles/collaborative-deep-learning-for-reading-japanese).

Bien sûr, en pratique, ce n'est pas si simple. Pour commencer, le petit modèle mignon que vous avez entraîné sur MNIST ne fonctionnera probablement pas aussi bien. Parce que, vous savez, déterminer si un nombre est un 2 ou un 5 est juste un peu plus facile que de déchiffrer un script cursif oublié que seule une poignée de personnes sur terre sait lire.

![GIF animé montrant](https://assets.website-files.com/5ac6b7f2924c652fd013a891/5d2951d9e7d17dd802b65c0c_giphy.gif)

En dehors de cela, je suppose que je devrais souligner que Kuzushiji, qui est ce que le "K" dans KMNIST représente, ne fait pas seulement 10 caractères de long. Malheureusement, je ne fais **PAS** partie de la poignée d'experts qui peuvent lire la langue, donc je ne peux pas décrire en détail comment cela fonctionne.

Mais voici ce que je sais : il y a en fait trois variantes de ces ensembles de données de caractères Kuzushiji — KMNIST, Kuzushiji-49 et Kuzushiji-Kanji.

Kuzushiji-49 est une variante avec 49 classes au lieu de 10. Kuzushiji-Kanji est encore plus fou, avec un nombre impressionnant de 3832 classes.

Oui, vous avez bien lu. C'est trois fois plus de classes qu'ImageNet.

## Comment ne pas gâcher votre ensemble de données

Pour garder les choses aussi proches que possible de MNIST, il semble que les chercheurs qui ont publié l'ensemble de données KMNIST l'ont gardé dans le format original (man, ils ont vraiment pris cette histoire de MNIST à cœur, n'est-ce pas).

Si vous jetez un coup d'œil au [dépôt GitHub KMNIST](https://github.com/rois-codh/kmnist), vous verrez que l'ensemble de données est servi dans deux formats : la chose originale MNIST, et sous forme de plusieurs tableaux Numpy.

Bien sûr, je sais que vous étiez probablement trop paresseux pour cliquer sur ce lien. Alors voici. Vous pouvez me remercier plus tard.

![Capture d'écran GitHub montrant les divers formats de téléchargement pour l'ensemble de données KMNIST](https://assets.website-files.com/5ac6b7f2924c652fd013a891/5d2951da80b61183001c8a76_s_F44ECE835EEC7420BCA13A4D3C5E89A345A0759A53AF1A997CB55909898D5236_1561571516749_Screenshot%2B2019-06-26%2Bat%2B11.20.09%2BPM.png)
_<a data-w-id="918a6e10-931f-dc94-b89a-4e2c3a4135a5" href="https://github.com/rois-codh/kmnist" target="_blank" data-rt-link-type="external">Source</a>_

Personnellement, j'ai trouvé le format de tableau NumPy plus facile à utiliser avec fastai, mais le choix vous appartient. Si vous utilisez PyTorch, KMNIST est disponible gratuitement dans [`torchvision.datasets`](https://pytorch.org/docs/stable/torchvision/datasets.html?highlight=kmnist#kmnist).

Le prochain défi est d'obtenir ces coups de pinceau vieux de 10 000 ans sur votre notebook (ou IDE, qui suis-je pour juger). Heureusement, le dépôt GitHub mentionne qu'il y a ce script pratique appelé `download_data.py` qui fera tout le travail pour nous. Youpi !

![party popper](https://paper.dropboxstatic.com/static/img/ace/emoji/1f389.png?version=3.1.2)

À partir de là, cela va probablement devenir gênant si je continue à parler de la façon de pré-traiter vos données sans code réel. Alors consultez [le notebook](https://colab.research.google.com/gist/iyaja/fe102ae34312e48e637edd804a450207/kmnist.ipynb) si vous voulez approfondir.

Passons à la suite...

## Devrais-je utiliser un hyper ultra Inception ResNet XXXL ?

### Réponse courte

Probablement pas. Un ResNet régulier devrait suffire.

### Une réponse un peu moins courte

D'accord, écoutez. À ce stade, vous pensez probablement : "KMNIST est grand. KMNIST est difficile. J'ai besoin d'utiliser un modèle très nouveau, très sophistiqué."

Ai-je trop forcé la voix de Bizzaro ?

Le point est, vous **N'AVEZ PAS** besoin d'un nouveau modèle brillant pour bien performer sur ces tâches de classification d'images. Au mieux, vous obtiendrez probablement une amélioration marginale de la précision au coût d'un temps et d'un argent considérables.

La plupart du temps, vous allez simplement gaspiller beaucoup de temps et d'argent.

Alors écoutez mon conseil — restez avec les bons vieux ResNets. Ils fonctionnent vraiment bien, ils sont relativement rapides et légers (comparés à certains autres gouffres de mémoire comme Inception et DenseNet), et surtout, les gens les utilisent depuis un moment, donc ce ne devrait pas être trop difficile de les ajuster.

Si l'ensemble de données sur lequel vous travaillez est simple comme MNIST, utilisez ResNet18. Si c'est de difficulté moyenne, comme CIFAR10, utilisez ResNet34. Si c'est vraiment difficile, comme ImageNet, utilisez ResNet50. Si c'est plus difficile que cela, vous pouvez probablement vous permettre d'utiliser quelque chose de mieux qu'un ResNet.

Vous ne me croyez pas ? Consultez ma première entrée pour la compétition Stanford DAWNBench d'avril 2019 :

![Image](https://assets.website-files.com/5ac6b7f2924c652fd013a891/5d2951dae06d1bb7f8a731ba_s_F44ECE835EEC7420BCA13A4D3C5E89A345A0759A53AF1A997CB55909898D5236_1561651063683_D4s0U9_UwAA3vk2.png)

Qu'est-ce que vous voyez ? Des ResNets partout ! Alors, il doit y avoir une raison à cela.

## Hyperparamètres à gogo

Il y a quelques mois, j'ai écrit un article sur [comment choisir les bons hyperparamètres](https://blog.nanonets.com/hyperparameter-optimization/). Si vous êtes intéressé par une solution plus générale à cette tâche herculéenne, allez voir cela. Ici, je vais vous guider à travers mon processus de choix de bons hyperparamètres pour obtenir de bons résultats sur KMNIST.

Pour commencer, passons en revue les hyperparamètres que nous devons ajuster.

Nous avons déjà décidé d'utiliser un ResNet34, donc c'est réglé. Nous n'avons pas besoin de déterminer le nombre de couches, la taille des filtres, le nombre de filtres, etc., car cela est intégré dans notre modèle.

Vous voyez, je vous avais dit que cela ferait gagner du temps.

Donc, ce qui reste est le grand trio : le taux d'apprentissage, la taille du lot et le nombre d'époques (plus des choses comme la probabilité de dropout pour lesquelles nous pouvons simplement utiliser les valeurs par défaut).

Passons-les en revue un par un.

### Nombre d'époques

Commençons par le nombre d'époques. Comme vous le verrez lorsque vous jouerez avec le modèle dans le notebook, notre entraînement est assez efficace. Nous pouvons facilement dépasser 90 % de précision en quelques minutes.

![Image](https://assets.website-files.com/5ac6b7f2924c652fd013a891/5d2955a222d8c93af99209f9_Screenshot%202019-07-13%20at%209.23.20%20AM.png)

Étant donné que notre entraînement est si rapide dès le départ, il semble extrêmement improbable que nous utilisions trop d'époques et surajustions. J'ai vu d'autres modèles KMNIST s'entraîner pendant plus de 50 époques sans aucun problème, donc rester dans la plage 0-30 devrait être absolument correct.

Cela signifie que dans le cadre des restrictions que nous avons imposées au modèle en termes d'époques, plus il y en a, mieux c'est. Dans mes expériences, j'ai trouvé que 10 époques offrent un bon équilibre entre la précision du modèle et le temps d'entraînement.

### Taux d'apprentissage

Ce que je vais dire va énerver beaucoup de gens. Mais je vais le dire quand même — nous n'avons pas besoin de prêter trop d'attention au taux d'apprentissage.

Oui, vous avez bien entendu. Mais donnez-moi une chance de m'expliquer.

Au lieu de dire "Hmm... cela ne semble pas fonctionner, essayons à nouveau avec lr=3e-3", nous allons utiliser une approche beaucoup plus systématique et disciplinée pour trouver un bon taux d'apprentissage.

Nous allons utiliser le chercheur de taux d'apprentissage, une idée révolutionnaire proposée par Leslie Smith dans son [article sur les taux d'apprentissage cycliques](https://arxiv.org/pdf/1506.01186.pdf).

Voici comment cela fonctionne :

* Tout d'abord, nous configurons notre modèle et nous préparons à l'entraîner pour une époque. Au fur et à mesure que le modèle s'entraîne, nous allons augmenter progressivement le taux d'apprentissage.
* En cours de route, nous allons suivre la perte à chaque itération.
* Enfin, nous sélectionnons le taux d'apprentissage qui correspond à la perte la plus faible.

Lorsque tout est dit et fait, et que vous tracez la perte par rapport au taux d'apprentissage, vous devriez voir quelque chose comme ceci :

![Image](https://assets.website-files.com/5ac6b7f2924c652fd013a891/5d2951dabfaf72811274abb2_s_F44ECE835EEC7420BCA13A4D3C5E89A345A0759A53AF1A997CB55909898D5236_1561652469267_Unknown.png)

Maintenant, avant de vous exciter et de choisir 1e-01 comme taux d'apprentissage, je tiens à vous faire savoir que ce n'est **PAS** le meilleur choix.

C'est parce que fastai met en œuvre une technique de lissage appelée moyennes pondérées exponentiellement, qui est la version du chercheur en apprentissage profond d'un filtre Instagram. Cela empêche nos graphiques de ressembler au résultat de donner trop de temps à l'enfant de vos voisins avec un crayon bleu.

![Image](https://assets.website-files.com/5ac6b7f2924c652fd013a891/5d2951dae06d1b5fb4a731bb_art2_loss_vs_lr.png)

Puisque nous utilisons une forme de moyenne pour rendre le graphique lisse, le point "minimum" que vous regardez sur le chercheur de taux d'apprentissage n'est pas réellement un minimum. C'est une moyenne.

Au lieu de cela, pour trouver le taux d'apprentissage, une bonne règle de base est de choisir le taux d'apprentissage qui est d'un ordre de grandeur inférieur au point minimum sur le graphique lissé. Cela fonctionne généralement très bien en pratique.

Je comprends que tout ce traçage et cette moyenne peuvent sembler étranges si vous avez toujours forcé les valeurs du taux d'apprentissage toute votre vie. Je vous conseille donc de consulter [l'explication de Sylvain Gugger sur le chercheur de taux d'apprentissage](https://sgugger.github.io/how-do-you-find-a-good-learning-rate.html) pour en savoir plus.

### Taille du lot

D'accord, vous m'avez pris la main dans le sac ici. Mes expériences initiales ont utilisé une taille de lot de 128 puisque c'est ce que la meilleure soumission a utilisé.

Je sais, je sais. Pas très créatif. Mais c'est ce que j'ai fait. Ensuite, j'ai expérimenté avec quelques autres tailles de lot, et je n'ai pas pu obtenir de meilleurs résultats. Donc 128 c'est !

En général, les tailles de lot peuvent être une chose étrange à optimiser, car cela dépend partiellement de l'ordinateur que vous utilisez. Si vous avez un GPU avec plus de VRAM, vous pouvez entraîner sur des tailles de lot plus grandes.

Donc si je vous dis d'utiliser une taille de lot de 2048, par exemple, au lieu d'obtenir cette place convoitée en haut de Kaggle et la gloire éternelle pour la vie, vous pourriez simplement obtenir une erreur CUDA : mémoire insuffisante.

Il est donc difficile de recommander une taille de lot parfaite car, en pratique, il y a clairement des limites computationnelles. La meilleure façon de la choisir est d'essayer des valeurs qui fonctionnent pour vous.

Mais comment choisir un nombre aléatoire dans la vaste mer des entiers positifs ?

Eh bien, vous ne le faites pas. Puisque la mémoire GPU est organisée en bits, il est bon de choisir une taille de lot qui est une puissance de 2 pour que vos mini-lots s'adaptent parfaitement en mémoire.

Voici ce que je ferais : commencez avec une taille de lot modérément grande comme 512. Ensuite, si vous trouvez que votre modèle commence à agir bizarrement et que la perte n'est pas sur une tendance clairement à la baisse, divisez-la par deux. Ensuite, répétez le processus d'entraînement avec une taille de lot de 256, et voyez si cela se comporte cette fois-ci.

Si ce n'est pas le cas, lavez, rincez et répétez.

## Quelques belles images

Avec les optimisations en cours ici, il sera assez difficile de suivre ce grand désordre de modèles, de métriques et d'hyperparamètres que nous avons créés.

Pour nous assurer que nous restons tous des êtres humains sains d'esprit tout en gravissant la montagne de la précision, nous allons utiliser [l'intégration wandb + fastai](https://docs.wandb.com/docs/frameworks/fastai.html).

Alors, que fait réellement wandb ?

Il suit un grand nombre de statistiques sur votre modèle et ses performances automatiquement. Mais ce qui est vraiment cool, c'est qu'il fournit également des graphiques et des visualisations instantanés pour suivre les métriques critiques comme la précision et la perte, le tout en temps réel !

Si cela ne suffisait pas, il stocke également tous ces graphiques, visualisations et statistiques dans le cloud, afin que vous puissiez y accéder à tout moment et n'importe où.

Vos jours de démarrage sur un écran de terminal noir et de bidouillage avec matplotlib sont révolus.

[Le tutoriel notebook](https://colab.research.google.com/gist/iyaja/fe102ae34312e48e637edd804a450207/kmnist.ipynb) pour cet article propose une introduction simple à son fonctionnement en harmonie avec fastai. Vous pouvez également consulter [l'espace de travail wandb](https://app.wandb.ai/ajayuppili/kmnist/runs/41gbr2yx), où vous pouvez jeter un coup d'œil à tout ce dont j'ai parlé sans écrire de code.

## Conclusion

F30E

Cela signifie "c'est la fin".

Mais vous n'aviez pas besoin que je vous le dise, n'est-ce pas ? Pas après avoir pris la peine d'obtenir un ensemble de données de caractères japonais, d'utiliser le chercheur de taux d'apprentissage, d'entraîner un ResNet en utilisant les meilleures pratiques modernes, et de regarder votre modèle s'élever vers la gloire en utilisant la surveillance en temps réel dans le cloud.

Oui, en environ 20 minutes, vous avez réellement fait tout cela ! Donnez-vous une tape dans le dos.

Et s'il vous plaît, allez regarder un peu de Dragonball.