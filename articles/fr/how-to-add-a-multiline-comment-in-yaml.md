---
title: Commentaires YAML – Comment ajouter un commentaire multiline dans YAML
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-01T18:28:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-multiline-comment-in-yaml
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/vipul-jha-a4X1cdC1QAc-unsplash.jpg
tags:
- name: data
  slug: data
- name: YAML
  slug: yaml
seo_title: Commentaires YAML – Comment ajouter un commentaire multiline dans YAML
seo_desc: 'You can use a YAML file to store data in a format that can be easily read
  and understood by humans. It is a data serialization language that is often used
  for configuration files and data transfer between applications.

  YAML is similar to XML and JSON...'
---

Vous pouvez utiliser un fichier YAML pour stocker des données dans un format qui peut être facilement lu et compris par les humains. C'est un [langage de sérialisation de données](https://www.freecodecamp.org/news/what-is-yaml-the-yml-file-format/#intro:~:text=Serialization%20is%20a%20process%20where%20one%20application%20or%20service%20that%20has%20different%20data%20structures%20and%20is%20written%20in%20a%20different%20set%20of%20technologies%20can%20transfer%20data%20to%20another%20application%20using%20a%20standard%20format.) qui est souvent utilisé pour les fichiers de configuration et le transfert de données entre applications.

YAML est similaire à XML et JSON car ils peuvent tous être utilisés pour stocker des données dans différents formats. La principale différence réside dans leur syntaxe.

Voici à quoi ressemble le format XML :

```xml
<user>
  <name>John Doe</name>
  <phone>00223344</phone>
  <age>80</age>
</user>
```

Voici à quoi ressemble le format JSON :

```json
{
  "user": {
    "name": "John Doe",
    "phone": "00223344",
    "age": 80
  }
}

```

Voici à quoi ressemble le format YAML :

```yaml
user:
  name: John Doe
  phone: 00223344
  age: 80

```

Chacun des formats ci-dessus est utilisé pour stocker des données sur le nom, le numéro de téléphone et l'âge d'un utilisateur.

Vous pouvez en savoir plus sur les fonctionnalités, les règles de base et la syntaxe de YAML, ainsi que ses différences avec JSON et XML dans [cet article](https://www.freecodecamp.org/news/what-is-yaml-the-yml-file-format/).

Dans cet article, vous apprendrez à utiliser les commentaires multiline dans YAML.

## Comment ajouter un commentaire multiline dans YAML

Vous pouvez utiliser des commentaires pour diverses raisons, comme documenter votre code, collaborer avec d'autres personnes, empêcher un bloc de code de s'exécuter, etc.

Vous pouvez utiliser le symbole `#` pour créer des commentaires dans un fichier YAML. C'est-à-dire :

```yaml
# L'objet ci-dessous représente un utilisateur

user:
  name: John Doe
  email: john.doe@example.com
  age: 30

```

Contrairement à certains autres langages, YAML n'a pas de format différent pour créer des commentaires de bloc ou multiline.

Vous devrez utiliser le symbole `#` sur chaque ligne que le commentaire couvre. Voici un exemple :

```yaml
# L'objet ci-dessous est un exemple qui représente un 
# nom d'utilisateur, un numéro de téléphone et un âge

user:
  name: John Doe
  email: john.doe@example.com
  age: 30

```

Si vous retirez le symbole `#` sur la deuxième ligne, le texte peut encore apparaître comme un commentaire, mais l'analyseur YAML peut l'interpréter comme du texte brut, ce qui peut entraîner une erreur.

Pour être sûr, utilisez le symbole `#` au début de chaque ligne de commentaire.

## Résumé

Dans cet article, nous avons parlé de YAML. Il est principalement utilisé pour stocker et transférer des données.

Nous avons vu comment créer des commentaires en ligne et multiline. Dans YAML, le symbole `#` est utilisé pour les commentaires en ligne et multiline.

Bon codage ! Consultez [mon blog](https://ihechikara.com/) pour plus de contenu sur la programmation.