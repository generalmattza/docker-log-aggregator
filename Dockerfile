FROM python:3

WORKDIR /app

COPY . .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir .


CMD [ "python", "./main.py" ]