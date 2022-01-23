FROM fontibus.azurecr.io/aiohttp-setup:latest
COPY backend/lib/yababay/ backend/lib/yababay/
COPY backend/.env backend/
COPY frontend/docs/ frontend/docs/
COPY assets/analitics/*.pkl assets/analitics/
COPY assets/corpus/*.txt assets/corpus/
EXPOSE 80/tcp
WORKDIR /srv/backend
ENTRYPOINT [ "python3", "main.py" ]

