import matplotlib.pyplot as plt

def showThings(all_y_values):
    # Sample data
    x_values = [1, 2, 3, 4, 5, 6, 7]

    for y_values in all_y_values:
        # Plot the data
        plt.plot(x_values, y_values, marker='', linestyle='-')

    # Adding labels to the x-axis
    plt.xticks(x_values, ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label 6', 'Label 7'])

    # Adding labels to the y-axis and the plot
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Multiple Lines on a Line Graph')

    # Adding a legend to differentiate between the lines
    plt.legend()

    # Display the plot
    plt.show()
