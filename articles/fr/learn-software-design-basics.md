---
title: 'Apprendre les bases de la conception logicielle : phases clés et meilleures
  pratiques'
subtitle: ''
author: Soham Banerjee
co_authors: []
series: null
date: '2025-03-07T21:25:26.455Z'
originalURL: https://freecodecamp.org/news/learn-software-design-basics
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1741188275855/9858518f-38c0-4e3b-8be1-7c56b68c77a7.png
tags:
- name: software design
  slug: software-design
- name: software architecture
  slug: software-architecture
- name: System Design
  slug: system-design
- name: TDD (Test-driven development)
  slug: tdd
- name: Coding Best Practices
  slug: coding-best-practices
- name: Software Engineering
  slug: software-engineering
- name: software development
  slug: software-development
- name: Programming Blogs
  slug: programming-blogs
- name: Developer
  slug: developer
seo_title: 'Apprendre les bases de la conception logicielle : phases clés et meilleures
  pratiques'
seo_desc: 'Coding has become one of the most common tasks in modern society. With
  computers now central to almost every field, more people are designing algorithms
  and writing code to solve various problems.

  From healthcare to finance, robust software systems p...'
---

Le codage est devenu l'une des tâches les plus courantes dans la société moderne. Avec les ordinateurs désormais centraux dans presque tous les domaines, de plus en plus de personnes conçoivent des algorithmes et écrivent du code pour résoudre divers problèmes.

De la santé à la finance, des systèmes logiciels robustes alimentent nos opérations quotidiennes, rendant une bonne conception logicielle essentielle pour éviter les inefficacités et les goulots d'étranglement. Cela implique non seulement d'écrire du code, mais aussi de concevoir des systèmes faciles à mettre à l'échelle, à maintenir et à déboguer, tout en permettant à d'autres de contribuer efficacement.

Une conception logicielle inefficace ou inefficace peut entraîner des problèmes significatifs, comme l'extension du périmètre, la mauvaise communication au sein des équipes, les retards de projet, la mauvaise allocation des ressources et des systèmes complexes difficiles à maintenir ou à comprendre. Sans une conception solide, les équipes accumulent souvent une dette technique, ce qui entrave les progrès à long terme et augmente les coûts de maintenance.

Cet article vous présentera les éléments clés de la conception logicielle qui vous aideront, vous et votre équipe, à relever ces défis et vous guidera dans la construction de systèmes efficaces et évolutifs. En comprenant et en appliquant correctement ces éléments, vous pouvez configurer un projet pour un succès à court et à long terme.

## **Prérequis**

Je vais expliquer ces concepts à travers des exemples, mais une compréhension de base de la programmation dans n'importe quel langage est requise pour cet article (la connaissance de Python sera particulièrement bénéfique).

## **Portée**

L'article présentera les éléments clés de la conception logicielle et les expliquera à l'aide d'un exemple. Bien que je ne fournirai pas une conception logicielle complète pour le problème d'exemple, j'inclurai suffisamment de détails pour illustrer efficacement chaque élément de conception.

## Table des matières

* [Aperçu des éléments clés de la conception logicielle](#heading-aperçu-des-éléments-clés-de-la-conception-logicielle)
    
* [Un guide du processus de conception logicielle](#heading-un-guide-du-processus-de-conception-logicielle)
    
    * [Énoncé du problème](#heading-énoncé-du-problème)
        
    * [Cas d'utilisation](#heading-cas-dutilisation)
        
    * [Exigences](#heading-exigences)
        
    * [Architecture du système de haut niveau](#heading-architecture-du-système-de-haut-niveau)
        
    * [Conception logicielle détaillée et décomposition des composants](#heading-conception-logicielle-détaillée-et-décomposition-des-composants)
        
* [Conclusion : La valeur d'une conception logicielle réfléchie](#heading-conclusion-la-valeur-dune-conception-logicielle-réfléchie)
    

## **Aperçu des éléments clés de la conception logicielle**

Pour comprendre pleinement les avantages du processus de conception logicielle, vous devrez comprendre certains éléments clés et leur portée.

Une fois que vous aurez une bonne compréhension de ceux-ci, l'étape suivante consiste à les définir pour le problème spécifique en question. La définition précise de ces éléments réduit les risques et simplifie la phase de mise en œuvre.

Faire ce travail préparatoire avant la mise en œuvre aide à prévenir les découvertes tardives, minimise le besoin de réécriture et garantit que la conception peut gérer les contraintes et les cas particuliers.

Passons maintenant brièvement en revue les éléments clés du processus de conception logicielle :

1. **Création d'un énoncé de problème** : Cette étape consiste à créer une description claire et concise du problème à résoudre, ainsi que de sa portée. La portée est essentielle car elle se concentre sur le problème exact à traiter et inclut les hypothèses qui doivent être prises en compte lors de la conception.
    
2. **Identification des cas d'utilisation** : Cette étape décrit toutes les interactions possibles de l'utilisateur avec le logiciel pour atteindre le résultat souhaité. C'est une entrée cruciale pour l'architecture, car elle aide à créer une conception qui répond aux cas d'utilisation généraux et particuliers.
    
3. **Énonciation des exigences** : Cette étape définit les attentes du logiciel, telles que ses limitations, ses comportements et ses capacités pour différents cas d'utilisation.
    
4. **Conception de l'architecture** : Cette étape fournit une structure de haut niveau de la conception logicielle, en se concentrant sur la manière de répondre aux exigences. L'architecture comprend généralement des composants, leurs interactions et le flux de données à travers le système.
    
5. **Rédiger une conception détaillée** : Cette étape affine l'architecture de haut niveau en conceptions détaillées, spécifiques aux composants, prêtes pour la mise en œuvre.
    

En plus de ces éléments de base, il y a deux facteurs importants que vous devez prendre en compte tout au long de la phase de conception.

Tout d'abord, vous devrez identifier et énoncer toutes les hypothèses que vous avez. Les hypothèses peuvent être présentes à n'importe quelle étape du processus de conception. Faire des hypothèses correctes augmente les chances de succès, améliore la concentration et réduit la complexité de la conception.

Deuxièmement, vous devrez créer une bonne documentation. La documentation est l'un des éléments les plus importants du processus de conception logicielle. Il est essentiel de documenter chaque étape au fur et à mesure. La documentation sert de seul enregistrement formel de la conception logicielle et est inestimable pour les présentations à la direction, pour l'intégration de nouveaux membres de l'équipe et pour toute personne revenant au projet après une pause. Elle économise un temps précieux et assure la continuité, car nous surestimons souvent notre propre mémoire.

La figure ci-dessous fournit un résumé visuel des éléments clés de la conception logicielle discutés dans cette section.

![Figure 1: Éléments clés de la conception logicielle](https://cdn.hashnode.com/res/hashnode/image/upload/v1738540359869/2ee49614-84b1-439a-ae7e-af637c0f34dd.png?auto=compress,format&format=webp align="left")

Ensuite, nous appliquerons ces éléments clés de la conception logicielle à un exemple pratique, démontrant comment chaque élément contribue à la construction d'un système robuste et évolutif.

## **Un guide du processus de conception logicielle**

Dans tout projet logiciel bien structuré, la définition claire du problème est la première étape cruciale avant de plonger dans la conception et la mise en œuvre. Un problème bien défini garantit que le logiciel répond aux besoins des utilisateurs, reste maintenable et évolue efficacement au fil du temps.

Pour ce guide, nous nous concentrerons sur la conception d'un système de catégorisation des dépenses financières qui traite et analyse les données de transaction. Ce système fait partie d'une solution de gestion financière plus large et doit être facile à déboguer, à maintenir et à mettre à l'échelle.

### **Énoncé du problème**

L'énoncé du problème fournit un objectif de haut niveau pour le logiciel que nous allons concevoir.

Pour cet exemple, voici notre énoncé : Concevoir une solution logicielle qui catégorise les dépenses mensuelles et génère un rapport à partir d'une liste de transactions.

#### **Définir la portée**

Définir la portée clarifie les petites tâches qui doivent être accomplies pour atteindre l'objectif de haut niveau. Elle décrit le focus de la conception logicielle et inclut certaines hypothèses.

Inclut :

1. Mise en œuvre d'un analyseur pour traiter une liste de transactions fournies en entrée.
    
2. Filtrage des transactions pour un mois donné.
    
3. Analyse, catégorisation et génération d'un rapport pour chaque catégorie de dépenses.
    

Exclut :

Optimisation des performances et de la mémoire (exclue en raison de la portée limitée de cet article). Bien que les optimisations de performance et de mémoire ne soient pas l'objectif principal ici, il est important de garder à l'esprit la scalabilité future. De petits choix de conception faits maintenant, comme la sélection des structures de données, peuvent aider à éviter des refactorisations importantes plus tard lorsque le système grandit.

Hypothèses :

1. La liste des transactions sera fournie sous forme de fichier CSV dans le format suivant :
    Colonnes : "Date, Description, Montant, Type, Étiquette de catégorie".
    
2. Les catégories de dépenses seront fournies en entrée via un fichier JSON.
    
3. Le logiciel s'exécutera dans un environnement shell, et les entrées seront prises en tant qu'arguments de ligne de commande.
    

Maintenant que la portée est claire, examinons comment les utilisateurs interagiront avec le système à travers divers cas d'utilisation.

### **Cas d'utilisation**

Les cas d'utilisation définissent comment les utilisateurs interagiront avec le système pour accomplir des objectifs spécifiques. L'identification de cas d'utilisation précis et valides est cruciale pour créer des exigences complètes. Ne pas capturer suffisamment de cas d'utilisation peut conduire à une conception incomplète et manquant de robustesse. Cela peut entraîner le besoin de reconceptions, ce qui augmente le temps et la consommation de ressources.

D'un autre côté, identifier trop de cas d'utilisation sans considérer leur faisabilité peut conduire à des conceptions trop complexes qui sont difficiles à maintenir et à mettre en œuvre à court terme.

Pour notre problème spécifique, l'utilisateur devra fournir les entrées suivantes lors de l'exécution du logiciel dans un shell :

1. Un fichier CSV contenant une liste de transactions.
    
2. Un numéro de mois.
    
3. Un fichier JSON contenant les catégories de dépenses.
    

Nous devons considérer toutes les façons possibles dont l'utilisateur peut interagir avec le script pour atteindre le résultat souhaité. Pour chacune des trois entrées, il y a deux possibilités : entrée valide ou entrée invalide. Cela nous donne 8 cas d'utilisation potentiels (2 possibilités par entrée : valide et invalide). Il est important de définir ce qui constitue des entrées valides et invalides pour ce problème :

* Fichier CSV : Valide s'il est au format décrit dans l'hypothèse 1 (colonnes : "Date, Description, Montant, Type, Étiquette de catégorie").
    
* Numéro de mois : Valide si la valeur est comprise entre 1 et 12.
    
* Fichier JSON : Valide s'il contient des catégories de dépenses au format JSON correct.
    

Une entrée est invalide si elle ne répond pas à ces définitions ou si l'entrée est absente.

Il est également crucial de considérer la corrélation entre les entrées lors de l'évaluation de la faisabilité de certains cas d'utilisation, car elles peuvent interagir entre elles de manière imprévue. Sur la base de ces cas d'utilisation, nous pouvons maintenant définir les exigences spécifiques que le système doit satisfaire.

### **Exigences**

Maintenant, définissons les comportements attendus, les limitations et les capacités pour chaque cas d'utilisation. Les exigences servent de fondement à l'architecture, aux spécifications et à la mise en œuvre. Sur la base de notre énoncé de problème, le logiciel devra accomplir les tâches suivantes :

1. Le script doit prendre trois entrées : un fichier CSV de transactions, un numéro de mois et un fichier JSON de catégories de dépenses.
    
2. Le script doit vérifier toutes les entrées.
    
3. Le script doit générer une erreur et quitter si le fichier CSV ne peut pas être ouvert ou s'il ne correspond pas au format de l'hypothèse 1.
    
4. Le script doit générer une erreur et quitter si le fichier JSON ne peut pas être ouvert.
    
5. Le script doit générer une erreur si le numéro de mois n'est pas compris entre 1 et 12.
    
6. Le script doit analyser chaque transaction et la charger dans une structure de données.
    
7. Le script doit filtrer les transactions par le mois spécifié.
    
8. Le script doit charger les catégories de dépenses à partir du fichier JSON dans une structure de données.
    
9. Le script doit catégoriser les transactions en fonction de l'étiquette de catégorie fournie dans le fichier CSV.
    
10. Le script doit générer une exception si une étiquette de catégorie dans le fichier CSV n'est pas présente dans les catégories de dépenses.
    
11. Le script doit utiliser une fonction de catégorisation pour attribuer les transactions aux catégories du fichier JSON.
    
12. Une classe doit encapsuler les transactions catégorisées, fournissant des API pour les modifier ou y accéder.
    
13. Le script doit prendre en charge le calcul des statistiques et la génération de rapports pour les transactions catégorisées.
    

Avec les exigences en place, nous pouvons maintenant concevoir une architecture de haut niveau pour répondre à ces besoins.

### **Architecture du système de haut niveau**

À ce stade, nous allons concevoir le système à un niveau élevé, un peu comme créer un plan directeur. L'architecture implique d'organiser les fonctions du logiciel en composants distincts, illustrant comment ils interagissent et cartographiant le flux de contrôle et de données à travers le système. Lors de la conception de l'architecture dans ce tutoriel, nous incorporerons de bons principes de conception.

Pour cet exemple, les exigences de haut niveau incluent :

1. Chargement des entrées et vérification.
    
2. Application d'un filtrage basé sur le temps.
    
3. Catégorisation des transactions en fonction des étiquettes de catégorie et des descriptions.
    
4. Gestion des transactions catégorisées dans un registre financier.
    
5. Génération de rapports à partir des données catégorisées.
    

Un composant important de l'architecture logicielle est la télémétrie. La télémétrie collecte des données sur le comportement du logiciel, ce qui est inestimable pour le débogage et l'évaluation des performances dans des environnements réels.

Pour les systèmes plus petits, des mécanismes de journalisation plus simples peuvent suffire pour suivre les erreurs de base et surveiller les performances. La décision de mettre en œuvre la télémétrie doit dépendre de la complexité du système et des exigences opérationnelles.

Étant donné que la télémétrie fournit une boucle de rétroaction si utile pour améliorer la conception dans les itérations futures, nous l'ajouterons à la liste des composants ici.

Nous construirons notre architecture système autour d'une approche de développement piloté par les tests (TDD). Nous concevrons chaque composant en gardant à l'esprit les tests pour nous assurer qu'il répond à nos exigences.

Gardez simplement à l'esprit que bien que le TDD soit une pratique solide pour garantir la qualité du code, il peut ne pas être le meilleur choix pour tous les projets. Dans les scénarios où vous avez besoin de prototypage rapide ou de développement exploratoire, les tests peuvent être priorisés après les itérations initiales. L'équilibre entre le TDD et d'autres méthodologies dépend du contexte du projet et des préférences de l'équipe.

Notre architecture suivra une structure modulaire, ce qui signifie que le système sera divisé en composants autonomes. Chaque composant sera responsable d'une fonctionnalité spécifique, rendant le système plus facile à tester, à maintenir et à mettre à l'échelle.

Pour y parvenir, l'architecture mettra l'accent sur un couplage lâche entre les composants. Chaque composant interagira avec les autres par le biais d'interfaces ou d'API bien définies, garantissant des dépendances minimales. Nous abstraierons et encapsulerons les détails de mise en œuvre internes, exposant uniquement les informations nécessaires à l'interaction. De plus, chaque composant gérera ses propres erreurs et exceptions pour garantir la robustesse et l'isolement des pannes.

Mais il est également important de considérer une stratégie de gestion des erreurs centralisée dans certains cas. La centralisation de la gestion des erreurs peut réduire la redondance, améliorer la cohérence et faciliter la maintenance. Le choix entre une gestion des erreurs locale et centralisée doit dépendre de la complexité du système et de la manière dont les composants interagissent. Cela contribuera à la scalabilité et à la maintenabilité globales du système.

Ci-dessous se trouve un résumé de la fonctionnalité de chaque composant dans cette architecture :

* Charger et vérifier l'entrée : Ce composant prendra le fichier CSV, le fichier JSON et le numéro de mois en entrée, vérifiera leur validité et chargera les données dans des structures.
    
* Filtre basé sur le temps : Ce composant filtrera les transactions en fonction du mois d'entrée et stockera les transactions filtrées dans une structure de données.
    
* Catégorisation basée sur les étiquettes : Ce composant catégorisera les transactions en fonction de l'étiquette de catégorie dans le fichier CSV.
    
* Catégorisation basée sur la description : Ce composant catégorisera les transactions à l'aide d'un algorithme basé sur la description de la transaction.
    
* Registre financier : Ce composant stockera toutes les transactions catégorisées pour un traitement ultérieur. Il isole le post-traitement des transactions catégorisées du processus de catégorisation et fournit des méthodes pour mettre à jour ou récupérer des ensembles de données.
    
* Génération de rapports : Ce composant générera des rapports de dépenses à partir des données de transactions catégorisées.
    
* Télémétrie : Ce composant surveillera les performances des autres composants. Il suivra le flux des transactions, garantissant que toutes les transactions sont catégorisées soit par étiquette, soit par description. Des paramètres supplémentaires peuvent être ajoutés selon les besoins pour surveiller des fonctionnalités spécifiques.
    

Le diagramme ci-dessous illustre le flux de données à travers ces composants :

![Figure 2: Flux de données à travers divers composants définis dans l'architecture](https://cdn.hashnode.com/res/hashnode/image/upload/v1738540585066/6236b867-8c57-4a04-b5ea-4f9dd7f1fef3.png?auto=compress,format&format=webp align="left")

### **Conception logicielle détaillée et décomposition des composants**

Bien que nous ne couvrirons pas la conception complète du système, cette section mettra en lumière les composants clés et leurs spécifications. Pour cet exemple, je vais assumer le rôle à la fois du concepteur et du développeur du logiciel.

La conception logicielle et les spécifications dépendent de plusieurs facteurs, y compris les connaissances du concepteur, ses compétences, le temps disponible et les ressources. Nous allons définir certains détails de conception pour le système, en commençant par le choix du langage de mise en œuvre.

Le choix du bon langage repose sur plusieurs facteurs importants :

1. Le langage doit répondre aux exigences logicielles.
    
2. Il doit être stable et bénéficier d'un soutien solide de la part d'une communauté de développeurs active.
    
3. D'autres considérations incluent les performances (vitesse et mémoire), l'évolutivité (capacité à croître avec les exigences futures) et la prise en charge des plateformes (capacité à s'exécuter sur tous les principaux systèmes d'exploitation).
    

Si vous êtes celui qui met en œuvre cette conception, vous devrez être familier avec ce langage de programmation et avoir confiance en son utilisation. Pour ce projet, j'ai choisi Python car il répond à toutes les exigences du projet, bénéficie d'une communauté de développeurs robuste pour le soutien, il est stable et j'ai confiance en son utilisation pour mener à bien la mise en œuvre.

#### **Structures de données**

Maintenant, examinons les structures de données fondamentales que nous utiliserons dans la conception. Nous devons charger le contenu du fichier CSV dans une structure de données pour une analyse et un traitement ultérieurs. En Python, le DataFrame Pandas de la bibliothèque Pandas est idéal pour analyser et traiter des tableaux, nous l'utiliserons donc pour stocker les transactions.

Pour générer des rapports, nous encapsulerons les transactions catégorisées ainsi que les statistiques pertinentes, telles que le nombre total de transactions, le montant moyen et le montant maximum, dans une classe de jeu de données dédiée. Cette approche garantit une séparation claire des préoccupations, où la classe de jeu de données gère le traitement des données, tandis que le composant de rapport se concentre sur la présentation.

En structurant le système de cette manière, nous améliorons la réutilisabilité, la maintenabilité et l'évolutivité, ce qui facilite son extension et sa modification à l'avenir.

Cette classe de jeu de données comprendra :

* Variables membres : nom de la catégorie, description de la catégorie, un DataFrame Pandas pour les transactions, nombre total de transactions, montant moyen et montant maximum des transactions.
    
* Fonctions membres : définir/obtenir DataFrame, sauvegarder le jeu de données en CSV (utile pour le débogage).
    

Voici un exemple de classe Dataset en Python pour la gestion et le traitement structurés des données :

```python
import pandas as pd  # Import Pandas pour la gestion des données

class Dataset:
    """
    Une classe représentant un jeu de données structuré avec un nom, des clés prédéfinies, 
    et un DataFrame Pandas.
    """

    def __init__(self, name, keys):
        """
        Initialise l'objet Dataset.

        Paramètres:
        name (str): Le nom du jeu de données.
        keys (list): Une liste de noms de colonnes attendus pour le jeu de données.
        
        Attributs:
        self.name (str): Stocke le nom du jeu de données sous forme de chaîne.
        self.keys (list): Stocke les noms de colonnes attendus pour l'organisation des données.
        self.mean_amt (float): Suivi du montant moyen (moyenne) des transactions.
        self.max_amt (float): Suivi du montant maximum des transactions.
        self.count (int): Stocke le nombre total de transactions dans le jeu de données.
        self.dataframe (pd.DataFrame): Un DataFrame Pandas initialisé avec les noms de colonnes spécifiés.
        """
        self.name = str(name)  # Convertit et stocke le nom du jeu de données sous forme de chaîne
        self.keys = keys  # Stocke les noms de colonnes attendus pour la cohérence
        self.mean_amt = 0  # Initialise le montant moyen des transactions à zéro
        self.max_amt = 0  # Initialise le montant maximum des transactions à zéro
        self.count = 0  # Initialise le compteur de transactions à zéro
        self.dataframe = pd.DataFrame(columns=keys)  # Initialise un DataFrame vide avec des colonnes prédéfinies

    def getName(self):
        """
        Retourne le nom du jeu de données.

        Retourne:
        str: Le nom du jeu de données.
        """
        return self.name  # Corrigé : Suppression des parenthèses incorrectes

    def getValue(self, key):
        """
        Récupère une colonne spécifique du DataFrame.

        Paramètres:
        key (str): Le nom de la colonne à récupérer.

        Retourne:
        pandas.Series ou None: Les données de la colonne si la clé existe, sinon None.
        """
        if key in self.dataframe.columns:
            return self.dataframe[key]
        else:
            print(f"Avertissement : La clé '{key}' n'a pas été trouvée dans le DataFrame.")
            return None  # Empêche KeyError

    def getKeys(self):
        """
        Retourne la liste des clés (noms de colonnes) attendues du jeu de données.

        Retourne:
        list: Les clés définissant le jeu de données.
        """
        return self.keys

    def setDataFrame(self, dataframe):
        """
        Définit le DataFrame du jeu de données tout en s'assurant qu'il ne contient que les clés attendues.

        Paramètres:
        dataframe (pandas.DataFrame): Le DataFrame à attribuer au jeu de données.
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Les données fournies ne sont pas un DataFrame Pandas valide.")

        # Assure que seules les colonnes attendues sont incluses
        self.dataframe = dataframe[self.keys].copy() if set(self.keys).issubset(dataframe.columns) else dataframe.copy()

    def getDataFrame(self):
        """
        Retourne le DataFrame associé au jeu de données.

        Retourne:
        pandas.DataFrame: Le DataFrame du jeu de données.
        """
        return self.dataframe

    def save_to_csv(self, file_name):
        """
        Sauvegarde le DataFrame du jeu de données dans un fichier CSV.

        Paramètres:
        file_name (str): Le nom du fichier CSV à sauvegarder.
        """
        self.dataframe.to_csv(file_name, mode='w', index=False)  # Sauvegarde le DataFrame en CSV
```

Dans la section précédente, nous avons décrit l'architecture du système de haut niveau, détaillant les composants principaux et leurs interactions. Maintenant, plongeons dans la conception détaillée de certains des composants individuels, en spécifiant comment nous allons implémenter chacun d'eux et comment il fonctionnera au sein du système. Nous allons également décomposer les composants pour expliquer comment ils fonctionnent ensemble pour traiter l'entrée et générer le rapport.

Ci-dessous, vous pouvez voir le diagramme de flux du logiciel, illustrant l'interaction entre les composants principaux et le flux de données à travers le système.

![Figure 3 Diagramme de flux du logiciel](https://cdn.hashnode.com/res/hashnode/image/upload/v1739209441033/60142953-c1f4-4146-b64e-c042039e1ef6.png?auto=compress,format&format=webp align="left")

#### **Composant de filtrage basé sur les étiquettes de catégorie**

Le composant de filtrage basé sur les étiquettes de catégorie classe les transactions en faisant correspondre leur "Étiquette de catégorie" avec des catégories de dépenses prédéfinies à partir d'un fichier JSON. Les transactions avec des étiquettes de catégorie valides sont stockées dans le registre financier, tandis que celles non appariées restent pour un traitement ultérieur.

* Entrée : DataFrame de transactions filtrées dans le temps, catégories de dépenses à partir de JSON.
    
* Bibliothèques utilisées : DataFrame Pandas.
    
* Conception logicielle : Filtre les transactions en fonction de la colonne "Étiquette de catégorie" et les attribue aux catégories correspondantes. Les transactions qui ne peuvent pas être catégorisées restent pour un traitement ultérieur.
    
* Sortie : DataFrame des transactions restantes avec des valeurs vides dans le champ "Étiquette de catégorie".
    
* Tests de composant : Valider la gestion des étiquettes de catégorie valides, invalides et manquantes.
    

#### **Composant de registre financier**

Le composant de registre financier gère les transactions catégorisées en les stockant sous forme de jeux de données pour chaque catégorie de dépenses. Il maintient une collection structurée de DataFrames, chacun contenant des transactions et des statistiques récapitulatives telles que le nombre total, le montant maximum et le montant moyen.

* Entrée : Catégories de dépenses à partir de JSON.
    
* Bibliothèques utilisées : DataFrame Pandas.
    
* Conception logicielle : Implémente une classe qui organise les jeux de données pour toutes les catégories de dépenses, fournissant des méthodes pour définir et récupérer les DataFrames.
    
* Tests de composant : Valider la création de jeux de données, en assurant un stockage et une récupération corrects des transactions catégorisées.
    

Voici une implémentation simple et efficace du registre financier en Python pour la gestion des jeux de données financiers catégorisés :

```python
from Dataset import Dataset
import pandas as pd  # Assurez-vous que Pandas est importé si utilisé ailleurs

# Définir la structure des colonnes pour les jeux de données
KEYS = ("Date", "Description", "Montant", "Type de transaction", "Catégorie", "Nom du compte", "Étiquettes", "Notes")

# Définir les noms des jeux de données pour différentes catégories financières
EXAMPLE_DATASET_NAMES = ("Investissement", "Dépense", "Épargne")

class FinanceRegistry:
    """
    Une classe pour gérer les jeux de données financiers catégorisés, y compris les jeux de données d'investissement, de dépenses et d'épargne.
    Ce registre permet un accès structuré aux données de transaction et maintient des métriques financières agrégées.
    """

    def __init__(self):
        """
        Initialise l'objet FinanceRegistry.

        Attributs:
        self.example_dataset (dict): Un dictionnaire stockant des objets Dataset pour les jeux de données financiers.
        """
        self.example_dataset = {name: Dataset(name, KEYS) for name in EXAMPLE_DATASET_NAMES}  # Créer des jeux de données pour les catégories

    def setExampleDatasetToRegistry(self, name, dataframe):
        """
        Fusionne un nouveau dataframe dans le jeu de données existant pour une catégorie financière donnée.

        Paramètres:
        name (str): Le nom de la catégorie (par exemple, "Investissement", "Dépense" ou "Épargne").
        dataframe (pd.DataFrame): Les nouvelles données à ajouter.

        Si le jeu de données contient déjà des données, il concatène le nouveau dataframe à celui existant.

        Lève:
        ValueError: Si le nom fourni n'est pas une catégorie de jeu de données valide.
        """
        if name not in self.example_dataset:
            raise ValueError(f"Nom de jeu de données invalide : '{name}'. Attendu l'un des {EXAMPLE_DATASET_NAMES}")

        df = self.example_dataset[name].getDataFrame()  # Obtenir le jeu de données existant

        if not dataframe.empty:  # Assurer que le nouveau dataframe n'est pas vide
            dataframe = pd.concat([df, dataframe], axis=0, ignore_index=True)  # Ajouter les nouvelles données

        self.example_dataset[name].setDataFrame(dataframe)  # Mettre à jour le jeu de données dans le registre

    def getExampleDatasetFromRegistry(self, name):
        """
        Récupère le jeu de données pour une catégorie financière donnée.

        Paramètres:
        name (str): Le nom de la catégorie (par exemple, "Investissement", "Dépense" ou "Épargne").

        Retourne:
        Dataset: Le jeu de données correspondant au nom donné.

        Lève:
        ValueError: Si le nom fourni n'est pas une catégorie de jeu de données valide.
        """
        if name not in self.example_dataset:
            raise ValueError(f"Nom de jeu de données invalide : '{name}'. Attendu l'un des {EXAMPLE_DATASET_NAMES}")

        return self.example_dataset[name]
```

Le diagramme ci-dessous illustre comment le registre financier organise ces jeux de données pour un traitement ultérieur dans le composant de génération de rapports.

![Figure 4 Jeux de données du registre financier pour la catégorie de dépenses](https://cdn.hashnode.com/res/hashnode/image/upload/v1739209411075/7a772e4f-9687-4c96-8995-10a70e27a36d.png?auto=compress,format&format=webp align="left")

#### **Composant de génération de rapports**

Le composant de génération de rapports traite les jeux de données de transactions catégorisées à partir du registre financier et génère des statistiques récapitulatives. Il calcule des métriques financières clés telles que le montant maximum, le montant moyen et le nombre total de transactions. Il fournit également une fonctionnalité pour afficher les transactions catégorisées dans un format structuré dans le shell.

* Entrée : Jeux de données de transactions catégorisées à partir du registre financier.
    
* Bibliothèques utilisées : Numpy pour les calculs, Tabulate pour la sortie formatée du shell (si nécessaire).
    
* Conception logicielle : Implémente une classe avec des méthodes pour calculer les statistiques financières et afficher les résumés de transactions par catégorie de dépenses.
    
* Tests de composant : Valider le calcul correct de la moyenne, du maximum et du nombre total de transactions, et assurer un affichage précis des jeux de données catégorisées dans le shell.
    

Voici une fonction pour calculer les statistiques des transactions, y compris la moyenne, le maximum et le compte, à partir d'un jeu de données dans le composant de génération de rapports :

```python
from Dataset import Dataset
import numpy as np

def calculateStats(dataset):
    """
    Calcule les métriques statistiques pour un jeu de données donné.

    Paramètres:
    dataset: Le jeu de données contenant les données de transaction.

    Mises à jour:
    - dataset.mean: Montant moyen des transactions.
    - dataset.max: Montant maximum des transactions.
    - dataset.count: Nombre de transactions.
    """

    # Retourne tôt si le jeu de données n'a pas de transactions
    if dataset.dataframe.empty:
        return

    # Extrait les montants des transactions sous forme de liste
    tx_amount_list = dataset.dataframe['Amount'].astype(float).round(2).tolist()

    # Ajuste les montants des transactions en fonction du "Type de transaction"
    for i, tx_type in enumerate(dataset.dataframe['Transaction Type']):
        if tx_type == 'debit':
            tx_amount_list[i] *= -1  # Convertit les transactions de débit en valeurs négatives

    # Calcule les métriques statistiques
    dataset.mean = round(np.mean(tx_amount_list), 2)
    dataset.max = max(tx_amount_list)
    dataset.count = len(tx_amount_list)
```

Cela conclut la section de conception, où nous avons exploré les éléments clés de la conception logicielle avec un exemple pratique. L'étape suivante, la mise en œuvre, dépasse le cadre de cet article. Mais il est crucial de reconnaître que de nouveaux défis émergent souvent pendant le développement, nécessitant des mises à jour des exigences, de l'architecture et des spécifications.

Le but de cet article n'est pas de fournir une mise en œuvre complète, mais de vous enseigner quelques principes de base de la conception logicielle à travers un exemple. L'accent est mis sur la compréhension de la manière de structurer le logiciel, de définir des exigences claires et de créer des architectures évolutives, le tout avant d'écrire du code.

En suivant un processus de conception structuré, vous pouvez déplacer la résolution de problèmes complexes de la phase de mise en œuvre à la phase d'architecture, où vous pouvez explorer des solutions plus efficacement à l'aide de diagrammes de flux, de diagrammes de blocs et de documentation. Cela rend le processus de développement plus organisé, plus efficace et plus maintenable, une compétence cruciale pour l'ingénierie logicielle dans le monde réel.

Si vous apprenez à coder, rappelez-vous qu'une bonne conception est tout aussi importante que l'écriture de code elle-même !

## **Conclusion : La valeur d'une conception logicielle réfléchie**

Avec des énoncés de problème bien définis, une portée, des exigences, des spécifications et une conception, même les problèmes complexes peuvent être résolus et maintenus de manière durable.

Les étapes que nous avons suivies dans cet article peuvent vous aider à décomposer tout problème, quelle que soit sa complexité, en tâches plus petites et réalisables que vous et votre équipe pouvez traiter efficacement.

Sans une planification appropriée, les projets sont souvent confrontés à des extensions de portée, à des pertes de temps et de ressources, à des problèmes de communication entre les équipes, à des conceptions trop complexes, à une dette technique et à des reconceptions fréquentes. Une bonne conception est souvent une conception simple, mais atteindre la simplicité est difficile sans une planification minutieuse.

Aborder chaque problème avec l'état d'esprit de définir un énoncé de problème, une portée, des cas d'utilisation, des exigences, une architecture et des spécifications aide à cultiver un état d'esprit solide de conception logicielle. Cet état d'esprit est crucial pour développer un logiciel évolutif, maintenable et de haute qualité.