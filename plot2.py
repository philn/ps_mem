import numpy as np
import matplotlib
#matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import sys

def main(args):
    if not args:
        print("Usage: %s /path/to/csv-file.csv")
        return 0

    time_format = '%Y-%m-%d %H:%M:%S'

    col_names = ["timestamp", "mem"]
    dtypes = ["object", "float"]
    print(args)
    mydata = np.genfromtxt(args[0], skip_header=1,delimiter=",", names=col_names, dtype=dtypes)

    time = [datetime.strptime(i.decode("utf-8"), time_format) for i in mydata['timestamp']]

    mem = mydata['mem']

    fig = plt.figure()
    rect = fig.patch
    rect.set_facecolor('#31312e')

    ax1 = fig.add_subplot(1, 1, 1, axisbg='grey')
    ax1.plot_date(time, mem, 'c', linewidth=2)
    ax1.tick_params(axis='x', colors='c')
    ax1.tick_params(axis='y', colors='c')
    ax1.spines['bottom'].set_color('w')
    ax1.spines['top'].set_color('w')
    ax1.spines['left'].set_color('w')
    ax1.spines['right'].set_color('w')
    ax1.yaxis.label.set_color('c')
    ax1.xaxis.label.set_color('c')
    ax1.set_title('Memory usage', color='c')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Mem (MiB)')

    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax1.xaxis.set_minor_formatter(mdates.DateFormatter("%H:%M"))

    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=25)
    plt.savefig('out.png', dpi=100)
    #plt.show()
    print("Figure saved to out.png")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
