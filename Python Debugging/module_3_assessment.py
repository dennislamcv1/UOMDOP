# ── Section 2.0: Split faculty_data into headers + rows ───────────────────────

faculty_headers = faculty_data[0]   # ['Last Name', 'First Name']
faculty = faculty_data[1:]          # remaining rows: [['Adar', 'Eytan'], ...]


# ── Section 3.0: has_faculty_coauthor() ───────────────────────────────────────

def has_faculty_coauthor(publication, author, faculty):
    """
    Returns True if the publication's 'Authors' string contains at least one
    UMSI faculty member other than < author >.

    Parameters:
        publication (dict): A dictionary representing a single publication.
        author (str): Author to exclude from the search (e.g. "Resnick, Paul").
        faculty (list): List of [last_name, first_name] rows from the faculty CSV.

    Returns:
        bool: True if a faculty coauthor (other than author) is found, else False.
    """
    # Split into individual author strings and strip whitespace
    pub_authors = [a.strip() for a in publication["Authors"].split(";")]
    for coauthor in pub_authors:
        # Skip the excluded author
        if coauthor.lower() == author.lower():
            continue
        # Check if this coauthor is a UMSI faculty member (exact match)
        for row in faculty:
            faculty_name = f"{row[0]}, {row[1]}"
            if coauthor.lower() == faculty_name.lower():
                return True
    return False


# ── Section 4.0: Tag each publication with a "Group" key ──────────────────────

for pub in publications:
    if has_faculty_coauthor(pub, RESNICK_PAUL, faculty):
        pub["Group"] = "UMSI coauthors"
    else:
        pub["Group"] = "No UMSI coauthors"


# ── Section 5.0: get_group() ──────────────────────────────────────────────────

def get_group(publications, name):
    """
    Filters publications by the value of the 'Group' key.

    Parameters:
        publications (list): List of publication dictionaries.
        name (str): Group name to filter on (e.g. "UMSI coauthors").

    Returns:
        list: Publications whose 'Group' matches name.
    """
    return [pub for pub in publications if pub["Group"] == name]


# ── Section 6.1: Chart data – all publications ────────────────────────────────

chrt_all_cits = lab.create_chart_data(publications, years)


# ── Section 6.2: Chart data – UMSI coauthored ────────────────────────────────

umsi_coauth_pubs = get_group(publications, "UMSI coauthors")
chrt_umsi_coauth_cits = lab.create_chart_data(umsi_coauth_pubs, years, "UMSI coauthors")


# ── Section 6.3: Chart data – non-UMSI coauthored ────────────────────────────

non_umsi_coauth_pubs = get_group(publications, "No UMSI coauthors")
chrt_non_umsi_coauth_cits = lab.create_chart_data(non_umsi_coauth_pubs, years, "No UMSI coauthors")


# ── Section 8.1: Publications 2007–2023 ───────────────────────────────────────

pubs_2007_2023 = [
    pub for pub in publications
    if 2007 <= pub["Publication Year"] <= 2023
]

umsi_coauth_pubs_2007_2023 = [
    pub for pub in umsi_coauth_pubs
    if 2007 <= pub["Publication Year"] <= 2023
]

non_umsi_coauth_pubs_2007_2023 = [
    pub for pub in non_umsi_coauth_pubs
    if 2007 <= pub["Publication Year"] <= 2023
]


# ── Section 8.2: Publication group percentages 2007–2023 ─────────────────────

umsi_coauth_2007_2023_pct = round(
    len(umsi_coauth_pubs_2007_2023) / len(pubs_2007_2023) * 100, 2
)

non_umsi_coauth_2007_2023_pct = round(
    len(non_umsi_coauth_pubs_2007_2023) / len(pubs_2007_2023) * 100, 2
)

print(f"UMSI coauthored pubs: {umsi_coauth_2007_2023_pct}%")
print(f"Non-UMSI coauthored pubs: {non_umsi_coauth_2007_2023_pct}%")


# ── Section 8.3: Citation counts 2007–2023 ───────────────────────────────────
# lab.count_citations_per_annum(publications, year) returns total citations
# across all supplied publications for a given year.

years_2007_2023 = [yr for yr in years if 2007 <= yr <= 2023]

total_cits_2007_2023 = sum(
    lab.count_citations_per_annum(pubs_2007_2023, yr)
    for yr in years_2007_2023
)

total_umsi_coauth_cits_2007_2023 = sum(
    lab.count_citations_per_annum(umsi_coauth_pubs_2007_2023, yr)
    for yr in years_2007_2023
)

total_non_umsi_coauth_cits_2007_2023 = sum(
    lab.count_citations_per_annum(non_umsi_coauth_pubs_2007_2023, yr)
    for yr in years_2007_2023
)

print(f"Total citations 2007-2023: {total_cits_2007_2023}")
print(f"UMSI coauthor citations:   {total_umsi_coauth_cits_2007_2023}")
print(f"Non-UMSI citations:        {total_non_umsi_coauth_cits_2007_2023}")


# ── Section 8.4: Citation count percentages 2007–2023 ────────────────────────

total_umsi_coauth_cits_2007_2023_pct = round(
    total_umsi_coauth_cits_2007_2023 / total_cits_2007_2023 * 100, 2
)

total_non_umsi_coauth_cits_2007_2023_pct = round(
    total_non_umsi_coauth_cits_2007_2023 / total_cits_2007_2023 * 100, 2
)

print(f"UMSI coauthor citation share:     {total_umsi_coauth_cits_2007_2023_pct}%")
print(f"Non-UMSI coauthor citation share: {total_non_umsi_coauth_cits_2007_2023_pct}%")


# ── Section 9.0: Chart data 2007–2023 ────────────────────────────────────────

chrt_all_cits_2007_2023 = lab.create_chart_data(pubs_2007_2023, years)
chrt_umsi_coauth_cits_2007_2023 = lab.create_chart_data(umsi_coauth_pubs_2007_2023, years, "UMSI coauthors")
chrt_non_umsi_coauth_cits_2007_2023 = lab.create_chart_data(non_umsi_coauth_pubs_2007_2023, years, "No UMSI coauthors")


# ── Section 11.0: Write UMSI coauthored publications to JSON ──────────────────

output_filepath = "./data/stu-resnick-citations-umsi_coauthors.json"
with open(output_filepath, "w", encoding="utf-8") as file_obj:
    json.dump(umsi_coauth_pubs, file_obj, indent=2)

print(f"File written: {output_filepath}")
