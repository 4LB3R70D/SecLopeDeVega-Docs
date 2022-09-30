.. index:: Engine Installation & Execution
    
.. _engine_installation:

Engine Installation & Execution
===============================

For intallting the **engine**, there are two options: 

* One is using the compiled version provided in the project under the *'bin'* folder of the  `engine repository <https://github.com/4LB3R70D/SecLopeDeVega-Engine>`_. 
  This is ready to run in **linux** operating systems for AMD64 cpu architecture.

* Or compiling the source code. This option is better if you want to run it in a different operating system (OS) or cpu architecture. 
  To do so, you should be aware that one of the libraries of this project ('zeromq/goczmq') is a wrapper of a C library, 
  so you have to have a C compiler for the operating system (OS) and cpu architecture installed too.


.. index:: Engine Compilation
  
Compiling the Project
---------------------
If you want to compile the project, the first thing you need is to install `GO <https://go.dev/doc/install>`_. 
As mentioned in the previous paragraph, you will need the C compiler in place for the OS and cpu architecture. 
**Go** allows compiling the project for several different architectures and operating systems, 
but the mentioned library can do the things a bit harder (especially when you compile the project for a different OS and CPU architecture of your machine).
If you have a message error like this at building time: 

.. code-block::

  build constraints exclude all Go files in ../go/pkg/mod/gopkg.in/zeromq/goczmq.v4@v4.X.X 

the cause may be the lack of the right C compiler in place.

For compiling the project, this `tutorial <https://www.digitalocean.com/community/tutorials/how-to-build-go-executables-for-multiple-platforms-on-ubuntu-16-04>`_ can be of interest to you,
but for this project you can do just the following (provided you are in the root folder of the project):

.. code-block::

  go build -o {{the place you want to put the executable file}} cmd/main.go 
 
or just ``make`` (or ``make build``)

For compiling to a different target system, you should check the following links:

* `When using CGO_ENABLED is must and what happens <https://stackoverflow.com/questions/61515186/when-using-cgo-enabled-is-must-and-what-happens>`_.

* `CGO_ENABLED=1 causing the '-marm' unrecognized #16801  <https://github.com/golang/go/issues/16801>`_.

* `cmd/go: give a better error message when building Go package with CGO_ENABLED=0  <https://github.com/golang/go/issues/24068>`_.

But in general, you should take into account that you might need to specify the flags ``CC``, ``CXX``, and ``CGO_ENABLED="1"``; 
apart from the ``GOOS`` and ``GOARCH`` as described in the tutorial cited previously. 

.. index:: Engine Location of Configuration Files

Location of Configuration Files
-------------------------------
The main configuration file for the **engine** is the *engine_config.yml*, and by default the engine tries to get it from ``./config`` (config folder in the folder where the executable file is located).
However, this can be changed using some command line options, as we are going to see in the next section.

The *conversation rules* folder location is described in that configuration file, so it is up to you. This topic is described in detail in :ref:`conversation_rules`

If you import this project in an IDE, the **engine** tries to get the configuration file from the config folder of the project. 
This is only possible if the ``env (environment)`` command line option is defined as ``DEV``.

.. index:: Engine Command Line Options

Launch Engine and Command Line Options
--------------------------------------
As mentioned, the **engine** can use `command line flags <https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option>`_ to start. 
The three command line optines are:

* ``-env`` (environment): It tells the **engine** if the it is running in an IDE ( ``DEV``) or not.

* ``-nobanner`` (no banner): If present, the banner will not be printed at the beginning of the execution.

* ``-config`` (config): If present, it change the default location of the configuration file *engine_config.yml*. 
  If this is provided, the ``env`` option will not be used. You can use a different name for that configuration file instead of the default one, 
  since the path is not the location (folder) of the file, is directly the file to be used as configuration file **(but always a .yml file)**.

The default and the alternative values are defined in the following table:

+----------------------+-----------------------+------------------------------------------------------------------+
| Command Line Option  | Default value         | Alternative values                                               |           
+======================+=======================+==================================================================+
|``env``               |``PRO``                | ``DEV``                                                          |
+----------------------+-----------------------+------------------------------------------------------------------+
|``nobanner``          |(not present)          |``nobanner`` (present)                                            |       
+----------------------+-----------------------+------------------------------------------------------------------+
|``config``            |(not present)          | ``/path/to/the/configuration/file/configuration_file_name.yml``  |        
+----------------------+-----------------------+------------------------------------------------------------------+

To start the execution of the **engine**, there are two options:

* If the software is not compiled, you can compile and run it by doing ``go run cmd/main.go`` or just ``make run`` 
  (provided that you have the environment ready for compilation as described in the previous section)

* If the software is compiled, just run it as any executable. An example using the already compile version in linux: 
  
  .. code-block::

    bin/slv_engine_linux_amd64

  or using the command line options:   
  
  .. code-block::

    bin/slv_engine_linux_amd64 -config=/home/alber/SecLopeDeVega/engine/config/engine_config.yml -nobanner

.. index:: Database Setup

Database Setup
---------------
The schema of the database to be used is already provided in the *db* folder in the  `repository <https://github.com/4LB3R70D/SecLopeDeVega-Engine>`_. 
If you do not know how to import it in your project, check this `guide <https://www.digitalocean.com/community/tutorials/how-to-import-and-export-databases-in-mysql-or-mariadb>`_.