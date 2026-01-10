---
title: How to build a collaborative text editor using Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T01:11:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-collaborative-text-editor-using-swift-df7402c82510
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1Y-djx_fBY4GWJoNR6pVAw.jpeg
tags:
- name: coding
  slug: coding
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Neo Ighodaro

  Text editors are increasingly popular these days, whether they’re embedded in a
  website comment form or used as a notepad. There are many different editors to choose
  from. In this post, we are not only going to learn how to build a be...'
---

By Neo Ighodaro

Text editors are increasingly popular these days, whether they’re embedded in a website comment form or used as a notepad. There are many different editors to choose from. In this post, we are not only going to learn how to build a beautiful text editor mobile app in iOS, but also how to make it possible to collaborate on a note in realtime using Pusher.

Please note, however, that to keep the application simple, the article will not cover concurrent edits. Therefore, only one person can edit at the same time while others watch.

The application will work by triggering an event when some text is entered. This event will be sent to Pusher and then picked up by the collaborator’s device and updated automatically.

To follow along in this tutorial, you will need the following:

1. **Cocoapods:** to install, run `gem install cocoapods` on your machine
2. **Xcode**
3. A **Pusher application:** you can create a free account and application [here](https://pusher.com)
4. Some knowledge of the **Swift** language
5. **Node.js**

Lastly, a basic understanding of Swift and Node.js is needed to follow this tutorial.

### Getting started with our iOS application in Xcode

Launch Xcode and create a new project. I’ll call mine **Collabo**. After following the set up wizard, and with the workspace open, close Xcode and then `cd` to the root of your project and run the command `pod init`. This should generate a `Podfile` for you. Change the contents of the `Podfile`:

```
# Uncomment the next line to define a global platform for your project    platform :ios, '9.0'
```

```
    target 'textcollabo' do      # Comment the next line if you're not using Swift and don't want to use dynamic frameworks      use_frameworks!
```

```
      # Pods for anonchat      pod 'Alamofire'      pod 'PusherSwift'    end
```

Now run the command `pod install` so the Cocoapods package manager can pull in the necessary dependencies. When this is complete, close Xcode (if open) and then open the `.xcworkspace` file that is in the root of your project folder.

### Designing the views for our iOS application

We are going to create some views for our iOS application. These will be the backbone where we will hook all the logic into. Using the Xcode story board, make your views look a little like the screenshots below.

This is the **LaunchScreen.storyboard** file. I’ve just designed something simple with no functionality at all.

![Image](https://cdn-media-1.freecodecamp.org/images/QzhBjZMrhJiM66feDQLG6npu-aYqA1VEgGlt)

The next storyboard we will design is the **Main.storyboard.** As the name implies, it will be the main one. This is where we have all the important views that are attached to some logic.

![Image](https://cdn-media-1.freecodecamp.org/images/eibpbvrTnwGPiY9BGpN2dcvELgUgtczDbH-K)

Here we have three views.

The first view is designed to look exactly like the launch screen, with the exception of a button that we have linked to open up the second view.

The second view is the Navigation controller. It is attached to a third view which is a `ViewController`. We have set the third view as the root controller to our Navigation Controller.

In the third view, we have a `UITextView` that is editable which is placed in the view. There’s also a label that is supposed to be a character counter. This is the place where we will increment the characters as the user is typing text into the text view.

### Coding the iOS collaborative text editor application

Now that we have successfully created the views required for the application to load, the next thing we will do is start coding the logic for the application.

Create a new cocoa class file and name it `TextEditorViewController` and link it to the third view in the `Main.storyboard` file. The `TextViewController` should also adopt the `UITextViewDelegate`. Now, you can `ctrl+drag` the `UITextView` and also `ctrl+drag` the `UILabel` in the `Main.storyboard` file to the `TextEditorViewController` class.

Also, you should import the `PusherSwift` and `AlamoFire` libraries to the `TextViewController`. You should have something close to this after you are done:

```
import UIKit    import PusherSwift    import Alamofire
```

```
    class TextEditorViewController: UIViewController, UITextViewDelegate {        @IBOutlet weak var textView: UITextView!        @IBOutlet weak var charactersLabel: UILabel!    }
```

Now we need to add some properties that we will be needing sometime later in the controller.

```
import UIKit    import PusherSwift    import Alamofire
```

```
    class TextEditorViewController: UIViewController, UITextViewDelegate {        static let API_ENDPOINT = "http://localhost:4000";
```

```
        @IBOutlet weak var textView: UITextView!
```

```
        @IBOutlet weak var charactersLabel: UILabel!
```

```
        var pusher : Pusher!
```

```
        var chillPill = true
```

```
        var placeHolderText = "Start typing..."
```

```
        var randomUuid : String = ""    }
```

Now we will break up the logic into three parts:

1. View and Keyboard events
2. UITextViewDelegate methods
3. Handling Pusher events.

#### **View and Keyboard events**

Open the `TextEditorViewController` and update it with the methods below:

```
override func viewDidLoad() {        super.viewDidLoad()        // Notification trigger        NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillShow), name: NSNotification.Name.UIKeyboardWillShow, object: nil)        NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillHide), name: NSNotification.Name.UIKeyboardWillHide, object: nil)        // Gesture recognizer        view.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(tappedAwayFunction(_:))))        // Set the controller as the textView delegate        textView.delegate = self        // Set the device ID        randomUuid = UIDevice.current.identifierForVendor!.uuidString        // Listen for changes from Pusher        listenForChanges()    }    override func viewWillAppear(_ animated: Bool) {        super.viewWillAppear(animated)        if self.textView.text == "" {            self.textView.text = placeHolderText            self.textView.textColor = UIColor.lightGray        }    }    func keyboardWillShow(notification: NSNotification) {        if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {            if self.charactersLabel.frame.origin.y == 1.0 {                self.charactersLabel.frame.origin.y -= keyboardSize.height            }        }    }    func keyboardWillHide(notification: NSNotification) {        if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {            if self.view.frame.origin.y != 1.0 {                self.charactersLabel.frame.origin.y += keyboardSize.height            }        }    }
```

In the `viewDidLoad` method, we registered the keyboard functions so they will respond to keyboard events. We also added gesture recognizers that will dismiss the keyboard when you tap outside the `UITextView`. And we set the `textView` delegate to the controller itself. Finally, we called a function to listen for new updates (we will create this later).

In the `viewWillAppear` method, we simply hacked the `UITextView` into having a placeholder text, because, by default, the `UITextView` does not have that feature. Wonder why, Apple…

In the `keyboardWillShow` and `keyboardWillHide` functions, we made the character count label rise up with the keyboard and descend with it, respectively. This will prevent the Keyboard from covering the label when it is active.

#### **UITextViewDelegate methods**

Update the `TextEditorViewController` with the following:

```
func textViewDidChange(_ textView: UITextView) {        charactersLabel.text = String(format: "%i Characters", textView.text.characters.count)
```

```
        if textView.text.characters.count >= 2 {            sendToPusher(text: textView.text)        }    }
```

```
    func textViewShouldBeginEditing(_ textView: UITextView) -> Bool {        self.textView.textColor = UIColor.black
```

```
        if self.textView.text == placeHolderText {            self.textView.text = ""        }
```

```
        return true    }
```

```
    func textViewDidEndEditing(_ textView: UITextView) {        if textView.text == "" {            self.textView.text = placeHolderText            self.textView.textColor = UIColor.lightGray        }    }
```

```
    func tappedAwayFunction(_ sender: UITapGestureRecognizer) {        textView.resignFirstResponder()    }
```

The `textViewDidChange` method simply updates the character count label and also sends the changes to Pusher using our backend API (which we will create in a minute).

The `textViewShouldBeginEditing` is gotten from the `UITextViewDelegate` and it is triggered when the text view is about to be edited. In here, we basically play around with the placeholder, same as the `textViewDidEndEditing` method.

Finally, in the `tappedAwayFunction` we define the event callback for the gesture we registered in the previous section. In the method, we basically dismiss the keyboard.

#### **Handling Pusher events**

Update the controller with the following methods:

```
func sendToPusher(text: String) {        let params: Parameters = ["text": text, "from": randomUuid]
```

```
        Alamofire.request(TextEditorViewController.API_ENDPOINT + "/update_text", method: .post, parameters: params).validate().responseJSON { response in            switch response.result {
```

```
            case .success:                print("Succeeded")            case .failure(let error):                print(error)            }        }    }
```

```
    func listenForChanges() {        pusher = Pusher(key: "PUSHER_KEY", options: PusherClientOptions(            host: .cluster("PUSHER_CLUSTER")        ))
```

```
        let channel = pusher.subscribe("collabo")        let _ = channel.bind(eventName: "text_update", callback: { (data: Any?) -> Void in
```

```
            if let data = data as? [String: AnyObject] {                let fromDeviceId = data["deviceId"] as! String
```

```
                if fromDeviceId != self.randomUuid {                    let text = data["text"] as! String                    self.textView.text = text                    self.charactersLabel.text = String(format: "%i Characters", text.characters.count)                }            }        })
```

```
        pusher.connect()    }
```

In the `sendToPusher` method, we send the payload to our backend application using `AlamoFire`, which will, in turn, send it to Pusher.

In the `listenForChanges` method, we then listen for changes to the text and, if there are any, we apply the changes to the text view.

> _? R**emember to replace the key and cluster with the actual value you have gotten from your Pusher dashboard.**_

If you have followed the tutorial closely, then your `TextEditorViewController` should look something like this:

```
import UIKit    import PusherSwift    import Alamofire
```

```
    class TextEditorViewController: UIViewController, UITextViewDelegate {        static let API_ENDPOINT = "http://localhost:4000";
```

```
        @IBOutlet weak var textView: UITextView!
```

```
        @IBOutlet weak var charactersLabel: UILabel!
```

```
        var pusher : Pusher!
```

```
        var chillPill = true
```

```
        var placeHolderText = "Start typing..."
```

```
        var randomUuid : String = ""
```

```
        override func viewDidLoad() {            super.viewDidLoad()
```

```
            // Notification trigger            NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillShow), name: NSNotification.Name.UIKeyboardWillShow, object: nil)            NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillHide), name: NSNotification.Name.UIKeyboardWillHide, object: nil)
```

```
            // Gesture recognizer            view.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(tappedAwayFunction(_:))))
```

```
            // Set the controller as the textView delegate            textView.delegate = self
```

```
            // Set the device ID            randomUuid = UIDevice.current.identifierForVendor!.uuidString
```

```
            // Listen for changes from Pusher            listenForChanges()        }
```

```
        override func viewWillAppear(_ animated: Bool) {            super.viewWillAppear(animated)
```

```
            if self.textView.text == "" {                self.textView.text = placeHolderText                self.textView.textColor = UIColor.lightGray            }        }
```

```
        func keyboardWillShow(notification: NSNotification) {            if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {                if self.charactersLabel.frame.origin.y == 1.0 {                    self.charactersLabel.frame.origin.y -= keyboardSize.height                }            }        }
```

```
        func keyboardWillHide(notification: NSNotification) {            if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {                if self.view.frame.origin.y != 1.0 {                    self.charactersLabel.frame.origin.y += keyboardSize.height                }            }        }
```

```
        func textViewDidChange(_ textView: UITextView) {            charactersLabel.text = String(format: "%i Characters", textView.text.characters.count)
```

```
            if textView.text.characters.count >= 2 {                sendToPusher(text: textView.text)            }        }
```

```
        func textViewShouldBeginEditing(_ textView: UITextView) -> Bool {            self.textView.textColor = UIColor.black
```

```
            if self.textView.text == placeHolderText {                self.textView.text = ""            }
```

```
            return true        }
```

```
        func textViewDidEndEditing(_ textView: UITextView) {            if textView.text == "" {                self.textView.text = placeHolderText                self.textView.textColor = UIColor.lightGray            }        }
```

```
        func tappedAwayFunction(_ sender: UITapGestureRecognizer) {            textView.resignFirstResponder()        }
```

```
        func sendToPusher(text: String) {            let params: Parameters = ["text": text, "from": randomUuid]
```

```
            Alamofire.request(TextEditorViewController.API_ENDPOINT + "/update_text", method: .post, parameters: params).validate().responseJSON { response in                switch response.result {
```

```
                case .success:                    print("Succeeded")                case .failure(let error):                    print(error)                }            }        }
```

```
        func listenForChanges() {            pusher = Pusher(key: "PUSHER_KEY", options: PusherClientOptions(                host: .cluster("PUSHER_CLUSTER")            ))
```

```
            let channel = pusher.subscribe("collabo")            let _ = channel.bind(eventName: "text_update", callback: { (data: Any?) -> Void in
```

```
                if let data = data as? [String: AnyObject] {                    let fromDeviceId = data["deviceId"] as! String
```

```
                    if fromDeviceId != self.randomUuid {                        let text = data["text"] as! String                        self.textView.text = text                        self.charactersLabel.text = String(format: "%i Characters", text.characters.count)                    }                }            })
```

```
            pusher.connect()        }    }
```

Great! Now we need to make the backend of the application.

### Building the backend Node application

Now that we are done with the Swift part, we can focus on creating the Node.js backend for the application. We are going to be using Express so that we can quickly get something running.

Create a directory for the web application and then create some new files.

The **index.js** file:

```
let path = require('path');    let Pusher = require('pusher');    let express = require('express');    let bodyParser = require('body-parser');    let app = express();    let pusher = new Pusher(require('./config.js'));
```

```
    app.use(bodyParser.json());    app.use(bodyParser.urlencoded({ extended: false }));
```

```
    app.post('/update_text', function(req, res){      var payload = {text: req.body.text, deviceId: req.body.from}      pusher.trigger('collabo', 'text_update', payload)      res.json({success: 200})    });
```

```
    app.use(function(req, res, next) {        var err = new Error('Not Found');        err.status = 404;        next(err);    });
```

```
    module.exports = app;
```

```
    app.listen(4000, function(){      console.log('App listening on port 4000!');    });
```

In the JS file above, we are using Express to create a simple application. In the `/update_text` route, we simply receive the payload and pass it on to Pusher. Nothing complicated there.

Create a **package.json** file also:

```
{      "main": "index.js",      "dependencies": {        "body-parser": "^1.17.2",        "express": "^4.15.3",        "path": "^0.12.7",        "pusher": "^1.5.1"      }    }
```

The **package.json** file is where we define all the NPM dependencies.

The last file to create is a **config.js** file. This is where we will define the configuration values for our Pusher application:

```
module.exports = {      appId: 'PUSHER_ID',      key: 'PUSHER_KEY',      secret: 'PUSHER_SECRET',      cluster: 'PUSHER_CLUSTER',      encrypted: true    };
```

> _? R**emember to replace the key and cluster with the actual value you have gotten from your Pusher dashboard.**_

Now run `npm install` on the directory and then `node index.js` once the npm installation is complete. You should see an _App listening on port 4000!_ message.

![Image](https://cdn-media-1.freecodecamp.org/images/TGJKpixfoUkwEIal-2tDPo25Rb7Bo8BuEWMa)

### Testing the application

Once you have your local node web server running, you will need to make some changes so your application can talk to the local web server. In the `info.plist` file, make the following changes:

![Image](https://cdn-media-1.freecodecamp.org/images/FARWGcIZQDh0lMGVsdWlhAmDwm1FIon921ch)

With this change, you can build and run your application and it will talk directly with your local web application.

### Conclusion

In this article, we have covered how to build a realtime collaborative text editor on iOS using Pusher. Hopefully, you have learned a thing or two from following the tutorial. For practice, you can expand the statuses to support more instances.

This post was first published to [Pusher](https://pusher.com/tutorials/collaborative-text-editor-swift/).

