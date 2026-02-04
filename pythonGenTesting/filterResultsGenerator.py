#######################################
cat1possibilities = ["null", "Natural resources, agriculture and related production", "Trades, transport and equipment operators and related occupations", "Occupations in education, law and social, community and government services", "Sales and service occupations", "Business, finance and administration occupations", "Occupations in education, law and social, community and government services"]
cat2possibilities = ["null", "Agriculture, forestry, fishing and hunting", "Mining, quarrying, and oil and gas extraction", "Transportation and warehousing", "Professional, scientific and technical services", "Other services (except public administration)", "Administrative and support, waste management and remediation service", "Health care and social assistance", "Accommodation and food services", "Public administration", "Arts, entertainment and recreation", "Retail trade", "Manufacturing", "Construction"]
cat3possibilities = ["null", "Women", "Men", "Immigrants", "Indigenous people", "Rural", "Urban", "20-39", "40-59", "60+", "Retired"]

for tag1 in cat1possibilities:
    for tag2 in cat2possibilities:
        for tag3 in cat3possibilities:
            with open(str(tag1) + str(tag2) + str(tag3) + ".md", "a+") as f:
                fullString = str(tag1) + "_" + str(tag2) + "_" + str(tag3)
                fixedString = fullString.replace(" ", "_")
                fixedString = fixedString.replace(",", "")
                fixedString = fixedString.replace("+", "")
                fixedString = fixedString.replace("(", "")
                fixedString = fixedString.replace(")", "")
                f.write("---\n")
                f.write("layout: peopleExploreResults\n")
                f.write("permalink: /explore/filterResults/" + fixedString + "\n")
                f.write("occupationtag: \"" + tag1 + "\"\n")
                f.write("industrytag: \"" + tag2 + "\"\n")
                f.write("demographicstag: \"" + tag3 + "\"\n")
                f.write("---\n")