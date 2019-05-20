FROM python
EXPOSE 3000
RUN pip install beautifulsoup4 requests
WORKDIR /app
COPY app.py /app
