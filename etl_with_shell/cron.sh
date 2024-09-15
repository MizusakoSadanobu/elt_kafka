#!/bin/bash

# Path to the script you want to schedule
SCRIPT_PATH="/c/Users/sadan/OneDrive/Desktop/code/elt_kafka/etl_with_shell/Temperature_ETL.sh"

# Cron schedule: Run every hour at minute 1
CRON_SCHEDULE="1 * * * *"

# Full cron job entry
CRON_JOB="$CRON_SCHEDULE $SCRIPT_PATH"

# Check if the cron job is already present
crontab -l | grep -F "$SCRIPT_PATH" > /dev/null

if [ $? -eq 0 ]; then
    echo "Cron job for $SCRIPT_PATH is already installed."
else
    # Add the new cron job to the crontab
    (crontab -l; echo "$CRON_JOB") | crontab -
    echo "Cron job added: $CRON_JOB"
fi