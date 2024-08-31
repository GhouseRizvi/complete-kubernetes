# Build Stage: Use official Maven image
FROM maven:3.6.3-jdk-8 AS build

# Set the working directory inside the container
WORKDIR /opt/shipping

# Copy the pom.xml and resolve dependencies
COPY pom.xml /opt/shipping/
RUN mvn dependency:go-offline

# Copy the source code and package the application
COPY src /opt/shipping/src/
RUN mvn package

# Run Stage: Use smaller OpenJDK image
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
