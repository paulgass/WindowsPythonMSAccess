FROM quay.agilesof.com/brandi/brandi-python-ubi:v0.0.2
USER root
COPY * /opt/app-root/src/
COPY app /opt/app-root/src/app
COPY .venv /opt/app-root/src/app/.venv
RUN chmod -R +w ${APP_ROOT} && \
    chmod -R g=u ${APP_ROOT} 
USER 100
