import sys
import pandas as pd
import numpy as np
import platform
from pathlib import Path, PureWindowsPath

real_historic_data = Path("../data/real/Chispazo.csv")
simulated_data = Path('../data/simulation/simulation.csv')
save_path = Path("../data/")

if not real_historic_data.exists():
    print("File not found in path")
    sys.exit()
elif(platform.system() == 'Windows'):
    df = pd.read_csv(PureWindowsPath(real_historic_data), sep = ',', encoding = 'utf8')
else:
    df = pd.read_csv(real_historic_data, sep = ',', encoding = 'utf8')

def generate_transition_matrix(Rn, flag):
    matrix = list(df[Rn])
    matrix = pd.DataFrame(matrix)
    matrix['shift'] = matrix[0].shift(-1)
    matrix['count'] = 1
    matrix = matrix.groupby([0, 'shift']).count().unstack().fillna(0)
    matrix = matrix.div(matrix.sum(axis = 1), axis = 0).values
    #for an easier reading of results, in the consolidation of transition matrices file, matrices are transposed and multiplied by 100 for a percentage representatrion of probability
    if(flag):
        matrix = np.multiply(np.asmatrix(matrix).transpose(),100.00)
    else:
        pass
    matrix = pd.DataFrame(matrix)
    matrix = matrix.rename(columns= dict(zip(matrix.columns, [x for x in range(min(list(df[Rn])), max(list(df[Rn])) + 1)])))
    matrix.insert(0, 'state/transition', [x for x in range(min(list(df[Rn])), max(list(df[Rn])) + 1)])
    return matrix

def convert_to_csv(data_frame, Rn):
    if(platform.system() == 'Windows'):
        data_frame.to_csv(PureWindowsPath(save_path / (Rn + '.csv')), index = False, sep = ',', encoding = 'utf8')
    else:
        data_frame.to_csv(save_path / (Rn + '.csv') ,index = False, sep = ',', encoding = 'utf8')
    pass

def convert_to_excel():
    if(platform.system() == 'Windows'):
        writer = pd.ExcelWriter( PureWindowsPath(save_path / ('consolidado_matrices_lr.xlsx'))) #generates easy to read matrix consolidation
        writer2 = pd.ExcelWriter(PureWindowsPath(save_path) / ('consolidado_matrices.xlsx')) #generates raw matrices consolidation
    else:
        writer = pd.ExcelWriter( save_path / ('consolidado_matrices_lr.xlsx')) #generates easy to read matrix consolidation
        writer2 = pd.ExcelWriter(save_path / ('consolidado_matrices.xlsx')) #generates raw matrices consolidation
    for i in range(1, 6):
        generate_transition_matrix(f'R{i}', True).to_excel(writer, sheet_name = f'R{i}', index = False)
        generate_transition_matrix(f'R{i}', False).to_excel(writer2, sheet_name = f'R{i}', index = False)
        #genertate indivial CSV files for each variable instead of a consolidation
        convert_to_csv(generate_transition_matrix(f'R{i}',False), f'R{i}')
    writer.save()
    writer2.save()
    print("All files were saved... The process has ended successfully ")
    pass

convert_to_excel()