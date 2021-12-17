########## build image ##########
FROM python:3.8-buster AS builder

ARG DEV_DEPENDENCIES_FLAG
ENV DEV_DEPENDENCIES_FLAG=${DEV_DEPENDENCIES_FLAG}
## add and install requirements
ENV PIPENV_VENV_IN_PROJECT=1
RUN pip install pipenv
WORKDIR /opt
COPY ./Pipfile .
COPY ./Pipfile.lock .
# --dev is temporary because currently production code uses helpers from the tests to generate data
RUN pipenv sync $DEV_DEPENDENCIES_FLAG

########## motion detection image ##########
FROM python:3.8-slim-buster AS runtime-image
ARG CI_COMMIT_TAG
ARG CI_COMMIT_SHA

ENV CI_COMMIT_TAG=$CI_COMMIT_TAG
ENV CI_COMMIT_SHA=$CI_COMMIT_SHA

## add user motion_detection
RUN addgroup --system motion_detection && adduser --system --no-create-home --group motion_detection

COPY --chown=motion_detection:motion_detection ./motion_detection /opt/motion_detection/motion_detection
# this is temporary because currently production code uses helpers from the tests to generate data
COPY --chown=motion_detection:motion_detection ./tests /opt/motion_detection/tests

COPY --chown=motion_detection:motion_detection --from=builder /opt/.venv /opt/.venv
RUN chown -R motion_detection:motion_detection /opt/motion_detection && chmod -R 755 /opt/motion_detection

## virtualenv
ENV VIRTUAL_ENV=/opt/.venv
#RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## switch to non-root user motion_detection
USER motion_detection
WORKDIR /opt/motion_detection

## run motion detection
CMD ["python3", "-m" , "motion_detection"]
