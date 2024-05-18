import pandas as pd

#Import Data 
labels= pd.read_csv('labels_obf.csv')
transaction = pd.read_csv('transactions_obf.csv')

#Combine the data and create Fraudulent column 
dataframe = pd.merge(transaction, labels, on='eventId', how='left')
dataframe['fradulent'] = dataframe['reportedTime'].notnull()

# Review the data dictionary to understand the meaning of each column
data_dictionary = {
    'transactionTime': 'Timestamp of the transaction',
    'eventId': 'ID associated with the event',
    'accountNumber': 'Account number associated with the transaction',
    'merchantId': 'ID of the merchant involved in the transaction',
    'mcc': 'Merchant category code',
    'merchantCountry': 'Country of the merchant',
    'merchantZip': 'ZIP code of the merchant',
    'posEntryMode': 'Point of sale entry mode',
    'transactionAmount': 'Amount of the transaction',
    'availableCash': 'Available cash for the transaction'
}

print("\nData dictionary:")
for column, description in data_dictionary.items():
    print(f"{column}: {description}")

# Check the data types of each column
print("\nData types of each column:")
print(dataframe.dtypes)

# Check for missing values
print("\nMissing values:")
print(dataframe.isnull().sum())


# For categorical columns, you can check unique values and their frequencies
print("\nUnique values for categorical columns:")
for column in dataframe.select_dtypes(include='object').columns:
    print(f"{column}: {dataframe[column].nunique()} unique values")

#Convert the fradulent column to Binary
dataframe['fradulent'] = dataframe['fradulent'].astype(int)

import matplotlib.pyplot as plt




def plot_fraudulent_transactions_by_country(dataframe):
    # Filter the dataframe for fraudulent transactions
    fraudulent_transactions = dataframe[dataframe['fradulent'] == True]

    # Count the number of fraudulent transactions for each country
    fraudulent_counts = fraudulent_transactions['merchantCountry'].value_counts()

    # Plot the bar plot
    plt.figure(figsize=(12, 6))
    fraudulent_counts.plot(kind='bar', color='red')
    plt.xlabel('Merchant Country')
    plt.ylabel('Number of Fraudulent Transactions')
    plt.title('Fraudulent Transactions by Country')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

# Call the function
plot_fraudulent_transactions_by_country(dataframe)



