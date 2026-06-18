FROM python:3.7-slim
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV WERKZEUG_RUN_MAIN=true
CMD ["python", "app.py"]
