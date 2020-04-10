# Merge SQL insert file to one big SQL insert file
#   hierarchy of the models needs to be respected!


table_list = ["treatment", "auction", "group", "user", "player", "voucher", "period", "player_stats",
              "phase", "penalty", "offer", "question", "option_mc", "player_questions", "player_question_options",
            "page", "voucherre", "distribution"]
debug = False

with open("complete.sql", "w") as result:
    for i, table in enumerate(table_list):
        filename = "dauction2_public_dAuction2_" + table + ".sql"
        with open(filename, "r") as source:
            print(table, str(i+1) + "/" + str(len(table_list)))
            # problem with some files, newline is not the end of SQL command -> end must be ; !
            content = source.read().replace("\n", "").replace(";", ";\n")
            if debug and table == "treatment":
                print(content)
            result.write(content)
