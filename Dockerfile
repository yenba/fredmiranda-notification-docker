FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD fredNotificationChecker.py /
ADD pushoverSend.py /
ENTRYPOINT [ "python", "fredNotificationChecker.py" ]