def page_rank(links, d=0.85, epsilon=0.01, max_iterations=100): 
    """
    Calculate the PageRank of each page using the PageRank algorithm.

    Parameters:
    - links: A dictionary where keys are page names and values are lists of pages they link to.
    - d: Damping factor.
    - epsilon: Convergence tolerance.
    - max_iterations: Maximum number of iterations to perform.

    Returns:
    - A dictionary containing the PageRank of each page.
    """
    
    # Step 1: Find out sinks and add outgoing links
    N = len(links)
    sinks = [page for page in links if not links[page]]
    for sink in sinks:
        links[sink] = [p for p in links if p != sink]

    #Step 2: Dampening factor was implemented on function call
    
    # Step 3: Initialize all ranks to be 1/N
    ranks = {page: 1/N for page in links}

    # Step 4: Calculate PageRank of each page
    for _ in range(max_iterations):
        new_ranks = {}
        total_sink_rank = sum(ranks[sink] for sink in sinks)
        
        for page in ranks:
            # Calculate sum of page ranks of incoming links
            rank_sum = 0
            for in_page in links:
                if page in links[in_page]:
                    rank_sum += ranks[in_page] / len(links[in_page])
            rank_sum += total_sink_rank / N  # Add sink rank distributed to all pages
            new_rank = (1 - d) / N + d * rank_sum
            
            new_ranks[page] = new_rank

        # Check convergence by summing the absolute rank changes
        if sum(abs(new_ranks[page] - ranks[page]) for page in ranks) < epsilon:
            ranks = new_ranks
            break
        ranks = new_ranks
    
    # Normalize the ranks so they sum up to 1
    normalization_factor = sum(ranks.values())
    for page in ranks:
        ranks[page] /= normalization_factor
    
    return ranks

# Diagram from the user's description
links = { #Used instead of a double array
    'A': [],
    'B': ['A', 'C'],
    'C': ['A'],
    'D': ['A']
}

# Calculate PageRank
page_ranks = page_rank(links)
print(f"Page Ranks:\n{page_ranks}\n")
