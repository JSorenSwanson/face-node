FROM python:alpine3.8
WORKDIR /flasks
ENV FLASK_APP node_api.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . .
RUN pip install -r requirements.txt
CMD ["flask", "run"]