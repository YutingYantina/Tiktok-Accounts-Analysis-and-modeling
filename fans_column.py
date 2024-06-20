import pandas as pd

def fans_column(csv_file):
    try:
        # 读取CSV文件，指定编码
        df = pd.read_csv(csv_file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(csv_file, encoding='gbk')

    # 处理粉丝列中的'万'
    if '粉丝' in df.columns:
        df['粉丝'] = df['粉丝'].astype(str).str.replace('万', '*10000')
        df['粉丝'] = df['粉丝'].apply(lambda x: eval(x) if '*' in x else x)
        df['粉丝'] = pd.to_numeric(df['粉丝'], errors='coerce').fillna(0).astype(int)
    
    # 将处理后的数据保存回CSV文件
    df.to_csv(csv_file, index=False, encoding='utf-8')
    print(f"Processed CSV file saved: {csv_file}")

# 示例用法
csv_file = '/accounts_info.csv'  # 替换为你的CSV文件路径
fans_column(csv_file)
