# Build Stage
FROM debian:10 AS build

# Install Maven and Java
RUN apt-get update && apt-get -y install maven && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /opt/shipping

# Copy the pom.xml and resolve dependencies (faster builds with cached dependencies)
COPY pom.xml /opt/shipping/
RUN mvn dependency:go-offline

# Copy the source code and package the application
COPY src /opt/shipping/src/
RUN mvn package

# Run Stage
FROM openjdk:8-jdk

# Expose port 8080 for the application
EXPOSE 8080

# Set the working directory inside the container
WORKDIR /opt/shipping

# Environment variables
ENV CART_ENDPOINT=cart:8080 \
    DB_HOST=mysql

# Copy the packaged JAR from the build stage
COPY --from=build /opt/shipping/target/shipping-1.0.jar shipping.jar

# Command to run the application
CMD [ "java", "-Xmn256m", "-Xmx768m", "-jar", "shipping.jar" ]
