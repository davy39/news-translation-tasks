---
title: Cette introduction rapide à Dash vous permettra d'atteindre "Hello World" en
  moins de 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-08T15:31:17.000Z'
originalURL: https://freecodecamp.org/news/this-quick-intro-to-dash-will-get-you-to-hello-world-in-under-5-minutes-86f8ae22ca27
coverImage: https://cdn-media-1.freecodecamp.org/images/0*H4-8vzau4b1jqGgs.
tags:
- name: Dash
  slug: dash
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Cette introduction rapide à Dash vous permettra d'atteindre "Hello World"
  en moins de 5 minutes
seo_desc: 'By Anuj Pahade

  Dash is an open source library for creating reactive apps in Python. You can create
  amazing dashboards in your browser using Dash.

  The Iris data set can be called the ‘hello world’ of data sets. In this article,
  we’ll learn how to buil...'
---

Par Anuj Pahade

[Dash](https://plot.ly/products/dash/) est une bibliothèque open source pour créer des applications réactives en Python. Vous pouvez créer des tableaux de bord incroyables dans votre navigateur en utilisant Dash.

Le [jeu de données Iris](https://gist.github.com/curran/a08a1080b88344b0c8a7) peut être appelé le "hello world" des jeux de données. Dans cet article, nous apprendrons à construire une simple application Dash dans laquelle nous utiliserons le jeu de données Iris. Ce jeu de données est propre, ce qui est bien pour nous afin que nous puissions nous concentrer sur Dash plutôt que sur le nettoyage des données.

### Installation de Dash

Pour construire des applications cool, vous avez besoin de bibliothèques hot.

Si vous n'avez pas encore installé Dash, alors exécutez ces [commandes](https://dash.plot.ly/installation) dans votre terminal :

`pip install dash==0.21.1 # Le cœur de Dash`  
`pip install dash-renderer==0.12.1 # Le front-end de Dash`  
`pip install dash-html-components==0.10.1 # Composants HTML`  
`pip install dash-core-components==0.22.1 # Composants surpuissants`  
`pip install plotly --upgrade`

Exécutez votre application comme suit :

```
python helloiris.py
```

Soyez clair avec vos versions de Python.

### Disposition de l'application

Nous pouvons construire la disposition avec la bibliothèque `dash_html_components` et la bibliothèque `dash_core_components`. Je les ai importées comme montré ci-dessus. La bibliothèque `dash_html_components` est pour toutes les balises HTML, tandis que la seconde est pour les composants interactifs construits avec React.js. Cela dit, écrivons quelque chose dans notre navigateur en utilisant Dash :

```
app.layout = html.Div(children=[    html.H1(children='Visualisation Iris'),    html.Div(    '''        Construit avec Dash : Un framework d'application web pour Python.    ''')])
```

Oui ! C'est aussi simple que cela. Le code HTML équivalent ressemblerait à ceci :

```
<div> <h1> Visualisation Iris </h1> <div> Construit avec Dash : Un framework d'application web pour Python. </div></div>
```

Remarquez l'attribut `children` dans le premier `Div`. Il est utilisé pour définir la `liste` des éléments enfermés dans cette balise. C'est un argument positionnel (toujours en premier) et peut être omis comme vous pouvez le voir dans le prochain `H1` et `Div` montré ci-dessus.

Pouvons-nous le **styliser** ? Je vous entends demander. Bien sûr ! Dash vous permet d'écrire des dictionnaires de style comme vous le feriez dans une balise `<style>` en HTML. Il vous permet également d'écrire du CSS en ligne et de lier des fichiers CSS externes. Voici comment nous pouvons le faire.

#### **Dictionnaires de style**

Créons un dictionnaire appelé couleurs.

```
colors = {         'background': '#0000FF',         'color': '#FFA500'}
```

Il peut être attaché à un élément en utilisant l'attribut `style` comme montré.

```
app.layout = html.Div(style=colors,children=[    html.H1(children='Visualisation Iris'),    html.Div(    '''        Construit avec Dash : Un framework d'application web pour Python.    ''')])
```

#### **CSS en ligne**

Dans Dash, les clés des dictionnaires sont en `camelCase`. Donc au lieu de `text-align`, nous utilisons `textAlign`. De plus, l'attribut `class` des balises HTML est `className` comme vous le savez peut-être si vous utilisez React.

```
app.layout = html.Div(style=colors,children=[    html.H1(children='Visualisation Iris',style = {'textAlign':'center'}),
```

```
html.Div(style={'textAlign':'center'},children='''        Construit avec Dash : Un framework d'application web pour Python.    ''')])
```

#### **CSS externe**

Nous pouvons créer une liste d'URLs ou de chemins vers des fichiers CSS que nous voulons inclure dans notre application Dash, puis utiliser `app.css.append_css` pour les inclure.

```
external_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",              "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" ]
```

```
for css in external_css:    app.css.append_css({"external_url": css})
```

Nous pouvons inclure JavaScript de la même manière en utilisant `app.scripts.append_script`

J'espère que vous êtes toujours avec moi ! Voici à quoi ressemble notre fichier helloiris.py :

```
import dashimport dash_core_components as dccimport dash_html_components as html
```

```
app = dash.Dash()
```

```
#CSS externeexternal_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",                "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css", ]
```

```
for css in external_css:    app.css.append_css({"external_url": css})
```

```
#JavaScript externeexternal_js = ["http://code.jquery.com/jquery-3.3.1.min.js",               "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"]
```

```
for js in external_js:    app.scripts.append_script({"external_url": js})
```

```
#CSS internecolors = {         'background': '#0000FF',         'color': '#FFA500'}
```

```
#Disposition de notre applicationapp.layout = html.Div(style=colors,children=[    html.H1(children='Visualisation Iris',style={'textAlign':'center'}),
```

```
html.Div(style={'textAlign':'center'},children='''     Construit avec Dash : Un framework d'application web pour Python.    ''')])
```

```
if __name__ == '__main__':    app.run_server(debug=True)
```

### Obtenons quelques données

En supposant que vous êtes familier avec pandas, nous utiliserons cette bibliothèque Python pour importer le fichier iris.csv dans notre application. Si vous ne savez pas de quoi parle ce jeu de données, alors je vous recommande de le lire et de le télécharger depuis [ici](https://archive.ics.uci.edu/ml/datasets/iris).

```
import pandas as pd
```

```
header_names =[ 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
```

```
df = pd.read_csv('path/to/Iris.csv',names=header_names)
```

Maintenant que nos données sont chargées dans le dataframe `df`, il est temps de les visualiser.

### Visualisation des données

Vous vous souvenez des composants interactifs dont je vous ai parlé ? La bibliothèque `dash_core_components` ? Eh bien, c'est ce que nous allons utiliser ici.

```
import plotly.graph_objs as go
```

Ajoutons un nouveau composant à notre `app.layout`. Cette fois, ce n'est pas une balise HTML mais un graphique interactif. Dash utilise [Plotly](https://plot.ly/) pour tracer des graphiques.

```
dcc.Graph(        id='Iris Viz',        figure={            'data': [                go.Scatter(                    x=df[df['class'] == i]['petal_length'],                    y=df[df['class'] == i]['sepal_length'],                    mode='markers',                    opacity=0.7,                    marker={                        'size': 15,                        'line': {'width': 0.5, 'color': 'white'}                    },                    name=i                ) for i in df['class'].unique()            ],            'layout': go.Layout(                xaxis={'title': 'Longueur du Pétale'},                yaxis={'title': 'Longueur du Sépale'},                margin={'l': 200, 'b': 40, 't': 100, 'r': 200},                legend={'x': 0, 'y': 1},                hovermode='closest'            )        }    )
```

![Image](https://cdn-media-1.freecodecamp.org/images/68GicF5oCR6Ygfo4AOEHvLXecS1ZAWT892Np)
_C'est à quoi ressemble le graphique._

Whoa ! Un paragraphe entier en Python ! Ne vous inquiétez pas. Ce n'est pas difficile à comprendre. Passons-le en revue pièce par pièce :

Le `dcc.Graph` a un argument `id` qui est utilisé pour référencer le graphique à l'avenir pour le supprimer ou le superposer ou pour toute autre utilisation.

L'argument `figure` est le même que celui utilisé dans [plotly.py](https://plot.ly/). Il prend deux arguments, `data` et `layout`.

Dans `data`, nous pouvons spécifier quelles colonnes du dataframe tracer sur quel axe. Nous pouvons également spécifier le mode, par exemple : **marker** puis les propriétés du marqueur telles que **width** et **line** (signifiant bordure).

Dans `layout`, nous définissons les étiquettes des axes, la position de la légende, les marges du graphique (gauche, haut, bas, droite) et bien plus encore.

Ce n'est pas tout. Ces graphiques sont [interactifs](https://dash-stock-tickers.plot.ly/) et peuvent être manipulés par les entrées de l'utilisateur.

D'accord, alors construisons quelques DashApps cool cet été !

Restez à l'écoute pour mes prochains articles. Ce n'est pas ma première fois en codage ou en création d'une application, mais c'est mon premier article sur Medium ! Je pense que les applaudissements et les recommandations me motiveront :)

N'hésitez pas à me contacter par email : anujp5678[at]gmail[dot]com

Ou connectez-vous avec moi sur LinkedIn [https://www.linkedin.com/in/anuj-pahade/](https://www.linkedin.com/in/anuj-pahade/)

Continuez à Dash et bon codage !