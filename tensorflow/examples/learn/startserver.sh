#!/bin/bash

if [ ! -f serving/1/saved_model.pb ]; then
   echo "Place saved_model.pb and variables directory from model in serving/1"
   exit
fi

tensorflow_model_server --model_base_path=`pwd`/serving --port=8500 --rest_api_port=8501
