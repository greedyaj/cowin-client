FROM python:3.8

WORKDIR /usr/home/app/

COPY . ./

RUN chmod +x -R /usr/home/app/

RUN ./dependency.sh

EXPOSE 5000

ENV FLASK_APP="app"

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
