# RP2040 Development Workspace

This repository serves as a workspace for developing applications in C for the RP2040 microcontroller, specifically the Pico W board.
![board](resources/board.png)

## Getting Started

To compile the code in this repository, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the desired application folder.
3. Create the build output directory
```
  mkdir build
```
3. Run CMake to generate the build files.
```
  cmake -DPICO_SDK_PATH=/home/freire/pico-sdk -DPICO_BOARD=pico_w ..
```
4. Build the application using either make or CMake.
```
  cmake --build .
```
or
```
  make
```

## Application Structure

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
## Board Specifications
![pinout](resources/picow-pinout.svg)

## Contributing

Contributions to this repository are welcome! If you have an application you'd like to add or improvements to existing applications, please submit a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).