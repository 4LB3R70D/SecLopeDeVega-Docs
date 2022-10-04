.. index:: Advance Conversation Rules

.. _advance_conversation_rules:

Advance Conversation Rules
==========================
In this chapter, we are going to see more advance options that are available for the use of the conversation rules to provide more tools
for defining more complete scenarios, or just easy the use of *Lope* to operators. 


.. index:: Conditional External Connector Execution

Conditional External Connector Execution
----------------------------------------
This feature allows the **external connector** to wait for certain conditions before starting to interact with third parties. This feature needs the use of multi external 
connector memory varibales, because the **external connector** starts its execution but it does not interact directly with third parties. It will wait until some conditions
are satisfied (memory variables in Redis have the right values), before starting any interaction. We can say that the **external connector** is 'sleeping' until the right
time to 'wake up'. 

In order to use this functionality, you have to configure it in the ``operation`` section of the conversation rules. It can get the IP and port for the execution from some 
memory variables as well, so as to start the execution using dynamic data. The memory variables used for the conditions can be different for those declared to be used in the 
interaction, therefore you do not need to declare them as you do for those you are going to use. In the following example you can see how this can be configured

.. code-block:: 

  # -----------------------------------------------------------
  # Operational parameters of the interation 
  # and connection with third parties
  # -----------------------------------------------------------
  operation:

    # GENERAL ASPECTS
    # ===============
    ...

    # TO ENABLE TLS/DTLS USE
    # ======================
    ...

    # SOCKET CONNECTION CLOSE
    # =======================
    ...

    # SESSION SUPPORT
    # ===============
    ...

    # CONDITIONAL EXT CONN EXECUTION
    # ==============================
    conditional_execution:
        # use conditional execution in this execution?
        enable: no # yes/no(default)

        # list of conditions: memory values and the value
        conditions:
            # One condition
            - var_name: order_66
                value: True

            # Another condition
            - var_name: order_67
                value: False

        # If present, the ip value will be 
        # gathered from this memory variable
        mem_var_ip: var1 
        
        # If present, the port value will be 
        # gathered from this memory variable
        mem_var_port: var2

    # OTHER TOPICS
    # ============
    # Additional aspects should be defined here, but 
    # they will be described in the respective sections
    # of this documentation, for the sake of clarity
    ...

.. index:: Async Switch

Async Switch
------------------------------------



.. index:: Async Loop

Async Loop
----------



.. index:: External Connector Fork

External Connector Fork
-----------------------



.. index:: Conversation Rules Groups

Conversation Rules Groups
-------------------------



.. index:: Multiple Conversation Rules Files

Multiple Conversation Rules Files
---------------------------------