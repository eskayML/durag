Contributing
============

Development Setup
-----------------

.. code-block:: bash

   git clone https://github.com/eskayML/durag.git
   cd durag
   uv venv
   uv pip install -e ".[dev,test,local]"

Running Tests
-------------

.. code-block:: bash

   python -m pytest tests/ -q

Building Docs
-------------

.. code-block:: bash

   cd docs
   make html
