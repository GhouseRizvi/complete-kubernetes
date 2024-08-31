FROM nginx:alpine

RUN apk add --no-cache \
    git \
    build-base \
    cmake \
    libexecinfo-dev \
    curl-dev

RUN git clone https://github.com/opentracing-contrib/nginx-opentracing.git /tmp/nginx-opentracing && \
    cd /tmp/nginx-opentracing && \
    mkdir .build && cd .build && \
    cmake .. && make && make install
RUN curl -LO https://github.com/jaegertracing/jaeger-client-cpp/releases/download/v0.8.0/libjaegertracing_plugin.so && \
    mv libjaegertracing_plugin.so /usr/local/lib/libjaegertracing_plugin.so

RUN rm -rf /usr/share/nginx/html/*
RUN rm -rf /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/nginx.conf 
ADD static /usr/share/nginx/html/

ENV CATALOGUE_HOST="catalogue"