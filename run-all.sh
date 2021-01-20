docker network create phonebookdb-network --attachable
docker run -d --rm --name redis-server --network phonebookdb-network -h redis-server redis:5.0.10-alpine
docker run -d --rm --name phonebookdb-service  --network phonebookdb-network -h phonebookdb-service my-phonebook-service:latest
