---
title: Comment créer une feuille de calcul d'actions géniale avec React 16
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-14T19:47:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-awesome-stocks-spreadsheet-with-react-16-f945b3137a42
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AK6DfcdIDmYnEyEAZ9-Ijg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer une feuille de calcul d'actions géniale avec React 16
seo_desc: 'By Sandeep Adwankar

  React 16 is the first version of React built on top of React’s new core architecture,
  codenamed “Fiber”. React 16 is designed from the ground up to support asynchronous
  rendering. This allows processing large component trees witho...'
---

Par Sandeep Adwankar

React 16 est la première version de React construite sur la nouvelle architecture centrale de React, nommée "Fiber". React 16 est conçu dès le départ pour supporter le rendu asynchrone. Cela permet de traiter de grands arbres de composants sans bloquer le thread d'exécution principal.

React 16 est populaire car il supporte un certain nombre de fonctionnalités clés, telles que la capture des exceptions à l'aide de limites d'erreur, le retour de plusieurs composants à partir du rendu, la réduction de la taille des fichiers et son support pour la licence MIT.

Pour construire une application web pilotée par les données comme une feuille de calcul d'actions, vous aurez besoin d'une interface de type feuille de calcul pour afficher les données pour vos utilisateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/sOsMwULzRp-OYDAE4tMHSEbF9Dg8xKpKcBeO)
_Feuille de calcul d'actions_

Vos utilisateurs s'attendront à ce que la feuille de calcul de votre application soit capable de :

* Faire défiler avec un en-tête fixe
* Trier en cliquant sur un en-tête de colonne
* Afficher et masquer des colonnes spécifiques
* Pagination, regroupement et résumé
* Modifier les données dans les cellules
* Exporter vers Excel
* Approfondir/expansion de ligne

Une feuille de calcul ou une grille, cependant, peut être l'un des composants d'interface utilisateur les plus délicats et les plus complexes à construire dans React. Cela est dû au fait que de nombreuses fonctionnalités nécessaires nécessitent à la fois une expertise significative en React, ainsi que la volonté et la capacité de creuser dans le DOM.

Si vous souhaitez coder une grille en utilisant un tableau HTML ou un autre composant tiers, vous devrez implémenter plusieurs fonctionnalités courantes. Ces fonctionnalités incluent le clic sur un en-tête de colonne de grille pour trier ou le clic sur un diviseur entre un en-tête de colonne pour redimensionner, ou le glissement d'un paginateur et la récupération de la page suivante de données.

Pour construire rapidement cette application, nous allons utiliser les composants ExtReact de Sencha. ExtReact de Sencha est un ensemble de composants de 115+ composants d'interface utilisateur pré-construits que vous pouvez facilement intégrer avec les applications React 16. L'un des composants clés dans ExtReact est Grid. Il fournit une fonctionnalité de type feuille de calcul nécessaire pour construire rapidement une application de feuille de calcul d'actions. Nous allons utiliser ExtReact Grid pour afficher des informations sur les actions et les sociétés de capitaux propres.

Commençons à construire une application d'actions en utilisant ExtReact Grid de Sencha.

### Échafaudage de l'application de feuille de calcul d'actions

Pour créer l'échafaudage de l'application, veuillez suivre les étapes ci-dessous :

* **Assurez-vous d'avoir un environnement Node configuré**

Tout d'abord, assurez-vous d'avoir Node 8.11+ et NPM 6+ configurés sur votre système. Vous pouvez télécharger la dernière version de Node depuis le [site web de Node](https://nodejs.org/en/download/). Si vous avez déjà installé Node, vous pouvez facilement vérifier les versions de Node et npm en utilisant ces commandes : _node -v_ et _npm -v_

* **Obtenez vos identifiants de connexion pour le dépôt NPM ExtReact**

Les packages NPM ExtReact sont hébergés sur le dépôt NPM privé de Sencha. Vous vous connectez à ce dépôt une fois pour obtenir l'accès à tous les packages ExtReact. Pour obtenir des identifiants de connexion, allez sur la page [ExtReact 30-Day Free Trial](https://www.sencha.com/products/extreact/evaluate/?utm_source=freecodecamp&utm_medium=advertising&utm_campaign=sncextreact&utm_content=180914-ft-sncextreact) et remplissez le formulaire. Nous vous enverrons un email avec les détails de connexion ainsi que quelques liens vers des ressources telles que la documentation et des projets d'exemple.

* **Connectez-vous au dépôt NPM ExtReact et obtenez le générateur d'applications**

L'étape suivante consiste à vous connecter au dépôt npm privé de Sencha, qui héberge les packages ExtReact. Utilisez votre connexion npm (fournie dans l'email d'essai ExtReact) pour associer le dépôt npm à la portée @sencha, et entrez les identifiants lorsque vous y êtes invité :

```
npm login --registry=http://npm.sencha.com --scope=@sencha
```

L'étape suivante consiste à installer le package générateur ExtReact.

```
npm install -g @sencha/ext-react-gen
```

* **Créez votre première application React**

Exécutez le générateur d'applications ExtReact pour créer votre première application ExtReact :

```
ext-react-gen app votre-nom-d-application-ici -i
```

Le générateur d'applications vous posera quelques questions — comme le nom de votre application. Par défaut, l'application utilise le thème Material (basé sur les [directives de conception Material de Google](https://material.io/guidelines/)) et est un bon choix comme thème de départ.

Sélectionnez « Générer une application vide » dans l'une des invites. Le générateur vous invitera également à créer un nouveau répertoire pour votre projet. Le générateur téléchargera et créera ensuite votre application d'exemple, y compris les dépendances pertinentes.

* **Exécutez votre application React**

Dans la sortie du générateur, vous trouverez les étapes pour exécuter votre application. Changez pour votre nouveau répertoire d'application et exécutez l'application en utilisant :

```
npm start
```

Cela lancera l'application, et votre application React vide apparaîtra simplement avec le titre de l'application. Le composant principal (par exemple, StocksGrid) dans l'application a un conteneur à la racine. Celui-ci est marqué comme plein écran, la disposition est définie pour s'adapter, ce qui signifie qu'il étirera son enfant pour le remplir.

[Voir le code jusqu'à cette étape](https://github.com/adwankar/react16-stocks-grid/tree/empty-extreact-app) sur GitHub.

### Ajout de la grille d'actions à l'application

#### **Ajout des données d'actions**

Nous allons ajouter un ensemble de données d'exemple de 10 000 lignes, appelé stocks.json à l'application. Chaque ligne de données contient le nom de l'entreprise, le symbole boursier, le secteur et les industries dans lesquelles elles se trouvent. La ligne contient également un tableau de _ticks_ qui sont les 5 dernières ventes de cette action.

Ce sont les données que nous allons afficher dans notre grille. Dans ce tutoriel, nous allons charger les données de manière statique à partir de stocks.json, mais vous pouvez également construire une API REST back-end pour obtenir les mêmes données.

#### **Création d'une grille de base**

Dans le composant React StockGrid, dans la méthode render, nous allons retourner une grille avec des colonnes.

Pour ajouter des colonnes dans notre grille, nous utilisons un composant Column. Le composant Column prend un index de données qui est le même que le champ de nom des données des actions. Le Column prend une prop text qui est le texte de l'en-tête de colonne. Nous pouvons également donner à la Column une largeur, comme une largeur fixe ou un flex ou une combinaison de flex et de minimum ou de maximum également. Nous allons ajouter des composants de colonne pour le nom de l'entreprise, le symbole, les ticks, le secteur et l'industrie. Cela créera une nouvelle classe StocksGrid avec Grid comme montré ci-dessous

```
<Grid >       <Column dataIndex="name" text="Nom" width={300} />       <Column dataIndex="symbol" text="Symbole" />       <Column dataIndex="ticks" text="Tendance" />       <Column dataIndex="sector" text="Secteur" width={200} />       <Column dataIndex="industry" text="Industrie" width={350} /></Grid>
```

Votre application retournera StockGrid comme partie du rendu comme ci-dessous :

```
export default class App extends Component {
```

```
   render() {        return (            <ExtReact>                <StocksGrid />            </ExtReact>            )    }}
```

[Voir le code jusqu'à cette étape](https://github.com/adwankar/react16-stocks-grid/tree/adding-stocks-grid-component-6.6) sur GitHub.

En exécutant, vous pourrez voir l'application web avec une grille vide sur _npm start_

### Liaison des données d'actions avec la grille

Une grille ExtReact est un tableau de type feuille de calcul qui extrait et rend les données d'un magasin de données. Dans ExtReact, Store est une structure de données qui vous permet de trier et de filtrer les données dans une grille.

Nous pouvons maintenant commencer par charger les données des actions et créer un magasin. Les grilles extrairont leurs données du Store. Les interactions avec la grille déclencheront des événements sur le Store, comme le rechargement ou le tri ou la pagination.

Le concept de magasin de données ExtReact est un peu différent du magasin Flux. Ce qui rend la grille et le magasin un peu différents de l'approche React standard, c'est que les deux sont étroitement intégrés. Typiquement, vous pouvez passer des données directement à un Store, ou un Store peut extraire des données par lui-même d'un back-end en utilisant un Proxy. La grille ExtReact fournit une fonctionnalité interactive comme le filtrage, le tri, la pagination, le regroupement et la synthèse sans aucun code supplémentaire.

Pour cet exemple, nous passons les données directement au magasin à partir du fichier de données Stocks. Alternativement, vous pouvez créer un magasin avec une configuration de proxy — avoir un proxy nous permet de faire toutes sortes de grandes choses comme la pagination à distance, le filtrage et le tri. Pour cette application, nous définissons autoload sur true, donc il charge automatiquement les données dans la grille. Les données brutes ne sont pas particulièrement triées selon un critère, donc nous allons les trier côté client en spécifiant la propriété name.

```
this.store =        new Ext.data.Store({            data: stocks,            autoLoad: true,            sorters: [{                property: 'name'            }],            listeners: {                update: this.onRecordUpdated            }})
```

Dans la grille, attribuez la configuration du magasin au magasin que nous avons créé.

```
<Grid store={this.store}>
```

```
       ...</Grid>
```

Maintenant, en exécutant _npm start_, notre application a une grille avec toutes les données comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/tKgjkb2j9G5QRJgARyZgagZBCdI1nJLZGdoP)
_Grille de base avec données_

Avec ce simple code React, vous obtenez beaucoup de fonctionnalités gratuitement. Ces fonctionnalités incluent le tri, qui vous permet de cliquer sur n'importe quel en-tête de colonne et il trie automatiquement côté client. Si nous implémentions une vraie API back-end, nous pourrions configurer le Proxy Store pour faire un tri à distance sur le back-end et utiliser une clause "order by" dans la base de données pour faire un tri. ExtReact Grid fournit également des colonnes redimensionnables gratuitement. Ainsi, l'utilisateur peut faire glisser la colonne de côté à côté.

ExtReact Grid fournit également une fonctionnalité de regroupement agréable. Votre utilisateur d'application peut regrouper par industrie, et l'application regroupera toutes les données par industrie. ExtReact Grid vous donnera un en-tête épinglé lorsque vous ferez défiler vers le bas pour chacun des regroupements.

![Image](https://cdn-media-1.freecodecamp.org/images/XmuNfIYeVCiAAnMmZypdGekVKLOJohV7ZPR9)
_Regroupement par industrie_

Lorsque vous exécutez votre application, vous remarquerez que ces données se rendent assez rapidement pour 10 000 enregistrements. La raison pour laquelle cela se rend si rapidement est qu'il utilise ce que nous appelons le _rendu tampon_. Avec le _rendu tampon_, lors du chargement initial, la grille rend les données qui sont un peu plus que ce que vous voyez réellement en termes de « hauteur du port de vue ». Lorsque vous faites défiler vers le bas, elle remplace en fait le contenu des cellules de la grille avec les nouveaux enregistrements lorsque vous faites défiler les pages dans le magasin. Ainsi, la grille conserve en fait les éléments DOM autant que possible. En gardant le DOM petit, il garde la consommation de mémoire faible et assure des performances élevées de l'application.

[Voir le code jusqu'à cette étape](https://github.com/adwankar/react16-stocks-grid/tree/adding-stocks-store-6.6) sur GitHub.

### **Stylisation de votre grille d'actions**

Vous souhaitez styliser la grille, afin que les données soient plus faciles à analyser.

#### **Utilisation de la prop Cellule de la grille**

Examinons le contrôle du style des cellules de la grille. Nous voulons rendre le nom en gras — la meilleure façon de faire cela est d'utiliser la prop cellule. La cellule de la grille prend un certain nombre de configurations qui contrôlent l'apparence de la cellule. Nous allons ajouter une configuration de style, puis nous allons dire que le poids de la police est égal à gras.

```
cell={ { style: {fontWeight:'bold'}}}
```

#### **Ajout d'un bouton dans une ligne**

Maintenant, disons que nous voulons avoir un bouton que nous pouvons cliquer pour acheter l'une de ces actions. Pour ce faire, nous pouvons ajouter une colonne avec un bouton. Cette fois, nous n'allons pas ajouter un index de données car il ne correspond à aucun champ dans le Store. Nous allons ajouter un WidgetCell avec un Button. Nous allons faire un peu de style — nous allons mettre une interface utilisateur ronde d'action, donc le bouton aura une apparence ronde d'action comme ci-dessous :

```
<Column >    <WidgetCell>        <Button ui ="round action"                 handler = {this.buyHandler}                  text = "Acheter"/>    </WidgetCell></Column>
```

Le gestionnaire d'achat que nous allons utiliser est très simple. Lorsque vous cliquez sur le bouton d'achat, nous allons simplement afficher un petit message qui indique le symbole de l'action que vous achetez. Lorsque vous cliquez dessus, il va appeler cette fonction :

```
buyHandler = (button) => {      let gridrow = button.up('gridrow'),      record = gridrow.getRecord();      Ext.toast(`Acheter ${record.get('name')}`)}
```

![Image](https://cdn-media-1.freecodecamp.org/images/2xNENu00B48uW-DSzPjjcsrOlG-ryTuembWZ)
_Ajout d'un bouton dans une grille_

Comme vous pouvez le voir dans cet exemple, vous pouvez essentiellement intégrer n'importe quel composant ExtReact dans une cellule de grille ExtReact, et il est entièrement interactif.

[Voir le code jusqu'à cette étape](https://github.com/adwankar/react16-stocks-grid/tree/adding-stocks-grid-component-6.6) sur GitHub

### Ajout d'un graphique Sparkline de tendances à la grille d'actions

Dans les données d'actions, nous avons un tableau de ticks sur les cinq dernières ventes d'actions. Intégrons cela sous forme de graphique Sparkline à l'intérieur de la grille. Encore une fois, nous allons utiliser Widgetcell pour rendre le composant ExtReact à l'intérieur d'une cellule de grille.

```
<Column dataIndex="ticks"         text="Tendance"         sortable={false}         cell = { {                xtype: 'widgetcell',               forceWidth: true,               widget: {                        xtype: 'sparklineline',                        tipTpl:                        'Prix : {y:number("0.00")}'               }        } }/>
```

Lorsque vous exécutez votre application avec _npm start_, utilisez votre souris pour survoler différents points dans le graphique sparkline, il affichera la valeur Y formatée avec deux décimales.

![Image](https://cdn-media-1.freecodecamp.org/images/YryHE9CDxi45TvsePo3BddZMCxxS-A2aWo3B)
_Graphique de tendances dans une grille_

[Voir le code jusqu'à cette étape](https://github.com/adwankar/react16-stocks-grid/tree/adding-sparkline-chart-6.6) sur GitHub.

### Exportation des données d'actions vers Excel

Comme pour toute application intensive en données, nous voulons la capacité d'exporter les données vers Excel. Pour ajouter cette capacité, nous allons ajouter gridexporter aux props de plugins à une grille comme montré :

```
<Grid      ..      plugins={{            gridexporter: true,      }}>
```

Nous allons ajouter quelques composants supplémentaires à l'application pour faciliter l'appel de la fonctionnalité d'exportation. Nous allons ajouter une barre de titre et docker la barre de titre en haut de la grille et y mettre un menu. Lorsque vous cliquez sur le bouton « exporter », vous aurez l'option d'exporter soit vers Excel soit vers CSV.

```
<TitleBar docked="top" title="Actions">           <Button align="right" text="Exporter">                    <Menu indented={false}>                           <MenuItem text="Excel"                                 handler=                               {this.export.bind(this, 'excel07')}/>                            <MenuItem text="CSV"                                  handler=                                  {this.export.bind(this, 'csv')}/>                     </Menu>            </Button></TitleBar>
```

Le gestionnaire d'exportation transmettra le type d'exportation et l'extension du nom de fichier comme montré :

```
export = (type) => {            this.grid.cmp.saveDocumentAs(           { type, title: 'Actions' });}
```

Vous devrez passer l'exportateur dans les dépendances du package.json comme montré :

```
"@sencha/ext-exporter": "~6.6.0"
```

Vous devrez installer la dépendance avec _npm install_ puis _npm start_ pour exécuter l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/2P5JfBKrfGAjSiYK2fcWAh5q-mrKjVAY9Pdd)
_Exportation des données de la grille_

Le plugin Exporter permet l'exportation de données vers divers formats de fichiers. Il supporte les formats XSLX natifs, Excel XML ainsi que HTML et CSV/TSV (valeurs séparées par des virgules/tabulations).

[Voir le code jusqu'à cette étape](https://github.com/adwankar/react16-stocks-grid/tree/adding-exporter-6.6) sur GitHub.

### Ajout d'une capacité d'édition à une grille d'actions

La feuille de calcul nécessite la capacité de modifier les données. Pour ajouter cette capacité, nous devons ajouter un autre plugin de grille appelé gridcellediting. En ajoutant ce plugin et en marquant les colonnes comme éditables, vous avez maintenant une feuille de calcul qui peut être modifiée en double-cliquant sur n'importe quelle cellule de la grille. Vous pouvez continuer à modifier la grille en tabulant à travers les cellules de la grille.

Ajoutez le plugin d'édition de cellule de grille avec _gridcellediting: true_ et rendez le « Nom » éditable dans la colonne de la grille comme montré :

```
<Column        dataIndex="name"        text="Nom"        width={300}        cell={ { style: {fontWeight:'bold'}}}        editable/>
```

Lorsque vous exécutez votre application avec _npm start_, vous pourrez maintenant modifier les cellules de la grille.

![Image](https://cdn-media-1.freecodecamp.org/images/5l9b0vUDDMx6spxsIIVHQRryUU89eFsJ4EaQ)
_Capacité d'édition dans une grille_

#### **Gestion des événements d'édition**

Après avoir modifié la cellule de la grille, vous devrez écouter cet événement sur le magasin pour les changements de données. Vous faites cela en ajoutant une configuration d'écouteur et un écouteur pour l'événement « update ». L'événement de mise à jour passera un certain nombre de paramètres, y compris le magasin, l'enregistrement mis à jour, l'objet qui décrit l'opération qui s'est produite, puis passera un tableau de noms de champs modifiés. Vous ajouterez cela dans le gestionnaire.

Dans cette application, nous affichons simplement un message toast. Dans une application réelle, vous appliqueriez en fait une logique métier telle que la persistance des changements dans la base de données.

```
...
```

```
listeners: {            update: this.onRecordUpdated }
```

```
...
```

```
onRecordUpdated = (store, record, operation, modifiedFieldNames) => {      const field = modifiedFieldNames[0];      Ext.toast(`${record.get('name')}                  ${field} mis à jour à  ${record.get(field)}`) }
```

#### **Ajout d'une option de sélection à une cellule de grille**

Si vous souhaitez ajouter une option « Sélectionner » à une cellule de grille, vous pouvez le faire en utilisant un autre composant ExtReact appelé SelectField. Vous ajoutez simplement le composant ExtReact SelectField dans la colonne requise.

```
<Column dataIndex="sector" text="Secteur" width={200} editable>         <SelectField options={sectors}/></Column>
```

Lorsque vous exécutez votre application avec _npm start_, vous pourrez maintenant voir les options de sélection comme montré :

![Image](https://cdn-media-1.freecodecamp.org/images/ttfWeJagFIacxsRk63TrcVdiecmSSlxRHAp9)
_Ajout d'une option de sélection à la grille_

[Voir le code jusqu'à cette étape](https://github.com/adwankar/react16-stocks-grid/tree/adding-grid-editing-6.6) sur GitHub.

### Optimisation de la feuille de calcul d'actions pour l'expérience mobile

Cette application fonctionne bien pour l'expérience de bureau, mais vous pouvez vouloir fournir une expérience optimisée lorsque vous utilisez la même application sur le navigateur de téléphone mobile. Pour cette application, l'édition des cellules peut ne pas être la meilleure expérience pour l'édition sur petit écran de téléphone mobile. Pour les appareils à petit écran, vous pouvez vouloir choisir un style d'édition différent.

L'option _platformconfig_ de ExtReact vous permet de spécifier un comportement pour le bureau ou le mobile. Vous pouvez définir n'importe quelle prop à une valeur différente basée sur _platformConfig_ et ici nous définissons le plugin basé sur la plateforme. Dans cet exemple, nous allons utiliser _gridcellediting_ lorsque l'application est sur le bureau. Lorsque l'application est sur mobile, nous allons utiliser _grideditable_ qui fournit un meilleur moyen d'éditer les données sur les appareils mobiles comme montré :

```
platformConfig= {{                desktop: {                        plugins: {                            gridexporter: true,                            gridcellediting: true                        }                },                '!desktop': {                        plugins: {                            gridexporter: true,                            grideditable: true                        }                }}}
```

Lorsque vous exécutez votre application avec _npm start_, vous pourrez maintenant voir la vue mobile comme montré :

![Image](https://cdn-media-1.freecodecamp.org/images/6oo5ww0cXrXu-scyA5PQok1jEKQNnMvCjgDG)
_Application d'actions sur un appareil mobile_

[Voir le code jusqu'à cette étape](https://github.com/adwankar/react16-stocks-grid) sur GitHub.

### Résumé

Cette application de feuille de calcul d'actions montre à quel point il est facile de créer une interface de type feuille de calcul dans votre application web pilotée par les données en utilisant React 16 et Sencha ExtReact. Vous pouvez voir l'application complète en cours d'exécution dans [Sencha Fiddle](https://fiddle.sencha.com/?extreact#view/editor&fiddle/2l0s).