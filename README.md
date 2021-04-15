## Conversational AI in Vietnamese using Rasa for Trí Nhân Robot

This project illustrates Tri Nhan's ability to communicate in Vietnamese. This is a demo for educational and research purposes only, it does not reflect the robot's true conversational capabilities.

This open source version does not include skills such as question answering, weather forecast, solving maths, poetry (Natural Language Generation), device control,... However, it has skills to tell the current time and to offer a search link for out-of-scope questions.

Tested with Rasa Open Source 2.5.0.

## Installation

Create a virtual environment, install Rasa Open Source and additional packages:

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -U pip setuptools wheel
(venv) $ pip3 install rasa
(venv) $ pip3 install pyvi
(venv) $ pip3 install fasttext
```
Optional, if you want to use 'underthesea' for tokenizer:
```
(venv) $ pip3 install underthesea
```

## Usage

1. Download and extract pre-trained fasttext model

Download [this file](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.vi.300.bin.gz) and extract cc.vi.300.bin into 'fasttext' directory. The file path will be: tri-nhan-rasa/fasttext/cc.vi.300.bin

2. Run Custom Action Server

Inside the virtual environment, go to the project directory:
```
(venv) $ cd tri-nhan-rasa
(venv) $ rasa run actions
```
or:
```
(venv) $ python3 -m rasa_sdk --actions actions
```

3. Train your model

Edit training data (in data/nlu.yml) and responses (in domain.yml) if you want, and train your model:
```
(venv) $ rasa train
```

4. Start Rasa

```
(venv) $ rasa shell
```

See [Rasa documentation](https://rasa.com/docs/rasa/) for more help.

## Customization

1. You can use 'pyvi' (default) or 'underthesea' for tokenizer. Change the parameter 'tokenizer' in config.yml to 'underthesea' if you need to use 'underthesea' instead of 'pyvi', and retrain your model.

2. The fasttext featurizer in Rasa NLU pipeline needs a minimum of 8GB of RAM. You can use config-minimal.yml to avoid using fasttext vectors, but the accuracy may be less.

3. To build Docker image for Custom Action Server, run this command in the project directory (you need Docker Engine installed):

```
$ sudo docker build . -t <yourname>/<yourimage>:<yourtag>
```
Now you can run Custom Action Server outside of Rasa:
```
sudo docker run -p 5055:5055 <yourname>/<yourimage>:<yourtag>
```

4. You can change the fallback thresholds and others in config.yml. Run 'rasa train' then 'rasa test' for an evaluation of your new model (the evaluation will be in 'results' directory).
