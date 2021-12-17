import logging


def get_logger(name=__name__, level=logging.DEBUG):
    logging.basicConfig(
        format=(
            "%(asctime)s %(module)15s %(name)20s [pid: "
            "%(process)d] %(levelname)s %(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
        level=level,
    )
    return logging.getLogger(name)
