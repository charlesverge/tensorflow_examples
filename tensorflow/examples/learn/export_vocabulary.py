import os
from tensorflow.contrib import learn

# Load vocabulary
vocab_processor = learn.preprocessing.VocabularyProcessor.restore(os.path.join('savedmodel', 'vocab'))

# Export vocabulary, starting with item 0 which is a place holder for unknown.
with open('vocabulary.csv', 'w') as f:
  for item in vocab_processor.vocabulary_._reverse_mapping:
      f.write("%s\n" % item)
