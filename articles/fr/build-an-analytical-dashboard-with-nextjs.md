---
title: Comment créer un tableau de bord analytique avec Next.js
subtitle: ''
author: Stefan Muzyka
co_authors: []
series: null
date: '2025-02-05T18:13:18.449Z'
originalURL: https://freecodecamp.org/news/build-an-analytical-dashboard-with-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738347998117/46877c78-f5e5-4a94-954e-029b73b8f952.png
tags:
- name: flexmonster
  slug: flexmonster
- name: Next.js
  slug: nextjs
- name: dashboard
  slug: dashboard
- name: analytics
  slug: analytics
- name: highcharts
  slug: highcharts
seo_title: Comment créer un tableau de bord analytique avec Next.js
seo_desc: 'If you work with data or plan to in the future, at some point you''ll likely
  need to build a comprehensive analytics dashboard.

  Sharing data through charts is a great way to provide others with a clearer understanding
  of this information. Pairing it w...'
---

Si vous travaillez avec des données ou prévoyez de le faire à l'avenir, à un moment donné, vous devrez probablement créer un tableau de bord analytique complet.

Partager des données à travers des graphiques est un excellent moyen de fournir aux autres une compréhension plus claire de ces informations. L'associer à un tableau croisé dynamique est également une approche intelligente, vous permettant de visualiser vos données sous différents angles. Et que se passerait-il si vous pouviez également agréger des données et personnaliser des graphiques pour répondre à vos besoins ?

Dans ce guide, j'ai consolidé mes connaissances sur la création d'un tableau de bord analytique dans Next.js en utilisant Flexmonster et Highcharts. Pour le rendre engageant, nous explorerons certains résultats intéressants d'une enquête sur l'étiquette des passagers en vol. J'espère que vous le trouverez utile. C'est parti !

## **Table des matières**

* [Prérequis](#heading-prerequisites)
    
* [Le domaine du sujet](#heading-the-subject-area)
    
* [Le tableau de bord final](#heading-the-final-dashboard)
    
* [Comment configurer Highcharts et Flexmonster pour notre application Next.js](#heading-how-to-configure-highcharts-and-flexmonster-for-our-next-js-app)
    
* [Comment configurer le tableau de bord](#heading-installation)
    
* [Comment configurer la configuration des graphiques](#heading-how-to-set-up-the-chart-configuration)
    
* [Remplir le tableau de bord avec d'autres graphiques](#heading-filling-up-the-dashboard-with-other-charts)
    
* [Connexion entre Flexmonster et Highcharts](#heading-connect-between-flexmonster-and-highcharts)
    
* [Lien vers la démonstration complète](#heading-full-demo-link)
    
* [Conclusion](#heading-wrapping-up)
    

## Prérequis

1. Installer Next.js (guide d'installation [ici](https://nextjs.org/docs/app/getting-started/installation))
    
2. Dans ce projet, nous utiliserons les bibliothèques `flexmonster`, `react-flexmonster` et `highcharts`.
    

```bash
npm i react flexmonster react-flexmonster highcharts highcharts-react-official
npm i -g flexmonster-cli
```

Ce sont des outils payants pour partager des analyses, mais ils offrent plus d'options pour travailler avec des données et la personnalisation. Vous pouvez également utiliser des alternatives gratuites/open-source comme :

**Bibliothèques de données/analyses :**

* [PivotTable.js](https://github.com/nicolaskruchten/pivottable) — fonctionnalité de tableau croisé dynamique open-source de base
    
* [Orb](https://www.npmjs.com/package/orb) — interface utilisateur de tableau croisé dynamique propre avec un design soigné
    
* [WebDataRocks](https://www.webdatarocks.com/demos/react/pivot-table-demo/) — solution moderne de tableau croisé dynamique gratuite
    

**Graphiques :**

1. [Nivo](https://nivo.rocks/) — graphiques gratuits impressionnants avec la puissance de D3
    
2. [Chart.js](https://www.chartjs.org/) — graphiques canvas simples mais puissants
    
3. [Recharts](https://recharts.org/en-US/) — composants React pour les graphiques D3
    

## **Le domaine du sujet**

Avez-vous déjà été curieux de savoir pourquoi les gens se mettent si en colère dans les avions face au comportement des autres ? Ou peut-être êtes-vous cette personne qui... se comporte mal ? Vous êtes-vous demandé s'il était acceptable de déranger vos voisins à bord, que ce soit pour sortir de votre siège ou pour demander quelque chose ?

Imaginez : vous montez dans un avion avec vos amis, et vous êtes assis séparément, pas tous ensemble. Vous voulez changer de place avec quelqu'un pour vous asseoir près les uns des autres. Quelle est la probabilité que la personne à côté de vous considère cela comme impoli ou inacceptable ?

Nous pouvons explorer ces questions à travers une [enquête](https://fivethirtyeight.com/features/airplane-etiquette-recline-seat/) sur l'étiquette des passagers menée par ABC News. Notre objectif est d'examiner les attitudes des passagers envers les interactions en vol et de présenter nos conclusions avec des graphiques et un tableau croisé dynamique. Les données complètes de l'enquête proviennent de [ici](https://github.com/fivethirtyeight/data/tree/master/flying-etiquette-survey).

Dans ce guide, je mettrai en évidence certaines corrélations intrigantes entre différents groupes sociaux et leurs perspectives sur certaines questions, telles que :

* L'impact de l'âge et du revenu sur l'insatisfaction globale.
    
* Quels comportements les passagers considèrent-ils comme les plus impolis ?
    
* Comment voyager avec des enfants affecte-t-il l'expérience de vol ?
    
* Quels groupes sociaux ont tendance à quitter le vol les plus satisfaits ou insatisfaits ?
    
* Qui est plus susceptible de violer les règles de vol ?
    

## **Le tableau de bord final**

Dans ce tutoriel, nous créerons un tableau de bord interactif en utilisant Next.js, présentant un tableau croisé dynamique et plusieurs graphiques sur la page finale.

![Le tableau de bord final](https://cdn.hashnode.com/res/hashnode/image/upload/v1736375903721/ea1faca7-0bf3-4d32-83fc-5963035b832e.png align="center")

### **Outils**

Je cherchais des outils qui offrent une interface utilisateur personnalisable et fonctionnelle, une large gamme de types de graphiques et des fonctionnalités de tableau croisé dynamique. J'ai donc choisi [Flexmonster](https://www.flexmonster.com/) pour créer des tableaux et [Highcharts](https://www.highcharts.com/) pour les graphiques. Ces outils offrent des interfaces conviviales, des options de personnalisation étendues, gèrent de grands ensembles de données et s'intègrent bien ensemble.

Maintenant, plongeons dans le processus d'intégration.

## **Comment configurer Highcharts et Flexmonster pour notre application Next.js**

Pour créer le tableau de bord analytique, vous devrez installer les bibliothèques et configurer votre projet.


### 1\. Définir le projet Next.js :

```bash
npx create-next-app flexmonster-project --ts --app
cd flexmonster-project
```

### 2\. Obtenir le wrapper Flexmonster pour React :

```bash
flexmonster add react-flexmonster
```

Les bibliothèques sont maintenant installées ! Passons à l'étape suivante, en les intégrant dans le projet.

### 3\. Importer les styles Flexmonster dans `global.css` :

```bash
@import "flexmonster/flexmonster.css";
```

### 4\. Créer le wrapper

Vous allez maintenant créer le wrapper pour votre futur tableau croisé dynamique qui intègre Flexmonster et Highcharts. Commencez par créer un fichier `PivotWrapper.tsx`.

```typescript
'use client'
import * as React from 'react';
import * as FlexmonsterReact from "react-flexmonster";
import Flexmonster from 'flexmonster';
import "flexmonster/lib/flexmonster.highcharts.js";


// prendre les paramètres généraux de Flexmonster et certains spéciaux pour Next.js
type PivotProps = Flexmonster.Params & {
    pivotRef?: React.ForwardedRef<FlexmonsterReact.Pivot>;
  }
 
// pivotRef fournit une référence à l'instance Flexmonster pour accéder à l'API Flexmonster.
const PivotWrapper: React.FC<PivotProps> = ({ pivotRef, ...params}) => {
    return (
        <FlexmonsterReact.Pivot
            {...params}
            ref={pivotRef}
        />
    )
}

export default PivotWrapper;
```

### 5\. Importer le wrapper

Maintenant, importez le wrapper dans le fichier `analytical-dashboard/page.tsx`. Vous pouvez changer le nom de la route `analytical-dashboard` selon vos préférences :

```typescript
"use client"
import * as React from "react";
import type { Pivot } from "react-flexmonster";
import dynamic from "next/dynamic";
import * as Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';


// Charger le wrapper dynamiquement
const PivotWrap = dynamic(() => import('@/app/PivotWrapper'), {
    ssr: false,
    loading: () => <h1>Chargement de Flexmonster...</h1>
});


const ForwardRefPivot = React.forwardRef<Pivot, Flexmonster.Params>((props, ref?: React.ForwardedRef<Pivot>) =>
    <PivotWrap {...props} pivotRef={ref} />

)

ForwardRefPivot.displayName = 'ForwardRefPivot';
```

Au fait, Flexmonster prend en charge le chargement dynamique pour ses tableaux, ce qui offre une expérience fluide lors de l'extraction de grandes quantités de données.


### 6\. Placer votre wrapper de tableau croisé dynamique et les graphiques dans le tableau de bord.

Définissons une fonction `WithHighcharts()` pour rendre notre tableau de bord et travailler avec ses parties essentielles. Tout d'abord, nous initialiserons l'objet [ref](https://react.dev/reference/react/useRef) pour le tableau croisé dynamique afin d'y accéder et à ses événements. Les graphiques seront créés dans la fonction `createChart()`, qui s'exécute lorsque les données du tableau croisé dynamique sont chargées (dans l'événement `reportComplete`). Enfin, nous retournerons la fonction `layout`.

Ajoutez le code ci-dessous au fichier `analytical-dashboard/page.tsx` :

```typescript

export default function WithHighcharts() {
    const pivotRef: React.RefObject<Pivot> = React.useRef<Pivot>(null);

    const reportComplete = () => {
        pivotRef.current!.flexmonster.off("reportComplete", reportComplete);
        createChart();
    }

    // définir et créer des graphiques sur la page. Appelé lorsque le chargement des données est terminé avec succès
    const createChart = () => {
        // ici nous placerons le rendu des graphiques plus tard
    }

    return (
        <div className="App">
            <div id="pivot-container" className="">
              <ForwardRefPivot
                ref={pivotRef}
                toolbar={true}
                beforetoolbarcreated={toolbar => {
                  toolbar.showShareReportTab = true;
                }}
                shareReportConnection={{
                  url: "https://olap.flexmonster.com:9500"
                }}
                width="100%"
                height={600}
                report = {{
                  dataSource: {
                    type: "csv",
                    // se connecter à notre ensemble de données
                    filename: "https://query.data.world/s/vvjzn4x5anbdunavdn6lpu6tp2sq3m?dws=00000"
                  }
                }}
                reportcomplete={reportComplete}
                // votre clé de licence
                licenseKey="XXXX-XXXX-XXXX-XXXX-XXXX"
              />
          </div>

          // ici nous placerons les dispositions des graphiques
    )
}
```

### 7\. Exécuter l'application :

```bash
npm run build
npm start
```

Si vous êtes intéressé par une intégration détaillée de Flexmonster avec [Next.js](https://www.flexmonster.com/doc/integration-with-next-js/) et [Highcharts](https://www.flexmonster.com/doc/integration-with-highcharts/), vous pouvez consulter la documentation complète que j'ai liée ici.

Pour l'instant, nous avons configuré un tableau de bord vide prêt à être rempli avec des données. Dans la section suivante, je vous guiderai à travers le processus de définition globale des graphiques et je mettrai en évidence quelques considérations clés.

Tout d'abord, vous devrez vous assurer que vos graphiques se mettent à jour en fonction des filtres appliqués à la grille. Pour cela, vous devez ajouter le code suivant :

```typescript
 React.useEffect(() => {
    if (pivotRef.current) {
        const pivot = pivotRef.current.flexmonster;

        // Déclencher la mise à jour du graphique lorsque les données changent
        pivot.on('dataChanged', createChart);
        pivot.on('filterclose', createChart);


        return () => {
          pivot.off('dataChanged', createChart);
          pivot.off('filterclose', createChart);
        }
    }
}, [pivotRef]);
```

Dans ce cas, Next.js suit l'événement [`filterClose`](https://www.flexmonster.com/api/filterclose/?r=stfc2) et déclenche la fonction `createChart()`, qui met à jour les graphiques. Malheureusement, il n'y a pas d'événement pour les changements de filtre, seulement pour l'ouverture/fermeture de la fenêtre contextuelle de filtre. J'ai donc utilisé l'événement qui se déclenche à la fermeture de la fenêtre contextuelle de filtre, car je l'utilise généralement pour appliquer des filtres. Vous pouvez en savoir plus sur les événements Flexmonster [ici](https://www.flexmonster.com/api/events/?r=stfc2).

## **Comment configurer le tableau de bord**

Pour commencer, familiarisons-nous avec notre tableau croisé dynamique. Les graphiques à venir tireront leurs informations directement de celui-ci, il est donc judicieux de comprendre d'abord comment fonctionne le tableau de bord.

Dans l'étape précédente, nous avons déjà créé une grille par défaut. Si vous l'exécutez maintenant, elle ressemblera à ceci :

![La grille par défaut du tableau croisé dynamique Flexmonster](https://cdn.hashnode.com/res/hashnode/image/upload/v1736375968187/a71c06db-1f6d-4d0a-ad0e-4b4457d5f575.png align="center")

Il affiche simplement certaines données par défaut de l'ensemble de données. Pas mal, mais nous voulons configurer des données plus représentatives et explorer tout le potentiel de Flexmonster.

### **1\. Configurer le tableau croisé dynamique**

Les principaux boutons qui vous permettent de configurer ce qui est affiché dans le tableau et comment sont **Format**, **Paramètres** et **Champs**. Nous commencerons par les Champs.

![GIF : connexion des champs de l'ensemble de données à la grille](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376015936/122a95ed-98aa-4128-9c18-d31e95be4437.gif align="center")

En ouvrant l'onglet Champs, vous pouvez sélectionner les colonnes de votre ensemble de données que vous souhaitez afficher dans le tableau. Que devons-nous choisir ?

Hmm... Il semble intéressant de voir la distribution en pourcentage des répondants de différents âges dans diverses régions. Certaines régions interrogées ont probablement plus de répondants âgés, d'autres plus jeunes, et d'autres encore peuvent avoir un mélange équilibré. Cela concerne davantage l'analyse de la composition de l'enquête elle-même, mais c'est un bon début.

Pour ce faire, sélectionnez les champs nécessaires dans les lignes et les colonnes. Ensuite, choisissez la fonction pour calculer les valeurs finales. Il y a assez d'options, mais nous opterons pour **Pourcentage de colonne**. En conséquence, vous obtiendrez la distribution en pourcentage des répondants de groupes d'âge spécifiques dans chaque région.

Voici le résultat :

![Grille Location et Age avec données brutes](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376040585/181e9f1d-38ed-4731-8700-bbee02a7bbd5.png align="center")

D'accord, nettoyons un peu ce tableau. Nous garderons seulement une décimale, ce que vous pouvez faire dans l'onglet **Format** comme ceci :

![Onglet Format](https://cdn.hashnode.com/res/hashnode/image/upload/v1736378089026/8e853863-86ee-40a8-be66-6fa9c339f164.png align="center")

C'est assez simple : sélectionnez le champ requis (dans ce cas, il n'y en aura qu'un seul) dans le champ **Choisir la valeur** et définissez **Décimales** à 1.

Nous supprimerons également les **Totaux généraux** car ils ne sont pas nécessaires pour nos besoins. Vous pouvez faire cela dans l'onglet **Paramètres** :

![Options de disposition](https://cdn.hashnode.com/res/hashnode/image/upload/v1736378067956/a66dd0f9-0589-473e-b0af-c9c6bfe0d0b1.png align="center")

Enfin, nous voudrons supprimer les réponses vides. C'est une caractéristique de l'ensemble de données sélectionné - certains répondants ont choisi de ne pas répondre à certaines questions, laissant le champ de réponse vide. Pour notre analyse, ces données ne sont pas nécessaires, nous allons donc les filtrer.

![GIF : filtrage des données](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376126270/4bc3f72c-5e68-4e39-b1da-19f179ad2e4f.gif align="center")

Et voici à quoi ressemble le tableau maintenant. Plutôt propre !

### **2\. Mise en forme conditionnelle**

Maintenant, nous voulons configurer la mise en forme conditionnelle pour mettre en évidence les données exceptionnelles. Le tableau est déjà configuré, mais l'ajout d'indices visuels rendra les informations plus faciles à interpréter. Heureusement, Flexmonster prend en charge cette fonctionnalité, alors utilisons-la.

Voici mon idée : nous voulons identifier les zones où la distribution des répondants par âge est inégale. Nous avons quatre tranches d'âge : les jeunes (18-29), les milléniaux (30-44), la génération X (45-59) et les seniors (60+). Dans une distribution équilibrée, chaque groupe d'âge devrait représenter 100/4 = 25 % (avec une marge de ±2÷3 %).

Voici le plan :

* 22-27 % : Distribution moyenne (dans la fourchette).
    
* 17-22 % ou 27-32 % : légèrement sous-représenté ou surreprésenté.
    
* <17 % ou >32 % : fortement sous-représenté ou surreprésenté.
    

Dans l'onglet **Format**, sélectionnez **Mise en forme conditionnelle** et ajoutez des conditions. Définissez la plage avec la valeur à laquelle elle s'applique, et la couleur de surbrillance. En conséquence, vous obtiendrez un tableau qui ressemble à ceci :

![GIF : Mise en forme conditionnelle](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376163028/c7c28901-30b4-49f7-b146-2ed5e6dbfc9f.gif align="center")

Selon le tableau, la plupart des répondants sont d'âge moyen. Dans certains cas, ils représentent la majorité des personnes interrogées de leur région. La distribution la plus déséquilibrée se trouve autour des États du Centre-Sud et de l'Atlantique moyen. Ils sont surreprésentés dans un groupe d'âge et sous-représentés dans d'autres.


Super ! Nous avons exploré le tableau Flexmonster. Au-delà de l'affichage des données, il peut également filtrer les données pour tous nos graphiques à venir. Passons à la configuration des graphiques, et je vous montrerai comment le tableau peut influencer ses données.

## **Comment configurer la configuration des graphiques**

Dans cette section, nous créerons des graphiques en camembert, en barres, en colonnes, en aires et en lignes. Cela semble beaucoup, mais Highcharts propose une large gamme de [types de graphiques](https://www.highcharts.com/docs/chart-and-series-types/chart-types). Vous pouvez également les personnaliser selon vos préférences.

Tout d'abord, nous créerons un [graphique en camembert](https://www.highcharts.com/docs/chart-and-series-types/pie-chart) montrant la distribution des passagers par lieu. Bien qu'un graphique en camembert de base soit généralement un cercle, j'opte pour un graphique en forme de donut. Cet exemple démontre le processus de configuration commun des graphiques. Pour les autres graphiques, modifiez simplement le type de graphique, les lignes et les mesures. Vous pouvez également jouer avec les champs de l'ensemble de données et les types de graphiques selon vos préférences.

### **1\. Insérer Highcharts dans la page.**

Tout d'abord, descendez jusqu'à la section `return()`. En bas, laissez un espace libre pour les dispositions des graphiques. Ici, nous insérerons le premier bloc `<div>` pour stocker le futur graphique en camembert. Comme il s'agit de l'étiquette des passagers à bord, attribuons-lui un identifiant `chart-location-distribution` :


```typescript
<div className="chart-item">


<h2>Distribution par lieu</h2>


<div id="chart-location-distribution"></div>
</div>
```

### **2\. Définir les options du graphique.**


Passons à la fonction `createChart()`. Pour l'instant, elle est vide. Pour définir le graphique, collez [`pivotRef.current!.flexmonster.highcharts?.getData()`](https://www.flexmonster.com/doc/integration-with-highcharts/?r=stfc2) à l'intérieur. Il obtient trois paramètres : `options du graphique`, `gestionnaire de rappel` et `gestionnaire de mise à jour`.

```typescript
pivotRef.current!.flexmonster.highcharts?.getData(
    // obtenir la tranche actuelle des données de la grille pour appliquer les filtres au graphique
    const gridSlice = pivotRef.current!.flexmonster.getReport()?.slice as Flexmonster.Slice
        {
            type: 'pie',
            slice: {
                rows: [{ uniqueName: 'Location (Census Region)', }],
                measures: [
                    {
                        uniqueName: 'RespondentID',
                        aggregation: 'count',
                    },
                ],
                // appliquer les filtres actuels de la grille au graphique
                reportFilters: gridSlice.reportFilters
            },
        },
    // ...
    // dans la section de code suivante, je décris les deux derniers paramètres
    // à suivre
)
```

Puisque nous passons les options du graphique en tant que Flexmonster.Slice de `getReport()`, les données se mettent à jour dynamiquement à partir de la grille. L'objet `Slice` spécifie quel échantillon de données afficher sur le graphique en sélectionnant dans l'ensemble de données. Vous pouvez en savoir plus sur les propriétés des tranches de grille [ici](https://www.flexmonster.com/api/slice-object/).

Vous pouvez personnaliser le graphique en modifiant les propriétés des données à l'intérieur du paramètre `callbackHandler`. Ci-dessous, nous créerons un graphique en donut personnalisé en faisant ceci :

```typescript
pivotRef.current!.flexmonster.highcharts?.getData(
  // ...
  // continuation de la configuration du graphique
  // les options du graphique définies dans la section de code précédente

  (data: any) => {  
        // Définir la configuration du graphique dans l'objet data
        data.chart = {
            type: 'pie',
        };

        data.title = {
            text: 'Réponses agrégées de l\'enquête'
        };

        data.legend = {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom', 
            x: 0,
            y: 10, 
        }

        data.plotOptions = {
            pie: {
                innerSize: '50%',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                },
            },
        };
 
        Highcharts.chart('chart-location-distribution', data);
    },
    (data: any) => {
        Highcharts.chart('chart-location-distribution', data);
    }
)
```

**Note !** Vous devez modifier `data` **avant** qu'il ne soit passé à la fonction `Highcharts.chart()` en tant que paramètre.

### **3\. Graphique en camembert de la distribution par lieu terminé**

Le graphique montre que les passagers les plus courants de cette compagnie aérienne sont des locaux de la région Pacifique, et les passagers les moins courants sont de la région Centre-Sud des États-Unis. C'est assez intéressant. Cela pourrait être dû au fait que la région Pacifique comprend de grandes villes comme San Francisco, Los Angeles, Seattle et Portland, tandis que la région Centre-Sud des États-Unis comprend des États comme le Mississippi et l'Alabama, qui ont des populations et une densité de population plus faibles.

!['Location distribution' pie chart](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376204736/797d7944-cc61-454f-9cbc-f3d9d2d24e43.png align="center")

## **Remplir le tableau de bord avec d'autres graphiques**

Maintenant, créons les graphiques restants en suivant le même processus - en ajustant le `type` de graphique, les options `slice` et les fonctions `callbackHandler` pour chaque diagramme. Vous pouvez trouver la configuration complète de chaque graphique [à la fin du guide](#heading-full-demo-link) sur mon GitHub.

### **1\. Fréquence d'utilisation des compagnies aériennes distribuée par lieux**

Ici, nous pouvons voir avec un [graphique en colonnes empilées](https://www.highcharts.com/docs/chart-and-series-types/column-chart) à quelle fréquence les personnes de différentes régions prennent l'avion.

!['Frequency of using airlines distributed by locations' stacked column chart](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376209953/a1fd26e5-c7eb-4612-a376-dcb61315d61a.png align="center")

Le passager moyen de toutes les régions tend à voler rarement, la plupart volant une fois par an. Globalement, la tendance suggère que les habitudes de vol sont influencées par des facteurs régionaux, les voyages occasionnels étant plus courants que les vols fréquents. Un fait intéressant est que beaucoup des personnes interrogées ici n'ont jamais pris l'avion ! (Comment ont-elles été incluses dans ce sondage ?!)

### **2\. Qui enfreint les règles à bord ?**

!['Frequency of travel to rule violations' bar chart](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376226439/2c8c093e-e4b3-4964-9097-5110b6813f6f.png align="center")

Question délicate, n'est-ce pas ? Nous savons tous que fumer et utiliser des appareils électroniques sont interdits à bord. Mais tout le monde ne suit pas ces règles, et encore moins avouent les enfreindre.

Pourtant, les sondeurs ont réussi à recueillir quelques informations sur les violations des règles. Le [graphique en barres](https://www.highcharts.com/docs/chart-and-series-types/bar-chart) ci-dessus révèle une tendance : les voyageurs fréquents ont tendance à négliger les règles, tandis que ceux qui volent moins souvent sont plus susceptibles de les respecter.

De ma propre expérience, vos premiers vols sont stressants, et vous essayez généralement de ne pas perturber l'équilibre délicat de l'avion. Chaque règle semble cruciale, presque sacrée. Mais les voyageurs réguliers ne semblent pas penser de cette manière.

### **3\. Facilité de communication en fonction de l'âge**

Le [graphique en lignes](https://www.highcharts.com/docs/chart-and-series-types/line-chart) ci-dessous montre que l'âge influence votre facilité de communication avec des inconnus, les personnes d'âge moyen se sentant souvent plus à l'aise pour engager des conversations.

Personnellement, j'apprécie toujours de me lier d'amitié ou de communiquer avec des inconnus, car cela apporte un sentiment de connexion. Mais pour beaucoup de gens, surtout à bord d'un vol, aborder des inconnus peut être difficile, les passagers plus âgés se sentant souvent plus hésitants à engager la conversation.

!['Age and ease of communication' line chart](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376241508/ebe08ce7-bcb9-4e08-8296-2ad4c953c4ac.png align="center")

Les personnes âgées de 30 à 44 ans sont les plus à l'aise pour communiquer avec des inconnus pendant les vols. En revanche, les passagers plus jeunes (moins de 30 ans) et les passagers plus âgés (60 ans et plus) considèrent une communication excessive comme impolie et préfèrent rester entre eux pendant le voyage.

### **4\. Les hommes considèrent-ils que le fait d'amener des enfants à bord est plus impoli que les femmes ?**

Je pensais que les hommes pourraient être plus affectés par les enfants turbulents dans différents espaces, alors j'ai décidé de vérifier cela. La question posée était : « Est-il impoli d'amener des enfants turbulents à bord ? » Les options étaient « Non, pas du tout », « Oui, un peu impoli » et « Oui, c'est impoli ». J'ai donc construit un autre graphique en camembert pour voir la relation.

![Gender distribution of 'Yes, very rude' responses to question: 'Is it rude to bring unruly babies oboard?' pie chart](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376256453/7d8b1e74-6c1a-45b1-8601-84dc4d806382.png align="center")

Presque les deux tiers des hommes ont choisi l'option « Oui, impoli », tandis que moins de femmes ont sélectionné cette réponse.

### **5\. Les exigences des gens envers les autres et eux-mêmes.**

Les gens ont souvent des doubles standards, considérant certains comportements comme impolis lorsqu'ils sont faits par d'autres, mais pas lorsqu'ils s'engagent eux-mêmes dans ces comportements. L'un des problèmes les plus douloureux à bord est le désordre créé par l'inclinaison des sièges, ce qui peut affecter le confort des autres passagers. Cela m'a conduit à rechercher comment les gens se sentent à propos de l'inclinaison des sièges et à quelle fréquence ils pratiquent cette action.

!['Seat recline and seat obligation' stacked column chart](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376314682/b686dc8d-ee38-4e98-b5db-6e8397d9f5c5.png align="center")

Une corrélation intéressante est apparue en deux points clés : les passagers les plus outrés sont souvent ceux qui n'inclinent pas leurs sièges et sont généralement ceux qui ne tolèrent pas que les autres le fassent. De plus, il y a toujours un petit groupe de personnes qui inclinent régulièrement leurs sièges mais sont prêtes à discuter avec les autres de la même action.

### **6\. Quel groupe d'âge a tendance à être outré ?**

Le [graphique en aires](https://www.highcharts.com/docs/chart-and-series-types/area-chart) couvre toutes les questions sur ce que les passagers considèrent comme impoli, nous permettant d'observer comment différents groupes d'âge répondent à diverses situations.


!['Age and 'Yes, it is rude' responds' area chart](https://cdn.hashnode.com/res/hashnode/image/upload/v1736376320810/9a9a31b8-565a-4044-b221-7d40f8fdf32e.gif align="center")

Intéressamment, les réponses les plus outrées concernent les bébés à bord et les personnes qui se réveillent pour se promener dans l'avion. Les jeunes sont les plus outrés par l'inclinaison des sièges, tandis que les passagers âgés de 30 à 44 ans ont tendance à être plus contrariés par les personnes se rendant aux toilettes. Les passagers plus âgés sont également préoccupés par l'inclinaison des sièges.

Les réponses les moins outrées concernent la communication avec les autres et le déplacement vers des sièges non vendus, indiquant que les gadgets n'ont pas complètement volé la valeur de la communication en direct.

J'ai joint des liens vers la documentation Highcharts pour chaque graphique, mais des graphiques supplémentaires sont disponibles. Vous pouvez les inspecter [ici](https://www.highcharts.com/docs/chart-and-series-types/chart-typeshttps://www.highcharts.com/docs/chart-and-series-types/chart-types).

## Comment synchroniser les données entre Flexmonster et Highcharts

Rappelons la section précédente sur la [configuration des options de graphique](#heading-2-define-the-chart-options). Ici, l'ajout du champ `reportFilters` à l'objet slice permet la synchronisation des données entre tous les éléments du tableau de bord, du tableau croisé dynamique aux graphiques.

Pour filtrer les données du tableau de bord, ajoutez des champs aux **Filtres de rapport** dans l'onglet **Champs** et observez les mises à jour des graphiques. Par exemple, le filtrage des valeurs de localisation affecte le graphique en camembert et le graphique en colonnes puisqu'ils utilisent les données de localisation.

Vous pouvez l'essayer en ajoutant d'autres lignes aux Filtres de rapport et influencer directement l'apparence de vos graphiques.

## **Lien vers la démonstration complète**

![](https://noname-hub.com/imgs/final.gif align="center")

Vous pouvez consulter l'application de démonstration complète Next.js et le tableau de bord vous-même [ici](https://github.com/StefanErrorerko/AnalyticalDashboardFlyingEtiquette).

## **Conclusion**

Dans ce tutoriel, nous avons construit un tableau de bord statistique interactif, analysé le sujet et traité l'ensemble de données. En cours de route, nous avons exploré les spécificités de configuration clés des bibliothèques que nous avons utilisées : Highcharts et Flexmonster. Nous avons ensuite rempli le tableau de bord avec des graphiques et démontré comment interagir avec lui efficacement.

J'ai cherché à mettre en évidence un ensemble de données diversifié et engageant pour rendre le processus plus intéressant. J'espère que ce guide servira de ressource utile pour construire des tableaux de bord analytiques dans Next.js. Bonne chance avec vos projets !