---
title: Comment et pourquoi j'ai utilisé Plotly (au lieu de D3) pour visualiser mes
  données de Lollapalooza
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-04T21:57:10.000Z'
originalURL: https://freecodecamp.org/news/how-and-why-i-used-plotly-instead-of-d3-to-visualize-my-lollapalooza-data-d48345e2ca68
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MbduYVMgabo7VzOTps5VPg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment et pourquoi j'ai utilisé Plotly (au lieu de D3) pour visualiser
  mes données de Lollapalooza
seo_desc: 'By Déborah Mesquita

  D3.js is an awesome JavaScript library, but it has a very steep learning curve.
  This makes the task of building a valuable visualization something that can take
  a lot of effort. This extra effort is ok if your goal is to make new ...'
---

Par Débora Mesquita

D3.js est une bibliothèque JavaScript géniale, mais elle a une courbe d'apprentissage très raide. Cela rend la tâche de création d'une visualisation précieuse quelque chose qui peut prendre beaucoup d'efforts. Cet effort supplémentaire est acceptable si votre objectif est de créer de nouvelles visualisations de données créatives, mais souvent ce n'est pas le cas.

Souvent, votre objectif peut simplement être **de créer une visualisation interactive avec certains graphiques bien connus**. Et si vous n'êtes pas un ingénieur front-end, cela peut devenir un peu délicat.

En tant que scientifiques des données, l'une de nos principales tâches est la manipulation des données. Aujourd'hui, le principal outil que j'utilise pour cela est [Pandas](https://en.wikipedia.org/wiki/Pandas_(software)) (Python). Que diriez-vous si je vous disais que **vous pouvez créer de beaux graphiques interactifs pour le web directement à partir de vos dataframes Pandas** ? Eh bien, **vous pouvez !** Nous pouvons utiliser [**Plotly**](https://en.wikipedia.org/wiki/Plotly) pour cela.

Pour information, il existe également des bibliothèques Plotly API pour Matlab, R et JavaScript, mais nous nous en tiendrons à la bibliothèque Python ici.

Pour être juste, Plotly est construit [sur d3.js (et stack.gl)](https://plot.ly/python/user-guide/). La principale différence entre D3 et Plotly est que Plotly est spécifiquement **une bibliothèque de graphiques**.

Construisons un graphique à barres pour comprendre comment Plotly fonctionne.

### Construire un graphique à barres avec Plotly

Il y a 3 concepts principaux dans la philosophie de Plotly :

* Données
* Disposition
* Figure

#### Données

L'objet Données définit ce que nous voulons afficher dans le graphique (c'est-à-dire les données). Nous définissons une collection de données et les spécifications pour les afficher sous forme de **trace**. Un objet Données peut avoir plusieurs traces. Imaginez un graphique en ligne avec deux lignes représentant deux catégories différentes : chaque ligne est une trace.

#### Disposition

L'objet Disposition définit les caractéristiques qui ne sont pas liées aux données (comme le titre, les titres des axes, etc.). Nous pouvons également utiliser la Disposition pour ajouter des annotations et des formes au graphique.

#### Figure

L'objet Figure crée l'objet final à tracer. C'est un objet qui contient à la fois les données et la disposition.

Les visualisations Plotly sont construites avec plotly.js. Cela signifie que l'API Python est simplement **un package pour interagir avec la bibliothèque plotly.js**. Le module `plotly.graph_objs` contient les fonctions qui généreront des objets graphiques pour nous.

D'accord, nous sommes maintenant prêts à construire un graphique à barres :

```
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as offline
```

```
df = pd.read_csv("data.csv")
```

```
df_purchases_by_type = df.pivot_table(    index = "place",     columns = "date",     values = "price",     aggfunc = "sum"    ).fillna(0)
```

```
trace_microbar = go.Bar(    x = df_purchases_by_type.columns,     y = df_purchases_by_type.loc["MICROBAR"])
```

```
data = [trace_microbar]
```

```
layout = go.Layout(title = "Purchases by place", showlegend = True)
```

```
figure = go.Figure(data = data, layout = layout)
```

```
offline.plot(figure)
```

_Note : dans cet article, nous ne parlerons pas de ce que je fais avec les dataframes. Mais si vous souhaitez un article à ce sujet, faites-le moi savoir dans les commentaires ?_

D'accord, donc d'abord nous voulons montrer les barres d'une catégorie (un lieu appelé `"MICROBAR"`). Nous créons donc un objet de données (une liste) avec `go.Bar()` (une trace) en spécifiant les données pour les axes x et y. Trace est un dictionnaire et data est une liste de dictionnaires. Voici le contenu de `trace_microbar` (remarquez la clé type) :

```
{'type': 'bar',  'x': Index(['23/03/2018', '24/03/2018', '25/03/2018'], dtype='object', name='date'),   'y': date  23/03/2018     0.0  24/03/2018     0.0  25/03/2018    56.0  Name: MICROBAR, dtype: float64}
```

Dans l'objet Disposition, nous définissons le titre du graphique et le paramètre showlegend. Ensuite, nous enveloppons les Données et la Disposition dans une figure et appelons `plotly.offline.plot()` pour afficher le graphique. Plotly a différentes options pour afficher les graphiques, mais restons avec l'option hors ligne ici. Cela ouvrira une fenêtre de navigateur avec notre graphique.

![Image](https://cdn-media-1.freecodecamp.org/images/UpBNLA8zEIXNHLy8j4Y10cbLP2piXXmZ2bhm)
_Le résultat_

Je veux tout afficher dans un graphique à barres empilées, donc nous allons créer une liste de données avec toutes les traces (lieux) que nous voulons afficher et définir le paramètre `barmode` sur **stack**.

```
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as offline
```

```
df = pd.read_csv("data.csv")
```

```
df_purchases_by_place = df.pivot_table(index="place",columns="date",values="price",aggfunc="sum").fillna(0)
```

```
data = []
```

```
for index,place in df_purchases_by_place.iterrows():    trace = go.Bar(        x = df_purchases_by_place.columns,         y = place, name=index    )    data.append(trace)
```

```
layout = go.Layout(          title="Purchases by place",           showlegend=True,           barmode="stack"        )
```

```
figure = go.Figure(data=data, layout=layout)
```

```
offline.plot(figure)
```

![Image](https://cdn-media-1.freecodecamp.org/images/sXdlsRvCRWAfr8ve73JM2bYX7YjswDXO0xTV)
_Graphique à barres empilées_

Et ce sont les bases de Plotly. Pour personnaliser nos graphiques, nous définissons différents paramètres pour les traces et la disposition. Maintenant, passons à la visualisation de Lollapalooza.

### Mon expérience à Lollapalooza

Pour l'édition 2018 de Lollapalooza Brésil, tous les achats ont été effectués via un bracelet à puce RFID. Ils envoient les données à votre adresse e-mail, alors j'ai décidé de les examiner. **Que pouvons-nous apprendre sur moi et mon expérience en analysant les achats que j'ai faits au festival ?**

Voici à quoi ressemblent les données :

* date d'achat
* heure d'achat
* produit
* quantité
* scène
* lieu où j'ai fait l'achat

Sur la base de ces données, répondons à quelques questions.

#### Où suis-je allé pendant le festival ?

Les données ne nous indiquent que le nom de l'endroit où j'ai fait l'achat, et le festival a eu lieu à l'Autódromo de Interlagos. J'ai pris la carte avec les scènes [ici](https://www.lollapaloozabr.com/mapa-2018/) et utilisé l'outil de géoréférencement de [georeference.com](https://www.georeferencer.com/maps/897503229699/view) pour obtenir les coordonnées de latitude et de longitude des scènes.

![Image](https://cdn-media-1.freecodecamp.org/images/2oYtS8TBUrEtk2pmtTvgV6nI05yfAtqMxJmZ)
_Carte de Lollapalooza Brésil 2018_

Nous devons afficher une carte et les marqueurs pour chaque achat, donc nous allons utiliser [Mapbox](https://www.mapbox.com/about/) et la trace `scattermapbox`. Commençons par tracer uniquement les scènes pour voir comment cela fonctionne :

```
import plotly.graph_objs as go
import plotly.offline as offline
import pandas as pd
```

```
mapbox_token = "" #https://www.mapbox.com/help/define-access-token/
```

```
df = pd.read_csv("stages.csv")
```

```
trace = go.Scattermapbox(    lat = df["latitude"],     lon = df["longitude"],     text=df["stage"],     marker=go.Marker(size=10),     mode="markers+text",     textposition="top"  )
```

```
data = [trace]
```

```
layout = go.Layout(          mapbox=dict(            accesstoken=mapbox_token,             center=dict(              lat = -23.701057,              lon = -46.6970635             ),             zoom=14.5          )         )
```

```
figure = go.Figure(data = data, layout = layout)
```

```
offline.plot(figure)
```

![Image](https://cdn-media-1.freecodecamp.org/images/4ermT5RH5imnzvnjqNQ7lLSeF8Gyz70VtWWq)
_Notre première carte_

Apprenons un nouveau paramètre de Disposition : `updatemenus`. Nous allons l'utiliser pour afficher les marqueurs par date. Il existe quatre méthodes de mise à jour possibles :

* `"restyle"` : modifier les données ou les attributs de données
* `"relayout"` : modifier les attributs de disposition
* `"update"` : modifier les données **et** les attributs de disposition
* `"animate"` : démarrer ou mettre en pause une [animation](https://plot.ly/python/#animations))

Pour mettre à jour les marqueurs, nous devons uniquement modifier les données, donc nous utiliserons la méthode `"restyle"`. Lors du restyling, vous pouvez définir les changements pour chaque trace ou pour toutes les traces. Ici, nous définissons chaque trace pour qu'elle soit visible uniquement lorsque l'utilisateur change l'option du menu déroulant :

```
import plotly.graph_objs as go
import plotly.offline as offline
import pandas as pd
import numpy as np
```

```
mapbox_token = ""
```

```
df = pd.read_csv("data.csv")
```

```
df_markers = df.groupby(["latitude","longitude","date"]).agg(dict(product = lambda x: "%s" % ", ".join(x), hour = lambda x: "%s" % ", ".join(x)))
df_markers.reset_index(inplace=True)
```

```
data = []
update_buttons = []
```

```
dates = np.unique(df_markers["date"])
```

```
for i,date in enumerate(dates):    df_markers_date = df_markers[df_markers["date"] == date]    trace = go.Scattermapbox(               lat = df_markers_date["latitude"],               lon = df_markers_date["longitude"],               name = date, text=df_markers_date["product"]+"<br>"+df_markers_date["hour"],               visible=False            )    data.append(trace)
```

```
    visible_traces = np.full(len(dates), False)    visible_traces[i] = True
```

```
    button = dict(               label=date,                method="restyle",                args=[dict(visible = visible_traces)]             )    update_buttons.append(button)
```

```
updatemenus = [dict(active=-1, buttons = update_buttons)]
```

```
layout = go.Layout(            mapbox=dict(              accesstoken=mapbox_token,               center=dict(                  lat = -23.701057,                  lon = -46.6970635),                   zoom=14.5),               updatemenus=updatemenus           )
```

```
figure = go.Figure(data = data, layout = layout)
```

```
offline.plot(figure)
```

![Image](https://cdn-media-1.freecodecamp.org/images/EJFQgSo-90XJEj4dO2sLW6nkOsvrAQBjqpmC)
_Une carte avec une liste déroulante_

#### Comment ai-je dépensé mon argent ?

Pour répondre à cela, j'ai créé un graphique à barres avec mes dépenses pour la nourriture et les boissons chaque jour et construit une carte thermique pour montrer quand j'ai acheté des choses. Nous avons déjà vu comment construire un graphique à barres, alors construisons maintenant une carte thermique :

```
import plotly.graph_objs as go
import pandas as pd
import plotly.offline as offline
```

```
df = pd.read_csv("data.csv")
```

```
df_purchases_by_type = df.pivot_table(index="place",columns="date",values="price",aggfunc="sum").fillna(0)
df["hour_int"] = pd.to_datetime(df["hour"], format="%H:%M", errors='coerce').apply(lambda x: int(x.hour))
```

```
df_heatmap = df.pivot_table(index="date",values="price",columns="hour", aggfunc="sum").fillna(0)
```

```
trace_heatmap = go.Heatmap(                 x = df_heatmap.columns,                  y = df_heatmap.index,                  z = [df_heatmap.iloc[0], df_heatmap.iloc[1], df_heatmap.iloc[2]]                )
```

```
data = [trace_heatmap]
```

```
layout = go.Layout(title="Purchases by place", showlegend=True)
```

```
figure = go.Figure(data=data, layout=layout)
```

```
offline.plot(figure)
```

![Image](https://cdn-media-1.freecodecamp.org/images/G7TnpLRmkUsTxI4HbpPzePIiU7QFcNDip2tX)
_Quand j'ai dépensé mon argent (nous devrons changer cette échelle de couleurs haha)_

#### Quels concerts ai-je regardés ?

Passons maintenant à la partie la plus cool : pourrais-je deviner les concerts auxquels j'ai assisté en me basant uniquement sur mes achats ?

Idéalement, lorsque nous regardons un spectacle, nous **regardons** le spectacle (et non en train d'acheter des choses), donc les achats devraient être faits **avant** ou **après** chaque concert. J'ai ensuite fait une liste de chaque concert ayant lieu une heure avant, une heure après, et selon l'heure à laquelle l'achat a été fait.

Pour découvrir à quels spectacles j'ai assisté, j'ai calculé la distance entre le lieu de l'achat et chaque scène. Les spectacles auxquels j'ai assisté devraient être ceux avec la distance la plus courte par rapport aux stands.

Comme nous voulons montrer chaque point de données, le meilleur choix pour une visualisation est un tableau. Construisons-en un :

```
import plotly.graph_objs as go
import plotly.offline as offline
import pandas as pd
```

```
df_table = pd.read_csv("concerts_I_attended.csv")
```

```
def colorFont(x):    if x == "Yes":       return "rgb(0,0,9)"    else:       return "rgb(178,178,178)"
```

```
df_table["color"] = df_table["correct"].apply(lambda x: colorFont(x))
```

```
trace_table = go.Table(      header=dict(          values=["Concert","Date","Correct?"],          fill=dict(            color=("rgb(82,187,47)"))          ),          cells=dict(          values= [df_table.concert,df_table.date,df_table.correct],          font=dict(color=([df_table.color])))      )
```

```
data = [trace_table]
```

```
figure = go.Figure(data = data)
```

```
offline.plot(figure)
```

![Image](https://cdn-media-1.freecodecamp.org/images/5hBhtw5LGupq5nBxUhBCpX27w4cS6JNB0ziW)
_À quoi ressemble le tableau_

Trois concerts étaient manquants et quatre étaient incorrects, ce qui nous donne une précision de 67 % et un rappel de 72 %.

### Tout rassembler : Dash

Nous avons tous les graphiques, mais l'objectif est de les rassembler sur une page. Pour cela, nous allons utiliser [Dash](https://plot.ly/products/dash/) (par Plotly).

> « Dash est un framework Python pour construire des applications web analytiques. Pas besoin de JavaScript. Dash est idéal pour construire des applications de visualisation de données avec des interfaces utilisateur hautement personnalisées en Python pur. Il est particulièrement adapté à toute personne qui travaille avec des données en Python. » — Site de Plotly

Dash est écrit sur Flask, Plotly.js et React.js. Il fonctionne de manière très similaire à la façon dont nous créons des graphiques Plotly :

```
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
app = dash.Dash()
```

```
df_table = pd.read_csv("concerts_I_attended.csv").dropna(subset=["concert"])
def colorFont(x):    if x == "Yes":       return "rgb(0,0,9)"    else:       return "rgb(178,178,178)"
```

```
df_table["color"] = df_table["correct"].apply(lambda x: colorFont(x))
```

```
trace_table = go.Table(header=dict(values=["Concert","Date","Correct?"],fill=dict(color=("rgb(82,187,47)"))),cells=dict(values=[df_table.concert,df_table.date,df_table.correct],font=dict(color=([df_table.color]))))
```

```
data_table = [trace_table]
```

```
app.layout = html.Div(children=[    html.Div(        [            dcc.Markdown(                """                ## Mon expérience à Lollapalooza Brésil 2018                ***                """.replace('  ', ''),                className='eight columns offset-by-two'            )        ],        className='row',        style=dict(textAlign="center",marginBottom="15px")    ),
```

```
html.Div([        html.Div([            html.H5('Quels concerts ai-je regardés ?', style=dict(textAlign="center")),            html.Div('Les gens achètent généralement des choses avant ou après un concert, alors j'ai pris la liste des concerts, obtenu les distances entre le lieu des achats et les scènes et essayé de deviner à quels concerts j'ai assisté. 8 concerts étaient corrects et 3 manquaient sur un total de 12 concerts.', style=dict(textAlign="center")),            dcc.Graph(id='table', figure=go.Figure(data=data_table,layout=go.Layout(margin=dict(t=30)))),        ], className="twelve columns"),    ], className="row")])
```

```
app.css.append_css({    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
```

```
if __name__ == '__main__':    app.run_server(debug=True)
```

![Image](https://cdn-media-1.freecodecamp.org/images/FMIYSv4Jj3oBsqjRu-jM9G9bS2Bt74XlnWik)
_Tout rassembler avec Dash !_

Cool, non ?

J'ai hébergé la visualisation finale [ici](https://dmesquita.pythonanywhere.com/) et [tout le code est ici](https://github.com/dmesquita/dash-lollapalooza-brasil-2018).

Il existe quelques alternatives pour héberger les visualisations : Dash propose un hébergement public d'applications Dash et Plotly fournit également un service web pour héberger des graphiques.

Avez-vous trouvé cet article utile ? Je fais de mon mieux pour écrire un article approfondi chaque mois, vous pouvez [recevoir un e-mail lorsque j'en publie un nouveau](https://goo.gl/forms/SLrJDrGtxgAoILkt1).

J'ai eu une expérience assez positive avec Plotly, je l'utiliserai définitivement pour mon prochain projet. Quels sont vos avis à ce sujet après cet aperçu ? Et quels autres outils utilisez-vous pour créer des visualisations pour le web ? Partagez-les dans les commentaires ! Et merci pour votre lecture ! ?