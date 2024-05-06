from opensuse/tumbleweed
RUN zypper -n update
RUN zypper -n install python3 python3-pip scapy
RUN useradd app
RUN mkdir /app
RUN chown app: /app
USER app
WORKDIR /app