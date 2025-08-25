FROM python:3.12-slim

WORKDIR /app
COPY update_readme.py /app/update_readme.py
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
