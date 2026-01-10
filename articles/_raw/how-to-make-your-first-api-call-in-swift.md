---
title: How to make an API call in Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-29T11:49:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-first-api-call-in-swift
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ef3740569d1a4ca4004.jpg
tags:
- name: api
  slug: api
- name: iOS
  slug: ios
- name: Swift
  slug: swift
seo_title: null
seo_desc: 'By Ai-Lyn Tang

  If you are looking to become an iOS developer, there are some fundamental skills
  worth knowing. First, it''s important to be familiar with creating table views.
  Second, you should know how to populate those table views with data. Third,...'
---

By Ai-Lyn Tang

If you are looking to become an iOS developer, there are some fundamental skills worth knowing. First, it's important to be familiar with creating table views. Second, you should know how to populate those table views with data. Third, it's great if you can fetch data from an API and use this data in your table view.

The third point is what we'll cover in this article. Since the introduction of `Codable` in Swift 4, making API calls is much easier. Previously most people used pods like Alamofire and SwiftyJson (you can read about how to do that [here](https://code.likeagirl.io/3-steps-to-make-your-first-api-call-836e43ed702c)). Now the Swift way is much nicer out of the box, so there's no reason to download a pod.

Let's go through some building blocks that are often used to make an API call. We'll cover these concepts first, as they are important parts to understanding how to make an API call.

* Completion handlers
* `URLSession`
* `DispatchQueue`
* Retain cycles

Finally we'll put it all together. I'll be using the open source [Star Wars API](https://www.swapi.co/) to build this project. You can see my full project code on [GitHub](https://github.com/ailyntang/starwars/).

_Disclaimer alert: I am new to coding and am largely self-taught. Apologies if I misrepresent some concepts._

## Completion handlers

![Image](https://www.freecodecamp.org/news/content/images/2019/10/pheobe.jpeg)
_Poor patient Pheobe_

Remember the episode of Friends where Pheobe is glued to the phone for days waiting to speak with customer service? Imagine if at the very start of that phone call, a lovely person called Pip said: "Thanks for calling. I have no idea how long you'll need to wait on hold, but I'll call you back when we're ready for you." It wouldn't have been as funny, but Pip is offering to be a completion handler for Pheobe.

You use a completion handler in a function when you know that function will take a while to complete. You don't know how long, and you don't want to pause your life waiting for it to finish. So you ask Pip to tap you on the shoulder when she's ready to give you the answer. That way you can go about your life, run some errands, read a book, and watch TV. When Pip taps on you on the shoulder with the answer, you can take her answer and use it.

This is what happens with API calls. You send a URL request to a server, asking it for some data. You hope the server returns the data quickly, but you don't know how long it will take. Instead of making your user wait patiently for the server to give you the data, you use a completion handler. This means you can tell your app to go off and do other things, such as loading the rest of the page.

You tell the completion handler to tap your app on the shoulder once it has the information you want. You can specify what that information is. That way, when your app gets tapped on the shoulder, it can take the information from the completion handler and do something with it. Usually what you'll do is reload the table view so the data appears to the user.

Here's an example of what a completion handler looks like. The first example is setting up the API call itself:

```swift
func fetchFilms(completionHandler: @escaping ([Film]) -> Void) {
  // Setup the variable lotsOfFilms
  var lotsOfFilms: [Film]
  
  // Call the API with some code
  
  // Using data from the API, assign a value to lotsOfFilms  
  
  // Give the completion handler the variable, lotsOfFilms
  completionHandler(lotsOfFilms)
}
```

Now we want to call the function `fetchFilms`. Some things to note:

* You don't need to reference `completionHandler` when you call the function. The only time you reference `completionHandler` is inside the function declaration.
* The completion handler will give us back some data to use. Based on the function we've written above, we know to expect data which is of type `[Film]`. We need to name the data so that we can refer to it. Below I'm using the name `films`, but it could be `randomData`, or any other variable name I'd like.

The code will look something like this: 

```swift
fetchFilms() { (films) in
  // Do something with the data the completion handler returns 
  print(films)
}
```

## URLSession

`URLSession` is like the manager of a team. The manager doesn't do anything on her own. Her job is to share the work with the people in her team, and they'll get the job done. Her team are `dataTasks`. Every time you need some data, write to the boss and use `URLSession.shared.dataTask`.  

You can give the `dataTask` different types of information to help you achieve your goal. Giving information to `dataTask` is called initialization. I initialism my `dataTasks` with URLs. `dataTasks` also use completion handlers as part of their initialization. Here's an example:

```swift
let url = URL(string: "https://www.swapi.co/api/films")

let task = URLSession.shared.dataTask(with: url, completionHandler: { (data, response, error) in 
  // your code here
})

task.resume()
```

`dataTasks` use completion handlers, and they always return the same types of information: `data`, `response` and `error`. You can give these data types different names, like `(data, res, err)` or `(someData, someResponse, someError)`. For the sake of convention, it's best to stick to something obvious rather than go rogue with new variable names.

Let's start with `error`. If the `dataTask` returns an `error`, you'll  want to know that upfront. It means you can direct your code to handle the error gracefully. It also means you won't bother trying to read the data and do something with it as there is an error in returning the data. 

Below I am handling the error really simply by printing an error to the console and exiting the function. There are many other ways you could handle the error if you wanted to. Think about how fundamental this data is to your app. For example, if you have a banking app and this API call shows users their balance, then you may want to handle the error by presenting a modal to the user that says, "Sorry, we're experiencing a problem right now. Please try again later."

```swift
if let error = error {
  print("Error accessing swapi.co: /(error)")
  return
}
```

Next we look at the response. You can cast the response to be an `httpResponse`. That way you can look at the status codes and make some decisions based on the code. For example, if the status code is 404, then you know the page was not found. 

The code below uses a `guard` to check that two things exist. If both exist, then it allows the code to continue to the next statement after the `guard` clause. If either of the statements fail, then we exit the function. This is a typical use case of a `guard` clause. You expect the code after a guard clause to be the happy days flow (i.e. the easy flow with no errors).

```swift
  guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
    print("Error with the response, unexpected status code: \(response)")
    return
  }
```

Finally you handle the data itself. Notice that we haven't used the completion handler for the `error` or the `response`. That's because the completion handler is waiting for data from the API. If it doesn't get to the data part of the code, there's no need to invoke the handler.

For the data, we are using the `JSONDecoder` to parse the data in a nice way. This is pretty nifty, but requires that you have established a model. Our model is called `FilmSummary`. If `JSONDecoder` is new to you, then have a look online for how to use it and how to use `Codable`. It's really simple in Swift 4 and above compared to the Swift 3 days.

In the code below, we are first checking that the data exists. We are pretty sure it should exist, because there are no errors and no strange HTTP responses. Second, we check that we can parse the data we receive in the way we expect. If we can, then we return the film summary to the completion handler. Just in case there is no data to return from the API, we have a fall back plan of the empty array.

```swift
if let data = data,
        let filmSummary = try? JSONDecoder().decode(FilmSummary.self, from: data) {
        completionHandler(filmSummary.results ?? [])
      }
```

So the full code for API call looks like this:

```swift
func fetchFilms(completionHandler: @escaping ([Film]) -> Void) {
    let url = URL(string: domainUrlString + "films/")!

    let task = URLSession.shared.dataTask(with: url, completionHandler: { (data, response, error) in
      if let error = error {
        print("Error with fetching films: \(error)")
        return
      }
      
      guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
        print("Error with the response, unexpected status code: \(response)")
        return
      }

      if let data = data,
        let filmSummary = try? JSONDecoder().decode(FilmSummary.self, from: data) {
        completionHandler(filmSummary.results ?? [])
      }
    })
    task.resume()
  }
```

## Retain cycles

_NB: I am extremely new to understanding retain cycles! Here's the gist of what I researched online._

Retain cycles are important to understand for memory management. Basically you want your app to clean up bits of memory that it doesn't need anymore. I assume this makes the app more performant. 

There are lots of ways that Swift helps you do this automatically. However there are many ways that you can accidentally code retain cycles into your app. A retain cycle means that your app will always hold on to the memory for a certain piece of code. Generally it happens when you have two things that have strong pointers to each other. 

To get around this, people often use `weak`. When one side of the code is `weak`, you don't have a retain cycle and your app will be able to release the memory. 

For our purpose, a common pattern is to use `[weak self]` when calling the API. This ensures that once the completion handler returns some code, the app can release the memory.

```swift
fetchFilms { [weak self] (films) in
  // code in here
}
```

## DispatchQueue

Xcode uses different threads to execute code in parallel. The advantage of multiple threads means you aren't stuck waiting on one thing to finish before you can move on to the next. Hopefully you can start to see the links to completion handlers here.

These threads seem to be also called dispatch queues. API calls are handled on one queue, typically a queue in the background. Once you have the data from your API call, most likely you'll want to show that data to the user. That means you'll want to refresh your table view.

Table views are part of the UI, and all UI manipulations should be done in the main dispatch queue. This means somewhere in your view controller file, usually as part of the `viewDidLoad` function, you should have a bit of code that tells your table view to refresh. 

We only want the table view to refresh once it has some new data from the API. This means we'll use a completion handler to tap us on the shoulder and tell us when that API call is finished. We'll wait until that tap before we refresh the table.

The code will look something like:

```swift
fetchFilms { [weak self] (films) in
  self.films = films

  // Reload the table view using the main dispatch queue
  DispatchQueue.main.async {
    tableView.reloadData()
  }
}
```

## viewDidLoad vs viewDidAppear

Finally you need to decide where to call your `fetchfilms` function. It will be inside a view controller that will use the data from the API. There are two obvious places you could make this API call. One is inside `viewDidLoad` and the other is inside `viewDidAppear`.

These are two different states for your app. My understanding is `viewDidLoad` is called the first time you load up that view in the foreground. `viewDidAppear` is called every time you come back to that view, for example when you press the back button to come back to the view.

If you expect your data to change in between the times that the user will navigate to and from that view, then you may want to put your API call in `viewDidAppear`. However I think for almost all apps, `viewDidLoad` is sufficient. Apple recommends `viewDidAppear` for all API calls, but that seems like overkill. I imagine it would make your app less performant as it's making many more API calls that it needs to.

## Combining all the steps

First: write the function that calls the API. Above, this is `fetchFilms`. This will have a completion handler, which will return the data you are interested in. In my example, the completion handler returns an array of films.

Second: call this function in your view controller. You do this here because you want to update the view based on the data from the API. In my example, I am refreshing a table view once the API returns the data.

Third: decide where in your view controller you would like to call the function. In my example, I call it in `viewDidLoad`.

Fourth: decide what to do with the data from the API. In my example, I am refreshing a table view.

Inside `NetworkManager.swift` (this function can be defined in your view controller if you'd like, but I am using the MVVM pattern).

```swift
func fetchFilms(completionHandler: @escaping ([Film]) -> Void) {
    let url = URL(string: domainUrlString + "films/")!

    let task = URLSession.shared.dataTask(with: url, completionHandler: { (data, response, error) in
      if let error = error {
        print("Error with fetching films: \(error)")
        return
      }
      
      guard let httpResponse = response as? HTTPURLResponse,
            (200...299).contains(httpResponse.statusCode) else {
        print("Error with the response, unexpected status code: \(response)")
        return
      }

      if let data = data,
        let filmSummary = try? JSONDecoder().decode(FilmSummary.self, from: data) {
        completionHandler(filmSummary.results ?? [])
      }
    })
    task.resume()
  }
```

Inside `FilmsViewController.swift`:

```swift
final class FilmsViewController: UIViewController {
  private var films: [Film]?

  override func viewDidLoad() {
    super.viewDidLoad()
    
    NetworkManager().fetchFilms { [weak self] (films) in
      self?.films = films
      DispatchQueue.main.async {
        self?.tableView.reloadData()
      }
    }
  }
  
  // other code for the view controller
}
```

Gosh, we made it! Thanks for sticking with me.

