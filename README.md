# Udacity Cloud Native Foundations Course


## Exercises
#### All the given exercises are added into their specific branches. Switch the branches to see the respective codes for exercises.

---

## Detailed Course Notes
#### Detailed course notes have been added in [Detailed Notes Section](../detailed_notes.md)

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
* As part of the course, few things need to be setup in the machines -
[ I have mac with me and going forward all the commands and installation will be with respect to mac. ]
    * Python - have installed v3.9 (had to upgrade from v2.7 as its the default one shipped with mac)
    * Git - was available with mac
    * Docker - nstalled docker desktop v3.3.3
    * Vagrant - installed using homebrew (useful package manager for mac)
        * If you do not have homebrew, install it from their official site.
        * For installing vagrant, run the command - `brew cask install vagrant` or simply - `brew install vagrant`
    * VirtualBox - installed latest version from official site v6.1

---

### Lesson 2 - Architecture Consideration for Cloud Native Applications

* Two main approaches or architectures to application development are Monoliths and Microservices.
    * Monolithic architecture - entire application behaves as a single unit.
    * Microservice architecture - entire application is split into small units called services that combined together work as one.
* Design considerations -

