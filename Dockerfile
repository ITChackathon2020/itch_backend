FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Maintainer info
LABEL maintainer="mikelevenson88@gmail.com"

# Make working directories
COPY . /app


# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip

# Copy application requirements file to the created working directory
# COPY requirements.txt .

# Install application dependencies from the requirements file
RUN pip install -r requirements.txt



# Run the python application
CMD ["sh", "run_deploy.sh"]