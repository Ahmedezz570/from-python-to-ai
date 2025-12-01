# import tensorflow as tf
# mnist = tf.keras.datasets.mnist
# (x_train, y_train),(x_test, y_test) = mnist.load_data()
#
#
#
#
# model = tf.keras.models.Sequential() ## Deep Neural Network empty
# model.add(tf.keras.layers.Flatten()) # make ths one Dimension
# model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  #128 neuron => hidden layer
# model.add(tf.keras.layers.Dropout(0.2)) # Random neuron 20% delete every time
# model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
#
# model.fit(x_train, y_train, epochs=5    )
# model.predict(x_train)
# val_loss , val_acc = model.evaluate(x_test , y_test)
# print('\nVal loss:', val_loss)
# print('Val accuracy:', val_acc)
# model.save('1.model')
# new_model = tf.keras.models.load_model('1.model')
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(128, activation=tf.nn.relu),
#     tf.keras.layers.Dense(128, activation=tf.nn.relu),
#     tf.keras.layers.Dense(10, activation=tf.nn.softmax)
# ])




# print("X Train Shape is " , x_train.shape)
# # print("X Train Shape is " , x_train[5])
# print("---------------------------------")
# print("X Test Shape is " , x_test.shape)
# print("Y Train Shape is " , y_train.shape)

# import matplotlib.pyplot as plt
# plt.imshow(x_train[5], cmap='gray')
# plt.show()






import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize البيانات
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=5)

val_loss, val_acc = model.evaluate(x_test, y_test)
print("Val Loss:", val_loss)
print("Val Accuracy:", val_acc)

# Save
model.save("model.keras")

# Load
new_model = tf.keras.models.load_model("model.keras")



# Normalize
#
# Build model
#
# Compile
#
# Train
#
# Evaluate
#
# Save/Load

















