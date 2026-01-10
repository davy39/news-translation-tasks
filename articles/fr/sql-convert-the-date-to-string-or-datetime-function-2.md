---
title: SQL CONVERT – La fonction de conversion de DATE en chaîne ou DATETIME
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-10T18:30:50.000Z'
originalURL: https://freecodecamp.org/news/sql-convert-the-date-to-string-or-datetime-function-2
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/dateToString.png
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: SQL CONVERT – La fonction de conversion de DATE en chaîne ou DATETIME
seo_desc: 'When you''re working with SQL, you''ll need to learn how to format dates
  properly.

  This is because dates are an important aspect of any SQL and other software-related
  activities. You need to be able to work with dates to add timestamps to entries
  and k...'
---

Lorsque vous travaillez avec SQL, vous devrez apprendre à formater correctement les dates.

C'est parce que les dates sont un aspect important de toute activité SQL et liée à d'autres logiciels. Vous devez être capable de travailler avec des dates pour ajouter des horodatages aux entrées et suivre quand les choses se produisent, par exemple. Presque tout dépend d'une date.

Dans cet article, je veux vous montrer comment convertir une date et un datetime en chaîne en SQL avec les fonctions `CONVERT()` et `STR_TO_DATE()`.

## Ce que nous allons couvrir
- [Comment convertir une date en chaîne avec la fonction `CONVERT()`](#heading-comment-convertir-une-date-en-chaine-avec-la-fonction-convert)
- [Comment convertir une date en chaîne avec la fonction `STR_TO_DATE()`](#heading-comment-convertir-une-date-en-chaine-avec-la-fonction-strtodate)
- [Comment utiliser `DATE_FORMAT()` pour changer le format de l'heure](#heading-comment-utiliser-dateformat-pour-changer-le-format-de-lheure)
- [Conclusion](#heading-conclusion)

## Comment convertir une date en chaîne avec la fonction `CONVERT()`

La fonction `CONVERT()` attend deux arguments :

- la date – doit être une chaîne, ou avec des fonctions intégrées comme `NOW()` ou `SYSDATE()`
- le type de données – le type de données auquel vous voulez convertir la date.

Voici la fonction `CONVERT()` en action :
```sql
SELECT CONVERT(NOW(), CHAR);
```

![ss1](https://www.freecodecamp.org/news/content/images/2023/01/ss1.png) 

La requête ci-dessus a utilisé la fonction `NOW()` pour obtenir la date et l'heure actuelles. Le deuxième argument, `CHAR`, est le type de données auquel la date a été convertie. 

Vous pouvez également utiliser `SYSDATE()` à sa place si vous le souhaitez :

```sql
SELECT CONVERT(SYSDATE(), CHAR);
``` 
![ss2](https://www.freecodecamp.org/news/content/images/2023/01/ss2.png)

Il existe de nombreuses autres fonctions que vous pouvez utiliser pour travailler avec des dates. J'en ai parlé [dans ce tutoriel](https://www.freecodecamp.org/news/sql-date-function-query-timestamp-example-format/) si vous souhaitez en savoir plus.

Les fonctions ne sont pas les seuls paramètres que vous pouvez utiliser comme premier argument de la fonction convert. Vous pouvez utiliser une date écrite sous forme de chaîne, puis spécifier `DATE` comme type de données auquel vous voulez la convertir :

```sql
SELECT CONVERT("2023-01-10", DATE)
```

![ss3](https://www.freecodecamp.org/news/content/images/2023/01/ss3.png) 


## Comment convertir une date en chaîne avec la fonction `STR_TO_DATE()`

La fonction `STR_TO_DATE()` est une autre fonction utile pour convertir une date ou un datetime. Elle accepte deux paramètres :

- la date – elle doit être une chaîne. Par exemple, '09-01-2023'

- le format – le format auquel vous voulez que la date soit convertie. Par exemple `mm-dd-yyyy`. Vous spécifiez le format comme ceci `%d-%m-%Y`.

Voici comment fonctionne la fonction `STR_TO_DATE()` :

```sql
SELECT STR_TO_DATE('09-01-2023', '%d-%m-%Y')
```

![ss4](https://www.freecodecamp.org/news/content/images/2023/01/ss4.png) 

Vous pouvez également utiliser une barre oblique (`/`) pour séparer la date et le format :

```sql
SELECT STR_TO_DATE('09/01/2023', '%d/%m/%Y')
```

**N.B.** : Si vous n'utilisez pas le même séparateur pour la date et le format, vous obtiendrez null en retour. 

![ss5](https://www.freecodecamp.org/news/content/images/2023/01/ss5.png) 

Si vous entrez le jour comme le n-ième jour de cette date, vous devez changer le `d` dans le format en une lettre majuscule :

```sql 
SELECT STR_TO_DATE('9th-01-2023', '%D-%m-%Y')
``` 

![ss6](https://www.freecodecamp.org/news/content/images/2023/01/ss6.png) 

Et si vous entrez le mois comme l'abréviation de ce mois, vous devez changer le `m` dans le format en une lettre majuscule :

```sql
SELECT STR_TO_DATE('9th-JAN-2023', '%D-%M-%Y')
```

![ss7](https://www.freecodecamp.org/news/content/images/2023/01/ss7.png) 

Ensuite, nous verrons comment vous pouvez travailler avec les formats de date avec la fonction `DATE_FORMAT()`.


## Comment utiliser `DATE_FORMAT()` pour changer le format de l'heure

Si vous voulez le mois comme le nom complet de ce mois, changez le `m` dans le format en une lettre majuscule et utilisez la fonction `DATE_FORMAT()` :

```sql
SELECT DATE_FORMAT('2023-01-09', '%d-%M-%y')
```

![ss8](https://www.freecodecamp.org/news/content/images/2023/01/ss8.png) 

Si vous voulez le jour comme le n-ième numéro de ce jour, changez le d dans le format en une lettre majuscule :

```sql
SELECT DATE_FORMAT('2023-01-09', '%D-%M-%y')
```

![ss9](https://www.freecodecamp.org/news/content/images/2023/01/ss9.png) 

Et si vous voulez l'année en entier, changez le y en une lettre majuscule :

```sql
SELECT DATE_FORMAT('2023-01-09', '%D-%M-%Y')
```

![ss10](https://www.freecodecamp.org/news/content/images/2023/01/ss10.png) 


## Conclusion
Cet article vous a montré comment convertir une date en chaîne avec les fonctions `CONVERT()` et `STR_TO_DATE()`. Nous avons également vu comment vous pouvez changer le format de la date avec la fonction `DATE_FORMAT()`.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis sur les réseaux sociaux.