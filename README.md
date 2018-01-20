# Deep Bilateral Learning for Real-Time Image Enhancements (batch processing version)

This code aims at implementing the batch version of source code [Code Page](https://github.com/mgharbi/hdrnet).

Tested on Python 2.7, Ubuntu 16.04, gcc-5.4 and Cython-0.27.3 (**Note**: OS and gcc are different from the original source).

## Setup

### Dependencies

To install the Python dependencies, run:

    cd hdrnet
    pip install -r batch_requirements.txt

### Build

Please refer hdrnet project  [Code Page](https://github.com/mgharbi/hdrnet)

### Test

Please refer hdrnet project  [Code Page](https://github.com/mgharbi/hdrnet)

### Download pretrained models

Please refer hdrnet project  [Code Page](https://github.com/mgharbi/hdrnet)

## Usage

To train a batch of models, run the following command:

    ./hdrnet/bin/batch train.py <batch_checkpoint_dir> <path/to_training_data/folder>

The folders under the training data folder represent different task. Look at `sample_data/identity/` for a typical structure of the each training task data folder.

You can monitor the training process using Tensorboard:

    tensorboard --logdir <batch_checkpoint_dir>

To run a trained model on a novel image (or set of images), use:

    ./hdrnet/bin/batch_run.py <batch_checkpoint_dir> <path/to_eval_data_batch> <output_dir>

## Fixed issues 

* The requirement.txt contains mistake 'scikit', it should be 'scikit_image', which already includes. I already reported it the author.
* The requirement.txt does not include all of the required packages. For example, python-opencv and slicy do not exist. I already put them in the batch_requriements.txt.
* The GPU will be OOM,  it may work if adjust the batch size.
* The root folder is not automatically added to the python path. I already fixed in train.py and run.py.

## Contact

Email: achenfengb@gmail.com

