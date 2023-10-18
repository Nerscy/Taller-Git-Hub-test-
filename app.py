'''
Hacemos Featuring Engineering
'''
<<<<<<< HEAD
train_df = pd.concat([train_df, pd.get_dummies(train_df['Embarked'],
prefix='Embarked')], axis=1)
test_df = pd.concat([test_df, pd.get_dummies(test_df['Embarked'], prefix='Embarked')],
axis=1)
test_df['Fare'].fillna(test_df['Fare'].dropna().mean(), inplace=True)
=======
train_df['CabinBool'] = (train_df['Cabin'].notnull().astype('int'))
test_df['CabinBool'] = (test_df['Cabin'].notnull().astype('int'))
train_df = pd.concat([train_df, pd.get_dummies(train_df['Embarked'],
prefix='Embarked')], axis=0)
test_df = pd.concat([test_df, pd.get_dummies(test_df['Embarked'], prefix='Embarked')],
axis=0)
>>>>>>> ticket-3
