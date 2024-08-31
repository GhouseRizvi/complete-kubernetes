# Use NGINX base image with Alpine
FROM nginx:alpine

# Update repository indexes and install dependencies for OpenTracing and Jaeger
RUN apk update && apk add --no-cache \
    git \
    build-base \
    cmake \
    libexecinfo-dev \
    curl-dev

# Install OpenTracing NGINX module and Jaeger tracer
RUN git clone https://github.com/opentracing-contrib/nginx-opentracing.git /tmp/nginx-opentracing && \
    cd /tmp/nginx-opentracing && \
    mkdir .build && cd .build && \
    cmake .. && make && make install

RUN curl -LO https://github.com/jaegertracing/jaeger-client-cpp/releases/download/v0.8.0/libjaegertracing_plugin.so && \
    mv libjaegertracing_plugin.so /usr/local/lib/libjaegertracing_plugin.so

# Remove default NGINX configuration and add custom configuration
RUN rm -rf /usr/share/nginx/html/index.html \
    && rm -rf /etc/nginx/nginx.conf \
    && rm -rf /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/nginx.conf
ADD static /usr/share/nginx/html/

# Set environment variables
ENV CATALOGUE_HOST="catalogue"
