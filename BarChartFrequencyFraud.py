Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import matplotlib.pyplot as plt
>>> df = pd.read_csv(r'C:\Users\tbkcpu\Desktop\CreditFraudLevel2.csv')
>>> # Filter data for fraud cases only 
... fraud_cases = df[df['Fraud_Flag_or_Label'] == 1]
>>> # Count the number of fraud cases per card type
... fraud_counts = fraud_cases['Card_Type'].value_counts()
>>> # Define colors for each card type as requested
... colors = {
...     'American Express': 'royalblue',
...     'MasterCard': 'orangered',
...     'Visa': 'navy'
... }
>>> # Create the bar chart
... plt.figure(figsize=(10, 6))
<Figure size 1000x600 with 0 Axes>
>>> bars = plt.bar(fraud_counts.index, fraud_counts.values, color=[colors.get(x, 'gray') for x in fraud_counts.index])
>>> # Add numbers (counts) above each bar
... for bar in bars:
...     yval = bar.get_height()
...     plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')
... 
...     
Text(0.0, 86, '85')
Text(1.0, 83, '82')
Text(2.0, 82, '81')
>>> # Customize the plot
... plt.title('Number of Reported Fraud Cases by Card Type')
Text(0.5, 1.0, 'Number of Reported Fraud Cases by Card Type')
>>> plt.xlabel('Card Type')
Text(0.5, 0, 'Card Type')
>>> plt.ylabel('Number of Fraud Cases')
Text(0, 0.5, 'Number of Fraud Cases')
>>> plt.xticks(rotation=0)  # Rotate x-axis labels if needed
([0, 1, 2], [Text(0, 0, 'MasterCard'), Text(1, 0, 'American Express'), Text(2, 0, 'Visa')])
>>> # Show plot
... plt.tight_layout()
>>> plt.show()
