#!/bin/bash
#Want to bring this repo into the container
#Get location of this script
SCRIPT_LOC=$(readlink -f $0)
SCRIPT_FOLDER=$(dirname $SCRIPT_LOC)
REPO_LOC=$SCRIPT_FOLDER/.. #need to go one path back as this is in the docker folder

echo $REPO_LOC

IMAGE_NAME=jack-scott/personal_covid_map
CONTAINER=personal_covid_map


#build image
$SCRIPT_FOLDER/build_docker.sh

docker run -it \
    --net host \
    --volume $REPO_LOC:/usr/src/app/personal_covid_map:rw \
    --rm \
    --name=$CONTAINER \
    $IMAGE_NAME bash


