import os
import requests
import tensorflow as tf
from tensorflow.contrib import learn
import json
import numpy as np

TENSOR_SERVER_API = "http://localhost:8501/v1/models/default/versions/1:predict"

# Load vocabulary
vocab_processor = learn.preprocessing.VocabularyProcessor.restore(os.path.join('savedmodel', 'vocab'))

# Test data
predict_text = [
    'a newspaper published in Albania',
    'The cat and the dog',
    'The place is Punjab',
]

# Numpy arrays are not serializable, tolist converts arrays including sub arrays.
predict = np.array(list(vocab_processor.transform(predict_text))).tolist()
data= {
    'inputs': {
        'words': predict,
    }
}

# Convert to json.
data = json.dumps(data)
r = requests.post(TENSOR_SERVER_API, data=data)

print("JSON Result:\n{}\n".format(r.text))
result = json.loads(r.text)

for i in range(len(result["outputs"]["class"])):
   print("Class: {}\nText: {}\n".format(result["outputs"]["class"][i], predict_text[i]))
