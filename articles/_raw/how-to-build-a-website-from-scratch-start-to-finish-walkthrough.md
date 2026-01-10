---
title: How to Build a Website from Scratch – Start to Finish Walkthrough
subtitle: ''
author: Kunal Nalawade
co_authors: []
series: null
date: '2025-04-28T19:21:02.308Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-website-from-scratch-start-to-finish-walkthrough
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745260046049/62b5c730-dc06-49de-8bdd-2cd44facb9e9.png
tags:
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Hi, fellow developers!

  Building a website can feel overwhelming at first – especially when you''re staring
  at a blank HTML file, wondering how it ever turns into a real website on the internet.
  If you''re new to web development, you''ve probably asked y...'
---

Hi, fellow developers!

Building a website can feel overwhelming at first – especially when you're staring at a blank HTML file, wondering how it ever turns into a real website on the internet. If you're new to web development, you've probably asked yourself: *"Where do I even start?"*

Well, this tutorial is here to guide you through that journey. We'll build a simple website from scratch and walk through every step — all the way to deploying it on the internet.

Let’s dive in!

## Table of Contents

1. [Starting with the Website Idea](#heading-starting-with-the-website-idea)
    
2. [How to Set Up the Project](#heading-how-to-set-up-the-project)
    
3. [How to build the website](#heading-how-to-build-the-website)
    
4. [How to test the code](#heading-how-to-test-the-code)
    
5. [How to Push your code to Version Control](#heading-how-to-push-your-code-to-version-control)
    
6. [Deployment and Hosting](#heading-deployment-and-hosting)
    

## Starting with the Website Idea

We are going to a build a simple weather app that shows you today’s weather in your city. It will have the following features:

* Search by city name: User enters city name and fetches weather information
    
* Display the following weather information: temperature, weather condition and wind speed
    
* Error handling
    

This is a simple website with pretty basic features, and should be relatively easy to build.

Before we start, let’s go over some prerequisites. I assume you are already familiar with the basics of HTML, CSS and JavaScript. Knowing Git would be helpful, but it’s not necessary – you can still follow along with the steps in this article.

## How to Set Up the Project

Let’s begin by setting up the project. To keep things simple, we’ll just use HTML, CSS, and JavaScript to build the website. So, let’s create the following files:

```bash
weather-app/
│── index.html
│── style.css
│── script.js
```

Next, to get the weather data, we’ll use an open-source weather API form [Open-Meteo](https://open-meteo.com), since it’s free and doesn’t need an API key. It will provide us with the temperature, wind speed, and weather conditions.

Before we really dive in, make sure that you have Git installed in your system. If you don’t have Git, you can refer to [Git SCM](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for an installation guide on Mac and Windows. If you are not familiar with Git, then check out the following guides to get started:

* [Learn the Basics of Git in Under 10 Minutes](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/)
    
* [Full book on Git and GitHub + version control basics](https://www.freecodecamp.org/news/gitting-things-done-book/)
    
* [Getting Started with GitHub](https://docs.github.com/en/get-started/start-your-journey)
    

Now you can create and initialise your Git repository. To initialise a local repository, run the following command inside your project directory:

```bash
git init
```

Next, go to GitHub and create a new repository with the same name as your project. Refer to the [Quickstart guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories) if you are not familiar with the process. Run the commands shown on the screen once you have created the repository.

Once you’re done with these steps, we are ready to get started on the development process.

## How to Build the Website

In this phase, we’ll develop or code our website. By looking at the designs and requirements, we’ll decide how to approach the development of each component.

This is a simple, small website with few requirements. So we won’t be using any frameworks, just simple HTML,CSS and JavaScript. But, depending on how complex the requirements are, you may decide to use frameworks like React, Angular, and so on.

First, let’s create a basic layout of the webpage with HTML:

```xml
 <div class="container">
      <h1>Weather App</h1>
      <div class="searchContainer">
        <input
          class="inputField"
          id="cityField"
          placeholder="Enter city name..."
          type="text"
        />
        <button id="searchBtn">Search</button>
      </div>
      <div id="weatherContainer">
        <h2 id="cityName"></h2>
        <p id="temperature"></p>
        <p id="condition"></p>
        <p id="windSpeed"></p>
      </div>
      <p id="errorMessage"></p>
    </div>
    <script src="script.js"></script>
```

We have added the following:

* A search container that will contain our search field with an input to enter city name, and a Search button
    
* Another container that will display the weather information or error message once the user clicks on Search
    

Next, let’s style it with CSS:

```css
.container {
  max-width: 400px;
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin: auto;
}

.searchContainer {
  margin: 20px 0;
}

.inputField {
  padding: 10px;
  width: 70%;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.searchBtn {
  padding: 10px;
  background: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

#weatherContainer {
  display: none; /* Hide until data is available to display */
}

#errorMessage {
  color: red;
  font-weight: bold;
}
```

With HTML and CSS, we have built a static website that looks like this:

![Rendered Static UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1742722248758/46e8d7d8-c1dd-47d8-9697-03fb9d07229f.png align="center")

Now, let’s add some functionality to it with JavaScript. We’ll be calling the following endpoints:

* `/v1/search` for getting longitude and latitude by city name
    
* `v1/forecast` for getting weather info
    

First, let’s add an `onclick` handler to our button:

```javascript
document.getElementById("searchBtn").addEventListener("click", () => {
  const city = document.getElementById("cityField").value.trim();
  if (city) {
    getCoordinates(city);
  } else {
    showError("Please enter a city name");
  }
});
```

Clicking on the search button should call the above two APIs, one after the other. Let’s call the first API in the `getCoordinates` method:

```javascript
async function getCoordinates(city) {
  showError("");
  try {
    const response = await fetch(
      `https://geocoding-api.open-meteo.com/v1/search?name=${city}&count=1`
    );

    if (!response.ok) {
      throw new Error("City not found");
    }

    const data = await response.json();
    if (!data.results || data.results.length === 0) {
      throw new Error("Location not found");
    }

    const { latitude, longitude, name, country } = data.results[0];
    getWeather(latitude, longitude, name, country);
  } catch (error) {
    showError(error.message);
  }
}
```

Here, we call the first API to fetch coordinates, and check if the response is positive. If it isn’t we throw an error and show it in the DOM. If the coordinates are fetched successfully, we move forward and get the weather data for those coordinates:

```javascript
async function getWeather(latitude, longitude, city, country) {
  try {
    const response = await fetch(
      `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`
    );

    if (!response.ok) {
      throw new Error("Weather data not available");
    }

    const data = await response.json();
    displayWeather(data.current_weather, city, country);
  } catch (error) {
    showError(error.message);
  }
}
```

Here, again we do the same thing, handle any errors and render the weather data on the screen, inside the `displayWeather` method:

```javascript
function displayWeather(weather, city, country) {
  const weatherContainer = document.getElementById("weatherContainer");
  const cityHeader = document.getElementById("cityName");
  const temp = document.getElementById("temperature");
  const condition = document.getElementById("condition");
  const windSpeed = document.getElementById("windSpeed");

  const weatherCondition =
    weatherDescriptions[weather.weathercode] || "Unknown Condition";

  weatherContainer.style.display = "block";
  cityHeader.textContent = `${city}, ${country}`;
  temp.textContent = `Temperature: ${weather.temperature}°C`;
  condition.textContent = `Condition: ${weatherCondition}`;
  windSpeed.textContent = `Wind Speed: ${weather.windspeed} km/h`;
}
```

Next, the `showError` method contains our error handling logic. It will display any error on the screen.

```javascript
function showError(message) {
  const weatherContainer = document.getElementById("weatherContainer");
  weatherContainer.style.display = "none";
  const errorPara = document.getElementById("errorMessage");
  errorPara.textContent = message;
}
```

Alright, we’re done with the development part! Now it’s time to test our code.

## How to Test the Code

Whenever you develop a feature, you’ll want to make sure to test it thoroughly. One way to test is by considering all the ways a user might interact with your website. Then, check how your website behaves in each scenario or test case.

First, let's see if the website works as expected when given a valid city name. Enter a city name and click on search – it should display the weather information like this:

![Weather Data Visible for Mumbai](https://cdn.hashnode.com/res/hashnode/image/upload/v1743082937133/ab532ffe-2a48-4101-9d04-7c2eb10d944b.png align="center")

Next, let’s test our error handling, by adding gibberish in the input:

![Gibberish Input results in Location Not Found](https://cdn.hashnode.com/res/hashnode/image/upload/v1743082992278/8b8629a4-db3a-45b6-87fd-295be4386941.png align="center")

With this input, our API fails, and returns the above error, which is being displayed correctly.

Remember that our website is really simple, so we don’t have a lot of test cases. But in a real world website, a good practice is to make a list of test cases, and test your website against each of them.

In this context, we are doing functional testing to ensure that the website behaves as expected in different scenarios. This includes testing the core functionalities like searching for a city and handling errors. This type of testing is crucial because it verifies that the application performs its intended functions correctly.

In addition to this, you can perform other types of testing on a website:

* Unit Testing: Testing individual components or pieces of code in isolation
    
* Integration Testing: Testing interactions between different components of the website
    
* End to End Testing: Testing the entire application flow from start to finish
    

Once you are sure that the website is working as expected, it’s time to push your code to a remote repository like GitHub and release it into production – that is, on the internet.

## How to Push Your Code to Version Control

Before moving forward, you might be wondering why version control is important. Version control helps you keep track of changes in your code in an organized way. Here are the benefits:

* If something breaks in your code, you can revert back to a previous version if necessary.
    
* Your project is safely stored on GitHub, so you won’t lose progress.
    
* With [branches](https://www.atlassian.com/git/tutorials/using-branches), you can work on different features at the same time, without them interfering with each other, or the main code. This is helpful especially when there are multiple people working on the project.
    
* Deployment and Hosting platforms like Netlify integrate seamlessly with version control systems like GitHub.
    

Let’s push our code to Github now. Make sure you have run all the commands that are displayed when you create the repository for the first time.

Run the following commands:

```bash
git add .
git commit -m "Added weather information with API calls"
git push origin main
```

The first command adds your changes to the [staging area](https://git-scm.com/about/staging-area). The second one commits your changes locally, while the last one pushes them to the remote repository.

Here, we have pushed the code directly to `master`. But usually, you will work on a feature in a separate branch and raise a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#) (or merge request), after which your code can be [merged](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request) into master/main branch.

Now that your code is pushed to GitHub, we’ll move forward to deployment and hosting. you can find the git repo of my code [here](https://github.com/KunalN25/test-weather-app).

## Deployment and Hosting

Before jumping into these steps, let's first understand what deployment and hosting mean. Simply put, deployment is about taking your website and putting it on the Internet, while hosting services store your website to ensure it is accessible to people online.

We'll use Netlify, a beginner-friendly platform that lets you deploy websites directly from your GitHub repository. It's perfect for deploying simple websites built with HTML, CSS, and JavaScript. You also get a free URL with your website (or you can pay for a domain name).

To get started, first visit [netlify.com](https://www.netlify.com), and sign up with your email or GitHub account. Once logged in, you’ll see a landing page. Click on "Add new site” → “Import an existing project”.

![Netlify Landing Page](https://cdn.hashnode.com/res/hashnode/image/upload/v1744635933602/b092d758-ceec-4980-a36f-7e2d863ff5b6.png align="center")

Then, connect your GitHub account by authorising Netlify to access your GitHub repositories. It will show a list of all your GitHub repositories. Search for your repository `test-weather-app`, or whatever you named it and select it.

Then, you’ll be greeted with the following page to enter configurations. Since our project does not use any frameworks, we do not need to specify any build commands. So, we leave most of the fields empty and click one “Deploy”.

![Website Config](https://cdn.hashnode.com/res/hashnode/image/upload/v1744635796692/3176dc6c-5f3c-4abf-948f-dda44536dce0.png align="center")

Netlify will deploy your site in a few minutes and will provide you with the link. You can find this example website by visiting the following link:

[https://testweatherapp11.netlify.app](https://testweatherapp11.netlify.app)

Netlify will also give you an option to purchase a custom domain. So, if you aim to build an actual website to profit from, then you can use that option.

If you want to make any changes, Netlify will deploy those automatically when you push them to GitHub.

## Wrapping Up

And just like that, your website is live on the internet. That’s all it took. You just wrote some code on your local machine, built a simple web page from scratch, and now it’s live on the internet for other people to use. How great is that!

Now that you have learned how to build a website from scratch and deploy it to the internet, here are few additional things you should remember:

* Website development is not finished just yet. As you keeping building stuff, your website will grow. You’ll explore different designs, fix bugs, and improve features as per feedback.
    
* As your website grows, you’ll also need to think about website’s performance, with increased usage, and security, to protect yourself and your users from attackers.
    
* I have described a highly simplified process. Usually there’s requirement gathering, creating a website design, and estimations before you even start the development.
    
* You’ll also collaborate with other people such as designers, backend engineers, product managers and stakeholders.
    
* Often, a website is developed in increments, that is a basic version of the website with basic features will be released at first, like we did. Then, for each feature, the whole process starting from the design, through the development and testing to deployment is followed.
    
* To make your website usable for everyone, including people who have various disabilities, you’ll want to follow web accessibility best practices. There are a number of practices that you should follow during the development phase. I have described them in detail in my [web accessibility handbook here](https://www.freecodecamp.org/news/the-web-accessibility-handbook/).
    

## Conclusion

The journey of building a website from scratch and releasing it to the internet is rewarding in many ways. Through this process, you gain valuable web development skills, plus you’ll get better at using version control to keep track of your work. And sharing what you’ve built with the community is so satisfying.

In this tutorial, I have explained a very simplified process, but remember that real-world projects often involve more complexity, including collaboration, performance optimisation, and security considerations.

As you continue to develop your skills, you'll face new challenges and have great opportunities to enhance your website's functionality and user experience. Embrace the learning process, and enjoy the satisfaction of seeing your creation come to life on the internet. Happy coding!

If you have any questions or need further clarification, please don't hesitate to reach out. Your feedback is always valued and appreciated! Connect with me on [Twitter](https://x.com/i/flow/login?redirect_after_login=%2FKunal_N25) for more updates and discussions. Thank you for reading, and I look forward to seeing you next time!
