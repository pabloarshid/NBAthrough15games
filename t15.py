import numpy as np
import pandas as pd
from nba_py import player

get_player = player.get_player("Lebron", last_name="James")

print(get_player)