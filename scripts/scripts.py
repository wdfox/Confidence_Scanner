
"""Functions designed to collect all data starting with a single search term/database pairing"""

import base
import urls
import data

def collect_papers(paper_count, search_term):
    """Collects a given number of papers related to a given term

    Parameters
    ----------
    paper_count : str
        Number of papers to be collected and saved
    search_term : str
        Papers returned will be associated with this term

    Notes
    -----
    - Currently this function overwrites the existing file every time it runs - Must fix
    - Perhaps worth checking if a paper with a given ID is already in saved data? Or just scrape new file every time?
    """

    # Build search URL
    search = urls.build_search(search_term, retmax=paper_count)
    # Get associated IDs
    ids = urls.get_ids(search)

    # Create a list of paper objects to be saved
    papers = [base.Paper(id) for id in ids]

    # Initialize an index to be used in saving the papers
    i = 0

    # Extract the desired info from each paper and save to JSON
    for paper in papers:
        paper.scrape_data()
        outfile = data.assign_outfile(i)
        data.save('Papers', search_term, paper, outfile)

        # Increment the index to save the next paper
        i += 1


def collect_prs(pr_count, db_url="https://www.nih.gov/news-events/news-releases"):
    """Collects a given number of press releases related to a given term

    Parameters
    ----------
    pr_count : str
        Number of press releases to be collected and saved
    db_url : str
        Base URL from which to begin the search for individual press release links (preset to NIH db)

    Notes
    -----
    - Currently this function overwrites the existing file every time it runs
    """

    # Retrieve press release URLS
    pr_links = urls.crawl(db_url)

    # Create a list of press release objects to be saved
    prs = []
    for link in pr_links:
        if len(prs) < pr_count:
            prs.append(base.Press_Release(db_url+link))

    # Initialize an index to be used in saving the papers
    i = 0

    # Extract the desired info from each press release and save to JSON
    for pr in prs:
        pr.scrape_data()
        outfile = data.assign_outfile(i)
        data.save('PRs', db_url, pr, outfile)