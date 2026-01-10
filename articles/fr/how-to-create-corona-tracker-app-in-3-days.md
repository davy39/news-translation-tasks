---
title: Comment j'ai créé une application de suivi du coronavirus en seulement 3 jours
  avec Ionic et Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T20:31:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-corona-tracker-app-in-3-days
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/CoronaSnap3-1.jpg
tags:
- name: Firebase
  slug: firebase
- name: Ionic Framework
  slug: ionic
seo_title: Comment j'ai créé une application de suivi du coronavirus en seulement
  3 jours avec Ionic et Firebase
seo_desc: "By KAPIL RAGHUWANSHI\nI am really fond of Hybrid App technologies – they\
  \ help us achieve so much in a single codebase. Using the Ionic Framework, I developed\
  \ a cross-platform mobile solution for tracking Coronavirus cases in just 3 days.\
  \ \nIn this tuto..."
---

Par KAPIL RAGHUWANSHI

Je suis vraiment passionné par les technologies d'applications hybrides – elles nous aident à accomplir tant de choses avec une seule base de code. En utilisant le Framework Ionic, j'ai développé une solution mobile multiplateforme pour suivre les cas de coronavirus en seulement 3 jours. 

Dans ce tutoriel, nous allons apprendre à développer une **application Android, iOS et Progressive Web App** pour suivre les cas autour de nous avec les dernières nouvelles, l'aide et les sections de feedback. Préparez-vous pour un nouveau voyage de codage ! ?

### Prérequis

Le processus de développement d'applications mobiles hybrides est destiné à tous les types de développeurs, quel que soit leur stack technologique. Puisque nous utiliserons les trois piliers de base du développement Web – **HTML+CSS+JAVASCRIPT** – au cœur, vous pouvez facilement comprendre le processus et les techniques. 

Ainsi, ce tutoriel est pour tout le monde qui a juste une compréhension de base des fondamentaux du Web. Alors, commençons.

## Jour 0 - Idée, Plan et Ingénierie 

### Idée

Initialement, je cherchais les derniers cas de Covid19 autour de moi (en mars 2020). J'ai obtenu plusieurs liens qui avaient peu de différence dans les chiffres. 

Ensuite, j'ai réalisé que les données de [https://github.com/backtrackbaba/covid-ap](https://github.com/backtrackbaba/covid-api)i sont régulièrement mises à jour et plus précises. J'ai décidé de développer une solution mobile universelle, petite et pratique en utilisant les données fournies par **Johns Hopkins University.**

### Plan

J'ai prévu de développer une solution mobile multiplateforme qui pourrait être universellement accessible par tout le monde. J'ai considéré le framework Ionic qui me permettrait de développer une **Android**, iOS & Progressive Web App** **(PWA)****? en écrivant et maintenant une seule base de code. 

Je voulais également montrer les cas de virus COVID19 à travers le monde et les pays individuels à travers diverses illustrations.

### Ingénierie

L'idée était de développer 5 onglets séparés qui seraient en bas de l'application:

1. **Monde** — montrerait le tableau de bord COVID19
2. **Pays** — vous permettrait de sélectionner un pays pour vérifier les cas
3. **Nouvelles** — obtiendrait les dernières nouvelles concernant la pandémie de coronavirus
4. **Directives** — vous permettrait de lire et de regarder tous les avis et directives
5. **Aide** — fournirait de l'aide et des commentaires.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-170.png)
_Photo par [Unsplash](https://unsplash.com/@sctgrhm?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Scott Graham</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### Stack Technologique

J'ai développé plusieurs sites web et applications via Angular et Ionic auparavant. Mais cette fois, je voulais apprendre et utiliser React.js. Les bibliothèques suivantes sont nécessaires à installer en utilisant le gestionnaire de paquets Node (**npm**):

* **React.js** inclut les derniers react-hooks
* **Ionic Framework** (version 4) avec **Capacitor**
* Environnement **Node.js** pour supporter JavaScript et les bibliothèques npm
* Langage **TypeScript** pour écrire le code réel (.tsx files)
* **Chart.js** pour diverses illustrations
* **Firebase** pour héberger le contenu (**Progressive Web App**)

### Outils

* VS Code
* Google Chrome
* Android Studio pour l'application Android
* Xcode pour l'application iOS (Malheureusement seulement disponible sur les ordinateurs Apple)

### Installation & Échafaudage

Nous devons installer et configurer tous les logiciels et frameworks mentionnés ci-dessus. Alors, commençons avec le premier ensemble de commandes terminal (que ce soit sur Mac, Linux ou Windows):

1. Installer ionic avec une portée globale **"npm install -g @ionic/cli native-run cordova-res"**
2. Créer une application react avec Capacitor **"ionic start corona-tracker tabs — type=react — capacitor"**
3. Ajouter les hooks react et les éléments pwa **"npm install @ionic/react-hooks @ionic/pwa-elements"**

Ouvrez le dossier **corona-tracker** dans votre espace de travail par défaut. Vous devriez avoir obtenu tous les fichiers HTML, CSS et .tsx par défaut avec d'autres sous-dossiers dans la séquence appropriée. Maintenant, allez dans votre dossier d'application et exécutez ces 2 commandes

 **cd corona-tracker**
 **ionic serve**

Voilà! ? Votre application Ionic est maintenant en cours d'exécution dans un navigateur web. Cliquez sur l'option localhost dans le terminal pour vérifier. ?Ceci est votre installation et échafaudage de base de l'application. 

Jusqu'à présent, vous devriez exécuter votre application ionic-react dans votre navigateur local. Maintenant, **index.html** et **index.tsx** sont vos premières pages pour les **Single Page Applications (SPAs).**

### Routage de l'application

Ajoutons le routage à notre application qui nous permettra de visiter les 5 onglets différents expliqués ci-dessus. Ouvrez votre fichier **App.tsx** et ajoutez le routeur ci-dessous à l'intérieur de <IonReactRouter></IonReactRouter>

```ts
     <IonTabs>
        <IonRouterOutlet>
          <Route path="/world" component={WorldTab} exact={true} />
          <Route path="/country" component={CountryTab} exact={true} />
          <Route path="/news" component={NewsTab} />
          <Route path="/guidelines" component={GuidelinesTab} />
          <Route path="/help" component={HelpTab} />
          <Route path="/" render={() => <Redirect to="/world" />} exact={true} />
        </IonRouterOutlet>
        <IonTabBar slot="bottom" >
          <IonTabButton tab="WorldTab" href="/world">
            <IonIcon icon={planet} />
            <IonLabel>Monde</IonLabel>
          </IonTabButton>
          <IonTabButton tab="CountryTab" href="/country">
            <IonIcon icon={home} />
            <IonLabel> Pays</IonLabel>
          </IonTabButton>
          <IonTabButton tab="NewsTab" href="/news">
            <IonIcon icon={newspaper} />
            <IonLabel> Nouvelles</IonLabel>
          </IonTabButton>
          <IonTabButton tab="GuidelinesTab" href="/guidelines">
            <IonIcon icon={informationCircleOutline} />
            <IonLabel>Directives</IonLabel>
          </IonTabButton>
          <IonTabButton tab="HelpTab" href="/help">
            <IonIcon icon={call} />
            <IonLabel>Aide</IonLabel>
          </IonTabButton>
        </IonTabBar>
      </IonTabs>
```

Vérifiez votre application dans le navigateur à nouveau, et vous devriez voir tous ces onglets avec leurs pages respectives. Tous les onglets devraient fonctionner correctement avec un routage approprié.

> _Faites-moi savoir _si vous êtes _bloqué avec des problèmes liés à l'installation, aux erreurs de compilation_, _ou aux erreurs d'exécution.__

C'est tout pour le **Jour** 0.?

## Jour 1 - Développement des onglets Tableau de bord COVID19 et Directives de sécurité 

  
Dans cette partie du processus, nous allons développer les onglets **Monde** et **Directives** pour notre application hybride Ionic React. Jusqu'à présent, nous avons fait l'installation et l'échafaudage de base de l'application. Nous avons également ajouté 5 onglets différents à notre application avec le routage.

### Onglet Monde : Design

Construisons maintenant notre page d'accueil, l'onglet **Monde**. J'ai décidé d'avoir 4 sections différentes sur cet onglet d'accueil:

1. 4 boîtes différentes pour montrer les chiffres réels : Total, Actifs, Rétablis et Décès
2. Un graphique en camembert représentant le nombre de cas
3. Diaporamas pour les conseils de santé de base
4. Tous les pays listés avec ces catégories dans l'ordre décroissant.

### Onglet Monde : Données & API

J'ai étudié la source API open-source postman qui contient toutes les interfaces de programmation d'applications (API) liées aux cas de Corona [**https://documenter.getpostman.com/view/2568274/SzS8rjbe?version=latest**](https://documenter.getpostman.com/view/2568274/SzS8rjbe?version=latest)**.** 

Tout d'abord, nous allons consommer l'API [global](https://covidapi.info/api/v1/global) avec la bibliothèque Axios pour obtenir le nombre total de cas dans le monde en utilisant les hooks React useState & useEffect.

```ts
const [data, setData] = useState<IGLobalCount>();
const [showLoading, setShowLoading] = useState(true);
  useEffect(() => {
    const getGlobalData = async () => {
      //dernier compte global
      const result = await axios('https://covidapi.info/api/v1/global');
      // console.log(result);
      setData(result.data);
      setShowLoading(false);
    };
    getGlobalData();
  }, []);
```

Ensuite, définissez les données à l'intérieur de votre bloc de retour en utilisant HTML:

```html
<IonRow class="casesBox">
    <IonCol class="totalCases">Total <AddNumFunc a={confirmed} b={recovered} c={deaths} /></IonCol>
    <IonCol class="confirmedBox">Confirmés {confirmed?.toLocaleString()}</IonCol>
    <IonCol class="recoveredBox">Rétablis {recovered?.toLocaleString()}</IonCol>
    <IonCol class="deathsBox">Décès {deaths?.toLocaleString()}</IonCol>
</IonRow>
```

Maintenant, nous avons les quatre premières boîtes réactives contenant les cas totaux, les cas confirmés, les rétablis et les décès. Installez chart.js dans votre projet en utilisant **npm install react-chartjs-2**. Utilisons les mêmes données pour dessiner un PieChart.

```ts
import axios from 'axios';
import { Pie } from 'react-chartjs-2';

<IonCard class="pieCard">
   <Pie data={GlobalCasesPieChart}
     options={{
       legend: {
         display: true,
         position: 'bottom',
       },
       plugins: {
         datalabels: {
           anchor: 'end',
           clamp: 'true',
           align: 'bottom',
           color: 'black',
           labels: {
             title: {
               font: {
                 weight: 'bold'
               }
             }
           }
         }
       }
    }} />
</IonCard>
```

Maintenant, nous avons 2 des 4 sections dans l'onglet **Monde**. Ensuite, ajoutons un diaporama représentant des conseils de santé généraux.

```ts
<IonSlides class="tipsSlides" options={slideOpts}>
  <IonSlide class="slide">
    Maintenez au moins 1 mètre (3 pieds) de distance entre vous et toute personne qui tousse ou éternue.
  </IonSlide>
  <IonSlide class="slide">
    Nettoyez régulièrement et soigneusement vos mains avec une solution hydroalcoolique ou lavez-les avec du savon et de l'eau.
  </IonSlide>
  <IonSlide class="slide">
    Si vous avez de la fièvre, de la toux et des difficultés à respirer, cherchez des soins médicaux rapidement.
  </IonSlide>
  <IonSlide class="slide">
    Évitez de toucher les yeux, le nez et la bouche. #RestezChezVousRestezEnSécurité
  </IonSlide>
  <IonSlide class="slide">
    L'alerte santé de l'OMS apporte des faits sur le COVID-19 à des milliards de personnes via WhatsApp.
  </IonSlide>
</IonSlides>
```

Maintenant, créons un tableau de données pour tous les pays dans l'ordre décroissant pour représenter tous les types de cas. Encore une fois, nous allons consommer l'API [latest](https://covidapi.info/api/v1/global/latest) avec la bibliothèque Axios pour obtenir le nombre total de cas pour tous les pays du monde en utilisant les hooks React useState & useEffect.

```ts
const [countryWiseData, setCountryWiseData] = useState<ICountry[]>([]);
  useEffect(() => {
    const getGlobalCountryData = async () => {
      //dernier compte global par pays
      const result = await axios('https://covidapi.info/api/v1/global/latest');
      //console.log(result.data.result);
      let sortedResult = result.data.result;
      sortedResult.sort((a: Object, b: Object) => {
        return (Object.values(a)[0].confirmed > Object.values(b)[0].confirmed ? -1 : (Object.values(a)[0].confirmed < Object.values(b)[0].confirmed ? 1 : 0));
      });
      setCountryWiseData(sortedResult);
    };
    getGlobalCountryData();
  }, []);
```

Nous avons terminé le développement de notre onglet d'accueil avec les 4 sections décrites ci-dessus. Vous pouvez les voir ci-dessous:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/CoronaHybridAppSnap1.jpg)
_Onglet Monde — Captures d'écran de l'émulateur en PWA, Android et iOS_

Maintenant, passons au développement de notre prochain onglet — l'onglet **Directives**.

Ceci est juste un onglet informatif et statique pour diverses **conseils** et **directives** donnés par l'OMS et les gouvernements d'État. Nous avons ajouté diverses images et vidéos ici en HTML:

```ts
<IonList>
   <IonCard>
     <iframe title="OMS" width="100%" height="200" src="https://www.youtube.com/embed/5jD2xd3Cv80"
       allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture">
     </iframe>
   </IonCard>
   <IonCard>
     <IonCardHeader>Symptômes</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/Symptoms2.png"></IonImg>
   </IonCard>
   <IonCard>
     <IonCardHeader>Maladies</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/Symptoms.png"></IonImg>
   </IonCard>
   <IonCard>
     <IonCardHeader>Mythes démystifiés</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/Myth.jpeg"></IonImg>
   </IonCard>
   <IonCard>
     <IonCardHeader>Conseils pour distraire le stress</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/Stress.jpg"></IonImg>
   </IonCard>
   <IonCard>
     <IonCardHeader>Restez chez vous</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/SafeHands.jpeg"></IonImg>
   </IonCard>
</IonList>
```

Faites-moi savoir si vous êtes bloqué avec des problèmes liés à l'installation, aux erreurs de compilation ou d'exécution.

C'est tout pour le Jour 1.?

## Jour 2 - Développement des onglets Pays et Nouvelles

Dans cette section, nous allons développer les onglets **Pays** et **Nouvelles** pour notre application hybride Ionic React. Jusqu'à présent, nous avons construit les onglets **Monde** et **Directives** dans notre application ionic react avec le routage de base de l'application.

### Onglet Pays : Design

Construisons maintenant notre deuxième page, l'onglet **Pays**. J'ai décidé d'avoir 4 sections différentes sur ce deuxième onglet:

1. Menu déroulant des pays pour sélectionner le pays de votre choix
2. 4 boîtes différentes pour montrer les chiffres réels : Total, Actifs, Rétablis et Décès dans le pays sélectionné
3. Un graphique en anneau représentant le nombre de cas dans le pays sélectionné
4. Tendance hebdomadaire pour les cas dans le pays sélectionné. 

### Onglet Pays : Données & API

J'ai étudié le lien open-source postman qui contient toutes les interfaces de programmation d'applications (API) liées aux cas de Corona [**https://documenter.getpostman.com/view/2568274/SzS8rjbe?version=latest**](https://documenter.getpostman.com/view/2568274/SzS8rjbe?version=latest)**.** 

Ici, nous allons consommer l'API [country](https://covidapi.info/api/v1/country/) avec la bibliothèque Axios pour obtenir le nombre total dans le pays sélectionné en utilisant les hooks React useState & useEffect.

Nous allons stocker le pays que l'utilisateur a sélectionné dans le stockage local pour que les autres illustrations soient mises à jour.

```ts
import moment from 'moment';
import axios from 'axios';
import { Doughnut, Bar } from 'react-chartjs-2';
 
  const [yourCountry, setYourCountry] = useState<string>('IND');
  Storage.set({ key: 'yourCountry', value: yourCountry });
  const [countryData, setcountryData] = useState<ICountryCount>();
  const [showLoading, setShowLoading] = useState(true);

  useEffect(() => {
    const getCountryData = async () => {
      let result: any = '';
      const { value } = await Storage.get({ key: 'yourCountry' });
      if (value) {
        result = await axios('https://covidapi.info/api/v1/country/' + value + '/latest');
      } else {
        result = await axios('https://covidapi.info/api/v1/country/' + yourCountry + '/latest');
      }
      // console.log(result);
      setcountryData(result.data.result);
      setShowLoading(false);
    };

    getCountryData();
  }, [yourCountry]);
```

Maintenant, consommez l'API pour obtenir les données spécifiques au pays:

```ts
const [countryTimeSeriesData, setcountryTimeSeriesData] = useState<ISeriesCases[]>([]);
  let endDate: string = new Date().toISOString().split('T')[0];
  let todaysDate = new Date();
  let startDate: string = new Date(todaysDate.getTime() - (5 * 24 * 60 * 60 * 1000)).toISOString().split('T')[0];

  useEffect(() => {
    const getCountryTimeSeriesData = async () => {
      const result = await axios('https://covidapi.info/api/v1/country/' + yourCountry + '/timeseries/' + startDate + '/' + endDate);
      // console.log(result);
      setcountryTimeSeriesData(result.data.result);
      setShowLoading(false);
    };

    getCountryTimeSeriesData();
  }, [yourCountry, endDate, startDate]);
```

Maintenant, concevez le graphique en anneau et le graphique à barres de tendance:

```ts

 <IonCard>
    <Doughnut
      data={CountryDoughnutChart}
      options={{
        legend: {
          display: true,
          position: 'right'
        },
        plugins: {
          datalabels: {
            anchor: 'bottom',
            clamp: 'true',
            align: 'end',
            color: 'black',
            labels: {
              title: {
                font: {
                  weight: 'bold',
                  size: 10
                }
              }
            }
          }
        }
    }} />
  </IonCard>
```

```ts
 <Bar
   data={countryBarChart}
   options={{
     scales: {
       xAxes: [{
         stacked: true
       }],
       yAxes: [{
         stacked: true
       }]
     },
     title: {
       display: true,
       text: 'Cas de la semaine en cours',
       fontSize: 15
     },
     legend: {
       display: true,
       position: 'bottom'
     },
     plugins: {
       datalabels: { display: false }
     }
   }}
  />
```

Maintenant, enregistrez le fichier et vérifiez-le dans le navigateur. Donc, finalement, nous devrions obtenir le design ci-dessous:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/CoronaSnap3-2.jpg)
_Onglet Pays — Captures d'écran de l'émulateur en PWA, Android et iOS_

Maintenant, continuons et développons notre troisième onglet — l'onglet **Nouvelles**.

### Onglet Nouvelles : Design

Nous avons ajouté une carte Ionic de base qui contient diverses ressources d'actualités telles que l'URL, le titre, l'image, l'auteur et les détails de l'éditeur:

```ts
<IonList>
   {data.map((news, idx) => (
     <IonItem key={idx}>
       <IonCard>
         <IonImg src={news?.urlToImage} class="newsImage" ></IonImg>
         <IonGrid>
           <IonRow class="newsTitle">{news?.title}</IonRow>
           <IonRow class="newsSource">
             <IonCol>{news?.source?.name}</IonCol>
             <IonCol>{trimSourceDetails(news?.author)}</IonCol>
             {/* <IonCol text-right>{moment(news?.publishedAt).format('DD MMM YYYY')}</IonCol> */}
           </IonRow>
           <IonRow class="newsContent">{news?.description}</IonRow>
         </IonGrid>
       </IonCard>
     </IonItem>
   ))}
</IonList>
```

### Onglet Nouvelles : Données & API

Pour obtenir les nouvelles, j'ai utilisé **Newsapi.org** qui n'est pas une **interface de programmation d'application (API) open-source** ?. Mais avec un compte développeur, j'ai recherché des nouvelles liées au coronavirus. Si vous souhaitez utiliser d'autres API de nouvelles, vous pouvez les utiliser à la place.

Ici, nous allons consommer l'API [top-headlines](https://newsapi.org/v2/top-headlines) avec la bibliothèque Axios pour obtenir le nombre total dans le pays sélectionné en utilisant les hooks React useState & useEffect.

```ts
const [data, setData] = useState<IArticles[]>([]);
  const [showLoading, setShowLoading] = useState(true);

  useEffect(() => {
    const getNewsData = async () => {
      const result = await axios('https://newsapi.org/v2/top-headlines?q=coronavirus&language=en&apiKey=YOUR_OWN_KEY');
      // console.log(result);
      setData(result.data.articles);
      setShowLoading(false);
    };

    getNewsData();
  }, []);
```

Maintenant, enregistrez le fichier et vérifiez dans le navigateur. Donc, finalement, nous devrions obtenir le design ci-dessous:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/CoronaSnap2.jpg)
_Onglet Nouvelles — Captures d'écran de l'émulateur en PWA, Android et iOS_

Faites-moi savoir si vous êtes bloqué avec des problèmes liés aux codes, aux erreurs de compilation ou d'exécution.

C'est tout pour le Jour 2.?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image.png)

## Jour 3 - Développement de l'onglet Aide et Déploiement

Dans cette section - notre dernière - nous allons développer l'**onglet Aide** et apprendre à utiliser **Capacitor pour construire** des applications **Android** et **iOS**. 

Jusqu'à présent, nous avons construit les onglets **Monde, Pays, Nouvelles**, **et Directives** dans notre application ionic react. De plus, nous allons déployer notre application sur Firebase en tant que **PWA**. Cela va être le plus intéressant maintenant. Mettez vos chaussettes et soyez prêt à voir votre propre application dans un environnement réel.

### Onglet Aide : Design

Tout d'abord, créons l'onglet Aide et Feedback. Ceci est juste un onglet informatif et statique pour l'aide de l'**Organisation Mondiale de la Santé (OMS** qui donne des commentaires au développeur.

```ts
<IonCard>
    <IonList>
      <IonItem>
        <IonLabel>Appeler le numéro de la ligne d'assistance de l'OMS</IonLabel>
        <IonButton color='warning' href="tel:+41-22-7912111"><IonIcon slot="start" icon={callOutline} /> Appeler</IonButton>
      </IonItem>
      <IonItem>
        <IonLabel>Envoyer un email à l'équipe de l'OMS</IonLabel>
        <IonButton color='warning' href="mailto:mediainquiries@who.int"><IonIcon slot="start" icon={mailOutline} /> Email</IonButton>
      </IonItem>
      <IonItem>
        <IonLabel>Envoyer 'Salut' au service d'assistance de l'OMS</IonLabel>
        <IonButton color='warning' href="https://api.whatsapp.com/send?phone=41798931892&text=hi&source=&data="><IonIcon slot="start" icon={logoWhatsapp} /> WhatsApp</IonButton>
      </IonItem>
      <IonItem>
        <IonLabel>Faire un don via le site web de l'OMS</IonLabel>
        <IonButton color='warning' href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/donate"><IonIcon slot="start" icon={walletOutline} /> Faire un don</IonButton>
      </IonItem>
    </IonList>
  </IonCard>
```

## Vérification de l'installation de l'environnement

Comme mentionné dans notre première section (Jour 0), nous devrions avoir tous les logiciels suivants installés dans notre système:

* VS Code
* Google Chrome
* Android Studio pour l'application Android
* Xcode pour l'application iOS (Malheureusement seulement disponible sur les ordinateurs Apple)

Nous devons définir le chemin requis et installer les versions ciblées d'Android (comme Android 9 Pie) et d'iOS (comme iOS 11) des systèmes d'exploitation. 

Attendez, ne vous inquiétez pas si vous êtes très nouveau dans cette configuration de plateforme. Suivez les étapes suivantes de manière séquentielle avec tous les **liens** **importants** fournis dans les sections à venir.

Nous avons déjà installé **Capacitor** dans notre première commande de terminal lors de la création de l'application ionic react. (Vérifiez le Jour 0 pour la section d'installation). Capacitor est le pont natif pour les applications web multiplateformes. Il invoque les SDK natifs sur iOS, Android et le Web avec une seule base de code.

// Allez dans votre répertoire de projet et exécutez les commandes ci-dessous pour initialiser Capacitor dans votre projet et ajouter les plateformes Android et iOS à votre application:

**npm install --save @capacitor/core @capacitor/cli
npx cap init
npx add android
npx add ios**

## Icônes et écrans de démarrage de l'application

Pour créer des icônes et des écrans de démarrage pour Android et iOS, je recommande d'utiliser [https://pgicons.abiro.com/](https://pgicons.abiro.com/). Il créera différentes tailles d'icônes et d'écrans de démarrage pour tous les systèmes d'exploitation mobiles ciblés. 

Après avoir créé ceux-ci, vous pouvez directement remplacer ces icônes par les icônes et écrans de démarrage par défaut d'Ionic dans les dossiers de vos plateformes ciblées.

# Application Web Progressive (PWA)

Les deux exigences principales d'une PWA sont les [Service Workers](https://developers.google.com/web/fundamentals/primers/service-workers/) et un [Web Manifest](https://developers.google.com/web/fundamentals/web-app-manifest/). Une fois ces fichiers ajoutés, exécutez `ionic build` et le répertoire `build` sera prêt à être déployé en tant que PWA sur n'importe quelle plateforme d'hébergement comme Firebase. 

Suivez le lien ? [https://ionicframework.com/docs/react/pwa](https://ionicframework.com/docs/react/pwa) pour plus de détails.

Tout d'abord, [créez le projet](https://console.firebase.google.com/) sur le site web **Firebase**. Vous pouvez choisir le plan gratuit pour l'instant. Activez l'option d'hébergement dans la navigation de gauche. Ensuite, dans un terminal, installez l'interface de ligne de commande Firebase:

**npm install -g firebase-tools**

Il vous demandera certains noms et options de dossiers par défaut pour les fichiers liés à Firebase. Continuez à répondre à toutes les questions. Maintenant, construisez votre projet à nouveau avec le drapeau **--prod** comme indiqué ci-dessous:

**ionic build --prod
firebase deploy**

C'est tout. ? Allez sur le lien fourni par Firebase dans la section hébergement. Il est très simple et direct de déployer votre application sur Firebase. Chaque fois que vous poussez votre code vers votre propre dépôt GitHub, suivez simplement ces 2 commandes pour construire et déployer les dernières modifications dans votre projet Firebase.

# Application Android

[Android Studio](https://developer.android.com/studio/) est l'IDE pour créer des applications Android natives. Il inclut le [Android SDK](https://ionicframework.com/docs/reference/glossary#android-sdk), qui devra être configuré pour une utilisation en ligne de commande.

Android Studio est également utilisé pour [créer des appareils virtuels Android](https://ionicframework.com/docs/developing/android#creating-an-android-virtual-device), qui sont requis pour l'émulateur Android. Les applications Ionic peuvent également être [lancées sur un appareil](https://ionicframework.com/docs/developing/android#set-up-an-android-device). 

Utilisez le lien pour la configuration et l'installation complètes ?[https://ionicframework.com/docs/developing/android](https://ionicframework.com/docs/developing/android).

// Exécutez les commandes ci-dessous pour synchroniser les plugins natifs et exécuter les applications natives:
**ionic cap copy
ionic cap sync
ionic capacitor run android
ionic cap open android**

Maintenant, votre application sera ouverte dans Android Studio où vous pouvez vérifier le même dossier, votre ID de projet et d'autres paramètres par défaut. De plus, vous pouvez créer des icônes et des écrans de démarrage pour votre propre application et remplacer ceux par défaut d'Ionic dans le projet. 

Créez un émulateur et exécutez l'application. Vous devriez voir votre application de suivi du coronavirus dans l'émulateur Android maintenant. Allez dans l'option **Build** en haut dans Android Studio, et sélectionnez **Build Bundle(s)/APK(s).** Pour la première fois, vous devez créer la clé de signature. Ensuite, cliquez sur suivant pour construire l'option apk/bundle.

**Hourra**! ? Vous avez maintenant votre propre application Android dans le dossier de construction qui est prête à être déployée sur le **Google Play Store** (Les comptes développeurs **coûtent 25 USD** avec un accès à vie) et **Amazon App Store** (gratuit).

# Application iOS

[Xcode](https://developer.apple.com/xcode/) est l'IDE pour créer des applications iOS natives. Il inclut le SDK iOS et les outils de ligne de commande Xcode. Xcode peut être [téléchargé gratuitement](https://developer.apple.com/download/) avec un compte Apple ou il peut être installé via l'App Store. 

Utilisez le lien pour la configuration et l'installation complètes ? [https://ionicframework.com/docs/developing/ios](https://ionicframework.com/docs/developing/ios). 

Malheureusement, les applications iOS ne peuvent être construites que sur des ordinateurs Apple avec des systèmes d'exploitation macOS.

// Exécutez les commandes ci-dessous pour synchroniser les plugins natifs et exécuter les applications natives:
**ionic cap copy
ionic cap sync
ionic capacitor run ios
ionic cap open ios**

Maintenant, votre application sera ouverte dans Xcode où vous pouvez définir votre ID de projet et d'autres paramètres par défaut. De plus, créez des icônes et des écrans de démarrage pour votre propre application et remplacez ceux par défaut d'Ionic dans le projet. 

Créez un émulateur et exécutez l'application. Vous devriez voir votre application de suivi du coronavirus dans l'émulateur iOS maintenant. Si vous avez un compte **Apple Developers Account** actif qui coûte **99 USD** par an, vous pouvez construire votre application iOS et la déployer sur l'**App Store**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-1.png)

En raison de problèmes de politique liés à l'épidémie, le Google Play Store, l'Amazon App Store et autres n'acceptent pas les packages d'applications liés au coronavirus. Donc, à moins que vous n'ayez des preuves d'authenticité de la part d'un gouvernement, d'hôpitaux ou d'une institution de santé désignée, aucun magasin n'accepte ces applications. 

Cependant, le World Wide Web (**WWW**) est libre d'utilisation. Nous avons donc déployé notre application sur le web uniquement pour l'instant.

**Enfin, notre application Ionic React est librement disponible sur Internet pour les utilisateurs finaux – ta-da !**

[CoronaTracker](https://coronatracker-20efc.web.app/) (Utilisez des appareils mobiles pour une expérience fluide) [https://coronatracker-20efc.web.app/world](https://coronatracker-20efc.web.app/world)

## Travail en attente

Depuis la rédaction de cet article, j'ai rendu ce projet open source sur GitHub. Vous pouvez contribuer ici en forkant le dépôt ci-dessous.

1. Réactivité du bureau ? (Fonctionne actuellement bien pour les mobiles et les tablettes)
2. Cas de test unitaire.
3. Il y a toujours de la mise en forme et de l'indentation.?

Pour le code complet, plongez dans le dépôt GitHub. N'oubliez pas de starer et de forker au cas où vous aimeriez ajouter d'autres fonctionnalités sympas. Pour le processus de fork, suivez les étapes données dans le fichier README.MD.

%[https://github.com/kapilraghuwanshi/corona-tracker-app]

J'espère que vous avez trouvé cet article utile et qu'il vous a aidé à apprendre et à construire une application géniale aujourd'hui. Si vous l'avez vraiment aimé, n'hésitez pas à le partager sur toutes les plateformes de médias sociaux.

**Restons connectés sur LinkedIn (**[**@kapilraghuwansh**](https://www.linkedin.com/in/kapilraghuwanshi/)**i) et Twitter (**[**@techygeeek**](https://twitter.com/techygeeeky)**y) pour plus d'histoires tech comme celle-ci.?**