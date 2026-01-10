---
title: Comment fonctionnent les HashMaps en Java - Mécanismes internes expliqués
subtitle: ''
author: Anjan Baradwaj
co_authors: []
series: null
date: '2024-08-09T20:10:23.759Z'
originalURL: https://freecodecamp.org/news/how-java-hashmaps-work-internal-mechanics-explained
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/Or_Fa550XaQ/upload/f4d40f1c8e94855d53776a3bb6179673.jpeg
tags:
- name: Java
  slug: java
- name: hashmap
  slug: hashmap
- name: Collection Framework
  slug: collection-framework
seo_title: Comment fonctionnent les HashMaps en Java - Mécanismes internes expliqués
seo_desc: 'A HashMap is one of the most commonly used data structures in Java, and
  it''s known for its efficiency. Data in a HashMap is stored in the form of key-value
  pairs.

  In this article, I will introduce you to HashMaps in Java. We will explore the common
  o...'
---

Un `HashMap` est l'une des structures de données les plus couramment utilisées en Java, et il est connu pour son efficacité. Les données dans un `HashMap` sont stockées sous la forme de paires clé-valeur.

Dans cet article, je vais vous présenter les `HashMap` en Java. Nous explorerons les opérations courantes de `HashMap` puis nous plongerons dans son fonctionnement interne. Vous comprendrez la fonction de hachage et comment le calcul d'index se déroule. Enfin, nous examinerons les complexités temporelles des opérations et aborderons le comportement dans un environnement concurrent.

## **Qu'est-ce qu'un** `HashMap` **en Java ?**

Un `HashMap` implémente l'interface `Map`, qui fait partie du framework de collection Java. Il est basé sur le concept de hachage.

Le hachage est une technique qui transforme une entrée de taille arbitraire en une sortie de taille fixe en utilisant une fonction de hachage. La sortie générée est appelée code de hachage et est représentée par une valeur entière en Java. Les codes de hachage sont utilisés pour des opérations de recherche et de stockage efficaces dans un `HashMap`.

## **Opérations courantes**

Comme nous l'avons discuté ci-dessus, les données dans un `HashMap` sont stockées sous la forme de paires clé-valeur. La clé est un identifiant unique, et chaque clé est associée à une valeur.

Voici quelques opérations courantes supportées par un `HashMap`. Comprenons ce que font ces méthodes avec quelques exemples de code simples :

### **Insertion**

* Cette méthode insère une nouvelle paire clé-valeur dans le `HashMap`.
  
* L'ordre d'insertion des paires clé-valeur n'est pas maintenu.
  
* Lors de l'insertion, si une clé est déjà présente, la valeur existante sera remplacée par la nouvelle valeur qui est passée.
  
* Vous pouvez insérer seulement une clé null dans le `HashMap`, mais vous pouvez avoir plusieurs valeurs null.
  

La signature de la méthode pour cette opération est donnée ci-dessous, suivie d'un exemple :

```java
public V put(K key, V value)
```

```java
Map<String, Integer> map = new HashMap<>();
map.put("apple", 1);
map.put("banana", 2);
```

Dans le code ci-dessus, nous avons un exemple de HashMap où nous ajoutons une clé de type String et une valeur de type Integer.

### **Récupération :**

* Récupère la valeur associée à une clé donnée.
  
* Retourne `null` si la clé n'existe pas dans le `HashMap`.
  

La signature de la méthode pour cette opération est donnée ci-dessous, suivie d'un exemple :

```java
public V get(Object key)
```

```java
Integer value = map.get("apple"); // retourne 1
```

Dans le code ci-dessus, nous récupérons la valeur associée à la clé `apple`.

D'autres opérations courantes incluent :

* `remove` : Supprime la paire clé-valeur pour la clé spécifiée. Il retourne `null` si la clé n'est pas trouvée.
  
* `containsKey` : Vérifie si une clé spécifique est présente dans le `HashMap`.
  
* `containsValue` : Vérifie si la valeur spécifiée est présente dans le `HashMap`.
  

## **Structure interne d'un** `HashMap`

En interne, un `HashMap` utilise un tableau de buckets ou de bacs. Chaque bucket est une liste chaînée de type `Node`, qui est utilisée pour représenter la paire clé-valeur du `HashMap`.

```java
static class Node<K, V> {
    final int hash;
    final K key;
    V value;
    Node<K, V> next;
    
    Node(int hash, K key, V value, Node<K, V> next) {
        this.hash = hash;
        this.key = key;
        this.value = value;
        this.next = next;
    }
}
```

Ci-dessus, vous pouvez voir la structure de la classe `Node` qui est utilisée pour stocker les paires clé-valeur du `HashMap`.

La classe `Node` a les champs suivants :

* `hash` : Fait référence au `hashCode` de la clé.
  
* `key` : Fait référence à la clé de la paire clé-valeur.
  
* `value` : Fait référence à la valeur associée à la clé.
  
* `next` : Agit comme une référence au nœud suivant.
  

Le `HashMap` est fondamentalement basé sur une implémentation de table de hachage, et ses performances dépendent de deux paramètres clés : la capacité initiale et le facteur de charge. La [documentation originale](https://docs.oracle.com/javase/8/docs/api/java/util/Hashtable.html) de la classe Hash table définit ces deux paramètres comme suit :

* La capacité est le nombre de buckets dans la table de hachage, et la capacité initiale est simplement la capacité au moment où la table de hachage est créée.
  
* Le facteur de charge est une mesure de la quantité de remplissage autorisée dans la table de hachage avant que sa capacité ne soit automatiquement augmentée.
  

Essayons maintenant de comprendre comment les opérations de base, `put` et `get`, fonctionnent dans un `HashMap`.

### **Fonction de hachage**

Lors de l'insertion (`put`) d'une paire clé-valeur, le `HashMap` calcule d'abord le code de hachage de la clé. La fonction de hachage calcule ensuite un entier pour la clé. Les classes peuvent utiliser la méthode `hashCode` de la classe `Object` ou remplacer cette méthode et fournir leur propre implémentation. (Lisez à propos du contrat de code de hachage [ici](https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html#hashCode())). Le code de hachage est ensuite XORé (OU exclusif) avec ses 16 bits supérieurs (h >>> 16) pour obtenir une distribution plus uniforme.

XOR est une opération bit à bit qui compare deux bits, résultant en 1 si les bits sont différents et 0 s'ils sont identiques. Dans ce contexte, effectuer une opération XOR bit à bit entre le code de hachage et ses 16 bits supérieurs (obtenus en utilisant l'opérateur de décalage à droite non signé `>>>`) aide à mélanger les bits, conduisant à un code de hachage plus uniformément distribué.

```java
static final int hash(Object key) {
	int h;
	return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
```

Ci-dessus, vous pouvez voir la méthode de hachage statique de la classe `HashMap`.

L'idée est d'avoir un code de hachage unique pour chaque clé, mais la fonction de hachage pourrait produire le même code de hachage pour différentes clés. Cela conduit à une situation connue sous le nom de collision. Nous verrons comment gérer les collisions dans la section suivante.

### **Calcul de l'index**

Une fois le code de hachage pour une clé généré, le `HashMap` calcule un index dans le tableau de buckets pour déterminer où la paire clé-valeur sera stockée. Cela se fait en utilisant une opération ET bit à bit, qui est un moyen efficace de calculer le modulo lorsque la longueur du tableau est une puissance de deux.

```java
int index = (n - 1) & hash;
```

Ici, nous calculons l'index où n est la longueur du tableau de buckets.

Une fois l'index calculé, la clé est ensuite stockée à cet index dans le tableau de buckets. Cependant, si plusieurs clés finissent par avoir le même index, cela provoque une collision. Dans un tel scénario, le `HashMap` le gère de l'une des deux manières suivantes :

* Chaînage/Liaison : Chaque bucket dans le tableau est une liste chaînée de nœuds. Si une clé existe déjà à un index particulier et qu'une autre clé est hachée au même index, elle est ajoutée à la liste.
  
* Arborescence : Si le nombre de nœuds dépasse un certain seuil, la liste chaînée est convertie en un arbre (ceci a été introduit dans Java 8).
  

```java
static final int TREEIFY_THRESHOLD = 8;
```

C'est le seuil qui détermine l'arborescence.

Par conséquent, il est essentiel d'avoir une bonne fonction de hachage qui distribue uniformément les clés dans les buckets et minimise les chances de collisions.

Les opérations de récupération (`get`) et de suppression (`remove`) fonctionnent de manière similaire à l'opération d'insertion (`put`). Voici comment :

* Récupération (`get`) : Calcule le code de hachage en utilisant la fonction de hachage -> calcule l'index en utilisant le code de hachage -> parcourt la liste chaînée ou l'arbre pour trouver le nœud avec la clé correspondante.
  
* Suppression (`remove`) : Calcule le code de hachage en utilisant la fonction de hachage -> calcule l'index en utilisant le code de hachage -> supprime le nœud de la liste chaînée ou de l'arbre.
  

### **Complexité temporelle**

Les opérations de base d'un `HashMap`, telles que `put`, `get` et `remove`, offrent généralement des performances en temps constant de O(1), en supposant que les clés sont uniformément distribuées. Dans les cas où la distribution des clés est mauvaise et où de nombreuses collisions se produisent, ces opérations peuvent se dégrader en une complexité temporelle linéaire de O(n).

Avec l'arborescence, où de longues chaînes de collisions sont converties en arbres équilibrés, les opérations de recherche peuvent s'améliorer pour atteindre une complexité temporelle logarithmique plus efficace de O(log n).

### **Synchronisation**

L'implémentation de `HashMap` n'est pas synchronisée. Si plusieurs threads accèdent à une instance de HashMap simultanément et parcourent la map, et si l'un des threads effectue une modification structurelle (comme l'ajout ou la suppression d'une association clé-valeur) sur la map, cela conduit à une `ConcurrentModificationException`.

Pour éviter cela, vous pouvez créer une instance thread-safe en utilisant la méthode `Collections.synchronizedMap`.

## **Conclusion**

En résumé, comprendre le fonctionnement interne d'un `HashMap` est crucial pour les développeurs afin de prendre des décisions éclairées. Savoir comment une clé est mappée, comment les collisions se produisent et comment elles peuvent être évitées vous aide à utiliser le `HashMap` de manière efficace et efficace.