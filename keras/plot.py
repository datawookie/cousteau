import matplotlib.pyplot as plt

def plot_history(history, figsize=(12, 6), log=None):
  fig = plt.figure(figsize = figsize)
  
  keys = [k.replace('val_', '') for k in list(history.history)]
  # Remove duplicates.
  keys = set(keys)
  # Convert to list and sort (so that panels have consistent order).
  keys = list(keys)
  keys.sort()

  # Move loss to first place (if present).
  #
  try:
    keys.remove('loss')
  except ValueError:
    pass
  else:
    keys.insert(0, 'loss')
  
  for i, key in enumerate(keys):
    fig.add_subplot(1, len(keys), i+1)
    plt.plot(history.history[key])
    plt.plot(history.history['val_'+key])
    plt.legend(['train', 'validate'])
    plt.title(key)
    plt.xlabel('epoch')
    plt.ylabel(key)
    if 'y' in log:
      plt.yscale('log')
    if 'x' in log:
      plt.xscale('log')

  plt.show()
