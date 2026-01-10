---
title: How to build a realtime chart in iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-20T02:38:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-realtime-chart-in-ios-34a07410d50d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DLK3pjfoFjF_hCEU7Lkf2g.jpeg
tags:
- name: iOS
  slug: ios
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Neo Ighodaro

  Nowadays, gathering data is one of the keys to understanding how products are perceived.
  Gathering some data from users can help you build better products and understand
  your users. However, all the data in the world would be useless ...'
---

By Neo Ighodaro

Nowadays, gathering data is one of the keys to understanding how products are perceived. Gathering some data from users can help you build better products and understand your users. However, all the data in the world would be useless without a way to visualize it.

In this article, we will explore how to create a simple realtime chart in iOS. The chart will receive data and update in realtime to the screens of everyone currently logged into your application. We will assume this is a chart that monitors how many visitors are using a website. Let’s begin.

For context, here is a sample of what we will be building:

![Image](https://cdn-media-1.freecodecamp.org/images/paeVVTUrY7xK9gLwZL2xmcLbJhjbIcSpm8dw)

Please note: A basic understanding of Swift and Node.js is needed to follow this tutorial.

### Requirements for building a realtime chart in iOS

Before we begin this tutorial, you will need to have the following requirements:

* A MacBook Pro.
* [Xcode](https://developer.apple.com/xcode/) installed on your machine.
* Basic knowledge of [Swift](https://developer.apple.com/swift/) and using Xcode.
* Basic knowledge of JavaScript (Node.js).
* [Node.js](https://docs.npmjs.com/getting-started/installing-node) and NPM installed on your machine.
* [Cocoapods](http://www.raywenderlich.com/12139/introduction-to-cocoapods) _**_installed on your machine.
* A [Pusher](https://pusher.com) application

When you have all the requirements, then we can begin.

### Preparing to create our realtime chart application in Xcode

Launch Xcode on your Mac and create a new project (call it whatever you want). Follow the new application wizard and create a new **Single-page application**. Once the project has been created, close Xcode and launch your terminal application.

In the terminal, `cd` to the root of the application directory. Then run the command `pod init`. This will generate a **Podfile**. Update the contents of the Podfile to the contents below (replace `PROJECT_NAME` with your project name):

```
platform :ios, '9.0'target 'PROJECT_NAME' do  use_frameworks!    pod 'Charts', '~> 3.0.2'  pod 'PusherSwift', '~> 4.1.0'  pod 'Alamofire', '~> 4.4.0'end
```

Save the Podfile and then go to your terminal and run the command: `pod install`.

Running this command will install all the third-party packages we need to build our realtime iOS chart application.

The first package it will install is [Charts](https://github.com/danielgindi/Charts), which is a package for making beautiful charts on iOS. The second package is the Pusher swift SDK. The last package is [Alamofire](https://github.com/Alamofire/Alamofire), a package for making HTTP requests on iOS.

Once the installation is complete, open the `**.xcworkspace**` file in your project directory root. This should launch Xcode. Now we are ready to start creating our iOS application.

### Creating our realtime chart application views in Xcode

To begin, we will create the necessary views we need for our realtime chart application. Open the **Main.storyboard** file and let’s start designing our view.

First, create a rectangular view from edge to edge at the top of the View Controller in the storyboard. In that view, add a button and add the title “Simulate Visits”. Next, create another view that is also a rectangle, spanning from the end of the first view above to the bottom of the screen. This view will be where we will render the realtime chart.

When you are done creating the views, you should have something like what’s shown in the image below.

![Image](https://cdn-media-1.freecodecamp.org/images/huuI0xR6kxUoSTaWfQCKN4NddLbtIkv8G5C6)

As it currently stands, the views do nothing. Let us connect some functionality to the iOS chart application view.

### Adding basic functionality to our iOS chart application

As said before, our application’s views and buttons are not connected to our `ViewController` , so let’s fix that.

In Xcode, while the storyboard is still open, click on the “Show the Assistant Editor” button on the top right of the page to split the view into storyboard and code view. Now, click once on the button you created, and while holding `ctrl`, click and drag the link to the code editor. Then create an `@IBaction` as seen in the images below:

![Image](https://cdn-media-1.freecodecamp.org/images/qREVxZDqIVLbvbXVMEVNpFnVfrWtMGNBRoKz)

![Image](https://cdn-media-1.freecodecamp.org/images/-xNvKpDLIWBBQnEvmE4gWWFzOiCy0Raw9eAJ)

When the link is complete, you should see something like this added to the code editor:

```
@IBAction func simulateButtonPressed(_ sender: Any) {}
```

Great! Now that you have created the first link, we will have to create one more link to the chart view.

On your storyboard, click the view and on the “Identity Inspection” tab, make sure the view is connected to `LineChartView` as seen below.

![Image](https://cdn-media-1.freecodecamp.org/images/8cXCATmAKj7FvkFjOAeRvzBh0qxhjU76cNuN)

Now that the view is connected to a view class, repeat the same as we did before to link the button. Only this time, instead of creating an `@IBAction` , we will create an `@IBOutlet`. Images are shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/ryie0CqwHghtuz3m68Rp-3NFRbwWeumv4-kT)

![Image](https://cdn-media-1.freecodecamp.org/images/AEUIIpDFJsNUkZQG7aOZ4FPZmj8fMuziPfHZ)

When the link is complete, you should see something like this added to the code editor:

```
@IBOutlet weak var chartView: LineChartView!
```

Finally, at the top of the `ViewController` , import the Charts package. You can add the code below right under `import UIKit` in the `ViewController`.

```
import Charts
```

Now that we have linked both elements to our code, every time the **Simulate Visits** button is pressed, the **simulateButtonPressed** function will be called.

### Adding realtime functionality to our iOS chart application

The final piece of the puzzle will be displaying a chart and making it update in realtime across all devices viewing the chart.

To achieve this, we will do the following:

* Create a function that updates our chart depending on the numbers.
* Make our request button call the backend, which will in turn send simulated data to Pusher.
* Create a function that listens for events from Pusher and, when one is received, it triggers the update chart function we created earlier.

### Create a trigger function to update our chart

Let’s create the function that updates our chart depending on the numbers supplied to it. Open the `ViewController`, and in it declare a class property right under the class declaration. We will use this property to track the visitors:

```
var visitors: [Double] = []
```

Next, we will add the function that will do the actual update to the chart view:

```
private func updateChart() {    var chartEntry = [ChartDataEntry]()
```

```
    for i in 0..<visitors.count {        let value = ChartDataEntry(x: Double(i), y: visitors[i])        chartEntry.append(value)    }        let line = LineChartDataSet(values: chartEntry, label: "Visitor")    line.colors = [UIColor.green]
```

```
    let data = LineChartData()    data.addDataSet(line)
```

```
    chartView.data = data    chartView.chartDescription?.text = "Visitors Count"}
```

In the code above, we declare `chartEntry` where we intend to store all our chart data. Then we loop through the available `visitors` and, for each of them, we add a new `ChartDataEntry(x: Double(i), y: visitors[i])` that tells the chart the X and Y positions.

We set the color the line chart will be displayed in. We create the `LineChartData` and add the `line` which contains our data points. Finally, we add the data to the `chartView` and set the chart view description.

### Make our simulate button call an endpoint

The next thing we need to do is make our request button trigger a backend, which will in turn send simulated data to Pusher.

To do this, we need to update the view controller one more time. In the `ViewController` , import the Alamofire package right under the Charts package:

```
import Alamofire
```

Now, replace the `simulateButtonPressed` function with the code below:

```
@IBAction func simulateButtonPressed(_ sender: Any) {    Alamofire.request("http://localhost:4000/simulate", method: .post).validate().responseJSON { (response) in        switch response.result {        case .success(_):           _ = "Successful"        case .failure(let error):           print(error)        }    }}
```

In the code below, we use Alamofire to send a POST request to [http://localhost:4000/simulate](http://localhost:4000/simulate), which is a local web server (we will create this backend soon). In a real application, this will typically point to a real web server.

This endpoint does not take any parameters in order to keep the tutorial simple. We also do not need to do anything with the response. We just need the POST request to be sent every time the simulate visits button is pressed.

### Tie in realtime functionality using Pusher

To make all this work, we will create a function that listens for events from Pusher and, when one is received, we save the value to `visitors` and then trigger the update chart function we created earlier.

To do this, open the `ViewController` and import the `PusherSwift` SDK under the Alamofire package at the top:

```
import PusherSwift
```

Next, we will declare a class property for the Pusher instance. We can do this right under the `visitors` declaration line:

```
var pusher: Pusher!
```

Then after declaring the property, we need to add the function below to the class so it can listen to the events:

```
private func listenForChartUpdates() {    pusher = Pusher(        key: "PUSHER_KEY",         options: PusherClientOptions(            host: .cluster("PUSHER_CLUSTER")        )    )    let channel = pusher.subscribe("visitorsCount")    channel.bind(eventName: "addNumber", callback: { (data: Any?) -> Void in       if let data = data as? [String: AnyObject] {           let count = data["count"] as! Double           self.visitors.append(count)           self.updateChart()       }    })    pusher.connect()}
```

In the code above, we instantiate Pusher and pass in our key and the cluster (you can get your key and cluster from your Pusher application’s dashboard). We then subscribe to the `visitorsChannel` and bind to the event name `addNumber` on that channel.

When the event is triggered, we fire the logic in the callback which simply appends the count to `visitors` and then calls the `updateChart` function, which updates the actual Chart in realtime.

Finally we call `pusher.connect()` which forms the connection to Pusher.

In the `viewDidLoad` function, just add a call to the `listenForChartUpdates` method:

```
override func viewDidLoad() {    super.viewDidLoad()    // ...stuff        listenForChartUpdates()}
```

That’s all! We have created our application in Xcode and we are ready for testing. However, to test, we need to create the backend that we send a `POST` request to when the button is clicked. To create this backend, we will be using Node.js. Let’s do that now.

### Creating the backend service for our realtime iOS chart application

To get started, create a directory for the web application and then create some new files inside the directory:

File: **index.js**

```
// -------------------------------------------------------// Require Node dependencies// -------------------------------------------------------
```

```
let Pusher     = require('pusher');let express    = require('express');let bodyParser = require('body-parser');let app        = express();
```

```
// Instantiate Pusherlet pusher     = new Pusher(require('./config.js'));
```

```
// -------------------------------------------------------// Load express middlewares// -------------------------------------------------------
```

```
app.use(bodyParser.json());app.use(bodyParser.urlencoded({ extended: false }));
```

```
// -------------------------------------------------------// Simulate multiple changes to the visitor count value,// this way the chart will always update with different// values.// -------------------------------------------------------
```

```
app.post('/simulate', (req, res, next) => {    var loopCount = 0;    let sendToPusher = setInterval(function(){    let count = Math.floor((Math.random() * (100 - 1)) + 1)    pusher.trigger('visitorsCount', 'addNumber', {count:count})    loopCount++;    if (loopCount === 20) {        clearInterval(sendToPusher);    }    }, 2000);    res.json({success: 200})})
```

```
// Handle indexapp.get('/', (req, res) => {    res.json("It works!");});
```

```
// Handle 404'sapp.use((req, res, next) => {    let err = new Error('Not Found');    err.status = 404;    next(err);});
```

```
// -------------------------------------------------------// Serve application// -------------------------------------------------------
```

```
app.listen(4000, function(){    console.log('App listening on port 4000!')});
```

The file above is a simple Express application written in JavaScript. We instantiate all the packages we require and configure pusher using a config file we will create soon. Then we create a route `/simulate` and in this route we trigger the `addNumber` event in the `visitorCount` channel. This is the same channel and event the application is listening for.

To make it a little easier, we use `setInterval` to send a random visitor count to the Pusher backend every 2000 milliseconds. After looping 20 times, the loop stops. This should be sufficient to test our application.

Create the next file **config.js**:

```
module.exports = {    appId: 'PUSHER_APP_ID',    key: 'PUSHER_APP_KEY',    secret: 'PUSHER_APP_SECRET',    cluster: 'PUSHER_APP_CLUSTER',};
```

In this file, we simply declare dependencies.

Now open terminal and `cd` to the root of the web application directory. Run the commands below to install the NPM dependencies, and run the application respectively:

```
$ npm install$ node index.js
```

When installation is complete and the application is ready, you should see the output below:

![Image](https://cdn-media-1.freecodecamp.org/images/gTvq-SQMzsRUv7V3-pRpPCI86EImjbY-fB8Z)

### Testing the application

Once you have your local node web server running, you will need to make some changes so your application can talk to the local web server. In the `info.plist` file, make the following changes:

![Image](https://cdn-media-1.freecodecamp.org/images/kVCEsKQ9oIKlWITzxNKQ8hOSBxc16eA60bkA)

With this change, you can build and run your application and it will talk directly with your local web application.

### Conclusion

This article has shown you how you can combine Pusher and the Charts package to create a realtime iOS chart application. There are many other chart types you can create using the package but, for brevity, we have done the easiest. You can explore the other chart types and even pass in multiple data points per request.

This post first appeared on the [Pusher blog.](https://pusher.com/tutorials/chart-swift/)

