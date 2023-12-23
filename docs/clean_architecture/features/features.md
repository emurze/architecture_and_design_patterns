# Features

### Dataclass

* Type Container

* Boilerplate Reduction

### Pydantic

* Type Container

* Validation and Serialization


### \__hash__ and \__eq__ always specify explicitly

* Entity should have hashable ref or id

* Value Object should have hash for entire data (frozen=True or something else) 

* When you retrieve values from a dictionary or set using a key, Python first computes the hash value of the key using the __hash__ method.

* If there are hash collisions (different keys with the same hash value), Python uses the __eq__ method to verify the actual equality of the keys and retrieves the correct value.

* Inconsistent hashing and equality can lead to situations where the wrong value is retrieved or stored in hash-based collections.
