
import pandas as pd


def f1():
    df = pd.read_csv("../graduate_data/topCategory.csv")
    df["id:ID"] = df["id"]
    df[":LABEL"] = "TopCategory"
    df = df.loc[:, ["id:ID", "name", ":LABEL"]]
    df.to_csv("topCategory.csv", index=False)
    print(df)


def f2():
    df = pd.read_csv("../graduate_data/subCategory.csv")
    df["id:ID"] = df["id"]
    df[":LABEL"] = "SubCategory"
    df = df.loc[:, ["id:ID", "name", ":LABEL"]]
    df.to_csv("subCategory.csv", index=False)
    print(df)


def top_sub():
    df = pd.read_csv("../graduate_data/subCategory.csv")
    # :START_ID,:END_ID,:TYPE
    df[":START_ID"] = df["parent_id"]
    df[":END_ID"] = df["id"]
    df[":TYPE"] = "hasSub"
    df = df.loc[:, [":START_ID", ":END_ID", ":TYPE"]]
    df.to_csv("top_sub.csv", index=False)


def f3():
    df = pd.read_csv("../graduate_data/thirdCategory.csv")
    df["id:ID"] = df["id"]
    df[":LABEL"] = "ThirdCategory"
    df = df.loc[:, ["id:ID", "name", ":LABEL"]]
    df.to_csv("ThirdCategory.csv", index=False)
    print(df)


def sub_third():
    df = pd.read_csv("../graduate_data/thirdCategory.csv")
    # :START_ID,:END_ID,:TYPE
    df[":START_ID"] = df["parent_id"]
    df[":END_ID"] = df["id"]
    df[":TYPE"] = "hasSub"
    df = df.loc[:, [":START_ID", ":END_ID", ":TYPE"]]
    df.to_csv("sub_third.csv", index=False)


def f4():
    df = pd.read_csv("../graduate_data/lastCategory.csv")
    df["code:ID"] = "code" + df["code"]
    df[":LABEL"] = "LastCategory"
    df = df.loc[:, ["code:ID", "name", "link", ":LABEL"]]
    df.to_csv("LastCategory.csv", index=False)


def third_last():
    df = pd.read_csv("../graduate_data/lastCategory.csv")
    # :START_ID,:END_ID,:TYPE
    df[":START_ID"] = df["parent_id"]
    df[":END_ID"] = "code" + df["code"]
    df[":TYPE"] = "hasSub"
    df = df.loc[:, [":START_ID", ":END_ID", ":TYPE"]]
    df.to_csv("third_last.csv", index=False)


def college():
    df = pd.read_csv("../graduate_data/college.csv", encoding="gbk")
    df["name:ID"] = df["name"]
    df[":LABEL"] = "College"
    df = df.loc[:, ["name:ID", "place", "attachment", "has_graduate_institute", "is_self_score", "adjustment", "announcement", "regulations", ":LABEL"]]
    df.to_csv("college.csv", index=False)


def major_college():
    df = pd.read_csv("../graduate_data/graduateMajorSchool.csv")
    data = []
    headers = [":START_ID", ":END_ID", ":TYPE"]
    for index, row in df.iterrows():
        code = "code" + row["parent_code"]
        rlist = eval(row["college"])
        for item in rlist:
            data.append([code, item, "belongTo"])
    print(len(data))

    df2 = pd.DataFrame(data, columns=headers)
    print(df2.head())
    df2.to_csv("major_college.csv", index=False)

third_last()