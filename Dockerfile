FROM python:3.12

WORKDIR /Python-Voice-Quickstart

# Copy requirements.txt
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the source code into the container
COPY . .

# Run the application.
ENTRYPOINT [ "python3", "main.py" ]
