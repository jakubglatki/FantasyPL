import pandas as pd


def split_gameweek_data(gw, season, is_last):
    gw_df = pd.read_csv('data/' + season + '/gw' + str(gw) + '.csv', encoding="ISO-8859-1")
    for col in gw_df['name']:
        if '_' in col:
            gw_df[['first_name', 'second_name']] = gw_df['name'].str.split('_', n=1, expand=True)
            for col2 in gw_df['second_name']:
                if '_' in col2:
                    gw_df['second_name'] = gw_df['second_name'].str.split('_').str[0]
                    break
                else:
                    break
        else:
            break

    if season == '17_18' or season == '18_19':
        gw_df = gw_df.drop(
            ['name','id', 'round', 'kickoff_time', 'kickoff_time_formatted', 'element', 'was_home', 'fixture', 'transfers_in',
             'transfers_out', 'transfers_balance', 'team_a_score', 'team_h_score', 'opponent_team', 'ea_index',
             'loaned_in', 'loaned_out'],
            axis=1)
    elif season == '19_20':
        gw_df = gw_df.drop(['name', 'round', 'kickoff_time', 'element', 'was_home', 'fixture', 'transfers_in', 'transfers_out',
                            'transfers_balance', 'team_a_score', 'team_h_score', 'opponent_team'],
                           axis=1)
    elif season == '20_21' or season == '21_22':
        gw_df = gw_df.drop(
            ['round', 'kickoff_time', 'element', 'was_home', 'fixture', 'team', 'position', 'xP', 'transfers_in',
             'transfers_out', 'transfers_balance', 'team_a_score', 'team_h_score', 'opponent_team'],
            axis=1)

    suffix = '_' + str(gw) + '_' + season
    gw_df = gw_df.add_suffix(suffix)
    gw_df = gw_df.rename(
        columns={'first_name' + suffix: 'first_name', 'second_name' + suffix: 'second_name', 'name' + suffix: 'name'})

    if is_last:
        players = pd.read_csv('data/players_' + season + '.csv', encoding="ISO-8859-1")
        players = players[
            ['first_name', 'second_name', 'team_code_' + season, 'element_type_' + season,
             'total_points_' + season]]
        if season != '20_21' and season != '21_22':
            gw_df = gw_df.merge(players, left_on=['first_name', 'second_name'],
                                right_on=['first_name', 'second_name'])
        else:
            players['name'] = players['first_name'] + ' ' + players['second_name']
            gw_df = gw_df.merge(players, left_on=['name'],
                                right_on=['name'])
        gw_df['now_cost_' + season] = gw_df['value' + suffix]

    return gw_df


def add_gameweeks_data(first_gw, last_gw, season):
    df = pd.read_csv('data/' + season + '/players_gws.csv', encoding="ISO-8859-1")
    number_of_gameweeks = range(first_gw, last_gw + 1)
    for gw in number_of_gameweeks:
        if 'team_code_' + season in df:
            df = df.drop(
                ['team_code_' + season, 'element_type_' + season, 'total_points_' + season, 'now_cost_' + season],
                axis=1)
        if gw == last_gw:
            gw_df = split_gameweek_data(gw, season, True)
        else:
            gw_df = split_gameweek_data(gw, season, False)
        if season != '20_21' and season != '21_22':
            df = df.merge(gw_df, left_on=['first_name', 'second_name'],
                          right_on=['first_name', 'second_name'],
                          how='right')
        else:
            df['name'] = df['first_name'] + ' ' + df['second_name']
            df = df.merge(gw_df, left_on=['name'],
                          right_on=['name'],
                          how='right')

        # df.to_csv('data/' + season + '/players_gws.csv', index=False)
    if season == '20_21' or season == '21_22':
        df = df.drop(['name', 'first_name_x', 'second_name_x'], axis=1)
        df = df.rename(
            columns={'first_name_y': 'first_name', 'second_name_y': 'second_name'})

    fill_nan(df, last_gw, season)


def fill_nan_team_code_element_type(df, season):
    columns_team_code = df.filter(like='team_code_').columns
    for column in columns_team_code:
        df[column] = df[column].fillna(df['team_code_' + season])
    columns_element_type = df.filter(like='element_type_').columns
    for column in columns_element_type:
        df[column] = df[column].fillna(df['element_type_' + season])
    return df


def fill_nan(df, gw, season):
    df = fill_nan_team_code_element_type(df, season)
    columns = df.columns
    columns = columns.drop(['first_name', 'second_name'])
    for column in columns:
        df[column] = df.groupby(['value_' + str(gw) + '_' + season, 'element_type_' + season])[column].transform(
            lambda x: x.fillna(x.min()))

    for column in columns:
        df[column] = df.groupby(['element_type_' + season])[column].transform(
            lambda x: x.fillna(x.min()))
    df.to_csv('data/' + season + '/players_gws.csv', index=False)

