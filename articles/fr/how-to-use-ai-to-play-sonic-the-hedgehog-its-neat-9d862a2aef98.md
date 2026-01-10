---
title: Comment utiliser l'IA pour jouer à Sonic the Hedgehog. C'est NEAT !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T16:28:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-ai-to-play-sonic-the-hedgehog-its-neat-9d862a2aef98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RYknGhjxRw8arZlI-_ib4A.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: gaming
  slug: gaming
- name: Machine Learning
  slug: machine-learning
- name: Reinforcement Learning
  slug: reinforcement-learning
- name: technology
  slug: technology
seo_title: Comment utiliser l'IA pour jouer à Sonic the Hedgehog. C'est NEAT !
seo_desc: 'By Vedant Gupta

  Generation after generation, humans have adapted to become more fit with our surroundings.
  We started off as primates living in a world of eat or be eaten. Eventually we evolved
  into who we are today, reflecting modern society. Throug...'
---

Par Vedant Gupta

Génération après génération, les humains se sont adaptés pour devenir plus aptes à vivre dans leur environnement. Nous avons commencé en tant que primates vivant dans un monde où il fallait manger ou être mangé. Finalement, nous avons évolué pour devenir qui nous sommes aujourd'hui, reflétant la société moderne. À travers le processus d'évolution, nous sommes devenus plus intelligents. Nous sommes capables de mieux travailler avec notre environnement et d'accomplir ce dont nous avons besoin.

Le concept d'apprentissage par l'évolution peut également être appliqué à l'Intelligence Artificielle. Nous pouvons entraîner des IA à effectuer certaines tâches en utilisant NEAT, Neuroevolution of Augmented Topologies. En termes simples, NEAT est un algorithme qui prend un ensemble d'IA (génomes) tentant d'accomplir une tâche donnée. Les IA les mieux performantes "se reproduisent" pour créer la génération suivante. Ce processus continue jusqu'à ce que nous ayons une génération capable de compléter ce dont elle a besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/kB3DscigQ-nDtQhS5em32jfdsFdAKp236CXt)
_Clip de l'IA jouant à STH_

NEAT est incroyable car il élimine le besoin de données préexistantes nécessaires pour entraîner nos IA. En utilisant la puissance de NEAT et OpenAI's Gym Retro, j'ai entraîné une IA à jouer à Sonic the Hedgehog pour la SEGA Genesis. Apprenons comment !

### Un réseau de neurones NEAT (Implémentation Python)

#### Dépôt GitHub

[**Vedant-Gupta523/sonicNEAT**](https://github.com/Vedant-Gupta523/sonicNEAT)  
[_Contribuez au développement de Vedant-Gupta523/sonicNEAT en créant un compte sur GitHub._github.com](https://github.com/Vedant-Gupta523/sonicNEAT)

**Note :** Tout le code dans cet article et le dépôt ci-dessus est une version légèrement modifiée des tutoriels YouTube de Lucas Thompson sur Sonic AI Bot Using Open-AI and NEAT [YouTube tutorials](https://www.freecodecamp.org/news/how-to-use-ai-to-play-sonic-the-hedgehog-its-neat-9d862a2aef98/Sonic%20AI%20Bot%20Using%20Open-AI%20and%20NEAT%20Tutorial) et [code](https://gitlab.com/lucasrthompson/Sonic-Bot-In-OpenAI-and-NEAT).

#### Comprendre OpenAI Gym

Si vous n'êtes pas déjà familier avec OpenAI Gym, parcourez la terminologie ci-dessous. Ces termes seront utilisés fréquemment tout au long de l'article.

**agent —** Le joueur IA. Dans ce cas, ce sera Sonic.

**environnement —** L'environnement complet de l'agent. L'environnement de jeu.

**action —** Quelque chose que l'agent a la possibilité de faire (c'est-à-dire aller à gauche, aller à droite, sauter, ne rien faire).

**step —** Effectuer 1 action.

**state —** Une frame de l'environnement. La situation actuelle dans laquelle se trouve l'IA.

**observation —** Ce que l'IA observe à partir de l'environnement.

**fitness —** À quel point notre IA performe bien.

**done —** Quand l'IA a complété sa tâche ou ne peut plus continuer.

#### Installer les dépendances

Ci-dessous se trouvent les liens GitHub pour OpenAI et NEAT avec les instructions d'installation.

**OpenAI** : [https://github.com/openai/retro](https://github.com/openai/retro)

**NEAT** : [https://github.com/CodeReclaimers/neat-python](https://github.com/CodeReclaimers/neat-python)

**Pip install** des bibliothèques telles que cv2, numpy, pickle, etc.

#### Importer les bibliothèques et définir l'environnement

Pour commencer, nous devons importer tous les modules que nous allons utiliser :

```py
import retro
import numpy as np
import cv2
import neat
import pickle
```

Nous allons également définir notre environnement, composé du jeu et de l'état :

```py
env = retro.make(game = "SonicTheHedgehog-Genesis", state = "GreenHillZone.Act1")
```

Pour entraîner une IA à jouer à Sonic the Hedgehog, vous aurez besoin du ROM du jeu (fichier de jeu). La manière la plus simple de l'obtenir est d'acheter le jeu sur [Steam](https://store.steampowered.com/app/71113/Sonic_The_Hedgehog/) pour 5 $. Vous pourriez également trouver des téléchargements gratuits du ROM en ligne, cependant c'est illégal, alors ne faites pas cela.

Dans le dépôt OpenAI à **retro/retro/data/stable/** vous trouverez un dossier pour Sonic the Hedgehog Genesis. Placez le ROM du jeu ici et assurez-vous qu'il est appelé rom.md. Ce dossier contient également des fichiers .state. Vous pouvez en choisir un et définir le paramètre state égal à celui-ci. J'ai choisi GreenHillZone Act 1 puisque c'est le tout premier niveau du jeu.

#### Comprendre data.json et scenario.json

Dans le dossier Sonic the Hedgehog, vous aurez ces deux fichiers :

**data.json**

```json
{
  "info": {
    "act": {
      "address": 16776721,
      "type": "|u1"
    },
    "level_end_bonus": {
      "address": 16775126,
      "type": "|u1"
    },
    "lives": {
      "address": 16776722,
      "type": "|u1"
    },
    "rings": {
      "address": 16776736,
      "type": ">u2"
    },
    "score": {
      "address": 16776742,
      "type": ">u4"
    },
    "screen_x": {
      "address": 16774912,
      "type": ">u2"
    },
    "screen_x_end": {
      "address": 16774954,
      "type": ">u2"
    },
    "screen_y": {
      "address": 16774916,
      "type": ">u2"
    },
    "x": {
      "address": 16764936,
      "type": ">i2"
    },
    "y": {
      "address": 16764940,
      "type": ">u2"
    },
    "zone": {
      "address": 16776720,
      "type": "|u1"
    }
  }
}
```

**scenario.json**

```py
{
  "done": {
    "variables": {
      "lives": {
        "op": "zero"
      }
    }
  },
  "reward": {
    "variables": {
      "x": {
        "reward": 10.0
      }
    }
  }
}
```

Ces deux fichiers contiennent des informations importantes concernant le jeu et son entraînement.

Comme son nom l'indique, le fichier data.json contient des informations/données sur différentes variables spécifiques au jeu (c'est-à-dire la position x de Sonic, le nombre de vies qu'il a, etc.).

Le fichier scenario.json nous permet d'effectuer des actions en synchronisation avec les valeurs des variables de données. Par exemple, nous pouvons récompenser Sonic de 10,0 chaque fois que sa position x augmente. Nous pourrions également définir notre condition de fin à vrai lorsque les vies de Sonic atteignent 0.

#### Comprendre la configuration feedforward de NEAT

Le fichier config-feedforward peut être trouvé dans mon dépôt GitHub lié ci-dessus. Il agit comme un menu de paramètres pour configurer notre entraînement. Pour souligner quelques paramètres simples :

```py
fitness_threshold     = 10000 # À quel point nous voulons que Sonic devienne performant
pop_size              = 20 # Combien de Sonics par génération
num_inputs            = 1120 # Nombre d'entrées dans notre modèle
num_outputs           = 12 # 12 boutons sur le contrôleur Genesis
```

Il existe de nombreux paramètres avec lesquels vous pouvez expérimenter pour voir comment cela affecte l'entraînement de votre IA ! Pour en savoir plus sur NEAT et les différents paramètres dans la configuration feedforward, je vous recommande vivement de lire la documentation [ici](https://neat-python.readthedocs.io/en/latest/)

#### Mettre tout ensemble : Créer le fichier d'entraînement

**Configurer la configuration**

Notre configuration feedforward est définie et stockée dans la variable config.

```py
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config-feedforward')
```

**Créer une fonction pour évaluer chaque génome**

Nous commençons par créer la fonction, eval_genomes, qui évaluera nos génomes (un génome pourrait être comparé à 1 Sonic dans une population de Sonics). Pour chaque génome, nous réinitialisons l'environnement et prenons une action aléatoire

```py
for genome_id, genome in genomes:
        ob = env.reset()
        ac = env.action_space.sample()
```

Nous allons également enregistrer la longueur et la largeur de l'environnement de jeu ainsi que la couleur. Nous divisons la longueur et la largeur par 8.

```py
inx, iny, inc = env.observation_space.shape
inx = int(inx/8)
iny = int(iny/8)
```

Nous créons un [réseau de neurones récurrents](https://searchenterpriseai.techtarget.com/definition/recurrent-neural-networks) (RNN) en utilisant la bibliothèque NEAT et entrons le génome et notre configuration choisie.

```py
net = neat.nn.recurrent.RecurrentNetwork.create(genome, config)
```

Enfin, nous définissons quelques variables : current_max_fitness (la fitness la plus élevée dans la population actuelle), fitness_current (la fitness actuelle du génome), frame (le compteur de frames), counter (pour compter le nombre de steps que notre agent prend), xpos (la position x de Sonic), et done (si nous avons atteint notre objectif de fitness ou non).

```py
current_max_fitness = 0
fitness_current = 0
frame = 0
counter = 0
xpos = 0
done = False
```

Tant que nous n'avons pas atteint notre exigence de fin, nous devons exécuter l'environnement, incrémenter notre compteur de frames et façonner notre observation pour imiter celle du jeu (toujours pour chaque génome).

```py
env.render()
frame += 1
ob = cv2.resize(ob, (inx, iny))
ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
ob = np.reshape(ob, (inx,iny))
```

Nous allons prendre notre observation et la mettre dans un tableau unidimensionnel, afin que notre RNN puisse la comprendre. Nous recevons notre sortie en alimentant ce tableau à notre RNN.

```py
imgarray = []
imgarray = np.ndarray.flatten(ob)
nnOutput = net.activate(imgarray)
```

En utilisant la sortie du RNN, notre IA effectue un step. À partir de ce step, nous pouvons extraire de nouvelles informations : une nouvelle observation, une récompense, si nous avons atteint notre exigence de fin ou non, et des informations sur les variables dans notre data.json (info).

```py
ob, rew, done, info = env.step(nnOutput)
```

À ce stade, nous devons évaluer la fitness de notre génome et s'il a satisfait l'exigence de fin.

Nous regardons notre variable "x" de data.json et vérifions si elle a dépassé la longueur du niveau. Si c'est le cas, nous augmenterons notre fitness de notre seuil de fitness, signifiant que nous avons terminé.

```py
xpos = info['x']
            
if xpos >= 10000:
        fitness_current += 10000
        done = True
```

Sinon, nous augmenterons notre fitness actuelle par la récompense que nous avons gagnée en effectuant le step. Nous vérifions également si nous avons une nouvelle fitness la plus élevée et ajustons la valeur de notre current_max_fitness en conséquence.

```py
fitness_current += rew

if fitness_current > current_max_fitness:
        current_max_fitness = fitness_current
        counter = 0
else:
        counter += 1
```

Enfin, nous vérifions si nous avons terminé ou si notre génome a effectué 250 steps. Si c'est le cas, nous imprimons des informations sur le génome qui a été simulé. Sinon, nous continuons à boucler jusqu'à ce que l'une des deux exigences soit satisfaite.

```py
if done or counter == 250:
        done = True
        print(genome_id, fitness_current)
                
genome.fitness = fitness_current
```

**Définir la population, imprimer les statistiques d'entraînement, et plus**

La toute dernière chose que nous devons faire est de définir notre population, imprimer les statistiques de notre entraînement, sauvegarder les checkpoints (au cas où vous voulez pause et reprendre l'entraînement), et pickler notre génome gagnant.

```py
p = neat.Population(config)

p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)
p.add_reporter(neat.Checkpointer(1))

winner = p.run(eval_genomes)

with open('winner.pkl', 'wb') as output:
    pickle.dump(winner, output, 1)
```

Il ne reste plus qu'à exécuter le programme et regarder Sonic apprendre lentement comment battre le niveau !

![Image](https://cdn-media-1.freecodecamp.org/images/caPrOTLL9OmL9C2V3BLMmUYtx1g0ckxZF1wu)

![Image](https://cdn-media-1.freecodecamp.org/images/FsO5NOjcc5S9cQiDjO56TbQLlOQIzFfdwmwc)
_Génération précoce vs génération tardive_

**Pour voir tout le code assemblé, consultez le fichier Training.py dans mon dépôt GitHub.**

#### Bonus : Entraînement parallèle

Si vous avez un CPU multi-cœur, vous pouvez exécuter plusieurs simulations d'entraînement en même temps, augmentant exponentiellement la vitesse à laquelle vous pouvez entraîner votre IA ! Bien que je ne passerai pas en revue les spécificités de la manière de faire cela dans cet article, je vous suggère vivement de consulter l'implémentation **sonicTraining.py** dans mon dépôt GitHub.

### Conclusion

C'est tout ce qu'il y a à faire ! Avec quelques ajustements, ce framework est applicable à n'importe quel jeu pour la NES, SNES, SEGA Genesis, et plus encore. Si vous avez des questions ou si vous voulez simplement dire bonjour, n'hésitez pas à m'envoyer un email à vedantgupta523[at]gmail[dot]com ?

De plus, assurez-vous de consulter les tutoriels YouTube de Lucas Thompson sur Sonic AI Bot Using Open-AI and NEAT [YouTube tutorials](https://www.freecodecamp.org/news/how-to-use-ai-to-play-sonic-the-hedgehog-its-neat-9d862a2aef98/Sonic%20AI%20Bot%20Using%20Open-AI%20and%20NEAT%20Tutorial) et [code](https://gitlab.com/lucasrthompson/Sonic-Bot-In-OpenAI-and-NEAT) pour voir ce qui a inspiré cet article à l'origine.

### Points clés à retenir

1. **Neuroevolution of Augmenting Topologies (NEAT)** est un algorithme utilisé pour entraîner l'IA à effectuer certaines tâches. Il est modélisé après l'évolution génétique.
2. **NEAT** élimine le besoin de données préexistantes lors de l'entraînement de l'IA.
3. Le processus de mise en œuvre d'**OpenAI** et de **NEAT** en utilisant Python pour entraîner une IA à jouer à n'importe quel jeu.