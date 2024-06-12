# RP2040 Development Workspace

This repository serves as a workspace for developing applications in C for the RP2040 microcontroller, specifically the Pico W board.
![board](resources/board.png)

This project aims to use Pico's SDK initially. After the basic usage and implementations, other languages such as MicroPython and frameworks (Zephyr, NuttX...) might be added.  

## Board Specifications
![pinout](resources/picow-pinout.svg)

## Getting Started with SDK Projects

To compile the code in this repository, follow these steps:

1. Clone the SDK repository and initialize its submodules
```
  git clone https://github.com/raspberrypi/pico-sdk.git
  cd pico-sdk
  git submodule update --init --recursive
```
2. Clone this repository to your local machine.
3. Navigate to the desired application folder.
4. Create the build output directory and navigate to it
```
  mkdir build
  cd build/
```
5. Run CMake to generate the build files.
```
  cmake -DPICO_SDK_PATH=/path/to/pico-sdk -DPICO_BOARD=pico_w ..
```
6. Build the application using either CMake or make.
```
  cmake --build .
```
or
```
  make
```
7. (Optional) Set the SDK path as enviroment variable
```
  export PICO_SDK_PATH=/path/to/pico-sdk
```

## SDK Application Structure

The repository is organized into separate application folders. Each folder represents a different application for the RP2040 microcontroller. 

Each application directory should look like:
```
project/ 
├── CMakeLists.txt
├── inc
│   ├── header1.h
│   └── header2.h
├── pico_sdk_import.cmake
└── src
    └── source.c

```

## Contributing

Contributions to this repository are welcome! If you have an application you'd like to add or improvements to existing applications, please submit a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).