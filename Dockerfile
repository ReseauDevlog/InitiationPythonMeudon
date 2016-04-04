FROM andrewosh/binder-base

USER main

ADD environment.yml /home/main/

RUN conda env create -f environment.yml
RUN /bin/bash -c "source activate synope && ipython kernelspec install-self --user"
RUN pip install notebook
RUN pip install pypandoc
RUN mkdir $HOME/.jupyter
RUN ipython profile create
RUN git clone https://github.com/damianavila/RISE.git
RUN cd RISE; python setup.py install
ADD session-2016-03-idf/styles/custom.css /home/main/.ipython/profile_default/static/custom/
