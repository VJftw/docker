#!/usr/bin/with-contenv sh

echo "Running initial sync from ${SOURCE} to ${DESTINATION}"
aws s3 sync ${SOURCE} ${DESTINATION}

echo "${SCHEDULE} aws s3 sync ${DESTINATION} ${SOURCE}" > /etc/crontabs/root
echo "Added cron for syncing ${DESTINATION} to ${SOURCE} every ${SCHEDULE}"

crond -f
