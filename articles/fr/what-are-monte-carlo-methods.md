---
title: Qu'est-ce que les méthodes de Monte Carlo ? Comment prédire l'avenir avec des
  simulations Python
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-07-16T21:42:38.000Z'
originalURL: https://freecodecamp.org/news/what-are-monte-carlo-methods
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-matej-117839-716661.jpg
tags:
- name: Python
  slug: python
seo_title: Qu'est-ce que les méthodes de Monte Carlo ? Comment prédire l'avenir avec
  des simulations Python
seo_desc: 'Monte Carlo methods have revolutionized programming and engineering.

  These methods use the power of randomness, which makes them effective tools that
  help developers solve difficult problems in many fields.

  Monte Carlo methods have been adopted in ph...'
---

Les méthodes de Monte Carlo ont révolutionné la programmation et l'ingénierie.

Ces méthodes utilisent la puissance de l'aléatoire, ce qui en fait des outils efficaces aidant les développeurs à résoudre des problèmes difficiles dans de nombreux domaines.

Les méthodes de Monte Carlo ont été adoptées en physique, en finance, en ingénierie et dans de nombreux autres domaines où les méthodes déterministes sont souvent impraticables pour résoudre des problèmes.

Avec les méthodes de Monte Carlo, les simulations et les calculs très complexes sont devenus efficaces et faciles à gérer.

Il existe de nombreuses variantes des méthodes de Monte Carlo. Mais toutes partagent l'idée d'utiliser l'aléatoire pour approximer des solutions à des problèmes difficiles. Dans cet article, vous apprendrez tout sur les méthodes de Monte Carlo.

## Ce que nous allons couvrir :

* [Comprendre les méthodes de Monte Carlo à travers une analogie](#heading-comprendre-les-methodes-de-monte-carlo-a-travers-une-analogie)
* [Qu'est-ce que les méthodes de Monte Carlo ? Un guide en langage simple](#heading-quest-ce-que-les-methodes-de-monte-carlo-un-guide-en-langage-simple)
* [Applications réelles des méthodes de Monte Carlo](#heading-applications-reelles-des-methodes-de-monte-carlo)
* [Différents types de méthodes de Monte Carlo](#heading-exploration-des-differents-types-de-methodes-de-monte-carlo)
* [Implémentation pratique : Méthodes de Monte Carlo en Python](#heading-implementation-pratique-methodes-de-monte-carlo-en-python)
* [L'avenir des méthodes de Monte Carlo](#heading-conclusion-lavenir-des-methodes-de-monte-carlo)

### Prérequis

Vous devez avoir une connaissance de base en statistiques pour comprendre tout dans cet article.

Si vous avez besoin de rafraîchir vos compétences en statistiques, je recommande de consulter ce cours freeCodeCamp :

%[https://www.youtube.com/watch?v=xxpc-HPKN28]

<h2 id ="understanding">Comprendre les méthodes de Monte Carlo à travers une analogie</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/2.jpg)
_Photo par [veeterzy sur Pexels](https://www.pexels.com/photo/green-leafed-tree-38136/)_

Imaginez que vous voulez trouver la hauteur moyenne des arbres dans une grande forêt.

Mesurer chaque arbre est impossible et impraticable. Mais avec les méthodes de Monte Carlo, il est possible de sélectionner aléatoirement quelques endroits dans la forêt et de mesurer la hauteur de tous les arbres à ces endroits.

En faisant cela plusieurs fois et en faisant la moyenne de toutes ces mesures, nous pouvons estimer la hauteur moyenne de tous les arbres de la forêt.

De cette manière, il est possible de faire de grandes estimations dans des populations larges et complexes en trouvant de petits échantillons gérables et en faisant la moyenne.

<h2 id ="what">Qu'est-ce que les méthodes de Monte Carlo ? Un guide en langage simple</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/pexels.jpg)
_Photo par [Jonathan Petersson sur Pexels](https://www.pexels.com/photo/photo-of-two-red-dices-965879/)_

Les méthodes de Monte Carlo sont un type d'algorithme informatique qui utilise des mesures aléatoires répétées pour obtenir des résultats approximatifs pour un problème donné.

Elles font partie du domaine mathématique appelé [analyse numérique](https://www.freecodecamp.org/news/numerical-analysis-explained-how-to-apply-math-with-python/) – l'utilisation de méthodes d'approximation pour trouver des solutions où les méthodes déterministes sont impraticables.

L'idée principale est de trouver des solutions approximatives suffisamment bonnes pour résoudre des problèmes trop difficiles ou impossibles à résoudre directement.

Ces solutions sont obtenues en calculant une moyenne de nombreux échantillons choisis aléatoirement dans la population du problème en question.

De cette manière, dans les systèmes avec de nombreux facteurs incertains et des parties interactives, les méthodes de Monte Carlo sont capables de fournir des informations sur le comportement et la performance du système.

Elles sont basées sur l'idée mathématique de la [Loi des grands nombres](https://www.investopedia.com/terms/l/lawoflargenumbers.asp) en théorie des probabilités :

> La moyenne de nombreuses variables aléatoires indépendantes et identiquement distribuées converge vers la valeur attendue, si elle existe.

Le principal problème des méthodes de Monte Carlo est le manque de ressources informatiques pour effectuer de nombreuses simulations afin d'obtenir de bons résultats.

### Pourquoi sont-elles appelées "Monte Carlo" ?

Les méthodes de Monte Carlo, nommées d'après le [Casino de Monte Carlo à Monaco](https://www.montecarlosbm.com/en/casino-monaco/casino-monte-carlo), ont été inventées par des mathématiciens pendant le projet Manhattan des années 1940.

[Stanislaw Ulam](https://www.britannica.com/biography/Stanislaw-Ulam), [John von Neumann](https://www.britannica.com/biography/John-von-Neumann), et d'autres ont été impliqués dans ce projet, qui a développé la bombe nucléaire américaine.

Le nom reflète l'aléatoire dans leurs simulations, similaire aux résultats aléatoires des jeux de casino.

<h2 id ="real">Applications réelles des méthodes de Monte Carlo</h2>

### Conception de circuits en ingénierie électrique

![Image](https://www.freecodecamp.org/news/content/images/2024/07/circuit.jpg)
_Photo de [Pixabay](https://www.pexels.com/photo/close-up-photography-of-computer-motherboard-163125/)_

Les circuits ont de nombreux composants. En voici quelques-uns :

* Résistances
* Inductances
* Condensateurs
* Diodes
* Transistors

En raison des températures de l'environnement dans lequel ils se trouvent, parfois les circuits peuvent ne pas fonctionner.

Alors, comment les ingénieurs conçoivent-ils des circuits résistants à la température ?

En d'autres termes : comment pouvons-nous tester les performances d'un circuit à différentes températures ?

Grâce aux méthodes de Monte Carlo, nous pouvons simuler de nombreux intervalles de conditions de température et voir leurs effets sur les composants du circuit et dans quelle mesure ils affectent les performances du circuit.

De cette manière, nous pouvons recueillir des données sur la manière dont les composants doivent performer sous différentes contraintes thermiques.

De cette manière, nous pouvons optimiser le circuit – que ce soit pour changer la conception du circuit ou choisir différents composants – pour qu'il fonctionne dans de nombreuses conditions environnementales.

### Conception de fusées en ingénierie aérospatiale

![Image](https://www.freecodecamp.org/news/content/images/2024/07/rocket.jpg)
_Photo de [Pixabay](https://www.pexels.com/photo/white-rocket-2159/)_

La conception de fusées implique de nombreuses variables différentes, telles que :

* Propriétés des matériaux
* Forces aérodynamiques
* Efficacité de la propulsion
* Conditions environnementales.

Les méthodes de Monte Carlo permettent de nombreuses simulations avec des propriétés de matériaux variables, une efficacité de propulsion et d'autres variables de conception.

Cela aide à comprendre profondément le comportement des fusées dans des conditions diverses.

En essence, cette manière stochastique de résoudre un grand problème est clé pour comprendre le comportement probabiliste de la performance de la fusée, comme :

* Trajectoire
* Stabilité
* Intégrité structurelle

En analysant comment ces variables de conception affectent le comportement probabiliste des métriques de performance de vol cruciales de la fusée, les ingénieurs peuvent rendre les fusées plus sûres et plus fiables.

### Optimisation de portefeuille financier en finance et investissement

![Image](https://www.freecodecamp.org/news/content/images/2024/07/finance.jpg)
_Photo par [energepic.com](https://www.pexels.com/photo/close-up-photo-of-monitor-159888/)_

Dans l'optimisation de portefeuille financier, quel est le meilleur mélange d'actifs dans un portefeuille pour maximiser les rendements tout en minimisant les risques ?

Les méthodes de Monte Carlo sont utilisées pour [simuler](https://www.quantconnect.com/learning/articles/introduction-to-options/stochastic-processes-and-monte-carlo-method) à quel point un portefeuille est bon pour maximiser les rendements tout en minimisant les risques dans diverses conditions de marché.

En générant de nombreux scénarios aléatoires pour les prix des actifs et les rendements, les banques et les institutions financières peuvent connaître, dans différentes conditions, les résultats des portefeuilles et gérer les risques.

De cette manière, il est possible de prendre des décisions basées sur les données pour trouver un équilibre entre les risques et les récompenses.

<h2 id ="exploring">Exploration des différents types de méthodes de Monte Carlo</h2>

Il existe de nombreuses variantes des méthodes de Monte Carlo. En voici quelques-unes des plus importantes :

### Monte Carlo Classique :

Le Monte Carlo classique utilise des échantillons aléatoires pour estimer des valeurs et simuler des systèmes. Il est utile pour des tâches où les solutions directes sont difficiles à trouver, comme l'intégration numérique.

### Monte Carlo Bayésien :

Le Monte Carlo Bayésien améliore les estimations en utilisant des informations existantes avec de nouvelles observations pour faire de meilleures prédictions.

Il est appelé Monte Carlo Bayésien car il utilise le [théorème de Bayes](https://www.freecodecamp.org/news/bayes-rule-explained/).

Le théorème de Bayes a été créé par le mathématicien Thomas Bayes et il est très important en théorie des probabilités.

L'idée principale du théorème est de **réviser les croyances existantes avec de nouvelles données.**

Cette méthode est idéale lorsque vous avez déjà certaines informations sur le problème.

### Monte Carlo par Chaînes de Markov (MCMC) :

Pour les grands ensembles de données, les méthodes de Monte Carlo prennent souvent trop de temps pour calculer les résultats.

Une façon de résoudre ce problème est d'utiliser une version plus petite des grands ensembles de données. C'est un peu comme un résumé qui **représente** le contenu d'un livre car il est plus rapide à lire.

Cette version plus petite est appelée une [Chaîne de Markov](https://www.freecodecamp.org/news/what-is-a-markov-chain/).

En termes simples, les Chaînes de Markov sont des modèles qui montrent comment un système passe d'un état à un autre.

Un grand ensemble de données peut être vu comme un système et les états comme des motifs de données.

De cette manière, les Chaînes de Markov sont des modèles simples qui peuvent **représenter** un grand ensemble de données car ils montrent comment les choses changent d'un état à un autre.

Ce changement d'état peut représenter, avec moins de nombres, les motifs importants dans les données.

De cette manière, à partir de la Chaîne de Markov, la méthode de Monte Carlo calcule ses résultats.

En essence, le Monte Carlo fait ses prédictions **indirectement** à partir des données originales. La Chaîne de Markov agit comme une étape de **prétraitement des données** pour calculer les résultats de Monte Carlo.

En fin de compte, MCMC est simplement une méthode de Monte Carlo régulière mais beaucoup plus efficace sur le plan computationnel.

### Autres variantes

D'autres méthodes comme _Gradient, Semi-Gradient, et Quasi Monte Carlo_ se concentrent également sur l'efficacité computationnelle. Mais dans cet article, je cherche uniquement à souligner l'importance des méthodes de Monte Carlo en science, en ingénierie et en programmation.

<h2 id ="pratical">Implémentation pratique : Méthodes de Monte Carlo en Python</h2>

Dans le code ci-dessous, vous verrez comment implémenter une variante MCMC en Python.

Je vais démontrer une variante populaire de MCMC appelée Hamiltonian Monte Carlo (HMC).

Elle est appelée Hamiltonian car elle utilise des concepts de la mécanique hamiltonienne pour proposer de nouveaux états pour les chaînes de Markov dans l'étape de prétraitement des données.

### Qu'est-ce que la mécanique hamiltonienne ?

Pour répondre à cette question, vous devez connaître un peu la mécanique classique.

La mécanique classique utilise les lois du mouvement de Newton pour expliquer comment les systèmes physiques se comportent et changent au fil du temps.

La mécanique hamiltonienne est une autre façon de regarder ces systèmes. Elle met souvent l'accent sur le rôle de l'énergie et sa conservation en utilisant différentes variables comme les positions généralisées et les moments.

Cette manière unique de décrire l'état et l'évolution d'un système est utilisée dans HMC.

### Objectif principal de l'exemple de code

Nous allons créer une distribution cible à partir d'une distribution gaussienne 2D en utilisant TensorFlow Probability. Cela signifie que le HMC va modéliser cette distribution cible.

La distribution gaussienne 2D est créée avec des données synthétiques pour démontrer le processus d'approximation en utilisant Hamiltonian Monte Carlo.

En d'autres termes, HMC représentera avec précision cette distribution gaussienne 2D.

Dans des scénarios réels, des circuits à la finance, tous les systèmes peuvent être décrits comme une distribution de probabilité.

Les méthodes de Monte Carlo approximient ces distributions complexes. Et le MCMC rend ce processus beaucoup plus rapide.

Dans cet exemple de code simple, j'approximie une distribution cible simple afin que vous puissiez comprendre comment, dans un scénario réel, cela serait appliqué.

Voici le code complet (nous allons le parcourir étape par étape ci-dessous) :

```
import tensorflow as tf
import tensorflow_probability as tfp

# Définir la distribution cible (Gaussienne 2D)
def target_log_prob(x, y):
    return -0.5 * (x**2 + y**2)

# Initialiser le noyau de transition HMC
num_results = 1000
num_burnin_steps = 500

hmc = tfp.mcmc.HamiltonianMonteCarlo(
    target_log_prob_fn=lambda x, y: target_log_prob(x, y),
    num_leapfrog_steps=3,
    step_size=0.1
)

# Définir la fonction de trace pour enregistrer l'état et les résultats du noyau
@tf.function
def run_chain(initial_state, kernel, num_results, num_burnin_steps):
    return tfp.mcmc.sample_chain(
        num_results=num_results,
        num_burnin_steps=num_burnin_steps,
        current_state=initial_state,
        kernel=kernel,
        trace_fn=lambda _, pkr: pkr
    )

# Exécuter la chaîne MCMC
initial_state = [tf.zeros([]), tf.zeros([])]
samples, kernel_results = run_chain(initial_state, hmc, num_results, num_burnin_steps)

# Extraire les échantillons et les enregistrer
samples_ = [s.numpy() for s in samples]
samples_x, samples_y = samples_

print("Taux d'acceptation : ", kernel_results.is_accepted.numpy().mean())
print("Moyenne de x : ", samples_x.mean())
print("Moyenne de y : ", samples_y.mean())

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/1-3.png)
_Implémentation pratique de la Méthode de Monte Carlo par Chaînes de Markov_

Comprenons comment le code fonctionne étape par étape.

### Importer les bibliothèques

```
import tensorflow as tf
import tensorflow_probability as tfp
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/2-2.png)
_Importation des bibliothèques_

Dans ce code, nous importons deux bibliothèques Python :

* [TensorFlow](https://www.tensorflow.org/) : Construction et entraînement de modèles de machine learning
* [TensorFlow Probability](https://www.tensorflow.org/probability) : Raisonnement probabiliste et modélisation statistique

### Créer une distribution cible

```
def target_log_prob(x, y):
    return -0.5 * (x**2 + y**2)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3-1.png)
_Création de la distribution cible_

Dans ce code, nous définissons une distribution gaussienne 2D :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/output-1.png)
_Distribution gaussienne 2D_

Ce graphique est défini par :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Affichage d'équation</title>
    <style>
        .equation {
            font-family: 'Times New Roman', Times, serif;
            font-size: 24px;
            text-align: center;
            width: 100%;
            margin-top: 20px; /* Optionnel : Ajoute un peu d'espace au-dessus de l'équation */
        }
    </style>
</head>
<body>
    <div class="equation">
        -0.5 &times; (x<sup>2</sup> + y<sup>2</sup>)
    </div>
</body>
</html>


En étant une distribution gaussienne 2D, chaque point de données est représenté par deux variables corrélées qui suivent une distribution gaussienne conjointe.

Si cela était un scénario réel, nous modéliserions un système en trouvant sa distribution de probabilité basée sur deux variables.

Dans de nombreuses applications pratiques, comme les circuits, il peut y avoir des dizaines de variables impliquées.

Pour modéliser correctement de tels systèmes, nous utilisons souvent des distributions de probabilité multivariées, qui généralisent le concept de la distribution gaussienne à de nombreuses dimensions.

### Initialiser le Monte Carlo par Chaînes de Markov

```
num_results = 1000
num_burnin_steps = 500

hmc = tfp.mcmc.HamiltonianMonteCarlo(
    target_log_prob_fn=lambda x, y: target_log_prob(x, y),
    num_leapfrog_steps=3,
    step_size=0.1
)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/4-1.png)
_Initialisation du Monte Carlo par Chaînes de Markov_

Ce bloc de code configure un noyau de transition Hamiltonian Monte Carlo (HMC) en utilisant TensorFlow Probability.

Il définit d'abord deux variables :

* `num_results` à 1000, indiquant le nombre d'échantillons à générer
* `num_burnin_steps` à 500, représentant le nombre d'échantillons initiaux à rejeter (période de rodage).

Le noyau de transition HMC est configuré avec :

* Une fonction de probabilité logarithmique cible qui prend deux entrées et retourne leur probabilité logarithmique. Dans notre cas, la fonction de probabilité logarithmique cible est la distribution gaussienne 2D. La probabilité logarithmique est la vraisemblance d'un ensemble particulier de valeurs.
* L'algorithme prend 3 étapes à chaque fois.
* Chaque taille de pas (quantité de changement) est de 0,1.

### Créer la fonction de trace pour enregistrer l'état et les résultats du noyau

```
@tf.function
def run_chain(initial_state, kernel, num_results, num_burnin_steps):
    return tfp.mcmc.sample_chain(
        num_results=num_results,
        num_burnin_steps=num_burnin_steps,
        current_state=initial_state,
        kernel=kernel,
        trace_fn=lambda _, pkr: pkr
    )
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/5-1.png)
_Création de la fonction de trace pour enregistrer l'état et les résultats du noyau_

La fonction est décorée avec `@tf.function`, qui l'optimise pour la performance en la compilant dans un graphe TensorFlow.

La fonction `run_chain` prend quatre arguments :

1. `initial_state` : L'état initial de la Chaîne de Markov.
2. `kernel` : Le noyau de transition MCMC à utiliser (comme Hamiltonian Monte Carlo).
3. `num_results` : Le nombre d'échantillons à générer.
4. `num_burnin_steps` : Le nombre d'échantillons initiaux à rejeter (période de rodage).

La fonction appelle `tfp.mcmc.sample_chain` pour effectuer l'échantillonnage MCMC :

* `num_results` : Le nombre d'échantillons à tirer.
* `num_burnin_steps` : Le nombre d'étapes de rodage.
* `current_state` : L'état de départ de la Chaîne de Markov.
* `kernel` : Le noyau de transition qui définit le processus d'échantillonnage.
* `trace_fn` : Une fonction qui spécifie quoi tracer pendant l'échantillonnage. Dans ce cas, elle retourne les résultats du noyau précédent (`pkr`), traçant effectivement l'état interne de l'algorithme MCMC.

### Exécuter la chaîne MCMC

```
# Exécuter la chaîne MCMC
initial_state = [tf.zeros([]), tf.zeros([])]
samples, kernel_results = run_chain(initial_state, hmc, num_results, num_burnin_steps)

# Extraire les échantillons et les enregistrer
samples_ = [s.numpy() for s in samples]
samples_x, samples_y = samples_

print("Taux d'acceptation : ", kernel_results.is_accepted.numpy().mean())
print("Moyenne de x : ", samples_x.mean())
print("Moyenne de y : ", samples_y.mean())

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/6.png)
_Exécution de la chaîne MCMC_

D'accord, décomposons cela car il se passe beaucoup de choses ici :

**Initialiser l'État** :

* `initial_state` est défini comme une liste contenant deux tenseurs nuls, qui sert de point de départ pour la Chaîne de Markov.

**Exécuter la Chaîne MCMC** :

* La fonction `run_chain` est appelée avec l'état initial, le noyau HMC, le nombre de résultats et le nombre d'étapes de rodage.
* La fonction retourne deux valeurs : `samples`, qui sont les échantillons générés, et `kernel_results`, qui contiennent les résultats du noyau (y compris les informations de diagnostic).

**Extraire et Convertir les Échantillons** :

* Les échantillons sont convertis de tenseurs TensorFlow en tableaux NumPy pour une manipulation et une analyse plus faciles.
* `samples_` est une liste en compréhension qui convertit chaque tenseur d'échantillon en un tableau numpy.
* `samples_x` et `samples_y` sont les échantillons extraits pour les deux dimensions.

**Imprimer les Diagnostics** :

* Le taux d'acceptation de l'échantillonneur MCMC est calculé et imprimé. Il montre la proportion de propositions acceptées pendant l'échantillonnage.
* Les moyennes des échantillons pour les deux dimensions (`x` et `y`) sont calculées et imprimées pour fournir un résumé des résultats de l'échantillonnage.

Cela donne les résultats suivants :

* Taux d'acceptation : 1.0. Cela signifie que toutes les propositions faites pendant l'échantillonnage ont été acceptées
* Moyenne de x : -0.11450629 et moyenne de y : -0.23079416. Dans une distribution gaussienne 2D parfaite, les moyennes de x et y sont 0.

Avec cette variante MCMC, nous approximons la distribution gaussienne 2D. Mais c'est proche de zéro. Cela signifie que, donné plus de temps de calcul, elle irait probablement vers un nombre encore plus petit jusqu'à ce qu'il soit si petit qu'il pourrait être considéré comme zéro.

<h2 id ="conclusion">Conclusion : L'avenir des méthodes de Monte Carlo</h2>

L'avenir des méthodes de Monte Carlo réside dans la création de variantes nécessitant moins de ressources computationnelles et économisant du temps.

Avec ces avancées, les méthodes de Monte Carlo trouveront des applications supplémentaires dans plus de domaines.

Grâce aux méthodes de Monte Carlo, nous sommes capables de modéliser des systèmes et des phénomènes complexes qui étaient auparavant impossibles à faire de manière efficace.

Si vous voulez en savoir plus, vous pouvez [lire cet article sur les méthodes de Monte Carlo](https://www.freecodecamp.org/news/solve-the-unsolvable-with-monte-carlo-methods-294de03c80cd/).

Vous pouvez également consulter le code complet ici :

%[https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code]