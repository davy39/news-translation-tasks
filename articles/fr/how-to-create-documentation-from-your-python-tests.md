---
title: Comment créer de la documentation à partir de vos tests Python
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2020-09-15T19:12:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-documentation-from-your-python-tests
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/docs-from_tests_example_graph.png
tags:
- name: automation
  slug: automation
- name: documentation
  slug: documentation
- name: Python
  slug: python
- name: Testing
  slug: testing
seo_title: Comment créer de la documentation à partir de vos tests Python
seo_desc: "What if I told you that you could automatically create documentation from\
  \ your existing tests that would always be up to date? \nAnd what if it could be\
  \ in markdown format, so it would be committed along with the rest of your code,\
  \ and be shown on Git..."
---

Et si je vous disais que vous pourriez créer automatiquement de la documentation à partir de vos tests existants qui serait toujours à jour ?

Et si cette documentation pouvait être au format markdown, afin qu'elle soit validée avec le reste de votre code, et affichée sur GitLab / GitHub ?

Cela semble plutôt cool, n'est-ce pas ? Voyons comment cela se fait.

### Contexte

Des personnes comme [Simon Brown](https://c4model.com/) font un excellent travail pour me convaincre que je n'ai pas assez de documentation pour mes projets. Et que cette documentation devrait être à jour, et montrer des informations concises à différents niveaux d'abstraction. 

J'adorerais travailler sur une base de code avec une documentation comme celle-ci.

## Le problème avec la documentation

J'ai lu un bon nombre de [livres](https://www.goodreads.com/book/show/44144493-fundamentals-of-software-architecture) et d'articles sur l'architecture logicielle et des sujets connexes. Mais je n'ai jamais réussi à rassembler assez d'énergie, ou assez de capital politique, pour pouvoir créer une documentation à ce standard. Sans parler de la maintenir à jour.

Donc, pour ma situation au moins, j'ai besoin d'un moyen de créer et de mettre à jour la documentation automatiquement. 

J'aimerais également stocker les diagrammes "en tant que code", afin qu'ils puissent être validés dans le dépôt. De cette façon, les modifications apportées à ceux-ci peuvent être facilement vues et discutées dans les pull requests et autres revues de code.

Il existe de nombreux [outils](https://structurizr.com/help/code) qui peuvent générer des diagrammes de dépendance de construction à partir du code, et j'en ai utilisé plusieurs. 

Mais le problème semble être que ces diagrammes ressemblent toujours à des spaghettis, même lorsque le code est bon. Et ils sont complexes à configurer. 

Il semble très difficile d'obtenir le bon niveau de détail. Il n'y a aucun moyen de montrer le code lié dans des groupes logiques pour les diagrammes de haut niveau. Il n'y a également aucun moyen de sélectionner les relations de code spécifiques à un contexte particulier pour les diagrammes de bas niveau. 

Ils ne vous donnent également aucune information sur les relations d'exécution du code, ce qui est généralement un problème plus important que les relations de conception.

## Une solution

Pour capturer les relations d'exécution, la génération de diagrammes à partir du code en cours d'exécution est la seule option. Et nous avons déjà beaucoup de code qui est exécuté régulièrement, sous forme de tests.

Les dépôts devraient déjà avoir une bonne suite de tests (unitaires, d'intégration et de bout en bout, par exemple), et chaque test devrait être relativement court et simple. 

Ces tests devraient déjà incarner des regroupements logiques de code, et des niveaux d'abstraction sensés. Ils sont donc un excellent candidat pour générer de la documentation.

La solution implique d'instrumenter le code importé par un test. Ce code instrumenté enregistre ensuite la hiérarchie des appels d'exécution, et est capable d'écrire les résultats sous forme de [diagramme markdown Mermaid](https://mermaid-js.github.io/mermaid/#/) (techniquement un [diagramme de séquence](http://agilemodeling.com/artifacts/sequenceDiagram.htm)).

Le code ci-dessous ([un test du package python](https://github.com/resgroup/docs-from-tests/blob/master/tests/test_hello_world.py)) montre comment cela fonctionne. 

Pour chaque test existant, vous créez un test "wrapper", qui est responsable de l'initialisation de la hiérarchie des appels et de l'enregistrement du diagramme. Si vous avez beaucoup de tests, vous pourriez vouloir introduire un [décorateur](https://realpython.com/primer-on-python-decorators/) pour éviter la répétition.

```python
from docs_from_tests.instrument_call_hierarchy import instrument_and_import_package, instrument_and_import_module, initialise_call_hierarchy, finalise_call_hierarchy
from samples.hello_world_combiner import HelloWorldCombiner

# vous pouvez instrumenter des packages / dossiers entiers à la fois comme ceci
instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'samples'), 'samples')
# Vous pouvez instrumenter des modules individuels comme ceci
# instrument_and_import_module('tests.blah')

# ceci est un wrapper autour du test qui génère également la documentation / le diagramme de séquence
def test_hello_world():
    # cela initialise l'enregistrement de la hiérarchie des appels
    initialise_call_hierarchy('start')

    # Ceci exécute le test réel
    _test_hello_world()
    
    # cela finalise la hiérarchie des appels et retourne la racine
    root_call = finalise_call_hierarchy()

    # ceci retourne un diagramme de séquence de la hiérarchie des appels
    sequence_diagram = root_call.sequence_diagram(
        show_private_functions=False,
        excluded_functions=[
            'HelloWorldCombiner.__init__',
        ]
    )

    # ceci écrit le markdown sur le disque    
    sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'top-level-sequence-diagram.md')
    Path(sequence_diagram_filename).write_text(sequence_diagram)

# ceci est le test original / source
def _test_hello_world():
    assert HelloWorldCombiner().combine() == 'Hello world'

```

L'exécution de `pytest` sur ce code entraînera l'exécution du test, et la création du [markdown "diagramme en tant que code"](https://github.com/resgroup/docs-from-tests/blob/master/doc/top-level-sequence-diagram.md) (ci-dessous) dans le répertoire doc :

```
sequenceDiagram
  start->>HelloWorldCombiner.combine: appelle x1
  HelloWorldCombiner.combine->>hello: appelle x1
  hello-->>HelloWorldCombiner.combine: retourne str
  HelloWorldCombiner.combine->>world: appelle x1
  world-->>HelloWorldCombiner.combine: retourne str
  HelloWorldCombiner.combine-->>start: retourne str

```

Cela se rend comme le diagramme suivant :

![Exemple de diagramme docs-from-tests](https://www.freecodecamp.org/news/content/images/2020/09/docs-from_tests_example_graph-2.png)

Les modifications du diagramme apparaîtront dans Git et seront validées avec le code qui a provoqué le changement. Cela signifie que le changement du code et le changement du diagramme sont liés et peuvent être vus ensemble.

Les méthodes privées seraient généralement exclues (bien que ce soit facultatif), et vous pouvez exclure d'autres fonctions afin que le graphique ait l'apparence souhaitée. 

Parce que la hiérarchie des appels est stockée dans une structure d'arbre, l'exclusion d'une fonction exclut également toutes les fonctions en dessous.

## Qualité du code

Espérons que vous avez déjà des tests à des niveaux d'abstraction appropriés (classiquement, vous auriez des tests unitaires, d'intégration et de bout en bout). Cela facilite la création de diagrammes à ces niveaux. 

Si ce n'est pas le cas, alors le désir de créer de bons diagrammes devrait vous guider vers la création de bons tests.

Parfois, les diagrammes peuvent sembler un peu fous, et vous pourriez finir par ignorer beaucoup de fonctions. C'est un indice que le code pourrait probablement être simplifié. Et dans ce cas, le désir de créer de bons diagrammes devrait vous guider vers la simplification du code.

## Conclusion

Espérons que cela vous inspirera à créer et à maintenir la documentation que vos coéquipiers et votre futur vous remercieront ! C'est assez facile à faire.  

Toutes les fonctionnalités sont dans un package Python ([docs-from-tests)](https://pypi.org/project/docs-from-tests/), et il y a un [dépôt exemple qui démontre comment l'utiliser](https://github.com/ceddlyburge/docs-from-tests-example).