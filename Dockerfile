# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:3.6.2

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary
COPY ./requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary
RUN pip install -r requirements-actions.txt

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001
