FROM python:3.11
EXPOSE 5000
# This is the docker image file we are creating and we are putting app.py (application/API) into it
WORKDIR /develop_store
# Putting this image into some folder (in this case the app folder itself)
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# COPY Source destination, source & destination are same in this case
CMD ["flask", "run", "--host", "0.0.0.0"]