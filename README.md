# Dashboard

Implementation of a small dashboard showing important information to myself.

## Tech Stack

The data is stored in a Redis instance. A collector is collecting data from
multiple instances and stores it in the Redis instance. On the presentor site
is a Python web service, based on the [Sanic Framework](https://sanicframework.org/en/).
It requests the data from Redis and serves it to an Ember.js based frontend.

Ember visualizes the data dynamically.


