import tensorflow as tf


def get_dataset(path, width, heigth, batch):
    train_ds = tf.keras.utils.image_dataset_from_directory(
        path,
        validation_split=0.1,
        subset='training',
        seed=123,
        image_size=(width, heigth),
        batch_size=batch
        )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        path,
        validation_split=0.1,
        subset='validation',
        seed=123,
        image_size=(224, 224),
        batch_size=batch
        )

    class_names = train_ds.class_names

    normalization_layer = tf.keras.layers.Rescaling(1./255)
    normalized_train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    normalized_val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = normalized_train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = normalized_val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    return train_ds, val_ds, class_names
