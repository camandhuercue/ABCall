FROM python:3
COPY ./requirements.txt /app/requirements.txt
ENV FLASK_APP=app.py
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
