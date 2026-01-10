---
title: Comment utiliser l'IA pour automatiser les tests unitaires avec TestGen-LLM
  et Cover-Agent
subtitle: ''
author: Oluwadamisi Samuel
co_authors: []
series: null
date: '2024-06-03T14:45:24.000Z'
originalURL: https://freecodecamp.org/news/automated-unit-testing-with-testgen-llm-and-cover-agent
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Final-X3-Cover-FFC-Cover-Agent.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: 'LLM''s '
  slug: llms
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
seo_title: Comment utiliser l'IA pour automatiser les tests unitaires avec TestGen-LLM
  et Cover-Agent
seo_desc: 'It''s important to write clear and efficient unit tests that actually work
  during the software development process. Unit tests separate out individual code
  elements and confirm that they work as intended.

  Effective unit tests not only catch errors but...'
---

Il est important d'écrire des tests unitaires clairs et efficaces qui fonctionnent réellement pendant le processus de développement logiciel. Les tests unitaires isolent les éléments individuels du code et confirment qu'ils fonctionnent comme prévu.

Des tests unitaires efficaces non seulement attrapent les erreurs mais aident également à être confiant que votre code peut être maintenu et est fiable. Mais cela prend du temps et des ressources pour créer manuellement une suite exhaustive de tests unitaires.

Il y a eu des développements récents en intelligence artificielle qui promettent d'aider à automatiser les processus de développement des tests unitaires. En février, des chercheurs de Meta ont publié un article sur [l'amélioration automatisée des tests unitaires utilisant des grands modèles de langage](https://arxiv.org/abs/2402.09171). Cela a introduit une méthode innovante pour automatiser les tests unitaires.

Leur recherche se concentre sur un nouvel outil appelé `TestGen-LLM`, qui explore les possibilités d'utiliser les LLMs pour analyser les tests unitaires déjà existants et les améliorer pour augmenter la couverture de code.

Bien que le code pour TestGen-LLM n'ait pas été publié, je vais présenter une alternative open-source inspirée par leur recherche dans cet article. Vous apprendrez comment elle génère des suites de tests, pourquoi elle est meilleure que la plupart des LLMs, et où obtenir cette technologie et commencer à l'essayer.

## Table des matières

* [TestGen-LLM de Meta](#heading-testgen-llm-de-meta)
    
* [Comment fonctionne TestGen-LLM ?](#heading-comment-fonctionne-testgen-llm)
    
* [Implémentation Open-Source (Cover-Agent)](#heading-implementation-open-source-cover-agent)
    
* [Comment fonctionne Cover-Agent ?](#heading-comment-fonctionne-cover-agent)
    
* [Comment utiliser Cover-Agent](#heading-comment-utiliser-cover-agent)
    
* [Avantages de l'Open-Source Cover-Agent](#heading-avantages-de-lopen-source-cover-agent)
    
* [Comment pouvez-vous contribuer à cette technologie ?](#comment-pouvez-vous-contribuer-a-cette-technologie)
    
* [Conclusion](#heading-conclusion)
    

## TestGen-LLM de Meta

TestGen-LLM de Meta aborde la tâche chronophage de l'écriture de tests unitaires en exploitant la puissance des grands modèles de langage (LLMs). Les LLMs à usage général comme Gemini ou ChatGPT pourraient avoir du mal avec le domaine spécifique du code de test unitaire, la syntaxe de test et la génération de tests qui n'ajoutent pas de valeur. Mais TestGen-LLM est spécifiquement conçu pour les tests unitaires.

Cette spécialisation lui permet de comprendre les intrications de la structure du code et de la logique de test, conduisant à des suites de tests plus ciblées et générant des tests qui ajoutent réellement de la valeur et augmentent la couverture de code.

TestGen-LLM est capable d'évaluer les tests unitaires et d'identifier les domaines à améliorer. Il y parvient grâce à sa compréhension des motifs de test courants avec lesquels il a été formé. Mais générer des tests seuls est insuffisant pour une couverture de code appropriée.

Les chercheurs de Meta ont implémenté des garde-fous dans TestGen-LLM pour garantir l'efficacité des tests qu'il écrit. Ces garde-fous, appelés `filtres`, agissent comme un mécanisme de contrôle de qualité. Ils éliminent les suggestions qui :

* ne compileraient pas
    
* échoueraient constamment, ou
    
* échoueraient à améliorer réellement la couverture de code (suggestions qui sont déjà couvertes par d'autres tests).
    

## Comment fonctionne TestGen-LLM ?

TestGen-LLM utilise une approche appelée "Ingénierie Logicielle Basée sur les LLMs Assurée" (Assured LLMSE). TestGen-LLM augmente simplement une classe de test existante avec des cas de test supplémentaires, conservant tous les cas de test existants et garantissant ainsi qu'il n'y aura pas de régression.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/img-testgen-llm-paper.jpg align="left")

*Flux de travail de génération de tests(*[*D'après le document TestGen_LLM*](https://arxiv.org/abs/2402.09171)*)*

TestGen-LLM génère un ensemble de tests, puis filtre les tests qui ne s'exécutent pas et supprime ceux qui ne passent pas. Enfin, il écarte ceux qui n'augmentent pas la couverture de code.

Après avoir utilisé TestGen-LLM pour automatiser une suite de tests, Meta a utilisé un réviseur humain pour accepter ou rejeter les tests où les tests générés avaient un taux d'acceptation de 73 % dans leurs meilleurs cas rapportés.

Selon le document, TestGen-LLM génère un seul test à chaque exécution qui est ensuite ajouté à une suite de tests existante écrite précédemment par un développeur. Mais il ne génère pas nécessairement des tests pour une suite de tests donnée.

L'efficacité de TestGen-LLM a été démontrée lors des test-a-thons internes de Meta. Ici, l'outil a été utilisé pour analyser les suites de tests existantes et suggérer des améliorations. Les résultats étaient prometteurs :

> *75 % des cas de test de TestGen-LLM se sont compilés correctement, 57 % ont passé avec fiabilité, et 25 % ont augmenté la couverture. Lors des test-a-thons d'Instagram et de Facebook de Meta, il a amélioré 11,5 % de toutes les classes auxquelles il a été appliqué, avec 73 % de ses recommandations étant acceptées pour le déploiement en production par les ingénieurs logiciels de Meta*.

De plus, les recommandations de TestGen-LLM ont été jugées utiles et pertinentes par les développeurs qui ont participé aux test-a-thons.

## Implémentation Open-Source (Cover-Agent)

La recherche TestGen-LLM de Meta a un grand potentiel pour changer les tests unitaires et la génération automatisée de tests. L'outil aidera probablement à améliorer la couverture de code et à accélérer la création de tests en utilisant des LLMs particulièrement formés sur le code. Mais cette technologie n'est pas disponible pour une utilisation par n'importe qui, puisque le code pour TestGen-LLM n'a pas été publié.

Les développeurs qui se sont intéressés à cette technologie sont probablement frustrés par le manque de code disponible publiquement. Après tout, l'étude TestGen-LLM de Meta offre un aperçu de l'avenir de ce que les tests automatisés peuvent être.

Il est assez attrayant de pouvoir plonger dans le fonctionnement interne de la nouvelle technologie, comprendre ses procédures de prise de décision et peut-être même aider à façonner son évolution. Mais bien que l'absence de code de Meta soit un obstacle, il existe une implémentation open-source appelée `Cover-Agent` qui peut servir d'alternative utile.

`Cover-Agent de CodiumAI` est la première implémentation open-source d'un outil de test automatisé basé sur TestGen-LLM. Inspiré par la recherche de Meta, Cover-Agent est maintenant à l'avant-garde des développements en matière de tests unitaires pilotés par l'IA en open-source.

### Pourquoi des LLMs spécifiques aux tests sont-ils nécessaires ?

Puisque la plupart des LLMs (comme ChatGPT et Gemini) sont capables de générer des tests, alors pourquoi se donner la peine avec une nouvelle technologie ?

Eh bien, Cover-Agent et TestGen-LLM ont été créés pour être la prochaine étape dans l'évolution des tests unitaires efficaces. Leur objectif est d'éviter les pièges courants que les développeurs rencontrent lors de la génération de tests avec des LLMs tels que :

* Hallucination des LLMs
    
* Génération de tests qui n'ajoutent pas de valeur
    
* Génération de tests qui omettent certaines parties du code, résultant en une faible couverture de code
    

Pour surmonter de tels défis (spécifiquement pour les tests unitaires de régression), les chercheurs de TestGen-LLM ont établi les critères suivants que les tests générés doivent satisfaire avant que le test puisse être accepté :

* Le test généré se compile-t-il et s'exécute-t-il correctement ?
    
* Le test augmente-t-il la couverture de code ?
    
* Ajoute-t-il de la valeur ?
    
* Répond-il à d'autres exigences supplémentaires que nous pourrions avoir ?
    

Ce sont des questions et des problèmes fondamentaux que le test généré doit résoudre avant d'être considéré comme une amélioration de la technologie existante. Cover-Agent fournit des tests qui répondent à ces questions à un degré étonnamment élevé.

## Comment fonctionne Cover-Agent ?

Cover-Agent fait partie d'une suite plus large d'utilitaires conçus pour automatiser la création de tests unitaires pour les projets logiciels. Utilisant le modèle d'IA générative TestGen-LLM, il vise à simplifier et à accélérer le processus de test, garantissant un développement logiciel de haute qualité.

Le système est composé de plusieurs composants :

* **Test Runner** : Exécute la commande ou les scripts pour exécuter la suite de tests et générer des rapports de couverture de code.
    
* **Coverage Parser** : Valide que la couverture de code augmente à mesure que les tests sont ajoutés, garantissant que les nouveaux tests contribuent à l'efficacité globale des tests.
    
* **Prompt Builder** : Rassemble les données nécessaires à partir de la base de code et construit le prompt à passer au Grand Modèle de Langage (LLM).
    
* **AI Caller** : Interagit avec le LLM pour générer des tests basés sur le prompt fourni.
    

Ces composants travaillent ensemble avec TestGen-LLM pour générer uniquement des tests qui sont garantis d'améliorer la base de code existante.

## Comment utiliser Cover-Agent

### Exigences

Vous devez avoir les exigences suivantes avant de pouvoir commencer à utiliser Cover-Agent :

* `OPENAI_API_KEY` défini dans vos variables d'environnement, ce qui est requis pour appeler l'`OpenAI API`.
    
* Outil de couverture de code : Un rapport de couverture de code XML Cobertura est requis pour que l'outil fonctionne correctement. Par exemple, en Python, vous pourriez utiliser `pytest-cov`. Ajoutez l'option `--cov-report=xml` lors de l'exécution de Pytest.
    

### Installation

Si vous exécutez Cover-Agent directement depuis le dépôt, vous aurez également besoin de :

* Python installé sur votre système.
    
* Poetry installé pour gérer les dépendances des packages Python. Vous pouvez trouver les instructions d'installation pour Poetry [ici](https://python-poetry.org/docs/).
    

#### Runtime autonome

Vous pouvez installer Cover-Agent en tant que package Python Pip ou l'exécuter en tant qu'exécutable autonome.

#### Python Pip

Pour installer le package Python Pip directement via GitHub, exécutez la commande suivante :

```py
pip install git+https://github.com/Codium-ai/cover-agent.git
```

#### Binaire

Vous pouvez exécuter le binaire sans aucun environnement Python installé sur votre système (par exemple, dans un conteneur Docker qui ne contient pas Python). Vous pouvez télécharger la version pour votre système en naviguant vers la page de [version du projet](https://github.com/Codium-ai/cover-agent/releases).

#### Configuration du dépôt

Exécutez la commande suivante pour installer toutes les dépendances et exécuter le projet à partir de la source :

```py
poetry install
```

#### Exécution du code

Après avoir téléchargé l'exécutable ou installé le package Pip, vous pouvez maintenant exécuter Cover-Agent pour générer et valider des tests unitaires.

Exécutez-le à partir de la ligne de commande en utilisant la commande suivante :

```py
cover-agent \
--source-file-path "chemin_vers_fichier_source" \
--test-file-path "chemin_vers_fichier_test" \
--code-coverage-report-path "chemin_vers_rapport_couverture.xml" \
--test-command "commande_pour_executer_test" \
--test-command-dir "repertoire_pour_executer_commande_test/" \
--coverage-type "type_rapport_couverture" \
--desired-coverage "couverture_souhaitee_entre_0_et_100" \
--max-iterations "nombre_max_iterations_llm" \
 --included-files "<liste_optionnelle_fichiers_a_inclure>"
```

Vous pouvez utiliser les projets d'exemple dans ce dépôt pour exécuter ce code en tant que test.

#### Arguments de commande

* **source-file-path** : Chemin du fichier contenant les fonctions ou le bloc de code que nous voulons tester.
    
* **test-file-path** : Chemin du fichier où les tests seront écrits par l'agent. Il est préférable de créer un squelette de ce fichier avec au moins un test et les instructions d'importation nécessaires.
    
* **code-coverage-report-path** : Chemin où le rapport de couverture de code est enregistré.
    
* **test-command** : Commande pour exécuter les tests (par exemple pytest).
    
* **test-command-dir** : Répertoire où la commande de test doit être exécutée. Définissez ceci à la racine ou à l'emplacement de votre fichier principal pour éviter les problèmes avec les imports relatifs.
    
* **coverage-type** : Type de couverture à utiliser. Cobertura est un bon choix par défaut.
    
* **desired-coverage** : Objectif de couverture. Plus élevé est mieux, bien que 100 % soit souvent irréaliste.
    
* **max-iterations** : Nombre de fois où l'agent doit réessayer de générer le code de test. Plus d'itérations peuvent entraîner une utilisation plus élevée de tokens OpenAI.
    
* **additional-instructions** : Prompts pour s'assurer que le code est écrit d'une manière spécifique. Par exemple, ici nous spécifions que le code doit être formaté pour fonctionner dans une classe de test.
    

Lors de l'exécution de la commande, l'agent commence à écrire et à itérer sur les tests.

### Comment utiliser Cover-Agent

Il est temps de tester Cover-Agent. Nous allons utiliser une simple application calculator.py pour comparer la couverture de code pour les tests manuels et automatisés.

#### Tests manuels

```py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Ceci est le test_calculator.py placé dans le dossier de test.

```py
# tests/test_calculator.py
from calculator import add, subtract, multiply, divide

class TestCalculator:

    def test_add(self):
        assert add(2, 3) == 5
```

Pour voir la couverture de test, nous devons installer `pytest-cov`, une extension pytest pour les rapports de couverture mentionnée précédemment.

```py
pip install pytest-cov
```

Exécutez l'analyse de couverture avec :

```py
pytest --cov=calculator
```

La sortie montre :

```py
Name            Stmts   Miss  Cover
-----------------------------------
calculator.py      10      5    50%
-----------------------------------
TOTAL              10      5    50%
```

La sortie ci-dessus montre que 5 des 10 instructions dans calculator.py ne sont pas exécutées, résultant en seulement 50 % de couverture de code. Pour une base de code plus grande, cela deviendra un problème sérieux et entraînera des retards.

Maintenant, voyons si cover-agent peut faire mieux.

#### Tests automatisés avec Cover-Agent

Pour configurer Cover-Agent de Codium, suivez ces étapes :

Tout d'abord, installez Cover-Agent :

```py
pip install git+https://github.com/Codium-ai/cover-agent.git
```

Assurez-vous que votre OPENAI_API_KEY est définie dans vos variables d'environnement, car elle est requise pour l'API OpenAI.

Ensuite, écrivez les commandes pour commencer à générer des tests dans le terminal :

```py
cover-agent \
--source-file-path "calculator.py" \
--test-file-path "tests/test_calculator.py" \
--code-coverage-report-path "coverage.xml" \
--test-command "pytest --cov=. --cov-report=xml --cov-report=term" \
--test-command-dir "./" \
--coverage-type "cobertura" \
--desired-coverage 80 \
--max-iterations 3 \
--openai-model "gpt-4o" \
--additional-instructions "Puisque j'utilise une classe de test, chaque ligne de code (y compris la première ligne) doit être précédée de 4 espaces blancs. Cela est extrêmement important pour s'assurer que chaque ligne retournée contient cette indentation de 4 espaces blancs ; sinon, mon code ne s'exécutera pas."
```

Cela génère le code suivant :

```py
import pytest
from calculator import add, subtract, multiply, divide

class TestCalculator:

    def test_add(self):
        assert(add(2, 3), 5

    def test_subtract(self):
        """
        Test soustraction de deux nombres.
        """
        assert subtract(5, 3) == 2
        assert subtract(3, 5) == -2

    def test_multiply(self):
        """
        Test multiplication de deux nombres.
        """
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(2, -3) == -6
        assert multiply(-2, -3) == 6

    def test_divide(self):
        """
        Test division de deux nombres.
        """
        assert divide(6, 3) == 2
        assert divide(-6, 3) == -2
        assert divide(6, -3) == -2
        assert divide(-6, -3) == 2

    def test_divide_by_zero(self):
        """
        Test division par zéro, devrait lever ValueError.
        """
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
```

Vous pouvez voir que l'agent a également écrit des tests qui vérifient les erreurs pour tous les cas limites.

Maintenant, il est temps de tester la couverture à nouveau :

```py
pytest --cov=calculator
```

Sortie :

```py
Name            Stmts   Miss  Cover
-----------------------------------
calculator.py      10      0   100%
-----------------------------------
TOTAL              10      0   100%
```

Dans cet exemple, nous avons atteint 100 % de couverture de code. Pour des bases de code plus grandes, la procédure est relativement la même. Vous pouvez lire [ce guide](https://dev.to/oluwadamisisamuel1/how-to-automate-test-generation-with-ai-using-codiumai-cover-agent-1kep) pour un tutoriel sur une base de code plus grande.

Bien que Cover-Agent représente une avancée significative, il est important de noter que cette technologie en est encore à ses débuts. La recherche et le développement continus sont cruciaux pour un affinement supplémentaire et une adoption plus large, et codiumAI vous invite à apporter vos contributions à cet outil open source.

## Avantages de l'Open Source Cover-Agent

La nature open source de Cover-Agent offre plusieurs avantages qui devraient aider à propulser la technologie vers l'avant. Parmi eux :

* **Accessibilité** : Sa nature open source permet l'expérimentation de tests basés sur les LLMs et il est accessible aux développeurs de divers horizons. Cela augmentera le nombre d'utilisateurs et conduira au développement d'une meilleure technologie et de plus d'applications.
    
* **Coopération** : Les développeurs sont en mesure de faire des contributions, de suggérer des améliorations, de proposer de nouvelles fonctionnalités et de signaler des problèmes. Cover-Agent grandira et se développera rapidement en un projet parfait pour les développeurs.
    
* **Transparence** : Les informations sur les opérations internes sont disponibles et cela favorise la confiance et augmentera finalement le potentiel de la technologie.
    

En plus de ses avantages open-source, Cover-Agent offre aux développeurs un ensemble solide de bénéfices propres :

* **Accès simple** : Les développeurs peuvent facilement installer et expérimenter avec les tests basés sur les LLMs. Cela permet une exploration directe et immédiate des capacités de la technologie avec peu ou pas de perturbation dans leur flux de travail.
    
* **Personnalisation pour des besoins spécifiques** : La nature open-source de Cover-Agent permet aux développeurs d'adapter l'outil à leurs exigences spécifiques de projet. Cela pourrait impliquer de modifier le modèle LLM utilisé, d'ajuster les données de formation pour mieux refléter leur base de code, ou d'intégrer Cover-Agent avec des frameworks de test existants. Ce niveau de personnalisation permet aux développeurs de tirer parti de la puissance des tests basés sur les LLMs d'une manière qui s'aligne avec leurs besoins de projet.
    
* **Intégration facile** : Il s'intègre facilement avec VSCode (un éditeur de code populaire) ce qui rend l'intégration avec les flux de travail existants très simple. Vous pouvez également l'intégrer facilement avec des tests écrits par des humains.
    

## Comment pouvez-vous contribuer à Cover-Agent ?

Le code source de Cover-Agent est disponible publiquement via [ce dépôt GitHub](https://github.com/Codium-ai/cover-agent). Ils encouragent les développeurs de tous horizons à tester leur produit et à faire des contributions pour améliorer et faire grandir cette nouvelle technologie.

## Conclusion

Les outils d'amélioration des tests basés sur les LLMs détiennent un immense potentiel pour révolutionner la manière dont les développeurs abordent les tests unitaires. En exploitant la puissance des grands modèles de langage spécifiquement formés sur le code, ces outils peuvent rationaliser la création de tests, améliorer la couverture de code et, en fin de compte, améliorer la qualité du logiciel.

Bien que la recherche de Meta avec TestGen-LLM offre des perspectives précieuses, le manque de code disponible publiquement entrave une adoption plus large et un développement continu. Heureusement, Cover-Agent a fourni une solution facilement accessible et personnalisable. Il permet aux développeurs d'expérimenter avec les tests basés sur les LLMs et de contribuer à son évolution.

Le potentiel pour TestGen-LLM et Cover-Agent est immense, et un développement supplémentaire grâce aux contributions des développeurs conduira à un outil révolutionnaire qui transformera à jamais la génération automatisée de tests.

* [Document de recherche de Meta](https://arxiv.org/abs/2402.09171)
    
* [Blog Cover-Agent pour une étude approfondie](https://www.codium.ai/blog/we-created-the-first-open-source-implementation-of-metas-testgen-llm/)
    
* [Article pour le processus d'installation et les cas d'utilisation](https://dev.to/oluwadamisisamuel1/how-to-automate-test-generation-with-ai-using-codiumai-cover-agent-1kep)
    

Connectez-vous avec moi sur [LinkedIn](http://www.linkedin.com/in/samuel-oluwadamisi-01b3a4236) et [Twitter](https://twitter.com/Data_Steve_) si vous avez trouvé cela utile.