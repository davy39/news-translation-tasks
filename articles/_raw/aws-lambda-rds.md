---
title: How to Connect to AWS RDS from AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-09T23:22:38.000Z'
originalURL: https://freecodecamp.org/news/aws-lambda-rds
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/AWS-Lambda-RDS-Proxy-1.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: database
  slug: database
seo_title: null
seo_desc: "By Mugilan Ragupathi\nIn this article, we're going to learn about how to\
  \ communicate with AWS RDS from AWS Lambda. \nIn this tutorial, we'll be using AWS\
  \ CDK. It's an open source software development framework that lets you define cloud\
  \ infrastructure...."
---

By Mugilan Ragupathi

In this article, we're going to learn about how to communicate with AWS RDS from AWS Lambda. 

In this tutorial, we'll be using `AWS CDK`. It's an open source software development framework that lets you define cloud infrastructure. 

`AWS CDK` supports many languages including TypeScript, Python, C#, Java and others. We're going to use TypeScript in this tutorial. 

When deploying (using the `cdk deploy` command), your code is converted to Cloudformation templates, and all the corresponding AWS resources are created. Only basic knowledge of CDK and TypeScript is required for trying this tutorial. Of course, you need to have an AWS account to create AWS resources.

You can learn more about AWS CDK from the docs [here](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html), and I wrote a beginner's guide to it on my blog [here](https://www.cloudtechsimplified.com/the-beginners-guide-to-aws-cdk/).

## Introduction to AWS Lambda and RDS

AWS Lambda is a serverless, event-driven compute service which lets you run your code without having to provision servers.

AWS RDS is a managed relational database service from AWS and supports various RDMBS such as MySQL, Postgres, Oracle, SQL Server and so on. AWS takes care of setting up, patching, and maintaining these database servers.

### Why would you use RDS with Lambda?

AWS Lambda is just a compute service and it does not have any recommendation about data stores. In fact, some of your lambda functions will not even interact with data stores of any kind. Even if you want to use a data store, you could use any type of database based on your needs.

However, most of the serverless architectures use DynamoDB as a data store just to reduce costs and eliminate the need to maintain database servers.   
  
DynamoDB is great and has its use cases. But using DynamoDB for all projects involving lambda is not possible for the following reasons:

**Dynamic access patterns:** If you're using DynamoDB, you would have to design your querying patterns in advance. This isn't always possible, as your product (and its associated requirements) might evolve based on customer feedback. 

**Limited access patterns:** DynamoDB does not provide flexibility in writing your queries. You can't do `group by` functionality just as you do in RDBMS. You need to export the data and have some other system to provide that functionality.

**Existing database:** If you have an existing RDBMS database, you wouldn't want to migrate to DynamoDB unless there is a compelling reason to do so. Even if you want to use DynamoDB, you might have to re-write your entire data access layer to use DynamoDB instead of a regular RDBMS. 

### Pros for using RDBMS:

**Relationship between entities:** RDBMS allows relationships between entities. You can define foreign keys to restrict any invalid data from getting stored in the database.

**Access patterns:** RDMBS allows you to use dynamic access patterns. A new entity can be brought in without much change to any of the existing models. And, it has many functionalities such as `group by` – so that you don't need to have any external system to do such functionalities.

**Familiarity with SQL:** Most developers are familiar with SQL to query databases, and you have a wide range of databases to choose from, including Oracle, Postgres, and MySQL.

You might choose RDMBS if you have following requirements:

* You have an existing RDBMS database and you'd like to adapt serverless compute provided by AWS Lambda
* You have dynamic access patterns and you don't want to change much of your existing models

With that out of our way, let's discuss how we're going to connect to RDS from Lambda.

## Project Architecture

In almost all cases, your RDBMS database will be in a private subnet of the Virtual Private Cloud (VPC) so that no one from outside of the VPC can access it. As your lambda function will contain business logic, this lambda might also be in a private subnet.  
  
We're going to use Postgres as our database in this tutorial. But the process here is applicable for any database (MySQL, Oracle, MS SQL and so on) that you want to use. The architecture will remain the same.

Below is the architecture for this project:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/AWS-Lambda-RDS-Latest.png)

We're going to use `AWS CDK` as an Infrastructure as Code (IaC) tool to create the AWS resources

### How to Create a Virtual Private Cloud to Host our Lambda and RDBMS

We're going to create 2 subnets – a private subnet and a public subnet. In the private subnet, we'll have our Postgres database.

```typescript
const vpc = new ec2.Vpc(this, 'VpcLambda', {
      maxAzs: 2,
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: 'privatelambda',
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
        },
        {
          cidrMask: 24,
          name: 'public',
          subnetType: ec2.SubnetType.PUBLIC,
        },
      ],
    });
```

When you create a subnet of type `PRIVATE_WITH_EGRESS` in AWS CDK, it will also create a NAT Gateway and will place that NAT Gateway in the public subnet. 

The purpose of the NAT Gateway is to allow only the outbound connections from your private subnet to the internet. No one can initiate connections to your private subnet from the public internet.

### Why Are We Using NAT Gateway for Internet Connectivity?

You may be wondering why you need an internet connection, as we have both lambda and the RDS database in the same private subnet.

`Secrets Manager` is a service from AWS for storing and managing secrets such as database passwords, certificates, and so on. The password for connecting to the database is stored in `secrets manager` which is accessible by public endpoint.   
  
Either you can use `NAT Gateway` to access the public endpoint of the `secrets manager` service or you can create an interface endpoint to connect to `secrets manager` using AWS Network without going to the public internet.

Both will cost money, but NAT Gateway can be re-used for making internet connections from the lambda too (say if you're calling any public external API) whereas in an interface endpoint you would not be able to do that.

### How to Create an RDS Database Instance to Store Our Data:

We're going to use a `small` instance type for the database – just for the sake of this tutorial. But in production environments, you'll likely be using instances of larger sizes. 

We're creating a new security group for the database so that we can control who can access the database instance and through which port.

```typescript
const dbSecurityGroup = new ec2.SecurityGroup(this, 'DbSecurityGroup', {
      vpc,
    });

    const databaseName = 'cloudtechsimplified';

    const dbInstance = new rds.DatabaseInstance(this, 'Instance', {
      engine: rds.DatabaseInstanceEngine.postgres({
        version: rds.PostgresEngineVersion.VER_13,
      }),
      // optional, defaults to m5.large
      instanceType: ec2.InstanceType.of(
        ec2.InstanceClass.BURSTABLE3,
        ec2.InstanceSize.SMALL
      ),
      vpc,
      vpcSubnets: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      }),
      databaseName,
      securityGroups: [dbSecurityGroup],
      credentials: rds.Credentials.fromGeneratedSecret('postgres'),
      maxAllocatedStorage: 200,
    });
```

The above `CDK` code will create a database instance and place it in the private subnet (as per the subnet selection that we've made).  
  
The method `fromGeneratedSecret` will create the secret in the secret manager service with the user name passed as a parameter. We want the database username to be `postgres`, so we're passing that value.  
  
And finally, we're allocating 200GB of storage space for the database.

### How to Configure Lambda Function Properties

We're using Node16 for writing our lambda function, and below are the generic properties for the lambda. 

We want timeout to be 3 minutes instead of the default 3 seconds, and we want to allocate 256 MB for the lambda function. 

As `aws-sdk` is provided by the lambda runtime itself, we want to exclude the `aws-sdk` library while bundling the lambda. 

We've installed the `pg` npm package for communicating with the Postgres database and we're excluding the `pg-native` package as we don't need it.

```typescript
 const nodeJsFunctionProps: NodejsFunctionProps = {
      bundling: {
        externalModules: [
          'aws-sdk', // Use the 'aws-sdk' available in the Lambda runtime
          'pg-native',
        ],
      },
      runtime: Runtime.NODEJS_16_X,
      timeout: Duration.minutes(3), // Default is 3 seconds
      memorySize: 256,
    };
```

Next, we'll create a security group for the lambda function. Our lambda function should have information about the endpoint, user name, and password of the database so that lambda can connect to the database. 

We're going to pass these values as environment variables to the lambda function.

```typescript
 const lambdaSG = new ec2.SecurityGroup(this, 'LambdaSG', {
      vpc,
    });

    const rdsLambdaFn = new NodejsFunction(this, 'rdsLambdaFn', {
      entry: path.join(__dirname, '../src/lambdas', 'rds-lambda.ts'),
      ...nodeJsFunctionProps,
      functionName: 'rdsLambdaFn',
      environment: {
        DB_ENDPOINT_ADDRESS: dbInstance.dbInstanceEndpointAddress,
        DB_NAME: databaseName,
        DB_SECRET_ARN: dbInstance.secret?.secretFullArn || '',
      },
      vpc,
      vpcSubnets: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      }),
      securityGroups: [lambdaSG],
    });
```

**Important note:** We're not passing the database password as an environment variable to the lambda. Instead, we're passing the `ARN`(Amazon Resource Name) to the lambda and we'll be fetching the actual password (dynamically at runtime ) from the secret manager within lambda for better security.

### Permissions for Lambda to Access the Database Password

Even though we pass the `secret arn` to lambda as an environment variable, lambda should have the necessary permissions to fetch the secret (database password, in our case) from the `secrets manager` service. 

The below line of code provides those permissions:

```typescript
dbInstance.secret?.grantRead(rdsLambdaFn);
```

The above `cdk` line will create a role for the lambda with 2 permissions `DescribeSecret` and `GetSecretValue` of the secrets manager so that our lambda will have permissions to get the secret value (database password, in our case) before talking to the database.  
  
You can see the same in the AWS console in Lambda service.

![AWS Lambda Permissions for Secrets Manager](https://www.freecodecamp.org/news/content/images/2022/11/image-23.png)
_AWS Lambda Permissions for Secrets Manager_

### Security Group for RDS Database Instance

We don't want to allow the connection to the database to be open for all and we want the database connections to be allowed from lambda. 

The below `cdk` code adds an ingress rule for allowing connectivity from our lambda function to the RDS instance through the port `5432` (port for the Postgres database):

```typescript
  dbSecurityGroup.addIngressRule(
      lambdaSG,
      ec2.Port.tcp(5432),
      'Lambda to Postgres database'
    );
```

### Lambda Function Code to Communicate with the Database

The actual lambda function code where it talks to the database is pretty simple. As we're using a Postgres database, we're using the `pg` package to communicate with Postgres from the `nodejs` environment.  
  
Before initiating the connection to the database, we're fetching the secret string from the `secrets manager` service. This secret string is a JSON string which contains both username and password. Just parse the JSON string and take only the password.

```
import * as AWS from 'aws-sdk';
import { Client } from 'pg';

export const handler = async (event: any, context: any): Promise<any> => {
  try {
    const host = process.env.DB_ENDPOINT_ADDRESS || '';
    console.log(`host:${host}`);
    const database = process.env.DB_NAME || '';
    const dbSecretArn = process.env.DB_SECRET_ARN || '';
    const secretManager = new AWS.SecretsManager({
      region: 'us-east-1',
    });
    const secretParams: AWS.SecretsManager.GetSecretValueRequest = {
      SecretId: dbSecretArn,
    };
    const dbSecret = await secretManager.getSecretValue(secretParams).promise();
    const secretString = dbSecret.SecretString || '';

    if (!secretString) {
      throw new Error('secret string is empty');
    }

    const { password } = JSON.parse(secretString);

    const client = new Client({
      user: 'postgres',
      host,
      database,
      password,
      port: 5432,
    });
    await client.connect();
    const res = await client.query('SELECT $1::text as message', [
      'Hello world!',
    ]);
    console.log(res.rows[0].message); // Hello world!
    await client.end();
  } catch (err) {
    console.log('error while trying to connect to db');
  }
};

```

And, finally we're running a simple select query in our database.

### How to Test the Project

Now, you can log-in to your AWS console for testing. Select the `Lambda` service and select your lambda function – in our case, it would be `rdsLambdaFn` . 

You don't need to worry about the `event` property of lambda for this tutorial, as we're not using it in our lambda function code. Click the Test button, and you'll be able to see the logs.

![Test Lambda function](https://www.freecodecamp.org/news/content/images/2022/11/Lambda-perf-without-proxy.png)
_Test Lambda function_

### The Performance Problem

Lambda is well-suited for functions which don't take much time. In fact, the maximum timeout limit of a lambda function is 15 minutes. 

As you can see from the lambda code, we're initiating the connection to the database every time the lambda function is invoked. 

Depending on the event source for the lambda (SQS queue, for instance), this would create connections at a higher rate and would disconnect at the end of the lambda function.  
  
This increases the load on the RDS server significantly which in turn reduces the performance. So how do we fix this problem?

## How to Use RDS Proxy

Instead of directly creating connections from lambda to the database, we can have an RDS Proxy sit in between the lambda and the RDS database. 

The purpose of RDS proxy is to maintain pool of connections so that any consumer can connect to proxy and can get the database connection. Note that we're NOT creating a connection here – we're just getting connecting which were created already.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/AWS-RDS-Proxy-Logical-1.png)
_Using RDS Proxy with Lambda_

There are 2 advantages of following this approach:

1. **Reduced load on the database server**: As we don't need to create a connection for every lambda invocation in the database server, the load on the server is reduced significantly.
2. **Improved lambda performance**: From lambda, we're just getting a connection from the RDS proxy and we're not creating a new connection. This increases performance of the lambda function.

### Required Changes to Use the RDS Proxy

We don't need to make many changes either to our architecture or to our code. We just need to do a couple of things:

* Create the RDS proxy and associate the db security group that we've created earlier
* Update the environment variable of the lambda endpoint so that lambda can connect to the RDS proxy instead of RDS directly

You don't need to change your lambda code.

### Updated Architecture

Below is the updated architecture diagram

![RDS Proxy with Lambda - Architecture](https://www.freecodecamp.org/news/content/images/2022/11/AWS-Lambda-RDS-Proxy.png)
_RDS Proxy with Lambda - Architecture_

### How to Create the RDS Proxy

We need to create the RDS Proxy and add the database instance as the proxy target.

```typescript
const dbProxy = new rds.DatabaseProxy(this, 'Proxy', {
      proxyTarget: rds.ProxyTarget.fromInstance(dbInstance),
      secrets: [dbInstance.secret!],
      securityGroups: [dbSecurityGroup],
      vpc,
      requireTLS: false,
      vpcSubnets: vpc.selectSubnets({
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      }),
    });
```

Note that we're passing the database secret to this proxy too, as it is responsible for maintaining connections. We're using the same security group of the database as we did to open the port 5432 .

### How to Update the Endpoint for Lambda

We don't need to change the lambda code. We just need to update the endpoint which is passed as the environment variable.

```
 environment: {
        DB_ENDPOINT_ADDRESS: dbProxy.endpoint,
        DB_NAME: databaseName,
        DB_SECRET_ARN: dbInstance.secret?.secretFullArn || '',
      },
```

There will be no change to any other code.

### Performance Improvements

When you test the lambda function, you can see that the lambda is getting connected to the proxy instead of the database instance (as we're printing endpoint information as `host`). 

You should also notice that performance is improved significantly. Before, it took around 500ms to connect. Now, it is taking around 50 ms.

![Performance of lambda with RDS Proxy](https://www.freecodecamp.org/news/content/images/2022/11/image-22.png)
_Performance of lambda with RDS Proxy_

Note that it may take additional time when you're getting the initial connection from RDS proxy. And, getting any further connections will be fast, as shown above.

## Conclusion

I hope this tutorial helped you learn how to connect to RDS from AWS Lambda.

Thanks for reading to this point. I write about [aws lambda](https://www.cloudtechsimplified.com/tag/aws-lambda/), [fargate,](https://www.cloudtechsimplified.com/tag/fargate/)  [ci/cd pipeline](https://www.cloudtechsimplified.com/tag/ci-cd-pipeline/) and serverless technologies at [https://www.cloudtechsimplified.com](https://www.cloudtechsimplified.com). If you're interested, you can subscribe [here](https://www.cloudtechsimplified.com/subscribe/).

