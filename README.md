# Tensorflow saved model example

This is an example of creating a saved_model.pb for use in  tensorflow server. It is indented for people with experience with python and new to Tensorflow.

## Files
text_classification_cnn.py - An example of using a Tensorflow estimator and saved_model to create a saved_model.pb for use with Tensorflow server.
predict.py - Run predictions on a Tensorflow server with a rest api request
predict.sh - Run predictions with a curl request
startupserver.sh - Start tensorflow server
export_vocabulary.py - Export vocabulary to csv file

### Requirements
* python 3
* Tensorflow
* Tensorflow server https://www.tensorflow.org/serving/setup
* curl for testing

### Setup
* clone the repo git clone https://github.com/charlesverge/tensorflow_examples.git
* cd tensorflow/examples/learn
* Execute pip install -r requirements.txt
* Execute the training model python3 text_classification_cnn.py
* Move the saved pb model to serving/1 mv saved_model_pb/* serving/1
* Start the tensor server
* tensorflow_model_server --model_base_path=`pwd`/serving --port=8500 --rest_api_port=8501
* Test prediction with a curl command ```
curl -d '{"inputs":{"words":[[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0],[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]]}}' \
   -X POST http://localhost:8501/v1/models/default/versions/1:predict ```

The result should be a json object with the class for each item and the probabilities for each class

```javascript
{
    "outputs": {
        "class": [
            12,
            12
        ],
        "prob": [
            [
                0.0,
                5.55529e-07,
                1.48694e-20,
                7.7422e-17,
                0.0,
                1.34299e-15,
                2.09542e-35,
                4.36592e-19,
                3.26157e-36,
                0.0,
                4.50993e-25,
                1.01477e-25,
                0.999999,
                1.45415e-13,
                4.56743e-14
            ],
            [
                0.0,
                5.55529e-07,
                1.48693e-20,
                7.74226e-17,
                0.0,
                1.34297e-15,
                2.09542e-35,
                4.3659e-19,
                3.2615e-36,
                0.0,
                4.50986e-25,
                1.01477e-25,
                0.999999,
                1.45413e-13,
                4.56736e-14
            ]
        ]
    }
}
```

### Encoding text for predictions

The model generated accepts an array of batches to run predictions for. A batch is an array of words converted to their integer index in the vocabulary. predict.py uses the Tensorflow library to load the vocabulary to transform the text. export_vocabulary.py can be used to convert the vocab file to a csv file for use in another language or database format.

### Notes
* The examples are based on Tensorflow's examples which have not been updated to the latest tf.data API.
* Several of the API's in Tensorflow are depreciated in v1.11 in the future will stop working. The primary goal is to give an example of a working saved model for the tensor server.

The original model is from the Tensorflow examples, (v1.11.0) https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/learn
