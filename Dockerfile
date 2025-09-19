#BASE IMAGE
FROM python:3.13-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#DJANGO
FROM base AS django 
COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cotizacion.wsgi:application"]

#CRON 
FROM base AS cron
RUN apt-get update && \
    apt-get install -y cron wget gnupg2 \
        libnss3 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdrm2 \
        libxcomposite1 \
        libxdamage1 \
        libxrandr2 \
        libgbm1 \
        libasound2 \
        libxshmfence1 \
        libx11-6 \
        libxext6 \
        libxfixes3 \
        libxkbcommon0 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*
RUN pip install playwright && playwright install chromium
COPY . .
COPY crontab /etc/cron.d/cotizaciones-cron
RUN chmod 0644 /etc/cron.d/cotizaciones-cron && \
    crontab /etc/cron.d/cotizaciones-cron
RUN mkdir -p /var/log/cron
CMD ["cron", "-f"]
