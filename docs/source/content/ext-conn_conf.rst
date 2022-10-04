.. index:: External Connector Configuration

.. _external_connector_configuration:

External Connector Configuration 
=================================
The main configuration file of the **external connector** is the *ext_conn_config.ini* file, but the name can be changed if the configuration file is passed 
as command line option (as explained in :ref:`ext-conn_installation`). Just keep in mind that the file should be always a `ini <https://en.wikipedia.org/wiki/INI_file>`_ file.
In this file you can configure those aspects that are relevant for only the **external connector** such as how to connect with the **engine**, the use of certificates for TLS support,
the logs, different times, the connection with the Redis server (its role is explained in :ref:`architecture`), and other operation configuration.

Engine Connection
-----------------
The first thing you have to configure is where to find the engine:

.. code-block:: 

    # ==========================================================================
    [NETWORKING]
    # ==========================================================================
    # ZEROMQ
    # IP or domain
    ENGINE_IP = 127.0.0.1
    ENGINE_PORT = 5555

.. index:: External Connector Logging

External Connector Logging
--------------------------
The next interesting section to configure is the logs of the **external connector**. In the same way that the **engine** can generate logs, there are several possibilities:

* **Console logging:** The logs are only showed via the terminal.

* **File logging:** The logs are saved in a single file. 

* **Console & file logging:** Logs are saved in a file, as well as shown via console.

* **File logging with log rotation:** In this case, the logs are `rotated <https://en.wikipedia.org/wiki/Log_rotation>`_ in several files depending on the configuration parameters.

* **Console & file with log rotation:** Logs are saved in several files as described in the previous point, as well as shown via console.

The created log files have the following name structure: ``slv_ext_conn_%Y_%m_%d-%H_%M_%S.log`` (example: ``slv_ext_conn_2022_09_21-08_29_11.log``). But the prefix and file extension can be 
changed in the configuration file. If the specified log folder does not exist, it will be created.

.. code-block:: 

    # ==========================================================================
    [LOGGING]
    # ==========================================================================
    # LEVEL: one of the following: DEBUG, INFO (default), WARNING, ERROR, CRITICAL
    LEVEL = DEBUG 
    # LOG_Folder: not include the final '/', for local folder use '.' 
    # It creates the the folder if it does not exist
    LOG_FOLDER = ./logs
    # LOG_MODE: CONSOLE (default), FILE, FILE_ROTATION, BOTH, BOTH_ROTATION
    LOG_MODE =  CONSOLE 
    # Log rotation parameters, by default the max size is 20 MB and 5 files
    LOG_ROTATION_MAX_SIZE = 20
    LOG_ROTATION_FILE_NUMBERS = 5
    # Log file name utils. if not used, LOG_PREFIX = "slv_ext_conn_" and LOG_EXTENSION = ".log"
    LOG_PREFIX =  
    LOG_EXTENSION =  

.. index:: External Connector Timing

External Connector Timing
-------------------------
For the **external connector**, timing is an important aspect. Depending on the context, the different values should be adapted.

.. code-block:: 

    # ==========================================================================
    [TIMES]
    # ==========================================================================
    # Timeout for the connection with the engine
    # 5s by default
    ENGINE_TIME_OUT = 5

    # Timeout (seconds) for the external connector (lifespan), 
    # 'NONE' for not using a timeout
    # by default = 1 hour = 3600 seconds
    EXT_CONNECTOR_TIME_OUT = NONE

    # Time (seconds) for main thread operation loop without contacting 
    # the engine in case if there is not
    # information to send to the engine. By default = 5 seconds. 
    # If this value is less than the
    # ENGINE_TIME_OUT, then this last value is used 
    # for the loop waiting time
    MAIN_THREAD_CHECKING_TIME = 5

    # Time (float-seconds) between loops when the external connector 
    # wait for interaction The default value is 0.5 seconds
    TIME_BETWEEN_INTERACTION_LOOPS = 0.5

    # Time (float seconds) between loops for the async thread. 
    # The default value us 0.1 seconds
    TIME_BETWEEN_ASYNC_LOOPS = 0.10

    # Number of async loops to clean the connection register. 
    # It results in a time value depending on 
    # the time between async loops
    NUMBER_ASYNC_LOOPS_TO_CLEAN_CONN_REGISTER = 10000

    # Waiting time (int-seconds) before restarting 
    # the external connector according to 'restart' order
    RESTARTING_WAITING_TIME = 60

    # Time (float-seconds) between connections of 
    # client sockets during starting-up (by deafult = 0.5s)
    TIME_BETWEEN_CLIENT_SOCKET_CONNECTIONS = 0.5

    # Time (float-seconds) between closing a tcp connection 
    # and connecting again for tcp client mode (by deafult = 0.5s)
    # Or initial delay for having enough time to do the 
    # TLS handhsake in the reconnection
    TIME_BETWEEN_CLIENT_SOCKET_CLOSE_CONNECT = 1

    # Time (float-seconds) before allowing the async tasks in 
    # client mode checks if no active connections are alive (by deafult = 3s)
    # Recommended: 5s or more for several TLS or DTLS connections. 
    TIME_INITIAL_DELAY_ASYNC_THREAD = 5  

.. index:: External Connector Operation

External Connector Operation
----------------------------
The following parameters cover other operational aspects of the **external connector**. The first two are the credentials to authenticate the
**external connector** against the **engine**, but if other values will replace them if they are provided via command line options, as described 
in :ref:`ext-conn_installation`. The third one is for being used to authenticate the **engine** against the **external connector**, as mentioned
in :ref:`engine_installation`.

The last two parameters allow to find the custom code that you can add to customize even further the interaction. This is described in detail in
:ref:`custom_functions`.
    
.. code-block::
    
    # ==========================================================================
    [OPERATION]
    # ==========================================================================

    # external connector ID, by default is autogenerated (AUTO, or empty)
    EXTERNAL_CONNECTOR_ID = ExtConTest

    # API key for connecting with the engine
    EXTERNAL_CONNECTOR_SECRET = 3sT0_3S_s3Cr3t0

    # For the hash code sent to external connectors from 
    # the engine as authentication proof
    ENGINE_AUTH_CODE = Y0_s0y_0zym4nd14s_r3y_d3_r3y3s

    # Custom functions directory. The software is going to 
    # look for a python module called with the given name 
    # ('slv_custom_functions[.py]' in this case). If it is not found, 
    # no custom functions will be executed. Please do not 
    # add the extension .py in the name
    CUSTOM_FUNCTIONS_DIRECTORY = ../custom_functions/
    CUSTOM_FUNCTIONS_MODULE_NAME = slv_custom_functions

.. index:: TLS/DTLS Support

TLS/DTLS Support
----------------
In case the **external connector** needs to use TLS for **tcp**, or DTLS for **udp**, this will be the place 
for configuring it. The support of TLS includes the client authentication, as well as the case the private key is encrypted;
but always using material created as `OpenSSL <https://www.openssl.org/>`_ does.

It is important to mention that for the DTLS case and if the private key is protected, a temporary file will created with the 
unencrypted key for the exection and deleted once the execution ends.

The following links can help you to configure the TLS or DTLS correctly for the **external connector**:

* `TLS support in Python offical documentation <https://docs.python.org/3/library/ssl.html>`_.

* `OpenSSL tutorial from Jamie Nguyen <https://jamielinux.com/docs/openssl-certificate-authority/create-the-root-pair.html>`_.

* `Certificate chains in Python offical documentation <https://docs.python.org/3/library/ssl.html#certificate-chains>`_.

* `OpenSSL cheat sheet from Cédric Lauradoux <https://ensiwiki.ensimag.fr/images/b/b3/Cheat.pdf>`_.

* `Problems using TLS in Python (ssl.SSLCertVerificationError) <https://stackoverflow.com/questions/52855924/problems-using-paho-mqtt-client-with-python-3-7>`_.

* `Working with OpenSSL and DNS alternative names <https://two-oes.medium.com/working-with-openssl-and-dns-alternative-names-367f06a23841>`_.

* `Key usage extensions and extended key usage <https://help.hcltechsw.com/domino/11.0.0/conf_keyusageextensionsandextendedkeyusage_r.html>`_.

* `How to create an HTTPS certificate for localhost domains <https://gist.github.com/cecilemuller/9492b848eb8fe46d462abeb26656c4f8>`_.


.. code-block:: 

    # ==========================================================================
    [D/TLS]
    # ==========================================================================
    # https://docs.python.org/3/library/ssl.html#module-ssl 

    # Custom CA:
    # - in server mode, it is the CA for validating client certificates
    # - in client mode, it is the CA for validating the server certificate if default
    #   settings are not used
    CLIENT_CABUNDLE_PEM = ../tls/ca/certs/ca.crt.pem

    # Is the key of the certificate to use protected with a password? YES (default) / NO
    KEY_PROTECTED = YES

    # ---------------------
    # TLS SERVER MODE
    # ---------------------
    # https://docs.python.org/3/library/ssl.html#server-side-operation
    SERVER_CERTCHAIN_PEM = ../tls/ca/intermediate/certs/ca-chain_server.crt.pem
    SERVER_PRIV_KEY_PEM = ../tls/ca/intermediate/private/seclopedevega_server.key.pem
    SERVER_KEY_PASSWORD = lope

    # ---------------------
    # TLS CLIENT MODE
    # ---------------------
    # https://docs.python.org/3/library/ssl.html#client-side-operation
    # Use Machine CAs: YES (default) / NO
    CLIENT_DEFAULT_SETTINGS = NO
    # Validate Server certificate: YES (default) / NO
    CLIENT_VALIDATE_SERVER_CERTIFICATE = YES
    CLIENT_CERTCHAIN_PEM = ../tls/ca/intermediate/certs/ca-chain_client.crt.pem
    CLIENT_PRIV_KEY_PEM = ../tls/ca/intermediate/private/seclopedevega_client.key.pem
    CLIENT_KEY_PASSWORD = lope

    # ---------------------
    # DTLS MODE
    # ---------------------
    #https://github.com/mcfreis/pydtls
    # One of the following: "DTLS" or "DTLSv1.2" (default)
    DTLS_VERSION = DTLSv1.2

.. index:: Redis Integration

Redis Integration
-----------------
As described in :ref:`architecture`, the `Redis <https://redis.io/>`_ server is an important element for allowing to share information among different **external connectors**, 
using memory variables. These variables are explained in detail in :ref:`session_support_and_memory_variables`, here we only address what is the configuration
capabilities to use Redis.

he following links can help you to install and use Redis, as well as understaning the integration between the external connector and Redis:

* `How to Use Redis With Python <https://realpython.com/python-redis/>`_.

* `How To Install and Secure Redis on Ubuntu 20.04 <https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04>`_.

* `Redis TLS support <https://redis.io/topics/encryption>`_.

* `Redis-py TLS Connection Examples <https://redis-py.readthedocs.io/en/stable/examples/ssl_connection_examples.html?highlight=ssl>`_.


.. code-block:: 

    # ==========================================================================
    [REDIS] # Multi external connector memory
    # ==========================================================================
    # IP or domain 
    REDIS_IP = 127.0.0.1

    REDIS_PORT = 6379 

    REDIS_PASSWORD = 3st33s3lB4uLD3L4sV4r14Bl3sC0mP4Rt1D4s

    REDIS_TLS = NO

    # use certificate for autenticate against the redis server?
    REDIS_USE_CLIENT_CERTIFICATE = YES
    REDIS_CLIENT_CERTIFICATE = ../tls/ca/intermediate/certs/ca-chain_client.crt.pem

    # Private Key fields for the certificate
    REDIS_PRIV_KEY_CLIENT_PROTECTED = YES
    REDIS_PRIV_KEY_PASSWORD =  lope
    REDIS_PRIV_KEY_CLIENT = ../tls/ca/intermediate/private/seclopedevega_client.key.pem
    
    # Machine CAs in linux: /etc/ssl/certs/ca-certificates.crt
    REDIS_CA_CERT = ../tls/ca/certs/ca.crt.pem

