# Autoheal with docker container healthcheck

Your healthcheck, your rules!

This is an example code of how Autoheal tool can be used to recover your container when they stop working. This is particularly useful not only when the container goes down, but when the container is still running (healthy) but somehow your app stops running. By defining the correct healthcheck per container, autoheal can restart your container.

Please visit the following repo for more info:

https://github.com/willfarrell/docker-autoheal

## Execution

Just run the command, and only until the autoheal container does its magic.

```
make up
```

With the current settings, it might take up to 1 minute to see any container restart.