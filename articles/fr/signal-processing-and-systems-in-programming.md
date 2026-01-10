---
title: Traitement du signal et systèmes en programmation – Guide pour débutants
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2023-09-06T14:49:58.000Z'
originalURL: https://freecodecamp.org/news/signal-processing-and-systems-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-igor-mashkov-6325003.jpg
tags:
- name: data
  slug: data
- name: Signal Processing
  slug: signal-processing
- name: systems
  slug: systems
seo_title: Traitement du signal et systèmes en programmation – Guide pour débutants
seo_desc: "Signal processing is an important field in engineering and programming.\
  \ \nBasically, it allows engineers and programmers to improve data so that people\
  \ can use it more effectively.\nFor example, it is thanks to signal processing that\
  \ much of the backgr..."
---

Le traitement du signal est un domaine important en ingénierie et en programmation. 

En effet, il permet aux ingénieurs et aux programmeurs d'améliorer les données afin que les utilisateurs puissent les exploiter plus efficacement.

Par exemple, c'est grâce au traitement du signal que la majeure partie du bruit de fond dans un appel téléphonique est supprimée. Ainsi, seule votre voix parvient à l'autre bout de la ligne.

D'autres exemples incluent :

* Les logiciels audio et musicaux
* Les logiciels de traitement d'images et de vidéos
* Les logiciels d'imagerie médicale 
* Les logiciels de traitement de la parole et du langage 
* Les logiciels de communication sans fil

Comprendre le traitement du signal et les systèmes est essentiel pour tout programmeur qui doit traiter, manipuler et analyser ces types de données.

Ce tutoriel explorera le domaine du traitement du signal et les principales caractéristiques d'un système, y compris certaines caractéristiques importantes des systèmes telles que :

* La causalité
* La mémoire
* L'invariance temporelle
* La linéarité

Voici ce que nous allons couvrir :

1. [Qu'est-ce que le traitement du signal ?](#heading-quest-ce-que-le-traitement-du-signal)
2. [Exemple de code Python – Comment filtrer un signal](#heading-exemple-de-code-python-comment-filtrer-un-signal)
3. [Contexte sur la transformée de Fourier](#heading-contexte-sur-la-transformee-de-fourier)
4. [Qu'est-ce qu'un système en traitement du signal](#heading-quest-ce-quun-systeme-en-traitement-du-signal) ?
5. [Conclusion](#heading-conclusion)

## Qu'est-ce que le traitement du signal ?

Le traitement du signal, simplement expliqué, est le domaine où des outils sont créés pour permettre aux ingénieurs et aux programmeurs de manipuler certains signaux afin de résoudre des problèmes.

Il implique l'analyse des sons ou des images pour en extraire uniquement les données nécessaires.

Par exemple, les données des biocapteurs qui indiquent la quantité d'oxygène dans le sang sont affichées dans un oxymètre de pouls. Ces données sont filtrées à l'aide d'outils de traitement du signal.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/pexels-cottonbro-studio-7580256.jpg)
_[Photo par cottonbro studio](https://www.pexels.com/photo/index-finger-in-blue-pulse-oximeter-7580256)_

Ces données sont traitées dans un programme à l'intérieur de l'oxymètre à l'aide d'outils logiciels de traitement du signal.

De plus, lorsque vous passez un appel téléphonique à un ami, des algorithmes de traitement du signal sont en cours d'exécution afin que seule votre voix soit envoyée à votre ami pour réduire autant que possible le bruit de fond.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/pexels-karolina-grabowska-4195335.jpg)
_[Photo par Karolina Grabowska](https://www.pexels.com/photo/charging-smartphone-and-white-earphones-on-wooden-table-4195335/)_

Souvent, le traitement du signal fonctionne à l'aide d'outils comme la **Transformée de Fourier Rapide**. Et ne vous inquiétez pas – je vais expliquer ce que c'est.

En utilisant l'algorithme de la Transformée de Fourier Rapide, nous sommes capables de décomposer un signal pour trouver les ondes individuelles qui le composent.

Ainsi, nous sommes capables de supprimer les ondes individuelles que nous ne voulons pas (par exemple, le bruit de fond d'un appel téléphonique est un ensemble d'ondes que nous pouvons supprimer pour améliorer la qualité).

La Transformée de Fourier Rapide est également utilisée comme bloc de construction ou source d'inspiration pour certains algorithmes de compression de fichiers.

En fin de compte, c'est cela le traitement du signal : décomposer un signal pour en extraire ce que nous voulons.

### Où le traitement du signal est-il utilisé dans la vie réelle ?

* Traitement audio – comme la suppression du bruit de fond d'un film
* Traitement d'image – comme la conversion d'une image en noir et blanc
* Systèmes de communication sans fil – comme la modulation d'un signal pour qu'il puisse voyager plus loin (modulation de fréquence)

## Exemple de code Python – Comment filtrer un signal

Vous n'avez pas besoin de comprendre tout le code que je vais vous montrer maintenant – il s'agit simplement du code que j'ai utilisé pour générer les graphiques que je vais vous montrer pour vous aider à comprendre comment fonctionne la Transformée de Fourier Rapide.

J'ai partagé le code complet dans la conclusion dans un dépôt GitHub afin que vous puissiez le consulter.

Voici le code qui filtre un signal :

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 300, endpoint=False)
x = np.sin(2*np.pi*10*t)
y = 0.5*np.sin(2*np.pi*20*t)
w = 0.2*np.sin(2*np.pi*50*t)
z = x + y + w

zf = np.fft.fft(z)

N = len(z)
freq = np.fft.fftfreq(N, d=t[1]-t[0])
spectrum = 2/N * np.abs(zf[:N//2])

mask = np.ones(len(freq), dtype=bool)
mask[(freq > 15) & (freq < 60)] = False
mask[(freq < -15) & (freq > -60)] = False

zf_filtered = zf.copy()
zf_filtered[~mask] = 0

z_filtered = np.fft.ifft(zf_filtered)
```

Ci-dessous, je vais montrer visuellement ce que chaque partie du code fait avec des graphiques :

### Étape 1 : Création des signaux

```
t = np.linspace(0, 1, 300, endpoint=False)
x = np.sin(2*np.pi*10*t)
y = 0.5*np.sin(2*np.pi*20*t)
w = 0.2*np.sin(2*np.pi*50*t)
z = x + y + w
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Figure_1.png)
_Trois signaux différents et un signal vert représentant leur somme_

Nous pouvons voir ici que le signal vert est la somme de :

* Onde rouge – Signal X
* Onde bleue – Signal Y
* Onde orange – Signal W

Notez que tout signal peut être composé d'un certain nombre d'ondes simples. En mathématiques, ces ondes sont les fonctions sinus et cosinus.

Cette idée incroyablement importante est appelée une série de Fourier.

Ci-dessous se trouve une vidéo que je recommande et qui explique simplement ce qu'est une série de Fourier :

%[https://www.youtube.com/watch?v=UKHBWzoOKsY]

### Étape 2 : Création d'une Transformée de Fourier Rapide sur le signal Z

Nous pouvons appliquer la Transformée de Fourier Rapide comme ceci :

```
zf = np.fft.fft(z)
```

Pour en faire un graphique, nous devons encore faire ce qui suit :

```
N = len(z)
freq = np.fft.fftfreq(N, d=t[1]-t[0])
spectrum = 2/N * np.abs(zf[:N//2])
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Figure_2.png)
_Voir le signal vert en termes de fréquence au lieu du temps - Nous "voyons" le signal vert d'un autre point de vue_

Grâce à la Transformée de Fourier Rapide, nous sommes capables de voir la composition du signal vert. 

Comme nous pouvons le voir, le signal vert est composé de 3 ondes avec 3 fréquences différentes :

* 10 hertz – Onde rouge – Signal X
* 20 hertz – Onde bleue – Signal Y
* 50 hertz – Onde orange – Signal W

### Étape 3 : Création et application du filtre

```
mask = np.ones(len(freq), dtype=bool)
mask[(freq > 15) & (freq < 60)] = False
mask[(freq < -15) & (freq > -60)] = False

zf_filtered = zf.copy()
zf_filtered[~mask] = 0

z_filtered = np.fft.ifft(zf_filtered)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Figure_3.png)
_Signal X filtré à partir du signal vert - Seul le signal de 10 hertz passe_

Ce filtre est appelé un filtre passe-bande, car il filtre toutes les fréquences entre 30 hertz et 60 hertz.

Ainsi, ce signal rouge filtré est essentiellement le signal rouge **original**.

## Contexte sur la transformée de Fourier

L'idée selon laquelle tout signal peut être représenté par la somme d'ondes simples a été créée par le mathématicien Joseph Fourier.

Ces ondes sont appelées sinus et cosinus.

Note : vous n'avez pas besoin de comprendre complètement ces équations – je les montre simplement pour que vous puissiez comprendre l'histoire de la transformée de Fourier.

C'est ce qu'on appelle une série de Fourier :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/fourier-series-1.png)
_Équation pour la série de Fourier_

[Voici une meilleure image de l'équation](https://cdn1.byjus.com/wp-content/uploads/2020/11/Fourier-series-formula.png)

Les coefficients sont donnés par ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/fourier-series-2.png)
_Coefficients de la série de Fourier_

À partir de la série de Fourier, la transformée de Fourier peut être déduite :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/fourier-tra-1.png)
_Équation de la transformée de Fourier_

[Voici une meilleure image de la formule](https://abakcus.com/wp-content/uploads/2021/09/Fourier-Transform-Equations-That-Changed-the-World-Abakcus-scaled.jpg)

Cependant, la transformée de Fourier a été développée par divers mathématiciens et physiciens au fil des ans.

Ainsi, c'est sur la base du travail de nombreux chercheurs au fil du temps que nous avons pu redéfinir la transformée de Fourier. 

Mais ce n'est pas l'expression mathématique compliquée pure qui est exécutée dans un ordinateur.

Dans un ordinateur, il s'agit d'un algorithme qui approxime très bien la transformée de Fourier appelé la **Transformée de Fourier Rapide**.

C'est de là que vient le FFT dans le code :

```
zf = np.fft.fft(z)
```

`fft` signifie Fast Fourier Transform.

Voici la documentation avec la fonction :

%[https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html]

Mais vous pourriez vous demander...

### Pourquoi utiliser la Transformée de Fourier Rapide ?

Parce que la Transformée de Fourier Rapide **s'exécute beaucoup plus rapidement** que l'équation mathématique pure.

Il existe même un domaine entier des mathématiques dédié à la recherche d'algorithmes qui approximient les mathématiques pures afin que les ordinateurs puissent les exécuter très rapidement.

Ce domaine est appelé **[Analyse Numérique](http://www.scholarpedia.org/article/Numerical_analysis).**

Il est également utilisé pour trouver des solutions approximatives pour des problèmes impossibles à résoudre à la main.

Par exemple, dans le domaine des équations différentielles partielles, de nombreuses solutions aux équations différentielles partielles ne sont résolues qu'avec des méthodes d'analyse numérique exécutées sur des ordinateurs.

Ainsi, grâce à ce domaine des mathématiques, les entreprises sont capables d'économiser des millions de coûts énergétiques.

Si vous êtes intéressé à en apprendre davantage sur l'analyse numérique, j'ai inclus quelques ressources supplémentaires dans la conclusion.

Changeant légèrement de sujet, nous allons maintenant parler des systèmes.

## Qu'est-ce qu'un système en traitement du signal ?

Un système est une combinaison de nombreuses "choses" qui fonctionnent ensemble comme si elles étaient un tout.

Un exemple de système pourrait être un ordinateur ou une voiture.

En traitement du signal, un système est souvent une combinaison de logiciels et de matériel dans une technologie qui prend un signal d'entrée et produit un signal de sortie.

Par exemple, lorsque vous appuyez sur la pédale d'accélération dans une voiture (entrée), la voiture va plus vite (sortie).

Connaître les caractéristiques d'un système est important pour comprendre comment il traitera le signal.

Quatre caractéristiques importantes d'un système sont :

* La causalité
* La mémoire
* L'invariance temporelle
* La linéarité

Mais, pourquoi est-il important de comprendre les principales caractéristiques d'un système en programmation ?

En comprenant ces caractéristiques, vous comprendrez mieux comment concevoir des logiciels (dans ce cas, le système peut être vu comme un logiciel) ainsi que comment les optimiser et les intégrer.

Connaître ces caractéristiques est très important en ingénierie des systèmes où elles sont appliquées au développement de logiciels. Elles vous aident à gérer la complexité des programmes, à définir leurs exigences et à assurer la qualité, l'adaptabilité et l'évolutivité.

Si vous souhaitez en apprendre davantage sur l'ingénierie des systèmes, [vous pouvez lire mon article à ce sujet](https://www.freecodecamp.org/news/what-is-systems-engineering/).

Alors, apprenons-en plus sur ce que chacune de ces caractéristiques représente.

### Causalité

La causalité est la propriété d'un système où la sortie dépend uniquement des entrées passées et présentes.

Par exemple, lors de la prédiction de la météo, il n'est possible d'utiliser que les données météorologiques passées pour faire une prévision. 

Il n'est pas possible d'utiliser les données météorologiques futures pour prédire la météo.

### Mémoire

La mémoire est la propriété d'un système où la sortie dépend des entrées passées.

Les systèmes de recommandation utilisés par des sites comme Netflix et Amazon suggèrent des films ou des produits en fonction des interactions précédentes d'un utilisateur.

Les algorithmes prennent en compte les produits consultés ou achetés, et utilisent ces informations pour recommander des articles similaires.

Avec plus de données collectées au fil du temps, les recommandations deviennent plus précises et personnalisées.

La mémoire est importante en programmation car elle nous permet de créer des systèmes capables d'apprendre et de s'adapter au fil du temps – par exemple, les systèmes de machine learning.

### Invariance temporelle

L'invariance temporelle est la propriété d'un système lorsque la sortie ne dépend pas du moment où l'entrée a été appliquée.

Les systèmes de contrôle en temps réel utilisés en robotique, en fabrication et dans les applications aérospatiales reposent sur des systèmes invariants dans le temps.

Par exemple, un système de contrôle de vol doit répondre rapidement et avec précision aux changements de position d'un aéronef, indépendamment du moment où ils se produisent.

### Linéarité

La linéarité en programmation est comme une recette où doubler les ingrédients entraîne un résultat proportionnellement doublé, permettant des résultats prévisibles et précis.

La linéarité fait référence à la propriété d'un système où la sortie est directement proportionnelle à l'entrée.

Cela signifie que si l'entrée est doublée, la sortie sera également doublée.

Par exemple, en traitement d'image numérique, la linéarité est utilisée dans des techniques telles que l'ajustement du contraste et la correction des couleurs pour garantir que la sortie est proportionnelle à l'entrée. 

Cela permet un traitement d'image prévisible et précis.

## Conclusion

Le traitement du signal et les systèmes sont essentiels pour la programmation car ils nous permettent de traiter, manipuler et analyser les données de manière fiable et prévisible.

Que vous travailliez sur le traitement audio, le traitement d'image ou toute autre application impliquant le traitement du signal, comprendre les fondamentaux du traitement du signal et des systèmes est crucial pour réussir.

Les systèmes sont étroitement liés au traitement du signal, car ils permettent la transformation du signal pour que les programmeurs et les ingénieurs atteignent leur objectif souhaité.

Si vous êtes intéressé à en apprendre davantage sur la transformée de Fourier, voici une vidéo YouTube qui l'explique plus en détail :

%[https://www.youtube.com/watch?v=spUNpyF58BY]

Voici une vidéo YouTube expliquant l'algorithme qui s'exécute réellement sur votre ordinateur :

%[https://www.youtube.com/watch?v=h7apO7q16V0]

Et voici également une vidéo détaillant l'histoire du développement de la transformée de Fourier rapide :

%[https://www.youtube.com/watch?v=nmgFG7PUHfo]

## Note finale

Il existe d'autres transformées utilisées pour le traitement du signal et d'autres fins, telles que la transformée de Laplace (utilisée pour les signaux continus) et la transformée en Z (utilisée pour les signaux discrets).

Mais, comme il existe tant de formules de transformées mathématiques, qu'est-ce qu'une transformée réellement ?

Une transformée est simplement un outil mathématique qui nous aide à voir quelque chose d'un point de vue différent.

En voyant les choses différemment, nous pouvons découvrir des détails que nous n'avions pas vus initialement.

Par exemple, avec la transformée de Fourier, nous pouvons voir le signal du point de vue de la fréquence au lieu du point de vue du temps.

Cela nous permet de voir la même chose d'une manière différente.

Mathématiquement, nous pouvons dire que nous changeons le domaine de la fonction. En d'autres termes, nous changeons l'axe des x.

Et je vous laisse avec ceci : la transformée de Laplace est une transformée de Fourier généralisée.

### Code complet :

%[https://github.com/tiagomonteiro0715/Signal-Processing-and-Systems-in-Programming-Guide-for-Beginners]