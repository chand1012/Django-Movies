# DBM Term Project: Movies

## Recommended Readings

* [Django Guide](https://docs.djangoproject.com/en/3.2/)
* [Docker Guide](https://docs.docker.com/get-started/)
* [Docker Compose Guide](https://docs.docker.com/compose/reference/)

## Dev Requirements

* Docker
    - [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
    - [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
    - [Docker for Linux](https://docs.docker.com/engine/install/)
* Just
    - If on Windows, install [Scoop](https://scoop.sh/) or [Chocolatey](https://chocolatey.org/) first.
    - If on Mac, install [Homebrew](https://brew.sh/) first.
    - If on Linux, skip to installation.
    - [Install Here](https://just.systems/man/en/chapter_4.html)

## Getting Started

First, clone the repo. After, open the repo in your preferred text editor and open a terminal window in the directory.

Then you can run the application for the first time.

```sh
$ just get-data
$ just run
$ just migrate
```

This will take about 3 hours to initialize. Please be patient.

Now you're ready to develop!

### Viewing Logs

```sh
$ just logs
```

### Creating an Admin User

**The app must be running before you can run this!!!!**

```sh
$ just createsuperuser
```

### Stopping the Application

```sh
$ just stop
```

### Running manage.py

**The app must be running before you can run this!!!!**

```sh
$ just manage <commands>
```
