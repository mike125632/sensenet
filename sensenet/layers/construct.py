from sensenet.layers.utils import make_sequence
from sensenet.layers.legacy import make_legacy_sequence
from sensenet.layers.tree import ForestPreprocessor
from sensenet.layers.block import SIMPLE_LAYERS, BLOCKS

LAYER_FUNCTIONS = {}
LAYER_FUNCTIONS.update(SIMPLE_LAYERS)
LAYER_FUNCTIONS.update(BLOCKS)

def layer_sequence(model):
    layers_params = model['layers']

    if any(p.get('type', None) == None for p in layers_params):
        return make_legacy_sequence(layers_params)
    else:
        return make_sequence(layers_params, LAYER_FUNCTIONS)

def tree_preprocessor(model):
    if model.get('trees', None):
        return ForestPreprocessor(model)
    else:
        return None