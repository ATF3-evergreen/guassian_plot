import random
import matplotlib.pyplot as plt


def average3(n):
    avg = 0
    averages = []  # list to store running averages

    for i in range(1, n):
        val = random.gauss(0, 1)
        avg = avg + (val - avg) / i
        averages.append(avg)

    # plot running averages
    plt.plot(range(1, n), averages)
    plt.xlabel('N')
    plt.ylabel('Running Average')
    plt.title('Running Average of random.gauss() Values')
    plt.show()


def average3_hist(n):
    avg = 0
    averages = []  # list to store running averages

    for i in range(1, n):
        val = random.gauss(0, 1)
        avg = avg + (val - avg) / i
        averages.append(avg)


# plot histogram of running averages, needs axes or scale adjusted
    plt.hist(averages, bins=500)
    plt.axvline(x=avg, color='r', linestyle='dashed', linewidth=2)
    plt.xlabel('Running Average')
    plt.ylabel('Frequency')
    plt.title('Histogram of Running Average of random.gauss() Values')
    plt.show()


'''def avg_animate(i):
    n = i + 1

    avg = 0
    averages = []

    for j in range(1, n):
        val = random.gauss(0, 1)
        avg = avg + (val - avg) / j
        averages.append(avg)

    # clear previous plot and plot new histogram of running averages
    plt.clf()
    plt.hist(averages, bins=50)
    plt.axvline(x=avg, color='r', linestyle='dashed', linewidth=2)
    plt.xlabel('Running Average')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of Running Average of random.gauss() Values (n={n})')


    fig = plt.figure()
    ani = FuncAnimation(fig, avg_animate, frames=100, interval=10)
    
    plt.show()
'''

if __name__ == '__main__':

    # average3(1000)  # test with N = 1000

    average3_hist(1000)

    # avg_animate(1000)
