---
title: Comment parser du XML en Python sans utiliser de bibliothèques externes
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2025-11-12T20:29:56.941Z'
originalURL: https://freecodecamp.org/news/how-to-parse-xml-in-python-without-using-external-libraries
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762979370762/de792485-6d8a-42aa-adcc-66bd797c207c.png
tags:
- name: Python
  slug: python
seo_title: Comment parser du XML en Python sans utiliser de bibliothèques externes
seo_desc: In software development, you’ll run into XML (Extensible Markup Language)
  when working with configuration files, API responses, data exports, and more. While
  there are powerful third-party libraries for parsing XML, Python's standard library
  already ...
---

Dans le développement de logiciels, vous rencontrerez du XML (Extensible Markup Language) lors de l'utilisation de fichiers de configuration, de réponses d'API, d'exports de données, et plus encore. Bien qu'il existe de puissantes bibliothèques tierces pour analyser le XML, la bibliothèque standard de Python inclut déjà tout ce dont vous avez besoin.

Dans ce tutoriel, vous apprendrez à parser du XML en utilisant le module intégré de Python [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html). Aucune installation via pip n'est requise.

🔗 [**Vous pouvez trouver le code sur GitHub**](https://github.com/balapriyac/python-basics/tree/main/parse-xml).

## Prérequis

Pour suivre ce tutoriel, vous devez disposer de :

* Python 3.7 ou une version ultérieure installée sur votre système
    
* Une compréhension de base de la syntaxe et des structures de données Python
    
* Une familiarité avec les concepts de programmation de base tels que les boucles et les conditions
    
* Un éditeur de texte ou un IDE pour écrire du code Python
    

Aucune bibliothèque externe n'est requise car nous utiliserons le module intégré `xml.etree.ElementTree` de Python.

## Table des matières

1. [Comment lire une chaîne XML](#heading-comment-lire-une-chaine-xml)
    
2. [Comment lire un fichier XML](#heading-comment-lire-un-fichier-xml)
    
3. [Comment trouver des éléments dans un arbre XML](#heading-comment-trouver-des-elements-dans-un-arbre-xml)
    
4. [Comment extraire du texte et des attributs du XML](#heading-comment-extraire-du-texte-et-des-attributs-du-xml)
    
5. [Comment construire un parseur XML simple](#heading-comment-construire-un-parseur-xml-simple)
    
6. [Comment gérer les données manquantes](#heading-comment-gerer-les-donnees-manquantes)
    

## Comment lire une chaîne XML

Commençons simplement. Nous allons parser du XML directement à partir d'une chaîne de caractères pour comprendre les concepts fondamentaux.

```python
import xml.etree.ElementTree as ET

xml_string = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <price currency="USD">29.99</price>
    </product>
</catalog>
"""

root = ET.fromstring(xml_string)
print(f"Root tag: {root.tag}")
print(f"Root attributes: {root.attrib}")
```

Comment cela fonctionne :

* Nous importons `xml.etree.ElementTree` et lui donnons l'alias `ET` (c'est la convention)
    
* `ET.fromstring()` analyse la chaîne XML et renvoie l'élément racine (`root`)
    
* Chaque élément possède une propriété `.tag` (le nom de l'élément) et un dictionnaire `.attrib` (ses attributs)
    
* L'objet `root` représente l'élément `<catalog>` dans notre XML
    

Pour l'exemple ci-dessus, vous verrez la sortie suivante :

```plaintext
Root tag: catalog
Root attributes: {}
```

Ici, `root.attrib` est vide car l'élément racine `<catalog>` dans la chaîne `xml_string` fournie n'a aucun attribut défini. Les attributs sont des paires clé-valeur à l'intérieur de la balise d'ouverture d'un élément XML, comme `id="101"` ou `currency="USD"` dans les éléments `<product>` et `<price>`. Comme `<catalog>` n'a qu'une balise et aucune information supplémentaire dans sa balise d'ouverture, son dictionnaire d'attributs est vide.

## Comment lire un fichier XML

Dans les applications réelles, vous lirez généralement le XML à partir de fichiers. Supposons que vous ayez un fichier [products.xml](https://github.com/balapriyac/python-basics/blob/main/parse-xml/products.xml). Voici comment vous pouvez lire à partir du fichier XML :

```python
# Analyser un fichier XML
tree = ET.parse('products.xml')
root = tree.getroot()

print(f"Root element: {root.tag}")
```

Avant de passer à l'exécution et à la vérification de la sortie, notons les différences entre la lecture de chaînes XML et de fichiers :

* `ET.parse()` lit à partir d'un fichier et renvoie un objet `ElementTree`
    
* Nous appelons `.getroot()` pour obtenir l'élément racine
    
* Utilisez `ET.parse()` pour les fichiers, `ET.fromstring()` pour les chaînes
    

L'exécution du code ci-dessus devrait vous donner :

```plaintext
Root element: catalog
```

## Comment trouver des éléments dans un arbre XML

`ElementTree` vous offre trois manières principales de rechercher des éléments. Il est important de comprendre quand utiliser chacune d'elles.

```python
import xml.etree.ElementTree as ET

xml_data = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <categories>
            <category>Electronics</category>
            <category>Accessories</category>
        </categories>
    </product>
    <product id="102">
        <name>USB Mouse</name>
        <categories>
            <category>Electronics</category>
        </categories>
    </product>
</catalog>
"""

root = ET.fromstring(xml_data)

# Méthode 1 : find() - renvoie le PREMIER élément correspondant
first_product = root.find('product')
print(f"First product ID: {first_product.get('id')}")

# Méthode 2 : findall() - renvoie TOUS les enfants directs qui correspondent
all_products = root.findall('product')
print(f"Total products: {len(all_products)}")

# Méthode 3 : iter() - trouve de manière récursive TOUS les éléments correspondants
all_categories = root.iter('category')
category_list = [cat.text for cat in all_categories]
print(f"All categories: {category_list}")
```

Voyons maintenant comment fonctionnent ces trois méthodes :

* `find()` s'arrête à la première correspondance. Utilisez-la lorsque vous n'avez besoin que d'un seul élément.
    
* `findall()` ne recherche que parmi les enfants directs (un seul niveau de profondeur). Utilisez-la pour les éléments enfants immédiats.
    
* `iter()` effectue une recherche récursive dans tout l'arbre. Utilisez-la lorsque les éléments peuvent être imbriqués n'importe où.
    

C'est important : `findall('category')` sur la racine ne trouvera rien car `<category>` n'est pas un enfant direct de `<catalog>`. Mais `iter('category')` trouvera toutes les catégories, peu importe leur niveau d'imbrication. Ainsi, lorsque vous exécutez le code ci-dessus, vous obtiendrez :

```plaintext
First product ID: 101
Total products: 2
All categories: ['Electronics', 'Accessories', 'Electronics']
```

## Comment extraire du texte et des attributs du XML

Maintenant, extrayons les données réelles de notre XML. C'est ici que vous transformez le XML structuré en données Python exploitables.

```python
xml_data = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <price currency="USD">29.99</price>
        <stock>45</stock>
    </product>
</catalog>
"""

root = ET.fromstring(xml_data)
product = root.find('product')

# Obtenir le contenu textuel de l'élément
product_name = product.find('name').text
price_text = product.find('price').text
stock_text = product.find('stock').text

# Obtenir les attributs (deux manières)
product_id = product.get('id')  # Méthode 1 : .get()
product_id_alt = product.attrib['id']  # Méthode 2 : dictionnaire .attrib

# Obtenir des attributs imbriqués
price_element = product.find('price')
currency = price_element.get('currency')

print(f"Product: {product_name}")
print(f"ID: {product_id}")
print(f"Price: {currency} {price_text}")
print(f"Stock: {stock_text}")
```

Ceci affiche :

```plaintext
Product: Wireless Keyboard
ID: 101
Price: USD 29.99
Stock: 45
```

Ce qui se passe ici :

* `.text` récupère le contenu textuel entre les balises d'ouverture et de fermeture
    
* `.get('nom_attribut')` récupère un attribut de manière sécurisée (renvoie `None` s'il est manquant)
    
* `.attrib['nom_attribut']` accède directement au dictionnaire d'attributs (lève une `KeyError` s'il est manquant)
    
* Utilisez `.get()` lorsqu'un attribut peut être optionnel, utilisez `.attrib[]` lorsqu'il est requis
    

## Comment construire un parseur XML simple

Mettons tout cela en pratique avec un exemple concret. Nous allons parser le catalogue complet de produits et le convertir en une liste Python de dictionnaires.

```python
def parse_product_catalog(xml_file):
    """Analyse un catalogue de produits XML et renvoie une liste de dictionnaires de produits."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    products = []

    for product_element in root.findall('product'):
        # Extraire les données du produit
        product = {
            'id': product_element.get('id'),
            'name': product_element.find('name').text,
            'price': float(product_element.find('price').text),
            'currency': product_element.find('price').get('currency'),
            'stock': int(product_element.find('stock').text),
            'categories': []
        }

        # Extraire les catégories (éléments imbriqués)
        categories_element = product_element.find('categories')
        if categories_element is not None:
            for category in categories_element.findall('category'):
                product['categories'].append(category.text)

        products.append(product)

    return products
```

Analyse de ce parseur :

* Nous itérons sur tous les éléments `<product>` en utilisant `findall()`
    
* Pour chaque produit, nous extrayons le texte et les attributs dans un dictionnaire. Nous convertissons les chaînes numériques en types appropriés (`float` pour le prix, `int` pour le stock)
    
* Pour les catégories imbriquées, nous vérifions d'abord si l'élément `<categories>` existe. Ensuite, nous itérons sur les éléments enfants `<category>` et collectons leur texte
    

Le résultat est une structure de données Python propre que vous pouvez facilement manipuler. Vous pouvez maintenant utiliser le parseur ainsi :

```python
products = parse_product_catalog('products.xml')

for product in products:
    print(f"\nProduct: {product['name']}")
    print(f"  ID: {product['id']}")
    print(f"  Price: {product['currency']} {product['price']}")
    print(f"  Stock: {product['stock']}")
    print(f"  Categories: {', '.join(product['categories'])}")
```

Sortie :

```plaintext
Product: Wireless Keyboard
  ID: 101
  Price: USD 29.99
  Stock: 45
  Categories: Electronics, Accessories

Product: USB Mouse
  ID: 102
  Price: USD 15.99
  Stock: 120
  Categories: Electronics
```

## Comment gérer les données manquantes

Le XML en conditions réelles est souvent désordonné (pas de surprise ici !). Des éléments peuvent être manquants, le texte peut être vide ou des attributs peuvent ne pas exister. Voici comment gérer cela proprement.

```python
xml_data = """
<catalog>
    <product id="101">
        <name>Wireless Keyboard</name>
        <price currency="USD">29.99</price>
    </product>
    <product id="102">
        <name>USB Mouse</name>
        <!-- Élément price manquant -->
    </product>
</catalog>
"""

root = ET.fromstring(xml_data)

for product in root.findall('product'):
    name = product.find('name').text
    
    # Manière sécurisée de gérer des éléments potentiellement manquants
    price_element = product.find('price')
    if price_element is not None:
        price = float(price_element.text)
        currency = price_element.get('currency', 'USD')  # Valeur par défaut
        print(f"{name}: {currency} {price}")
    else:
        print(f"{name}: Price not available")
```

Ici, nous gérons les données manquantes potentielles en :

1. Utilisant `product.find('price')` pour rechercher l'élément `<price>` dans l'élément `<product>` actuel.
    
2. Vérifiant si le résultat de `find()` est `None`. Si un élément n'est pas trouvé, `find()` renvoie `None`.
    
3. Utilisant une condition `if price_element is not None:` pour ne tenter d'accéder au texte `(price_element.text)` et aux attributs `(price_element.get('currency', 'USD'))` de l'élément `<price>` que s'il a réellement été trouvé.
    
4. Ajoutant un bloc `else` pour gérer le cas où l'élément `<price>` est manquant, en affichant "Price not available".
    

Cette approche évite les erreurs qui se produiraient si vous essayiez d'accéder à `.text` ou `.get()` sur un objet `None`. Pour l'extrait de code ci-dessus, vous obtiendrez :

```plaintext
Wireless Keyboard: USD 29.99
USB Mouse: Price not available
```

Voici quelques stratégies supplémentaires de gestion d'erreurs :

* Vérifiez toujours si `find()` renvoie `None` avant d'accéder à `.text` ou `.get()`
    
* Utilisez `.get('attr', 'default')` pour fournir des valeurs par défaut aux attributs manquants
    
* Envisagez d'envelopper l'analyse dans des blocs try-except pour le code en production
    
* Validez vos données après l'analyse plutôt que de supposer que la structure XML est correcte
    

## Conclusion

Vous savez maintenant comment parser du XML en Python sans installer de bibliothèques externes. Vous avez appris :

* Comment lire du XML à partir de chaînes et de fichiers
    
* La différence entre `find()`, `findall()` et `iter()`
    
* Comment extraire le contenu textuel et les attributs en toute sécurité
    
* Comment gérer les éléments imbriqués et les données manquantes
    

Le module `xml.etree.ElementTree` fonctionne suffisamment bien pour la plupart des besoins d'analyse XML, et il est toujours disponible dans la bibliothèque standard de Python.

Pour une navigation et une sélection XML plus avancées, vous pouvez explorer les [expressions XPath](https://www.w3schools.com/xml/xpath_syntax.asp). XPath fonctionne bien pour sélectionner des nœuds dans un document XML et peut être très utile pour les structures complexes. Nous aborderons cela dans un autre tutoriel.

D'ici là, bon parsing !