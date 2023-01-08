

cmake-make:
	cmake -G "Unix Makefiles" -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ ..

build-make: cmake-make
	cd build && make

run-make: build-make
	cd build && .\a.exe