FROM python:3.8
COPY main.py /tmp/ 
CMD ["python","/tmp/main.py"]