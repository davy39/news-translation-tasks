---
title: 'Going serverless with React and AWS Amplify Part 2: Creating And Using Serverless
  Services'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T16:52:41.000Z'
originalURL: https://freecodecamp.org/news/going-serverless-with-react-and-aws-amplify-part-2-creating-and-using-serverless-services-d401ba346eeb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0iJpmj6zVTc8EHFGW5VTnA.png
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Peter Mbanugo

  Serverless is a cloud-computing execution model in which the cloud provider is responsible
  for executing a piece of code by dynamically allocating resources to run the code
  when needed. In a previous post, we looked at what serverles...'
---

By Peter Mbanugo

Serverless is a cloud-computing execution model in which the cloud provider is responsible for executing a piece of code by dynamically allocating resources to run the code when needed. In a previous [post](https://medium.freecodecamp.org/going-serverless-with-react-and-aws-amplify-development-environment-set-up-9b15c3363bd), we looked at what serverless is, and we set up our computer to be able to build serverless applications using AWS Amplify. We bootstrapped a React project and added the Amplify library to it. In this post, we will use the Amplify CLI to provision a secured backend API and a NoSQL database. Then we will consume this API from the React project.

### Creating The Serverless Backend Services

The application we’re going to build will allow users to perform basic CRUD operations. We will use a REST API with a NoSQL database. Follow the instruction below to create the serverless backend.

1. Open the command line and go to the root directory of your project.
2. Run the command `amplify add api`.
3. You get a prompt to select a service type. Choose `REST` and press Enter.
4. It prompts you to enter a name for the current category (the API category). Enter `todosApi` and press Enter.
5. You’re asked for a path. Accept the default `items` path by pressing Enter.
6. The next prompt asks for the Lambda source. The serverless REST API works by creating a path on API Gateway and mapping that path to a lambda function. The lambda function contains code to execute when a request is made to the path it’s mapped to. We will create a new lambda. Select the option `Create a new Lambda function` and press Enter.
7. Enter `todosLambda` as the name of the resource for the category (function category), and press Enter.
8. You will be asked for the name of the lambda function. Enter `todos` and press Enter.
9. You will be asked to choose a template for generating code for this function. Choose the option `CRUD function for Amazon DynamoDB table (Integration with Amazon API Gateway and Amazon DynamoDB)` and press Enter. This creates an architecture using API Gateway with Express running in an AWS Lambda function that reads and writes to Amazon DynamoDB.
10. The next prompt asks you to choose a DynanoDB data source. We do not have an existing DynamoDB table so we will choose the `Create a new DynamoDB table` option. Press Enter to continue. Now you should see DynamoDB database wizard. It'll ask a series of questions to determine how to create the database.
11. You will be asked to enter the name for this resource. Enter `todosTable` and press Enter.
12. The next prompt is for the table name. Enter `todos` and press Enter.
13. You will be asked to add columns to the DynamoDB table. Follow the prompt to create column `id` with `String` as its type.
14. Select `id` column when asked for the partition key (primary key) for the table.
15. You will be asked if you want to add a sort key to the table. Choose false.
16. The next prompt asks if you want to add global secondary indexes to your table. Enter `n` and press Enter. You should see the message `Successfully added DynamoDb table locally`
17. The next prompt asks **Do you want to edit the local lambda function now?**. Enter `n` and press Enter. You should see the message `Successfully added the Lambda function locally`.
18. You get asked if you want to restrict access to the API. Enter `y` and press Enter.
19. For the next prompt, choose `Authenticated and Guest users` and press Enter. This option gives both authorized and guest users access to the REST API.
20. Next, you get asked `What kind of access do you want for Authenticated users`. Choose `read/write` and press Enter.
21. Now we get a prompt to choose the kind of access for unauthenticated users (i.e gues users). Choose `read` and press Enter. You should get the message `Successfully added auth resource locally`. This is because we have chosen to restrict access to the API, and the CLI added the Auth category to the project since we don't have any for the project. At this point, we've added resources that are needed to create our API (API Gateway, DynamoDB, Lambda function, and Cognito for authentication).
22. We get asked if we want to add another path to the API. Enter `n` and press Enter. This completes the process and we get the message `Successfully added resource todosApi locally`.

The `amplify add api` command took us through the process of creating a REST API. This API will be created based on the options we chose. To create this API requires 4 AWS services. They're:

1. Amazon DynamoDB. This will serve as our NoSQL database. We created a DynomoDB table named `todos` when we added the `todosTable` resource. We gave it 3 columns with `id` as the primary key.
2. AWS Lambda functions. This lets us run code without provisioning or managing servers. This is where our code to perform CRUD operations on the DynamoDB table will be.
3. Amazon Cognito. This is responsible for authentication and user management. This lets us add user sign-up, sign-in, and access control to our app. We chose the option to restrict access to our API, and this service will help us authenticate users.
4. Amazon API Gateway. This is what allows us to create REST API endpoint. We added a resource for this named `todosApi`, with a path `items`. We also selected the option to restrict access to the API.

However, the service specifications for these services are not yet in the cloud. We need to update the project in the cloud with information to provide the needed services. Run the command `amplify status`, and we should get a table with information about the amplify project.

![Image](https://cdn-media-1.freecodecamp.org/images/g08emYbuJANf72jvqIJIJmBvofadlT35UY13)

Open the file **backend/function/todosLambda/src/app.js**. You will notice that this file contains code generated during the resource set up process. It uses [Express.js](https://expressjs.com/) to set up routes, and [aws-serverless-express](https://github.com/awslabs/aws-serverless-express) package to easily build RESTful APIs using the Express.js framework on top of AWS Lambda and Amazon API Gateway.

When we push the project configuration to the cloud, it’ll configure a simple proxy API using Amazon API Gateway and integrate it with this Lambda function. The package includes middleware to easily get the event object Lambda receives from API Gateway. It was applied on line 32 `app.use(awsServerlessExpressMiddleware.eventContext());` and used across the routes with codes that looks like `req.apiGateway.event.*`. The pre-defined routes allow us to perform CRUD operation on the DynamoDB table.

We will make a couple of changes to this file. The first will be to change the value for `tableName` variable from `todosTable` to `todos`. When creating the DynamoDB resource, we specified `todosTable` as the resource name and `todos` as the table name, so it wrongly used the resource name as the table name when the file was created. This would likely be fixed in a future version of the CLI, so if you don't find it wrongly used, you can skip this step. We will also need to update the definitions.

Change the first route definition to use the code below.

```
app.get(path, function(req, res) {  const queryParams = {    TableName: tableName,    ProjectionExpression: "id, title"  };
```

```
  dynamodb.scan(queryParams, (err, data) => {    if (err) {      res.json({ error: "Could not load items: " + err });    } else {      res.json(data.Items);    }  });});
```

This defines a route to respond to the **/items** path with code to return all data in the DynamoDB table. The `ProjectionExpression` values are used to specify that it should get only the columns `id` and `title`.

Change the route definition on line 77 to read as `app.get(path + hashKeyPath + sortKeyPath, function(req, res) {`. This allows us to retrieve an item by its `id` following the path **/items/:id**. Also, change line 173 to be `app.delete(path + hashKeyPath + sortKeyPath, function(req, res) {`. This responds to HTTP DELETE method to delete an item following the path **/items/:id**.

The AWS resources have been added and updated locally, and we need to provision them in the cloud. Open the command line and run `amplify push`. You'll get a prompt if you want to continue executing the command. Enter `y` and press Enter. What this does is that it'll upload the latest versions of the resources nested stack templates to an S3 deployment bucket, and then call the AWS CloudFormation API to create / update resources in the cloud.

### Building The Frontend

When the `amplify push` command completes, you'll see a file **aws-exports.js** in the **src** folder. This file contains information to the resources that were created in the cloud. Each time a resource is created or updated by running the `push` command, this file will be updated. It's created for JavaScript projects and will be used in Amplify JavaScript library. We will be using this in our React project. We will also use Bootstrap to style the page. Open **public/index.html** and add the following in the head:

```
<link  rel="stylesheet"  href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"  integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"  crossorigin="anonymous"/><script  src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"  crossorigin="anonymous"></script><script  src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"  integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"  crossorigin="anonymous"></script><script  src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"  integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"  crossorigin="anonymous"></script>
```

Add a new file **src/List.js** with the following content:

```
import React from "react";
```

```
export default props => (  <div>    <legend>List</legend>    <div className="card" style={{ width: "25rem" }}>      {renderListItem(props.list, props.loadDetailsPage)}    </div>  </div>);
```

```
function renderListItem(list, loadDetailsPage) {  const listItems = list.map(item => (    <li      key={item.id}      className="list-group-item"      onClick={() => loadDetailsPage(item.id)}    >      {item.title}    </li>  ));
```

```
  return <ul className="list-group list-group-flush">{listItems}&lt;/ul>;}
```

This component will render a list of items from the API. Add a new file **src/Details.js** with the following content:

```
import React from "react";
```

```
export default props => (  <div>    <h2>Details</h2>    <div className="btn-group" role="group">      <button        type="button"        className="btn btn-secondary"        onClick={props.loadListPage}      >        Back to List      </button>      <button        type="button"        className="btn btn-danger"        onClick={() => props.delete(props.item.id)}      >        Delete      </button>    </div>    <legend>{props.item.title}</legend>    <div className="card">      <div className="card-body">{props.item.content}</div>    </div>  </div>);
```

This component will display the details of an item with buttons to delete that item or go back to the list view. Open **src/App.js** and update it with this code:

```
import React, { Component } from "react";import List from "./List";import Details from "./Details";
```

```
import Amplify, { API } from "aws-amplify";import aws_exports from "./aws-exports";import { withAuthenticator } from "aws-amplify-react";Amplify.configure(aws_exports);
```

```
class App extends Component {  constructor(props) {    super(props);    this.state = {      content: "",      title: "",      list: [],      item: {},      showDetails: false    };  }
```

```
  async componentDidMount() {    await this.fetchList();  }  handleChange = event => {    const id = event.target.id;    this.setState({ [id]: event.target.value });  };
```

```
  handleSubmit = async event => {    event.preventDefault();    await API.post("todosApi", "/items", {      body: {        id: Date.now().toString(),        title: this.state.title,        content: this.state.content      }    });
```

```
    this.setState({ content: "", title: "" });    this.fetchList();  };  async fetchList() {    const response = await API.get("todosApi", "/items");    this.setState({ list: [...response] });  }
```

```
  loadDetailsPage = async id => {    const response = await API.get("todosApi", "/items/" + id);    this.setState({ item: { ...response }, showDetails: true });  };
```

```
  loadListPage = () => {    this.setState({ showDetails: false });  };
```

```
  delete = async id => {    //TODO: Implement functionality  };
```

```
  render() {    return (      <div className="container">        <form onSubmit={this.handleSubmit}>          <legend>Add</legend>          <div className="form-group">            <label htmlFor="title">Title</label>            <input              type="text"              className="form-control"              id="title"              placeholder="Title"              value={this.state.title}              onChange={this.handleChange}            />          </div>          <div className="form-group">            <label htmlFor="content">Content</label>            <textarea              className="form-control"              id="content"              placeholder="Content"              value={this.state.content}              onChange={this.handleChange}            />          </div>          <button type="submit" className="btn btn-primary">            Submit          </button>        </form>        <hr />        {this.state.showDetails ? (          <Details            item={this.state.item}            loadListPage={this.loadListPage}            delete={this.delete}          />        ) : (          <List list={this.state.list} loadDetailsPage={this.loadDetailsPage} />        )}      </div>    );  }}
```

```
export default withAuthenticator(App, true);
```

We imported the Amplify library and initialized it by calling `Amplify.configure(aws_exports);`. When the component is mounted, we call `fetchList()` to retrieve items from the API.

This function uses the API client from the Amplify library to call the REST API. Under the hood, it utilizes [Axios](https://github.com/axios/axios) to execute the HTTP requests. It'll add necessary headers to the request so you can successfully call the REST API. You can add headers if you defined custom headers for your API.

For our project, we only specify the apiName and path when invoking the functions from the API client. The `loadDetailsPage()` function fetches a particular item from the database through the API. Then sets `item` state with the response and `showDetails` to true. This `showDetails` is used in the render function to toggle between showing a list of items or the details page of a selected item. The function `handleSubmit()` is called when the form is submitted. It sends the form data to the API to create a document in the database, with columns `id`, `title` and `content`, then calls `fetchList()` to update the list. I left the `delete()` function empty so you can implement it yourself. What better way to learn than to try it yourself ?.

This function will be called from the delete button in the `Details` component. The code you have in it should call the API to delete an item by `id` and display the list component with correct items.

We wrapped the App component with the `withAuthenticator` higher order component from the Amplify React library. This provides the app with complete flows for user registration, sign-in, signup, and sign out. Only signed in users can access the app since we're using this higher order component. The `withAuthenticator` component automatically detects the authentication state and updates the UI. If the user is signed in, the underlying **App** component is displayed, otherwise, sign-in/signup controls are displayed.

The second argument which was set to `true` tells it to display a sign-out button at the top of the page. Using the `withAuthenticator` component is the simplest way to add authentication flows into your app. You can also have a custom UI and use set of APIs from the Amplify library to implement sign-in and sign up flows. See the [docs](https://aws-amplify.github.io/docs/js/authentication#working-with-the-api) for more details.

We have all the code necessary to use the application. Open the terminal and run `npm start` to start the application. You'll need to signup and sign in to use the application.

![Image](https://cdn-media-1.freecodecamp.org/images/XpzhaOkjAB6ppf7XWKFAK8eMlbbzfU67letq)
_completed application_

### Wrapping Up

We went through creating our backend services using the Amplify CLI. The command `amplify add api` took us through adding resources for DynamoDB, Lambda, API Gateway, and Cognito for authentication. We updated the code in **backend/function/todosLambda/src/app.js** to match our API requirement. We added UI components to perform CRUD operations on the app and used a higher order component from the Amplify React library to allow only authenticated users access to the application.

You should notice we only used a few lines of code to add authentication flows and call the API. Also creating the serverless backend services and connecting them all together was done with a command and responding to the prompts that followed. Thus showing how AWS Amplify makes development easier.

> _Originally posted on my [blog](https://www.pmbanugo.me/blog/2019-01-14-going-serverless-with-react-and-aws-amplify-part-2-creating-and-using-serverless-services/)._

