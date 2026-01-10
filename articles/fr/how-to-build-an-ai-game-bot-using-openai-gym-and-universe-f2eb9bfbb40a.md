---
title: 'Jour 22 : Comment construire un bot de jeu IA en utilisant OpenAI Gym et Universe'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T15:54:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-ai-game-bot-using-openai-gym-and-universe-f2eb9bfbb40a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hyjwsHNsORWJngVh5uKx8g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: bots
  slug: bots
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: 'Jour 22 : Comment construire un bot de jeu IA en utilisant OpenAI Gym
  et Universe'
seo_desc: 'By Harini Janakiraman

  Let’s face it, AI is everywhere. A face-off battle is unfolding between Elon Musk
  and Mark Zuckerberg on the future of AI. There are some that demonize it. And some
  whose utopian views claim that AI could almost be God-like in h...'
---

Par Harini Janakiraman

Admettons-le, l'IA est partout. Une [bataille d'opinions](https://www.recode.net/2017/7/25/16026184/mark-zuckerberg-artificial-intelligence-elon-musk-ai-argument-twitter) se déroule entre Elon Musk et Mark Zuckerberg sur l'avenir de l'IA. Certains la démonisent. D'autres, avec des vues utopiques, affirment que l'IA pourrait presque être divine en aidant l'humanité. Peu importe de quel côté penchent vos opinions, l'IA est là pour rester.

> « Avec l'intelligence artificielle, nous invoquons le démon. » — Elon Musk

> « Craindre une montée de robots tueurs, c'est comme s'inquiéter de la surpopulation sur Mars. » — Andrew Ng

Si vous êtes excité à l'idée de plonger directement dans l'IA et de bricoler avec, alors les jeux sont un excellent point de départ. Ils ont été le banc d'essai de prédilection pour l'IA. Mais avant de vous lancer, voici un peu d'histoire sur la façon dont la programmation de jeux a évolué au fil du temps.

### L'Histoire de la Programmation de Jeux

Les programmeurs de jeux utilisaient des décisions heuristiques de type si-alors-sinon pour faire des suppositions éclairées. Nous avons vu cela dans les premiers jeux vidéo d'arcade comme Pong et PacMan. Cette tendance a été la norme pendant très longtemps. Mais les développeurs de jeux ne peuvent prédire qu'un nombre limité de scénarios et de cas particuliers pour que votre bot ne tourne pas en rond !

Les développeurs de jeux ont ensuite tenté d'imiter la façon dont les humains joueraient à un jeu, et ont modélisé l'intelligence humaine dans un bot de jeu.

L'équipe de DeepMind a fait cela en généralisant et en modélisant l'intelligence pour résoudre n'importe quel jeu Atari qui lui était présenté. Le bot de jeu utilisait des réseaux de neurones d'apprentissage profond qui n'auraient aucune connaissance spécifique au jeu. Ils battaient le jeu en fonction des pixels qu'ils voyaient à l'écran et de leur connaissance des commandes du jeu. Cependant, certaines parties de DeepMind ne sont toujours pas open-source car Google les utilise pour battre la concurrence.

### La Démocratisation de l'IA

Pour éviter de concentrer le pouvoir incroyable de l'IA entre les mains de quelques-uns, Elon Musk a fondé [OpenAI](https://openai.com/). Il cherche à démocratiser l'IA en la rendant accessible à tous. Aujourd'hui, nous allons explorer OpenAI Gym et l'Univers récemment publié, qui est construit sur Gym.

[OpenAI Gym](https://gym.openai.com/) fournit une interface simple pour interagir avec et gérer n'importe quel environnement dynamique arbitraire. [OpenAI Universe](https://universe.openai.com/) est une plateforme qui vous permet de construire un bot et de le tester.

Il existe des milliers d'environnements. Ils vont des jeux Atari classiques, Minecraft, et Grand Theft Auto, aux [simulations de repliement de protéines](https://fold.it/portal/) qui peuvent guérir le cancer. Vous pouvez créer un bot et le faire fonctionner dans n'importe quel environnement en utilisant seulement quelques lignes de code Python. C'est trop génial pour ne pas essayer !

### Projet (1 Heure)

Nous allons construire un bot de jeu IA qui utilise la technique de l'Apprentissage par Renforcement. Je vous expliquerai cela plus tard. Il jouera de manière autonome et battra le jeu Atari Neon Race Car (vous pouvez sélectionner n'importe quel jeu que vous voulez). Nous construirons ce bot de jeu en utilisant les bibliothèques Gym et Universe d'OpenAI.

#### Étape 1 : Installation

Assurez-vous d'avoir Python installé, ou installez-le en utilisant Homebrew. Vous pouvez télécharger un IDE Python dédié comme PyCharm ou iPython notebook. J'aime garder les choses simples et utiliser Sublime. Enfin, installez Gym, Universe et les autres bibliothèques requises en utilisant pip.

```
// Installer python en utilisant brew
brew install python3
// Installer les bibliothèques OpenAI requises
pip3 install gym
pip3 install numpy incremental
brew install golang libjpeg-turbo
pip install universe
```

Tout dans Universe (les environnements) s'exécute comme des conteneurs à l'intérieur de Docker. Au cas où vous ne l'auriez pas déjà, installez et exécutez Docker depuis [ici](https://docs.docker.com/docker-for-mac/).

#### Étape 2 : Coder le Bot de Jeu

Le bot de jeu est codé en Python, donc nous commençons par importer les deux seules dépendances nécessaires : Gym et Universe.

```
import gym
import universe
```

Pour ce bot de jeu, utilisons mon jeu d'enfance préféré, Neon Race Cars, comme environnement de test. Vous pouvez trouver une liste complète d'autres environnements/jeux parmi lesquels choisir [ici](https://universe.openai.com/envs).

Universe vous permet d'exécuter autant d'environnements que vous le souhaitez en parallèle. Mais pour ce projet, nous n'en utiliserons qu'un seul.

```
env = gym.make('flashgames.NeonRace-v0')
env.configure(remotes=1) # crée un conteneur docker local
```

#### **Apprentissage par Renforcement**

Maintenant, nous ajoutons la logique du bot de jeu qui utilise la technique d'apprentissage par renforcement. Cette technique observe l'état précédent du jeu et la récompense (comme les pixels vus à l'écran ou le score du jeu). Elle propose ensuite une action à effectuer sur l'environnement.

Le but est de rendre son observation suivante meilleure (dans notre cas — maximiser le score du jeu). Cette action est choisie et effectuée par un agent (Bot de Jeu) dans l'intention de maximiser le score. Elle est ensuite appliquée sur l'environnement. L'environnement enregistre l'état résultant et la récompense en fonction de si l'action était bénéfique ou non (a-t-elle gagné le jeu ?).

![Image](https://cdn-media-1.freecodecamp.org/images/Ca1muYeNrBcXtwx9qzvPtzD6Quq-63T4b45I)

Maintenant, nous pouvons récupérer la liste des observations pour chaque environnement initialisé en utilisant la méthode env.reset().

```
observation_n = env.reset()
```

L'observation ici est un objet spécifique à l'environnement. Il représente ce qui a été observé, comme les données brutes des pixels à l'écran ou le statut/le score du jeu.

L'étape suivante consiste à créer un agent de jeu en utilisant une boucle infinie, qui effectue continuellement une action basée sur l'observation. Dans notre bot, définissons une seule action consistant à appuyer répétitivement sur la flèche vers le haut (Bot stupide ! N'hésitez pas à l'améliorer en un bot complexe...). L'action ici est définie par le type d'événement (KeyEvent), la touche de contrôle (Flèche Haut), et la définir à vrai pour toutes les observations que l'agent voit.

```
while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
```

Nous utilisons ensuite la méthode `env.step()` pour utiliser l'action afin d'avancer d'une étape de temps. Il s'agit d'une implémentation très basique de l'apprentissage renforcé.

```
observation_n, reward_n, done_n, info = env.step(action_n)
```

La méthode step ici retourne quatre variables :

1. `observation_n` : Observations de l'environnement
2. `reward_n` : Si votre action était bénéfique ou non : +1/-1
3. `done_n` : Indique si le jeu est terminé ou non : Oui/Non
4. `info` : Informations supplémentaires telles que la performance et la latence à des fins de débogage

Vous pouvez exécuter cette action simultanément pour tous les environnements dans lesquels vous entraînez votre bot. Utilisez la méthode env.render() pour démarrer le bot.

```
env.render()
```

Maintenant, vous avez le bot de jeu prêt à rivaliser avec l'environnement. Le code complet pour ce bot basique ainsi qu'une version avancée est disponible dans mon dépôt Github [ici](https://github.com/harinij/100DaysOfCode/tree/master/Day%20022%20-%20AI%20GameBot%20using%20Universe).

#### **Étape 3 : Exécuter le Bot de Jeu**

Maintenant, la partie amusante : assurez-vous que Docker est en cours d'exécution et lancez le bot. Voyez-le en action en battant d'autres voitures ou en échouant à le faire. S'il échoue, continuez à ajuster votre bot pour qu'il batte l'intelligence !

```
python gamebot.py
```

![Image](https://cdn-media-1.freecodecamp.org/images/6lGP8Q22XzPi5aSnBcKidzRyP-AkplbGZHuo)

![Image](https://cdn-media-1.freecodecamp.org/images/deBMJ8LmSX5uZuZyQ2FkAZi4DJC7iKdiQCTx)
_Crash et burrrn ! #Basique_

Continuez à bricoler avec l'IA et vous pourrez éventuellement débloquer le Mode Dieu ! #100DaysOfCode

![Image](https://cdn-media-1.freecodecamp.org/images/EbRss6eo08UYIvzBcLMVjRrjoh0q0a78D2yh)

_Si vous avez aimé cela, applaudissez **? s** afin que d'autres puissent le voir également ! Suivez-moi sur Twitter @[H**ariniLabs**](https://twitter.com/harinilabs) ou M[**edium**](https://medium.com/@harinilabs) pour obtenir les dernières mises à jour sur d'autres histoires ou simplement pour dire Bonjour :)_

_PS : Inscrivez-vous à ma newsletter [**ici**](http://harinilabs.com/womenintech.html) pour être le premier à recevoir du nouveau contenu et elle est remplie d'une dose d'inspiration du monde de #[**WomenInTech**](http://harinilabs.com/womenintech.html) et oui, les hommes peuvent aussi s'inscrire !_