import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Equations from https://en.wikipedia.org/wiki/Lotka–Volterra_equations
# Initial guesses from Google Gemini, 4 Aug 2026
#    prompt: "predator prey population equation example values"


def func_penguin(x, y, gamma, delta, dt):
    """
    Generates population evolution for penguins
    Generates population evolution for fish
    :param x: population of penguins
    :type x: float
    :param y: population of fish
    :type y: float
    :param gamma: penguin death rate
    :type gamma: float
    :param delta: interaction parameter between penguins and fish
    :type delta: float
    :param dt: time step size
    :type dt: float
    :return: all
    :rtype: numpy.ndarray
    """
    return (-gamma*x + delta * x * y)*dt

def func_fish(x, y, alpha, beta, dt):
    """
    Generates population evolution for fish
    :param x: population of penguins
    :type x: float
    :param y: population of fish
    :type y: float
    :param alpha: fish growth rate
    :type alpha: float
    :param beta: interaction parameter between fish and penguins
    :type beta: float
    :param dt: time step size
    :type dt: float
    :return: all
    :rtype: numpy.ndarray
    """
    return (alpha*y - beta * x * y)*dt

def main(n, pen, fish, alpha, beta, gamma, delta, dt, sample=None, plot=False):
    """
    Main loop for creating population evolutions for penguins and fish and preparing arrays to
    write into Microsoft Excel files
    """

    fishes = np.zeros(n)
    penguin = np.zeros(n)
    ti =  np.zeros(n)

    all = np.zeros(n, dtype=[('time','f'),('penguins','f'),('fish','f'),
                             ('alpha','f'),('beta','f'),('gamma','f'),('delta','f')])

    for i in range(n):
        dpen = func_penguin(pen, fish, gamma, delta, dt)
        pen += dpen

        dfish = func_fish(pen, fish, alpha, beta, dt)
        fish += dfish

        fishes[i] = fish
        penguin[i] = pen
        ti[i] = i*dt

        all[i]['time'] = i*dt
        all[i]['penguins'] = pen
        all[i]['fish'] = fish
        all[i]['alpha'] = alpha
        all[i]['beta'] = beta
        all[i]['gamma'] = gamma
        all[i]['delta'] = delta


    if plot is not None:
        plt.figure()
        plt.plot(ti,fishes, label = "fish")
        plt.plot(ti,penguin, label = "penguins")
        plt.xlabel('Time')
        plt.ylabel('Population')

        plt.legend()
        plt.savefig(plot)

    if sample is not None:
        idx = np.random.choice(n, sample, replace=False)
        all = all[idx]

    df_all = pd.DataFrame(all)

    return df_all

p_pen = [10]*6
p_fish = [100, 10, 10, 10, 10, 100]
p_alpha = [2., 2., 2., 2., 5., 5.]
p_beta = [0.1, 0.1, 0.2, 0.2, 0.2, 0.2]
p_gamma = [1.5, 1.5, 1.5, 1.5, 1.5, 1.5]
p_delta = [0.02, 0.02, 0.02, 0.08, 0.08, 0.08]
p_dt = 0.1
p_n=200

path = "../data/penguin_project_data/project_data_2025/"

file_names = [  'data_final_v2a.xlsx',
                "data_final_v21.xlsx",
                "data_final_final.xlsx",
                "data_final_final_last_one.xlsx", 
                "data_final_final_last_one_test.xlsx",
                "data_final_v4_revised_jerrys_comments.xlsx"
             ]


for i in range(6):
    plotname = path+file_names[i][:-4]+"png"
    pan_df = main(p_n, p_pen[i], p_fish[i], p_alpha[i], p_beta[i], p_gamma[i], p_delta[i], p_dt, plot=plotname)
    pan_df.to_excel(path+file_names[i], sheet_name="Penguins")

plt.show()