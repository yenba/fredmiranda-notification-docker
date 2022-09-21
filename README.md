# Fred Miranda Buy/Sell Post Notifier

This is a python script that has been containerized into a Docker container to receive triggers from a Postgres Database on new content. It will then send a push notification to Pushover to alert you of any new items.

## Prerequisites

- You need to have already run the Docker container on [this Github page](https://github.com/yenba/fredmiranda-post-upload-docker) that populates your database with the Fred Miranda posts.
- **Postgres Database**
    - Postgres Database Name (`DBNAME`)
    - Postgres Database Username (`DBUSER`)
    - Postgres Database Password (`DBPASS`)
    - Postgres Database Hostname (`DBHOST`)
- **Pushover Account**
    - Notifications are achieved by utilizing [Pushover](https://pushover.net/). You will need to create a Pushover account to properly run this script.
- **Pushover API User Key (`USERKEY`)**
    - Documentation is here - [https://pushover.net/api](https://pushover.net/api)
- **Pushover API Token (`APIKEY`)**
    - Documentation is here - [https://pushover.net/api](https://pushover.net/api)
- **Docker**

## Docker Hub Repo

[https://hub.docker.com/repository/docker/yenba/fredmiranda-notification-docker](https://hub.docker.com/repository/docker/yenba/fredmiranda-notification-docker)

# ****Docker Run Command****

Run your docker command like this:

`docker run -it --rm --env "APIKEY=YOUR_PUSHOVER_API_KEY_HERE" --env "USERKEY=YOUR_PUSHOVER_USER_KEY_HERE" --env "DBNAME=YOUR_DB_NAME_HERE" --env "DBUSER=YOUR_DB_USERNAME_HERE" --env "DBPASS=YOUR_DB_PASSWORD_HERE" --env "DBHOST=YOUR_DB_HOSTNAME_OR_IP_HERE" yenba/fredmiranda-notification-docker`
