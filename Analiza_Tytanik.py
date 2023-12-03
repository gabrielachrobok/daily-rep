import argparse

import pandas as pd
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import csv

print("Pomoc w analizie ocalałych z Titanica!")

titanic_df = pd.read_csv("C://Users//Gabriela//Downloads//train.csv")

# titanic_df.info()
#
# print(titanic_df[["Survived", "Pclass", "Sex", "Age"]])

titanic_df.loc[:, "Survived"][titanic_df["Survived"] == 0] = "No"
titanic_df.loc[:, "Survived"][titanic_df["Survived"] == 1] = "Yes"
# print(titanic_df)


def if_survived():
    sns.catplot(
        data=titanic_df,
        x="Survived",
        kind="count"
    )
    plt.show()

def sex_1():
    sns.catplot(x="Sex",
                kind="count",
                data=titanic_df)
    plt.show()

def class_1():
    sns.catplot(x="Pclass",
                kind="count",
                data=titanic_df,)
    plt.show()

def survived_class():
    sns.catplot(data = titanic_df,
               x = "Survived",
               kind = "count",
               hue = "Pclass")
    plt.show()

def survived_sex():
    sns.catplot(data = titanic_df,
               x = "Survived",
               kind = "count",
               hue = "Sex")
    plt.show()

# if_survived()
# sex_1()
# class_1()
# survived_class()
# survived_sex()


def male_female_child(passenger):
    age, sex = passenger

    if age < 18:
        return 'child'
    else:
        return sex

titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child,axis=1)

# print(titanic_df[0:20])

def person_1():
    sns.catplot(x="person",
                kind="count",
                data=titanic_df)
    plt.show()

def survived_person():
    sns.catplot(data = titanic_df,
               x = "Survived",
               kind = "count",
               hue = "person")
    plt.show()


def class_person():
    sns.catplot(x='Pclass',
                kind ='count',
                hue ='person',
                data=titanic_df)
    plt.show()


# person_1()
# survived_person()
# class_person()


def age_1():
    sns.histplot(titanic_df["Age"], bins = 70)
    plt.show()

# age_1()
def mean():
    mean_all = titanic_df['Age'].mean()

    mean_if_survived = titanic_df[titanic_df["Survived"]=="Yes"]["Age"].mean()

# print(mean_all)
# print(mean_if_survived)

def survived_age():
    sns.histplot(titanic_df[titanic_df["Survived"]=="No"]["Age"], bins = 20)
    sns.histplot(titanic_df[titanic_df["Survived"]=="Yes"]["Age"], bins = 20)
    plt.show()

# survived_age()

def survived_adult():
    sns.histplot(titanic_df[titanic_df["person"]=="male"]["Age"], bins = 20)
    sns.histplot(titanic_df[titanic_df["person"]=="female"]["Age"], bins = 20)
    plt.show()

# survived_adult()


def tables():
    print(pd.pivot_table(titanic_df, index = 'Survived', columns = 'Pclass', values = 'Ticket' ,aggfunc ='count'))
    print()
    print(pd.pivot_table(titanic_df, index = 'Survived', columns = 'person', values = 'Ticket' ,aggfunc ='count'))
    print()
    print(pd.pivot_table(titanic_df, index = 'Survived', columns = 'Embarked', values = 'Ticket' ,aggfunc ='count'))
    print(pd.pivot_table(titanic_df, index = 'Pclass', columns = 'person', values = 'Ticket' ,aggfunc ='count'))

#INTERFEJS

import sys
arg = sys.argv
stop = False
while not stop:
    choice = int(input("Proszę wybrać cyfrę dla wskazanej czynnośći, która ma zostać wykonana:\n1. Wyświetl tabelę z danymi "
                   "pasażerów.\n2. Wyświetl wykres liczby ocalałych katastrofę.\n3. Wyświetl statystyki dotyczące płci "
                   "pasażerów.\n4. Wyświetl liczebę ocalałych w zależności od klasy biletu.\n5. Wyświetl liczbę ocalałych "
                   "w zależności od płci.\n6. Wyświetl rozkład wieku pasażerów i policz średnią wieku.\n7. Wyświetl wykres "
                   "liczebności pasażerów w zależności od wieku i czy ocaleli.\n8. Wyświetl wykres liczebności kobiet i "
                   "mężczyzn w zależności od wieku\n9. Przedstaw dane liczbowe ocalałych w zależności od klasy i płci.:\n"))


    if choice == 1:
        print(titanic_df)
    elif choice == 2:
        if_survived()
    elif choice == 3:
        sex_1()
        person_1()
    elif choice == 4:
        class_1()
        class_person()
    elif choice == 5:
        survived_sex()
        survived_person()
    elif choice == 6:
        age_1()
        mean()
    elif choice == 7:
        survived_age()
    elif choice == 8:
        survived_adult()
    elif choice == 9:
        tables()
    else:
        print("Wprowadzono błędnie wybór.")

    choice2 = input("Czy chcesz dokonać następnego wyboru? Wpisz 'tak' lub 'nie'.").lower()

    if choice2 == "nie":
        stop = True
        print("Dziękujęmy za skorzystanie z naszej analizy danych.")
