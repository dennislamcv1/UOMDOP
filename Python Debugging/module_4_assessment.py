# ── Section 2.1: List of keys ─────────────────────────────────────────────────

keys = list(publications[0].keys())
print(keys)


# ── Section 2.3: Total citation counts ────────────────────────────────────────

total_cits = sum(pub["Total Citations"] for pub in publications)
print(f"Total citations: {total_cits}")


# ── Section 3.2: Tag top 2 vs all others ──────────────────────────────────────
# The top 2 most cited are identified by Total Citations > 1000
# ("Recommender systems" = 1865, "Reputation systems" = 1130)

top_2_pubs = sorted(publications, key=lambda x: -x["Total Citations"])[:2]
top_2_titles = {pub["Title"] for pub in top_2_pubs}

for pub in publications:
    if pub["Title"] in top_2_titles:
        pub["Group"] = "top_02"
    else:
        pub["Group"] = "other"

keys.append("Group")


# ── Section 4.1: get_publication_citation_counts() ────────────────────────────

def get_publication_citation_counts(publications, max_pub_year, n_years=5):
    """Returns a list of dicts with citation counts for the first n_years full
    years after each publication's year of publication.

    Only publications published on or before max_pub_year are evaluated.
    Counting starts the year AFTER publication (to ensure complete years only).

    Parameters:
        publications (list): nested list of publications
        max_pub_year (int): latest publication year to be evaluated
        n_years (int): number of years to include in the interval

    Returns:
        list: list of dictionaries
    """
    result = []
    for pub in publications:
        pub_year = pub["Publication Year"]
        if pub_year > max_pub_year:
            continue

        start_year = pub_year + 1           # first complete year after publication
        end_year = start_year + n_years - 1 # inclusive end year

        cit_total = sum(
            cit["Count"]
            for cit in pub["Citations"]
            if start_year <= cit["Year"] <= end_year
        )

        result.append({
            "title": pub["Title"],
            "pub_year": pub_year,
            "interval": f"{start_year}-{end_year}",
            "citations": cit_total,
        })

    return result


# ── Section 4.2: First five years ─────────────────────────────────────────────

cits_first_5_yrs = get_publication_citation_counts(publications, 2018, 5)

# Sort: citations DESC, pub_year DESC, title ASC
cits_first_5_yrs.sort(key=lambda x: (-x["citations"], -x["pub_year"], x["title"]))

for item in cits_first_5_yrs[:5]:
    print(item)


# ── Section 4.4: Write to file ────────────────────────────────────────────────

output_path = parent_path.joinpath("data", "stu-resnick-citations-first_5_yrs.json")
with open(output_path, "w", encoding="utf-8") as file_obj:
    json.dump(cits_first_5_yrs, file_obj, indent=2)

print(f"Written: {output_path}")


# ── Section 5.1: get_citation_change_rates() ──────────────────────────────────

def get_citation_change_rates(citations):
    """Calculate year-over-year rate of change in citation counts, starting
    from the first year a citation is recorded.

    rate_of_change = (current - previous) / previous

    Returns an empty list if no citations have been recorded yet.

    Parameters:
        citations (list): list of dicts with 'Year' and 'Count' keys

    Returns:
        list: year-over-year rates of change (floats)
    """
    # Find the index of the first year with a citation
    first_cit_idx = None
    for i, cit in enumerate(citations):
        if cit["Count"] > 0:
            first_cit_idx = i
            break

    if first_cit_idx is None:
        return []  # no citations recorded

    rates = []
    for i in range(first_cit_idx + 1, len(citations)):
        current = citations[i]["Count"]
        previous = citations[i - 1]["Count"]
        if previous == 0:
            # Skip zero-division; a jump from 0 is not meaningful as a rate
            continue
        rates.append((current - previous) / previous)

    return rates


# ── Section 5.2: calc_avg_citation_change_rate() ──────────────────────────────

def calc_avg_citation_change_rate(publication):
    """Compute the average year-over-year citation count rate of change for a
    publication by delegating to get_citation_change_rates().

    Returns 0 if no citations have been recorded.

    Parameters:
        publication (dict): a publication dictionary

    Returns:
        float: average rate of change
    """
    rates = get_citation_change_rates(publication["Citations"])
    if not rates:
        return 0
    return sum(rates) / len(rates)


# ── Section 5.3: Top 5 by average citation change rate ────────────────────────

for pub in publications:
    pub["Citations Avg Change Rate"] = calc_avg_citation_change_rate(pub)

publications.sort(key=lambda x: (-x["Citations Avg Change Rate"], x["Title"]))

top_5_avg_cits = publications[:5]

for pub in top_5_avg_cits:
    print(
        f"\n{pub['Title']} ({pub['Publication Year']}):\n"
        f"Average year-over-year citation count rate of change: "
        f"{round(pub['Citations Avg Change Rate'], 3)}"
    )


# ── Section 5.5: Write to file ────────────────────────────────────────────────

output_path = parent_path.joinpath("data", "stu-resnick-citations-top_05_avg_change_rate.json")
with open(output_path, "w", encoding="utf-8") as file_obj:
    json.dump(top_5_avg_cits, file_obj, indent=2)

print(f"Written: {output_path}")
