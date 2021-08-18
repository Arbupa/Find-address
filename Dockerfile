# Use python image to execute python code.
FROM python:3.8
# Copy all files to container folder.
COPY . /app 
# Using the working directory.
WORKDIR /app
# Install libraries/frameworks needed. 
RUN pip install -r requirements.txt
# Command to run the Flask app.
CMD python app.py