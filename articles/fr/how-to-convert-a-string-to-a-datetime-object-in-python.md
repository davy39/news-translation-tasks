---
title: Comment convertir une chaîne de caractères en objet DateTime en Python
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-07-19T20:40:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-a-datetime-object-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-christina-morillo-1181359--3-.jpg
tags:
- name: Python
  slug: python
seo_title: Comment convertir une chaîne de caractères en objet DateTime en Python
seo_desc: 'When you get dates from raw data, they''re typically in the form of string
  objects. But in this form, you can''t access the date''s properties like the year,
  month, and so on.

  The solution to this problem is to parse (or convert) the string object into ...'
---

Lorsque vous obtenez des dates à partir de données brutes, elles sont généralement sous la forme d'objets chaîne de caractères. Mais sous cette forme, vous ne pouvez pas accéder aux propriétés de la date comme l'année, le mois, etc.

La solution à ce problème est de parser (ou convertir) l'objet chaîne de caractères en un objet datetime afin que Python puisse le reconnaître comme une date. Ensuite, vous pouvez extraire tous les attributs sous-jacents que vous souhaitez obtenir.

Ce tutoriel vous apprendra à convertir une chaîne de caractères en objet datetime en Python. Sans plus attendre, commençons.

# Codes de format DateTime

Avant d'apprendre à convertir des chaînes de caractères en dates, vous devez comprendre les codes de formatage des objets datetime en Python.

Ces prérequis seront utiles chaque fois que vous devrez convertir une chaîne de caractères en date. Nous examinerons certains des codes de formatage les plus courants avec lesquels vous travaillerez chaque fois que vous souhaiterez convertir une chaîne de caractères en date.

Voici quelques-uns des plus courants :

* %Y — Cela est utilisé pour représenter l'année et elle varie de 0001 à 9999
    
* %m — Cela est utilisé pour représenter le mois de l'année et il varie de 01 à 12.
    
* %d — Cela est utilisé pour représenter les jours du mois et varie de 01 à 31.
    
* %H — Cela est utilisé pour représenter les heures du jour dans un format 24 heures et varie de 00 à 23.
    
* %I — Cela est utilisé pour représenter les heures du jour dans un format 12 heures et varie de 01 à 12.
    
* %M — Cela est utilisé pour représenter les minutes dans une heure et varie de 00 à 59.
    
* %S — Cela est utilisé pour représenter les secondes dans une minute et varie de 00 à 59 également.
    

Nous nous arrêterons ici pour les codes de format de date, mais il en existe beaucoup d'autres dans la documentation Python. Vous pouvez cliquer [ici](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) pour en voir plus.

# Comment convertir une chaîne de caractères en objet DateTime

Notez que la première chose à considérer lors de la conversion d'une chaîne de caractères en date est de s'assurer que la chaîne de caractères est dans le bon format.

Pour convertir une chaîne de caractères en date, elle doit satisfaire les conditions suivantes.

* Tout d'abord, chaque élément de la chaîne de caractères doit être séparé des autres soit par un espace, une lettre ou un symbole tel que / & , % # - et ainsi de suite.
    
* L'élément de la chaîne de caractères à parser en année, mois ou jour doit être de la même longueur que le code de format. L'élément de la chaîne de caractères ne doit pas dépasser la plage du code de format. Par exemple, le code %Y nécessite 4 chiffres pour être passé comme année et sa plage est 0001 – 9999 (donc 09, par exemple, ne fonctionnerait pas – vous avez besoin de 2009).
    

Regardons quelques exemples de conversions de chaîne de caractères en date. Tout d'abord, nous convertirons la chaîne de caractères "2019/08/09" en date.

Nous devons importer la bibliothèque datetime en Python pour pouvoir y parvenir. Nous pouvons le faire en tapant ce qui suit :

```python
from datetime import datetime

date_string = "2018/08/09"

format = %Y/%m/%d #spécifiez le format de la date_string.

date = datetime.strptime(date_string, format)
print(date)
```

Revenons sur le code ci-dessus pour nous assurer que nous comprenons ce qui se passe.

La variable format déclare le format de la chaîne de caractères de date à passer au parseur (la fonction qui nous aidera à convertir la date). Nous devons connaître le format à l'avance, c'est-à-dire avant de le passer au parseur.

Dans ce cas, la chaîne de caractères est au format "2019/08/09".

Le premier élément de la chaîne de caractères représente une année, pour laquelle le code de format est `%Y`. Ensuite, nous avons une barre oblique suivie du mois, pour lequel le code de format est `%m`. Ensuite, nous avons une autre barre oblique, et enfin le jour, pour lequel le code de format est `%d`.

Par conséquent, nous devons inclure le symbole de la barre oblique dans la variable format de la même manière qu'il apparaît dans la chaîne de caractères. Si tout est fait correctement, le format devrait être `"%Y/%m/%d."`

La méthode `datetime.strptime` est le parseur qui nous aidera à convertir la `date_string` que nous lui avons passée en date. Elle nécessite deux paramètres : la chaîne de caractères de date et le format.

Lorsque nous l'imprimons après cela, cela devrait ressembler à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-199.png align="left")

*Image par l'auteur*

Nous pouvons décider de récupérer les attributs que nous voulons. Par exemple, si nous souhaitons obtenir uniquement l'année, nous pouvons le faire en tapant `date.year` et cela imprimera uniquement l'année.

Maintenant que nous comprenons cela, passons à un autre exemple plus complexe que le précédent.

### Exemple – comment convertir une chaîne de caractères en date

Nous allons convertir cet objet chaîne de caractères en date : `"2018-11-15T02:18:49Z"`.

Maintenant, à première vue, nous pouvons voir que cette chaîne de caractères de date contient l'année, le mois, le jour, les heures, les minutes et les secondes. Donc, tout ce que nous devons faire est de créer le format approprié et les symboles qui s'y trouvent.

```python
from datetime import datetime

date_string = "2018-11-15T02:18:49Z"

format = "%Y-%m-%dT%H:%M:%SZ"

date = datetime.strptime(date_string, format)
print(date)
```

Nous pouvons voir qu'il n'y a rien de trop complexe à ce sujet. Suivez simplement le format pour chaque partie de la date et passez également les symboles ou lettres respectifs que vous trouvez dans la chaîne de caractères de date.

Ne vous laissez pas distraire par les symboles ou les lettres dans la chaîne de caractères. Si vous faites tout correctement et que vous l'imprimez, vous devriez obtenir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-200.png align="left")

Assurez-vous de ne pas confondre le code de format `%m` avec `%M`. Le petit `%m` est utilisé pour les mois tandis que le grand `%M` est utilisé pour les minutes.

# Conclusion et pour aller plus loin

Maintenant, nous sommes arrivés à la fin de ce tutoriel. Vous avez appris à convertir une chaîne de caractères en format de date.

Une fois que vous aurez appris les codes de format, vous serez prêt à partir. Assurez-vous simplement de respecter les principes régissant le type de chaîne de caractères qui peut être converti.

Par exemple, vous devez vous souvenir que la chaîne de caractères doit être séparée par quelque chose qui peut être un espace, une lettre ou un symbole. De plus, la plage de la chaîne de caractères ne doit pas être supérieure ou inférieure à la plage du code de format.

Merci d'avoir lu.