# generate parameters for batch submission
# data source, layers, f_map, epochs, batch_size, n sampes, sample batches
import numpy as np
import pickle

params ={}
layers = np.array((80, 60, 40)).astype('uint8')
filters = np.array((60, 40, 20)).astype('uint16')
temperature = np.array((0))
n_runs= filters.size * layers.size * temperature.size
identity = np.ones(n_runs).astype('uint8')
params['filters'] = [filters[i] for i in range(filters.size) for j in range(layers.size) for k in range(temperature.size)]
params['layers'] = [layers[j] for i in range(filters.size) for j in range(layers.size) for k in range(temperature.size)]
params['softmax_temperature'] = temperature * identity# [temperature[k] for i in range(filters.size) for j in range(layers.size) for k in range(temperature.size)]
params['dataset_size'] = 40000 * identity
params['model'] = 5 * identity
params['bound_type'] = 0 * identity
params['boundary_layers'] = 2 * identity
params['training_data'] = 1 * identity
params['training_batch'] = 64 * identity
params['sample_batch_size'] = 2048 * identity
params['n_samples'] = 1 * identity
params['run_epochs'] = 1000 * identity
params['train_margin'] = 1e-5 * identity
params['average_over'] = 5 * identity
params['outpaint_ratio'] = 4 * identity
params['generation_type'] = 2 * identity
params['GPU'] = 1 * identity

with open('batch_parameters.pkl', 'wb') as f:
    pickle.dump(params, f, pickle.HIGHEST_PROTOCOL)
