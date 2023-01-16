# Manual
1. Docker Command
    - docker run --network host --name traefik -v /var/run/docker.sock:/var/run/docker.sock -v $PWD/traefik.yml:/etc/traefik/traefik.yml -v $PWD/route.yml:/etc/traefik/route.yml -d -it --rm -p 80:80 -p 443:443 -p 8080:8080 traefik:latest