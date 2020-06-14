
<p align="center">
<img src="https://i.imgur.com/mO5PdcB.png" height="200" alt="twinlink">
</p>
<p align="center">
    <a href="https://cloud.ibm.com">
    <img src="https://img.shields.io/badge/IBM%20Cloud-powered-blue.svg" alt="IBM Cloud">
    </a>
    <img src="https://img.shields.io/badge/platform-python-lightgrey.svg?style=flat" alt="platform">
    <img src="https://img.shields.io/badge/license-Apache2-blue.svg?style=flat" alt="Apache 2">
</p>

# Introduction

Twinlink View is a Python Flask microservice hosted on IBM Cloudfoundry. It is part of the Twinlink Platform which serves to link digitally twinned cities to emergency responders such as SCDF.

It retrieves processed data from IBM watson and presents it to building management for analytics and monitoring in normal operations. In the event of an emergency detected by any of the sensors, a digital pipeline is automatically unlocked for SCDF operations management platforms to access. It can also be manually unlocked by a building management if the sensors failed to detect emergencies.

The digital pipeline provides the following information:
- An API that allows SCDF operations management software to access Watson processed data such as number of people in specific locations, exact location of emergencies
- Geometry of the building, overlayed with Watson processed data to allow for rapid sense-making

# Features
## Digital Twin for Emergency Responders
[Twinlink view](http://pythonflaskpascal.us-south.cf.appdomain.cloud/twinbuilding) also allows for an interative access of the digital twin of the building here. This uses a WebGL-based 3D Visualization engine that retrieves stored geometries of the building from the cloud, and overlays critical information necessary for the emergency responders. In this example, a fire is detected at one corner of the office, and the presented data would be the spread of the fire, as well as the number of people trapped in the room. As it is a web-based platform, there is no need for specialized equipment/ application downloads, it is fully functioning on smartphones too.

## API for Emergency Services
[Twinlink access](http://pythonflaskpascal.us-south.cf.appdomain.cloud/api/v1/resources/locs/all) allows for API access into its database through URLs. Emergency services can set up their operations management platform to retrieve data from these API. With this data, they are able to use their own tools such as [Dynamic Resource Optimisation](https://sis.smu.edu.sg/news/2018/dec/17/scdf-rides-data-get-ambulances-patients-more-quickly) to optimise their response strategy.

## API for Cloud Services
[Twinlink write](http://pythonflaskpascal.us-south.cf.appdomain.cloud/write/1/15) is designed to allow cloud services such as Watson to write data into its database. A url-based sample is shown in this case, that will allow any cloud service to enter the number of people (noPax=15) at a location (id=1), the time of update is automatically generated.
Due to technical limitations, the machine learning model is currently ran locally and there will be no live data stream, as such, a snapshot of the locally generated data will be used to showcase in this demonstration.

# Live Demo
[Live demo hosted on IBM Cloudfoundry](http://pythonflaskpascal.us-south.cf.appdomain.cloud/)


# Technical Explanation
## Digital Twin for Emergency Responders

## Steps

You can [deploy this application to IBM Cloud](https://cloud.ibm.com/developer/appservice/starter-kits/python-flask-app) or [build it locally](#building-locally) by cloning this repo first. After your app is live, you can access the `/health` endpoint to build out your cloud native application.

### Deploying to IBM Cloud

<p align="center">
    <a href="https://cloud.ibm.com/developer/appservice/starter-kits/python-flask-app">
    <img src="https://cloud.ibm.com/devops/setup/deploy/button_x2.png" alt="Deploy to IBM Cloud">
    </a>
</p>

Click **Deploy to IBM Cloud** to deploy this same application to IBM Cloud. This option creates a deployment pipeline, complete with a hosted GitLab project and a DevOps toolchain. You can deploy your app to Cloud Foundry, a Kubernetes cluster, or a Red Hat OpenShift cluster. OpenShift is available only through a standard cluster, which requires you to have a billable account.

[IBM Cloud DevOps](https://www.ibm.com/cloud/devops) services provides toolchains as a set of tool integrations that support development, deployment, and operations tasks inside IBM Cloud.

### Building locally

To get started building this application locally, you can either run the application natively or use the [IBM Cloud Developer Tools](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) for containerization and easy deployment to IBM Cloud.

#### Native application development

* Install [Python](https://www.python.org/downloads/)
 
Running Flask applications has been simplified with a `manage.py` file to avoid dealing with configuring environment variables to run your app. From your project root, you can download the project dependencies with (NOTE: If you don't have pipenv installed, execute: `pip install pipenv`):

```bash
pipenv install
```

To run your application locally:

```bash
python manage.py start
```

`manage.py` offers a variety of different run commands to match the proper situation:
* `start`: starts a server in a production setting using `gunicorn`.
* `run`: starts a native Flask development server. This includes backend reloading upon file saves and the Werkzeug stack-trace debugger for diagnosing runtime failures in-browser.
* `livereload`: starts a development server via the `livereload` package. This includes backend reloading as well as dynamic frontend browser reloading. The Werkzeug stack-trace debugger will be disabled, so this is only recommended when working on frontend development.
* `debug`: starts a native Flask development server, but with the native reloader/tracer disabled. This leaves the debug port exposed to be attached to an IDE (such as PyCharm's `Attach to Local Process`).

There are also a few utility commands:
* `build`: compiles `.py` files within the project directory into `.pyc` files
* `test`: runs all unit tests inside of the project's `test` directory

Your application is running at: `http://localhost:3000/` in your browser.
- Your [Swagger UI](http://swagger.io/swagger-ui/) is running on: `/explorer`
- Your Swagger definition is running on: `/swagger/api`
- Health endpoint: `/health`

There are two different options for debugging a Flask project:
1. Run `python manage.py runserver` to start a native Flask development server. This comes with the Werkzeug stack-trace debugger, which will present runtime failure stack-traces in-browser with the ability to inspect objects at any point in the trace. For more information, see [Werkzeug documentation](http://werkzeug.pocoo.org/).
2. Run `python manage.py debug` to run a Flask development server with debug exposed, but the native debugger/reloader turned off. This grants access for an IDE to attach itself to the process (i.e. in PyCharm, use `Run` -> `Attach to Local Process`).

You can also verify the state of your locally running application using the Selenium UI test script included in the `scripts` directory.

> **Note for Windows users:** `gunicorn` is not supported on Windows. You may start the server with `python manage.py run` on your local machine or build and start the Dockerfile.

#### IBM Cloud Developer Tools

Install [IBM Cloud Developer Tools](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) on your machine by running the following command:
```
curl -sL https://ibm.biz/idt-installer | bash
```

Create an application on IBM Cloud by running:

```bash
ibmcloud dev create
```

This will create and download a starter application with the necessary files needed for local development and deployment.

Your application will be compiled with Docker containers. To compile and run your app, run:

```bash
ibmcloud dev build
ibmcloud dev run
```

This will launch your application locally. When you are ready to deploy to IBM Cloud on Cloud Foundry or Kubernetes, run one of the commands:

```bash
ibmcloud dev deploy -t buildpack // to Cloud Foundry
ibmcloud dev deploy -t container // to K8s cluster
```

You can build and debug your app locally with:

```bash
ibmcloud dev build --debug
ibmcloud dev debug
```

## Next steps
* Learn more about the services and capabilities of [IBM Cloud](https://cloud.ibm.com).
* Explore other [sample applications](https://cloud.ibm.com/developer/appservice/starter-kits) on IBM Cloud.

## License

This sample application is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)

