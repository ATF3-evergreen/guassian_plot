import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
TODO: stop infinite run
'''


def avg_animate(i, averages, ax, line, text):
    N = i + 1
    avg = averages[-1]
    val = random.gauss(0, 1)
    avg = avg + (val - avg) / N
    averages.append(avg)
    # averages = averages[-100:]  # only keep last 100 values for efficiency

    # update line and text
    line.set_data(range(len(averages)), averages)
    text.set_text(f'N = {N}, Avg = {avg:.2f}')

    # update axis limits
    ax.relim()
    ax.autoscale_view()

    if N >= 1000:  # stop animation after 1000 frames not working
        return None

    return line, text


# create figure and axis
fig, ax = plt.subplots()
ax.set_xlabel('N')
ax.set_ylabel('Running Average')

# create line and text objects
line, = ax.plot([], [])
text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

# create FuncAnimation instance
averages = [0]
ani = FuncAnimation(fig, avg_animate, fargs=(averages, ax, line, text), interval=10)

plt.show()
