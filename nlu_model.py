from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

#To train the model 
def train_nlu(data, configuration, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configuration))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'weathernlu')
	return model_directory

# def run_nlu(model_directory,parse_text):
# 	interpreter = Interpreter.load(model_directory)
# 	print(interpreter.parse(parse_text))

def run_nlu(parse_text):
	interpreter = Interpreter.load('./models/nlu/default/weathernlu')
	print(interpreter.parse(parse_text))

if __name__ == '__main__':

    model_directory = train_nlu('./data/data.json', 'config_spacy.yaml', './models/nlu')
    # run_nlu('Hi')

    # run_nlu("What's the weather in Bangalore at the moment?")

    # run_nlu("hello")
  
    run_nlu("What is the employee details of Raj?")