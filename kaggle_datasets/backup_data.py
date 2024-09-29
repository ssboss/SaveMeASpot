import numpy as np
import os
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.regularizers import l2



batch_size = 256
img_height = 180
img_width = 180
cwd = os.getcwd()
data_dir = f'{cwd}/parking-lot-dataset/PKLot/PKLot/PUCPR/'
data_dir2 = f'{cwd}/parking-lot-dataset/PKLot/PKLot/UFPR04/'
data_dir3 = f'{cwd}/parking-lot-dataset/PKLot/PKLot/UFPR05'

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
    data_dir2,
    validation_split=0.5,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)




AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(2000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


input_shape = (180,180,3)




simple_model = tf.keras.models.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=input_shape),
    tf.keras.layers.Conv2D(16 , 3),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2D(32 , 3, activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2D(64 , 3, activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=128, activation="relu"),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(units=10, activation="softmax")
])

op_1 = tf.keras.optimizers.Adam(learning_rate=0.01)
loss_fxn = tf.keras.losses.SparseCategoricalCrossentropy()

simple_model.compile(optimizer=op_1, loss=loss_fxn, metrics=['accuracy'])


epoch = 35

simple_model.fit(train_ds,validation_data=val_ds, epochs=epoch)

simple_model.evaluate(val_ds)

simple_model.save("backup_pklot.keras")








