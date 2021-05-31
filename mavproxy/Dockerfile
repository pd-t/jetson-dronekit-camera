FROM ubuntu:18.04 as MAVPROXY-BASE
RUN apt-get update
RUN apt-get install -y python3-dev python3-pip

FROM MAVPROXY-BASE as MAVPROXY
RUN pip3 install PyYAML mavproxy
WORKDIR /mavproxy
COPY mavproxy.sh .
RUN chmod +x mavproxy.sh
ENTRYPOINT ["./mavproxy.sh"]

