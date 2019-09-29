import matplotlib.pyplot as plt

def plot_history(history):
  fig = plt.figure(figsize = (12, 6))
  
  keys = [k.replace('val_', '') for k in list(history.history)]
  # Remove duplicates.
  keys = set(keys)
  # Convert to list and sort (so that panels have consistent order).
  keys = list(keys)
  keys.sort()
  
  for i, key in enumerate(keys):
    fig.add_subplot(1, len(keys), i+1)
    plt.plot(history.history[key])
    plt.plot(history.history['val_'+key])
    plt.legend(['train', 'validate'])
    plt.title(key.capitalize())
    plt.xlabel('epoch')
    plt.ylabel(key)

  plt.show()

