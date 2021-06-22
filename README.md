# Udacity Cloud Native Foundations Course

## Setup Instructions for MacOS
#### Setup instructions for the entire course on MacOS have been added in [Setup Instructions](../main/setup_instructions.md)

---

## Troubleshooting Guide
#### Troubleshooting guide has the details of issues that I faced during the course and how I resolved them [Troubleshooting Guide](../main/troubleshooting_guide.md)

---

## Exercises
#### All the given exercises are added into their specific branches. Switch the branches to see the respective codes for exercises.

---

## My Summary Notes

### Lesson 1 - Introduction to Cloud Native Fundamentals

* This lesson talks mainly about the definition of Cloud Native terminology. Cloud native in my view is a practice that would enable us to run an application in cloud smoothly.
* Some cloud native related tools used for transforming the application include containers and orchestrators.
* Containers help in running the applications as individual services.
* Container orchestrators are used to manage the containers thereby managing the services running. 
    * They also provide a host of integrations like networking, storage, log systems, etc...
* Microservice application architecture is the most suitable architecture for cloud native applications. Some benefits include - 
    * Improves application scalability.
    * Increases the feature development velocity.
    * Reduces cost to the organization.
    * Faster adaptability to new technologies.
* Most of the open source tools for cloud native technologies come under the umbrella of CNCF.
* To go with cloud native adoption, teams need to consider business perspective and technical perspective.
    * Business perspective includes application flexibility for transformation, faster development cycles and reduced application downtimes.
    * Technical perspective includes automated integration and deployment of services, management of services with less effort and individual application maintenance and debugging.
* As part of the course, few things need to be setup in the machines and the instructions for those are provided in the 
[Setup Instructions](../main/setup_instructions.md)

##### Detailed Notes:

* Cloud native - refers to practices using which the applications run in cloud environment.
* Benefits of cloud native -
    * Faster and easier application scaling.
    * Higher feature velocity.
    * Innovating with technology ecosystem.
* Types of cloud environments -
    * Private cloud
    * Public cloud
    * Hybrid cloud
* Containers - are small units of application.
* Benefits of containers -
    * Follows single application principle.
    * Easy to manage.
    * Easy to deploy.
    * Faster recovery from downtime.
* Microservices - are collection of small and independent services or applications.
* Types of container managers or orchestrators -
    * Kubernetes
    * Docker swarm
    * Apache mesos
* Kubernetes - is a container orchestrator that automates:
    * Configuration
    * Management
    * Scalability
* Kubernetes also integrates with -
    * Runtime
    * Networking
    * Storage
    * Service mesh
    * Logs and metrics
    * Tracing
* CNCF - Cloud native computing foundation is a home to open source projects that provide tools for running an application cloud environment.
* Cloud native adoption requires two things -
    * Business perspective -
        * Agility
        * Growth
        * Service availability
    * Technical perspective -
        * Automation
        * Orchestration
        * Observability

---

### Lesson 2 - Architecture Consideration for Cloud Native Applications

* Application architecture consists of 3 tires - MVC (Model-View-Controller).
* Two main approaches or architectures to application development are Monoliths and Microservices.
    * Monolithic architecture - entire application behaves as a single unit.
    * Microservice architecture - entire application is split into small units called services that combined together work as one.
* Design considerations for cloud native applications using context discovery -
    * List functional requirements or services involved, something like -
        * Stakeholders who would sponsor the project
        * Application features to be implemented
        * End user who would use the application
        * Inputs needed from the end users or the outputs that application will generate for the end users
        * Which engineering team would be capable of handling the project
    * List all resources available for the project, something like -
        * Available engineering resources
        * Financial resources for the application
        * Timeline to finish the project
        * Knowledge of engineering teams to use the technologies
* Both monolithic and microservices architectures have various benefits over each other. In terms of trade offs, few things to consider are -
    * Complexity of developing and maintaining the application
    * Flexibility to upgrade and use new technologies in the course of time
    * Cost arising out of operating the application
    * Application scalability (up and down) based on the traffic or system load
    * Better application reliability and availability
* Few best practices to consider for application deployment -
    * Use health checks
    * Implement logging tools help analyse application operation and draw insights
    * Use metrics to understand the load and usage of the infrastructure including resource consumption
    * Use log tracing to identify issues in the application code
* Application maintenance phase has following operations involved -
    * Split operation - when a service handles too many responsibilities
    * Merge operation - when multiple services handle one responsibility
    * Replace operation - when service has to be replaced with a newer version of the service
    * Stale operation - sunset the service when its no longer used

---

### Lesson 3 - Container Orchestration with Kubernetes

* Containers over VMs (Virtual Machines) -
    * Containers use less resources than VMs as the operating system that VM needs is eliminated
    * Containers are faster than VMs and so application uptime is reduced for containers
    * Reduced cost of maintenance for containers
* VMs provide better isolation environment for applications than containers and so are more secure than containers
* Containerization using Docker -
    * Application packaging creates a container
    * Docker tool is used to manage the containers
* Docker consists of 3 main components -
    * Docker file - set of instructions to create a docker image
    * Docker image - read only template that is used to run the application in a container
    * Docker registry - central place where all the images are stored and distributed
* Useful docker commands used to perform various operations -
    * docker build - builds an image
    * docker tag - tags an image with a version
    * docker push - pushes the image to the docker registry, in our case dockerhub
    * docker run - run the docker image locally and create a container
    * docker exec - login to running docker container
    * docker logs - print the logs of the running docker container
* Docker or containerization process: Create docker file -> Build docker file to create docker image -> 
Run the docker image to verify everything's working as expected -> Tag the docker image -> Push the docker image to registry
* Container orchestrators are very much needed as the number of containers that need management go out of control when the application needs scaling up.
* Kubernetes has laid the path for the container orchestration. It is widely used because of -
    * Portability
        * Open source technology under CNCF
        * Platform agnostic and has the support of almost all the cloud providers
    * Resiliency
        * Makes sure the required number of services are maintained 
        * Self healing ability using replicasets and various probes
    * Scalability
        * Uses HPA (horizontal pod autoscaler) to assign the resources for each container and manage the containers
        * Elasticity is the core feature which supports scaling up and down of the containers on demand
    * Service discovery
        * Provides cluster level DNS system
        * Distributes the traffic as necessary
    * Extensibility
        * Uses building blocks principle to build on top of base block
        * Uses CRD (custom resource definition) to add new resource to the cluster
    * Operational cost
        * Powerful scheduler to allocate the resources to the clusters
        * Cluster autoscaler - Automates the size of the cluster based on traffic to the application which can be specified in the configuration
* Kubernetes -
    * Has Clusters - pool of nodes
    * Has Nodes - 
        * Control plane - collection of master nodes
            * Takes global decisions about the cluster like api server, scheduler, control manager, etcd.
        * Data plane - collection of worked nodes
            * Used to host application nodes and components like kubelet and kube-proxy
    * Kubelet and kube-proxy runs on all nodes including master and worked nodes
    * Bootstrapping of a cluster (makes sure control and data planes are up and running) can be done with tools like Kubeadm, k3s, kops, kubespray in production. For development purpose kind and minikube tools can be used.
    * k3s is lightweight with single binary installation and can operate with just one node
    * kubectl is the command line utility tool for kubernetes
    * kubeconfig is the configuration file added in a cluster to manage the cluster configuration
        * It has the information about clusters, context and users
    * Various kubectl commands can be used to get all the necessary information about clusters or nodes and even modify the configuration of the clusters and nodes
    * Kubernetes resources consists of pods, namespaces, configuration maps and secrets, deployment and replicasets, services and ingress, CRD etc...
    * Pods -
        * Pod is a smallest deployable unit where the docker container application runs
        * A node can have multiple pods and a cluster can have multiple nodes
        * ReplicaSets are used to maintain the number of pods that should be up and running
        * Headless pods can be created using `kubectl run` command
    



