---
title: How to Build an Android News App with React Native and Native Base
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-23T18:23:27.000Z'
originalURL: https://freecodecamp.org/news/build-an-android-news-app-with-react-native-and-native-base
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/How-to-Build-a-Weather-Application-using-React--66-.png
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
seo_title: null
seo_desc: "By Nishant Kumar\nWe live in a world where things are constantly changing.\
  \ So if you want to stay up to date on what's happening, you'll want a good News\
  \ app. \nTo help you learn some cool tech and stay current, in this blog post we'll\
  \ build a News App..."
---

By Nishant Kumar

We live in a world where things are constantly changing. So if you want to stay up to date on what's happening, you'll want a good News app. 

To help you learn some cool tech and stay current, in this blog post we'll build a News Application for Android using React Native. It will fetch headlines from different news channels and show them by category.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-210544.png)

This is how our app will look when we're done. So let's jump right into it.

## How to Install Expo

So, what is Expo? Expo is a framework that helps you build and deploy a React Native app quickly and easily.

Let's install it.

```
npm install --global expo-cli
```

Run this command in your terminal to install the Expo CLI. Here, we are using `--global` to make sure it installs everywhere.

After it has been installed, we need to create an Expo Project.

```
expo init News-Application
```

Use the above command to initialize the project. It will ask you a few questions, like the name of your application, whether you want add TypeScript in your project, or start with a blank project. Just select blank, and press enter.

Then, it will download all the packages and dependencies in the folder.   
  
Now, after that's done, navigate into the project folder. To start the application, type **expo start**. It will open up developer tools in the browser.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-174505.png)
_Expo developer tools_

Here you'll see many options on the left, like run on Android device/emulator, or on iOS simulator. We will run the application on the Web Browser, so click the Run in Web Browser option.

```
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

```

This is our App.js file, which contains the default boilerplate.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-175022.png)
_Our output_

Now our application is running.

## How to Create Different Screens using React Navigation

Now, let's create various different screens for our application. For that, we will use React Navigation. So, let's install it.

Head to [https://reactnavigation.org/](https://reactnavigation.org/) and click Read Docs. It will open up the documentation page.

Let's install React Navigation by using the command below:

```
npm install @react-navigation/native

expo install react-native-screens react-native-safe-area-context
```

Now, our React Navigation has been installed. 

We will use `bottomTabNavigator`. So, from the left menu, choose API Reference, then Navigators, then the Bottom Tabs.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-175641.png)
_Choose Bottom Tabs_

Let's install the Bottom Tabs using the command below:

```
npm install @react-navigation/bottom-tabs
```

Now, in our App.js file, we need to import Bottom Tabs in order to use it.

So, import it like this:

```
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

```

Now, let's import the Tab Screens.

```
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
const Tab = createBottomTabNavigator();

function MyTabs() {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Settings" component={SettingsScreen} />
    </Tab.Navigator>
  );
}
```

This is how we create Bottom Tabs.

In our case, we need to do something like this:

```
<Tab.Navigator>
  <Tab.Screen name="All" component={All} />
  <Tab.Screen name="Business" component={Business} />
  <Tab.Screen name="Health" component={HealthScreen} />
  <Tab.Screen name="Sports" component={SportsScreen} />
  <Tab.Screen name="Tech" component={TechScreen} />
</Tab.Navigator>
```

We need to create these screens for the following tabs: All News, Business News, Sports News, Health News, and the Tech News. Also, create one component in the Project for each screen.

We need to wrap this `TabNavigtor` into a `NavigationContainer` like this:

```
<NavigationContainer>
  <Tab.Navigator>
    <Tab.Screen name="All" component={All} />
    <Tab.Screen name="Business" component={Business} />
    <Tab.Screen name="Health" component={HealthScreen} />
    <Tab.Screen name="Sports" component={SportsScreen} />
    <Tab.Screen name="Tech" component={TechScreen} />
  </Tab.Navigator>
</NavigationContainer>
```

We also need to import these all components, so import them at the top.

```
import All from './screens/All';
import Business from './screens/Business';
import HealthScreen from './screens/Health';
import SportsScreen from './screens/Sports';
import TechScreen from './screens/Tech';
```

Now, if we put all the code together that we have written, we will get the below code:

```
import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import All from './screens/All';
import Business from './screens/Business';
import HealthScreen from './screens/Health';
import SportsScreen from './screens/Sports';
import TechScreen from './screens/Tech';
const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="All" component={All} />
        <Tab.Screen name="Business" component={Business} />
        <Tab.Screen name="Health" component={HealthScreen} />
        <Tab.Screen name="Sports" component={SportsScreen} />
        <Tab.Screen name="Tech" component={TechScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
} 
```

And this will be our output:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-181356.png)
_Our five screens namely All, Business, Health, Sports and Tech_

We have five screens here for All, Business, Health, Sports and Tech.

Now, let's make a few adjustments here. We need to change the icons for the bottom tabs.

To do that, we'll need to get an icon library for our icons. For that we are going to use _react-native-elements._ 

To install it, type the below command:

```
npm install react-native-elements
```

This icon package has lots of icon options to choose from.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-193917.png)
_Available Icons in React Native Elements_

Now let's add our icons in the Bottom Tab Navigator.

```
<Tab.Screen name="All" component={All}
          options={{
            tabBarIcon: (props) => (
              <Icon type='feather' name='home' color={props.color} />
            ),
          }} />
```

Here we have added the icon named "home" for the home page and feather icon class for type.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-194136.png)
_Bottom Tab Navigator with the Home Icon_

This will yield the above output. And similarly, let's repeat the same process for all of them.

```
<Tab.Navigator>
        <Tab.Screen name="All" component={All}
          options={{
            tabBarIcon: (props) => (
              <Icon type='feather' name='home' color={props.color} />
            ),
          }} />

        <Tab.Screen name="Business" component={Business}
          options={{
            tabBarIcon: (props) => (
              <Icon type='feather' name='dollar-sign' color={props.color} />
            ),
          }} />

        <Tab.Screen name="Health" component={HealthScreen}
          options={{
            tabBarIcon: (props) => (
              <Icon type='feather' name='heart' color={props.color} />
            ),
          }} />

        <Tab.Screen name="Sports" component={SportsScreen}
          options={{
            tabBarIcon: (props) => (
              <Icon type='ionicon' name="tennisball-outline" color={props.color} />
            ),
          }} />

        <Tab.Screen name="Tech" component={TechScreen}
          options={{
            tabBarIcon: (props) => (
              <Icon type='ionicon' name="hardware-chip-outline" color={props.color} />
            ),
          }} />
      </Tab.Navigator>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-194525.png)

Now each of our different tabs or screens are done, and they each have their own distinct icon. 

## How to Call the News API

Now, let's call the News API from [https://newsapi.org/](https://newsapi.org/)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-194845.png)

Go to this website and signup. It will give you an API key.

We need a config file to store all the News constants, so let's create it.

```
export const API_KEY = ``;
export const endpoint = `https://newsapi.org/v2/top-headlines`;
export const country = 'in'
```

We need the API_KEY, the endpoint, and the country code.

Now, we need to create a service for our **GET API Request.**

Create a file called _services.js._

Here, import API_KEY, endpoint, and the country at the top.

```
import { API_KEY, endpoint, country } from '../config/config';
```

Then, we will write our services body.

```
export async function services(category = 'general') {
    let articles = await fetch(`${endpoint}?country=${country}&category=${category}`, {
        headers: {
            'X-API-KEY': API_KEY
        }
    });

    let result = await articles.json();
    articles = null;

    return result.articles;
}
```

So, we are fetching the news data by using our endpoint, and appending the country and the category. In the function, we pass the category as general because that is the default category. We also pass the API_key in the headers.

Then, we convert the response, or incoming data, into JSON format and storing it in a result variable. 

And lastly, we are returning it using the `return` keyword.

Here's the whole file for your reference:

```
import { API_KEY, endpoint, country } from '../config/config';

export async function services(category = 'general') {
    let articles = await fetch(`${endpoint}?country=${country}&category=${category}`, {
        headers: {
            'X-API-KEY': API_KEY
        }
    });

    let result = await articles.json();
    articles = null;

    return result.articles;
}
```

Now, we need to import this service into our All.js file.

```
import { services } from '../services/services';
```

We will need to use the `useState` and `useEffect` hooks. The useEffect hook will call this service within the All.js file and useState will create a state that will store the response coming from the API.

```
import React, { useEffect, useState } from 'react'
import { View } from 'react-native';
import { services } from '../services/services';
export default function All() {
    const [newsData, setNewsData] = useState([])
    useEffect(() => {
        services('general')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
    return (
        <View>

        </View>
    )
}

```

In this file, we call the services in our useEffect hook. And then we store the response in the newsData state, which is an array. We also pass a parameter for the category which is general. 

This screen will fetch all news, so we use the general category. It will change for every other screen. It will be _health_ for the Health screen, _sports_ for Sports, and so on.

Now, we need to show this data in our interface. And for that, we need yet another package called Native Base. So, let's install it.

Type the commands below to install Native Base:

```
yarn add native-base styled-components styled-system
expo install react-native-svg react-native-safe-area-context
```

In All.js, let's import a few things from Native Base:

```
import React, { useEffect, useState } from 'react'
import { View, Text } from 'react-native';
import { NativeBaseProvider, FlatList, ScrollView, Divider, Image, Spinner } from 'native-base';
import { services } from '../services/services';
```

Then in the return, we will add `NativeBaseProvider`.

```
return (
        <NativeBaseProvider>
            
        </NativeBaseProvider>
    )
```

Then, let's add the Scroll View. This will let users scroll if the news data goes beyond our screen height.

```
<NativeBaseProvider>
            <ScrollView height={850}>

            </ScrollView>
        </NativeBaseProvider>
```

Now, let's add the `FlatList` to show our news data.

```
<NativeBaseProvider>
            <ScrollView height={850}>
                <FlatList
                    data={newsData}
                    renderItem={({ item }) => (
                       <View>

                       </View> 
                    )}
                    keyExtractor={(item) => item.id}
                />
            </ScrollView>
        </NativeBaseProvider>
```

The FlatList takes a data prop, which is our `newsData` state that we created earlier, and it returns an `item` from `renderItems`_._

This is similar to `map` in JavaScript, which traverses over an array and returns an item. It also has a `keyExtractor` which we use to make each item unique.

Now, let's show our data in the View.

Create one more view inside the parent view like this:

```
<NativeBaseProvider>
            <ScrollView height={850}>
                <FlatList
                    data={newsData}
                    renderItem={({ item }) => (
                       <View>
                           <View>
                               
                           </View>
                       </View> 
                    )}
                    keyExtractor={(item) => item.id}
                />
            </ScrollView>
        </NativeBaseProvider>
```

Now, let's add some text inside the child view.

```
<NativeBaseProvider>
            <ScrollView height={850}>
                <FlatList
                    data={newsData}
                    renderItem={({ item }) => (
                        <View>
                            <View>
                                <Text>
                                    {item.title}
                                </Text>
                                <Text>
                                    {item.publishedAt}
                                </Text>
                                <Text>
                                    {item.description}
                                </Text>
                            </View>
                        </View>
                    )}
                    keyExtractor={(item) => item.id}
                />
            </ScrollView>
        </NativeBaseProvider>
```

This contains our news headline title, the description, and the published date.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-203253.png)

## How to Style our React Native News App

This is how our app looks now, with news title, description, and the date. To make it look a bit nicer, we need to give it some styling.

Import `StyleSheet` from React Native at the top in order to use its styling.

```
import { View, Text, StyleSheet } from 'react-native';
```

```
<View>
                            <View style={styles.newsContainer}>
                                <Text style={styles.title}>
                                    {item.title}
                                </Text>
                                <Text style={styles.date}>
                                    {item.publishedAt}
                                </Text>
                                <Text style={styles.newsDescription}>
                                    {item.description}
                                </Text>
                            </View>
                        </View>
```

Then, add styles like this. And at the bottom we need to create those styles.

```
const styles = StyleSheet.create({
    newsContainer: {
        padding: 10
    },
    title: {
        fontSize: 18,
        marginTop: 10,
        fontWeight: "600"
    },
    newsDescription: {
        fontSize: 16,
        marginTop: 10
    },
    date: {
        fontSize: 14
    },
});
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-203824.png)

This is how the application looks now after getting some styling. You can also scroll down the page.

Now, we need to change the date format to a readable format, because I don't understand **'2021-08-21T11:00:40Z'.**

We'll use the helpful moment.js package for that, so let's install it using the command below:

```
npm install moment --save
```

Then, import it in our All.js screen:

```
<Text style={styles.date}>
  {moment(item.publishedAt).format('LLL')}
</Text>
```

Format the date like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-204311.png)
_Moment.js time and date formats_

The moment documentation gives us so many formats to choose from. I have chosen the _'LLL'_ format.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-204439.png)

And now our dates are much more human-readable.

We also need a divider to separate the news articles from each other so they don't all run together.

```
<View>
                            <View style={styles.newsContainer}>
                                <Text style={styles.title}>
                                    {item.title}
                                </Text>
                                <Text style={styles.date}>
                                    {moment(item.publishedAt).format('LLL')}
                                </Text>
                                <Text style={styles.newsDescription}>
                                    {item.description}
                                </Text>
                            </View>
                            <Divider my={2} bg="#e0e0e0" />
                        </View>
```

So, after adding a divider after the child view, our app looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-204707.png)

Now our news headlines are divided which looks great.

This News API has an image too. So, let's add it.

```
<View>
                            <View style={styles.newsContainer}>
                                <Image
                                    width={550}
                                    height={250}
                                    resizeMode={"cover"}
                                    source={{
                                        uri: item.urlToImage,
                                    }}
                                    alt="Alternate Text"
                                />
                                <Text style={styles.title}>
                                    {item.title}
                                </Text>
                                <Text style={styles.date}>
                                    {moment(item.publishedAt).format('LLL')}
                                </Text>
                                <Text style={styles.newsDescription}>
                                    {item.description}
                                </Text>
                            </View>
                            <Divider my={2} bg="#e0e0e0" />
                        </View>
```

So, we have added the image and we used the key called `urlToImage` to do this_._

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-204945.png)

Now we have the news images showing up.

## How to Add a Spinner to Show News Loading

Let's add a spinner that will show when the news is loading.

First, we will create a check. If the `newsData` state's length is more than one, we will show our `FlatList`, which contains our news data. Otherwise we will show the loading spinner.

In other words, if the `newsData` state's length is less than one, it means it is empty and the API is still getting called. Once the API call finishes, it will store the data into the `newsData` state, and the state's length will change to more than one.

```
{newsData.length > 1 ? (
                    <FlatList
                        data={newsData}
                        renderItem={({ item }) => (
                            <View>
                                <View style={styles.newsContainer}>
                                    <Image
                                        width={550}
                                        height={250}
                                        resizeMode={"cover"}
                                        source={{
                                            uri: item.urlToImage,
                                        }}
                                        alt="Alternate Text"
                                    />
                                    <Text style={styles.title}>
                                        {item.title}
                                    </Text>
                                    <Text style={styles.date}>
                                        {moment(item.publishedAt).format('LLL')}
                                    </Text>
                                    <Text style={styles.newsDescription}>
                                        {item.description}
                                    </Text>
                                </View>
                                <Divider my={2} bg="#e0e0e0" />
                            </View>
                        )}
                        keyExtractor={(item) => item.id}
                    />
                ) : (
                    <View style={styles.spinner}>
                        <Spinner color="danger.400" />
                    </View>
                )}
```

And in our styles, add the below style code for the spinner.

```
spinner: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: 400
}
```

Here is the code below for your reference:

```
import React, { useEffect, useState } from 'react'
import { View, Text, StyleSheet } from 'react-native';
import { NativeBaseProvider, FlatList, ScrollView, Divider, Image, Spinner } from 'native-base';
import { services } from '../services/services';
import moment from 'moment'
export default function All() {
    const [newsData, setNewsData] = useState([])
    useEffect(() => {
        services('general')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
    return (
        <NativeBaseProvider>
            <ScrollView height={850}>
                {newsData.length > 1 ? (
                    <FlatList
                        data={newsData}
                        renderItem={({ item }) => (
                            <View>
                                <View style={styles.newsContainer}>
                                    <Image
                                        width={550}
                                        height={250}
                                        resizeMode={"cover"}
                                        source={{
                                            uri: item.urlToImage,
                                        }}
                                        alt="Alternate Text"
                                    />
                                    <Text style={styles.title}>
                                        {item.title}
                                    </Text>
                                    <Text style={styles.date}>
                                        {moment(item.publishedAt).format('LLL')}
                                    </Text>
                                    <Text style={styles.newsDescription}>
                                        {item.description}
                                    </Text>
                                </View>
                                <Divider my={2} bg="#e0e0e0" />
                            </View>
                        )}
                        keyExtractor={(item) => item.id}
                    />
                ) : (
                    <View style={styles.spinner}>
                        <Spinner color="danger.400" />
                    </View>
                )}
            </ScrollView>
        </NativeBaseProvider>
    )
}

const styles = StyleSheet.create({
    newsContainer: {
        padding: 10
    },
    title: {
        fontSize: 18,
        marginTop: 10,
        fontWeight: "600"
    },
    newsDescription: {
        fontSize: 16,
        marginTop: 10
    },
    date: {
        fontSize: 14
    },
    spinner: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: 400
    }
});
```

Our All.js screen is now complete.

And now, we can use the same code in all other screens as well. We just need to change the parameter we are passing in the services in the `useEffect` Hook.

So, for the Business screen, we will use business. For Health, we will use health, and so on.

```
import React, { useEffect, useState } from 'react'
import { View, Text, StyleSheet } from 'react-native';
import { NativeBaseProvider, FlatList, ScrollView, Divider, Image, Spinner } from 'native-base';
import { services } from '../services/services';
import moment from 'moment'
export default function Business() {
    const [newsData, setNewsData] = useState([])
    useEffect(() => {
        services('business')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
    return (
        <NativeBaseProvider>
            <ScrollView height={850}>
                {newsData.length > 1 ? (
                    <FlatList
                        data={newsData}
                        renderItem={({ item }) => (
                            <View>
                                <View style={styles.newsContainer}>
                                    <Image
                                        width={550}
                                        height={250}
                                        resizeMode={"cover"}
                                        source={{
                                            uri: item.urlToImage,
                                        }}
                                        alt="Alternate Text"
                                    />
                                    <Text style={styles.title}>
                                        {item.title}
                                    </Text>
                                    <Text style={styles.date}>
                                        {moment(item.publishedAt).format('LLL')}
                                    </Text>
                                    <Text style={styles.newsDescription}>
                                        {item.description}
                                    </Text>
                                </View>
                                <Divider my={2} bg="#e0e0e0" />
                            </View>
                        )}
                        keyExtractor={(item) => item.id}
                    />
                ) : (
                    <View style={styles.spinner}>
                        <Spinner color="danger.400" />
                    </View>
                )}
            </ScrollView>
        </NativeBaseProvider>
    )
}

const styles = StyleSheet.create({
    newsContainer: {
        padding: 10
    },
    title: {
        fontSize: 18,
        marginTop: 10,
        fontWeight: "600"
    },
    newsDescription: {
        fontSize: 16,
        marginTop: 10
    },
    date: {
        fontSize: 14
    },
    spinner: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: 400
    }
});
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-21-210200.png)

Scroll down the Business Screen, and you will see the news related to Business.

And you can do the same for all the other screens:

```
useEffect(() => {
        services('business')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
}, [])
```

```
useEffect(() => {
        services('health')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
```

```
useEffect(() => {
        services('sports')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
```

```
useEffect(() => {
        services('technology')
            .then(data => {
                setNewsData(data)
            })
            .catch(error => {
                alert(error)
            })
    }, [])
```

## Conclusion

Congratulations! Now our news application is complete.

So go ahead, build and experiment with it a bit. There are tons of things you can do.

You can check out my playlist on [Build a News Application using React Native and Native Base](https://youtube.com/playlist?list=PLWgH1O_994O8KP1srByN1OmoiRpLF6lNO), which is on my YouTube channel.

Feel free to download the code here: [https://github.com/nishant-666/React-Native-News](https://github.com/nishant-666/React-Native-News)

> Happy Learning.

