FROM ubuntu

RUN apt-get update && \
    apt-get install -y build-essential git

RUN git clone https://github.com/openssl/openssl && \
    cd openssl && \
    git checkout OpenSSL_1_0_1f && \
    ./config && \
    make && \
    make install_sw

RUN /openssl/apps/openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=US/ST=NC/L=Chapel Hill/O=Acme/CN=www.example.com"

ENTRYPOINT /openssl/apps/openssl s_server -key key.pem -cert cert.pem -accept 4433 -www