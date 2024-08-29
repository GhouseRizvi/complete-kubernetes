# Define a build argument 'VERSION' with a default value of 8 if not provided
ARG VERSION
# Use the specified or default version of AlmaLinux
FROM almalinux:${VERSION:-8}

# Define a build argument 'GREETING' with a default value of "Good Morning"
ARG GREETING="Good Morning"
# Set an environment variable 'GREET' with the value of 'GREETING'
ENV GREET=${GREETING}

# Echo the value of the 'GREETING' argument to the build logs
RUN echo "${GREETING}"
