from invoke import task


def _black(context, check=False):
    with_check = check and "--check" or ""
    context.run(
        f"black . {with_check}",
        shell="/bin/sh",
    )


def _flake8(context):
    context.run(
        "flake8 .",
        shell="/bin/sh",
    )


def _mypy(context):
    context.run(
        "mypy . --python-version 3.8",
        shell="/bin/sh",
    )


@task
def check_format(context):
    format(context, check=True)


@task
def format(context, check=False):
    _black(context, check)


@task
def lint(context):
    _flake8(context)
    _mypy(context)


@task
def coverage(context):
    context.run("coverage html", shell="/bin/sh")


@task
def test(context):
    context.run(
        "pytest --cov=motion_detection --junit-xml=test-report.xml tests/",
        shell="/bin/sh",
    )


@task
def compose_up(context):
    context.run("docker-compose up --detach", shell="/bin/sh")


@task
def compose_down(context):
    context.run("docker-compose down", shell="/bin/sh")


@task
def compose_destroy(context):
    context.run("docker-compose down --volumes", shell="/bin/sh")


@task
def motion_detection(context):
    context.run("python -m motion_detection", shell="/bin/sh")
