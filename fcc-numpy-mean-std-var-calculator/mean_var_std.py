import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {}
    res = np.array([list[0:3], list[3:6], list[6:9]])
    res_mean = [res.mean(axis=0).tolist(),
                res.mean(axis=1).tolist(),
                res.mean().tolist()]
    res_var = [res.var(axis=0).tolist(),
               res.var(axis=1).tolist(),
               res.var().tolist()]
    res_std = [res.std(axis=0).tolist(),
               res.std(axis=1).tolist(),
               res.std().tolist()]
    res_max = [res.max(axis=0).tolist(),
               res.max(axis=1).tolist(),
               res.max().tolist()]

    res_min = [res.min(axis=0).tolist(),
               res.min(axis=1).tolist(),
               res.min().tolist()]

    res_sum = [res.sum(axis=0).tolist(),
               res.sum(axis=1).tolist(),
               res.sum().tolist()]
    calculations = {
        'mean': res_mean,
        'variance': res_var,
        'standard deviation': res_std,
        'max': res_max,
        'min': res_min,
        'sum': res_sum
    }
    return calculations
