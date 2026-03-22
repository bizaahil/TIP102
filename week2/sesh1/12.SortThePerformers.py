def sort_performers(performer_names, performance_times):
    """
    :type performer_names: List[str]
    :type performance_times: List[int]
    :rtype: List[str]
    """


    combined = list(zip(performer_names, performance_times))

    combined.sort