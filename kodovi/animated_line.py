import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
i = 0;

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read data to show
    i = i+1;

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f')[:-5])       
    ys.append(i)

    # Limit x and y lists to 10 items
    xs = xs[-30:]
    ys = ys[-30:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Vrijeme')
    plt.ylabel('Vrijednost')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()