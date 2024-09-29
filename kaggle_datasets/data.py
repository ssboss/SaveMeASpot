import numpy as np
import os
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.regularizers import L1L2
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# input_shape = (100,100,3)

# x_train = np.ndarray((1, 100, 100, 3))
# y_train = np.ndarray((1, 2))
# x_val = np.ndarray((1, 100, 100, 3))
# y_val = np.ndarray((1, 2))

# # Define the path to the directory containing the images
# for folder_name in os.listdir('/kaggle/input/parking-lot-dataset/PKLot/PKLotSegmented/PUC/Cloudy'):
#     train_dir = f"/kaggle/input/parking-lot-dataset/PKLot/PKLotSegmented/PUC/Cloudy/{folder_name}"

#     # Define the input shape and number of classes for your dataset
#     num_classes = 2

#     # Define the image data generator with augmentation parameters
#     augment_datagen = ImageDataGenerator(
#             rescale=1./255,
#             shear_range=0.1,
#             rotation_range=20,
#             zoom_range=0.1,
#             horizontal_flip=True,
#             vertical_flip=True,
#             validation_split=0.2)

#     # Load the images into separate folders based on their class labels
#     train_generator = augment_datagen.flow_from_directory(
#             train_dir,
#             shuffle=True,
#             seed=42,
#             target_size=input_shape[:2],
#             batch_size=256,
#             class_mode='categorical',
#             subset='training')

#     validation_generator = augment_datagen.flow_from_directory(
#             train_dir,
#             target_size=input_shape[:2],
#             batch_size=256,
#             shuffle=True,
#             seed=42,
#             class_mode='categorical',
#             subset='validation')

#     x_tr, y_tr = next(train_generator)
#     x_v, y_v = next(validation_generator)
    
#     x_val = np.append(x_val, x_v, axis=0)
#     y_val = np.append(y_val, y_v, axis=0)
    
#     x_train = np.append(x_train, x_tr[:500], axis=0)
#     y_train = np.append(y_train, y_tr[:500], axis=0)


batch_size = 256
img_height = 100
img_width = 100
cwd = os.getcwd()
data_dir = f'{cwd}/parking-lot-dataset/PKLot/PKLot/PUCPR/'
data_dir2 = f'{cwd}/parking-lot-dataset-PKLot/PKLot/UFPRO4'

train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.5,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.5,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

test_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
)



normalization_layer = tf.keras.layers.Rescaling(1./255)

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

input_shape = (100,100,3)



simple_model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=input_shape),
    tf.keras.layers.Dense(units=128, activation="relu", kernel_regularizer=L1L2(l1=0.001,l2=0.001)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(units=128, activation="relu", kernel_regularizer=L1L2(l1=0.001,l2=0.001)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(units=128, activation="relu", kernel_regularizer=L1L2(l1=0.001,l2=0.001)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(units=10, activation="softmax")
])

op_1 = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_fxn = tf.keras.losses.SparseCategoricalCrossentropy()

simple_model.compile(optimizer=op_1, loss=loss_fxn, metrics=['accuracy'])


epoch = 15

simple_model.fit(train_ds,validation_data=val_ds, epochs=epoch)






