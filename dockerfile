FROM python:3
COPY . .
RUN pip install -U setuptools
RUN pip3 install --upgrade pip
RUN pip3 install pymysql
RUN pip3 install python-dotenv
CMD [ "python", "app.py" ]


