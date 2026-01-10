---
title: 'Comment construire un système de contrôle de fusée : théorie de base du contrôle
  avec Python'
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-08-06T14:26:44.000Z'
originalURL: https://freecodecamp.org/news/basic-control-theory-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-pixabay-2159.jpg
tags:
- name: control theory
  slug: control-theory
- name: Control Systems
  slug: control-systems
- name: Python
  slug: python
- name: System Design
  slug: system-design
seo_title: 'Comment construire un système de contrôle de fusée : théorie de base du
  contrôle avec Python'
seo_desc: 'Building any control systems, including a rocket control system, involves
  combining control theory with programming.

  Control theory is the study of how to make systems behave in a desired way using
  inputs.

  Planes, cars, trains, circuits, rockets and ...'
---

La construction de systèmes de contrôle, y compris un système de contrôle de fusée, implique de combiner la théorie du contrôle avec la programmation.

La théorie du contrôle est l'étude de la manière de faire en sorte que les systèmes se comportent de la manière souhaitée en utilisant des entrées.

Les avions, les voitures, les trains, les circuits, les fusées et bien d'autres systèmes doivent avoir un cerveau ou une architecture à l'intérieur.

La théorie du contrôle est l'étude des architectures de contrôle de ces systèmes complexes.

Dans cet article, nous explorerons comment appliquer la théorie du contrôle pour créer un système de contrôle de fusée en utilisant Python.

Il s'agit d'un guide simple sur la manière dont l'architecture des systèmes complexes est créée. Dans ce cas, il est basé sur une fusée.

Dans cet article, vous apprendrez :

* [Systèmes de fusée et cuisson de gâteaux : une comparaison amusante](#heading-systemes-de-fusee-et-cuisson-de-gateaux-une-comparaison-amusante)
* [Contrôle de fusée simplifié : comprendre les contrôleurs PID](#heading-controle-de-fusee-simplifie-comprendre-les-controleurs-pid)
* [Exemple de code : conception d'un contrôleur PID simple](#heading-exemple-de-code-conception-dun-controleur-pid-simple)
* [Conclusion : systèmes de contrôle non linéaires](#heading-conclusion-systemes-de-controle-non-lineaires)

**Note :** Nous supposerons que la fusée est invariante dans le temps, ce qui signifie que son comportement ne change pas avec le temps. Aborder les dynamiques variant dans le temps compliquerait ce tutoriel plus que je ne le souhaiterais.

<h2 id="Cake">Systèmes de fusée et cuisson de gâteaux : une comparaison amusante</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/08/cake.jpg)
_Photo par [Brent Keane sur Pexels](https://www.pexels.com/photo/white-icing-cover-cake-1702373/)_

### Qu'est-ce qu'un système de contrôle de fusée ?

Imaginez que vous êtes en train de cuire un gâteau. Votre recette fournit les étapes et les ingrédients nécessaires pour cuire le gâteau.

Dans cette analogie :

* Le gâteau est la fusée
* La recette est le plan de vol de la fusée
* Les actions du boulanger sont le système de contrôle de la fusée

Tout comme vous changez la température du four ou le temps de mélange pour obtenir le meilleur gâteau, un système de contrôle change les paramètres de la fusée pour s'assurer qu'elle reste sur sa trajectoire et reste stable.

### Pourquoi les systèmes de contrôle sont-ils importants en programmation ?

En comprenant les systèmes de contrôle, vous deviendrez meilleur en conception algorithmique et en pensée systémique.

Cela vous permet également de déterminer comment ajuster les processus dans les boucles de rétroaction. Cela est très important dans de nombreux domaines de la programmation.

Vous utiliserez principalement la théorie du contrôle et les systèmes de contrôle lors de la création de logiciels pour :

* **Robotique et automatisation** : Les systèmes de contrôle permettent des mouvements précis et une adaptabilité des robots en utilisant des boucles de rétroaction basées sur les entrées des capteurs.
* **Traitement du signal et communication** : Ils optimisent la transmission de données, la correction d'erreurs et le filtrage pour une communication fiable.
* **Systèmes embarqués et IoT** : Les systèmes de contrôle gèrent les interactions des appareils avec les environnements, traitent les entrées des capteurs et ajustent les sorties de manière efficace.

### Comment créer un système de contrôle de fusée

En termes de notre analogie de cuisson de gâteau :

1. **Choisir le gâteau et la recette** : Sélectionnez une stratégie de contrôle simple, comme choisir une recette de gâteau de base. Un choix courant est un contrôleur PID car il est simple et efficace.
2. **Comprendre les ingrédients** : Déduisez un modèle mathématique des caractéristiques et de la trajectoire de la fusée. Comme étudier la recette et les ingrédients. De cette manière, nous obtenons une compréhension claire du système.
3. **Rassembler les ingrédients initiaux** : Définissez les paramètres initiaux, similaires à la collecte de vos ingrédients de base.
4. **Mélanger et cuire** : Ajustez et testez le système, un peu comme mélanger les ingrédients et cuire. Cela implique l'utilisation de divers graphiques pour vérifier la stabilité et les performances.
5. **Ajouter les touches finales** : Affinez les paramètres, tout comme ajouter les dernières décorations à votre gâteau, pour optimiser le système de contrôle pour l'efficacité.
6. **Suivre la recette** : Convertissez votre conception en une forme pratique, comme suivre attentivement une recette de gâteau.

<h2 id="Rocket">Contrôle de fusée simplifié : comprendre les contrôleurs PID</h2>

### Un système de contrôle simple : le contrôleur PID

![Image](https://www.freecodecamp.org/news/content/images/2024/07/M6_ControlSystemsdiagram.png)
_Exemple de diagramme de système de contrôle ([source](https://edtech.engineering.utoronto.ca/object/control-systems-diagrams))_

Chaque système de contrôle possède un contrôleur qui le fait fonctionner. L'un des contrôleurs les plus utilisés est le contrôleur PID.

Dans l'exemple de code ici, nous utiliserons le contrôleur PID. Cela est dû à sa simplicité et à son efficacité pour les systèmes de contrôle simples.

Dans un système de contrôle de fusée, le contrôleur PID de la fusée ajuste constamment la trajectoire de la fusée (bloc de traitement) en comparant sa position actuelle à celle où elle devrait être (bloc de rétroaction).

De cette manière, la fusée reste sur sa trajectoire et atteint sa destination finale.

Le contrôleur PID possède trois parties clés qui fonctionnent dans la partie de traitement et de rétroaction du système : le gain proportionnel (Kp), le gain intégral (Ki) et le gain dérivé (Kd).

* **Le gain proportionnel (Kp)** : Réagit immédiatement à toute erreur, faisant en sorte que le système réponde rapidement mais provoquant parfois un dépassement de la cible.
* **Le gain intégral (Ki)** : Corrige les erreurs passées en les additionnant au fil du temps, éliminant toute erreur résiduelle, mais il peut rendre le système instable s'il est réglé trop haut.
* **Le gain dérivé (Kd)** : Prédit les erreurs futures pour aider à prévenir les dépassements et lisser la réponse du système.

C'est pourquoi il est appelé un contrôleur PID (Proportionnel-Intégral-Dérivé).

Ces trois parties travaillent ensemble pour créer un signal de contrôle qui modifie les paramètres de la fusée. Cela garantit qu'elle est stable, précise et efficace.

Avec le contrôleur PID, nous pouvons contrôler comment les entrées comme la poussée et l'altitude changent la position et la vitesse pour assurer la stabilité de la fusée et qu'elle reste sur sa trajectoire prévue.

### Analyser la stabilité

![Image](https://www.freecodecamp.org/news/content/images/2024/08/stability.jpg)
_Photo par [Shiva Smyth sur Pexels](https://www.pexels.com/photo/closeup-photography-of-stacked-stones-1051449/)_

Concevoir un contrôleur PID signifie concevoir un système de contrôle stable.

Le processus de conception d'un système de contrôle stable est appelé analyse de stabilité.

Il existe de nombreuses méthodes, mais dans l'exemple de code, nous utiliserons :

* **Lieu des racines** : Montre la stabilité et la réponse du système
* **Diagramme de Bode** : Affiche les marges de gain et de phase du système
* **Diagramme de Nyquist** : Illustre la stabilité et les oscillations potentielles

Dans ce cas, les marges de gain et de phase signifient simplement que le système de contrôle peut tolérer des changements.

La marge de gain nous indique combien le gain du système peut augmenter sans perdre de stabilité. Le gain signifie combien amplifier le signal d'entrée pour faire le signal de sortie.

La marge de phase nous indique combien de retard est tolérable sans perdre de stabilité. Le retard en théorie du contrôle signifie combien de temps il faut pour que la sortie réponde à l'entrée.

Cela nous indique comment changer les Kp, Ki et Kd afin que le contrôleur PID puisse contrôler la fusée de manière efficace.

### Le besoin de fonctions de transfert : contrôler la fusée et déterminer les valeurs des composants

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Transfer-function-v2.png)

Pour implémenter un système de contrôle, nous avons besoin de deux fonctions de transfert : une théorique et une physique.

Les fonctions de transfert nous indiquent comment les entrées se convertissent en sorties de manière mathématique.

La fonction théorique est, dans ce cas, le contrôleur PID.

La fonction de transfert du système physique représente la dynamique et le comportement du monde réel des composants physiques du système.

En combinant les deux, nous pouvons comprendre le comportement des matériaux et les valeurs des composants tels que :

* Valeurs des condensateurs pour le stockage d'énergie
* Valeurs d'étalonnage des capteurs pour une mesure de données précise et une rétroaction
* Constantes de ressort pour les systèmes d'absorption des chocs
* Classifications de pression pour les réservoirs de carburant et d'oxydant

De cette manière, le contrôleur PID n'est pas seulement le cerveau de la fusée, mais peut également nous indiquer les valeurs des composants nécessaires pour que la fusée puisse voler sur sa trajectoire.

### Comment les ingénieurs trouvent-ils l'équation de la fonction de transfert physique ?

Tout d'abord, nous devons comprendre à quoi sert la fusée.

Enverra-t-elle un satellite LEO (orbite terrestre basse) ou MEO (orbite terrestre moyenne) dans l'espace ou une fusée sur la lune ?

Après avoir connu son cas d'utilisation, nous pouvons, avec les mathématiques et la physique, trouver l'équation physique de la fonction de transfert.

Il existe en fait un domaine entier de l'ingénierie appelé **identification des systèmes** dédié à cela.

Maintenant, voyons comment trouver, pour tout système de contrôle, sa fonction de transfert physique.

<h2 id="Code">Exemple de code : conception d'un contrôleur PID simple</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/08/rocket.jpg)
_Photo par [Pixabay](https://www.pexels.com/photo/space-rocket-launching-73871/)_

Maintenant, avec cet exemple de code, nous allons créer un système de contrôle simple pour une fusée.

Avant de plonger dans le code, parlons des décibels.

Les décibels utilisent une échelle logarithmique pour mesurer le son. En théorie du contrôle, ils mesurent le gain d'une manière plus facile à visualiser sur les graphiques.

De cette manière, nous pouvons voir beaucoup plus de grandes et petites valeurs dans une plage gérable.

En d'autres termes, en voyant le gain sur une échelle logarithmique, nous voyons combien l'entrée est amplifiée pour être la sortie dans une plage gérable de valeurs.

Je vais également expliquer comment le lieu des racines, le diagramme de Bode et les diagrammes de Nyquist aident les ingénieurs dans l'analyse de stabilité.

Regardons le code – puis nous l'analyserons bloc par bloc :

```
# Étape 1 : Importer les bibliothèques
import matplotlib.pyplot as plt
import control as ctrl

# Étape 2 : Définir une nouvelle fonction de transfert de fusée avec des pôles plus proches de l'axe imaginaire
num = [10] 
den = [2, 2, 1] 
G = ctrl.TransferFunction(num, den)

# Étape 3 : Concevoir un contrôleur PID avec de nouveaux paramètres
Kp = 5
Ki = 2
Kd = 1
C = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Étape 4 : Appliquer le contrôleur PID à la fonction de transfert de la fusée
CL = ctrl.feedback(C * G, 1)

# Étape 5 : Tracer le lieu des racines pour le système en boucle fermée
plt.figure(figsize=(10, 6))
ctrl.root_locus(C * G, grid=True)
plt.title("Tracé du lieu des racines (boucle fermée)")

# Étape 6 : Tracer le diagramme de Bode pour le système en boucle fermée
plt.figure(figsize=(10, 6))
ctrl.bode_plot(CL, dB=True, Hz=False, deg=True)
plt.suptitle("Diagramme de Bode (boucle fermée)", fontsize=16)

# Étape 7 : Tracer le diagramme de Nyquist pour le système en boucle fermée
plt.figure(figsize=(10, 6))
ctrl.nyquist_plot(CL)
plt.title("Diagramme de Nyquist (boucle fermée)")

plt.show()

```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/1.png)
_Code complet_

### Étape 1 : Importer les bibliothèques

```
import matplotlib.pyplot as plt
import control as ctrl
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/2.png)
_Importation des bibliothèques_

Ici, nous importons deux bibliothèques :

* [matplotlib](https://matplotlib.org/) : Une bibliothèque de traçage pour créer divers types de visualisations
* [Control](https://python-control.readthedocs.io/en/0.10.0/) : Une bibliothèque pour analyser et concevoir des systèmes de contrôle

### Étape 2 : Définir la fonction de transfert du système de fusée

```
num = [10] 
den = [2, 2, 1] 
G = ctrl.TransferFunction(num, den)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/3.png)
_Définir la fonction de transfert du système de fusée_

Dans ce code, nous définissons la fonction de transfert du système physique

* **`num=[10]`** : Définit le gain du système à 10.
* **`den=[2,2,1]`** : Définit le dénominateur.
* **`G = ctrl.transferFunction(num, cen)`** : Construit la fonction de transfert.

C'est la fonction de transfert que nous allons contrôler avec le PID :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Black-Scholes Equation</title>
</head>
<body>
    <div class="card">
        <div class="card-body">
            <p class="card-text">
                $$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV - rS \frac{\partial V}{\partial S}$$
            </p>
            <h5 class="card-title" style="text-align: center;">Fonction de transfert de la fusée
          </h5>
        </div>
    </div>
</body>
</html>


Dans cet exemple de code, l'équation de la fonction de transfert de la fusée est très simple. Mais dans la vie réelle, les fonctions de transfert des fusées ne sont pas des systèmes linéaires invariants dans le temps. Habituellement, ce sont des systèmes non linéaires très complexes.

### Étape 3 : Concevoir un contrôleur PID avec de nouveaux paramètres

```
Kp = 5
Ki = 2
Kd = 1
C = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/4.png)
_Concevoir un contrôleur PID avec de nouveaux paramètres_

Ce code configure un contrôleur PID avec des gains spécifiques et crée une fonction de transfert :

* **`Kp = 5`** : Définit le gain proportionnel à 5.
* **`Ki = 2`** : Définit le gain intégral à 2.
* **`Kd = 1`** : Définit le gain dérivé à 1.
* **`C = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])`** : Crée une fonction de transfert du contrôleur PID

### Étape 4 : Appliquer le contrôleur PID à la fonction de transfert de la fusée

```
CL = ctrl.feedback(C * G, 1)

```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/5.png)
_Appliquer le contrôleur PID à la fonction de transfert de la fusée_

* **`C * G`** : Multiplie le contrôleur PID `C` avec le système `G` (la fusée) pour former la fonction de transfert en boucle ouverte, qui modélise le comportement du système sans rétroaction et repose sur des paramètres prédéfinis.
* **`ctrl.feedback(C * G, 1)`** : Calcule la fonction de transfert en boucle fermée en appliquant la rétroaction et en représentant le comportement du système avec rétroaction. Cela lui permet d'ajuster les entrées et de corriger automatiquement les erreurs.
* **`CL`** : Stocke le système en boucle fermée résultant, intégrant le contrôleur avec la fusée pour maintenir les performances souhaitées grâce à la rétroaction, et est utilisé pour une analyse ou une simulation ultérieure.

### Étape 5 : Lieu des racines pour l'analyse du gain

Dans ce code :

```
plt.figure(figsize=(10, 6))
ctrl.root_locus(C * G, grid=True)
plt.title("Tracé du lieu des racines (boucle fermée)")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/6.png)
_Créer le graphique du lieu des racines_

Nous générons ce graphique :

![Image](https://www.freecodecamp.org/news/content/images/2024/08/root-locus.png)
_Graphique simple du lieu des racines_

Il s'agit d'un graphique du lieu des racines. Il a été inventé pour aider les ingénieurs à étudier la stabilité des systèmes de contrôle.

Les croix sur le graphique, appelées pôles, sont très importantes.

S'ils sont du côté gauche du graphique, le système est stable. S'ils sont du côté droit, le système est instable.

Plus ils sont à gauche, plus le système reviendra rapidement à la normale après une perturbation, et ainsi, plus il sera stable.

Mais se déplacer plus à gauche peut causer trop d'oscillations, selon leurs emplacements spécifiques.

Le point clé est :

* En changeant le **`Kp`**, `Ki`, et **`Kd`**, cela déplace les pôles pour qu'ils soient aussi loin à gauche que possible sans causer d'oscillations.

Cependant, le graphique du lieu des racines n'est pas suffisant pour garantir la stabilité. Nous devons également utiliser les graphiques de Bode et de Nyquist. Seulement avec eux pouvons-nous obtenir les meilleures valeurs du contrôleur PID pour le système de contrôle de la fusée.

### Étape 6 : Diagramme de Bode pour l'analyse de stabilité

Dans ce code :

```
plt.figure(figsize=(10, 6))
ctrl.bode_plot(CL, dB=True, Hz=False, deg=True)
plt.suptitle("Diagramme de Bode (boucle fermée)", fontsize=16)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/7.png)
_Créer le graphique du diagramme de Bode_

Nous générons ce graphique :

![Image](https://www.freecodecamp.org/news/content/images/2024/08/bode.png)
_Diagramme de Bode simple_

Le diagramme de Bode a été inventé pour aider les ingénieurs à comprendre comment un système répond aux changements et à quel point il sera stable dans différentes conditions.

Le diagramme de Bode montre également la stabilité du système et les marges de sécurité.

Comprenons comment il fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2024/08/detail-bode.png)
_Diagramme de Bode en détail_

Le graphique du haut est appelé le graphique de magnitude et celui du bas est appelé le graphique de phase.

Le graphique de magnitude mesure le gain d'un système à travers différentes fréquences. Un gain plus élevé signifie des réactions plus rapides et plus fortes, ce qui est bon pour un contrôle précis.

Le graphique de phase mesure le déphasage introduit par le système à travers différentes fréquences. Le déphasage est observé lorsque le gain est de 0.

Dans ce cas, nous pouvons voir avec la ligne verte lorsque le gain est zéro et quel déphasage est associé à cela dans la ligne rouge. Il est d'environ 63 degrés.

Une plage idéale est un déphasage de 30 à 60 degrés, ce qui équilibre la stabilité et la vitesse de réponse.

Au-dessus de 60 degrés, le système est très stable, mais peut ralentir la réponse du système aux changements.

Ainsi, après avoir analysé le graphique, nous pouvons conclure que ce contrôleur PID est stable.

### Étape 7 : Diagramme de Nyquist pour l'analyse de stabilité

Dans ce code :

```
plt.figure(figsize=(10, 6))
ctrl.nyquist_plot(CL)
plt.title("Diagramme de Nyquist (boucle fermée)")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/08/8.png)
_Créer le graphique du diagramme de Nyquist_

Nous générons ce graphique :

![Image](https://www.freecodecamp.org/news/content/images/2024/08/nyquist.png)
_Graphique du diagramme de Nyquist_

Le diagramme de Nyquist est un outil pour aider les ingénieurs à vérifier rapidement si un système de contrôle est stable ou non.

C'est très simple :

* S'il n'y a pas de cercle autour de la croix rouge au point (-1 0), le système est stable.
* S'il y a des cercles autour de la croix rouge, notamment des cercles dans le sens des aiguilles d'une montre, au point (-1 0), le système est instable.

Puisqu'il n'y a pas de cercles autour de la croix rouge, ce système de contrôle est stable.

### Dernière étape après la conception du système de contrôle de la fusée

Après avoir terminé la conception de ce système de contrôle PID, nous pouvons utiliser des outils comme [Simulink](https://www.mathworks.com/products/simulink.html) pour trouver les valeurs nécessaires de nombreux composants.

En d'autres termes, après avoir obtenu les meilleures variables du contrôleur PID, il est temps de trouver les valeurs des composants physiques de la fusée.

Certaines de ces valeurs sont :

* Valeurs des résistances pour contrôler le flux de courant
* Valeurs des condensateurs pour le stockage d'énergie
* Valeurs des inductances pour gérer les interférences électromagnétiques
* Valeurs d'étalonnage des capteurs pour une mesure de données précise et une rétroaction
* Force et durabilité des matériaux pour le corps et les ailerons de la fusée
* Exigences de couple et de vitesse pour les servomoteurs
* Constantes de ressort pour les systèmes d'absorption des chocs
* Classifications de pression pour les réservoirs de carburant et d'oxydant

Grâce à Simulink, nous pouvons obtenir toutes ces valeurs nécessaires pour concevoir une fusée selon sa mission.

Avec un système de contrôle stable, basé sur un contrôleur PID pour contrôler la fonction de transfert physique d'une fusée, nous pouvons obtenir toutes les valeurs nécessaires pour chaque composant.

<h2 id="Conclusion">Conclusion : systèmes de contrôle non linéaires</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/08/moon.jpg)
_Photo par Peter de Vink : https://www.pexels.com/photo/photo-of-full-moon-975012/_

Il existe de nombreuses méthodes disponibles pour optimiser un système de contrôle linéaire invariant dans le temps (LTI) :

1. **Méthode du lieu des racines** : Ajuste les pôles du système pour réduire les oscillations.
2. **Analyse du diagramme de Bode** : Maintient la marge de phase et la stabilité.
3. **Diagramme de Nyquist** : Confirme la stabilité globale du système.

Avec ces outils, il est possible de créer un système de contrôle.

Cependant, dans ce processus, il est bon de pratiquer l'utilisation de méthodes comme la méthode de Ziegler-Nichols pour trouver plus rapidement les meilleures variables du contrôleur PID.

Dans notre exploration, nous avons travaillé avec un système de fusée très simple.

Dans la vie réelle, seuls des outils non linéaires sont utilisés car tous les systèmes de fusée sont des systèmes non linéaires.

Un exemple est le contrôle adaptatif, où le système de contrôle s'ajuste en temps réel pour gérer les conditions changeantes.

Un autre exemple est la méthode de Lyapunov. Dans ce cas, elle est utilisée pour l'analyse de stabilité au lieu de ces trois graphiques.

Néanmoins, le processus de création de ces systèmes de contrôle est toujours le même. Cet article a expliqué comment ce processus fonctionne et comment il est appliqué dans un système invariant dans le temps.

%[https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code]