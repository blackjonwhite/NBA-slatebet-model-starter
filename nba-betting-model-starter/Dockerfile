# Minimal dev container
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
ENV PYTHONPATH=/app/src
CMD ["bash", "-lc", "streamlit run src/nba_model/app/app.py --server.port=8501 --server.address=0.0.0.0"]
