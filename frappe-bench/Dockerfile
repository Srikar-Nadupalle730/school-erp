FROM frappe/bench:latest

USER root

RUN apt-get update && apt-get install -y \
    mariadb-client \
    curl

USER frappe

WORKDIR /home/frappe

CMD ["bash"]
