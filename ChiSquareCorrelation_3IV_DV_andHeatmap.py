Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
# Load the CSV data into a DataFrame 
df = pd.read_csv(r'C:\Users\tbkcpu\Desktop\CreditFraudLevel2.csv')
# Null hypothesis: There is no association between  Currency, Card Type, and Device with Fraud. 
# Alternative hypothesis: There is an association between Currency, Card Type, and Device with Fraud.

# Step 1: Check assumptions of the Chi-Square Test of Independence
# Create contingency table for the variables of interest
contingency_table = pd.crosstab([df['Transaction_Currency'], df['Card_Type'], df['Device_Information']], df['Fraud_Flag_or_Label'])
# Check assumption 1: Independence of observations 
#Observations are independent because each credit card transaction is independent of the other transactions, for example, no credit card transaction has the same transaction number. 
#Since each observation is independent of another observation, the assumption of independence is satisfied. 

# Check assumption 2: Categorical Variables
#The variables in the Chi-Square test are the following: Device Information {Tablet, Desktop, Mobile}, Transaction Currency {INR, USD, EUR}, Card Type {Visa, MasterCard, American Express}, and Fraud_Flag_or_Label {0,1) [where 0 denotes no fraud and 1 denotes fraud]. 
#All variables are categorical as Device Information, Transaction Currency, and Card Type use non-numeric entries to represent data. Fraud_Flag_or_Label is categorical because the numbers used within the variable represent a non-numerical entry. 

# Check assumption 3: Expected frequency count greater than 5 for at least 80% of cells
# Calculate expected frequencies
expected_freq = np.array(contingency_table)
chi2, p, dof, expected = chi2_contingency(expected_freq)
num_valid_cells = (expected > 5).sum()
total_cells = expected.size
percent_valid = (num_valid_cells / total_cells) * 100
# Print results of assumptions
print(f"Assumption 1: Independence of observations - Satisfied.")
Assumption 1: Independence of observations - Satisfied.
print(f"Assumption 2: Categorical Variables - Satisfied.")
Assumption 2: Categorical Variables - Satisfied.
print(f"Assumption 3: Expected frequency count is greater than 5 for at least 80% of cells.")
Assumption 3: Expected frequency count is greater than 5 for at least 80% of cells.
print(f"   - Number of valid cells: {num_valid_cells}")
   - Number of valid cells: 51
print(f"   - Total cells: {total_cells}")
   - Total cells: 54
print(f"   - Percentage valid: {percent_valid:.2f}%")
   - Percentage valid: 94.44%
if percent_valid >= 80:
    print("   - Assumption satisfied.")
else:
    print("   - Assumption violated.")

    
   - Assumption satisfied.
# Proceed only if assumptions are satisfied
if percent_valid < 80:
    print("Chi-Square test assumptions not satisfied. Exiting.")
    exit()

    
# Step 2: Perform Chi-Square Test of Independence
chi2, p, dof, expected = chi2_contingency(contingency_table)
# Print results of the Chi-Square test
print("\nChi-Square Test results:")

Chi-Square Test results:
print(f"   - Degree of Freedom: {dof}")
   - Degree of Freedom: 26
print(f"   - Chi-Square Statistic: {chi2}")
   - Chi-Square Statistic: 29.39656269910397
print(f"   - p-value: {p}")
   - p-value: 0.29335954755460625
# Interpret results
alpha = 0.05
print("\nChi-Square Test Interpretation:")

Chi-Square Test Interpretation:
if p < alpha:
    print("   - There is significant evidence to reject the null hypothesis.")
    print("   - Therefore, the relationship between Device, Card Type, and Currency")
    print("     is significant to Fraud at the 95% confidence level.")
else:
    print("   - There is not enough evidence to reject the null hypothesis.")
    print("   - Therefore, the relationship between Device, Card Type, and Currency")
    print("     is not significant to Fraud at the 95% confidence level.")

    
   - There is not enough evidence to reject the null hypothesis.
   - Therefore, the relationship between Device, Card Type, and Currency
     is not significant to Fraud at the 95% confidence level.
#Visualization for Chi-Square Test: Heatmap
#Calculate mean fraud for each combination of Transaction_Currency, Card_Type, and Device_Information
table = pd.pivot_table(df, values='Fraud_Flag_or_Label', index=['Transaction_Currency', 'Card_Type'], columns='Device_Information', aggfunc=np.mean)
# Plotting the heatmap using matplotlib
fig, ax = plt.subplots(figsize=(10, 8))
# Create heatmap
im = ax.imshow(table.values, cmap='coolwarm', vmin=0, vmax=1)
# Show all ticks and label them with respective list entries
ax.set_xticks(np.arange(len(table.columns)))
[<matplotlib.axis.XTick object at 0x000001DBF5B29290>, <matplotlib.axis.XTick object at 0x000001DBF426AA10>, <matplotlib.axis.XTick object at 0x000001DBF5A8BF10>]
>>> ax.set_yticks(np.arange(len(table.index)))
[<matplotlib.axis.YTick object at 0x000001DBF5C30D50>, <matplotlib.axis.YTick object at 0x000001DBF5C1D710>, <matplotlib.axis.YTick object at 0x000001DBF58FB4D0>, <matplotlib.axis.YTick object at 0x000001DBF6DD1AD0>, <matplotlib.axis.YTick object at 0x000001DBF6DD8110>, <matplotlib.axis.YTick object at 0x000001DBF5C0F310>, <matplotlib.axis.YTick object at 0x000001DBF6DDB550>, <matplotlib.axis.YTick object at 0x000001DBF6DDDA50>, <matplotlib.axis.YTick object at 0x000001DBF6DDFCD0>]
>>> ax.set_xticklabels(table.columns)
[Text(0, 0, 'Desktop'), Text(1, 0, 'Mobile'), Text(2, 0, 'Tablet')]
>>> ax.set_yticklabels(table.index)
[Text(0, 0, "('EUR', 'American Express')"), Text(0, 1, "('EUR', 'MasterCard')"), Text(0, 2, "('EUR', 'Visa')"), Text(0, 3, "('INR', 'American Express')"), Text(0, 4, "('INR', 'MasterCard')"), Text(0, 5, "('INR', 'Visa')"), Text(0, 6, "('USD', 'American Express')"), Text(0, 7, "('USD', 'MasterCard')"), Text(0, 8, "('USD', 'Visa')")]
>>> # Rotate the tick labels and set their alignment
... plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
[None, None, None, None, None, None, None, None, None, None, None, None]
>>> # Loop over data dimensions and create text annotations
... for i in range(len(table.index)):
...     for j in range(len(table.columns)):
...         text = ax.text(j, i, f'{table.values[i, j]:.2f}', ha="center", va="center", color="black")
... 
...         
>>> # Adding color bar
... cbar = ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
>>> cbar.set_label('Average Fraud Case')
>>> # Set labels, title, and adjust layout
... ax.set_xlabel('Device')
Text(0.5, 0, 'Device')
>>> ax.set_ylabel('Transaction Currency, Card Type')
Text(0, 0.5, 'Transaction Currency, Card Type')
>>> ax.set_title('Heatmap of Average Fraud by Currency, Card Type, and Device')
Text(0.5, 1.0, 'Heatmap of Average Fraud by Currency, Card Type, and Device')
>>> plt.tight_layout()
>>> plt.show()
