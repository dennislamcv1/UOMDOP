'''
Hello! The code below should look familiar to you from the Module 3 Lab notebook. 
For details about the following functions, please refer to that notebook and
attempt to read through and understand this provided solutions.
'''

def get_years(publications):
    return [citation["Year"] for citation in publications[0]["Citations"]]

def get_total_cits(publications):
    return sum([int(pub["Total Citations"]) for pub in publications])

def count_citations_per_annum(publications, year):
    count = 0
    for publication in publications:
        for citation in publication["Citations"]:
            if citation["Year"] == year:
                count += citation["Count"]
    return count

def create_chart_data(publications, years, group=None):
    data = []
    for year in years:
        count = count_citations_per_annum(publications, year)
        if group:
            data.append({"year": year, "citations": count, "group": group})
        else:
            data.append({"year": year, "citations": count})
    return data