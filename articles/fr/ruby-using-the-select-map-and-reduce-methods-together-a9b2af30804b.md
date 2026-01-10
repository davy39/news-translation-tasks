---
title: Tirez le meilleur parti de Ruby en utilisant les méthodes .select, .map et
  .reduce ensemble
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-30T06:01:48.000Z'
originalURL: https://freecodecamp.org/news/ruby-using-the-select-map-and-reduce-methods-together-a9b2af30804b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1WIbhb82wmieRfp3XL2Ysg.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Tirez le meilleur parti de Ruby en utilisant les méthodes .select, .map
  et .reduce ensemble
seo_desc: 'By Declan Meehan

  You should absolutely never ever repeat yourself when writing code. In other words,
  do not repeat yourself twice. To be clear — do not write something which has been
  explained already.

  This is called tautology, and when writing code ...'
---

Par Declan Meehan

Vous ne devriez absolument jamais vous répéter lorsque vous écrivez du code. En d'autres termes, ne vous répétez pas deux fois. Pour être clair — n'écrivez pas quelque chose qui a déjà été expliqué.

Cela s'appelle une tautologie, et lorsque vous écrivez du code, cela doit être évité à tout moment. Par exemple, n'aurait-il pas été plus agréable, au lieu de lire ce long paragraphe, si j'avais simplement utilisé les trois mots puissants « jamais, répéter, vous-même » ?

Eh bien, c'est ce que je vais vous montrer comment faire avec les méthodes .select, .map et .reduce (ou .inject) de Ruby.

### Exemple

Supposons que vous regardiez un dictionnaire rempli de noms d'employés, de titres de poste et de salaires. Imaginons également que vous souhaitiez connaître le montant total que l'entreprise dépensait en salaires de développeurs. Maintenant, sans utiliser une seule méthode en Ruby, vous écririez probablement votre code quelque chose comme ceci :

```ruby
people = [
  {
    first_name: "Gary", 
    job_title: "car enthusiast", 
    salary: "14000" 
  },  
  {
    first_name: "Claire", 
    job_title: "developer", 
    salary: "15000"
  },  
  {
    first_name: "Clem", 
    job_title: "developer", 
    salary: "12000"
  }
]
person1 = people[0][:job_title]
person2 = people[1][:job_title]
person3 = people[2][:job_title]
total = 0
if person1 == "developer"
    total += people[0][:salary].to_i
end
if person2 == "developer"
    total += people[1][:salary].to_i
end
if person3 == "developer"
    total += people[2][:salary].to_i
end
puts total
```

Wow — c'est beaucoup de lignes à écrire pour trouver seulement trois personnes. Imaginez si l'entreprise employait des centaines de personnes !

Maintenant, si vous connaissez un peu les boucles, alors l'étape suivante la plus facile serait d'écrire une méthode each pour mettre tous les salaires ensemble. Cela pourrait ne prendre que cinq ou six lignes, mais regardez ceci !

```ruby
puts people.select{|x| x[:job_title] == "developer"}.map{|y| y[:salary].to_i}.reduce(:+)
```

![Image](https://cdn-media-1.freecodecamp.org/images/CVi6LVbCoOsskAzyQdVJGQ2GzBZq68XOExMJ)
_Cela peut sembler confus, mais décomposons-le en morceaux._

Vous remarquerez que chaque méthode commence et se termine par une accolade. Cela peut être utilisé à la place des commandes do et end si c'est un bloc d'une seule ligne.

```ruby
{} == (do end) #uniquement pour les blocs d'une seule ligne
```

### .select

Commençons par la méthode .select. Nous créons une variable (x) et itérons sur chaque méthode dans le tableau people. Elle vérifie ensuite avec une expression booléenne si la clé (:job_title) est égale à la chaîne « developer ». Si le booléen retourne vrai, alors la méthode select place le hachage qui a retourné vrai dans un nouvel objet.

### .map

La méthode map est utilisée pour créer un nouveau tableau qui n'affecte pas le tableau sur lequel elle itère. J'ai utilisé cette méthode pour créer une nouvelle variable (y), puis utilisé cette variable pour récupérer la valeur de la clé (:salary). Ensuite, enfin, j'ai transformé cette valeur d'une chaîne en un entier.

### .reduce

Celle-ci semble probablement la plus confuse, alors développons-la un peu.

```ruby
.reduce(0){|sum, indv| sum + indv} #est la même chose que .reduce(:+)
```

La méthode reduce crée une nouvelle variable dont vous définissez la valeur égale dans les premières parenthèses (0). Vous créez ensuite deux nouvelles valeurs (sum et indv) dont l'une est la somme à laquelle vous ajoutez les salaires individuels.

J'espère que cela explique bien ! N'hésitez pas à me faire savoir si vous avez des questions.