---
title: How I Created a Coronavirus Tracker App in Just 3 Days with Ionic and Firebase
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
seo_title: null
seo_desc: "By KAPIL RAGHUWANSHI\nI am really fond of Hybrid App technologies – they\
  \ help us achieve so much in a single codebase. Using the Ionic Framework, I developed\
  \ a cross-platform mobile solution for tracking Coronavirus cases in just 3 days.\
  \ \nIn this tuto..."
---

By KAPIL RAGHUWANSHI

I am really fond of Hybrid App technologies – they help us achieve so much in a single codebase. Using the Ionic Framework, I developed a cross-platform mobile solution for tracking Coronavirus cases in just 3 days. 

In this tutorial, we are going to learn how to develop an **Android, iOS, and Progressive Web App** to track the cases around us with the latest related news, help, and feedback sections. Brace yourself for a new coding journey! ?

### Prerequisites

The process of hybrid mobile app development is meant for all kinds of developers irrespective of their technology stack. Since we will be using three basic pillars of Web Development – **HTML+CSS+JAVASCRIPT** – at the core, you can easily understand the process and techniques. 

Thus this tutorial is for everyone who has just a basic understanding of Web Fundamentals. So, let's begin.

## Day 0 - Idea, Plan, and Engineering 

### Idea

Initially, I was looking for the latest Covid19 cases around me (in March 2020). I got several links that had little difference in numbers. 

Then, I realised that data from [https://github.com/backtrackbaba/covid-ap](https://github.com/backtrackbaba/covid-api)i is regularly updated and more accurate. I decided to develop a universal, small, and handy mobile solution by using data provided by **Johns Hopkins University.**

### Plan

I planned to develop a cross-platform mobile solution that could be universally accessed by everyone. I considered the Ionic framework which would allow me to develop an **Android**, iOS & Progressive Web App** **(PWA)****? by just writing and maintaining a single codebase. 

I also wanted to show the COVID19 virus cases across the world and individual countries through various illustrations.

### Engineering

The idea was to develop 5 separate tabs which would be there at the bottom of the app:

1. **World** — would show the COVID19 Dashboard
2. **Country —** would allow you to select a country to check the cases
3. **News —** would get the latest news regarding the Coronavirus Pandemic
4. **Guidelines —** would allow you to read and watch all advisories and guidelines
5. **Help** — would provide help and feedback.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-170.png)
_Photo by [Unsplash](https://unsplash.com/@sctgrhm?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Scott Graham</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### Technology Stack

I have developed several websites and apps through Angular and Ionic before. But this time, I wanted to learn and use React.js. The below libraries are required to install using the Node package manager (**npm**):

* **React.js** includes the latest react-hooks
* **Ionic Framework** (version 4) with **Capacitor**
* **Node.js** environment to support JavaScript and npm libraries
* **TypeScript** language to write the actual code (.tsx files)
* **Chart.js** for various illustrations
* **Firebase** for hosting the content (**Progressive Web App**)

### Tools

* VS Code
* Google Chrome
* Android Studio for Android app
* Xcode for iOS app (Unfortunately only available in Apple computers)

### Installation & Scaffolding

We need to install and configure all the above mentioned Software and Frameworks. So, let’s start with the first set of terminal commands (whether it's on Mac, Linux or Windows):

1. Install ionic with global scope **"npm install -g @ionic/cli native-run cordova-res"**
2. Create react app with Capacitor **"ionic start corona-tracker tabs — type=react — capacitor"**
3. Add react hooks and pwa elements **"npm install @ionic/react-hooks @ionic/pwa-elements"**

Open the **corona-tracker** folder in your default workplace. You should have gotten all the default HTML, CSS and .tsx files with other sub-folders in the proper sequence. Now, go to your app folder and run these 2 commands

 **cd corona-tracker**
 **ionic serve**

Voilà! ?  Your Ionic app is now running in a web browser. Click on the localhost option in the terminal to check. ?This is your basic app installation and scaffolding. 

So far, you should be running your ionic-react app in your local browser. Now **index.html** and **index.tsx** are your first pages for **Single Page Applications (SPAs).**

### App Routing

Let’s add routing to our app which will allow us to visit all 5 different tabs explained above. Open your **App.tsx** file and add the below router inside <IonReactRouter></IonReactRouter>

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
            <IonLabel>World</IonLabel>
          </IonTabButton>
          <IonTabButton tab="CountryTab" href="/country">
            <IonIcon icon={home} />
            <IonLabel> Country</IonLabel>
          </IonTabButton>
          <IonTabButton tab="NewsTab" href="/news">
            <IonIcon icon={newspaper} />
            <IonLabel> News</IonLabel>
          </IonTabButton>
          <IonTabButton tab="GuidelinesTab" href="/guidelines">
            <IonIcon icon={informationCircleOutline} />
            <IonLabel>Guidelines</IonLabel>
          </IonTabButton>
          <IonTabButton tab="HelpTab" href="/help">
            <IonIcon icon={call} />
            <IonLabel>Help</IonLabel>
          </IonTabButton>
        </IonTabBar>
      </IonTabs>
```

Check your app in the browser again, and you should see all these tabs with their respective pages. All tabs should be working smoothly with proper routing.

> _Let me know _in case you_'re _stuck with any issues related to installation, compile-time_, _or run-time errors.__

This is it for **Day** 0.?

## Day 1 - Developing COVID19 Dashboard and Safety Guidelines tabs

  
In this part of the process, we will develop the **World** and **Guidelines** tabs for our Ionic React hybrid app. So far, we have done the basic installation and scaffolding of the app. We have also added 5 different tabs to our app with routing.

### World Tab: Design

Let’s build our home page **World** tab now. I decided to have 4 different sections on this home tab:

1. 4 different boxes to show actual numbers: Total, Active, Recovered and Deaths
2. A Pie Chart depicting the number of cases
3. Slideshows for basic health tips
4. All countries listed with these categories in descending order.

### World Tab: Data & API

I have studied the open-source postman API source which contains all Application Programming Interfaces (APIs) related to Corona Cases [**https://documenter.getpostman.com/view/2568274/SzS8rjbe?version=latest**](https://documenter.getpostman.com/view/2568274/SzS8rjbe?version=latest)**.** 

First, we will consume the [global](https://covidapi.info/api/v1/global) API with the Axios library to get the total global case count in the world using the useState & useEffect React-hooks.

```ts
const [data, setData] = useState<IGLobalCount>();
const [showLoading, setShowLoading] = useState(true);
  useEffect(() => {
    const getGlobalData = async () => {
      //latest global count
      const result = await axios('https://covidapi.info/api/v1/global');
      // console.log(result);
      setData(result.data);
      setShowLoading(false);
    };
    getGlobalData();
  }, []);
```

Then set the data inside your return block using HTML:

```html
<IonRow class="casesBox">
    <IonCol class="totalCases">Total <AddNumFunc a={confirmed} b={recovered} c={deaths} /></IonCol>
    <IonCol class="confirmedBox">Confirmed {confirmed?.toLocaleString()}</IonCol>
    <IonCol class="recoveredBox">Recovered {recovered?.toLocaleString()}</IonCol>
    <IonCol class="deathsBox">Deaths {deaths?.toLocaleString()}</IonCol>
</IonRow>
```

Now, we have the first 4 responsive boxes containing total cases, confirmed cases, recovered, and deaths. Install chart.js in your project using **npm install react-chartjs-2**. Let’s make use of the same data to draw a PieChart.

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

Now, we have 2 of the 4 sections in the **World** tab. So next, let’s add a slideshow depicting general health tips.

```ts
<IonSlides class="tipsSlides" options={slideOpts}>
  <IonSlide class="slide">
    Maintain at least 1 metre (3 feet) distance between yourself and anyone who is coughing or sneezing.
  </IonSlide>
  <IonSlide class="slide">
    Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water.
  </IonSlide>
  <IonSlide class="slide">
    If you have fever, cough and difficulty breathing, seek medical care early.
  </IonSlide>
  <IonSlide class="slide">
    Avoid touching eyes, nose and mouth. #StayHomeStaySafe
  </IonSlide>
  <IonSlide class="slide">
    WHO Health Alert brings COVID-19 facts to billions via WhatsApp.
  </IonSlide>
</IonSlides>
```

Now, let’s make a data table for all countries in descending order to depict all kinds of cases. Again, we will consume the [latest](https://covidapi.info/api/v1/global/latest) API with the Axios library to get the total global count for all the countries in the world using the useState & useEffect React-hooks.

```ts
const [countryWiseData, setCountryWiseData] = useState<ICountry[]>([]);
  useEffect(() => {
    const getGlobalCountryData = async () => {
      //latest global country wise count
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

We have completed the development for our home tab with all 4 sections described above. You can see them below:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/CoronaHybridAppSnap1.jpg)
_World Tab — Working Emulator Snapshots in PWA, android and iOS_

Now, let’s jump on to develop our next tab — the **Guideline**s **Tab**.

This is just an informative and static tab for various **Advisor**ies **and Guidelines** given by WHO and State Governments. We have added various images and videos here in the HTML:

```ts
<IonList>
   <IonCard>
     <iframe title="WHO" width="100%" height="200" src="https://www.youtube.com/embed/5jD2xd3Cv80"
       allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture">
     </iframe>
   </IonCard>
   <IonCard>
     <IonCardHeader>Symptoms</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/Symptoms2.png"></IonImg>
   </IonCard>
   <IonCard>
     <IonCardHeader>Diseases</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/Symptoms.png"></IonImg>
   </IonCard>
   <IonCard>
     <IonCardHeader>Myths Busted</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/Myth.jpeg"></IonImg>
   </IonCard>
   <IonCard>
     <IonCardHeader>Stress Distraction Tips</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/Stress.jpg"></IonImg>
   </IonCard>
   <IonCard>
     <IonCardHeader>Stay Home</IonCardHeader>
     <IonImg class="guidlineImages" src="assets/images/SafeHands.jpeg"></IonImg>
   </IonCard>
</IonList>
```

Let me know in case you get stuck with any issues related to installation, compile-time or run-time errors.

This is it for Day 1.?

## Day 2 - Developing Country and News tabs

In this section we will develop **Country** and **News** tabs for our Ionic React hybrid app. So far, we have built **World** and **Guideline** tabs in our ionic react app with basic app routing.

### Country Tab: Design

Let’s build our second page **Country** tab now. I decided to have 4 different sections on this second tab:

1. Country Dropdown to select the country of your choice
2. 4 different boxes to show actual numbers: Total, Active, Recovered and Deaths in the selected country
3. A Doughnut Chart depicting the number of cases in the selected country
4. Weekly Trend for the cases in the selected country. 

### Country Tab: Data & API

I have studied the open-source postman link which contains all Application Programming Interfaces (APIs) related to Corona Cases [**https://documenter.getpostman.com/view/2568274/SzS8rjbe?version=latest**](https://documenter.getpostman.com/view/2568274/SzS8rjbe?version=latest)**.** 

Here, we will consume the [country](https://covidapi.info/api/v1/country/) API with the Axios library to get the total count in the selected country using the useState & useEffect React-hooks.

We will store the country the user has selected in local storage for other illustrations to update.

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

Now, consume the API to get the country-specific data:

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

Now, design the Doughnut and Bar trend chart:

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
       text: 'Cases in the current week',
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

Now save the file and check it out in the browser. So, finally, we should get the below design:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/CoronaSnap3-2.jpg)
_Country tab — Working Emulator Snapshots in PWA, android and iOS_

Now, let’s keep going and develop our third tab — the **News Tab.**

### News Tab: Design

We have added a basic Ionic Card which contains various News resources such as URL, title, image, author and publisher’s details:

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

### News Tab: Data & API

To get the news, I used **Newsapi.org** which is **not an open-source** ?Application Programming Interface (API). But with a developer account, I searched news related to the Coronavirus. If you want to use other news APIs you can use them instead.

Here, we will consume the [top-headlines](https://newsapi.org/v2/top-headlines) API with the Axios library to get the total count in the selected country using the useState & useEffect React-hooks.

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

Now, save the file and check in the browser. So, finally, we should get the below design:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/CoronaSnap2.jpg)
_News tab — Working Emulator Snapshots in PWA, android and iOS_

Let me know in case you get stuck with any issues related to codes, compile-time or run-time errors.

This is it for Day 2.?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image.png)

## Day 3 - Developing the Help Tab and Deployment

In this section - our last one - we will develop the **Help tab** and learn to use **Capacitor to build** A**ndroid** and **iOS** apps. 

So far, we have built the **World, Country, News**, **and Guideline** tabs in our ionic react app. Also, will deploy our app to Firebase as a **PWA.** It is going to be most interesting now. Pull on your socks and be ready to actually see your own app in a real environment.

### Help Tab: Design

First, let’s create the Help and Feedback tab. This is just an informative and static tab for help from the **World Health Organization (WHO**) that gives feedback to the developer.

```ts
<IonCard>
    <IonList>
      <IonItem>
        <IonLabel>Call WHO helpline Number</IonLabel>
        <IonButton color='warning' href="tel:+41-22-7912111"><IonIcon slot="start" icon={callOutline} /> Call</IonButton>
      </IonItem>
      <IonItem>
        <IonLabel>Email WHO Team</IonLabel>
        <IonButton color='warning' href="mailto:mediainquiries@who.int"><IonIcon slot="start" icon={mailOutline} /> Email</IonButton>
      </IonItem>
      <IonItem>
        <IonLabel>Text 'Hi' to WHO helpdesk</IonLabel>
        <IonButton color='warning' href="https://api.whatsapp.com/send?phone=41798931892&text=hi&source=&data="><IonIcon slot="start" icon={logoWhatsapp} /> WhatsApp</IonButton>
      </IonItem>
      <IonItem>
        <IonLabel>Donate via WHO website</IonLabel>
        <IonButton color='warning' href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/donate"><IonIcon slot="start" icon={walletOutline} /> Donate</IonButton>
      </IonItem>
    </IonList>
  </IonCard>
```

## Environment Installation Check

As mentioned in our first (Day 0) section, we should have all the below Software installed in our system:

* VS Code
* Google Chrome
* Android Studio for Android app
* Xcode for iOS app (Unfortunately only available in Apple computers)

We need to set the required path, and install the targeted Android (such as Android 9 Pie) and iOS (such as iOS 11) operating system versions. 

Wait, don’t worry if you are very new to this platform setup. Follow the next steps sequentially with all the provided **important** **links** in the coming sections.

We have already installed **Capacitor** in our first terminal command while creating the ionic react app. (Check Day 0 for the installation section). Capacitor is the Native Bridge for Cross-Platform Web Apps. It invokes Native SDKs on iOS, Android, and the Web with one codebase.

// Go to your project directory and run below commands to initialize Capacitor into your project and add the Android and iOS platforms to your app:

**npm install --save @capacitor/core @capacitor/cli
npx cap init
npx add android
npx add ios**

## App icons and Splash screens

For creating android and iOS icons and splash screens, I recommend using [https://pgicons.abiro.com/](https://pgicons.abiro.com/). It will create varied sizes of icons and splashes for all the targeted mobile operating systems. 

After creating these, you can directly replace these icons with the default ionic icons and splashes in your targeted platforms folders.

# Progressive Web App (PWA)

The two main requirements of a PWA are [Service Workers](https://developers.google.com/web/fundamentals/primers/service-workers/) and a [Web Manifest](https://developers.google.com/web/fundamentals/web-app-manifest/). Once these files have been added, run `ionic build` and the `build` directory will be ready to deploy as a PWA to any hosting platform like Firebase. 

Follow the link ? [https://ionicframework.com/docs/react/pwa](https://ionicframework.com/docs/react/pwa) for more details.

First, [create the project](https://console.firebase.google.com/) in the **Firebase** Website. You can choose the free plan for now. Enable the hosting option from the left nav. Next, in a terminal, install the Firebase CLI:

**npm install -g firebase-tools**

It will ask you some default name and folder options for firebase related files. Continue answering all the questions. Now, build your project again with the **--prod** flag as given below:

**ionic build --prod
firebase deploy**

That’s it. ? Go to the link provided by Firebase under the hosting section. It is very simple and straightforward to deploy your app on Firebase. Every time you push your code to your own GitHub repo, just follow those 2 commands to build and deploy the latest changes into your Firebase project.

# Android App

[Android Studio](https://developer.android.com/studio/) is the IDE for creating native Android apps. It includes the [Android SDK](https://ionicframework.com/docs/reference/glossary#android-sdk), which will need to be configured for use in the command line.

Android Studio is also used to [create Android virtual devices](https://ionicframework.com/docs/developing/android#creating-an-android-virtual-device), which are required for the Android emulator. Ionic apps can also be [launched to a device](https://ionicframework.com/docs/developing/android#set-up-an-android-device). 

Use the link for complete setup and installation ?[https://ionicframework.com/docs/developing/android](https://ionicframework.com/docs/developing/android).

// Run the below commands to sync native plugins and run the native apps:
**ionic cap copy
ionic cap sync
ionic capacitor run android
ionic cap open android**

Now, your app will be open in Android Studio where you can check the same folder, your project ID, and other default settings. Also, you can build icons and splash screens for your own app and replace the existing default ionic ones in the project. 

Create an Emulator and run the app. You should see your Coronavirus-tracker app in the Android Emulator now. Go to the **Build** option in the top in Android Studio, and select the **Build Bundle(s)/APK(s).** For the first time, you need to create the signing key. Then, click next to build apk/bundle option.

**Hurray**! ? You have your own Android app now in the build folder which is ready to deploy to **Google Play Store** (Developer accounts **cost USD** $**25** with lifetime access) and **Amazon App Store** (free).

# iOS App

[Xcode](https://developer.apple.com/xcode/) is the IDE for creating native iOS apps. It includes the iOS SDK and Xcode command-line tools. Xcode can be [downloaded for free](https://developer.apple.com/download/) with an Apple account or it can be installed through the App Store. 

Use the link for complete setup and installation ? [https://ionicframework.com/docs/developing/ios](https://ionicframework.com/docs/developing/ios). 

Unfortunately, iOS apps can only be built in Apple Computers with macOS operating systems.

// Run the below commands to sync native plugins and run the native apps:
**ionic cap copy
ionic cap sync
ionic capacitor run ios
ionic cap open ios**

Now, your app will be open in Xcode where you can set your project ID and other default settings. Also, create icons and splash screens for your own app and replace the existing default ionic ones in the project. 

Create an Emulator and run the app. You should see your Coronavirus-tracker app in the iOS Emulator now. If you have an active **Apple Developers Account** which costs **USD** $99 annually, you can build your iOS app and deploy it to the **App Store**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-1.png)

Due to policy issues of the epidemic, Google Play Store, Amazon App Store, and others are not accepting app packages related to the Coronavirus. So until and unless you have authenticity proofs from any Government, Hospitals, or any designated Health Institution, no stores are accepting these apps. 

However, the World Wide Web (**WWW**) is free to use. So we have deployed our app on the web only for now.

**Finally, our Ionic React app is freely available on the internet for end users – ta-da!**

[CoronaTracker](https://coronatracker-20efc.web.app/) (Use mobile devices for a smooth experience) [https://coronatracker-20efc.web.app/world](https://coronatracker-20efc.web.app/world)

## Pending Work

Since writing this article, I have made this project open source on GitHub. You can contribute here by forking the below repo.

1. Desktop Responsiveness ? (Currently works well for Mobile and Tablets)
2. Unit test cases.
3. There is always formatting and indentation.?

For the complete code, jump into the GitHub repo. Don’t forget to star and fork in case you would like to add some more cool features to it. For the fork process, follow the steps given in README.MD file.

%[https://github.com/kapilraghuwanshi/corona-tracker-app]

I hope that you found this article useful and it was able to help you learn and build an awesome app today. If you really liked it, please do share it on all social media platforms.

**Let’s be connected on LinkedIn (**[**@kapilraghuwansh**](https://www.linkedin.com/in/kapilraghuwanshi/)**i) and Twitter (**[**@techygeeek**](https://twitter.com/techygeeeky)**y) for more such tech stories.?**

