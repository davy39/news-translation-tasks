---
title: Comment créer un jeu terminal avec CSV et Ruby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T17:57:39.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-build-a-terminal-game-with-csv-and-ruby-a269f17b88b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CsSq6749MEFgk7jBOHroEg.gif
tags:
- name: Data Science
  slug: data-science
- name: Games
  slug: games
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: technology
  slug: technology
seo_title: Comment créer un jeu terminal avec CSV et Ruby
seo_desc: 'By Andrew Bales

  In this article, you’ll learn how to build a terminal game with a CSV and a few
  Ruby gems! See a demo in the video above, and find the code on GitHub.

  This project comes from a lecture I gave at Ada Developers Academy in Seattle. The
  ...'
---

Par Andrew Bales

Dans cet article, vous apprendrez à créer un jeu terminal avec un CSV et quelques gems Ruby ! Voir une démonstration dans la vidéo ci-dessus, et trouver le code sur [GitHub](https://github.com/agbales/solar-system).

Ce projet provient d'une conférence que j'ai donnée à [Ada Developers Academy](https://www.adadevelopersacademy.org) à Seattle. Le sujet était la bibliothèque Ruby CSV, et je voulais une manière amusante d'illustrer ses méthodes et son potentiel.

En classe, nous avons discuté de la manière dont la plupart des gens utilisent des programmes comme Excel pour créer et éditer des CSV. Ils font des mises à jour en cliquant sur des cellules et en changeant des valeurs. Mais la question pour nous est devenue : que pouvons-nous faire avec un CSV si nous l'abordons en tant que **programmeurs** ? En utilisant un langage de programmation comme Ruby, comment pouvez-vous ouvrir, lire et manipuler ces valeurs ? Ces rangées et colonnes ordonnées peuvent-elles devenir une base de données pour une application ?

Cet article couvre ces questions en trois sections :

1. Valeurs séparées par des virgules
2. Bibliothèque CSV de Ruby : création, ouverture, ajout, utilisation des en-têtes
3. Construction du jeu

### Valeurs séparées par des virgules

CSV signifie "comma-separated values" (valeurs séparées par des virgules), et c'est exactement ce que cela semble être. Si vous avez déjà ouvert l'un de ces fichiers dans un programme comme Excel, vous avez vu ces valeurs rendues dans une feuille de calcul.

Cependant, si vous ouvriez ce même fichier dans un éditeur de texte comme Atom ou Sublime, vous trouveriez une série de — vous l'avez deviné — valeurs séparées par des virgules. Comme vous le voyez ci-dessous, Excel utilise ces valeurs brutes pour rendre un tableau convivial.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wrExasjrLVB2AOvKDG_TAQ.jpeg)

### Installation rapide

Il est plus facile de suivre si vous téléchargez ce [dépôt GitHub](https://github.com/agbales/solar-system). Une fois que vous l'avez fait, naviguez jusqu'à ce dossier dans votre terminal. Ce dépôt inclut **tous** les exemples ci-dessous, alors sachez que vous devrez commenter les sections que vous ne voulez pas exécuter.

De plus, vous voudrez installer [Awesome Print](https://github.com/awesome-print/awesome_print), qui embellit la sortie du terminal :

```
gem install awesome_print
```

### Bibliothèque CSV de Ruby

Ruby est livré avec une [bibliothèque CSV](http://ruby-doc.org/stdlib-2.0.0/libdoc/csv/rdoc/CSV.html) qui nous permet d'ouvrir, de lire et de manipuler des fichiers CSV.

#### **Création d'un CSV**

Commençons par créer notre propre CSV. Dans le dépôt GitHub, vous trouverez planets.rb. Ce fichier commence par définir la variable planets égale à un tableau à deux dimensions (un tableau de tableaux).

Dans chacun, nous avons les attributs de la planète : id, nom, masse et distance. Nous avons assigné les noms des attributs à la variable headers en tant qu'autre tableau.

```
require 'csv'
require 'awesome_print'
```

```
planets = [
  [1, "Mercury", 0.055, 0.4],
  [2, "Venus", 0.815, 0.7],
  [3, "Earth", 1.0, 1.0],
  [4, "Mars", 0.107, 1.5]
]
headers = ["id", "name", "mass", "distance"]
CSV.open("planet_data.csv", "w") do |file|
  file << headers
  planets.each do |planet|
    file << planet
  end
end
```

Ci-dessus, CSV.open accepte jusqu'à trois arguments :

```
CSV.open(nom_du_fichier, mode, options)
```

Nous lui avons donné un nom de fichier (planet_data.csv). Parce que nous avons également donné le mode "w" (écriture seule), il crée un nouveau fichier pour nous même s'il n'existait pas déjà. Aucune option n'a été passée cette fois.

Le bloc suivant fait quelques choses :

1. Il ajoute le tableau des en-têtes au fichier que nous avons créé. Cela crée une seule rangée avec quatre colonnes — chacune avec une entrée de chaîne de caractères du nom de la propriété.
2. Nous utilisons planets.each pour itérer à travers le tableau des planètes (rempli d'informations sur son id, son nom, etc.) et ajouter chaque entrée en tant que rangée individuelle.

Si vous exécutez ce bout de code, vous trouverez que le CSV suivant a été créé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4-WNK1cd7_0AQ_0yKVeNWg.png)

#### Modes

Ci-dessus, nous avons utilisé "w" comme notre mode pour écrire un nouveau fichier. Vous avez un certain nombre d'autres options disponibles, selon la tâche à accomplir. Les plus grands facteurs à considérer sont si vous voulez lire et/ou écrire, et où dans le CSV vous souhaitez commencer votre travail.

Par exemple, si vous utilisez le fichier pour remplir votre site web avec des listes, "r" (lecture seule) serait un mode approprié. Si vous voulez ajouter de nouvelles planètes à votre CSV, le mode "a" (ajout lecture-écriture) commencerait à la fin du fichier et vous permettrait immédiatement d'ajouter ces rangées.

Voici une liste complète des modes :

```
"r"  Lecture seule, commence au début du fichier (mode par défaut).
"r+" Lecture-écriture, commence au début du fichier.
"w"  Écriture seule, tronque le fichier existant à une longueur de zéro.
"w+" Lecture-écriture, tronque le fichier existant à une longueur de zéro.
"a"  Ajout écriture seule, commence à la fin du fichier si le fichier existe.
"a+" Ajout lecture-écriture, commence à la fin du fichier si le fichier existe.
"b"  Mode fichier binaire.
"t"  Mode fichier texte.
```

#### **Ajout**

Nous pouvons ajouter une nouvelle planète à planet_data.csv comme ceci :

```
CSV.open("planet_data.csv", "a") do |file|
  file << [5, "Jupiter", 1234, 3321]
end
```

Dans la liste des modes ci-dessus, "a" est "écriture seule" et "commence à la fin du fichier". Ainsi, les informations de Jupiter seront insérées à la fin du CSV existant.

#### Itération

Parce que .open avec le mode "r" retournera un tableau de tableaux, nous pouvons utiliser .each pour itérer sur les rangées. Le code ci-dessous imprimera chaque rangée du CSV dans le terminal.

```
CSV.open("planet_data.csv", "r").each do |row|
  ap row
end
```

Vous pouvez aller plus loin pour créer des phrases interpolées !

```
CSV.open("planet_data.csv", "r").each do |row|
  ap "#{row[1]} a une masse de #{row[2]} et une distance de #{row[3]}."
end
```

C'est bien, mais cela pourrait être un peu mieux. Nous devons utiliser des indices (1, 2, 3) pour accéder aux données. Cela est sujet à des erreurs et généralement pas amusant. Ensuite, nous verrons comment corriger cela en passant des options.

#### Utilisation des en-têtes

Lorsque vous ajoutez l'option pour que les en-têtes soient vrais, vous obtiendrez un nouvel objet CSV::Table.

```
csv_with_headers = CSV.open("planet_data.csv", "r", headers: true, header_converters: :symbol)
csv_with_headers.each do |row|
  ap row
end
```

En lisant avec des en-têtes et en convertissant ces en-têtes en symboles, nous obtiendrons un objet unique : un tableau de hachages. Cela signifie qu'il est possible d'itérer à travers chaque rangée comme nous l'avons fait auparavant, mais nous pouvons également utiliser les symboles dans le hachage pour isoler les données clés.

Si nous revenons à l'exemple de phrase, cela devient :

```
CSV.open("planet_data.csv", "r", headers: true, header_converters: :symbol).each do |row|
  ap "#{row[:name]} a une masse de #{row[:mass]} et une distance de #{row[:distance]}."
end
```

C'est beaucoup plus lisible que les indices numériques que nous avons utilisés auparavant !

Lorsque les en-têtes sont définis sur vrai, la bibliothèque nous donne l'objet CSV::Table, qui nous donne également accès à certaines méthodes pratiques. Ci-dessous, .read est synonyme de .open en mode "r" :

```
csv = CSV.read("planet_data.csv", headers: true, header_converters: :symbol)
ap csv               # <CSV::Table mode:col_or_row row_count:6>
ap csv.headers       # Retourne un tableau d'en-têtes
ap csv.by_col[:id]   # Tableau des données de la colonne id
ap csv.by_col[:name] # Tableau des données de la colonne name
ap csv.by_row[0]     # Rangée entière à la position 0 (ou toute autre position)
ap csv[:name][3]     # Nom de la 3ème entrée => "Mars"
ap csv[3][:name]     # Nom de la 3ème rangée => "Mars"
```

### Construction d'un jeu du système solaire !

Nous savons comment ouvrir et utiliser des données dans un fichier CSV avec Ruby, alors mettons ces méthodes au travail pour créer un jeu du système solaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CsSq6749MEFgk7jBOHroEg.gif)
_Via [SUPERNOVA](https://imahimesama.tumblr.com/post/164924479335" rel="noopener" target="_blank" title=")_

#### **Installation**

Vous devrez installer Catpix et Launchy. Catpix permet des illustrations dans le terminal et Launchy nous permet de contrôler une fenêtre de navigateur. Dans le terminal :

```
gem install catpix
gem install launchy
```

#### **CSV comme base de données**

Vous voudrez peut-être ouvrir "Solar System.csv" dans Excel pour avoir une idée visuelle des attributs de chaque entrée. Une fois que vous êtes à l'aise avec les données, nous utiliserons Ruby pour lire le fichier CSV et l'assigner à une variable globale ($solar_system_data). Cela servira de base de données.

Au démarrage du jeu, nous accueillons l'utilisateur DANS LE SYSTÈME SOLAIRE ! et créons cette base de données comme suit :

```
require 'catpix'
require 'launchy'
$solar_system_data = CSV.read("Solar System.csv", headers: true, header_converters: :symbol)
```

```
ap "BIENVENUE DANS LE SYSTÈME SOLAIRE !"
```

Le jeu démarre vraiment lorsque nous appelons la méthode explore_planet. Cette méthode contient ce code :

```
ap $solar_system_data.by_col[:name]
prompt = "Où souhaitez-vous commencer ? 0 - #{$solar_system_data.length}"
```

```
ap prompt
input = gets.chomp
```

```
until $selected_planet && /\d/.match(input)
  ap prompt
  input = gets.chomp
  $selected_planet = $solar_system_data[input.to_i]
end
```

```
ap $selected_planet
```

Ci-dessus, le terminal imprime tous les noms de la colonne "name". Il demande ensuite à l'utilisateur de sélectionner une entrée entre la première (index 0) et la dernière (la longueur de nos données). C'est un bon moment pour faire une pause et considérer ce qui suit :

**Question :** Si nous avons utilisé des en-têtes afin d'obtenir un hachage, comment solar_system_data.length peut-il être égal à 14 ?

**Réponse :** Ce CSV::Table peut **ressembler** à un hachage, mais c'est en réalité un tableau de hachages. Par conséquent, il a une longueur et nous pouvons itérer à travers chaque hachage. Pour sélectionner l'enregistrement correct, nous devons simplement convertir l'entrée d'une chaîne en un entier (.to_i)

Vous verrez également que nous avons utilisé une instruction until. Cela valide la sélection — demandant une réponse jusqu'à ce que l'utilisateur nous donne un nombre valide. Une fois qu'une sélection appropriée est faite, le terminal imprime les informations de la planète.

L'utilisateur peut ensuite choisir s'il veut APPRENDRE ou VOIR la planète :

```
prompt = "Voulez-vous APPRENDRE ou VOIR ?"
ap prompt
```

```
while input = gets.chomp
  case input.downcase
  when "learn"
    Launchy.open($selected_planet[:uri])
    return
  when "see"
    Catpix::print_image $selected_planet[:image]
    return
  else
    ap prompt
  end
end
```

Similaire à avant, une instruction while est utilisée pour s'assurer que nous obtenons une entrée valide. Cette fois, elle utilise soit Launchy pour ouvrir l'URI associé à la planète, soit imprime l'image dans le terminal avec Catpix.

Le jeu a une autre fonctionnalité. Celle-ci est contenue dans la méthode select_attribute. Nous utilisons les méthodes CSV que nous venons de couvrir pour retourner des attributs spécifiques pour **chaque** planète dans notre base de données.

```
ap "Quel attribut souhaitez-vous voir pour chaque planète (ex: number_of_moons) ?"
```

```
ap $solar_system_data.headers.to_s
attribute = gets.chomp
```

```
ap "Voici les résultats pour #{attribute} :"
```

```
$solar_system_data.each do |row|
  ap "#{row[:name]} --> #{attribute}: #{row[attribute.to_sym]}"
end
```

Tout d'abord, nous imprimons tous les en-têtes sous forme de chaînes. Cela donne à l'utilisateur une liste d'attributs parmi lesquels choisir. Avec la réponse de l'utilisateur, nous pouvons lister le nom de la planète ainsi que l'attribut demandé et sa valeur.

Enfin, ils peuvent SÉLECTIONNER un autre attribut ou recommencer et EXPLORER des planètes individuelles :

```
prompt = "SÉLECTIONNER un autre attribut ou EXPLORER une autre planète ?"
ap prompt
```

```
while input = gets.chomp
  case input.downcase
  when "select"
    select_attribute()
  when "explore"
    explore_planet()
  else
    ap prompt
  end
end
```

J'espère que cela aide à clarifier les méthodes CSV et vous donne envie de créer vos propres jeux.

Si vous développez ce jeu ou concevez quelque chose de nouveau, laissez un commentaire. J'adorerais voir ce que vous avez imaginé !