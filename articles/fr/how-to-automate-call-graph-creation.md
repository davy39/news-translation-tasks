---
title: Qu'est-ce qu'un graphe d'appels ? Et comment les générer automatiquement
subtitle: ''
author: Daniel García Solla
co_authors: []
series: null
date: '2023-01-03T23:58:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-call-graph-creation
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Untitled2-1.png
tags:
- name: automation
  slug: automation
- name: Java
  slug: java
- name: Python
  slug: python
seo_title: Qu'est-ce qu'un graphe d'appels ? Et comment les générer automatiquement
seo_desc: "Have you ever found yourself staring at lines of code, trying to wrap your\
  \ head around how all the different functions fit together and interact with each\
  \ other? \nIt can be a daunting task, especially in larger, more complex programs.\
  \ \nBut fear not! ..."
---

Vous êtes-vous déjà retrouvé à fixer des lignes de code, essayant de comprendre comment toutes les différentes fonctions s'emboîtent et interagissent entre elles ?

Cela peut être une tâche ardue, surtout dans des programmes plus grands et plus complexes.

Mais ne craignez rien ! Il existe un moyen de visualiser le flux des appels de fonctions et de tout comprendre : le graphe d'appels.

Imaginez pouvoir voir un diagramme qui vous montre exactement comment chaque fonction s'intègre dans le tableau général, et comment elles s'appellent les unes les autres pour accomplir leur travail. Cela ressemble à un rêve devenu réalité, n'est-ce pas ?

Eh bien, ce n'est pas qu'un rêve. Avec les bons outils et techniques, vous pouvez automatiser la création d'un graphe d'appels et obtenir une bien meilleure compréhension de votre base de code.

Dans cet article, nous allons vous montrer comment faire exactement cela. Nous aborderons les approches statiques et dynamiques pour créer des graphes d'appels, et discuterons des avantages et inconvénients de chacune.

Que vous soyez un développeur expérimenté ou que vous débutiez, vous trouverez des informations et des insights précieux dans ce guide sur la façon d'automatiser la création de graphes d'appels. Alors, prenez votre éditeur de texte préféré et commençons !

### **Dans cet article, nous aborderons :**

1. [Qu'est-ce qu'un graphe d'appels ?](#heading-quest-ce-quun-graphe-dappels)
2. [Graphes d'appels dynamiques vs statiques](#heading-graphes-dappels-dynamiques-vs-statiques)
3. [Pourquoi avons-nous besoin des graphes d'appels ?](#heading-pourquoi-avons-nous-besoin-des-graphes-dappels)
4. [Génération automatique de graphes d'appels](#heading-generation-automatique-de-graphes-dappels)
5. [Génération de graphes d'appels dynamiques](#heading-generation-de-graphes-dappels-dynamiques)
6. [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un graphe d'appels ?

Un graphe d'appels est une représentation graphique des relations entre différents appels de fonctions au sein d'un programme. Il montre comment les fonctions d'un programme interagissent entre elles, permettant aux développeurs de comprendre le flux du programme et d'identifier les problèmes de performance potentiels.

Les graphes d'appels peuvent être créés manuellement, mais cela peut être un processus fastidieux et chronophage, surtout pour les grands projets logiciels et applications.

C'est là qu'intervient l'automatisation. En automatisant la création de graphes d'appels, les développeurs peuvent gagner du temps et des efforts, et se concentrer sur des tâches plus importantes.

Il existe deux principales approches pour automatiser la création de graphes d'appels : l'analyse statique et l'analyse dynamique. L'analyse statique implique d'analyser le code source d'un programme sans l'exécuter, tandis que l'analyse dynamique implique d'exécuter le programme et d'analyser son comportement pendant l'exécution.

Les deux approches ont leurs propres avantages et inconvénients, et la meilleure approche pour une situation donnée dépendra des besoins et objectifs spécifiques du développeur.

Dans cet article, nous explorerons les deux approches plus en détail et discuterons de la manière de choisir la bonne pour vos besoins.

Quelle que soit l'approche que vous choisissez, l'automatisation de la création de graphes d'appels peut être un outil puissant pour améliorer l'efficacité et l'efficacité de votre processus de développement logiciel.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Example.png)
_Image par l'auteur_

Par exemple, l'image ci-dessus montre ce que serait le graphe d'appels d'un simple code Java dont le but est d'exécuter l'un des 3 sous-programmes possibles avec leurs propres entrées et sorties.

```java
import java.util.Scanner;

class Ejercicio3 extends Practicas {
    public String name = "3---Inversor dígitos";
    public String description = "Devuelve el número con los dígitos invertidos";

    public void mainExec() {
        showDescription(name, description);
        
        int b = in.nextInt();
        int h = in.nextInt();
        System.out.println(b*h/2);
    }
}

class Ejercicio2 extends Practicas {
    public String name = "2---Inversor dígitos";
    public String description = "Devuelve el número con los dígitos invertidos";

    public void mainExec() {
        showDescription(name, description);
        
        int input = in.nextInt();
        String temp = ""+input;
        String out = "";
        for(int i=0;i<temp.length();i++){
            out += temp.charAt(temp.length()-i-1);
        }
        int out1 = Integer.parseInt(out);
        System.out.println(out1);
    }
}

class Ejercicio1 extends Practicas {
    public String name = "1---Programa Hola mundo";
    public String description = "Simplemente Hola mundo";

    public void mainExec() {
        showDescription(name, description);
        System.out.println("Hello world!");
    }
}

public class Practicas {  
    Scanner in = new Scanner(System.in);  

    public void showDescription(String name, String description) {
        System.out.println(String.format("Nombre: %s \nDescripción: %s\nResultado de ejecución:\n", name, description));
    }

    public static void main(String args[]) {
           Ejercicio1 ej1 = new Ejercicio1();
           ej1.mainExec();

           Ejercicio2 ej2 = new Ejercicio2();
           ej2.mainExec();

           Ejercicio3 ej3 = new Ejercicio3();
           ej3.mainExec();
    }
}
```

Comme vous pouvez le voir dans le code, chaque sous-programme est stocké dans une classe appelée directement à partir de la méthode **`main()`**.

## Graphes d'appels dynamiques vs statiques

Un graphe d'appels dynamique est une représentation du flux de contrôle au sein d'un programme lors de son exécution. Il montre la séquence des appels de fonctions qui sont effectués pendant l'exécution du programme, ainsi que les paramètres qui sont passés à chaque fonction.

En revanche, un graphe d'appels statique est une représentation du flux de contrôle au sein d'un programme qui est construite sur la base du code source du programme, sans tenir compte de l'exécution réelle du programme.

L'une des principales différences entre les graphes d'appels dynamiques et statiques est le niveau de détail qu'ils fournissent.

Un graphe d'appels dynamique montre la séquence exacte des appels de fonctions qui ont été effectués pendant l'exécution d'un programme, ainsi que les paramètres spécifiques qui ont été passés à chaque fonction.

Cela peut être très utile pour le débogage et l'optimisation du code, car il permet aux développeurs de voir exactement comment le programme s'exécute et d'identifier les éventuels goulots d'étranglement ou inefficacités.

En revanche, un graphe d'appels statique est basé sur le code source du programme et ne tient pas compte de l'exécution réelle du programme. Par conséquent, un graphe d'appels statique ne fournit pas autant de détails qu'un graphe d'appels dynamique et peut ne pas refléter avec précision le flux de contrôle réel au sein du programme.

Mais les graphes d'appels statiques peuvent encore être très utiles pour comprendre la structure globale d'un programme et identifier les dépendances potentielles entre différentes parties du code.

Une autre différence entre les graphes d'appels dynamiques et statiques est la manière dont ils sont construits.

Les graphes d'appels dynamiques sont générés lorsque le programme est exécuté, ils nécessitent donc que le programme soit exécuté pour être créés. Cela peut être chronophage, surtout pour les grands programmes, et peut nécessiter que le programme soit exécuté plusieurs fois afin de capturer tous les chemins d'exécution possibles.

En revanche, les graphes d'appels statiques peuvent être générés directement à partir du code source du programme, sans avoir besoin d'exécuter réellement le programme. Cela peut être beaucoup plus rapide et plus efficace, surtout pour les grands programmes, et permet aux développeurs d'analyser la structure du programme sans avoir à attendre son exécution.

Il existe également certaines limitations pour les graphes d'appels dynamiques et statiques. Les graphes d'appels dynamiques ne peuvent fournir des informations que sur l'exécution réelle du programme et ne tiennent pas compte des chemins d'exécution potentiels qui n'ont pas été empruntés. Cela peut rendre difficile l'identification de certains types de bugs ou d'inefficacités qui peuvent ne se produire que dans certaines conditions.

Les graphes d'appels statiques, en revanche, ne peuvent fournir des informations que sur les chemins d'exécution potentiels du programme et ne tiennent pas compte de l'exécution réelle du programme. Cela peut rendre difficile la réflexion précise du flux de contrôle réel au sein du programme, surtout si le programme a un flux de contrôle complexe ou utilise des fonctionnalités avancées du langage telles que les fonctions récursives ou la gestion des exceptions.

Dans l'ensemble, les graphes d'appels dynamiques et statiques sont tous deux des outils utiles pour comprendre le flux de contrôle au sein d'un programme. Vous pouvez les utiliser ensemble pour obtenir une image plus complète de la manière dont un programme s'exécute.

Les graphes d'appels dynamiques fournissent des informations détaillées sur l'exécution réelle d'un programme, tandis que les graphes d'appels statiques fournissent une vue plus abstraite des chemins d'exécution potentiels d'un programme.

Les deux peuvent être très utiles pour le débogage, l'optimisation et la maintenance du code, et vous pouvez les utiliser dans une variété de contextes différents pour vous aider à mieux comprendre et améliorer votre code.

## Pourquoi avons-nous besoin des graphes d'appels ?

Les principaux avantages de l'utilisation des graphes d'appels, comme nous l'avons vu dans les sections précédentes, peuvent être résumés à travers les concepts suivants :

1. Comprendre la base de code
2. Débogage
3. Optimisation des performances
4. Refactorisation

En visualisant le flux de contrôle à travers le code, nous pouvons voir comment différentes parties du code interagissent entre elles et comment elles s'intègrent dans le tableau général. Cela peut être particulièrement utile lorsque l'on travaille sur une base de code qui nous est nouvelle, car cela peut nous donner un aperçu de haut niveau de la manière dont tout s'emboîte.

Les graphes d'appels peuvent également être utiles pour le débogage. En visualisant le flux de contrôle à travers le code, les développeurs peuvent identifier les problèmes ou bugs potentiels, tels que les boucles infinies ou la récursion. Cela peut être particulièrement utile lorsque l'on travaille sur une base de code sujette aux bugs ou lorsque l'on essaie de corriger un problème particulièrement délicat.

Ils améliorent également l'optimisation des performances, en affichant quelles fonctions ou méthodes sont appelées fréquemment et lesquelles peuvent causer des retards. En utilisant ces informations, nous pouvons identifier les fuites de performance et prendre des mesures pour optimiser le code.

Cela peut être particulièrement important dans les applications qui doivent être rapides et réactives, comme les systèmes en temps réel ou les applications mobiles.

Enfin, nous pouvons tirer parti des graphes d'appels lors de la refactorisation du code. Pour visualiser quelles fonctions ou méthodes dépendent du code que vous modifiez, nous pouvons voir l'impact de leurs changements et nous assurer qu'ils ne cassent rien.

Cela peut être particulièrement important lorsque l'on travaille sur une base de code qui est critique pour les opérations d'une organisation, car cela peut aider à prévenir les temps d'arrêt coûteux.

L'automatisation de la création de graphes d'appels est bénéfique car elle peut faire gagner du temps et des efforts au développeur. Au lieu de dessiner manuellement un graphe d'appels, vous pouvez utiliser un outil pour générer automatiquement le graphe en fonction du code. Cela peut être particulièrement utile dans les grandes bases de code, où la création manuelle d'un graphe d'appels pourrait être chronophage.

De plus, la création automatique de graphes d'appels aide à s'assurer que le graphe d'appels est précis et à jour, car il sera basé sur la version la plus récente du code. Cela devient particulièrement important dans les bases de code qui évoluent constamment, car cela peut aider à garantir que le graphe d'appels reste pertinent et correct.

En bref, les graphes d'appels peuvent être incroyablement utiles pour les développeurs travaillant sur un projet logiciel. Ils aident les développeurs à comprendre la base de code, à déboguer les problèmes, à optimiser les performances et à refactoriser le code.

L'automatisation de la création de graphes d'appels peut faire gagner du temps et des efforts au développeur et garantir que le graphe d'appels est précis et significatif.

## Génération automatique de graphes d'appels

La première méthode que nous aborderons est la création d'un graphe d'appels statique en Java, car il existe des éditeurs de code tels que Intellij Ultimate qui offrent des outils et des plugins pour visualiser un tel graphe sans avoir à ajouter plus de lignes de code.

Ainsi, une fois que vous avez l'éditeur ouvert, appuyez sur **Ctrl+Alt+S** pour accéder aux paramètres de l'éditeur, ou allez simplement dans le menu **Fichier->Paramètres**. Ensuite, entrez dans la section Plugins et recherchez le plugin Call Graph.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/A.png)
_Image par l'auteur_

Comme vous pouvez le voir dans sa description, son objectif est de visualiser les graphes d'appels **Java** (seul langage supporté) de la manière la plus simple possible, ce dont nous pouvons tirer parti.

Après avoir installé le plugin, vous pouvez commencer à créer vos propres graphes d'appels statiques en allant dans **View->Tool Window->Call Graph.** Si cela n'apparaît pas dans le menu supérieur, vous devrez peut-être redémarrer l'éditeur.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Untitled.png)
_Image par l'auteur_

Enfin, vous êtes maintenant en mesure de visualiser facilement le flux de votre code et les relations entre les composants internes, comme vous pouvez le voir dans l'exemple ci-dessus extrait de [ce](https://github.com/cardstdani/practica-java) projet, que nous utiliserons également dans les cas futurs.

En continuant avec les graphes d'appels statiques, nous nous concentrerons sur une méthode spécifique adaptée au langage de programmation Python. Nous commencerons donc par installer les modules requis pour effectuer le processus :

```python
!pip install pyvis
!pip install pycg
```

Avec la commande **pip**, nous avons installé **pyvis**, qui fournit une interface simple et intuitive pour créer, visualiser et analyser des réseaux. Nous avons également inclus **pycg** pour extraire les informations de format de graphe d'un fichier de script Python souhaité.

Dans ce cas, nous utiliserons comme exemple initial simple un script contenant uniquement un programme **hello world**. Cependant, vous pouvez utiliser n'importe quel programme souhaité, quelle que soit sa complexité ou son extension :

```python
print("hello world")
```

Une fois que tout est prêt à être exécuté, la première étape consiste à obtenir les données du graphe d'appels en utilisant la bibliothèque **pycg**. Avec la commande suivante, nous stockons dans un fichier .json toutes les informations nécessaires sur notre graphe d'appels statique, qui sera ensuite converti en sa représentation visuelle :

```
!pycg file.py -o cg.json
```

La deuxième étape consiste à visualiser le graphe résultant à partir du fichier .json. Ainsi, avec les modules **pyvis** et **json** de Python, nous pouvons transformer nos données au format JSON actuel en un fichier **HTML** qui affiche une version interactive du graphe résultant.

```python
import networkx as nx
from pyvis.network import Network
import json

def toNetwork(data: dict)->  nx.DiGraph:
    nt = nx.DiGraph()

    def checkKey(name):
        if name not in nt:
            nt.add_node(name, size=40)

    for node in data:
        checkKey(node)
        for child in data[node]:
            checkKey(child)
            nt.add_edge(node,child)
    return nt

def ntw_pyvis(ntx:nx.DiGraph):
    net = Network(width="1000px",height="1000px", directed=True)
    for node in ntx.nodes:
        net.add_node(node, **{"label":node},)

    for edge in ntx.edges:
        net.add_edge(edge[0], edge[1], width=1)
    net.show('graph.html')

with open("cg.json","r") as f:
    data = json.load(f)

ntw_pyvis(toNetwork(data))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/hw.png)
_Image par l'auteur_

Pour un simple programme hello world, voici à quoi ressemblerait le graphe d'appels statique. Comme vous pouvez le voir, il y a un nœud source (file.py) et un nœud puits encapsulant la fonction unique présente dans notre programme, la fonction intégrée **print().**

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Untitled2-2.png)
_Image par l'auteur_

Cependant, tous les graphes d'appels statiques n'ont pas besoin d'avoir une source et un puits, car ils peuvent appeler n'importe quel nombre de fonctions, de classes, ou même d'autres modules.

Par exemple, le graphe ci-dessus montre un algorithme plus complexe dont la fonction principale est de jouer à un jeu Wordle de manière intelligente. Remarquez le nombre de fonctions intégrées impliquées, ainsi que les références entre les fonctions du script. Tout cela prouve que le graphe n'a pas toujours une structure fixe - au contraire, il dépend de la qualité du code écrit.

## Génération de graphes d'appels dynamiques

Dans cette dernière section, nous allons apprendre comment créer automatiquement un graphe d'appels dynamique pour surveiller les processus Python.

Contrairement à la méthode précédente, ici nous n'avons besoin que d'un seul module pour générer le graphe, et le code supplémentaire global nécessaire pour le processus est substantiellement plus simple.

```python
!pip install pycallgraph
```

Lorsque nous avons installé la bibliothèque pycallgraph, qui, comme son nom l'indique, sera responsable de la génération et de la visualisation du graphe d'appels dynamique associé à notre code.

Nous pouvons l'importer dans un nouveau script Python et utiliser les objets **PyCallGraph/GraphvizOutput** pour générer un fichier .png avec le graphe d'appels correspondant.

```python
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

graph = GraphvizOutput()
graph.output_file = "file4.png"

with PyCallGraph(output=graph):
  print("Hello world")
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/file4.png)
_Image par l'auteur_

Pour un simple programme hello world lancé depuis Google Colab, vous pouvez observer que la structure du graphe dépend maintenant du processus par lequel notre code a été exécuté.

Ainsi, si une fonction n'est pas atteinte par le flux d'exécution, elle ne sera pas affichée dans le graphe dynamique, alors que dans le graphe statique, elle le sera. C'est l'une des raisons les plus transcendantes pour lesquelles nous faisons la distinction entre les deux types.

```python
import re
import math
import json
import os
import concurrent
from concurrent.futures import ProcessPoolExecutor
import requests
import numpy as np

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def procesarEntrada():
    entrada = []
    while len(entrada) != 5:
        entrada = [int(a) for a in input()[:5] if int(a) in range(0, 3)]
    return entrada


def generatePattern(entrada, word):
    pattern = ""
    procesed = {}

    for j in range(len(entrada)):
        letra = word[j]
        if letra not in procesed:
            condition = [k for k in range(j + 1, len(entrada)) if word[k] == letra and entrada[k] == 2]
            if entrada[j] == 0:
                if condition == []: procesed[letra] = 0
            else:
                procesed[letra] = 0
            pattern += [f"(?=[^{letra}]*$)" if condition == [] else f"(?!.{{{j}}}{letra})",
                        f"(?!.{{{j}}}{letra})(?=.*{letra})" + "".join(f"(?!.{{{i}}}{letra})" for i in [k for k in range(j + 1, len(entrada)) if word[k] == letra and entrada[k] in [0, 1]]),
                        f"(?=.{{{j}}}{letra})" + "".join(f"(?!.{{{i}}}{letra})" for i in [k for k in range(j + 1, len(entrada)) if word[k] == letra and entrada[k] in [0, 1]])][
                entrada[j]]
    return f"^{pattern}.*$"


def scoreWord(word, d):
    combinations = ["00000", "00001", "00002", "00010", "00011", "00012", "00020", "00021", "00022", "00100", "00101",
                    "00102", "00110", "00111", "00112", "00120", "00121", "00122", "00200", "00201", "00202", "00210",
                    "00211", "00212", "00220", "00221", "00222", "01000", "01001", "01002", "01010", "01011", "01012",
                    "01020", "01021", "01022", "01100", "01101", "01102", "01110", "01111", "01112", "01120", "01121",
                    "01122", "01200", "01201", "01202", "01210", "01211", "01212", "01220", "01221", "01222", "02000",
                    "02001", "02002", "02010", "02011", "02012", "02020", "02021", "02022", "02100", "02101", "02102",
                    "02110", "02111", "02112", "02120", "02121", "02122", "02200", "02201", "02202", "02210", "02211",
                    "02212", "02220", "02221", "02222", "10000", "10001", "10002", "10010", "10011", "10012", "10020",
                    "10021", "10022", "10100", "10101", "10102", "10110", "10111", "10112", "10120", "10121", "10122",
                    "10200", "10201", "10202", "10210", "10211", "10212", "10220", "10221", "10222", "11000", "11001",
                    "11002", "11010", "11011", "11012", "11020", "11021", "11022", "11100", "11101", "11102", "11110",
                    "11111", "11112", "11120", "11121", "11122", "11200", "11201", "11202", "11210", "11211", "11212",
                    "11220", "11221", "11222", "12000", "12001", "12002", "12010", "12011", "12012", "12020", "12021",
                    "12022", "12100", "12101", "12102", "12110", "12111", "12112", "12120", "12121", "12122", "12200",
                    "12201", "12202", "12210", "12211", "12212", "12220", "12221", "12222", "20000", "20001", "20002",
                    "20010", "20011", "20012", "20020", "20021", "20022", "20100", "20101", "20102", "20110", "20111",
                    "20112", "20120", "20121", "20122", "20200", "20201", "20202", "20210", "20211", "20212", "20220",
                    "20221", "20222", "21000", "21001", "21002", "21010", "21011", "21012", "21020", "21021", "21022",
                    "21100", "21101", "21102", "21110", "21111", "21112", "21120", "21121", "21122", "21200", "21201",
                    "21202", "21210", "21211", "21212", "21220", "21221", "21222", "22000", "22001", "22002", "22010",
                    "22011", "22012", "22020", "22021", "22022", "22100", "22101", "22102", "22110", "22111", "22112",
                    "22120", "22121", "22122", "22200", "22201", "22202", "22210", "22211", "22212", "22220", "22221",
                    "22222"]
    finalScore = 0

    for c in combinations:
        entrada = [int(i) for i in c]
        pattern = generatePattern(entrada, word)
        p = 0
        for i in d.keys(): p += 1 if re.match(pattern, i) else 0
        p /= len(d)
        finalScore += p * math.log(p, 2) if p > 0 else 0
    # print(f"{word}:{finalScore}")
    return finalScore


def paralelDict(item, d):
    return {i: scoreWord(i, d) for i in item}


def updateDict(d, pattern):
    d = {k: 0 for (k, v) in d.items() if re.match(pattern, k)}

    n = os.cpu_count()
    chunkSize = math.ceil(len(d) / n)
    out = {}
    with ProcessPoolExecutor(n) as executor:
        futures = [executor.submit(paralelDict, list(d.keys())[chunkSize * i:chunkSize * (i + 1)], d) for i in range(n)]
        for future in concurrent.futures.as_completed(futures):
            out.update(future.result())
        executor.shutdown()
    return out


def validarEntrada(entrada, word, globalPattern):
    procesed = {}
    for i in range(len(entrada)):
        letra = word[i]
        if letra not in procesed:
            if entrada[i] == 0:
                if (f"(?=.{{{i}}}{letra})" in globalPattern) or (f"(?=.*{letra})" in globalPattern and not max(
                        [entrada[j] == 2 and word[j] == letra for j in range(i + 1, len(entrada))] + [False])) or max([entrada[j] == 1 and word[j] == letra for j in range(i + 1, len(entrada))] + [False]):
                    print(f"Error en 0 letra {letra}")
                    return False
            elif entrada[i] == 1:
                if f"(?=.{{{i}}}{letra})" in globalPattern:
                    return False
            elif entrada[i] == 2:
                if f"(?!.{{{i}}}{letra})" in globalPattern or f"(?=[^{letra}]*$)" in globalPattern:
                    print(f"Error en 2 letra {letra}")
                    return False
            procesed[letra] = 0
    return True

if __name__ == '__main__':
  graph = GraphvizOutput()
  graph.output_file = "file3.png"

  with PyCallGraph(output=graph):
    intentos = 6
    d = json.loads(requests.get("https://media.githubusercontent.com/media/cardstdani/practica-java/main/Data/DictScoreData.txt").text)
    globalPattern = ""
    for intento in range(intentos):
        print(len(d), d, len(d))
        word = max(d, key=d.get)
        print(word, d[word])

        entrada = procesarEntrada()
        pattern = generatePattern(entrada, word)
        if validarEntrada(entrada, word, globalPattern):
            globalPattern += pattern[1:-3]
            try:
              d=json.loads(requests.get(f"https://media.githubusercontent.com/media/cardstdani/practica-java/main/Data/MaxTree/Dict{intento+1}-{''.join([str(a) for a in entrada])}.txt").text)
            except:
              d = updateDict(d, pattern)
        else:
            print("Error detectado, entrada inconsistente")
            intento -= 1
        if entrada == [2, 2, 2, 2, 2]:
            break
```

Pour compléter cette section, nous allons générer le graphe d'appels dynamique d'un code plus complexe comme celui ci-dessus, qui est l'algorithme de résolution de Wordle mentionné précédemment.

Si nous exécutons le code à partir de notre ordinateur personnel, nous obtiendrons le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/file.png)
_Image par l'auteur_

Vous pouvez observer comment dans chaque nœud, il y a des données sur le nom de la fonction, les appels pendant la durée de vie du processus et le temps "vivant" pendant l'exécution. De plus, le nombre d'appels peut être déduit par le degré entrant de chaque nœud, affiché au milieu de chaque arête dirigée.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/file2.png)
_Image par l'auteur_

Cependant, si nous exécutons le code à partir de Google Colab, nous rencontrerons un graphe d'appels beaucoup plus complexe, conséquence de tous les sous-processus qui doivent être effectués pour communiquer avec la machine distante offerte par les services Google, ainsi que les multiples récupérations de données du serveur et les routines de multiprocessus que nécessite le code lui-même.

## Conclusion

Avec ce guide, vous avez appris comment automatiser la création de graphes d'appels, ce qui en soi peut ne pas sembler aussi précieux que cela l'est vraiment.

Mais ils peuvent devenir essentiels dans des situations où nous devons optimiser des algorithmes suffisamment grands pour que la lecture de leur code s'avère inefficace par rapport à l'utilisation d'une représentation graphique.