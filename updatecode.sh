#!/bin/bash

DEPLOYDIR=/root/p2p
ENVIRONMENT=/root
echo "[log] - Starting code update "
cd "$DEPLOYDIR"; GIT_WORK_TREE="$DEPLOYDIR" git pull;
echo "[log] - Finished code update "

echo "[log] - Activating virtualEnv"
cd "$ENVIRONMENT"; source ../.env/bin/activate; cd -
echo "[log] - Finished activating virtualenv"

echo "[log] - Pulling down pip dependencies"
cd "$ENVIRONMENT"; pip install -r requirements.txt; cd -
echo "[log] - Finished pulling down pip dependencies"

echo "[log] - Staring DB migration"
cd "$DEPLOYDIR"; python manage.py migrate; cd -
echo "[log] - Finished DB migration "

echo "[log] - Collecting static assets"
cd "$DEPLOYDIR"; python manage.py collectstatic; cd -
echo "[log] - Finished collecting static assets"

echo "[log] - Restarting App"
sudo systemctl restart gunicorn; sudo service nginx restart; cd -
echo "[log] - Finished collecting static assets"






