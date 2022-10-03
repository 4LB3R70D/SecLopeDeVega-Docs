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

    # MEMORY UPDATE & CONDITIONS
    # ==========================
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

    # MEMORY UPDATE & CONDITIONS
    # ==========================
    memory:
        # new values for some memory variables.
        # In case or a reference variable is present then 
        # the updating process uses the value of the 
        # reference memory variable, the value is omitted
        updates:
          # One memory variable is updated
          - var_name: var2
            value: test2

          # Another memory variable is updated
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
            - regex: [any regex]
              # Memory variable to save the captured information
              mem_var_name: var2
              # Is the regex in base64 format?
              regex_b64: no # yes/no (default)


    # OTHER FIELDS
    # ============
    # Other fields expalined in this documentation
    ...

You can use memory variables of different scopes for doing the update. For instance, you can update a 
connection level memory variable using a global level memory variable. In case the reference memory variable
is in 'collision' with others that have the same name, the one with the more limited scope will be used 
(in the same way that we have seen about how to add a memory variable in a response).

.. index:: Custom Rule Conditional Execution

Custom Rule Conditional Execution
---------------------------------
One of the potential uses of the memory variables is to modify the behavior of the execution, according to
different values they may have. This is done similarly than the update process of memory variables.
This means that the custom rule is only executed if the memory conditions are satisfied, after being considered
as applicable. Therefore, in this case, there are two steps of allowing the execution of the rule:
  
* Being applicable synchronous or asynchronously

* Having the memory conditions satisfied


.. code-block:: 

  any_custom_rule:

    # GENERAL FIELDS
    # ==============
    ...

    # MEMORY UPDATE & CONDITIONS
    # ==========================
    memory:
        # conditions to satisfy for executing the rule.
        # In case or a reference variable is present,
        # then the comparison is if the value of the memory variable
        #  is the same of the reference memory variable.
        # In case the 'value' field and the 'reference_variable' are present, 
        # only the 'reference_variable' field
        # is used
        conditions:
          # var2 == 'test'?
          - var_name: var2
            value: test2

          # var1 == var2?
          - var_name: var1
            value: 2 # This value is not used!
            reference_variable: var2 # This is used for comparison 

    # OTHER FIELDS
    # ============
    # Other fields expalined in this documentation
    ...

You can add as many conditions as you wish, all of them will be evaluated to allow the rule execution.
Similarly to the update process, you can compare memory variables of different scopes. For instance, 
you can compare a connection level memory variable using a multi external connector level memory variable. 
In case of the reference memory variable is in 'collision' with others that have the same name, the one with 
the more limited scope will be used (in the same way that we have seen about how to add a memory variable in 
a response).

.. index:: Built-in Functions

Built-in Functions
------------------
You can do some operations using the memory variables to allow you to control more how the interaction takes place.
Every custom rule can call a built-in memory operation, where you define what are the input values to use and what
memory variables will save the output. 

The reserved word ``EXT_IN`` allow you to use the external input (message received 
from the third party) as input of the operation. You can use memory variables and fixed values as inputs as well.
For the output, you need to specify what memory variables will save the results of the operations (if they are not provided, 
the results are lost). Please, be also aware that the order of the list of inputs or outputs is important for the correct 
use of the operation.

In case you need to do more than one of memory operations, we recommend using a set of async rules as a set of steps,
where each of them is calling a memory operation. The reason to enforce one memory operation per conversation rule is 
for the sake of performance: Using async rules that are called in a sequential order, avoid blocking 
the interaction with one rule.


.. code-block:: 

  any_custom_rule:

    # GENERAL FIELDS
    # ==============
    ...

    # BUILT-IN MEMORY OPERATIONS
    # ==========================
    builtin_memory_operation:

      # built-in memory operation enable for this rule?
      enable: yes # yes/no(default)

      # Operation to execute
      operation: STR_CONCAT

      # List of inputs
      # EXT_IN = 'EXTERNAL INPUT'
      input:
        - EXT_IN
        - var1
        - 3

      # List of memory variables
      # to save the results
      output:
        - var3
        - var4


    # OTHER FIELDS
    # ============
    # Other fields expalined in this documentation
    ...

There are other reserved words that you can use as input for the memory operations:

* ``IP``: the ip of the connection

* ``PORT``: the port of the connection

* ``SESSION_KEY``: the session key of the connection

* ``SESSION_VALUE``: the session value of the connection

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