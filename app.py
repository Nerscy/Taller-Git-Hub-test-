<<<<<<< HEAD
'''
Hacemos Featuring Engineering
'''
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
test_df['Age'].fillna(test_df['Age'].mean(), inplace=True)
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)
test_df['Embarked'].fillna(test_df['Embarked'].mode()[0], inplace=True)
=======
<<<<<<< HEAD
'''
Hacemos Featuring Engineering
'''
<<<<<<< HEAD
=======
>>>>>>> epic-branch-2
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
<<<<<<< HEAD
axis=0)
>>>>>>> ticket-3
=======
axis=0)
>>>>>>> epic-branch-2
>>>>>>> epic-branch-2
