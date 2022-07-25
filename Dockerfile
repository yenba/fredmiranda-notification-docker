FROM python:3
#Setup the variables
ENV APIKEY="APIKEYHERE"
ENV USERKEY="USERKEYHERE"
ENV DBNAME="DBNAMEHERE"
ENV DBUSER="DBUSERHERE"
ENV DBPASS="DBPASSHERE"
ENV DBHOST="DBHOSTHERE"
#Install git
RUN mkdir /home/github && cd /home/github && git clone https://github.com/yenba/fredmiranda-notification-docker.git
#Set working directory
WORKDIR /home/github/fredmiranda-notification-docker
RUN pip install -r requirements.txt
CMD python fredNotificationChecker.py --apikey ${APIKEY} --userkey ${USERKEY} --dbname $DBNAME --dbuser $DBUSER --dbpass $DBPASS --dbhost $DBHOST