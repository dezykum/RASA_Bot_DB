from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from rasa_core.run import serve_application
from rasa_core import config
import rasa_core
#from rasa_core.train import online
from rasa_core.agent import Agent
from rasa_core.channels.console import CmdlineInput
# ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)


def run_weather_online(input_channel, interpreter,
                          domain_file="weather_domain.yml",
                          training_data_file='data/stories.md'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=10), KerasPolicy(batch_size=50,epochs=200,max_training_samples=300)],
                  interpreter=interpreter)
    data = agent.load_data(training_data_file)
    #agent.train(data)

    # agent.train(data,input_channel=input_channel,batch_size=50,epochs=200,max_training_samples=300)

    agent.train(data)

    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
    this_agent=run_weather_online(CmdlineInput(), nlu_interpreter)

    rasa_core.run.serve_application(this_agent,channel='cmdline')