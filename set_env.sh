#!/bin/bash

ENV_FILE=".env"

HOST_UID=`id -u`
HOST_GID=`id -g`
touch $ENV_FILE
echo "UID=$HOST_UID" > $ENV_FILE 
echo "GID=$HOST_GID" >> $ENV_FILE 