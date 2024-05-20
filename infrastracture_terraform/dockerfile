FROM jenkins/inbound-agent:3174.v2c9e67f8f9df-1-alpine

USER root

# Fix potential curl issues and install wget if not already available
RUN apk update && \
    apk add --no-cache curl libc6-compat libcurl wget unzip git openssh-client bash && \
    apk upgrade

# Debugging: Check Git version
RUN git --version

# Install AWS CLI v2 using wget
RUN wget "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -O "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Install kubectl using wget
RUN wget -O kubectl "https://dl.k8s.io/release/$(wget -O - -o /dev/null https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm -f kubectl

# Install Terraform (if required)
RUN apk add --no-cache terraform

RUN mkdir -p /home/jenkins/agent1 && \
    chown jenkins:jenkins /home/jenkins/agent1 && \
    chmod 755 /home/jenkins/agent1
USER jenkins


# ... the previous part of the Dockerfile ...

# Ensure that entrypoint.sh is present in the Docker build context
COPY --chmod=755 entrypoint.sh /entrypoint.sh

# Give execute permission to the entrypoint script
# This is the command that's failing for you

# Use the entrypoint script to start the container
ENTRYPOINT ["/entrypoint.sh"]
