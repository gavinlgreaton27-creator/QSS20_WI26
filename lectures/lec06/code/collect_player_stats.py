import pandas as pd
import numpy as np
import time


def get_player_ids(player_list_path):
    df = pd.read_csv(player_list_path, skiprows=1)
    return df.iloc[:, -1].tolist()


def get_player_stats(player_id):
    # The URL for the player's stats
    url = (
        f"https://www.pro-football-reference.com/players/{player_id[0]}/{player_id}.htm"
    )
    # read_html returns a list of all tables found on the page
    tables = pd.read_html(url)
    # The 'rushing_and_receiving' table is typically the first one (index 0)
    df = tables[1]
    return df


def main():
    PLAYER_LIST_PATH = "./data/2024_drafted_players.csv"
    PLAYER_STATS_OUTPUT_DIR = "./data/player_stats/"

    player_ids = get_player_ids(PLAYER_LIST_PATH)
    for pid in player_ids:
        # print out progress
        print(f"Fetching stats for player ID: {pid}")
        df = get_player_stats(pid)
        df.to_csv(f"{PLAYER_STATS_OUTPUT_DIR}{pid}.csv", index=False)
        # add random sleep to be polite to the server
        sleep_time = np.random.uniform(0.05, 2)
        print(f"Fetched stats for {pid}, sleeping for {sleep_time:.2f}")
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()
