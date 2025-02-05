# text-and-image-classification

The company "place du marché" wants to create a marketplace type e-commerce website. For the moment, the sellers have to choose the category of the product.

To avoid misclassification, the company wants to create a feature to automatically classify the category of a product using the image and the description of the item

## 1. Feature extraction

This part is divided into two notebooks.

The first one is an attempt to classify the items based on the pictures of the product.
SIFT and VGG16 were used to extract the features of the image.

Results were really poor with SIFT, and a bit better by using VGG16

The second part compares different text features extraction techniques:
- Bag of Words
- Text embeddings (Word2Vec, BERT, USE)

The results were much better with the text features, especially when adding the title of the items.

The best scoring algorithm was USE (Universal Sentence Encoder) with an ARI score of 0.63

## 2. Image Classification

In this notebook VGG16 is used again but the Imagenet weights are loaded and the last few layers are retrained to adjust for the 7 categories of product.
The results are much better than the image features non-supervised classification and the ARI score is comparable to some of the text feature extraction models (0.49)

## 3. API requesting script

This script is requesting the edaname API. Place du marché wants to collect data about products containing champagne. The first 10 items are kept for the test.