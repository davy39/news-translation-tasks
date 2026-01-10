---
title: Introduction à la théorie des jeux évolutionnaires
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-13T17:12:33.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-evolutionary-game-theory
coverImage: https://cdn-media-2.freecodecamp.org/w1280/605de4899618b008528a7b69.jpg
tags:
- name: evolution
  slug: evolution
- name: Game Theory
  slug: game-theory
- name: Math
  slug: math
- name: 'Science '
  slug: science
seo_title: Introduction à la théorie des jeux évolutionnaires
seo_desc: 'By Peter Gleeson

  For the longest time, the evolution of cooperative social behaviour has fascinated
  evolutionary biologists.

  The mathematical field of game theory helps shed light on how it emerges. Game theory
  is “the study of mathematical models of...'
---

Par Peter Gleeson

Pendant très longtemps, l'évolution du comportement social coopératif a fasciné les biologistes évolutionnistes.

Le domaine mathématique de la théorie des jeux aide à éclairer comment cela émerge. La théorie des jeux est « l'étude des modèles mathématiques d'interaction stratégique parmi des décideurs rationnels » (selon [Wikipedia](https://en.wikipedia.org/wiki/Game_theory)).

La théorie des jeux s'applique à des « jeux » aussi variés que l'économie, la politique, les échecs et le morpion. Dans chaque cas, il y a des règles, des « joueurs » ou des « agents », et un ensemble de stratégies disponibles pour eux.

Chaque joueur a un concept d'« utilité » – une « monnaie » qu'il cherche à maximiser individuellement à travers les stratégies qu'il joue.

La monnaie de l'évolution est le concept de [fitness](https://www.nature.com/scitable/blog/accumulating-glitches/the_meaning_of_fitness/).

C'est-à-dire, la chance d'être représenté dans la génération suivante. Les gènes et les traits qui augmentent les chances de survie jusqu'à l'âge de la reproduction sont plus susceptibles d'être transmis aux générations futures. Par conséquent, ils confèrent une plus grande fitness à l'individu qui les « héberge ».

La théorie des jeux évolutionnaires prend les concepts de la théorie des jeux et les applique dans un contexte évolutionnaire.

Pour un modèle donné, elle permet de poser des questions sur quelle stratégie prévaut et si certaines stratégies peuvent coexister. Et si oui – à quelles fréquences ?

## Dynamique des réplicateurs

La théorie des jeux évolutionnaires joue des « jeux » sur de nombreuses générations.

Chaque jeu modifiera l'utilité (c'est-à-dire la fitness) des joueurs. La génération suivante est produite, avec des joueurs représentés proportionnellement à leur fitness globale.

Cette configuration est appelée « dynamique des réplicateurs ». Elle est facile à simuler et à explorer différents modèles de jeux évolutionnaires.

Le modèle classique de la théorie des jeux évolutionnaires est le jeu « Faucon-Colombe », popularisé par John Maynard Smith dans les années 1970.

Dans ce jeu, il existe une population d'animaux qui se disputent une ressource finie (par exemple, de la nourriture). Plus un individu gagne de ressources, plus sa fitness est grande.

Chaque animal peut jouer l'une des deux stratégies :

* Les **Faucons** sont agressifs et se battent pour une ressource à tout prix.
* Les **Colombes** sont passives et partagent plutôt que de se battre pour une ressource.

Les animaux sont tous de la même espèce – « faucon » et « colombe » font référence à leur comportement.

Il existe trois compétitions par paires qui peuvent exister :

**Faucon vs Faucon**

* Si deux faucons se disputent, ils s'engageront dans une bataille à 50:50 pour gagner la ressource. C'est un scénario où le gagnant prend tout – le gagnant obtient la valeur totale de la ressource. Le perdant blessé paie un prix et perd une certaine quantité de fitness.

**Faucon vs Colombe**

* Si un faucon rencontre une colombe, la colombe recule immédiatement. Le faucon gagne la valeur totale de la ressource, et la colombe s'en va (ou plutôt, s'envole) sans rien. Mais ils ne paient aucun coût.

**Colombe vs Colombe**

* Lorsque deux colombes se rencontrent, elles conviennent de partager la ressource équitablement. Personne ne se blesse.

Cela peut être modélisé mathématiquement. Cela permet de comprendre si ces stratégies peuvent coexister (ou si l'une d'elles prévaut).

### Les mathématiques de la dynamique des réplicateurs

Soit _V_ la valeur de gagner un concours, et _C_ le coût de la blessure dans un concours.

Représentons la fréquence des faucons dans la population par _p_, et la fréquence des colombes par _1-p_.

Définissons maintenant deux fonctions F(H) et F(D) qui définissent la fitness attendue de jouer les stratégies du faucon et de la colombe, respectivement.

Jouer en tant que faucon signifie s'engager dans un concours faucon-contre-faucon avec une fréquence _p_. L'utilité attendue de le faire est comprise comme le résultat moyen. La moitié du temps, le faucon gagne _V_, l'autre moitié du temps, il perd _C_.

Le reste des concours d'un faucon sera contre des colombes. Cela garantit une victoire facile _V_.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8b5ac2e8-fdfb-4ffc-8abe-15d0d014f580_544x112.png)

Jouer en tant que colombe ne gagnera rien contre les faucons. Mais une colombe rencontrera une autre colombe avec une fréquence _1-p_. Dans ce scénario, l'utilité attendue est la ressource partagée, valant _V/2_.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6303e0b2-d6ab-434d-b7ec-cad18a82d154_508x110.png)

Maintenant, posons _F(H)_ égal à _F(D)_ et résolvons pour _p_.

Cela révèle la fréquence _p_ à laquelle la stratégie du faucon ne confère pas plus ou moins de fitness que la stratégie de la colombe.

À cette fréquence, il n'y a aucun avantage pour l'une ou l'autre stratégie, donc c'est l'équilibre auquel les deux stratégies peuvent coexister.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F77be89c1-0286-4673-867f-1c8e1a038cb7_516x104.png)

Un peu de réarrangement algébrique donne :

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fca77237e-29a4-4826-af4a-2fbb390d3572_404x108.png)

Ce qui fournit le ratio faucons-colombes qui existe à l'équilibre.

Un peu plus de réarrangement donne l'équilibre en termes de _p_ :

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb812b56c-8387-4a47-902e-61aaa87cf317_342x98.png)

En considérant les propriétés de cette expression, deux choses se révèlent :

* Chaque fois que le coût _C_ de perdre un concours est inférieur ou égal à la valeur _V_ de gagner, la stratégie du faucon dominera. Aucune stratégie ne peut coexister.
* Si le coût _C_ est supérieur à la valeur _V_, les stratégies coexisteront à l'équilibre.

En insérant les valeurs _V_=4 et _C_=6, on montre que l'équilibre se produit lorsque 2/3 de la population jouent la stratégie du faucon.

Vous pouvez tester cela en simulant le modèle en Python.

### Le code

Dans le fichier appelé bird.py :

```python
import random

class Bird:
    def __init__(self, strategy):
        """
        Chaque oiseau a un type de stratégie (faucon ou colombe)
        Et une petite fitness de départ
        """
        self.strategy = strategy
        self.fitness = 10

    def contest(self, opponent, v, c):
       """
       Simuler les résultats en fonction des stratégies
       """
        
        # les deux faucons --> bataille à 50:50

        if self.strategy == opponent.strategy == "hawk":
            if random.randint(0, 1) == 1:
                self.fitness = self.fitness + v
                opponent.fitness = opponent.fitness - c
            else:
                self.fitness = self.fitness - c
                opponent.fitness = opponent.fitness + v

        # faucon rencontre colombe

        elif self.strategy == "hawk" != opponent.strategy:
            self.fitness = self.fitness + v
            opponent.fitness = opponent.fitness
        elif self.strategy == "dove" != opponent.strategy:
            self.fitness = self.fitness
            opponent.fitness = opponent.fitness + v

        # les deux colombes --> partager la ressource

        else:
            self.fitness = self.fitness + v/2
            opponent.fitness = opponent.fitness + v/2

    def spawn(self):
        """
        Permettre une petite chance de mutation pour changer de stratégie
        Sinon, retourner une progéniture du même type
        """

        mutation = random.randint(0, 1000) > 999
        if mutation:
            if self.strategy == "dove":
                return Bird("hawk")
            else:
                return Bird("dove")
        else:
            return Bird(self.strategy)

```

Le fichier suivant s'appelle simulation.py.

1. Initialiser une population de toutes colombes.
2. Définir une fonction de pas de temps pour simuler des concours aléatoires.
3. Tirer la génération suivante pondérée par leurs fitness relatives.
4. Répéter mille fois, puis sauvegarder la sortie sous forme de graphique.

```python
from bird import Bird
import random
import numpy as np
import pandas as pd
import matplotlib


def initialise():
    """
    Créer une population d'oiseaux - toutes colombes au début
    """

    birds = []

    for _ in range(1000):
        birds.append(Bird("dove"))

    return (birds)


def timestep(birds, value, cost):
    """
    Associer les oiseaux, les faire concourir
    Puis produire la génération suivante, pondérée par la fitness
    """

    next_generation = []

    random.shuffle(birds)

    for _ in range(1000):

        # associer des oiseaux aléatoires pour concourir
        a, b = random.sample(birds, 2)
        a.contest(b, value, cost)

    # générer la génération suivante
    fitnesses = [bird.fitness for bird in birds]

    draw = random.choices(birds, k=1000, weights=fitnesses)
    next_generation = [bird.spawn() for bird in draw]

    return next_generation


def main():

    birds = initialise()

    rows = []

    V = 4 ; C = 6

    for _ in range(1000):
        
        # ajouter les comptes à une nouvelle ligne
        strategy = [bird.strategy for bird in birds]
        n_hawks = strategy.count("hawk")
        n_doves =  strategy.count("dove")
        row = {'n_hawks': n_hawks, 'n_doves': n_doves}
        rows.append(row)

        # exécuter la fonction de pas de temps
        birds = timestep(birds, V, C)


    # créer un dataframe et sauvegarder la sortie

    df = pd.DataFrame(rows)
    df.to_csv('simulation.csv')
    fig = df.plot(y=["n_hawks", "n_doves"]).get_figure()
    fig.savefig('simulation.pdf')

if __name__ == "__main__":
    main()

```

Et voilà - voici un exemple de sortie pour _V_=4 et _C_=6 :

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F44100a89-d377-435e-bf11-97b046db5f32_1438x1048.png)

Exactement comme le prédit la théorie.

## Conclusion

L'évolution des systèmes complexes est un domaine d'étude fascinant. Comprendre comment les forces naturelles et les pressions compétitives peuvent façonner les traits au niveau individuel pour donner lieu à des comportements sociaux complexes a été l'un des principaux domaines de recherche en sciences biologiques au cours des dernières décennies.

La capacité des modèles mathématiques relativement simples à prédire avec précision les résultats des systèmes dynamiques est également un point clé à retenir.

Dans ce cas, c'est l'existence d'une boucle de rétroaction qui conduit les deux stratégies à atteindre un équilibre. L'avantage conféré par l'une ou l'autre stratégie varie en fonction du nombre d'autres individus dans la population qui jouent cette stratégie.

En d'autres termes, lorsque plus d'individus jouent « colombe », il y a un avantage à jouer « faucon ». Cependant, à mesure que plus d'individus jouent « faucon », la valeur attendue de jouer « colombe » augmente.

Enfin, la disponibilité des outils de programmation et de logiciels permet de tester les prédictions théoriques par simulation.

Si vous avez trouvé cet article intéressant, vous pourriez également trouver [Comment modéliser une épidémie avec R](https://www.freecodecamp.org/news/how-to-model-an-epidemic-with-r/) intéressant à consulter.

Vous pouvez suivre plus de mes écrits sur [gleeson.substack.com](https://gleeson.substack.com/)