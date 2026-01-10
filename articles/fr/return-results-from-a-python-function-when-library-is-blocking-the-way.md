---
title: Comment retourner les résultats d'une fonction Python à votre programme lorsqu'une
  bibliothèque bloque le passage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-14T10:46:14.000Z'
originalURL: https://freecodecamp.org/news/return-results-from-a-python-function-when-library-is-blocking-the-way
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/master-gmd-gmd370-g3701-g3701s-cw0011000.jpg
tags:
- name: Python
  slug: python
seo_title: Comment retourner les résultats d'une fonction Python à votre programme
  lorsqu'une bibliothèque bloque le passage
seo_desc: "By David A. Kra\nUsually a Python function passes its results back using\
  \ a return statement.\nThe problem is that sometimes it can't, so you need to figure\
  \ out a different way to return those results. \nThis happens, most often, when\
  \ someone else's libr..."
---

Par David A. Kra

Habituellement, une fonction Python renvoie ses résultats à l'aide d'une instruction `return`.

Le problème est que parfois elle ne peut pas le faire, donc vous devez trouver un autre moyen de retourner ces résultats.

Cela se produit le plus souvent lorsqu'une interface de bibliothèque tierce se met en travers, et vous ne pouvez pas la modifier.

Ce que vous devez accomplir pourrait être appelé le passage de résultats hors bande, dans un flux secondaire, en contournant, en court-circuitant ou en faisant un détour.

Ce tutoriel décrit ce problème à plusieurs niveaux de difficulté, puis propose plusieurs solutions pour gérer ces niveaux, y compris une solution à ne pas utiliser, et pourquoi.

Il y a des conseils sur la façon d'utiliser aussi peu de solutions différentes que possible pour couvrir le problème dans votre projet.

Il s'agit d'un long article, car il vous guide à travers une progression de gravités de problèmes et de leurs solutions.

Cependant, vous n'aurez peut-être besoin que du début, d'une ou deux des solutions décrites, et des conseils vers la fin.

<p>Contenu de ce tutoriel :</p>
<ul>
    <li><a href="#quand-ce-problème-se-produit-il">Quand ce problème se produit-il ?</a>
    </li><li><a href="#comment-trouver-une-solution-en-fonction-de-la-gravité-du-problème">Comment trouver une solution, en fonction de la gravité du problème</a>
	</li><li><a href="#plusieurs-solutions-possibles">Plusieurs solutions possibles</a>
</li><li><a href="#exemple-dune-bibliothèque-python-qui-empêche-le-passage-de-résultats-utiles">Exemple d'une bibliothèque Python qui empêche le passage de résultats utiles</a>
    </li><li>Solutions avec exemples et discussion</li>
		<ul>	<li><a href="#solution-1-utilisation-dun-attribut-de-fonction">Solution #1 : Attribut de fonction</a>
			</li><li><a href="#solution-2-utilisation-dune-variable-globale">Solution #2 : Variable globale (Anti-pattern déprécié)</a>
			</li><li><a href="#solution-3-utilisation-dune-file-dattente">Solution #3 : File d'attente</a>
			</li><li><a href="#solution-4-files-dattente-multiples">Solution #4 : Files d'attente</a>
				<ul><li><a href="#quest-ce-si-votre-programme-de-haut-niveau-na-besoin-que-du-dernier-de-tous-les-résultats-étendus">Variation : File d'attente Last In First Out (LIFO)</a>
				</li><li><a href="#possibilité-de-conception-combiner-les-deux-solutions-viables">Variation : Attribut et file d'attente</a>
				</ul>
			</li><li><a href="#solution-5-enveloppe-python-simple">Solution #5 : Enveloppe Python simple</a>
			</li><li><a href="#solution-6-enveloppe-décorateur-python">Solution #6 : Enveloppe décorateur Python</a>
	</ul>
</li><li><a href="#conseils-pour-sélectionner-la-solution-à-utiliser">Conseils pour sélectionner la solution à utiliser</a>
</li><li><a href="#résumé">Résumé</a>
</ul>

## Quand ce problème se produit-il ?

Vous avez ce problème si une bibliothèque se met en travers, mais vous devez l'utiliser.

Imaginez que votre programme de fonction de haut niveau, **_p,_** appelle une fonction de bibliothèque tierce, **_L,_** qui appelle ensuite votre fonction cible de bas niveau, **_f_**. 

Un bon exemple d'une telle fonction de bibliothèque est `timeit`. 

Le programme de haut niveau doit invoquer la fonction de bibliothèque et obtenir les résultats retournés conformément aux spécifications de l'interface de programmation d'application (API) documentée de cette bibliothèque. 

De même, la fonction **_f_** accepte des paramètres et doit retourner des résultats qui, à nouveau, sont conformes aux spécifications de l'API de cette fonction de bibliothèque. 

La fonction de bibliothèque **_L_** est un intermédiaire interposé. 

Le problème se produit lorsque la bibliothèque intermédiaire et son API ne sont pas sous votre contrôle et ne répondent pas à votre besoin d'acquérir les résultats de la fonction cible.

Souvent, l'API pour retourner les résultats d'une fonction de bas niveau à la bibliothèque intermédiaire et l'API de la bibliothèque à votre fonction de haut niveau, combinées, ne transmettra pas les résultats complets de la fonction de bas niveau.

Typiquement, la bibliothèque provient de pip, Git, Anaconda ou Python lui-même. 

Même si ces bibliothèques sont open source, vous, vos pairs, votre employeur et vos clients ne voulez pas que quiconque modifie les internes et les externes de la bibliothèque.

De plus, si la bibliothèque est comme `timeit.repeat` ou `scipy.optimize.minimize`, alors la fonction cible de bas niveau sera généralement appelée de nombreuses fois. 

## Comment trouver une solution en fonction de la gravité du problème

Comment un programme Python peut-il contourner un blocage de bibliothèque intermédiaire ?

Les concepts que vous devez apprendre et utiliser pour gérer le problème dépendent de l'étendue des besoins : 

1. **Résultat le plus récent** : Votre fonction de haut niveau a besoin d'accéder uniquement au résultat le plus récent de la fonction de bas niveau, même si elle a été appelée de nombreuses fois. Cette solution utilise l'idée de [mémoisation](https://www.freecodecamp.org/news/memoization-in-javascript-and-react/) en stockant le dernier résultat dans [un attribut de la fonction de bas niveau](https://sethdandridge.com/blog/assigning-attributes-to-python-functions). En utilisant une convention de nommage, le nom de l'attribut est toujours le même. Cela est sûr, peu importe combien de fonctions différentes, même des alias, utilisent ce même nom d'attribut. Au lieu d'utiliser un attribut, une solution alternative utilise le concept de [variable globale](https://www.freecodecamp.org/news/python-global-variables-examples/#keyword). Utiliser une variable globale n'est pas une bonne chose à faire. L'exemple fourni démontre comment c'est une mauvaise pratique non sécurisée. 
2. **Besoin de chaque résultat** : Votre fonction de haut niveau a besoin du résultat de chacun des nombreux appels que la bibliothèque fait à la fonction de bas niveau. La solution utilise le concept de [file d'attente](https://www.guru99.com/python-queue-example.html), tel qu'implémenté par [la bibliothèque de file d'attente standard de Python](https://docs.python.org/3/library/queue.html). 
3. **Besoin de chaque résultat, mais allant à différents endroits** : Plusieurs endroits dans les fonctions de haut niveau appellent la fonction de bas niveau à travers un ou plusieurs intermédiaires. Chacun a besoin de son propre ensemble de résultats. La solution utilise plusieurs files d'attente, avec la file d'attente à utiliser étant passée en tant que paramètre à la fonction de bas niveau.
4. **Ne peut pas améliorer la fonction de bas niveau** : La fonction de bas niveau provient d'une bibliothèque ou d'ailleurs, donc vous ne pouvez pas ou ne devez pas la changer. La solution utilise le concept d'une [enveloppe](https://en.wikipedia.org/wiki/Wrapper_function). L'enveloppe configure la file d'attente et les attributs, appelle la fonction de bas niveau et fait ce qui est nécessaire avec le résultat. La solution utilise le concept générique d'une enveloppe, mais n'utilise pas le concept avancé de Python de "décorateurs enveloppes".
5. **Ne peut pas améliorer la fonction de bas niveau. Besoin de chaque résultat, mais allant à différents endroits** : Cela combine les besoins les plus avancés. La solution exploite le concept avancé de Python de [décorateurs enveloppes](https://forum.freecodecamp.org/t/python-decorators-explained-with-examples/19198). Cela élimine le besoin de passer des objets de file d'attente en tant que paramètres.

Des exemples de code sont fournis pour chacun de ces cas.

Mon cas qui a initialement motivé cet effort était au niveau de "besoin de chaque résultat". 

L'intermédiaire était une boucle imbriquée impliquant deux fonctions de bibliothèque. 

Mon programme de haut niveau a invoqué la fonction `timeit.repeat` qui a ensuite invoqué `scipy.optimize.minimize` plusieurs fois. 

Chaque invocation de `scipy.optimize.minimize` a invoqué ma fonction de bas niveau de nombreuses fois. 

Pour chaque exécution de ma fonction de bas niveau, je voulais qu'elle transmette des résultats au programme principal, tout en haut et autour des deux bibliothèques.

L'effort de conception et de développement a gardé à l'esprit certaines bonnes pratiques :

* **Éviter les conflits de nommage ou les interférences** : Cela est particulièrement important lorsqu'il y a plusieurs fonctions cibles qui doivent retourner leurs propres résultats de flux secondaire. Il est également important lorsque la fonction cible pourrait être appelée à partir de plusieurs endroits dans le code de haut niveau ou à travers plusieurs intermédiaires.
* **Éviter le couplage** : Minimiser le couplage explicite entre les fonctions de haut niveau et de bas niveau.
* **Fournir de l'optionalité** : Éviter d'imposer des exigences de codage supplémentaires à l'appelant de haut niveau s'il n'a pas besoin des résultats supplémentaires.

### Plusieurs solutions possibles

Les deux premières alternatives de solution dans ce tutoriel sont applicables lorsqu'un seul résultat est nécessaire, et que ce résultat provient de l'exécution finale de la fonction cible.

La troisième alternative de solution est applicable lorsqu'un résultat est nécessaire à partir de chaque exécution de la fonction cible ou de chaque exécution terminée d'une boucle intérieure d'appels à la fonction cible.

1. Attribut de fonction – Bon pour un résultat. Chaque définition d'un résultat écrase le précédent.
2. Variable globale – Bon pour un résultat. Chaque définition écrase également le précédent. Cette alternative est un anti-pattern déprécié pour des raisons philosophiques et techniques Pythoniques, qui seront expliquées ci-dessous.
3. File d'attente – Bon pour un ou plusieurs résultats. Il y a des choix concernant l'ordre des résultats. 
4. Files d'attente – Bon pour plusieurs résultats, mais où ils ne vont pas tous au même endroit.  
5. Enveloppe simple – Bon lorsque vous ne pouvez pas changer la fonction de bas niveau. Cette solution n'est pas vraiment fondamentalement différente de placer des résultats dans un attribut ou une file d'attente. Cependant, elle externalise le code qui irait à l'intérieur de la fonction cible. Le résultat est une fonction qui enveloppe la fonction cible, qui pourrait être immuable, dans une bibliothèque, d'une manière qui ne nécessite pas d'expertise avancée en Python.
6. Enveloppe décorateur Python – Utilise le mécanisme d'enveloppement de fonction avancé "décorateur" de Python. Il permet plusieurs files d'attente et attributs sans altérer la fonction de bas niveau sous-jacente. Il peut être difficile à comprendre, mais est facile à utiliser dans votre code.

Toutes les alternatives fonctionnent avec le multithreading. 

Les alternatives de file d'attente et d'enveloppe fonctionnent également avec le multiprocessing.

## Exemple d'une bibliothèque Python qui empêche le passage de résultats utiles

Commençons par causer le problème, puis nous passerons en revue chaque solution possible.

```python
# LibraryL.py
# usage:  from LibraryL import L
# Le but de cette bibliothèque et de sa seule fonction est de démontrer un intermédiaire qui empêche une fonction invoquée de retourner des résultats utiles à l'appelant de haut niveau.
# Imaginez qu'elle se trouve dans une bibliothèque externe non sous le contrôle du programmeur d'application.
#

def L(f,fparms=[],Lparms=[]): # fonction intermédiaire
# f: fonction cible; 
# fparms: objet paramètre à passer à f. Par défaut []
# Lparms: objet à utiliser par L lui-même (non utilisé dans cet exemple). Par défaut [].

    rf=f(fparms) # passe fparms à f, appelle f, collecte sa valeur de retour
    return rf.__class__.__name__
    
# L ne retourne pas à son appelant ce que la fonction f a retourné à L, seulement le nom de la classe de l'objet retourné, comme 'list'. C'est un bon exemple d'un mauvais exemple.
```

Cette fonction, L, sera utilisée comme fonction intermédiaire dans les exemples de solution ci-dessous.

### Solution #1 : Utilisation d'un attribut de fonction

La fonction de bas niveau stocke son résultat utile dans un attribut Python, conformément à une convention de nommage.

```python
def f(fparms):  # Fonction de bas niveau à appeler à travers un intermédiaire
# Convention de nommage des attributs : <nom_de_la_fonction>.mrrv 
#     où mrrv signifie Most Recent Result Value
    # Créer l'attribut, afin qu'il existe même en cas d'exception levée avant que le résultat ne soit défini.
    
    if not hasattr(f, "mrrv"): f.mrrv=None  
    # f.mrrv=None # décommentez pour le vider à chaque appel.
    # faire le travail 
    
    ultimate_result=["this", "that", 42, "and the other thing"]
    f.mrrv=ultimate_result
    result_to_return=42
    return result_to_return

def p(): # Fonction de haut niveau appelant f à travers l'intermédiaire L
    from LibraryL import L
    fparms=[]
    Lparms=[]
    r=L(f, fparms, Lparms) # invoque f à travers L
    resultfromf=f.mrrv
    print(resultfromf)
    # faire le travail 
p()
quit()
```

Sortie : 

`['this', 'that', 42, 'and the other thing']`

Dans cette solution, la fonction invoquée place son résultat de flux secondaire dans un attribut au sein de l'objet de fonction, conformément à une simple convention de nommage. 

Chaque fonction a son propre attribut local dans lequel déposer les résultats. 

Le nom de l'attribut, `mrrv`, pour la valeur de résultat la plus récente est le même dans toutes les fonctions qui utilisent cette technique, donc cela fonctionne même lorsque la fonction appelée est appelée à travers un alias, comme dans l'exemple suivant :

```python
# Démonstration de la façon dont la solution d'attribut fonctionne correctement,
#   même si la fonction cible a été aliasée.  

def get_target_function():
   return f

def p():
    g=get_target_function() # g.__name__ fournirait le nom de chaîne de la fonction aliasée sous-jacente. Alors quoi ? Nous n'en avons pas besoin. 
    # Faire d'autres choses.
    from LibraryL import L
    gparms=[]
    Lparms=[]
    r=L(g, gparms, Lparms) # invoque g à travers L
    # L invoque g, qui est vraiment f
    # f définit f.mrrv 
    # Peu importe que g ne soit pas le vrai nom de la fonction.
    resultfromg=g.mrrv # Pas de problème. 
    print(resultfromg)

p()
quit()
```

Sortie : 

`['this', 'that', 42, 'and the other thing']`

L'attribut a une seule valeur dans chaque fonction, bien que cette seule valeur puisse être une liste ou un autre objet complexe. 

Même si la fonction est appelée à partir de plusieurs endroits dans le code, même si à partir de plusieurs threads, l'attribut aura toujours la valeur définie le plus récemment par un appel dans le processus.

Dans la gestion initiale au début de la fonction de bas niveau, si l'attribut n'existe pas déjà, la valeur de l'attribut est définie sur `None`. 

De cette façon, même si la fonction retourne sans définir l'attribut sur une valeur utile, les références à l'attribut ne lanceront pas d'exception. 

Facultativement, l'attribut pourrait être défini sur `None` au début de chaque appel, afin de vider tout résultat précédent. 

Faire cela peut être indésirable dans un environnement multithread.

### Solution #2 : Utilisation d'une variable globale

**Avertissement** : Cette solution alternative est un [anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern) déprécié pour des raisons philosophiques et techniques Pythoniques, que j'expliquerai ci-dessous. 

Je l'ai fournie uniquement comme un homme de paille à des fins éducatives pour illustrer de mauvaises pratiques de programmation :

```python
def f(fparms): # DEPRECATED Fonction de bas niveau à appeler à travers un intermédiaire
    # Convention de nommage de l'objet global :    <nom_de_la_fonction_invoquée>_mrrv
    # où mrrv représente Most Recent Result Value
    
    global f_mrrv
    f_mrrv=None # efface le global, au cas où une exception est levée avant que le résultat ne soit défini.
    # faire le travail, puis
    
    ultimate_result=["this", "that", 42, "and the other thing"]
    f_mrrv=ultimate_result
    result_to_return=42
    return result_to_return

def p(): # programme d'appel de haut niveau
    from LibraryL import L
    # Convention de nommage de l'objet global :     <nom_de_la_fonction_invoquée>_mrrv
    global f_mrrv # inutile d'utiliser cette instruction globale si L est appelé depuis __main__ , mais cela ne fait pas de mal
    fparms=[]
    Lparms=[]
    r=L(f, fparms, Lparms) # invoque f à travers L
    resultfromf=f_mrrv
    print(resultfromf)
# faire le travail.

p()
quit()
```

Sortie :

`['this', 'that', 42, 'and the other thing']`

Cette solution donne à chaque fonction son propre espace global pour déposer les résultats. 

Le nom de la variable est basé sur le nom de la fonction invoquée. 

La fonction invoquée place son résultat de flux secondaire dans sa variable globale. 

La fonction `framus` placerait son résultat dans la variable globale `framus_mrrv`.

Dans la gestion initiale au début de la fonction invoquée, le code définit la valeur de la variable globale sur `None`. 

De cette façon, même si la fonction retourne sans définir la variable sur une valeur utile, les références à la variable ne lanceront pas d'exception. 

De plus, tout résultat d'un appel précédent est effacé. 

La variable globale est une seule valeur, bien que cette seule valeur puisse être une liste ou un autre objet complexe. 

Même si la fonction est appelée à partir de plusieurs endroits dans le code, la variable globale n'aura que la valeur la plus récente définie par un appel à cette fonction dans le processus.

#### Pourquoi cette solution est-elle dépréciée ?

Cette alternative de variable globale est dépréciée pour des raisons philosophiques et techniques Pythoniques.

**Philosophique** : Cette solution s'impose au code de la fonction de haut niveau et injecte un objet dans l'espace de noms global. La solution d'attribut ne fait pas cela. La fonction de bas niveau pourrait être utilisée dans de nombreux programmes. Certains pourraient ne pas avoir besoin du résultat étendu. Avec la solution d'attribut, si l'invocateur de haut niveau n'a pas besoin du résultat étendu, il n'a pas besoin de s'en soucier ou de faire quoi que ce soit d'extra.

**Technique** : D'un point de vue technique, la solution de variable globale n'est pas robuste. Python traite les fonctions comme des objets de première classe. Le même objet de fonction peut être assigné à plusieurs noms de variables. Chaque nom peut alors être utilisé comme un alias pour la fonction. Le code de démonstration cassé à venir fait cela. 

Dans l'exemple, la fonction cible crée une variable globale avec un nom.

Ensuite, la fonction de haut niveau cherche le résultat ailleurs, en supposant qu'il a un nom différent.

La solution d'attribut évite ce problème. 

Avec la solution d'attribut, la fonction cible définit un attribut, `mrrv`, à l'intérieur de la fonction elle-même, et non dans un autre objet. 

La fonction de haut niveau référence ce même nom d'attribut dans cet même objet, même si elle référence l'objet à travers un alias. 

Elle peut le faire car le nom de l'attribut est lié à l'objet dont il fait partie, et non au nom utilisé pour accéder à l'objet.

Voyons comment la solution de variable globale est cassée :

```python
# Démonstration de la façon dont la solution de variable globale est cassée.
def get_target_function():
   return f

def p(): # CASSÉ ! Démonstration de pourquoi NE PAS utiliser la solution de variable globale.
# Oubliez ou ignorez que g n'est pas le vrai nom de la fonction.
    g=get_target_function() # p() ne sait pas et ne peut pas savoir le nom de la fonction cible de g
    # Faire d'autres choses.
    
    from LibraryL import L
    # Convention de nommage de l'objet global : <nom_de_la_fonction_invoquée>_mrrv
    # Créer puis utiliser g_mrrv, que la fonction ne définira pas.
    
    global g_mrrv # PAS BIEN : Ce n'est pas le nom du global qui sera défini par le code à l'intérieur de la fonction.
    gparms=[]
    Lparms=[]
    r=L(g, gparms, Lparms) # invoque g à travers L
    
    # L invoque g, qui est f
    # f définit f_mrrv et non g_mrrv
    
    resultfromg=g_mrrv # N'a pas été défini. g (alias pour f) a défini f_mrrv
    print(resultfromg)
# Échec de faire le travail.
```

### Solution #3 : Utilisation d'une file d'attente

Dans cette solution, la fonction de bas niveau place ses résultats étendus dans une file d'attente Python. Une fonction de haut niveau récupère les résultats. 

Habituellement, en Python, nous pensons à utiliser des files d'attente dans des applications multithread ou multiprocessing. 

Ici, la file d'attente est utilisée pour le transfert d'informations entre les fonctions, même dans le même thread. 

Il existe des variations de la solution de file d'attente. 

Elles varient selon la fonction qui crée la file d'attente et la manière dont l'autre fonction accède à l'objet de file d'attente. 

Dans cette solution, l'objet de file d'attente est stocké dans un attribut de fonction dans la fonction de bas niveau. L'attribut est nommé conformément à une convention de nommage. 

Cela est conceptuellement similaire à la solution d'attribut, sauf que l'attribut contient un objet de file d'attente, plutôt que les résultats eux-mêmes. Les résultats sont placés dans la file d'attente. 

Si le programme d'appel est intéressé par les résultats étendus, il peut lire dans la file d'attente une fois que la fonction invoquée a terminé.  

**Avertissement** : Si la fonction de bas niveau s'exécute des milliers ou des millions de fois sans que la fonction de haut niveau ne vide la file d'attente, il pourrait y avoir un plantage du processus dû à un manque de mémoire.

```python
# Solution #3 : Objet de file d'attente dans un attribut de fonction

# fonction de bas niveau
def f(fparms): # le résultat final est placé dans une file d'attente qui est stockée dans un attribut de fonction. 
    ultimate_result=None
    # Convention de nommage de l'objet de file d'attente : <nom_de_la_fonction_invoquée>.sidestreamoutq
    
    if not hasattr(f, "sidestreamoutq"): f.sidestreamoutq=queue.Queue() # ne créer la file d'attente qu'une seule fois. 
    # faire des choses utiles
    
    ultimate_result=["what comes in is what is returned",fparms]
    f.sidestreamoutq.put(ultimate_result)
    result_to_return=42
    return result_to_return

def get_target_function():
   return f

# fonction de haut niveau
def p():
    fparms4=[4, "queueID in a function attribute", 84]
    fparms5=[5, "queueID in an aliased function's attribute", 84]
    Lparms=[]
    r4=L(f, fparms4, Lparms)
    while not f.sidestreamoutq.empty():
         f_result=f.sidestreamoutq.get()
         print(f_result) 
         
    # maintenant faire la même chose avec un alias de la fonction de bas niveau
    
    g=get_target_function() # p() ne sait pas et ne peut pas savoir le nom de la fonction cible de g
    r5=L(g, fparms5, Lparms)
    while not g.sidestreamoutq.empty(): # Notez que g.sidestreamoutq === f.sidestreamoutq. Lire depuis l'un est la même chose que lire depuis l'autre.
         g_result=g.sidestreamoutq.get()
         print(g_result)

#  __main__ 
import queue 
from LibraryL import L
p()
quit()
```

Dans cette variation de solution, la fonction de bas niveau crée un objet de file d'attente puis définit un attribut de fonction en elle-même pour y faire référence. 

Selon une convention de nommage, le nom de l'attribut est `sidestreamoutq`. 

Mais parce qu'il existe au sein d'un objet de fonction, il est référencé comme `whateverfunctionname.sidestreamoutq`. 

La fonction invoquée place son résultat de flux secondaire dans cette file d'attente. 

Comme démontré dans le code d'exemple, cette solution fonctionne même si le programme d'appel alias le nom de la fonction de bas niveau, comme avec `someotherfunctionname=lowlevelfunctionname`, puis invoque `L(`someotherfunctionname`, fparms, Lparms)`.  

La raison est que toutes les références dans `someotherfunctionname` sont des références aux mêmes instances d'objets que dans `lowlevelfunctionname`.

Dans la gestion initiale au début de la fonction invoquée, la fonction (a) définit la valeur du résultat étendu sur `None` et (b) crée la file d'attente des résultats, mais seulement si elle n'existe pas déjà. 

Faire cela ne force pas automatiquement les résultats à être placés dans la file d'attente si la fonction échoue ou se termine sans une mise explicite.

Mais si la fonction ne change pas la valeur en autre chose, alors si la fonction fait la mise, alors l'élément mis dans la file d'attente aurait la valeur définie `None`.

#### Solution #4 : Files d'attente multiples

Dans cette solution, les fonctions de haut niveau spécifient les files d'attente qui recevront les résultats. 

Aucune convention de nommage n'est requise pour l'objet de file d'attente. 

La fonction de haut niveau crée un objet de file d'attente puis l'inclut parmi les paramètres passés à travers l'intermédiaire à la cible. 

La fonction de bas niveau extrait la valeur de l'objet de file d'attente et l'utilise.  

Cela est significativement différent des solutions précédentes. 

Les solutions précédentes ont toutes reposé sur une convention de nommage pour l'objet à partager entre la fonction d'appel de haut niveau et la fonction cible. 

Cela crée un couplage de noms explicite entre les fonctions. 

En informatique, ce couplage est généralement considéré comme indésirable. 

Même dans le cas d'un intermédiaire, ce couplage est généralement évitable, au prix d'une augmentation de la complexité du code. 

Le "généralement évitable" est chaque fois que l'appelant de l'intermédiaire peut spécifier une valeur de paramètre supplémentaire qui sera passée à la cible. 

Dans ce cas, la valeur supplémentaire est l'objet de file d'attente. 

Cette solution n'est pas une option viable si l'intermédiaire ne permet pas à l'appelant de passer l'objet de file d'attente à la fonction cible. 

Ici, c'est faisable, et le code le fait :

```python

# Solution 4. Permettre plusieurs files d'attente.
def fqp(fparms): # fparms est une liste contenant des valeurs à passer à f, incluant un objet de file d'attente auquel envoyer le résultat final 
    ultimate_result=None
    # Complexité supplémentaire : Extraire l'objet de file d'attente des résultats de la liste de paramètres entrants
    
    sidestreamoutq=None
    for p in fparms: # trouver et utiliser le premier élément de la liste de paramètres qui est une Queue ou LifoQueue
        if p.__class__.__name__ in ["Queue", "LifoQueue"] : 
            sidestreamoutq=p
            break
    # faire des choses utiles
    
    ultimate_result=["this", "that", 42, "and the other thing", fparms]
    # mettre l'objet de résultat dans la file d'attente des résultats, s'il y en a une
    
    if not (sidestreamoutq is None): sidestreamoutq.put(ultimate_result)  
    result_to_return=42
    return result_to_return
    
# usage: 
def p():
    potusqueue=queue.Queue() # pourrait utiliser queue.LifoQueue(), et un seul get, si vous ne voulez que le dernier élément
    flotusqueue=queue.LifoQueue() 
    fparms1a=[11, "George", potusqueue, 1788] # bparms est une liste contenant des valeurs à passer à b
    fparms1b=[12, "George", potusqueue, 1792] # bparms est une liste contenant des valeurs à passer à b
    fparms2=[3, "no queueID in the parameters", 1789] # en n'incluant pas l'objet de file d'attente parmi les paramètres, la fonction ne mettra pas les résultats dans la file d'attente.
    fparms3=[4, flotusqueue, "Martha", 1788, 1792]
    Lparms=[]
    r1a=L(fqp, fparms1a, Lparms) # invoque fqp à travers L
    r1b=L(fqp, fparms1b, Lparms) # invoque fqp à travers L
    r2=L(fqp, fparms2, Lparms) # fparms2 manque un queueID.
    r3=L(fqp, fparms3, Lparms)
    #print("drain potusqueue and flotusqueue")
    while not potusqueue.empty():
         f_result=potusqueue.get()
         print(f_result)
         # utiliser le f_result
    if not flotusqueue.empty(): # seulement intéressé par le dernier résultat sur la file d'attente LIFO
         f_result=flotusqueue.get()
         print(f_result)
         # utiliser le f_result     
     
#  __main__ 
import queue 
from LibraryL import L
p()
quit()
    


Dans cette solution, la fonction d'appel crée un ou plusieurs objets de file d'attente LIFO ou FIFO. 

La fonction d'appel inclut cet objet de file d'attente parmi les paramètres passés à la bibliothèque pour que la bibliothèque les passe à la fonction cible. 

Cette fonction invoquée recherche et, si présent, extrait l'objet de file d'attente de ses paramètres entrants.

Dans la gestion initiale au début de la fonction invoquée, elle définit la valeur du résultat sur `None`. 

Faire cela ne provoque pas la mise de `None` dans la file d'attente si la fonction échoue ou se termine sans une mise explicite. 

Mais si la fonction ne change pas la valeur en autre chose, lorsque la fonction fait la mise, alors l'élément dans la file d'attente aura la valeur définie `None`. 

La fonction ne met les résultats dans la file d'attente que si elle a reçu un objet de file d'attente parmi ses paramètres.

#### Que faire si votre programme de haut niveau n'a besoin que du dernier de tous les résultats étendus ?

Parfois, seul le dernier résultat intéresse le programme de haut niveau. 

Si c'est vrai, et qu'une file d'attente est utilisée, il existe une alternative à la vidange de toute la file d'attente et à la conservation uniquement du dernier résultat. 

Au lieu de cela, créez la file d'attente comme une file d'attente Last-In-First-Out avec `anyqueue=queue.LifoQueue()` au lieu de `anyqueue=queue.Queue()`. 

Ensuite, le premier (et probablement le seul) `anyqueue.get()` obtiendra la dernière entrée mise dans la file d'attente.

Le code de solution d'exemple ci-dessus crée deux files d'attente, une FIFO et une LIFO. 

Il passe la file d'attente FIFO en tant que paramètre sur deux appels et la file d'attente LIFO sur un.

Il vide autant de résultats qu'il y en a sur la file d'attente FIFO, mais n'obtient qu'une seule entrée de la file d'attente LIFO. 

C'est parce que l'intention est d'utiliser la file d'attente LIFO lorsque l'élément le plus récemment mis est celui d'intérêt initial ou le seul d'intérêt. 

## Possibilité de conception – Combiner les deux solutions viables

Ces deux options, (a) attribut de fonction cible et (b) paramètre d'objet de file d'attente de fonction d'appel, peuvent être combinées. 

La combinaison permet à la fonction de haut niveau de spécifier facultativement une file d'attente pour recevoir les résultats étendus. 

Si elle n'est pas spécifiée par la fonction de haut niveau, la fonction de bas niveau les met dans l'objet de file d'attente qu'elle a créé et stocké dans un attribut de fonction. 

Le code suivant fait cela. 

Notez qu'il ne change pas l'attribut contenant la file d'attente par défaut lorsque la fonction est utilisée avec une file d'attente spécifiée par l'appelant. 

Cela permet aux appelants à plusieurs endroits dans le code d'appel d'utiliser différentes files d'attente, ou d'utiliser la file d'attente par défaut, comme spécifié dans l'attribut de la fonction :

```python
def fqap(fparms): # le résultat final est mis dans un objet de file d'attente dont la valeur est dans un paramètre de fonction ou, si non spécifié, dans un attribut. 
    ultimate_result=None
    # Convention de nommage de l'objet de file d'attente : <nom_de_la_fonction_invoquée>.sidestreamoutq
    
    if not hasattr(fqap, "sidestreamoutq"): fqap.sidestreamoutq = queue.Queue() # ne créer l'attribut de file d'attente par défaut qu'une seule fois. Il pourrait ne jamais être utilisé.
    q2use = fqap.sidestreamoutq
    for p in fparms: # trouver et utiliser le premier paramètre qui est une Queue ou LifoQueue, s'il y en a un.
        if p.__class__.__name__ in ["Queue", "LifoQueue"] : 
            q2use=p
            break
    # faire des choses utiles
    
    ultimate_result=["this", "that", 42, "and the other thing", fparms]
    fqap.mrrv=ultimate_result
    q2use.put(ultimate_result)
    result_to_return=42
    return result_to_return
```

Quelques points à garder à l'esprit lors de l'utilisation de solutions basées sur des files d'attente :

**Mémoire** : Les entrées de la file d'attente existent en mémoire virtuelle. Si les résultats étendus sont placés dans une file d'attente, mais jamais récupérés, alors après des milliers ou des millions d'appels, le processus ou le système manquera éventuellement de mémoire et plantera (sauf si le processus se termine en premier). Qu'il s'agisse d'une terminaison ordonnée ou d'un plantage, à ce moment-là, tous les éléments de la file d'attente qui n'ont pas été récupérés sont jetés.

**Plusieurs alias pour la même file d'attente** : La variation basée sur les attributs a un objet de file d'attente, peu importe le nombre d'alias que la fonction a. Lorsqu'une fonction de haut niveau vide une file d'attente basée sur les attributs, la boucle obtiendra tous les résultats de cette file d'attente, même s'ils y ont été placés par un appel à la fonction sous un autre alias.  

Dans l'exemple de la Solution #3 ci-dessus, `f.sidestreamoutq.get()` lit dans la même file d'attente que `g.sidestreamoutq.get()`. 

L'implication est que s'il y a des appels à `L(f,...)`, suivis d'appels à `L(g,...)`, suivis d'une boucle jusqu'à ce que `f.sidestreamoutq.get()` soit vide, alors cette boucle `get` obtiendra tous les résultats placés là par tous les appels, qu'ils soient à `f` ou à `g`. 

### Solution #5 : Enveloppe Python simple

Que faire si la fonction de bas niveau provient d'une bibliothèque ou d'ailleurs, donc vous ne pouvez pas ou ne devez pas la changer ? 

Cette solution utilise le concept d'une enveloppe. 

L'enveloppe configure la file d'attente et les attributs, appelle la fonction de bas niveau, fait ce qui est nécessaire avec le résultat, et fournit le retour que la bibliothèque exige. 

La solution utilise le concept générique d'une enveloppe, mais n'utilise pas le concept avancé de Python de "décorateurs enveloppes".

Cette solution n'est pas vraiment fondamentalement différente de placer des résultats dans un attribut ou une file d'attente. 

Cependant, elle externalise le code qui irait à l'intérieur de la fonction cible si vous pouviez la changer. 

Le résultat est une nouvelle fonction qui enveloppe simplement la fonction cible : 

```python
#Solution #5 : Enveloppe Python simple
import queue 
from LibraryL import L

# La fonction que nous ne pouvons pas changer
def f(fparms=[]):
    return ["f returns",fparms]

# Cette enveloppe est spécifique à la fonction f.
def wrapped_f(fparms): # enveloppe f. Utile lorsque le code source de f ne peut pas être édité.
    # Cette fonction invoque la fonction f puis 
    #  dépose les résultats retournés dans un attribut et une file d'attente.
    #   Convention de nommage de l'objet de file d'attente : 
    #         <nom_de_la_fonction_enveloppe>.sidestreamoutq
    #   Convention de nommage de l'objet de résultat : 
    #         <nom_de_la_fonction_enveloppe>.mrrv
    #
    # Pour des performances plus élevées si fwrap sera appelée des millions de fois, 
    #    déplacez l'instruction suivante dans une fonction de haut niveau,
    #    afin que les tests ne soient effectués qu'une seule fois chacun.
    
    if not hasattr(wrapped_f, "sidestreamoutq"): wrapped_f.sidestreamoutq=queue.Queue()    
    # 
    # Appeler simplement f
    ultimate_result=f(fparms)
    # Laisser le résultat dans les attributs de cette fonction et le mettre dans la file d'attente
    
    wrapped_f.mrrv=ultimate_result 
    wrapped_f.sidestreamoutq.put(ultimate_result)
    if False: # Les instructions suivantes créeraient et définiraient des attributs dans la fonction cible.
              # Cette injection n'est pas considérée comme une bonne pratique de programmation si elle n'est pas nécessaire, et ici elle ne l'est pas.
        if not hasattr(f, "sidestreamoutq"): f.sidestreamoutq=wrapped_f.sidestreamoutq # Même Queue. Ne la définir que si elle n'existe pas 
        f.mrrv=ultimate_result 
        # endif if False
    result_to_return=42
    return result_to_return
    
def test_wrapped_f():
    print(["object f: ", f ])
    print(["use f directly:", f("use f directly:")])
    # sidestream f
    print(["wrapped f object: ", wrapped_f])
    print(["use wrapped_f directly:", wrapped_f("use sidestreamed_f directly:")])
    print(["wrapped f Attribute:", wrapped_f.mrrv])
    print(["wrapped f Q entry:", wrapped_f.sidestreamoutq.get()])
    # print(["direct f Attribute:", f.mrrv])
    # print(["direct f Q entry:", f.sidestreamoutq.get()])
    print(["wrapped_f through L returns:", lwfr:=L(wrapped_f,["use L(sidestreamed_f):"])])
    print(["wrapped f Attribute:", wrapped_f.mrrv])
    print(["wrapped f Q entry:", wrapped_f.sidestreamoutq.get()])
    return 
    
test_wrapped_f()
quit()
""" Sortie attendue, mais avec des adresses différentes :
['object f: ', <function f at 0x7fbf5f57fd90>]
['use f directly:', ['f returns', 'use f directly:']]
['wrapped f object: ', <function wrapped_f at 0x7fbf5ea36cb0>]
['use wrapped_f directly:', 42]
['wrapped f Attribute:', ['f returns', 'use sidestreamed_f directly:']]
['wrapped f Q entry:', ['f returns', 'use sidestreamed_f directly:']]
['wrapped_f through L returns:', 'int']
['wrapped f Attribute:', ['f returns', ['use L(sidestreamed_f):']]]
['wrapped f Q entry:', ['f returns', ['use L(sidestreamed_f):']]]
"""
```

Cette solution est similaire à la Solution #3 File d'attente, en ce sens qu'il y a exactement une file d'attente pour l'enveloppe. 

Afin d'avoir des usages pour une fonction cible tout en ayant des résultats qui vont à différentes files d'attente et attributs, vous pourriez définir des fonctions d'enveloppe supplémentaires, telles que `wrapped_f2()`, `wrapped_f3()`, et ainsi de suite. 

Chacune serait presque identique à `wrapped_f()`, sauf pour changer toutes les instances de "wrapped_f" en "wrapped_f2", "wrapped_f3", et ainsi de suite.

### Solution #6 : Enveloppe décorateur Python

Que faire s'il y a beaucoup de fonctions de bas niveau, donc les modifier toutes serait un cauchemar de maintenance fastidieux ? 

Que faire si les nombreuses fonctions de bas niveau proviennent de bibliothèques ou d'ailleurs, donc vous ne pouvez pas ou ne devez pas les changer ? 

Que faire s'il doit y avoir plusieurs attributs de résultat pour certaines fonctions ? Par exemple, une fonction est appelée à partir de plusieurs endroits dans le code ou à partir de plusieurs threads.

Cette solution utilise également le concept d'une enveloppe, mais différemment de ce qui précède.

La Solution #5 a le problème de la prolifération du code. Elle nécessite d'écrire une fonction supplémentaire pour chaque utilisation indépendante de chaque fonction de bas niveau.  

À grande échelle, cela devient également un cauchemar de maintenance sujet aux erreurs. Il pourrait être catégorisé comme, "Facile à apprendre, mais pas facile à utiliser à grande échelle."

Au lieu de cela, cette solution génère les enveloppes à la demande, à l'exécution, à partir d'un ensemble de code générique de générateur d'enveloppe. Elle permet plusieurs files d'attente et attributs sans altérer la fonction de bas niveau sous-jacente. 

Chaque utilisation du générateur pour créer une autre enveloppe ne prend qu'une simple ligne de code, comme `sidestreamed_f2=create_sidestream_wrapper_func(f)`.

La technique utilisée ici est appelée un "décorateur" Python. Je catégorise les décorateurs comme avancés en Python. 

Les décorateurs sont expliqués dans deux articles de freeCodeCamp, un par [Roy Chng](https://www.freecodecamp.org/news/python-decorators-explained/), et un par [Brandon Wallace](https://www.freecodecamp.org/news/python-decorators-explained-with-examples/). Veuillez étudier le sujet à travers ces articles. 

Ici, nous allons simplement utiliser la technique.  Elle peut être catégorisée comme, "Facile à utiliser à grande échelle, mais pas facile à apprendre."

Ici, le générateur d'enveloppe, y compris le code définissant notre enveloppe spécifique et créant sa file d'attente, n'est que de 8 lignes de code exécutable dans `create_sidestream_wrapper_func`, sans compter les instructions `print`, que vous supprimerez pendant les tests :

```python
#!/bin/python3
#Solution #6 : Générateur d'enveloppe décorateur Python

import queue 
from LibraryL import L

# fonction que nous ne pouvons pas changer
def f(fparms=[]):
    return ["f returns",fparms]
    
def create_sidestream_wrapper_func(myfunc):
# Utilisation
# Créer la fonction : sidestreamed_f=create_sidestream_wrapper_func(f)
# fparm=["This", "that", "and the other thing"]
# Utiliser la fonction créée :
#    direct :  x=sidestreamed_f(fparm)
#  indirect :  x=L(sidestreamed_f,fparm,lparms)

# Chaque fois que cela est appelé, il crée une nouvelle instance de la fonction enveloppée
    def sidestream_wrapped_func(parms):
        print("Je vais exécuter : ", myfunc.__name__)
        ultimate_result=myfunc(parms)
        # La file d'attente a été créée lorsque la fonction enveloppée est créée
        sidestream_wrapped_func.sidestreamoutq.put(ultimate_result)
        sidestream_wrapped_func.mrrv=ultimate_result
        return 42  
    sidestream_wrapped_func.sidestreamoutq=queue.Queue()
    print(["sidestream_wrapper_func = ",sidestream_wrapped_func, " ; with queue at = ",id(sidestream_wrapped_func.sidestreamoutq)])
    return sidestream_wrapped_func
    
def test_create_and_use_sidestream_wrapper_func():
    print(["use f directly:", f("use f directly:")])
    # sidestream f
    sidestreamed_f=create_sidestream_wrapper_func(f) #convient pour une utilisation que f soit dans une bibliothèque ou en ligne ici, dans les deux cas.
    sidestreamed_f2=create_sidestream_wrapper_func(f) # crée une autre fonction sidestream avec son propre attribut de résultat et sa file d'attente
    print(["defined the sidestreamed f", sidestreamed_f])
    print(["defined the sidestreamed f2", sidestreamed_f2])
    print(["use sidestreamed_f directly:", sidestreamed_f("use sidestreamed_f directly:")])
    print(["use sidestreamed_f2 directly:", sidestreamed_f2("use sidestreamed_f2 directly:")])
    print(["wrapped f Attribute:", sidestreamed_f.mrrv])
    print(["wrapped f2 Attribute:", sidestreamed_f2.mrrv])
    print(["wrapped f Q entry:", sidestreamed_f.sidestreamoutq.get()])
    print(["wrapped f2 Q entry:", sidestreamed_f2.sidestreamoutq.get()])
    
    
test_create_and_use_sidestream_wrapper_func()
quit()

""" la sortie devrait être quelque chose comme ceci, sauf que les adresses seront différentes.
['use f directly:', ['f returns', 'use f directly:']]
['sidestream_wrapper_func = ', <function create_sidestream_wrapper_func.<locals>.sidestream_wrapped_func at 0x7efffca3edd0>, ' ; with queue at = ', 139637920186032]
['sidestream_wrapper_func = ', <function create_sidestream_wrapper_func.<locals>.sidestream_wrapped_func at 0x7efffca3ee60>, ' ; with queue at = ', 139637920175280]
['defined the sidestreamed f', <function create_sidestream_wrapper_func.<locals>.sidestream_wrapped_func at 0x7efffca3edd0>]
['defined the sidestreamed f2', <function create_sidestream_wrapper_func.<locals>.sidestream_wrapped_func at 0x7efffca3ee60>]
Je vais exécuter :  f
['use sidestreamed_f directly:', 42]
Je vais exécuter :  f
['use sidestreamed_f2 directly:', 42]
['wrapped f Attribute:', ['f returns', 'use sidestreamed_f directly:']]
['wrapped f2 Attribute:', ['f returns', 'use sidestreamed_f2 directly:']]
['wrapped f Q entry:', ['f returns', 'use sidestreamed_f directly:']]
['wrapped f2 Q entry:', ['f returns', 'use sidestreamed_f2 directly:']]

"""
```

La fonction génératrice et les fonctions générées ont quelques instructions print que vous voudrez commenter après avoir utilisé et testé le code. 

Il est important de remarquer dans la sortie d'exemple que les adresses des fonctions `sidestreamed_f` et `sidestreamed_f2` et de leurs objets de file d'attente sont différentes.

De même, les attributs `mrrv` sont également à des adresses différentes :

`sidestreamed_f ... at 0x7efffca3edd0>, ' ; with queue at = ', 139637920186032]`

`sidestreamed_f2 ... at 0x7efffca3ee60>, ' ; with queue at = ', 139637920175280]`

Cela renforce comment ces deux enveloppes sont des objets complètement séparés.

### Conseils pour sélectionner la solution à utiliser

Ce tutoriel vous a montré plusieurs solutions et variations. 

Laquelle ou lesquelles devriez-vous utiliser ? 

Quels sont les critères de considération, de sélection et les implications ? 

Cette section fournit un mélange de principes généraux de génie logiciel et des spécificités pour le sujet de cet article. 

Tout d'abord, éliminez les solutions à ne pas utiliser du tout. 

N'utilisez pas la solution de variable globale. Elle est dépréciée. 

Jusqu'à ce que vous compreniez la Solution #6 : Enveloppe décorateur Python, ne l'utilisez pas. 

Si vous ne pouvez pas améliorer le code dans la fonction de bas niveau, alors utilisez une enveloppe. 

L'enveloppe pourrait être basée sur la Solution #5 : Enveloppe Python simple pour chaque fonction spécifique, ou la Solution #6 : Enveloppe décorateur Python pour générer l'enveloppe.

Utilisez la solution d'attribut partout où c'est possible. La solution d'attribut fournit une très bonne pratique de codage générale, appelée [mémoisation](https://www.freecodecamp.org/news/memoization-in-javascript-and-react/). 

Je suggère d'ajouter la mémoisation des résultats de fonction aux normes de codage Python de votre groupe pour toutes les fonctions partout. 

Peut-être utiliser une convention de nommage d'attribut différente. J'utilise `.mrrv`, qui signifie "valeur de résultat la plus récente". 

Par exemple, une fonction `m` serait quelque chose comme :

```python
def m():
  result=[1,2,3]
  m.mrrv=result
  return m.mrrv.copy()
```

Ensuite, dans votre code ailleurs, utilisez et réutilisez le résultat mémoisé, comme avec `print([sum(m())," = sum(",m.mrrv,")"])` qui produit `[6, ' = sum(', [1, 2, 3], ')']`. 

Cependant, soyez conscient de l'ordre d'évaluation de Python et du court-circuit des expressions logiques, pour vous assurer que la fonction est appelée avant d'essayer d'utiliser son `mrrv`.

En d'autres termes, définissez toujours un attribut de fonction sur la valeur retournée, puis retournez une copie de celui-ci, même si vous n'avez pas le problème de contournement de bibliothèque de ce tutoriel.

Un appel à une fonction de bibliothèque invoque-t-il la fonction de bas niveau de nombreuses fois et le programme de haut niveau a-t-il besoin du résultat de chacune ? 

Si c'est le cas, alors utilisez une solution basée sur une file d'attente plutôt que ou en plus de la solution d'attribut.

Votre problème de contournement de bibliothèque s'applique-t-il à de nombreuses fonctions de bas niveau qui doivent passer plusieurs résultats via une ou plusieurs files d'attente pour chaque fonction ? 

Si vous comprenez la Solution #6 : Enveloppe décorateur Python, utilisez-la. Sinon, utilisez la Solution #4 : Files d'attente.

Est-il préférable d'utiliser la solution la plus simple pour chaque besoin dans le projet, ou aussi peu de ces différentes solutions que possible dans l'ensemble du projet ? 

Je recommande la méthode aussi-peu-que-possible. Pour moi, cela signifie utiliser la Solution #1 : Attribut de fonction et la Solution #6 : Enveloppe décorateur Python.

### À quel point ces solutions sont-elles bonnes ?

Vous vous demandez peut-être si ces solutions recommandées sont conformes aux principes directeurs en haut de ce tutoriel ?

Voici quelques points à considérer :

* Conflits : nous avons évité les conflits de nommage et les interférences en utilisant une convention de nommage.
* Optionnalité : Les deux alternatives de solution recommandées, attribut et file d'attente, ne nécessitent pas de code supplémentaire dans la fonction de haut niveau si elle n'a pas besoin des résultats étendus de la fonction de bas niveau. Les solutions de file d'attente pourraient planter si les résultats étendus s'accumulent indéfiniment sans être vidés.
* Couplage : Plusieurs solutions ont éliminé le couplage explicite du code source avec des noms codés en dur et une convention de nommage. Dans une solution, l'appelant de haut niveau a d'abord défini une ou plusieurs files d'attente de destination des résultats. Ensuite, l'appelant a passé une référence d'objet à une file d'attente dans les paramètres passés à travers l'intermédiaire à la fonction de bas niveau.   

## Résumé

Comme vous l'avez appris dans ce tutoriel, il est faisable de passer des résultats d'une fonction de bas niveau à récupérer par une fonction de haut niveau ou un programme principal. 

Cela vous permet de contourner tout intermédiaire en utilisant un flux secondaire hors bande. 

Plusieurs solutions sont présentées ici. Utilisez-en aussi peu que possible dans votre projet ou vos projets. 

Toutes ces solutions ont utilisé Python procédural. Elles sont également applicables à Python orienté objet avec des classes. 

Utilisez un attribut dans la fonction de bas niveau ou utilisez une file d'attente. 

N'utilisez pas de variable globale.

Crédits d'illustration : [Scott's Great Snake Blockading the Confederacy](https://www.loc.gov/resource/g3701s.cw0011000?r=0.019,0.021,0.937,0.585,0). (c) 1861