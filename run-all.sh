docker network create phonebookdb-network --attachable --label APP=PHONEBOOK
docker run -d --rm --label APP=PHONEBOOK --name redis-server --network phonebookdb-network -h redis-server redis:5.0.10-alpine
docker run -d --rm --label APP=PHONEBOOK --name phonebookdb-service  --network phonebookdb-network -h phonebookdb-service my-phonebook-service:latest
