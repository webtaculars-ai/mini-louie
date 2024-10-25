FROM continuumio/miniconda3:latest

WORKDIR /app

# Install the conda environment
COPY environment.yml /app/environment.yml
RUN conda env create -f environment.yml
SHELL ["conda", "run", "--no-capture-output", "-n", "louie", "/bin/bash", "-c"]

# Copy the server code
COPY server /app/server

# Expose the port
EXPOSE 8888

# Start the FastAPI server
CMD ["conda", "run", "--no-capture-output", "-n", "louie", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8888"]