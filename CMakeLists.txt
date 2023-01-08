cmake_minimum_required(VERSION 3.25.1)

project(FractureMLDiagnosticApp C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(QT_LIBS Widgets Core Gui)
find_package(Qt6 REQUIRED COMPONENTS ${QT_LIBS})
# qt_standard_project_setup()

set(POJECT_LIBS ${QT_LIBS})

# add_subdirectory(third-party/pytorch-cpp)

set(exec a)

add_executable(${exec}
    src/main.cpp
)

target_link_libraries(${exec} PRIVATE Qt6::Core Qt6::Gui Qt6::Widgets)
install(TARGETS ${exec})
