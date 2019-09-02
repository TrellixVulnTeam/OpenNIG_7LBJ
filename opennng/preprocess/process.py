import numpy as np
import os


def process_mnist(raw_data_path, processed_data_path, normalize=True):
    """
        This function loads the mnist .npy files and process them.

        Args:
            raw_data_path (str): Path of the mnist .npy raw files.
            processed_data_path (str): Path of the mnist .npy processed files.
            normalize (bool): Whether to normalize the data in [-1, 1] interval.
    """
    train = np.load(os.path.join(raw_data_path, "train.npy"))
    eval = np.load(os.path.join(raw_data_path, "eval.npy"))

    if normalize:
        train = (train - 127.5) / 255
        eval = (eval - 127.5) / 255

    if len(train.shape) == 3:
        train = np.expand_dims(train, axis=3)
    if len(eval.shape) == 3:
        eval = np.expand_dims(eval, axis=3)

    if not os.path.exists(processed_data_path):
        os.makedirs(processed_data_path)

    np.save(os.path.join(processed_data_path, "train.npy"), np.float32(train))
    np.save(os.path.join(processed_data_path, "eval.npy"), np.float32(eval))


def process_facade(raw_data_path, processed_data_path, normalize=True):
    """
        This function loads the facade .npy files and process them.

        Args:
            load_path (str): Path of the facade .npy raw files.
            save_path (str): Path of the facade .npy processed files.
            normalize (bool): Whether to normalize the data in [-1, 1] interval.
    """
    print("Working on processed raw data for facade dataset...")

    #train_X = np.load(os.path.join(raw_data_path, "train_X.npy"))
   # train_y = np.load(os.path.join(raw_data_path, "train_y.npy"))
    eval_X = np.load(os.path.join(raw_data_path, "eval_X.npy"))
    #eval_y = np.load(os.path.join(raw_data_path, "eval_y.npy"))

    if normalize:
       # train_X = (train_X - 127.5) / 255
       # train_y = (train_y - 127.5) / 255
        eval_X = np.divide(eval_X, 255)
        #eval_y = (eval_y - 127.5) / 255

    if not os.path.exists(processed_data_path):
        os.makedirs(processed_data_path)

    print(eval_X.shape)

   # np.save(os.path.join(processed_data_path, "train_X.npy"), np.float32(train_X))
  #  np.save(os.path.join(processed_data_path, "train_y.npy"), np.float32(train_y))
    np.save(os.path.join(processed_data_path, "eval_X.npy"), np.float32(eval_X))
   # np.save(os.path.join(processed_data_path, "eval_y.npy"), np.float32(eval_y))