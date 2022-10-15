.. index:: Quick Start

.. _quick_start:

Quick Start
===========
*Lope* comes with example interaction ready to show the capabilities it provides. In order to 'play' with *Lope*, first you have to decide if you want to compile the **engine**, 
or just using the compiled version for linux x64. In any case, take a look at the instructions described in :ref:`engine_installation`. For the **external connector**,
yo need to install Python 3, as the corresponding libraries as explained in :ref:`ext-conn_installation`.

*Lope* is configured to run this example interaction by default, working as a server in the port 8888. The interaction that will execute is the one described in the ``cr_test_neo-yml``. 
The version 2 is almost the same, it only use different concersation rules files, instead of using only one file. The approach is a kind of self-guided tutorial where you can just add
simple inputs (e.g. ``x1x``, ``x2x``, ``y1y``, ``n1n``, etc.) to see what happens. To do that, you have first to prepare the environment and, once everything is ready, then you have to start the **engine** first.
Take a look at the logs to see if you have the following message:

``Engine up and running, ready to receive messages of external connectors!``

This means the **engine** has started correctly. Then, you have to start the **external connector** and review the logs. If everything is ok, then you should see something like this:

``[InteractionWrkr][22-10-15][09:57:34][INFO]: Listening the socket in the port: 8888``

Then, you can interact with *Lope*, our recommendation is using `ncat <https://nmap.org/ncat/>`_ and do the following:

``ncat 127.0.0.1 8888`` (provided *Lope* is running in your local machine).

Just navigate in the *conversation rules* file and check the options you have and then, add the right input to see the effects. Additionally, you have other two example interactions the test client and the server. 
You can start an **external connector** as client (providing the id: ``ExtConTest_Client`` ) and another as server (providing the id: ``ExtConTest_Server``), and then, the client **external connector** will interact
with the server one. For this test, you will need to have the Redis server in place, and we recommend to use `wireshark <https://www.wireshark.org/>`_ to see what is happening in the interaction (port 8080). In any test, 
please review the configuration files to check if everything is correct anyway.


