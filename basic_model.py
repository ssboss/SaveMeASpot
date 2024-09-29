import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import regularizers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.regularizers import L1L2
import numpy as np
import pandas as pd

simple_model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(256,100,100,1),
    tf.keras.layers.Dense(units=128, activation="relu", kernel_regularizer=L1L2(l1=0.001,l2=0.001)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(units=64, activation="relu", kernel_regularizer=L1L2(l1=0.001,l2=0.001)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(units=32, activation="relu", kernel_regularizer=L1L2(l1=0.001,l2=0.001)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(units=10, activation="softmax")
])

op_1 = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_fxn = tf.keras.losses.SparseCategoricalCrossentropy()

simple_model.compile(optimizer=op_1, loss=loss_fxn, metrics=['accuracy'])


epoch = 15

simple_model.fit(train_ds,validation_data=val_ds, epochs=epoch)


