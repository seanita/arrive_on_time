import pickle
import matplotlib.pyplot as plt

# here = os.path.dirname(os.path.abspath(__file__))
def custom_scatter(x, y):
    """
    Parameters
    ----------
    x, y: iterable of floats
        x and y need to be the same size.
    """
    plt.plot(
        x, y,
        color = 'black',
        marker = '.',
        linestyle = 'none',
        alpha = 0.2,
    ) 
    plt.show()

def store(data, data_filename, verbose=True):
    """ 
    Parameters
    ----------
    data: Any serializable object
    data_filename: string
    verbose: boolean
    """
    with open(data_filename, 'wb') as data_file:
        pickle.dump(data, data_file)

    if verbose:
        print('Data is stored in \'{filename}\''.format(filename=data_filename))


def restore(data_filename):
    """
    Parameters
    ----------
    """
    data = None
    with open(data_filename, 'rb') as data_file:
        data = pickle.load(data_file)
    return data


