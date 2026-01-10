---
title: How to handle internet connection reachability in Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-30T18:15:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-internet-connection-reachability-in-swift-34482301ea57
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yRw9lns3oUletanc3gUBeA.png
tags:
- name: internet
  slug: internet
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Neo Ighodaro

  More often than not, mobile applications need an active internet connection to function
  properly. It is normal, however, for the internet connection to be lost. In cases
  like these, it is up to the developer to come up with ways to ma...'
---

By Neo Ighodaro

More often than not, mobile applications need an active internet connection to function properly. It is normal, however, for the internet connection to be lost. In cases like these, it is up to the developer to come up with ways to make the experience bearable, or in the least, notify the user.

In this article, we are going to see how we can detect internet connection issues in Swift, and some ways we can handle it.

Here is the sample application we will be building and how it handles different internet connectivity scenarios:

![Image](https://cdn-media-1.freecodecamp.org/images/mVMX39hAMJRBGeo3-gn5koLvThXvN17bZyLE)

### Requirements

For you to be able to follow along in this article, you will need the following requirements:

* [Xcode](https://developer.apple.com/xcode/) installed on your machine.
* Knowledge of the Swift programming language.
* [Cocoapods](https://guides.cocoapods.org/using/getting-started.html) installed on your machine.

When you have the above requirements, let’s dive in.

### Setting up our workspace

Before we begin, we will create a playground. This is where we will write all our use cases and handle them.

Swift comes with its own Reachability implementation for detecting connection issues, but we will be using a [third-party library](https://github.com/tonymillion/Reachability). We are doing this because it is easier and the API is more expressive than the one built in.

Open Xcode and set up a new project.

![Image](https://cdn-media-1.freecodecamp.org/images/lDZ0nerqBJ40Ta8ZQs4DBDOkxahc8i2eVBxQ)

This project will be a simple playground that we can experiment with.

To detect when the connection goes offline we are going to be using the [**Reachability.swift**](https://github.com/ashleymills/Reachability.swift) ****package. It is a “replacement for Apple’s Reachability re-written in Swift with closures”.

Open your terminal and run the command below:

```
$ pod init
```

This will create a new `Podfile` where we can declare the Cocoapods dependencies. Open the `Podfile` and replace the contents with the code below:

```
platform :ios, '9.0'
```

```
target 'project_name' do    use_frameworks!    pod 'ReachabilitySwift'    pod 'Alamofire'end
```

> **_You need to replace_** `**project_name**` **with the name of your project.**

Save the file and run the command below to install the Pods to your project:

```
$ pod install
```

When the installation is complete, open the `*.xcworkspace` file in the root of your project. This will launch Xcode.

### Creating our Network Reachability Manager

Create a new `NetworkManager` class. This class will store the network status and be a simple proxy to the `Reachability` package. In the file, paste the code below:

```
import Foundationimport Reachability
```

```
class NetworkManager: NSObject {
```

```
    var reachability: Reachability!
```

```
    static let sharedInstance: NetworkManager = {         return NetworkManager()     }()
```

```
    override init() {        super.init()
```

```
        // Initialise reachability        reachability = Reachability()!
```

```
        // Register an observer for the network status        NotificationCenter.default.addObserver(            self,            selector: #selector(networkStatusChanged(_:)),            name: .reachabilityChanged,            object: reachability        )
```

```
        do {            // Start the network status notifier            try reachability.startNotifier()        } catch {            print("Unable to start notifier")        }    }
```

```
    @objc func networkStatusChanged(_ notification: Notification) {        // Do something globally here!    }
```

```
    static func stopNotifier() -> Void {        do {            // Stop the network status notifier            try (NetworkManager.sharedInstance.reachability).startNotifier()        } catch {            print("Error stopping notifier")        }    }
```

```
    // Network is reachable    static func isReachable(completed: @escaping (NetworkManager) -> Void) {        if (NetworkManager.sharedInstance.reachability).connection != .none {            completed(NetworkManager.sharedInstance)        }    }
```

```
    // Network is unreachable    static func isUnreachable(completed: @escaping (NetworkManager) -> Void) {        if (NetworkManager.sharedInstance.reachability).connection == .none {            completed(NetworkManager.sharedInstance)        }    }
```

```
    // Network is reachable via WWAN/Cellular    static func isReachableViaWWAN(completed: @escaping (NetworkManager) -> Void) {        if (NetworkManager.sharedInstance.reachability).connection == .cellular {            completed(NetworkManager.sharedInstance)        }    }
```

```
    // Network is reachable via WiFi    static func isReachableViaWiFi(completed: @escaping (NetworkManager) -> Void) {        if (NetworkManager.sharedInstance.reachability).connection == .wifi {            completed(NetworkManager.sharedInstance)        }    }]
```

In the class above, we have defined a couple of helper functions that will help us get started with network status monitoring. We have a `sharedInstance` that is a singleton and we can call that if we do not want to create multiple instances of the `NetworkManager` class.

In the `init` method, we create an instance of `Reachability` and then we register a notification using the `NotificationCenter` class. Now, every time the network status changes, the callback specified by `NotificationCenter` (which is `networkStatusChanged`) will be called. We can use this to do something global that is activated when the network is unreachable.

We have defined other helper functions that will generally make running code, depending on the status of our internet connection, a breeze. We have `*isReachable*`, `*isUnreachable*`, `*isReachableViaWWAN*` and `*isReachableViaWiFi*`.

The usage of one of these helpers will generally look like this:

```
NetworkManager.isReachable { networkManagerInstance in  print("Network is available")}
```

```
NetworkManager.isUnreachable { networkManagerInstance in  print("Network is Unavailable")}
```

> **_This is not an event listener and will only run once. To use a listener to pick up network changes in real-time, you’ll need to use_** `NetworkManager.sharedInstance.reachability.whenReachable`**. We will show an example later in the article.**

Now that we have a manager class, let’s see how we can use this in an application.

### Handling Network Availability on Application Launch

Sometimes, your application relies heavily on an internet connection and you need to detect the status on launch. Let’s see how we can handle this using the `NetworkManager` class.

Create a new controller called `LaunchViewController`. We will treat the first controller view on the storyboard as the launch controller. We will try to detect if the user’s device is online and, if not, we will create an offline page to handle this so the user does not get into the application at all.

In the `LaunchController`, replace the contents with the following code:

```
import UIKit
```

```
class LaunchViewController: UIViewController {    let network: NetworkManager = NetworkManager.sharedInstance
```

```
    override func viewDidLoad() {        super.viewDidLoad()
```

```
        NetworkManager.isUnreachable { _ in            self.showOfflinePage()        }    }
```

```
    private func showOfflinePage() -> Void {        DispatchQueue.main.async {            self.performSegue(                withIdentifier: "NetworkUnavailable",                 sender: self            )        }    }}
```

In this class, we use our `NetworkManager`‘s `*isUnreachable*` method to fire the `showOffline` method when the network is unavailable. Let us create that view controller. Create a new view controller called `OfflineViewController`.

Open the `Main.storyboard` file and set the custom class of the first view to `LaunchViewController` .

Next, create a new view controller in the storyboard. Set the `OfflineViewController` as the custom class for this new view controller. Now create a manual segue called `NetworkUnavailable` between the new view controller and the `LaunchViewController`. When you are done you should have something similar to this:

![Image](https://cdn-media-1.freecodecamp.org/images/0i0-0rCSRzRgpa1oUqpcDfOXw3qWEUb5C8G7)

Now let’s run the application. Note, though, that before you run your application, your development machine should be offline as the iOS simulator uses the machine’s internet connection. When you run the application, you should get the offline page we created.

Now let us create a view controller that shows up when there is a connection.

### Handling Events When the Device Comes Online

Now that we have created an Offline View Controller and it works when the device is offline, let us handle what happens when the device is back online.

Create a new navigation view controller on the storyboard below the Offline View Controller. We will create a controller that displays the latest Reddit posts. Create a new view controller class called `PostsTableViewController`. Now make this the custom class for the view controller attached to the Navigation View Controller.

Now create a manual segue called `MainController` from the Navigation View Controller to the Launch View Controller and the Offline View Controller. You should have something similar to this:

![Image](https://cdn-media-1.freecodecamp.org/images/nU2vrOq897dT-Q2NBQFl9AqqFICaW81aaUny)

Now, open the `LaunchViewController` class and at the bottom of the `viewDidLoad` method add the following:

```
NetworkManager.isReachable { _ in    self.showMainPage()}
```

Then add the method below to the controller:

```
private func showMainPage() -> Void {    DispatchQueue.main.async {        self.performSegue(            withIdentifier: "MainController",             sender: self        )    }}
```

This will make sure that when the app is launched, it will check for connectivity and then, if the connection is available, it will present the `PostsTableViewController`. Otherwise it will present the `OfflineViewController`.

Great! But what happens when the user has hit the `OfflineViewController` and then the network comes back online? Let’s handle that scenario.

Open the `OfflineViewController` and replace the code with the code below:

```
import UIKit 
```

```
class OfflineViewController: UIViewController {    let network = NetworkManager.sharedInstance
```

```
    override func viewDidLoad() {        super.viewDidLoad()
```

```
        // If the network is reachable show the main controller        network.reachability.whenReachable = { _ in            self.showMainController()        }    }
```

```
    override func viewWillAppear(_ animated: Bool) {        super.viewWillAppear(animated)
```

```
        navigationController?.setNavigationBarHidden(true, animated: animated)    }
```

```
    override func viewWillDisappear(_ animated: Bool) {        super.viewWillDisappear(animated)
```

```
        navigationController?.setNavigationBarHidden(false, animated: animated)    }
```

```
    private func showMainController() -> Void {        DispatchQueue.main.async {            self.performSegue(withIdentifier: "MainController", sender: self)        }    }}
```

In the controller above, you can see, in the `viewDidLoad` method, that we set the `whenReachable` completion to show the main controller. This means that, as long as its offline, you watch for when the device comes back online. When it does, present the `PostsTableViewController`.

We also override the `viewWillAppear` and `viewWillDisappear` methods to ensure the navigation bar does not show on the Offline View Controller.

#### **Fetching Posts from Reddit API in Swift**

Now let us add the logic that’ll fetch data from Reddit and display on our `PostsTableViewController`. Open the file and replace the contents with the code below:

```
import UIKitimport Alamofire
```

```
struct RedditPost {    let title: String!    let subreddit: String!}
```

```
class PostsTableViewController: UITableViewController {    var posts = [RedditPost]()
```

```
    let network = NetworkManager.sharedInstance
```

```
    override func viewDidLoad() {        super.viewDidLoad()        navigationItem.title = "Latest Posts"
```

```
        // Fetch the posts and then reload the table        fetchPosts { posts in            self.posts = posts            self.tableView.reloadData()        }    }
```

```
    private func fetchPosts(completion: @escaping (_ posts: [RedditPost]) -> Void) -> Void {        // Send a request to the Reddit API        Alamofire.request("https://api.reddit.com").validate().responseJSON { response in            switch response.result {            case .success(let JSON):                let data = JSON as! [String:AnyObject]                guard let children = data["data"]!["children"] as? [AnyObject] else { return }                var posts = [RedditPost]()
```

```
                // Loop through the Reddit posts and then assign a post to the posts array                for child in 0...children.count-1 {                    let post = children[child]["data"] as! [String: AnyObject]
```

```
                    posts.append(RedditPost(                        title: post["title"] as! String,                        subreddit: "/r/" + (post["subreddit"] as! String)                    ))                }
```

```
                DispatchQueue.main.async {                    completion(posts)                }            case .failure(let error):                print(error)            }        }    }
```

```
    override func didReceiveMemoryWarning() {        super.didReceiveMemoryWarning()    }
```

```
    // MARK: - Table view data source    override func numberOfSections(in tableView: UITableView) -> Int {        return 1    }
```

```
    // Return the number of posts available    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {        return self.posts.count    }
```

```
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {        let cell = tableView.dequeueReusableCell(withIdentifier: "PostCell", for: indexPath)        let post = posts[indexPath.row] as RedditPost        cell.textLabel?.text = post.title        cell.detailTextLabel?.text = post.subreddit        return cell    }}
```

In the `fetchPosts` method, we use `Alamofire` to send a GET request to the Reddit API. We then parse the response and add it to the `RedditPost` struct we created at the top of the file. This makes the data we are passing to the `tableView` consistent.

### Handling Events when the Device Goes Offline

Now, let us handle one more scenario. Imagine while viewing the latest Reddit posts, you lose connectivity. What happens? Let’s show the offline page again when that happens.

As was previously done, create a manual segue called `NetworkUnavailable` from the `PostsTableViewController` to the `OfflineViewController`. Now add this code to the bottom of the `viewDidLoad` method:

```
network.reachability.whenUnreachable = { reachability in    self.showOfflinePage()}
```

Now add the method below to the controller:

```
private func showOfflinePage() -> Void {    DispatchQueue.main.async {        self.performSegue(withIdentifier: "NetworkUnavailable", sender: self)    }}
```

This will listen for when the device goes offline and, if that happens, it will `showOfflinePage`.

That’s all! We have been able to handle offline and online events using our NetworkManager in Swift.

### Conclusion

In this article, we considered how to make sure your application can handle online and offline events when they happen. You can always implement this any way you wish. If you have any questions or feedback, leave them below in the comments.

The source code to this playground is available on [GitHub](https://github.com/neoighodaro/Handling-internet-connection-reachability-in-Swift).

This article was first published on [Pusher](https://blog.pusher.com/handling-internet-connection-reachability-swift/).

