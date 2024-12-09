
#Use sudo docker run -it run final-first-project

#-it tag is -i keeps STDIN open, even if not attached.
#-t allocates a pseudo-TTY, which is necessary for interactive input.

import random

def firstProgram() :
    print ("Hello friend what's your name")
    name = input()
    if( name == '' ) :
        firstProgram()
    print(' Hey {name}  '.format( name = name ))

    print("\nWould you like to learn or take a quiz? \nTo learn, type 'L'. \nTo take a quiz, type 'Q'.\n")


    choice = input().lower()

    if( choice == 'l' ) :
        programMenu()
    elif (choice == 'q' ) :
        quizMenu()
    else :
        print ("Invalid input \n Please read and select properly")
        firstProgram()


def quizMenu () :
    print('select languages Number')
    print(' **** Select the number **** \n 1)Python \n 2)Js \n 3)C++ \n 4)C# \n 5) GO    ')
    n = input()
    
    if( n == '1' ) :
        pythonQuiz()
    elif (n == '2' ):
        jsQuiz()
    elif ( n =='3' ) :
        cppQuiz()
    elif ( n == '4' ) :
        csharpQuiz()
    elif ( n == '5' ) :
        goQuiz()
    else :
        print("Please read the menu")
        programMenu()


def programMenu( ):
    print('select languages Number')
    print(' **** Select the number **** \n 1)Python \n 2)Js \n 3)C++ \n 4)C# \n 5) GO    ')

    menuSelector()


def menuSelector ():
    
    n = input()

    if( n == '1' ) :
        pythonHistory()
    elif (n == '2' ):
        jsHistory()
    elif ( n =='3' ) :
        cppHistory()
    elif ( n == '4' ) :
        csharpHistory()
    elif ( n == '5' ) :
        goHistory()
    else :
        print("Please read the menu")
        programMenu()

def pythonHistory():
    print("\nPython History\n")
    print("Python was created by Guido van Rossum in the late 1980s and was first released in 1991.")
    print("It is an interpreted, high-level, and general-purpose programming language, emphasizing simplicity and readability.")
    print("Python is influenced by the ABC programming language and designed to support multiple paradigms, including procedural, object-oriented, and functional programming.")

    print("\nPython Applications\n")
    print("1. **Web Development**:")
    print("   - Python is widely used for building websites and web applications, thanks to frameworks like Django, Flask, and FastAPI.")
    print("   - It simplifies server-side programming, database interaction, and API creation.")
    print("2. **Data Science and Machine Learning**:")
    print("   - Python dominates data analysis and machine learning fields with libraries like Pandas, NumPy, TensorFlow, PyTorch, and Scikit-learn.")
    print("   - It is also popular in data visualization with tools like Matplotlib, Seaborn, and Plotly.")
    print("3. **Artificial Intelligence and Deep Learning**:")
    print("   - Python is used for developing AI applications like natural language processing, computer vision, and neural networks.")
    print("   - Libraries like Keras and OpenCV make it a go-to choice for AI researchers.")
    print("4. **Scientific Computing**:")
    print("   - Python is extensively used in scientific research for simulation, modeling, and analysis.")
    print("   - Tools like SciPy, SymPy, and Jupyter Notebooks enhance its capabilities.")
    print("5. **Game Development**:")
    print("   - Libraries like Pygame allow developers to build simple 2D games.")
    print("6. **Automation and Scripting**:")
    print("   - Python is ideal for automating repetitive tasks, such as file manipulation, web scraping (using libraries like BeautifulSoup and Selenium), and system administration.")
    print("7. **Embedded Systems and IoT**:")
    print("   - Python, particularly MicroPython, is used in small devices and Internet of Things (IoT) applications.")
    print("8. **Education**:")
    print("   - Python's simple syntax makes it an excellent choice for teaching programming to beginners.")
    
    print("\nPython Frameworks and Libraries\n")
    print("1. **Web Development Frameworks**:")
    print("   - **Django**: A full-stack framework that encourages rapid development and clean design.")
    print("   - **Flask**: A lightweight and flexible framework suitable for small and medium-sized applications.")
    print("   - **FastAPI**: Designed for building APIs quickly and efficiently, with modern Python features like type hints.")
    print("2. **Data Science Libraries**:")
    print("   - **Pandas**: For data manipulation and analysis.")
    print("   - **NumPy**: For numerical computations.")
    print("   - **Matplotlib/Seaborn**: For data visualization.")
    print("3. **Machine Learning and AI Libraries**:")
    print("   - **Scikit-learn**: For traditional machine learning algorithms.")
    print("   - **TensorFlow and PyTorch**: For deep learning and neural networks.")
    print("4. **Game Development**:")
    print("   - **Pygame**: For creating 2D games.")
    print("5. **Web Scraping**:")
    print("   - **BeautifulSoup**: For parsing HTML and XML documents.")
    print("   - **Selenium**: For automating web browser interactions.")
    print("6. **Scientific Computing**:")
    print("   - **SciPy**: For advanced scientific calculations.")
    print("   - **SymPy**: For symbolic mathematics.")
    print("7. **Automation Tools**:")
    print("   - **PyAutoGUI**: For automating mouse and keyboard tasks.")
    print("   - **Requests**: For HTTP requests and APIs.")

    print("\nPython's Ecosystem and Community\n")
    print("Python has a massive and supportive community that contributes to a rich ecosystem of libraries and frameworks.")
    print("It is open-source and regularly updated by the Python Software Foundation (PSF).")

    print("\nFuture of Python\n")
    print("Python continues to evolve with modern features, such as pattern matching, type hints, and performance improvements.")
    print("It remains one of the most popular programming languages due to its versatility and ease of use.")
    
    print('Do you want to take Python quiz? (y/n)')

    quiz = input().lower()
    if quiz == 'y':
       pythonQuiz()

    elif quiz == 'n':
        exitorConti()
    else:
        print("Invalid input, please enter 'y' or 'n'.")
        pythonHistory()


def jsHistory():
    print("\nJavaScript History\n")
    print("JavaScript was created by Brendan Eich in 1995 while working at Netscape Communications.")
    print("Initially developed in just 10 days, it was first named Mocha, then renamed LiveScript, and eventually became JavaScript.")
    print("It was intended to make web pages more interactive and dynamic, complementing the static nature of HTML and CSS.")
    print("JavaScript was standardized as ECMAScript in 1997 by ECMA International to ensure consistency across web browsers.")

    print("\nJavaScript Applications\n")
    print("1. **Web Development**:")
    print("   - JavaScript is a core technology of the web, alongside HTML and CSS, enabling dynamic and interactive user interfaces.")
    print("   - Frameworks like React, Angular, and Vue.js are popular for building modern web applications.")
    print("2. **Server-Side Development**:")
    print("   - JavaScript powers server-side applications with frameworks like Node.js, allowing developers to use the same language on both client and server.")
    print("   - Tools like Express.js simplify building APIs and backend services.")
    print("3. **Mobile App Development**:")
    print("   - JavaScript frameworks like React Native and Ionic enable cross-platform mobile app development.")
    print("4. **Game Development**:")
    print("   - Libraries like Phaser and Babylon.js make it possible to create 2D and 3D games directly in the browser.")
    print("5. **Desktop Application Development**:")
    print("   - Electron.js allows developers to create cross-platform desktop applications using JavaScript.")
    print("6. **Automation and Scripting**:")
    print("   - JavaScript can be used for browser automation, testing, and scripting tasks with tools like Puppeteer and Selenium.")
    print("7. **Internet of Things (IoT)**:")
    print("   - JavaScript is used in IoT projects with frameworks like Johnny-Five and Node-RED.")

    print("\nKey JavaScript Frameworks and Libraries\n")
    print("1. **Frontend Frameworks**:")
    print("   - **React**: A library for building user interfaces, developed by Facebook.")
    print("   - **Angular**: A full-featured framework for creating dynamic web applications, maintained by Google.")
    print("   - **Vue.js**: A progressive framework for building user interfaces, known for its simplicity and flexibility.")
    print("2. **Backend Frameworks**:")
    print("   - **Node.js**: A runtime environment for running JavaScript on the server side.")
    print("   - **Express.js**: A minimal and flexible web application framework built on Node.js.")
    print("3. **Game Development Libraries**:")
    print("   - **Phaser**: For creating 2D games.")
    print("   - **Babylon.js**: For creating 3D graphics and games.")
    print("4. **Testing Frameworks**:")
    print("   - **Jest**: For unit testing.")
    print("   - **Mocha**: For asynchronous testing.")
    print("5. **Visualization Libraries**:")
    print("   - **D3.js**: For creating interactive data visualizations.")
    print("   - **Three.js**: For 3D rendering and animations.")

    print("\nJavaScript Ecosystem and Community\n")
    print("JavaScript has a massive and active community, contributing to its robust ecosystem.")
    print("It is supported by modern browsers with powerful developer tools for debugging and optimization.")
    print("The npm (Node Package Manager) registry hosts millions of JavaScript packages, enabling developers to leverage a wide range of reusable modules.")

    print("\nFuture of JavaScript\n")
    print("JavaScript continues to evolve with features like ES6 modules, async/await, and optional chaining.")
    print("Its versatility ensures that it remains one of the most widely used programming languages for years to come.")

    
        
    print('Do you want to take JS quiz? (y/n)')

    quiz = input().lower()
    if quiz == 'y':
       jsQuiz()

    elif quiz == 'n':
        exitorConti()
    else:
        print("Invalid input, please enter 'y' or 'n'.")
        jsHistory()



def cppHistory():
    print("\nC++ History\n")
    print("C++ was created by Bjarne Stroustrup in 1979 at Bell Labs as an enhancement to the C programming language.")
    print("Initially called 'C with Classes,' it introduced object-oriented programming (OOP) concepts to C.")
    print("The first version of C++ was released in 1985, and it has undergone many updates, including:")
    print("  - The ISO C++98 standard in 1998.")
    print("  - C++11, which introduced modern features like lambdas, smart pointers, and multithreading support.")
    print("  - Subsequent updates like C++14, C++17, C++20, and the upcoming C++23, which continue to expand its capabilities.")
    print("C++ remains a powerful, versatile, and widely-used programming language.")

    print("\nKey Features of C++\n")
    print("1. **Object-Oriented Programming**: Classes, objects, inheritance, polymorphism, and encapsulation.")
    print("2. **Low-Level Memory Control**: Direct manipulation of memory using pointers, allowing high-performance programming.")
    print("3. **Standard Template Library (STL)**: Provides reusable templates for data structures (e.g., vectors, lists) and algorithms.")
    print("4. **Cross-Platform Compatibility**: Programs written in C++ can be compiled on multiple platforms.")
    print("5. **Performance**: Often chosen for applications requiring high-speed computation.")

    print("\nApplications of C++\n")
    print("1. **System Programming**:")
    print("   - Operating systems (e.g., parts of Windows, Linux kernel components).")
    print("   - Device drivers and embedded systems.")
    print("2. **Game Development**:")
    print("   - Game engines like Unreal Engine and Godot rely heavily on C++.")
    print("   - High performance and real-time computation make it ideal for game development.")
    print("3. **Software Development**:")
    print("   - Major software applications (e.g., Adobe Photoshop, Autodesk Maya).")
    print("   - Browsers like Mozilla Firefox and Google Chrome use C++ in their backends.")
    print("4. **Scientific Computing**:")
    print("   - Simulations and computational research due to its ability to handle complex mathematical calculations.")
    print("5. **Finance and Banking**:")
    print("   - High-frequency trading systems and financial modeling due to C++'s speed.")
    print("6. **Embedded Systems**:")
    print("   - Used in automotive systems, IoT devices, and robotics.")

    print("\nPopular C++ Frameworks and Libraries\n")
    print("1. **Qt**: For cross-platform GUI application development.")
    print("2. **Boost**: Provides portable libraries for multithreading, networking, and more.")
    print("3. **Eigen**: For linear algebra and matrix computations.")
    print("4. **OpenCV**: For computer vision and image processing.")
    print("5. **Poco**: For building networked applications.")

    print("\nC++ Community and Ecosystem\n")
    print("C++ has a vibrant global community of developers who contribute to open-source projects, forums, and standards development.")
    print("Modern tools like Visual Studio, CLion, and GCC/Clang compilers enhance the C++ development experience.")
    print("With continuous updates and a focus on performance and modern programming paradigms, C++ remains relevant for various domains.")

    print("\nFun Fact:\n")
    print("C++ influenced the creation of many modern programming languages, including Java, C#, and Rust.")

      
    print('Do you want to take C++ quiz? (y/n)')

    quiz = input().lower()
    if quiz == 'y':
       cppQuiz()

    elif quiz == 'n':
        exitorConti()
    else:
        print("Invalid input, please enter 'y' or 'n'.")
        cppHistory()


def hello () :
    print("Hello")

def csharpHistory():
    print("\nC# History\n")
    print("C# (pronounced 'C-Sharp') was developed by Microsoft under the leadership of Anders Hejlsberg and was first released in 2000 as part of the .NET framework.")
    print("It was designed to be a modern, general-purpose, and object-oriented programming language.")
    print("C# was heavily influenced by C++, Java, and Delphi, with an emphasis on simplicity, type safety, and productivity.")
    print("In 2002, C# was standardized by ECMA International (ECMA-334) and ISO (ISO/IEC 23270).")
    print("Over the years, it has undergone significant enhancements, with updates introducing features like generics, LINQ, async/await, and record types.")
    print("C# continues to be one of the primary languages for developing applications in the Microsoft ecosystem.")

    print("\nKey Features of C#\n")
    print("1. **Object-Oriented**: Supports encapsulation, inheritance, and polymorphism.")
    print("2. **Strongly Typed**: Ensures type safety and reduces runtime errors.")
    print("3. **Automatic Memory Management**: Uses garbage collection for managing memory allocation and deallocation.")
    print("4. **Rich Standard Library**: Provides extensive libraries for various tasks like file I/O, networking, and XML processing.")
    print("5. **Cross-Platform Development**: Supported by .NET Core and .NET 5/6, enabling the creation of applications that run on Windows, macOS, and Linux.")
    print("6. **Asynchronous Programming**: Provides native support for asynchronous programming with async and await keywords.")
    print("7. **Modern Language Features**: Includes features like pattern matching, records, tuples, nullable types, and more.")

    print("\nApplications of C#\n")
    print("1. **Enterprise Applications**:")
    print("   - Widely used for developing enterprise-grade applications, including CRM and ERP systems.")
    print("2. **Web Development**:")
    print("   - ASP.NET Core allows building high-performance, scalable web applications and APIs.")
    print("3. **Game Development**:")
    print("   - Unity, one of the most popular game engines, uses C# as its primary scripting language.")
    print("4. **Mobile Development**:")
    print("   - Xamarin, now part of .NET MAUI, enables cross-platform mobile application development.")
    print("5. **Desktop Applications**:")
    print("   - Windows Presentation Foundation (WPF) and Windows Forms are commonly used for creating GUI applications.")
    print("6. **Cloud Services**:")
    print("   - Azure integrations and tools for cloud-native application development.")
    print("7. **IoT and Embedded Systems**:")
    print("   - Leveraged in building IoT solutions using Azure IoT Hub and .NET libraries.")

    print("\nPopular C# Frameworks and Tools\n")
    print("1. **ASP.NET Core**: For web and API development.")
    print("2. **Entity Framework Core**: An ORM (Object-Relational Mapper) for database management.")
    print("3. **Blazor**: Enables building interactive web UIs using C# instead of JavaScript.")
    print("4. **Unity**: Game development engine using C# for scripting.")
    print("5. **Xamarin/.NET MAUI**: For cross-platform mobile application development.")
    print("6. **SignalR**: For real-time communication in web applications.")
    print("7. **NUnit/xUnit**: Popular testing frameworks for C# applications.")

    print("\nCommunity and Ecosystem\n")
    print("C# boasts a large and active developer community, with extensive support from Microsoft and open-source contributors.")
    print("The .NET ecosystem provides robust tools, libraries, and frameworks for a wide range of applications.")
    print("Modern IDEs like Visual Studio and Visual Studio Code offer excellent support for C# development.")
    print("With regular updates, C# remains a top choice for modern software development.")

    print("\nFun Fact:\n")
    print("C#'s name is derived from the musical notation where '#' means 'sharp,' symbolizing an evolution or step up from the C language.")

      
    print('Do you want to take C# quiz? (y/n)')

    quiz = input().lower()
    if quiz == 'y':
       csharpQuiz()

    elif quiz == 'n':
        exitorConti()
    else:
        print("Invalid input, please enter 'y' or 'n'.")
        csharpHistory()



def goHistory():
    print("\nGo (Golang) History\n")
    print("Go, also known as Golang, was created at Google in 2007 by Robert Griesemer, Rob Pike, and Ken Thompson.")
    print("The language was publicly released in 2009 as an open-source project.")
    print("Go was designed to overcome challenges in existing languages like C++ and Java, with a focus on simplicity, fast compilation, and scalability.")
    print("Its creators sought to create a language that is easy to learn, efficient, and capable of handling modern software development needs.")
    print("Today, Go is widely adopted for backend development, cloud computing, distributed systems, and high-performance applications.")

    print("\nKey Features of Go\n")
    print("1. **Simplicity**: Go has a clean syntax and avoids complex features like inheritance and annotations.")
    print("2. **Fast Compilation**: Go compiles quickly to machine code, making it suitable for large-scale systems.")
    print("3. **Concurrency**: Built-in support for concurrency through goroutines and channels makes it easy to write concurrent and parallel programs.")
    print("4. **Garbage Collection**: Automatic memory management simplifies programming and reduces errors.")
    print("5. **Cross-Platform**: Compiled binaries can run on different platforms without dependencies.")
    print("6. **Strong Standard Library**: Go provides a rich set of libraries for tasks like networking, cryptography, and web development.")

    print("\nApplications of Go\n")
    print("1. **Backend Development**:")
    print("   - Commonly used for building RESTful APIs, microservices, and web servers.")
    print("2. **Cloud Computing**:")
    print("   - A popular choice for cloud-native development and is widely used with platforms like Kubernetes and Docker.")
    print("3. **Distributed Systems**:")
    print("   - Go excels in building scalable, distributed systems due to its concurrency features.")
    print("4. **DevOps Tools**:")
    print("   - Many popular DevOps tools, such as Docker and Terraform, are built using Go.")
    print("5. **Command-Line Tools**:")
    print("   - Used to create robust and efficient CLI applications.")
    print("6. **Game Development**:")
    print("   - Although not as popular as other languages, Go is sometimes used for game development, especially for server-side logic.")

    print("\nPopular Go Frameworks and Tools\n")
    print("1. **Gin**: A lightweight and fast web framework for building APIs.")
    print("2. **Echo**: A high-performance, extensible web framework.")
    print("3. **Beego**: A comprehensive framework for rapid development of RESTful APIs, web applications, and backend services.")
    print("4. **Fiber**: Inspired by Express.js, Fiber is a web framework optimized for performance.")
    print("5. **Gorm**: An ORM library for database management.")
    print("6. **Cobra**: A library for creating powerful CLI applications.")
    print("7. **Chi**: A lightweight router for building HTTP services.")

    print("\nWhy Developers Love Go\n")
    print("1. **Efficiency**: Go combines the speed of C++ with the ease of modern programming languages.")
    print("2. **Concurrency**: Built-in goroutines make concurrent programming seamless.")
    print("3. **Community and Ecosystem**: An active and growing community, with excellent support and numerous open-source libraries.")
    print("4. **Scalability**: Ideal for projects that require scalability, like distributed systems and microservices.")
    print("5. **Simplicity**: The straightforward syntax and design philosophy reduce development time and errors.")

    print("\nFun Fact:\n")
    print("The Go mascot, a gopher, was created by Renée French and is widely recognized in the developer community.")

    
    print('Do you want to take Python quiz? (y/n)')

    quiz = input().lower()
    if quiz == 'y':
       goQuiz()

    elif quiz == 'n':
        exitorConti()
    else:
        print("Invalid input, please enter 'y' or 'n'.")
        goHistory()





def jsQuiz():
    correct = 0
    incorrect = 0
    
    # Question 1: JavaScript History
    print("1. Who created JavaScript?")
    print("a) Brendan Eich b) Tim Berners-Lee c) Mark Zuckerberg d) Steve Jobs")
    q1Ans = input()
    if q1Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1
    
    # Question 2: JavaScript Syntax
    print("\n2. Which of the following is the correct syntax for declaring a variable in JavaScript?")
    print("a) var x = 10; b) let x = 10; c) const x = 10; d) All of the above")
    q2Ans = input()
    if q2Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 3: JavaScript Data Types
    print("\n3. Which of the following is NOT a data type in JavaScript?")
    print("a) Number b) String c) Character d) Boolean")
    q3Ans = input()
    if q3Ans.lower() == 'c':
        correct += 1
    else:
        incorrect += 1
    
    # Question 4: JavaScript Functions
    print("\n4. How do you define a function in JavaScript?")
    print("a) function myFunc() {} b) def myFunc() {} c) func myFunc() {} d) function:myFunc() {}")
    q4Ans = input()
    if q4Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 5: JavaScript Comparison Operators
    print("\n5. Which operator is used to compare two values in JavaScript?")
    print("a) == b) === c) != d) Both a and b")
    q5Ans = input()
    if q5Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 6: JavaScript Arrow Functions
    print("\n6. Which syntax is used to define an arrow function in JavaScript?")
    print("a) function() => {} b) () => {} c) function() {} d) () => { return }")
    q6Ans = input()
    if q6Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    # Question 7: JavaScript Loops
    print("\n7. Which loop is used to iterate over the elements of an array in JavaScript?")
    print("a) for loop b) forEach() c) while loop d) All of the above")
    q7Ans = input()
    if q7Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 8: JavaScript Objects
    print("\n8. How do you access a property of an object in JavaScript?")
    print("a) object.property b) object[property] c) Both a and b d) None of the above")
    q8Ans = input()
    if q8Ans.lower() == 'c':
        correct += 1
    else:
        incorrect += 1

    # Question 9: JavaScript Arrays
    print("\n9. How do you add an element to the end of an array in JavaScript?")
    print("a) array.push() b) array.pop() c) array.shift() d) array.unshift()")
    q9Ans = input()
    if q9Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 10: JavaScript Promises
    print("\n10. What is a JavaScript Promise used for?")
    print("a) To handle asynchronous operations b) To define functions c) To loop over arrays d) To declare variables")
    q10Ans = input()
    if q10Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    print(f"\nTotal Correct: {correct}")
    print(f"Total Incorrect: {incorrect}")
    print(f"Your Score: {correct} out of 10")

def cppQuiz():
    correct = 0
    incorrect = 0
    
    # Question 1: C++ History
    print("1. Who created C++?")
    print("a) Dennis Ritchie b) Bjarne Stroustrup c) Ken Thompson d) Brian Kernighan")
    q1Ans = input()
    if q1Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1
    
    # Question 2: C++ Syntax
    print("\n2. What is the correct way to declare a pointer in C++?")
    print("a) pointer p; b) int *p; c) int p*; d) pointer *p;")
    q2Ans = input()
    if q2Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    # Question 3: C++ Functions
    print("\n3. How do you define a function in C++?")
    print("a) function myFunc() {} b) void myFunc() {} c) func myFunc() {} d) function:myFunc() {}")
    q3Ans = input()
    if q3Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1
    
    # Question 4: C++ Inheritance
    print("\n4. Which keyword is used to define inheritance in C++?")
    print("a) inherit b) extends c) public d) class")
    q4Ans = input()
    if q4Ans.lower() == 'c':
        correct += 1
    else:
        incorrect += 1

    # Question 5: C++ Classes
    print("\n5. How do you create a class in C++?")
    print("a) class MyClass {} b) MyClass class {} c) create class MyClass {} d) class:MyClass {}")
    q5Ans = input()
    if q5Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 6: C++ Constructors
    print("\n6. What is the purpose of a constructor in C++?")
    print("a) To initialize objects b) To perform calculations c) To handle errors d) To destroy objects")
    q6Ans = input()
    if q6Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 7: C++ Data Types
    print("\n7. Which of the following is NOT a valid data type in C++?")
    print("a) int b) float c) bool d) character")
    q7Ans = input()
    if q7Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 8: C++ Polymorphism
    print("\n8. Which of the following is an example of polymorphism in C++?")
    print("a) Function Overloading b) Operator Overloading c) Inheritance d) All of the above")
    q8Ans = input()
    if q8Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 9: C++ Arrays
    print("\n9. How do you declare an array in C++?")
    print("a) int[] arr; b) int arr[5]; c) arr(int, 5); d) array<int> arr;")
    q9Ans = input()
    if q9Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    # Question 10: C++ Smart Pointers
    print("\n10. Which of the following is used for memory management in C++?")
    print("a) Pointers b) Arrays c) Smart Pointers d) References")
    q10Ans = input()
    if q10Ans.lower() == 'c':
        correct += 1
    else:
        incorrect += 1

    print(f"\nTotal Correct: {correct}")
    print(f"Total Incorrect: {incorrect}")
    print(f"Your Score: {correct} out of 10")

def csharpQuiz():
    correct = 0
    incorrect = 0
    
    # Question 1: C# Basics
    print("1. Who developed C#?")
    print("a) Sun Microsystems b) Microsoft c) Google d) Apple")
    q1Ans = input()
    if q1Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1
    
    # Question 2: C# Syntax
    print("\n2. Which of the following is the correct syntax for defining a method in C#?")
    print("a) void myMethod() {} b) function myMethod() {} c) method myMethod() {} d) def myMethod() {}")
    q2Ans = input()
    if q2Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 3: C# Variables
    print("\n3. What is the default value of a boolean variable in C#?")
    print("a) true b) false c) 0 d) null")
    q3Ans = input()
    if q3Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1
    
    # Question 4: C# Inheritance
    print("\n4. Which keyword is used to create a derived class in C#?")
    print("a) inherits b) subclass c) : d) extends")
    q4Ans = input()
    if q4Ans.lower() == 'c':
        correct += 1
    else:
        incorrect += 1

    # Question 5: C# Arrays
    print("\n5. How do you declare an array in C#?")
    print("a) int[] arr; b) int arr[]; c) array<int> arr; d) arr<int> []")
    q5Ans = input()
    if q5Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 6: C# Constructors
    print("\n6. What is the purpose of a constructor in C#?")
    print("a) To create objects b) To initialize objects c) To delete objects d) To return a value")
    q6Ans = input()
    if q6Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    # Question 7: C# Interfaces
    print("\n7. How do you define an interface in C#?")
    print("a) class IMyInterface {} b) interface IMyInterface {} c) interface MyInterface {} d) class MyInterface {}")
    q7Ans = input()
    if q7Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    # Question 8: C# LINQ
    print("\n8. Which of the following is used for querying data in C#?")
    print("a) LINQ b) SQL c) Lambda d) API")
    q8Ans = input()
    if q8Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 9: C# Collections
    print("\n9. Which of the following is not a collection type in C#?")
    print("a) List b) Array c) Dictionary d) Tuple")
    q9Ans = input()
    if q9Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 10: C# Exception Handling
    print("\n10. Which of the following is used for exception handling in C#?")
    print("a) throw b) try-catch c) assert d) raise")
    q10Ans = input()
    if q10Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    print(f"\nTotal Correct: {correct}")
    print(f"Total Incorrect: {incorrect}")
    print(f"Your Score: {correct} out of 10")

def goQuiz():
    correct = 0
    incorrect = 0
    
    # Question 1: Go Basics
    print("1. Who developed Go programming language?")
    print("a) Dennis Ritchie b) Ken Thompson c) Robert Griesemer d) Bjarne Stroustrup")
    q1Ans = input()
    if q1Ans.lower() == 'c':
        correct += 1
    else:
        incorrect += 1
    
    # Question 2: Go Syntax
    print("\n2. Which of the following is the correct syntax for declaring a variable in Go?")
    print("a) var x int = 10 b) x := 10 c) var x = 10 d) All of the above")
    q2Ans = input()
    if q2Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 3: Go Concurrency
    print("\n3. What is used for concurrency in Go?")
    print("a) Threads b) Goroutines c) Promises d) Callbacks")
    q3Ans = input()
    if q3Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1
    
    # Question 4: Go Data Types
    print("\n4. What is the zero value of an int in Go?")
    print("a) 1 b) 0 c) null d) Undefined")
    q4Ans = input()
    if q4Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    # Question 5: Go Functions
    print("\n5. How do you declare a function in Go?")
    print("a) func myFunction() {} b) function myFunction() {} c) def myFunction() {} d) func myFunction[] {}")
    q5Ans = input()
    if q5Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 6: Go Arrays
    print("\n6. How do you define an array in Go?")
    print("a) var arr = [3]int{} b) var arr [3]int c) arr := [3]int{} d) All of the above")
    q6Ans = input()
    if q6Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 7: Go Interfaces
    print("\n7. How do you declare an interface in Go?")
    print("a) type MyInterface interface {} b) interface MyInterface {} c) interface: MyInterface {} d) type interface MyInterface {}")
    q7Ans = input()
    if q7Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 8: Go Pointers
    print("\n8. What is the purpose of a pointer in Go?")
    print("a) To store a memory address b) To store a function c) To store a value d) None of the above")
    q8Ans = input()
    if q8Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 9: Go Maps
    print("\n9. What is the correct syntax to declare a map in Go?")
    print("a) var m map[string]int b) map[string]int m c) m := map[string]int{} d) All of the above")
    q9Ans = input()
    if q9Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 10: Go Error Handling
    print("\n10. Which of the following is used for error handling in Go?")
    print("a) try-catch b) exception c) defer d) multiple return values")
    q10Ans = input()
    if q10Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    print(f"\nTotal Correct: {correct}")
    print(f"Total Incorrect: {incorrect}")
    print(f"Your Score: {correct} out of 10")

def pythonQuiz():
    correct = 0
    incorrect = 0
    
    # Question 1: Python History
    print("1. Who created Python?")
    print("a) Guido van Rossum b) James Gosling c) Dennis Ritchie d) Bjarne Stroustrup")
    q1Ans = input()
    if q1Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1
    
    # Question 2: Python Syntax
    print("\n2. Which of the following is the correct syntax for defining a function in Python?")
    print("a) def my_function(): b) function my_function() c) define my_function() d) func my_function()")
    q2Ans = input()
    if q2Ans.lower() == 'a':
        correct += 1
    else:
        incorrect += 1

    # Question 3: Python Data Types
    print("\n3. Which of the following is NOT a data type in Python?")
    print("a) int b) str c) float d) character")
    q3Ans = input()
    if q3Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1
    
    # Question 4: Python Loops
    print("\n4. Which of the following is used to iterate over a sequence in Python?")
    print("a) for loop b) while loop c) foreach loop d) Both a and b")
    q4Ans = input()
    if q4Ans.lower() == 'd':
        correct += 1
    else:
        incorrect += 1

    # Question 5: Python Variables
    print("\n5. How do you declare a variable in Python?")
    print("a) int x = 10 b) let x = 10 c) x = 10 d) var x = 10")
    q5Ans = input()
    if q5Ans.lower() == 'c':
        correct += 1
    else:
        incorrect += 1

    # Question 6: Python Collections
    print("\n6. Which data type is used to store key-value pairs in Python?")
    print("a) list b) tuple c) dictionary d) set")
    q6Ans = input()
    if q6Ans.lower() == 'c':
        correct += 1
    else:
        incorrect += 1

    # Question 7: Python Strings
    print("\n7. How do you write a multi-line string in Python?")
    print("a) ' ' b) \" \" c) ''' ''' or \"\"\" \"\"\" d) None of the above")
    q7Ans = input()
    if q7Ans.lower() == 'c':
        correct += 1
    else:
        incorrect += 1

    # Question 8: Python File Handling
    print("\n8. Which mode is used to open a file for writing in Python?")
    print("a) 'r' b) 'w' c) 'a' d) 'rw'")
    q8Ans = input()
    if q8Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    # Question 9: Python Libraries
    print("\n9. Which of the following libraries is used for data analysis in Python?")
    print("a) numpy b) pandas c) matplotlib d) scipy")
    q9Ans = input()
    if q9Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    # Question 10: Python Exceptions
    print("\n10. How do you handle exceptions in Python?")
    print("a) if...else b) try...except c) switch...case d) error handling block")
    q10Ans = input()
    if q10Ans.lower() == 'b':
        correct += 1
    else:
        incorrect += 1

    print(f"\nTotal Correct: {correct}")
    print(f"Total Incorrect: {incorrect}")
    print(f"Your Score: {correct} out of 10")


def exitorConti () :
    print(" \n Do you want to know more y/n ")
    yn = input()

    if (yn == 'y' ) :
        programMenu()
    elif ( yn == 'n' ) :
        print("Thank you for using the program. Goodbye!")
        return
    else :
        print( "Invalid selection" )
        exitorConti()

def exit() :
    exit(0)




firstProgram()

