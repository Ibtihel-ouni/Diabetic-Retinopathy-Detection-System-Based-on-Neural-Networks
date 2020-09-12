# Diabetic-Retinopathy-Detection-System-Based-on-Neural-Networks

>Diabetic Retinopathy (DR) is an ophthalmic disease that damages retinal blood vessels. DR causes impaired vision and may even lead to blindness but proper treatment and early diagnosis can prevent its progression.\
It  has five stages or classes, namely normal, mild, moderate, severe and PDR (Proliferative Diabetic Retinopathy ) .


![hayh](https://user-images.githubusercontent.com/58151963/93005351-22e36600-f548-11ea-8a48-61831087f72e.PNG)

we present a new feature of  extraction method 
using Neural Networks for the diagnosis of DR disease : 

## **[The Dataset : ](https://www.kaggle.com/c/aptos2019-blindness-detection/data?fbclid=IwAR1FBNTkaBpfpSE9iP8YNaALeMdzZXgjqgHS7Cy-vh5mNGS7tK13PhOO5A4)**
* To organize the images : `Image_Organizer.py` 

### **Training :**

![haha](https://user-images.githubusercontent.com/58151963/92936532-1aa10300-f442-11ea-918c-927d97a9f492.PNG)

### **The Model :**
* Pre-trained with : 
    *   Xception : `Model_Xception.ipynb`
    *   Inception : `inception_prune.py `
* From scratch :  `Model_Scratch.ipynb`

### **Regularization techniques :** 
* Data augmentation
* Dropout
* weight regularization
* Early stopping
* Drop Learning Rate on Plateau


### **Optimization techniques :**

*   ###  Pruning
    *   Prune_low_magnitude 
    *   [Keras Surgeon](https://medium.com/@anuj_shah/model-pruning-in-keras-with-keras-surgeon-e8e6ff439c07) : `Keras_Surgeon.ipynb`
    
    
*   ### Quantization
