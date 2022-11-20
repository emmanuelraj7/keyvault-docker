FROM python:3.6
LABEL maintainer="topintegrations.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ARG SECRET
ENV SA_PASSWORD $SECRET

EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
