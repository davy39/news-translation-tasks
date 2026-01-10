---
title: How to build a nested drawer menu with React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-25T01:59:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-nested-drawer-menu-with-react-native-a1c2fdcab6c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rts2oeflx0NgkJ5wdhBUhg.png
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Dhruvdutt Jadhav

  Screen space is a precious commodity on mobile. The drawer menu (or “hamburger menu”)
  is one of the most popular navigation patterns that helps you save it while offering
  intuitive navigation. In this post, I will demystify how to...'
---

By Dhruvdutt Jadhav

Screen space is a precious commodity on mobile. The **drawer menu** (or “hamburger menu”) is one of the most popular navigation patterns that helps you save it while offering intuitive navigation. In this post, I will demystify how to build a nested (multi-level) drawer menu using [React Native](https://facebook.github.io/react-native/) and [React Navigation](https://reactnavigation.org/). ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*YYYyBYo_SjxfgVnIsZyKUQ.gif)
_Nested Drawers in React Native_

Try the live demo on [**mobile**](https://expo.io/@dhruvdutt/native-kitchensink)?or on w[eb.](https://expo.io/appetize-simulator?url=https://expo.io/@dhruvdutt/native-kitchensink&appetizeCode=pc_0dybu6gxac) ?_️_

### _Navigation in React Native ⚛️_

_Navigation forms the backbone of a huge majority of apps built for production. The look and feel of navigation are important for driving use and engagement in mobile apps._

_However, if you are React Native developer, there isn’t a clear opinion when it comes to building a navigation menu. React Native [recommends](https://facebook.github.io/react-native/docs/navigation.html) a bunch of libraries for navigation. Each has its strength, depending on your needs, but there’s no one clear winner for all use-cases._

_None of the navigation libraries currently support nested drawers out-of-the-box. But one of the libraries that provides a rich API to build custom solutions is [React Navigation](https://reactnavigation.org/) — a JavaScript-based navigation. It is strongly backed and maintained by the React Native community. This is what we’re going to use in this tutorial._

### _The use case ?️_

_I had to build a playground app to showcase a UI components library for React Native. It consists of eight different components, each supporting various props, and more than 50 different options._

_It was not possible to show all options inside the drawer at one time without a multi-level drawer which would scope the options based on the selected component. I couldn’t find a ready-made solution for this, so I needed to build a custom one._

### _Base setup ?_

_For the base setup, I’m assuming you already have a React Native project setup with either [CRNA](https://facebook.github.io/react-native/docs/getting-started.html), [Expo Kit](https://docs.expo.io/versions/latest/), or [React Native CLI](https://facebook.github.io/react-native/docs/getting-started.html). Make sure you have the [react-navigation](https://www.npmjs.com/package/react-navigation) library installed with either yarn or npm. We’ll start right off with using the navigation API._

> _Feel free to check the [getting-started guide](https://reactnavigation.org/docs/getting-started.html) before proceeding if you aren’t familiar with the React Navigation API._

_We’ll start with an example similar to the one documented in the React Navigation’s DrawerNavigator [official guide](https://reactnavigation.org/docs/drawer-based-navigation.html). We’ll create a simple drawer that has two drawer items: Home and Notifications._

![Image](https://cdn-media-1.freecodecamp.org/images/1*48Gg3UOqNIKZpDGDlJ9tFQ.png)
_Base Setup_

### _Custom drawer content_

_React Navigation enables all navigators to do a lot of customizations by passing a navigator config as the second parameter. We’ll use it to render some custom content other than the stock drawer items._

_`**DrawerNavigator**(RouteConfigs, DrawerNavigatorConfig)`_

_We’ll pass a prop called `[contentComponent](https://reactnavigation.org/docs/drawer-navigator.html#drawernavigatorconfig)` to the config which would allow us to render custom content for the drawer. We’ll use that to show a header and footer along with the prevailing `[DrawerItems](https://reactnavigation.org/docs/drawer-navigator.html#providing-a-custom-contentcomponent)` from `react-navigation`._

![Image](https://cdn-media-1.freecodecamp.org/images/1*wz9NtNNwoXfw5mv7fv2EmQ.png)
_DrawerNavigator: Content Component_

_This potentially unlocks a lot of things that can be done by controlling what to render inside the drawer._

### _Creating screen mapping_

_We need to build a nested drawer for each component that we want to showcase. So let’s first register all the screens with the DrawerNavigator’s [Config](https://reactnavigation.org/docs/drawer-navigator.html#drawernavigatorconfig). We’ve created a separate screen mapping file for components. You can very well have your own convention, or define the object directly similar to the Home screen component._

_The screen mapping consists of simple objects with screen property. The `screenMapping` object looks something like this:_

_After registering all components, the drawer would look something like this:_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rh-POAkjqZBruVHAdejFlw.png)
_Registering all components along with child options_

_This would render all the components along with their options. We have two main components: [DataSearch](https://opensource.appbase.io/reactive-manual/native/components/datasearch.html) and [TextField](https://opensource.appbase.io/reactive-manual/native/components/textfield.html). Each has options like “With Icon Position,” “With Placeholder,” and more. Our task is to segregate these into a list of only components (DataSearch, TextField)._

### _Grouping outer drawer_

_A pattern I followed in the mapping was to use a delimiter `_` to group together options from one component. For instance, the navigation keys I used were “DataSearch_Basic” and “DataSearch_With Icon Position”. This is exactly what is going to help us combine the options for a single component like DataSearch. We’ll evaluate uniquely all the components we need to show for the outer drawer._

_We’ll create a util function to evaluate outer drawer list items to render._

_This function will return an object with unique components for the main components like (DataSearch, TextField) that we’ll render on the screen with the help of the `contentComponent` custom component. We’ll also maintain a _boolean_ to determine the content rendered on the drawer at a particular instant._

_The `renderMainDrawerComponent` is just a function iterating over the keys of the components object. It renders custom outer drawer items built on top of simply `Text` and `View` from react-native. Check the full code [here](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/components/OuterDrawerItem.js)._

_This will render the drawer like this:_

![Image](https://cdn-media-1.freecodecamp.org/images/1*NeMPqRQBQJr4JChGL2SMmQ.png)
_Showing only the outer component drawer items_

### _Rendering the child drawer ?_

_Now, we need to show the options based on the component that is tapped. You might have noticed that in utils, we’re also extracting the start and end indexes of the component groups based on the delimiter pattern._

_For instance, DataSearch screens start at index 1 (index 0 is Home screen) and ends at 3. TextField starts at 3 and end at 5. We’ll use these indices to magically slice the `items` that are passed to `DrawerItems` based on the selected component and its indices._

_Now, after tapping on DataSearch, the drawer will yield into something like this:_

![Image](https://cdn-media-1.freecodecamp.org/images/1*WdWUmlaxr-NUQaOr5C7UIA.png)
_Child components for a selected component_

_We’ve also added a sweet back button which basically toggles a boolean to render the main drawer items. You can check the full code [here](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/drawers/MainDrawer.js)._

_Now, the only thing left to do is make the drawer items look cleaner by trimming the redundant component name. Again, the rich React Navigation API comes handy here._

_There are various properties we can pass with `[navigationOptions](https://reactnavigation.org/docs/stack-navigator.html#navigationoptions-used-by-stacknavigator)`. A particular one we’re going to use here is the `[title](https://reactnavigation.org/docs/stack-navigator.html#title)` prop with the screen mapping. This will let us remove the part before the first delimiter. So, “DataSearch_Basic” will show as “Basic” only._

![Image](https://cdn-media-1.freecodecamp.org/images/1*k9mp_b8adb_a6WJlVwx63Q.png)
_Child drawer items_

_That’s all. We can add as many items we want based on the delimiter pattern. The playground app we’ve built consists of eight main components and over 53 total options._

![Image](https://cdn-media-1.freecodecamp.org/images/1*7cawloWms3S3_t23c03L4g.png)

> _Here’s the [link](https://expo.io/@dhruvdutt/native-kitchensink) to the final app and the [codebase](https://github.com/appbaseio-apps/native-kitchensink)._

### _Summary ?_

* _**Base setup**: DrawerNavigation hello world from [docs](https://reactnavigation.org/docs/drawer-based-navigation.html)._
* _**Custom drawer content**: Render drawer items with `[contentComponent](https://reactnavigation.org/docs/drawer-navigator.html#providing-a-custom-contentcomponent)`._
* _**Screen mapping**: [Define](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/screenMapping.js) and [register](https://github.com/appbaseio-apps/native-kitchensink/blob/master/App.js#L14-L15) all drawers components._
* _**Group outer drawer**: [Read](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/utils.js#L1-L20) delimiter pattern to [group](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/drawers/MainDrawer.js#L67-L68) drawer items._
* _**Rendering child drawer**: [Slice](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/drawers/MainDrawer.js#L81) and render child drawer items._

### _Conclusion ?_

_We learned to build a multi-level drawer menu with React Native. We used React Navigation API to render a custom content component inside the drawer, and used the delimiter pattern for screen mapping. Use this pattern to build any level of nesting or conditional rendering for drawers._

### _ReactiveSearch ?_

_Provides UI components for Native and Web platform to build perfect search experiences. You can check all the components it offers by playing with the [playground app](https://expo.io/@dhruvdutt/native-kitchensink) itself or [by creating your own component](https://opensource.appbase.io/reactive-manual/native/advanced/reactivecomponent.html)._

_[**appbaseio/reactivesearch**](https://github.com/appbaseio/reactivesearch)_  
_[reactivesearch - A React and React Native UI components library for building data-driven apps](https://github.com/appbaseio/reactivesearch)github.com_

