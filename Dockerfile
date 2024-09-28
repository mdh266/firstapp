FROM python:3.11-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt main.py /app
RUN pip install -r requirements.txt
RUN mkdir /app/pages
COPY pages/about.py /app/pages/

EXPOSE 8501
# EXPOSE 11434 

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
