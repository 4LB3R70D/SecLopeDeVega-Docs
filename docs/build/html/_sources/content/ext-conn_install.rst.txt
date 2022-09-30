.. index:: External Connector Installation & Execution
    
.. _ext-conn_installation:

External Connector Installation & Execution
===========================================
Since this component is in Python, you should have Python 3 installed in the environment yo want to run it.
Additionally, OpenSSL is also required. ``libzmq3-dev`` is recommended in some cases, as explained in 
the `pyzmq repository <https://github.com/zeromq/pyzmq#building-and-installation>`_ ,if you want to install
the dependencies compiling from source.

To have everything ready, you should install the dependencies as usual for any Python project. 
We recommend to use virtual environments, but it is up to you how to install the dependencies. In case you do not know how to do it, 
just check the offical `Python documentation <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>`_.

Since a ``requirements.txt`` is provided, you just can install the dependencies doing this:

.. code-block::

  python3 -m pip install -r requirements.txt

In this `part of the official documentation <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#using-requirements-files/>`_
you can find more information about how to use the ``requirements.txt`` file.


.. index:: External Connector Location of Configuration Files

Location of Configuration Files
-------------------------------
The main configuration file for the **external connector** is the *ext_conn_config.ini*, and by default the engine tries to get it from folder where the *start.py* file is located).
However, this can be changed using some command line options, as we are going to see in the next section.


.. index:: External Connector Command Line Options

Launch External Connector and Command Line Options
--------------------------------------------------
The **external connector** can use `command line flags <https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option>`_ to start too. 
The four command line options are:

* ``--nobanner`` or ``-NB`` (no banner): If present, the banner will not be printed at the beginning of the execution.

* ``--config`` or ``-CFG`` (config): If present, it change the default location of the configuration file *ext_conn_config.ini*. 
  You can use a different name for that configuration file instead of the default one, since the path is not the location (folder) of the file, 
  is directly the file to be used as configuration file **(but always a .ini file)**.

* ``--ID`` or ``-ID`` (**External Connector** ID): The service account ID to use to authenticate against the **engine**

* ``--password`` or ``-PWD`` (**External Connector** password): The password of the service account ID to use to authenticate against the **engine**

The default and the alternative values are defined in the following table:

+--------------------------+-----------------------+----------------------------------------------------------------+
| Command Line Option      | Default value         | Alternative value                                              |           
+==========================+=======================+================================================================+
|``--nobanner`` or ``-NB`` |(not present)          |``nobanner`` (present)                                          |       
+--------------------------+-----------------------+----------------------------------------------------------------+
|``--config`` or ``-CFG``  |(not present)          | ``/path/to/the/configuration/file/configuration_file_name.ini``|        
+--------------------------+-----------------------+----------------------------------------------------------------+
|``--ID`` or ``-ID``       |(not present)          | ``any id``                                                     |        
+--------------------------+-----------------------+----------------------------------------------------------------+
|``--password`` or ``-PWD``|(not present)          | ``any password``                                               |
+--------------------------+-----------------------+----------------------------------------------------------------+

To start the execution of the **external connector**,  just run it as any python script. An example: 

.. code-block::

  python3 start.py

or using the command line options: 

.. code-block::

  python3 start.py -NB -ID=lope

.. note::

   Please, take into account that **external connectors** need to contact the **engine** to run. Otherwise, 
   they will stop the execution since they cannot get the *conversation rules*.