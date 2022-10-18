Potential Use Cases 
===================
In this section, we provide some ideas about in what use cases we think *Lope* might help you. Please, be aware the success of
implementing those potential use cases

.. index:: Server Mode Use Cases

Server Mode 
-----------
In this mode, *Lope* is waiting for third party connections to start interacting. The main use here is about being a honeypot, 
or a set of them by providing a more realistic experience. Since this software may emulate real scenarios, this could be used
as a fake training IT environment for some cases. Since all the generated activities are signed, you can prove that the things
happened in the interaction, have indeed happened. The following list is some use cases that we have identified that could be relevant:

* **Simple Honeypot**: Just create an interaction to be executed by an **external connector**, and wait to get the activities about what happens.

* **Complex Honeypot Scenario**: Create a set of **external connectors** working together, where what happens none of them is affecting
  how others react. You can start new ones dynamically by using your own code, or using the *fork* functionality.

* **Perform Security Tests in a Client by Sending Tests from the Server Side**: Sometimes, perform security test in client software is hard
  because it is not easy to send back some things to test the software (e.g.: input validation). *Lope* can help you in this by pretending to 
  be the corresponding server and send something to validate the client software. 

* **'Training Arena'**: As mentioned, since *Lope* may behave as a real system (or set of them), provided that you have worked the right interactions, 
  you might create an environment for 'training', and even to evaluate the performance more officially (activities are signed, do you remember?)


.. index:: Client Mode Use Cases

Client Mode 
-----------
This mode is more about checking if a running server software is working as expected, in the sense of security or quality. This can perform different tests
in different application protocols by having the right *conversation rules* for doing so. As you know, the activities results are tamper-proof, so you can 
attest how a server software status is (in terms of security, quality, or what ever.).

* **Navigation in Web Applications**: You can navigate in web applications to test how the software is working, and even to perform web-scrapping in the target
  websites with the right interactions. You can emulate user interactions at some extent, that allows you to test navigation and performance.

* **Testing APIs**: Similarly to the previous point, you can also work with APIs and verify their behavior. This cal help you to verify API contracts, and perform
  some dynamic testing to ensure the API is working as it should be.

* **Perform Security Tests**: If you can test any exposed software in terms of quality, you can do it in terms of security (provided that you have the right 
  *conversation files*). Since you can create new **external connectors** during the test dynamically, you can get information from other place and go on with the interaction
  (for instance, being able to pass single sign-on). TLS authentication is also supported, so you might test systems that require it as well. In case of application protocols
  where there are not other security tools able to work with that, this tool might help you to do security test because it tries to be as agnostic as possible from the application 
  protocols, but limited to TCP or UDP.

* **Perform Load and Stress Testing**: Considering that one **external connector** can perform several connections against a target (M), and you can have several external connectors 
  working in parallel (N); this means you can have M x N connections against a target performing interactions (that can be simple, or can be complex emulating real expected interaction).
  This can help you in checking if the software is able to support, and to what extent, the high load situations.

* **Perform Denial of Service Testing**: In the same way of thinking with the previous point, you can directly try to test if the software can support some denial of service attacks.
  Not only some that are based on brute force, even other that are more 'intelligent' or based on interactions (IDoS?).

* **Assist Other Testing Tools**: Since you can add your code to this tool, this allows you to mix *Lope* capabilities with other tools. *Lope* can work as a kind of orchestrator and 
  perform some tests, while other tools perform others. Each tool will generate their corresponding results independently, but *Lope* can get help in organizing a unified testing experience.
  A simple example could be that you need to pass a single sign-one, and provide the session cookie to another security tool to access the system.


