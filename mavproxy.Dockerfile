FROM ubuntu:18.04 as MAVPROXY-BASE
RUN apt-get update
RUN apt-get install -y python3-dev python3-pip

FROM MAVPROXY-BASE as MAVPROXY
RUN pip3 install PyYAML mavproxy
CMD mavproxy.py --master=tcp:127.0.0.1:5760 --out 127.0.0.1:14550 --out 127.0.0.1:14551
