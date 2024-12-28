import pandas as pd 

pd.DataFrame({'A': [1,2,3]})

#print(pd.DataFrame({'A':[10,2,3]}))


dates = pd.date_range("20130101", periods=6)

#print(dates)

dic = {
    'name': ["A","B","C"],
    'values': [10,20,30],
    'size': [4,6,9]
}

df = pd.DataFrame(dic)

#print(df)


df2 = pd.DataFrame(
    {
        "A":1.0,
        "B":pd.date_range("20130102", periods = 4),
        "C":pd.Series(1, index=list(range(4)), dtype="float32"),
        "D":np.array([3] *4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

df2.loc[:, ["D", "F"]]