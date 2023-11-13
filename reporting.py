import pandas as pd

filename = 'trace_file.log'

def diff(a, b):
    return (b - a) / 1000

def div (a, b):
    return a / b

lines_start = []
lines_stop = []
with open(filename, 'r') as log:
    for line in log:
        id, func_name, event, time = line.strip().split(',', 3)
        if 'start' in event:
            lines_start.append([func_name, id, event, time[-6:]])
        if 'stop' in event:
            lines_stop.append([func_name, id, event, time[-6:]])

# Seperating the start and stop time for each function call
df_start = pd.DataFrame(lines_start, columns=['func_name', 'id', 'event', 'start'])
df_stop = pd.DataFrame(lines_stop, columns=['func_name', 'id', 'event', 'stop'])

df_start = df_start.sort_values(by=['func_name', 'id'])
df_stop = df_stop.sort_values(by=['func_name', 'id'])

# Calculating the total execution for each function call
df = pd.concat([df_start, df_stop['stop']], axis=1).drop(['event'], axis=1)
df['start'] = df['start'].astype(float)
df['stop'] = df['stop'].astype(float)
df['time'] = df.apply(lambda x: diff(x['start'], x['stop']), axis=1)
df = df.drop(['start', 'stop'], axis=1)

# Grouping functions by function names
df_count = df.groupby(['func_name'])['id'].count()
df_sum = df.groupby(['func_name'])['time'].sum()

# Calculating the average execution time for each funtion
df = pd.concat([df_count, df_sum], axis=1).reset_index()
df.rename(columns={'func_name': 'Function Name', 'id': 'Num. of calls', 'time': 'Total Time (ms)'}, inplace=True)
df['Average Time (ms)'] = df.apply(lambda x: div(x['Total Time (ms)'], x['Num. of calls']), axis=1)

# Making the print pretty
df.loc[-1] = ['--------------------'] * 4
df.index = df.index + 1
df.sort_index(inplace=True)

df['Average Time (ms)'][1:] = df['Average Time (ms)'][1:].astype(float)
df['Total Time (ms)'][1:] = df['Total Time (ms)'][1:].astype(float)
df['Average Time (ms)'][1:] = df['Average Time (ms)'][1:].apply(lambda x: "{:.3f}".format(x))
df['Total Time (ms)'][1:] = df['Total Time (ms)'][1:].apply(lambda x: "{:.3f}".format(x))

pattern1 = ['|'] * len(df)
pattern2 = pattern1
pattern2[0] = '-'
df.insert(0, '|', pattern1, True)
df.insert(2, '|', pattern2, True)
df.insert(4, '|', pattern2, True)
df.insert(6, '|', pattern2, True)
df.insert(8, '|', pattern1, True)

print(df.to_string(index=False))
