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
interaction, therefore you do not need to declare them as you do for those you are going to use. In the following example you can see how this can be configured.

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
------------
We have already seen that one custom rule can trigger several async or hybrid custom rules as well. However, the 'OR' is missing, this means that
you may trigger this set of custom rules asynchronously, or this another set of them; depending on some conditions (memory variables and their values).
This provides flexibility to interact differently depending on the execution context, so alternative interactions now can take place. 

In order to configure that, you can follow the below example. Any 'case' of the 'switch' has to define the list of ``conditions`` that make it applicable, 
and the list of ``rules`` to trigger asynchronously when that happens. The 'switch' structure is made up of ``options`` (cases) and the ``dafault`` (when 
no option is applicable). However, the ``default`` one is optional.

.. code-block:: 

  any_custom_rule:

    # GENERAL FIELDS
    # ==============
    ...

    # ASYNC SWITCH 
    # ============
    # Switch for executing some async (or hybrid) rules depending 
    # on conditions. E.g., ff memory variable 'AAAA' has the value 
    # 'X' (value field), or it has the same content of the memory 
    # variable 'BBB', then execute the async Rule 'N'. In case no 
    # option fits, use the async rule of the default field (if present, 
    # and the list length is greater than 0)
    async_switch:

        options:
            # first option or 'case' wit a list of conditions to satisfy
            - conditions:
                # list of conditions
                - var_name: var1
                    value: 2
                    reference_variable: var2

                # if conditions are satisfied, then a set of async 
                # (or hybrid) rules to execute
              rules:
                - rule_id: 3
                  delay: 3

            # second option or 'case'
            - conditions:
                - var_name: var1
                    value: 2
                    reference_variable: var2
              rules:
                - rule_id: 3
                  delay: 3

        # other cases:
        #   Another case
        #   - conditions:...
        #     rules:...
        #
        #   and another one
        #   - conditions:...
        #     rules:...

        default:
        # set of async ruls to execute if no 'case' statement
        # is applicable
        - rule_id: 3
            delay: 3


    # OTHER FIELDS
    # ============
    # Other fields expalined in this documentation
    ...


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