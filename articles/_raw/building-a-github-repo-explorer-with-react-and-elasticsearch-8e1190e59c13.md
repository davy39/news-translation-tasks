---
title: Building a GitHub Repo Explorer with React and Elasticsearch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-10T21:57:37.000Z'
originalURL: https://freecodecamp.org/news/building-a-github-repo-explorer-with-react-and-elasticsearch-8e1190e59c13
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QunMstJjXbPkRfFwRBVVkg.png
tags:
- name: elasticsearch
  slug: elasticsearch
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Divyanshu Maithani


  _The [GitXplore](https://appbaseio-apps.github.io/gitxplore-app/" rel="noopener"
  target="blank" title=") app

  Elasticsearch is one of the most popular full-text search engines which allows you
  to search huge volumes of data quic...'
---

By Divyanshu Maithani

![Image](https://cdn-media-1.freecodecamp.org/images/1*QunMstJjXbPkRfFwRBVVkg.png)
_The [GitXplore](https://appbaseio-apps.github.io/gitxplore-app/" rel="noopener" target="_blank" title=") app_

[Elasticsearch](https://www.elastic.co/products/elasticsearch) is one of the most popular [full-text search](https://en.wikipedia.org/wiki/Full-text_search) engines which allows you to search huge volumes of data quickly, while [React](https://reactjs.org/) is arguably [the best library](http://stateofjs.com/2017/front-end/results/) for building user interfaces. During the past few months I’ve been co-authoring an open-source library, [**ReactiveSearch**](https://github.com/appbaseio/reactivesearch), which provides React components for Elasticsearch and simplifies the process of building a search User Interface (UI).

This is the app which I’ll be building in this story:

![Image](https://cdn-media-1.freecodecamp.org/images/1*KPB8Sq7N3WId2jL57VGT-Q.png)
_Check out the app on [CodeSandbox](https://codesandbox.io/s/github/appbaseio-apps/gitxplore-app/tree/master/" rel="noopener" target="_blank" title=")_

### A brief idea of Elasticsearch

Elasticsearch is a [NoSQL](https://en.wikipedia.org/wiki/NoSQL) database which can search through large amounts of data in a short time. It performs a [full-text search](https://en.wikipedia.org/wiki/Full-text_search) on the data which is stored in the form of documents (like objects) by examining all the words in every document.

Here’s what the [Elasticsearch docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html) say:

> Elasticsearch is a highly scalable open-source full-text search and analytics engine. It allows you to store, search, and analyze big volumes of data quickly and in near real time.

Even if you’ve never used Elasticsearch before you should be able to follow along with this story and build your very own Elasticsearch powered search using React and ReactiveSearch. ?

### What is ReactiveSearch?

[ReactiveSearch](https://github.com/appbaseio/reactivesearch) is a React UI components library for Elasticsearch. In order to search data in Elasticsearch, you need to write [**queries**](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html). Then you will need to format and render the JSON data in your UI. ReactiveSearch simplifies the entire process since you don’t need to worry about writing these queries. This makes it easier to focus on creating the UI.

Here is an example that generates a search-box UI with category specific suggestions:

```js
<CategorySearch
  componentId="repo"
  dataField={["name", "name.raw"]}
  categoryField="language.raw"
/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*2wZ7uDqfizcjV9JCnre0mQ.png)
_Component rendered from the above code_

This would likely have taken us 100+ lines without the library, and knowledge of [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) to construct the query.

In this post, I’ll use different components from the library to build the final UI.

You should try out [the final app](https://appbaseio-apps.github.io/gitxplore-app/) before we deep-dive. Here’s the [CodeSandbox link](https://codesandbox.io/s/github/appbaseio-apps/gitxplore-app/tree/master/) for the same.

### Setting things up

Before we start building the UI, we’ll need the dataset containing GitHub repositories in Elasticsearch. ReactiveSearch works with any Elasticsearch index and you can easily [use it with your own dataset](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html).

For brevity, you can use [my dataset](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJDAQAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFsoFSyhi0TotY1ZI3dCbzpZ5wZmCa4HoWjWiBHcRO1KpPWzrR3-ungbYF_FBD7IY3vlhuTW9dQQFtt3qksr-wGqyFf_qxW2Z3widjMRY5xGpv9lCIh4b5Dyi-O2wVMmUzKADc-0pG1tyzQ558Y_SoViZ27V2qq-px_fIGV-GVRTcrO-LdiYhDhtFK4tYVTak07UxRRvGaqeK3GI2sU7O67YnSdDZNv8_5pnc3SPxlPV9t9YdkGW3YkckG3LAVp03TbrSWI7GdN0fMZCgwqWv0FP1iNWHQrUW2v8-B___Y4BHg) or clone it for yourself by following [this link](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJDAQAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFsoFSyhi0TotY1ZI3dCbzpZ5wZmCa4HoWjWiBHcRO1KpPWzrR3-ungbYF_FBD7IY3vlhuTW9dQQFtt3qksr-wGqyFf_qxW2Z3widjMRY5xGpv9lCIh4b5Dyi-O2wVMmUzKADc-0pG1tyzQ558Y_SoViZ27V2qq-px_fIGV-GVRTcrO-LdiYhDhtFK4tYVTak07UxRRvGaqeK3GI2sU7O67YnSdDZNv8_5pnc3SPxlPV9t9YdkGW3YkckG3LAVp03TbrSWI7GdN0fMZCgwqWv0FP1iNWHQrUW2v8-B___Y4BHg) and clicking on _Clone this App_ button. This will let you make a copy of the dataset as your own app.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5tXgJvJROclI-NFXUKziIQ.png)
_The GitHub repo [dataset](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJDAQAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFsoFSyhi0TotY1ZI3dCbzpZ5wZmCa4HoWjWiBHcRO1KpPWzrR3-ungbYF_FBD7IY3vlhuTW9dQQFtt3qksr-wGqyFf_qxW2Z3widjMRY5xGpv9lCIh4b5Dyi-O2wVMmUzKADc-0pG1tyzQ558Y_SoViZ27V2qq-px_fIGV-GVRTcrO-LdiYhDhtFK4tYVTak07UxRRvGaqeK3GI2sU7O67YnSdDZNv8_5pnc3SPxlPV9t9YdkGW3YkckG3LAVp03TbrSWI7GdN0fMZCgwqWv0FP1iNWHQrUW2v8-B___Y4BHg" rel="noopener" target="_blank" title=")_

After you enter an app name, the cloning process should start importing the 26K+ repos to your account.

All the repos are structured in the following format:

```json
{
  "name": "freeCodeCamp",
  "owner": "freeCodeCamp",
  "fullname": "freeCodeCamp~freeCodeCamp",
  "description": "The https://freeCodeCamp.org open source codebase and curriculum. Learn to code and help nonprofits.",
  "avatar": "https://avatars0.githubusercontent.com/u/9892522?v=4",
  "url": "https://github.com/freeCodeCamp/freeCodeCamp",
  "pushed": "2017-12-24T05:44:03Z",
  "created": "2014-12-24T17:49:19Z",
  "size": 31474,
  "stars": 291526,
  "forks": 13211,
  "topics": [
    "careers",
    "certification",
    "community",
    "curriculum",
    "d3",
    "education",
    "javascript",
    "learn-to-code",
    "math",
    "nodejs",
    "nonprofits",
    "programming",
    "react",
    "teachers"
  ],
  "language": "JavaScript",
  "watchers": 8462
}
```

* We will use [create-react-app](https://github.com/facebookincubator/create-react-app.) to set up the project. You can install create-react-app by running the following command in your terminal:

```bash
npm install -g create-react-app
```

* After it’s installed, you can create a new project by running:

```bash
create-react-app gitxplore
```

* After the project is set up you can change into the project directory and install ReactiveSearch dependency:

```bash
cd gitxplore
npm install @appbaseio/reactivesearch
```

* You may also add fontawesome CDN, which we’ll be using for some icons, by inserting the following lines in `/public/index.html` before the `</body>` tag ends:

```html
<script defer         src="https://use.fontawesome.com/releases/v5.0.2/js/all.js"></script>
```

### Diving into the code

I’ll follow a simple directory structure for the app. Here are the important files:

```
src
├── App.css               // App styles
├── App.js                // App container
├── components
│   ├── Header.js         // Header component
│   ├── Results.js        // Results component
│   ├── SearchFilters.js  // Filters component
│   └── Topic.js          // rendered by Results
├── index.css             // styles
├── index.js              // ReactDOM render
└── theme.js              // colors and fonts
public
└── index.html
```

Here’s the link to [final repo](https://github.com/appbaseio-apps/gitxplore-app) if you wish to reference anything at any point.

#### 1. Adding styles

I’ve written responsive styles for the app which you can copy into your app. Just fire up your favorite text editor and copy the styles for `/src/index.css` from [here](https://github.com/appbaseio-apps/gitxplore-app/blob/master/src/index.css) and `/src/App.css` from [here](https://github.com/appbaseio-apps/gitxplore-app/blob/master/src/App.css) respectively.

Now, create a file `/src/theme.js` where we’ll add the colors and fonts for our app:

```js
const theme = {
	typography: {
		fontFamily: 'Raleway, Helvetica, sans-serif',
	},
	colors: {
		primaryColor: '#008000',
		titleColor: 'white'
	},
	secondaryColor: 'mediumseagreen',
};

export default theme;
```

#### 2. Adding the first ReactiveSearch component

All the ReactiveSearch components are wrapped around a container component [**ReactiveBase**](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html) which provides data from Elasticsearch to the children ReactiveSearch components.

We’ll use this in `/src/App.js`:

```js
import React, { Component } from 'react';
import { ReactiveBase } from '@appbaseio/reactivesearch';
import theme from './theme';
import './App.css';
class App extends Component {
  render() {
    return (
      <section className="container">
        <ReactiveBase
          app="gitxplore-app"
          credentials="4oaS4Srzi:f6966181-1eb4-443c-8e0e-b7f38e7bc316"
          type="gitxplore-latest"
          theme={theme}
        >
          <nav className="navbar">
            <div className="title">GitXplore</div>
          </nav>
        </ReactiveBase>
      </section>
    );
  }
}
export default App;
```

For the `app` and `credentials` prop you may use the ones I’ve provided here as it is. If you cloned the dataset in your own app earlier you can get them from the [app’s credentials page](https://dashboard.appbase.io/credentials). If you’re already familiar with Elasticsearch you may instead pass a `url` prop referring to [your own Elasticsearch cluster URL](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html#props).

![Image](https://cdn-media-1.freecodecamp.org/images/1*bI_3-Hej71eLbiVCGoK_hw.png)
_Getting app’s credentials from appbase.io [dashboard](https://dashboard.appbase.io/credentials" rel="noopener" target="_blank" title="). Just copy the Read-only API key_

Alternatively, you can also copy your app’s `credentials` from the [apps dashboard](https://dashboard.appbase.io/apps). Hover over your app’s card and click on _Copy Read Credentials_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5k1jVr3YHGBQ0Ts02gjL7g.png)
_Alternative to above link: Copy the read credentials from [apps dashboard](https://dashboard.appbase.io/apps" rel="noopener" target="_blank" title=")_

After adding this you would see a basic layout like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*P4WcAczVGDzrTm42prVSGA.png)
_After adding the first ReactiveSearch component_

#### 3. Adding a DataSearch

![Image](https://cdn-media-1.freecodecamp.org/images/1*yNVLrcjB1KEz1X_1s4RHaQ.png)
_DataSearch component_

Next, I’ll be adding a [DataSearch](https://opensource.appbase.io/reactive-manual/search-components/datasearch.html) component to search through repositories. It creates a search UI component and lets us search across one or more fields easily. The updated `render` function in `/src/App.js` would look like this:

```js
// importing DataSearch here
import { ReactiveBase, DataSearch } from '@appbaseio/reactivesearch';
...
<ReactiveBase ... >
// Adding the DataSearch here
    <div className="flex row-reverse app-container">
        <div className="results-container">
            <DataSearch
                componentId="repo"
                filterLabel="Search"
                dataField={['name', 'description', 'name.raw', 'fullname', 'owner', 'topics']}
                placeholder="Search Repos"
                autosuggest={false}
                iconPosition="left"
                URLParams
                className="data-search-container results-container"
                innerClass={{
                    input: 'search-input',
                }}
            />
        </div>
    </div>
</ReactiveBase>
...
```

The `DataSearch` component goes inside the `ReactiveBase` component and receives all the necessary data from it so we don’t have to write Elasticsearch queries ourselves. The surrounding `div`s add some `className` properties for styling. These just add a layout to the app. You can go through all the styles at `/src/App.css` which we created earlier. You might have noticed that we have passed some props to the `DataSearch` component.

Here’s how they work:

* `componentId`: a unique string identifier which we’ll use later to connect two different ReactiveSearch components.
* `filterLabel`: a string value which will show up in the filters menu later.
* `dataField`: an array of strings containing Elasticsearch fields on which search has to performed on. You can check [the dataset](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJiAQAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFsg1HFhlgIIPlpmP5RRZ-FWEcoSd0PjkMiILXm8GQxirVSZVrDiQlmtqn4TuMTBL2E1thSmnTeiFPBGQoqmavHhOSSrRxNeEjhNKDeff0pgxw5r5nv8t-un2YUoHpv1HKzI9aZA8KH8WAmQ6XktDDO-Hn95KeD_KPXp_E76PZ04Hl6H6MrevzUojYDnGynyNwjmI07lj0kXZeqltXcATyP8PMY7ncPHlUw1p1cnfe2JXyFgzRzZcNo7xtVJiEPCuLLKzxYehuirtvUcy6oC_KC15q9kmkWssXUCkBr7dAugoFbtjO5zUdpOFWdcz2wcD3AA3--k7h&editable=false) and see that these fields also matches the column name. All fields specified here matches the structure of data, for example `name` refers to the name of repo, `description` refers to its description, but there is a field with a `.raw` added here, `name.raw` which is a [multi-field](https://www.elastic.co/guide/en/elasticsearch/reference/current/multi-fields.html) of the `name` field. Elasticsearch can index the same data in different ways for different purposes, which we can use to get better search results.
* `placeholder`: sets the placeholder value in the input box.
* `autosuggest`: setting a `false` value for the prop causes the results to update immediately in the results.
* `iconPosition`: sets the position of the ? icon.
* `URLParams`: is a `boolean` which tells the component to save the search term in the browser’s URL so we can share a URL to a specific search query. For example, check [this link](https://appbaseio-apps.github.io/gitxplore-app/?repo=%22react%22) to see all results related to “react”.
* `className`: adds a `class` for styling using CSS.
* `innerClass`: adds a `class` to different sections of a component for styling using CSS. Here, I’ve added a `class` to the `input` box for styling. A detailed description can be found in the [docs](https://opensource.appbase.io/reactive-manual/search-components/datasearch.html#props).

With this, our app should get a working search bar:

![Image](https://cdn-media-1.freecodecamp.org/images/1*OLNYIuRpYi9AuPckJ9G_4w.png)
_Adding DataSearch component_

#### 4. Adding the Results view

Next, we’ll be adding the `Results` component at `/src/components/Results.js` and importing it in `/src/App.js`.

Here’s how you can write the `Results` component:

```js
import React from 'react';
import { SelectedFilters, ReactiveList } from '@appbaseio/reactivesearch';
const onResultStats = (results, time) => (
  <div className="flex justify-end">
    {results} results found in {time}ms
  </div>
);
const onData = (data) => (
  <div className="result-item" key={data.fullname}>
    {data.owner}/{data.name}
  </div>
);
const Results = () => (
  <div className="result-list">
    <SelectedFilters className="m1" />
    <ReactiveList
      componentId="results"
      dataField="name"
      onData={onData}
      onResultStats={onResultStats}
      react={{
        and: ['repo'],
      }}
      pagination
      innerClass={{
        list: 'result-list-container',
        pagination: 'result-list-pagination',
        resultsInfo: 'result-list-info',
        poweredBy: 'powered-by',
      }}
      size={6}
    />
  </div>
);
export default Results;
```

I’ve imported two new components from ReactiveSearch, `SelectedFilters` and `ReactiveList`. [SelectedFilters](https://opensource.appbase.io/reactive-manual/base-components/selectedfilters.html) will render the filters for our ReactiveSearch components at one place:

![Image](https://cdn-media-1.freecodecamp.org/images/1*FAROoZa3fhXuE5-H8_FJog.png)
_SelectedFilters renders removable filters_

[ReactiveList](https://opensource.appbase.io/reactive-manual/result-components/reactivelist.html) renders the search results. Here’s how its props work:

* `dataField`: orders the results using `name` field here.
* `onData`: accepts a function which returns a [JSX](https://reactjs.org/docs/glossary.html#jsx). The function is passed each result individually. Here we’re generating a basic UI which we’ll modify later.
* `onResultStats`: similar to `onData` but for the result stats. The function is passed the number of `results` found and `time` taken.
* `react`: the `[react](https://opensource.appbase.io/reactive-manual/advanced/react.html)` prop tells the `ReactiveList` to listen to changes made by`CategorySearch` component, we’ve provided the `componentId` of the `CategorySearch` component here called `repo`. Later we’ll add more components here.
* `pagination`: a `boolean` which tells the ReactiveList to split the results into pages, each page containing the number of results specified in the `size` prop.

Now we can `import` and use the `Results` component in `/src/App.js`. Just add it inside the `div` with `results-container` class.

```js
...
import Results from './components/Results';
...
render() {
  return(
    ...
    <div className="results-container">
      <DataSearch ... />
      <Results />
    </div>
    ...
  )
}
```

With this component, a basic version of our search UI should start coming together:

![Image](https://cdn-media-1.freecodecamp.org/images/1*txovjxQldUv-T2V5ALzP_Q.png)
_Adding the Results component_

#### 5. Adding a Header component

Lets create a `Header` component at `/src/components/Header.js` which we’ll use to render more search filters.

Here’s how to create a simple `Header` component:

```js
import React, { Component } from 'react';

import SearchFilters from './SearchFilters';

class Header extends Component {
	constructor(props) {
		super(props);
		this.state = {
			visible: false,
		};
	}

	toggleVisibility = () => {
		const visible = !this.state.visible;
		this.setState({
			visible,
		});
	}

	render() {
		return (
			<nav className={`navbar ${this.state.visible ? 'active' : ''}`}>
				<div className="title">GitXplore</div>
				<div className="btn toggle-btn" onClick={this.toggleVisibility}>Toggle Filters</div>
				<SearchFilters {...this.props} visible={this.state.visible} />
			</nav>
		);
	}
}

export default Header;

```

I’ve moved the navigation code in `<nav>..</nav>` from `/src/App.js` here. The Header component has a method which toggles visible in the state. We’re using this to add a class which would make it take up the entire screen size on mobile layout. I’ve also added a toggle button which calls the `toggleVisibility` method.

It also renders another component called `SearchFilters` and passes all the props from the parent `App` component. Let’s create this component to see things in action.

Create a new file `/src/components/SearchFilters.js`:

```js
import React from 'react';
const SearchFilters = () => (
    <div>
        Search filters go here!
    </div>
);
export default SearchFilters;
```

Next, I’ll update the `App` component to use the `Header` component that we created just now.

#### 6. Updating App component and handling topics in state

We’ll add a `state` variable in `App` component called `currentTopics` which would be an array of currently selected topics in the app.

We’ll then use the `currentTopics` and pass them to the `Header` and `Results` components:

```js
import React, { Component } from 'react';
import { ReactiveBase, DataSearch } from '@appbaseio/reactivesearch';

import Header from './components/Header';
import Results from './components/Results';

import theme from './theme';
import './App.css';

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			currentTopics: [],
		};
	}

	setTopics = (currentTopics) => {
		this.setState({
			currentTopics: currentTopics || [],
		});
	}

	toggleTopic = (topic) => {
		const { currentTopics } = this.state;
		const nextState = currentTopics.includes(topic)
			? currentTopics.filter(item => item !== topic)
			: currentTopics.concat(topic);
		this.setState({
			currentTopics: nextState,
		});
	}

	render() {
		return (
			<section className="container">
				<ReactiveBase
					app="gitxplore-app"
					credentials="4oaS4Srzi:f6966181-1eb4-443c-8e0e-b7f38e7bc316"
					type="gitxplore-latest"
					theme={theme}
				>
					<div className="flex row-reverse app-container">
						<Header currentTopics={this.state.currentTopics} setTopics={this.setTopics} />
						<div className="results-container">
							<DataSearch
								componentId="repo"
								filterLabel="Search"
								dataField={['name', 'description', 'name.raw', 'fullname', 'owner', 'topics']}
								placeholder="Search Repos"
								iconPosition="left"
								autosuggest={false}
								URLParams
								className="data-search-container results-container"
								innerClass={{
									input: 'search-input',
								}}
							/>
							<Results currentTopics={this.state.currentTopics} toggleTopic={this.toggleTopic} />
						</div>
					</div>
				</ReactiveBase>
			</section>
		);
	}
}

export default App;
```

The `setTopics` method will set whichever topics are passed to it, which we’ll pass to the `Header` component. The `toggleTopic` method will remove a topic from the `state` in `currentTopics` if it’s already present and add the topic if it is not present.

We’ll pass the `toggleTopic` method to the `Results` component:

![Image](https://cdn-media-1.freecodecamp.org/images/1*3Or7_Pwz3wpkUcDv-gryFQ.png)
_Its starting to come together, cheers!_

#### 7. Adding more filters

Lets add more filters to the UI in `/src/components/SearchFilters.js`. I’ll be using three new components from ReactiveSearch here, `MultiDropdownList`, `SingleDropdownRange` and `RangeSlider`. The components are used in a similar fashion as we used the `DataSearch` component earlier.

Here’s the code:

```js
import React from 'react';
import PropTypes from 'prop-types';
import {
	MultiDropdownList,
	SingleDropdownRange,
	RangeSlider,
} from '@appbaseio/reactivesearch';

const SearchFilters = ({ currentTopics, setTopics, visible }) => (
	<div className={`flex column filters-container ${!visible ? 'hidden' : ''}`}>
		<div className="child m10">
			<MultiDropdownList
				componentId="language"
				dataField="language.raw"
				placeholder="Select languages"
				title="Language"
				filterLabel="Language"
			/>
		</div>
		<div className="child m10">
			<MultiDropdownList
				componentId="topics"
				dataField="topics.raw"
				placeholder="Select topics"
				title="Repo Topics"
				filterLabel="Topics"
				size={1000}
				queryFormat="and"
				defaultSelected={currentTopics}
				onValueChange={setTopics}
			/>
		</div>
		<div className="child m10">
			<SingleDropdownRange
				componentId="pushed"
				dataField="pushed"
				placeholder="Repo last active"
				title="Last Active"
				filterLabel="Last Active"
				data={[
					{ start: 'now-1M', end: 'now', label: 'Last 30 days' },
					{ start: 'now-6M', end: 'now', label: 'Last 6 months' },
					{ start: 'now-1y', end: 'now', label: 'Last year' },
				]}
			/>
		</div>
		<div className="child m10">
			<SingleDropdownRange
				componentId="created"
				dataField="created"
				placeholder="Repo created"
				title="Created"
				filterLabel="Created"
				data={[
					{
						start: '2017-01-01T00:00:00Z',
						end: '2017-12-31T23:59:59Z',
						label: '2017',
					},
					{
						start: '2016-01-01T00:00:00Z',
						end: '2016-12-31T23:59:59Z',
						label: '2016',
					},
					{
						start: '2015-01-01T00:00:00Z',
						end: '2015-12-31T23:59:59Z',
						label: '2015',
					},
					{
						start: '2014-01-01T00:00:00Z',
						end: '2014-12-31T23:59:59Z',
						label: '2014',
					},
					{
						start: '2013-01-01T00:00:00Z',
						end: '2013-12-31T23:59:59Z',
						label: '2013',
					},
					{
						start: '2012-01-01T00:00:00Z',
						end: '2012-12-31T23:59:59Z',
						label: '2012',
					},
					{
						start: '2011-01-01T00:00:00Z',
						end: '2011-12-31T23:59:59Z',
						label: '2011',
					},
					{
						start: '2010-01-01T00:00:00Z',
						end: '2010-12-31T23:59:59Z',
						label: '2010',
					},
					{
						start: '2009-01-01T00:00:00Z',
						end: '2009-12-31T23:59:59Z',
						label: '2009',
					},
					{
						start: '2008-01-01T00:00:00Z',
						end: '2008-12-31T23:59:59Z',
						label: '2008',
					},
					{
						start: '2007-01-01T00:00:00Z',
						end: '2007-12-31T23:59:59Z',
						label: '2007',
					},
				]}
			/>
		</div>
		<div className="child m10">
			<RangeSlider
				componentId="stars"
				title="Repo Stars"
				dataField="stars"
				range={{ start: 0, end: 300000 }}
				showHistogram={false}
				rangeLabels={{
					start: '0 Stars',
					end: '300K Stars',
				}}
				innerClass={{
					label: 'range-label',
				}}
			/>
		</div>
		<div className="child m10">
			<RangeSlider
				componentId="forks"
				title="Repo Forks"
				dataField="forks"
				range={{ start: 0, end: 180500 }}
				showHistogram={false}
				rangeLabels={{
					start: '0 Forks',
					end: '180K Forks',
				}}
				innerClass={{
					label: 'range-label',
				}}
			/>
		</div>
	</div>
);

SearchFilters.propTypes = {
	currentTopics: PropTypes.arrayOf(PropTypes.string),
	setTopics: PropTypes.func,
	visible: PropTypes.bool,
};

export default SearchFilters;

```

The `SearchFilters` component we’ve created above takes in three props from the `Header` component, `currentTopics`, `setTopics` and `visible`. The `visible` prop is just used to add a `className` for styling.

The first component we’ve used here is a `[MultiDropdownList](https://opensource.appbase.io/reactive-manual/list-components/multidropdownlist.html)` which renders a dropdown component to select multiple options. The first `MultiDropdownList` has a `dataField` of `language.raw`. It’ll populate itself with all the languages available in the repositories dataset.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BwqnE21ABLW5q-xeCocmFA.png)
_The language [MultiDropdownList](https://opensource.appbase.io/reactive-manual/list-components/multidropdownlist.html" rel="noopener" target="_blank" title=")_

We’ve used another `MultiDropdownList` to render a list of topics:

```js
<MultiDropdownList
    componentId="topics"
    dataField="topics.raw"
    placeholder="Select languages"
    title="Repo Topics"
    filterLabel="Topics"
    size={1000}
    queryFormat="and"
    defaultSelected={currentTopics}
    onValueChange={setTopics}
/>
```

Here’s how the props work here:

* `componentId`: similar to the previous ReactiveSearch components, this is a unique identifier which we’ll later associate in the `Results` component that we created to get search results.
* `dataField`: maps the component to the `topics.raw` field in Elasticsearch.
* `placeholder`: sets the placeholder value when nothing is selected.
* `title`: adds a title for the component in the UI.
* `filterLabel`: sets the label of the components in the removable filters (the `SelectedFilters` which we used in the `Results` component).
* `size`: tells the component to render a maximum of `1000` items in the list.
* `queryFormat`: when set to `'and'` as we’ve used here, it gives results which matches all the selected tags (exactly like [intersection](https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwjq2aSbmLLYAhUBP48KHW7QDVMQFghHMAE&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FIntersection_(set_theory)&usg=AOvVaw3o-ni_Iic1U3sedPMsJMqV)).
* `defaultSelected`: sets the selected items in the component. Here we’re passing `currentTopics` which we’ve stored in the `state` at `/src/App.js`.
* `onValueChange`: is a function that will be called by the component when we make a change in its value. Here we call the `setTopics` function which we received in the props. Therefore, whenever we select or deselect a value in the component it would update the `currentTopics` in the `state` of main `App` component.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GPqMulHiFqd35bXmay2Cww.png)
_The topics MultiDropdownList component_

The next ReactiveSearch component we’ve used here is a `[SingleDropdownRange](https://opensource.appbase.io/reactive-manual/range-components/singledropdownrange.html)`. It uses a new prop called `[data](https://opensource.appbase.io/reactive-manual/range-components/singledropdownrange.html#props)`.

Here’s how it works:

```js
<SingleDropdownRange
    ...
    data={[
        { start: 'now-1M', end: 'now', label: 'Last 30 days' },
        { start: 'now-6M', end: 'now', label: 'Last 6 months' },
        { start: 'now-1y', end: 'now', label: 'Last year' },
    ]}
/>
```

The `data` prop accepts an array of objects with `start` and `end` values and shows the specified `label` in the dropdown. It’s mapped to the `pushed` field in the dataset which is a [date type in Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/date.html). One cool way to specify date range in Elasticsearch is using the `now` keyword. `now` refers to the current time, `now-1M` refers to one month before, `now-6M` to six month before and `now-1y` to a year before `now`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g6uRRdk37VyzQEqDIX_CCg.png)
_The pushed [SingleDropdownRange](https://opensource.appbase.io/reactive-manual/range-components/singledropdownrange.html" rel="noopener" target="_blank" title=") component_

I’ve used another `SingleDropdownRange` component for the `created` field in the dataset.

Here I’ve specified year ranges in datetime for different years:

```js
<SingleDropdownRange
    ...
    data={[
        {
            start: '2017-01-01T00:00:00Z',
            end: '2017-12-31T23:59:59Z',
            label: '2017',
        },
        {
            start: '2016-01-01T00:00:00Z',
            end: '2016-12-31T23:59:59Z',
            label: '2016',
        },
       ...
    ]}
/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*V1J8UQXBUCWJd4-EuC5I7w.png)
_SingleDropdownRange component for the created field_

The third component I’ve used is a `[RangeSlider](https://opensource.appbase.io/reactive-manual/range-components/rangeslider.html)` which renders a slider UI. I’ve used to `RangeSlider` components, one for the `stars` field and the other for `forks`.

Two main props that this component introduces are `range` and `rangeLabels`:

```js
<RangeSlider
    ...
    showHistogram={false}
    range={{ start: 0, end: 300000 }}
    rangeLabels={{
        start: '0 Stars',
        end: '300K Stars',
    }}
/>
```

* `range`: prop specifies a range for the data with a `start` and `end` value.
* `rangeLabels`: prop takes the labels to show below the slider.
* `showHistogram`: is a `boolean` prop which shows a histogram with the distribution of data. Here I’ve set it to `false` since it’s not needed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s98sSECpz1cX-9Q_jbUyLQ.png)
_[RangeSlider](https://opensource.appbase.io/reactive-manual/range-components/rangeslider.html" rel="noopener" target="_blank" title=") components for the stars and forks fields_

Now we just need to connect these filters to the `Results` component. We just have to update one line in the `ReactiveList` rendered by the `Results` component to include the `componentId`s of these components.

Update the `react` prop in the `ReactiveList` that we rendered in the `Results` component:

```js
const Results = () => (
  <div className="result-list">
    <SelectedFilters className="m1" />
    <ReactiveList
      ... // updating the react prop here
      react={{
        and: ['language', 'topics', 'pushed', 'created', 'stars', 'forks', 'repo'],
      }}
    />
  </div>
);
```

That should make your results update for all the filters ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*fAMt45ayVCNTLy77EI7Szg.png)
_After connecting the filters in the ReactiveList component_

#### 8. Updating the results view

Up until now, we’ve been seeing only a basic version of the results. As the final piece of this app, lets add some flair to the results ✌️

We’ll be using another component inside our `Results` components to render different topics.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AyocrMQaO0TQWoYcbhoHlA.png)
_Topics component to render these little guys_

Here’s how you can create your own at `/src/components/Topic`. Feel free to add your own taste ?

```js

import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Topic extends Component {
	handleClick = () => {
		this.props.toggleTopic(this.props.children);
	}
	render() {
		return (
			<div className={`topic ${this.props.active ? 'active' : ''}`} onClick={this.handleClick}>
				#{this.props.children}
			</div>
		);
	}
}

Topic.propTypes = {
	children: PropTypes.string,
	active: PropTypes.bool,
	toggleTopic: PropTypes.func,
};

export default Topic;
```

This component renders its `children` and adds a click handler to toggle the topics which updates the `currentTopics` inside the main `App` component’s state.

Next, we just need to update our `Results` component at `/src/components/Results.js`:

```js
import React from 'react';
import { SelectedFilters, ReactiveList } from '@appbaseio/reactivesearch';
import PropTypes from 'prop-types';

import Topic from './Topic';

const onResultStats = (results, time) => (
	<div className="flex justify-end">
		{results} results found in {time}ms
	</div>
);

const onData = (data, currentTopics, toggleTopic) => (
	<div className="result-item" key={data.fullname}>
		<div className="flex justify-center align-center result-card-header">
			<img className="avatar" src={data.avatar} alt="User avatar" />
			<a className="link" href={data.url} target="_blank" rel="noopener noreferrer">
				<div className="flex wrap">
					<div>{data.owner}/</div>
					<div>{data.name}</div>
				</div>
			</a>
		</div>
		<div className="m10-0">{data.description}</div>
		<div className="flex wrap justify-center">
			{
				data.topics.slice(0, 7)
					.map(item => (
						<Topic
							key={item}
							active={currentTopics.includes(item)}
							toggleTopic={toggleTopic}
						>
							{item}
						</Topic>
					))
			}
		</div>
		<div className="flex">
			<div><div className="btn card-btn"><i className="card-icon fas fa-star" />{data.stars}</div></div>
			<div><div className="btn card-btn"><i className="card-icon fas fa-code-branch" />{data.forks}</div></div>
			<div><div className="btn card-btn"><i className="card-icon fas fa-eye" />{data.watchers}</div></div>
		</div>
	</div>
);

const Results = ({ toggleTopic, currentTopics }) => (
	<div className="result-list">
		<SelectedFilters className="m1" />
		<ReactiveList
			componentId="results"
			dataField="name"
			onData={data => onData(data, currentTopics, toggleTopic)}
			onResultStats={onResultStats}
			react={{
				and: ['language', 'topics', 'pushed', 'created', 'stars', 'forks', 'repo'],
			}}
			pagination
			innerClass={{
				list: 'result-list-container',
				pagination: 'result-list-pagination',
				resultsInfo: 'result-list-info',
				poweredBy: 'powered-by',
			}}
			size={6}
			sortOptions={[
				{
					label: 'Best Match',
					dataField: '_score',
					sortBy: 'desc',
				},
				{
					label: 'Most Stars',
					dataField: 'stars',
					sortBy: 'desc',
				},
				{
					label: 'Fewest Stars',
					dataField: 'stars',
					sortBy: 'asc',
				},
				{
					label: 'Most Forks',
					dataField: 'forks',
					sortBy: 'desc',
				},
				{
					label: 'Fewest Forks',
					dataField: 'forks',
					sortBy: 'asc',
				},
				{
					label: 'A to Z',
					dataField: 'owner.raw',
					sortBy: 'asc',
				},
				{
					label: 'Z to A',
					dataField: 'owner.raw',
					sortBy: 'desc',
				},
				{
					label: 'Recently Updated',
					dataField: 'pushed',
					sortBy: 'desc',
				},
				{
					label: 'Least Recently Updated',
					dataField: 'pushed',
					sortBy: 'asc',
				},
			]}
		/>
	</div>
);

Results.propTypes = {
	toggleTopic: PropTypes.func,
	currentTopics: PropTypes.arrayOf(PropTypes.string),
};

export default Results;
```

I’ve updated the `onData` function to render more detailed results. You’ll also notice a new `sortOptions` prop in the `ReactiveList`. This prop accepts an array of objects which renders a dropdown menu to select how you wish to sort the results. Each object contains a `label` to display as the list item, a `dataField` to sort the results on and a `sortBy` key which can either be `asc` (ascending) or `desc` (descending).

That’s it, your very own GitHub repository explorer should be live!

![Image](https://cdn-media-1.freecodecamp.org/images/1*RQ6EPM9NrDsvX_ZdkpB_cw.png)
_GitXplore [final app preview](https://appbaseio-apps.github.io/gitxplore-app/" rel="noopener" target="_blank" title=")_

### Useful links

1. GitXplore app [demo](https://appbaseio-apps.github.io/gitxplore-app/), [CodeSandbox](https://codesandbox.io/s/github/appbaseio-apps/gitxplore-app/tree/master/) and [source code](https://github.com/appbaseio-apps/gitxplore-app)
2. [ReactiveSearch GitHub repo](https://github.com/appbaseio/reactivesearch)
3. ReactiveSearch [docs](https://opensource.appbase.io/reactive-manual/)

Hope you enjoyed this story. If you have any thoughts or suggestions, please let me know and do share your version of the app in comments!

---

You may follow me on [twitter](https://twitter.com/divyanshu013) for latest updates. I've also started posting more recent posts on my personal [blog](https://divyanshu013.dev/).

