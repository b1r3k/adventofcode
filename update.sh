#!/bin/bash
set -e

YEAR=$(date +%Y)

for DAY in {1..25}
do
    PUZZLE=`docker run -it trafilatura -u "https://adventofcode.com/${YEAR}/day/${DAY}"`
    if [ -z "$PUZZLE" ]
    then
        echo "Day ${DAY} not available yet"
        break
    fi
    # puzzle title is on the first line which looks like this --- Day 1: Calorie Counting ---
    TITLE=`echo "$PUZZLE" | head -n 1 | grep -oP "Day \d+: \K.*" | tr -d "-"`
#    strip whitespaces from title endingk
    TITLE=`echo $TITLE | sed 's/[[:space:]]*$//'`
    echo "Title: ${TITLE}"
    PUZZLE_DIR_NAME=`echo $TITLE | tr -d "[:punct:]" | tr "[:upper:]" "[:lower:]"`
#    replace whitespaces with underscores
    PUZZLE_DIR_NAME=`echo $PUZZLE_DIR_NAME | tr " " "_"`
    # pad day number with 3 leading zeros
    DAY_NO_PREFIX=`printf "%03d" $DAY`
    PUZZLE_DIR_NAME="${DAY_NO_PREFIX}_${PUZZLE_DIR_NAME}"
    mkdir -p ${YEAR}/${PUZZLE_DIR_NAME}
    if [ ! -f ${YEAR}/${PUZZLE_DIR_NAME}/puzzle.md ]
    then
        echo -e "\tSaving puzzle for day ${DAY}"
        echo ${PUZZLE} > ${YEAR}/${PUZZLE_DIR_NAME}/puzzle.md
    fi
    for FILE in templates/*
    do
        FILENAME=`basename $FILE | cut -d. -f1`
        EXTENSION=`basename $FILE | cut -d. -f2`
        if [ ! -f ${YEAR}/${PUZZLE_DIR_NAME}/${FILENAME}_1.${EXTENSION} ]
        then
            echo -e "\tCreating ${FILENAME}_1.${EXTENSION}"
            cp $FILE ${YEAR}/${PUZZLE_DIR_NAME}/${FILENAME}_1.${EXTENSION}
        fi
        if [ ! -f ${YEAR}/${PUZZLE_DIR_NAME}/${FILENAME}_2.${EXTENSION} ]
        then
            echo "\tCreating ${FILENAME}_2.${EXTENSION}"
            cp $FILE ${YEAR}/${PUZZLE_DIR_NAME}/${FILENAME}_2.${EXTENSION}
        fi
    done
    if [ ! -f ${YEAR}/${PUZZLE_DIR_NAME}/input.txt ]
    then
        echo "\tCreating input for day ${DAY}"
        touch ${YEAR}/${PUZZLE_DIR_NAME}/input.txt
    fi
    if [ ! -f ${YEAR}/${PUZZLE_DIR_NAME}/test_input.txt ]
    then
        echo "\tCreating test input for day ${DAY}"
        touch ${YEAR}/${PUZZLE_DIR_NAME}/test_input.txt
    fi
done
