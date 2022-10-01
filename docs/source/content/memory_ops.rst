.. index:: Memory Operations

.. _memory_operations:

Memory Operations
=================
Having memory variables is great, but using them is even better. In this section of the documentation we are going 
to see how you can work with them.

.. index:: Memory Modifications Using Rules

Memory Modifications Using Rules
--------------------------------
The first use of the memory variables is that any custom rule can change the value of those variables. This can be done
via directly changing the value, or by using the information received from the third party systems.

.. rubric:: Direct Memory Variable Update

The direct change of the memory variables needs first to decide 'when' this is going to happen, either in the 'rule detection' step 
(when the rule is considered as applicable to be executed), or in the 'rule execution' step (when the rule is executed and the response 
is sent, if there is any).  This is configured in in the ``operation`` section:

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

    # MEMORY VARIABLES
    # ================
    # # One of the following: "rule_detected", "rule_executed"(default). 
    # (Before session update and custom functions)
    memory_update_when: rule_executed 

    # To enable the use of Redis server to share memory 
    # variables between external connectors
    memory_variables_multi_ext_connector_enable: yes # yes/no(default) 

    # To overwrite exisisting memory variables in Redis 
    # during the initialization phase
    multi_ext_connector_memory_overwrite_during_init: yes # yes/no(default) 

    # OTHER TOPICS
    # ============
    # Additional aspects should be defined here, but 
    # they will be described in the respective sections
    # of this documentation, for the sake of clarity
    ...

And the memory variable update should be defined under the ``memory`` field, and ``update`` subfield of the custom rule.
Several memory variables can be updated at onces since you define a list of them to be updated.
The updating process can use a fixed (hardcoded) value, or another memory variable. In this second case,
the content of the reference memory variable is copied into the memory variable to update. In case both options are present
(fixed value and reference memory variable), the fixed value case is omitted.

.. code-block:: 

  any_custom_rule:

    # GENERAL FIELDS
    # ==============
    ...

    # SOCKET CLOSE SCENARIOS
    # ======================
    ...

    # SESSION UPDATE FIELDS
    # =====================
    ...

    # MEMORY OPERATIONS
    # =====================
    memory:
        # new values for some memory variables.
        # In case or a reference variable is present then 
        # the updating process uses the value of the 
        # reference memory variable, the value is omitted
        updates:
          # One memory variable is updated
          - var_name: var2
            value: test2

          # Anether memory variable is updated
          - var_name: var1
            value: 2 # This value is not used!
            reference_variable: var2 # This is used to update 
                                     # the memory variable

    # OTHER FIELDS
    # ============
    # Other fields expalined in this documentation
    ...

.. index:: Memory Modifications Using Captured Data

.. rubric:: Memory Modifications Using Captured Data

The memory variables can be updated via capturing specific information from the messages
that are received from the third parties. This allows to save specific set of information
in a memory variable. This only can be done in the sync or hybrid custom conversation rules, 
and it uses RegEx as well:

.. code-block:: 

  any_custom_rule:

    # GENERAL FIELDS
    # ==============
    ...

    # SOCKET CLOSE SCENARIOS
    # ======================
    ...

    # SESSION UPDATE FIELDS
    # =====================
    ...

    # CAPTURING INFORMATION
    # =====================
    capturing_data:
          enable: yes # yes/no(default)

          # list of different information to capture
          captures:

              # RegEx to capture the information
            - regex: [any regex]
              # Memory variable to save the captured information
              mem_var_name: var1 
              # Is the regex in base64 format?
              regex_b64: no # yes/no (default)

              # RegEx to capture the information
            - regex: capturing_[any regex]
              # Memory variable to save the captured information
              mem_var_name: var2
              # Is the regex in base64 format?
              regex_b64: no # yes/no (default)


    # OTHER FIELDS
    # ============
    # Other fields expalined in this documentation
    ...


.. index:: Custom Rule Conditional Execution

Custom Rule Conditional Execution
---------------------------------



.. index:: Built-in Functions

Built-in Functions
------------------

.. rubric:: String Operations



.. rubric:: Number Operations



.. rubric:: Boolean Operations



.. index:: Custom Functions

Custom Functions
----------------

.. rubric:: Importing Your Own Code


.. rubric:: Custom Pre-processor Function


.. rubric:: Custom Post-processor Function


.. rubric:: Custom Functions in Custom Rules