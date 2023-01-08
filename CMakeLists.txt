cmake_minimum_required(VERSION 3.25.1)

project(FractureMLDiagnosticApp C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)

set(POJECT_LIBS Widgets)

# add_subdirectory(third-party/pytorch-cpp)


add_executable(${PROJECT_NAME}
    src/main.cpp
)

target_link_libraries(${PROJECT_NAME} ${PROJECT_LIBS})
# install(TARGETS ${PROJECT_NAME})
