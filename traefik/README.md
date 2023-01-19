# Manual
- Docker Command
    - docker run --network host --name traefik -v /var/run/docker.sock:/var/run/docker.sock -v $PWD/traefik.yml:/etc/traefik/traefik.yml -v $PWD/route.yml:/etc/traefik/route.yml -d -it --rm -p 80:80 -p 443:443 -p 8080:8080 traefik:latest

# Note
- API Gateway (Reverse Proxy)
    - Nginx, HAProxy, Kong, Traefik...
- Traefik Authorization Logic
    - [BasicAuth](https://doc.traefik.io/traefik/middlewares/http/basicauth/)
        - **users** option
            - <span style='background-color: #f6f8fa'>name:hashed-password</span> format
        - **usersFile** option
            - file content is a list of <span style='background-color: #f6f8fa'>name:hashed-password</span>
        - ...
    - [ForwardAuth](https://doc.traefik.io/traefik/middlewares/http/forwardauth/)
        - Using an external service to forward authentication
            - If the service answes with a 2XX code, access is granted, and the original request is performed
            - Otherwise, the response from the authentication server is returned
        - **forwardAuth** option
            - <span style='background-color: #f6f8fa'>X-Forwarded-</span> headers
            - **address** option
            - ...