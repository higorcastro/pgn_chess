# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:10:49 2022

@author: HigorFPCastro
"""

import chess.pgn
import pandas as pd

pgn = open("lichess_tournament_2022.02.04_F7K4jHfG_419-trenzinho-das-onze.pgn")


my_list = []
for i in pgn:
    i = chess.pgn.read_game(pgn)
    my_list.append(i)
    df = pd.DataFrame(my_list)

#shows the 210 game in dataframe    
print(df[0][210])






    