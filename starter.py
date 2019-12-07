import log


def init():
    """
    Performs following init tasks
        - load question-map from disk
        - init stop words
    """
    log.log(f"Running init tasks", module="starter")


def end():
    """
    Performs the following end tasks
        - write question-segment map to disk

    """
    log.log(f" Running teardown tasks", module="starter")
