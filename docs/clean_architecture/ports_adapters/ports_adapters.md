# Ports and Adapter in Hexagon

### Ports

![ports](images/ports.png)


### Adapters

#### Driver

A driver adapter DOESN'T implement a driver port. This is a mistake 
lot of people does. A driver adapter is a software component outside 
the application that uses a driver port. The driver port is a dependency
of the driver adapter. 

Examples of driver adapters: a MVC web controller, a REST controller, 
an automated test framework, etc

#### Driven

A driven adapter implement a driven port


![main](images/main.gif)

### Hexagon

![layered_to_hexagon](images/layered_to_hexagon.png)

![hexagon](images/hexagon.png)

![hexagonal_archtiecture](images/hexagonal_archtiecture.png)

### Difference

![layered_architecture](images/layered.png)

![hexagon_architecture](images/v_hexagon.png)

![onion_architecture](images/onion.png)

#### Clean Architecture is Onion Architecture with more sensible naming

![clean_architecture](images/clean.png)