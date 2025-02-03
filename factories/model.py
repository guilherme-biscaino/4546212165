import tensorflow as tf
from PIL import Image
import numpy as np


def model_creator(num_classes):
    base_model = tf.keras.applications.MobileNetV2(
        weights="imagenet",
        include_top=False)
    base_model.trainable = False

    inp = tf.keras.Input(shape=(224, 224, 3))
    x = base_model(inp, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(num_classes)(x)
    out = tf.keras.layers.Softmax()(x)
    model = tf.keras.Model(inp, out)

    model.compile(
        optimizer='Adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


def model_save(model, name):
    model.save(name + ".keras")


def model_load(model_path):

    return tf.keras.models.load_model(model_path)


def model_predict(model, image, class_names):
    image = Image.open(image)
    image = np.array(image)
    image = image[:, :, :3]
    image = tf.image.resize(image, [224, 224])
    image = np.expand_dims(image, axis=0)
    preds = model.predict(image)
    predicted_class_index = np.argmax(preds)

    predicted_class = class_names[predicted_class_index]
    return predicted_class
