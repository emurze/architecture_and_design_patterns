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

* outer layer

### High-level modules

* inner layer
* Abstraction

### High level concepts should not depend on Low-level conepts by architecture circle

* Because use cases are specificBecause use cases are specific

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

  
### Value Object pattern is any domain object that is uniquely identified by the data it holds; we usually make them *immutable*: 

* An order line is uniquely identified by its order ID, SKU, and quantity; if we change one of those values, we now have a new line. 
That’s the definition of a value object: any object that is identified only by its data and doesn’t have a long-lived identity

![value_object](images/value_object.png)

### Entity patterns is any domain object that is uniquely identified by the id

* If we change Entity then get Entity

![entity](images/entity.png)
