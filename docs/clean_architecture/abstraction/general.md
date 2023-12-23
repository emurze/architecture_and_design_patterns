### Abstraction

* **Abstraction** is higher level of the classes that encapsulates all component logic.
* Abstraction can be an interface or a class

### Dependencies
      
#### Func( DI ) -> Class ( High-level Abstraction Class ) <- Low-level Instance

![high-level-modules](images/high-level-modules.png)

#### Func( DI ) -> Interface <- Low-level Class

![high-level-low-level-modules](images/high-level-low-level-modules.png)

### DDD

![ddd](images/ddd.png)

### Low-level modules 

* outer layer of clean architecture

### High-level modules

* inner layer of clean architecture
* Abstraction


### Entity is *Critical Business Data* + *Critical Business Rules*

* Entities are pure business and nothing else

* Entity is a small set of business rules operating on Critical Business Data.

* All that is required is that you bind the Critical Business Data and the Critical Business Rules together in a single
and separate software module named Entity.

### UseCase description of the way that an automated system is used that specify application-specific business rules

* UseCase specify application-specific business rules

* UseCase is a description of the way that an automated system is used

* Use cases contain the rules that specify how and when the Critical Business Rules
within the Entities are invoked

* Use cases do not describe how the system appears to the user.
Instead, they describe the application-specific rules that govern the interaction
between the users and the Entities.

* A use case is an object. It has one or more functions that implement the application-
specific business rules

  
### Value Object is critical business domain object that is uniquely identified by all data it holds; we usually make them *immutable*: 

![value_object](images/value_object.png)


### Entity patterns is critical business domain object that is uniquely identified by id

![entity](images/entity.png)


### Anemic model is model that can have behavior, but it saves it to the another module

In this example, Money is a Value Object representing a monetary amount. 
However, the BankAccount class is anemic because it primarily holds data and 
the behavior for deposit and withdrawal is in a separate BankService class.

![anemic_model_and_value_object](images/anemic_model_and_value_object.png)
