def calculate_love_score(name1, name2):
    count_true = 0
    count_love = 0

    count_true += name1.lower().count("t")
    count_true += name1.lower().count("r")
    count_true += name1.lower().count("u")
    count_true += name1.lower().count("e")

    count_true += name2.lower().count("t")
    count_true += name2.lower().count("r")
    count_true += name2.lower().count("u")
    count_true += name2.lower().count("e")

    count_love += name1.lower().count("l")
    count_love += name1.lower().count("o")
    count_love += name1.lower().count("v")
    count_love += name1.lower().count("e")

    count_love += name2.lower().count("l")
    count_love += name2.lower().count("o")
    count_love += name2.lower().count("v")
    count_love += name2.lower().count("e")

    print(f"{count_true}{count_love}")


calculate_love_score("Kanye West", "Kim Kardashian")
