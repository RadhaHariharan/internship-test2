import pandas as pd
product = pd.read_csv(main.csv)


product = product.sort_values(by=['Red Cards', 'Yellow Cards'])
product.to_csv(output_file)
