import matplotlib
import tensorflow as tf
import matplotlib.pyplot as plt

fashion = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion.load_data()

class_names = ['T-shirt/top', 'Trouser' , 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(train_images.shape)
print(train_labels)
print(test_images.shape)
print(test_labels.shape)

# plt.figure()
# plt.imshow(train_images[0] , cmap='gray')
# plt.colorbar()
# plt.grid(False)
# plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap='gray')
    plt.xlabel(class_names[train_labels[i]])
    # plt.title(class_names[train_labels[i]])
plt.show()