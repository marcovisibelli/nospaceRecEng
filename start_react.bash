#!/bin/bash
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

today=$(date +%Y-%m-%d)
cd react
npm start
