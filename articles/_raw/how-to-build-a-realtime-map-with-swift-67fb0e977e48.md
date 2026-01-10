---
title: How to build a realtime map with Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-10T22:09:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-realtime-map-with-swift-67fb0e977e48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*56icJ6WPoNlPAcAlhzEZCg.jpeg
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

  Realtime maps are very popular nowadays. Especially now that there are many on-demand
  transportation services like Uber and Lyft that have realtime location reporting.
  In this article, we are going to learn how to build a realtime map...'
---

By Neo Ighodaro

Realtime maps are very popular nowadays. Especially now that there are many on-demand transportation services like Uber and Lyft that have realtime location reporting. In this article, we are going to learn how to build a realtime map on iOS using Pusher.

Before we continue, you’ll need to make sure you have all of the following requirements:

* A MacBook (Xcode only runs on Mac).
* [Xcode](https://developer.apple.com/xcode/) installed on your machine.
* Knowledge of JavaScript (Node.js).
* Knowledge of Swift and using Xcode. You can get started [here](https://developer.apple.com/library/content/referencelibrary/GettingStarted/DevelopiOSAppsSwift/).
* [NPM and Node.js](https://docs.npmjs.com/getting-started/installing-node) installed locally.
* [Cocoapods](https://guides.cocoapods.org/using/getting-started.html) package manager installed locally.
* A Google iOS API key. See [here](https://developers.google.com/maps/documentation/ios-sdk/start#step_4_get_an_api_key) for instructions on how to get a key.
* A Pusher application. Create one [here](https://pusher.com).

A basic understanding of Swift and Node.js is needed to follow this tutorial.

Assuming you have all of the requirements, let’s begin. This is a screen recording of what we will be building:

![Image](https://cdn-media-1.freecodecamp.org/images/oNEt5czqqZUmTL5r6SvWAjv2QBSnWgYEr8RT)

As you can see in the demo, every time the location is updated, the change is reflected on both devices. This is what we want to replicate. Let’s get started.

### Setting up our iOS application

Launch Xcode and create a new “Single-app” project. You can call the project whatever you please.

![Image](https://cdn-media-1.freecodecamp.org/images/SykobSVDuoF5VSM3PZeNvC4sISPAbkoYUwIb)

When the project is created, close Xcode. Open your terminal, `cd` to the root directory of your application, and run the command below to initialize Cocoapods on the project:

```
$ pod init
```

The command above will create a `Podfile` in the root directory of our application. In this `Podfile`, we will specify our project dependencies and let Cocoapods pull and manage them. Open the `Podfile` and replace the content of the file with the content below:

```
platform :ios, '10.0'target 'application_name' do    use_frameworks!
```

```
    pod 'GoogleMaps'    pod 'Alamofire', '~> 4.4.0'    pod 'PusherSwift', '~> 4.1.0'end
```

> _⚠️ Make sure you replace `application_name` with the name of your application._

Run the command below to start installing the packages we specified in our `Podfile`:

```
$ pod install
```

When the installation is complete, open the `*.xcworkspace` file that was added to the root of your application directory. This should launch Xcode.

### Setting up our Node.js simulator app

Before going back into our iOS application, we need to create a simple Node.js application. This application will send events with data to Pusher. The data sent to Pusher will be simulated GPS coordinates. When our iOS application picks up the event’s data from Pusher, it will update the map’s marker to the new coordinates.

Create a new directory that will hold our Node.js application. Open your terminal and `cd` to the directory of your Node.js application. In this directory, create a new `package.json` file. Open that file and paste the JSON below:

```
{      "main": "index.js",      "dependencies": {        "body-parser": "^1.16.0",        "express": "^4.14.1",        "pusher": "^1.5.1"      }    }
```

Now run the command below to install the NPM packages listed as dependencies:

```
$ npm run install
```

Create a new `index.js` file in the directory and paste the code below into the file:

```
//    // Load the required libraries    //    let Pusher     = require('pusher');    let express    = require('express');    let bodyParser = require('body-parser');    //    // initialize express and pusher    //    let app        = express();    let pusher     = new Pusher(require('./config.js'));    //    // Middlewares    //    app.use(bodyParser.json());    app.use(bodyParser.urlencoded({ extended: false }));
```

```
//    // Generates 20 simulated GPS coords and sends to Pusher    //    app.post('/simulate', (req, res, next) => {      let loopCount = 0;      let operator = 0.001000        let longitude = parseFloat(req.body.longitude)      let latitude  = parseFloat(req.body.latitude)      let sendToPusher = setInterval(() => {        loopCount++;        // Calculate new coordinates and round to 6 decimal places...        longitude = parseFloat((longitude + operator).toFixed(7))        latitude  = parseFloat((latitude - operator).toFixed(7))        // Send to pusher        pusher.trigger('mapCoordinates', 'update', {longitude, latitude})        if (loopCount === 20) {          clearInterval(sendToPusher)        }      }, 2000);      res.json({success: 200})    })
```

```
//    // Index    //    app.get('/', (req, res) => {      res.json("It works!");    });
```

```
//    // Error Handling    //    app.use((req, res, next) => {        let err = new Error('Not Found');        err.status = 404;        next(err);    });
```

```
//    // Serve app    //    app.listen(4000, function() {        console.log('App listening on port 4000!')});
```

The code above is a simple Express application. We have initialized the Express `app` and the `pusher` instance. In the `/simulate` route, we run a loop in 2-second intervals and break the loop after the 20th run. Every time the loop runs, new GPS coordinates are generated and sent over to Pusher.

Create a new `config.js` file and paste the code below into it:

```
  module.exports = {        appId: 'PUSHER_APP_ID',        key: 'PUSHER_APP_KEY',        secret: 'PUSHER_APP_SECRET',        cluster: 'PUSHER_APP_CLUSTER',    };
```

Replace the values of `*PUSHER_APP_ID*`, `*PUSHER_APP_KEY*`, `PUSHER_APP_SECRET` and `PUSHER_APP_CLUSTER` with the values in your Pusher application dashboard. Our Node.js application is now ready to simulate GPS coordinates when our application triggers it.

Now that we are done creating the Node.js application, we can return to creating the iOS application.

### Creating the views of our realtime map in Xcode

Reopen Xcode with our project and open the `Main.storyboard` file. In the `ViewController` we will add a `UIView`, and in that `UIView` we will add a simulate button. Something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/rOVmC-h3c2R2xCeeuPcTlp8g7fG5Yr-tWJl6)

Create an `@IBAction` from the button to the `ViewController`. To do this, click on “Show the Assistant Editor” on the top right of the Xcode tool set. This will split the screen into storyboard and code editor. Now `ctrl` and drag from the button to the code editor to create the `@IBAction`. We will call the method `simulateMovement`.

![Image](https://cdn-media-1.freecodecamp.org/images/sirx-Tu8WaaGQUQVz4IKvuTdFlhZELT2qM0F)

Next, click the “Show standard editor” button on the Xcode toolbar to close the split screen and display just the `Main.storyboard`. Add another `UIView` starting from the bottom of the last `UIView` to the bottom of the screen. This view will be where the map will be displayed.

Set the `UIView`'s custom class in the “Identity inspector” to `GMSMapView`. Now click the “Show the Assistant Editor” on the top right of the Xcode tool set. `ctrl` and drag from the `UIView` to the code editor. Create an `@IBOutlet` and name it `mapView`.

Click on the “Show standard editor” button on the Xcode toolbar to close the split view. Open the `ViewController` file and replace the content with the code below:

```
//    // Import libraries    //    import UIKit    import PusherSwift    import Alamofire    import GoogleMaps
```

```
    //    // View controller class    //    class ViewController: UIViewController, GMSMapViewDelegate {        // Marker on the map        var locationMarker: GMSMarker!
```

```
        // Default starting coordinates        var longitude = -122.088426        var latitude  = 37.388064
```

```
        // Pusher        var pusher: Pusher!
```

```
        // Map view        @IBOutlet weak var mapView: GMSMapView!
```

```
        //        // Fires automatically when the view is loaded        //        override func viewDidLoad() {            super.viewDidLoad()
```

```
            //            // Create a GMSCameraPosition that tells the map to display the coordinate            // at zoom level 15.            //            let camera = GMSCameraPosition.camera(withLatitude:latitude, longitude:longitude, zoom:15.0)            mapView.camera = camera            mapView.delegate = self
```

```
            //            // Creates a marker in the center of the map.            //            locationMarker = GMSMarker(position: CLLocationCoordinate2D(latitude: latitude, longitude: longitude))            locationMarker.map = mapView
```

```
            //            // Connect to pusher and listen for events            //            listenForCoordUpdates()        }
```

```
        //        // Send a request to the API to simulate GPS coords        //        @IBAction func simulateMovement(_ sender: Any) {            let parameters: Parameters = ["longitude":longitude, "latitude": latitude]
```

```
            Alamofire.request("http://localhost:4000/simulate", method: .post, parameters: parameters).validate().responseJSON { (response) in                switch response.result {                case .success(_):                    print("Simulating...")                case .failure(let error):                    print(error)                }            }        }
```

```
        //        // Connect to pusher and listen for events        //        private func listenForCoordUpdates() {            // Instantiate Pusher            pusher = Pusher(key: "PUSHER_APP_KEY", options: PusherClientOptions(host: .cluster("PUSHER_APP_CLUSTER")))
```

```
            // Subscribe to a Pusher channel            let channel = pusher.subscribe("mapCoordinates")
```

```
            //            // Listener and callback for the "update" event on the "mapCoordinates"            // channel on Pusher            //            channel.bind(eventName: "update", callback: { (data: Any?) -> Void in                if let data = data as? [String: AnyObject] {                    self.longitude = data["longitude"] as! Double                    self.latitude  = data["latitude"] as! Double
```

```
                    //                    // Update marker position using data from Pusher                    //                    self.locationMarker.position = CLLocationCoordinate2D(latitude: self.latitude, longitude: self.longitude)                    self.mapView.camera = GMSCameraPosition.camera(withTarget: self.locationMarker.position, zoom: 15.0)                }            })
```

```
            // Connect to pusher            pusher.connect()        }    }
```

In the controller class above, we import all the required libraries. Then we instantiate a few properties on the class. In the `viewDidLoad` method, we set the coordinates on the `mapView`, and also add the `locationMarker` to it.

In the same method, we make a call to `listenForCoordUpdates()`. In the `listenForCoordUpdates` method we create a connection to Pusher and listen for the `update` event on the `mapCoordinates` channel.

When the `update` event is triggered, the callback takes the new coordinates and updates the `locationMarker` with them. Remember, you need to change the `PUSHER_APP_KEY` and `PUSHER_APP_CLUSTER` to the actual values provided for your Pusher application.

In the `simulateMovement` method, we just send a request to our local web server (the Node.js application we created earlier). The request will instruct the Node.js application to generate several GPS coordinates.

> _? The URL of the endpoint we are hitting (h[ttp://localhost:3000/simulate)](http://localhost:3000/simulate) is a local web server. This means that you will need to change the endpoint URL when building for real cases._

### Configuring Google Maps for iOS

We will need to configure the Google Maps iOS SDK to work with our application. First, [create a Google iOS SDK key](https://developers.google.com/maps/documentation/ios-sdk/start#step_4_get_an_api_key) and then, when you have the API key, open the `AppDelegate.swift` file in Xcode.

In the class, look for the class below:

```
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {        // Override point for customization after application     launch.        return true    }
```

and replace it with this:

```
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {        GMSServices.provideAPIKey("GOOGLE_IOS_API_KEY")        return true }
```

> _? You need to replace the G`OOGLE_IOS_API_KEY` with the key you got when you created the Google iOS API key._

At the top of the same file, look for `import UIKit` and add the following under it:

```
import GoogleMaps
```

With that, we are done configuring Google Maps to work on iOS.

### Testing our realtime iOS map

To test our application, we need to start the Node.js application, instruct iOS to allow connections to the local web server, and then run our iOS application.

To run the Node.js application, `cd` to the Node.js application directory using your terminal and run the command below to start the Node application:

```
$ node index.js
```

Now, before we launch our application, we need to make some final changes so our iOS application can connect to our `localhost` backend. Open the `info.plist` file in Xcode and make the following adjustments:

![Image](https://cdn-media-1.freecodecamp.org/images/k0V9gHDnWihDnOigSrwEOias6xFVD0Di-5Td)

This change will make it possible for our application to connect to localhost. To be clear, this step will not be needed in production environments.

Now build your application. You should see that the iOS application now displays the map and the marker on the map. Clicking the simulate button hits the endpoint which in turn sends the new coordinates to Pusher. Our listener catches the event and updates the `locationMarker`, thereby moving our marker.

### Conclusion

In this article, we have seen how we can use Pusher and Swift to build a realtime map on iOS. I hope you learned a few things on how to create realtime iOS applications. If you have any questions or suggestions, please leave a comment below.

This post was first published to Pusher.

