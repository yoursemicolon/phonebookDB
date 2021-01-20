docker rm -f $(docker ps -q --all --filter label=APP=PHONEBOOK)

