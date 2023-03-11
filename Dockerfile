FROM python:3.9.7-slim
EXPOSE 80
WORKDIR /usr/src/app 
COPY requirements.txt ./ 
RUN pip install -r requirements.txt 
ENV PATH="$PATH:/usr/bin/python"
COPY . . 
CMD [ "python", "./app.py" ] 
