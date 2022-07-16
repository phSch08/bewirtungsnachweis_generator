# bewirtungsnachweis_generator

## Deploy
Build the docker image
```
docker image build -t bngen .
```

Run the container
```
docker run -p 127.0.0.1:5000:5000 --restart unless-stopped bngen
```