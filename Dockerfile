FROM python:3
#Install git
RUN mkdir /home/github && cd /home/github && git clone https://github.com/yenba/fredmiranda-notification-docker.git
#Set working directory
WORKDIR /home/github/fredmiranda-notification-docker
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "fredNotificationChecker.py" ]